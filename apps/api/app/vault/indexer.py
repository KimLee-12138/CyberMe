"""Vault document indexer — orchestrates chunking, FTS, and graph building."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.knowledge import Course, DocumentChunk, KnowledgeEdge, KnowledgeNode
from app.models.vault import VaultDocument
from app.vault.chunker import chunk_document
from app.vault.parser import parse_markdown


async def index_document(
    db: AsyncSession,
    document_id: str,
) -> dict:
    """Index a single document: parse, chunk, store.

    Returns summary dict with chunk_count, node_count, edge_count.
    """
    # Load document
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == document_id)
    )
    doc = result.scalar_one_or_none()
    if not doc or not doc.markdown_body:
        return {"error": "Document not found or empty"}

    # Parse
    parsed = parse_markdown(
        content=doc.markdown_body,
        relative_path=doc.relative_path,
        vault_id=doc.vault_id,
        modified_at=doc.modified_at_local,
    )

    # Update document metadata from parsed YAML
    doc.title = parsed.title
    doc.document_type = parsed.document_type
    doc.course_code = parsed.course_code
    doc.status = parsed.status
    doc.mastery = parsed.mastery
    doc.importance = parsed.importance
    doc.verification = parsed.source_info.verification
    doc.needs_review = parsed.needs_review
    doc.frontmatter = _sanitize_json(parsed.frontmatter)
    doc.indexed_at = datetime.now(timezone.utc)

    # ── Chunking ──────────────────────────────────────
    # Delete old chunks
    await db.execute(
        delete(DocumentChunk).where(DocumentChunk.document_id == document_id)
    )

    chunks = chunk_document(parsed.markdown_body, [parsed.title or ""])
    for c in chunks:
        chunk = DocumentChunk(
            id=str(uuid.uuid4()),
            document_id=document_id,
            heading_path=c["heading_path"],
            ordinal=c["ordinal"],
            content=c["content"],
            token_count=c["token_count"],
            content_hash=c["content_hash"],
            chunk_metadata={
                "source": parsed.source_info.source,
                "verification": parsed.source_info.verification,
                "course_code": parsed.course_code,
            },
        )
        db.add(chunk)

    # ── Knowledge Graph ───────────────────────────────
    node_count, edge_count = await _build_graph(db, doc, parsed)

    await db.flush()

    return {
        "chunk_count": len(chunks),
        "node_count": node_count,
        "edge_count": edge_count,
    }


async def _build_graph(
    db: AsyncSession, doc: VaultDocument, parsed
) -> tuple[int, int]:
    """Build knowledge graph nodes and edges from a parsed document."""
    node_count = 0
    edge_count = 0

    # ── Create/update node for this document ─────────
    node_type = _map_node_type(parsed.document_type)
    node_id = str(uuid.uuid4())

    # Check for existing node
    existing = await db.execute(
        select(KnowledgeNode).where(
            KnowledgeNode.document_id == doc.id,
        )
    )
    existing_node = existing.scalar_one_or_none()

    if existing_node:
        node_id = existing_node.id
        existing_node.label = parsed.title or doc.relative_path
        existing_node.node_type = node_type
        existing_node.properties = {
            "course_code": parsed.course_code,
            "status": parsed.status,
            "mastery": parsed.mastery,
            "importance": parsed.importance,
            "path": doc.relative_path,
        }
    else:
        node = KnowledgeNode(
            id=node_id,
            node_type=node_type,
            document_id=doc.id,
            label=parsed.title or doc.relative_path,
            properties={
                "course_code": parsed.course_code,
                "status": parsed.status,
                "mastery": parsed.mastery,
                "importance": parsed.importance,
                "path": doc.relative_path,
            },
        )
        db.add(node)
        node_count += 1

    # ── belongs_to edge (document → course MOC) ──────
    if parsed.course_code:
        course_node = await _ensure_course_node(db, parsed.course_code)
        if course_node and node_id != course_node:
            edge_count += await _add_edge(
                db, node_id, course_node, "belongs_to", "vault"
            )

    # ── WikiLink edges ────────────────────────────────
    for wl in parsed.wikilinks:
        target = wl.target if hasattr(wl, 'target') else wl['target']
        target_doc = await db.execute(
            select(VaultDocument).where(
                VaultDocument.relative_path.like(f"%{target}%"),
                VaultDocument.deleted_at.is_(None),
            )
        )
        target_doc = target_doc.scalar_one_or_none()
        if target_doc:
            target_node = await db.execute(
                select(KnowledgeNode).where(
                    KnowledgeNode.document_id == target_doc.id
                )
            )
            target_node = target_node.scalar_one_or_none()
            if target_node and target_node.id != node_id:
                edge_count += await _add_edge(
                    db, node_id, target_node.id, "related_to", "vault"
                )

    # ── Course auto-registration ──────────────────────
    if parsed.course_code and parsed.document_type in ("concept", "moc"):
        await _ensure_course(db, parsed.course_code, doc)

    return node_count, edge_count


async def _ensure_course_node(db: AsyncSession, course_code: str) -> str | None:
    """Get or create a course MOC node."""
    result = await db.execute(
        select(KnowledgeNode).where(
            KnowledgeNode.external_key == course_code,
            KnowledgeNode.node_type == "course-moc",
        )
    )
    node = result.scalar_one_or_none()
    if node:
        return node.id

    # Check if we have a MOC document for this course
    moc_doc = await db.execute(
        select(VaultDocument).where(
            VaultDocument.course_code == course_code,
            VaultDocument.document_type == "moc",
            VaultDocument.deleted_at.is_(None),
        )
    )
    moc_doc = moc_doc.scalar_one_or_none()

    node_id = str(uuid.uuid4())
    node = KnowledgeNode(
        id=node_id,
        node_type="course-moc",
        external_key=course_code,
        document_id=moc_doc.id if moc_doc else None,
        label=f"{course_code} — 课程MOC",
    )
    db.add(node)
    return node_id


async def _ensure_course(db, course_code: str, doc: VaultDocument) -> None:
    """Ensure a Course record exists."""
    result = await db.execute(
        select(Course).where(Course.code == course_code)
    )
    course = result.scalar_one_or_none()
    if course:
        course.knowledge_count = (course.knowledge_count or 0) + 1
        course.last_indexed_at = datetime.now(timezone.utc)
    else:
        course = Course(
            id=str(uuid.uuid4()),
            code=course_code,
            name=f"{course_code} — 待命名",
            knowledge_count=1,
            last_indexed_at=datetime.now(timezone.utc),
        )
        db.add(course)


async def _add_edge(
    db: AsyncSession,
    source: str,
    target: str,
    edge_type: str,
    origin: str = "derived",
) -> int:
    """Add an edge if it doesn't already exist. Returns 1 if added, 0 if exists."""
    existing = await db.execute(
        select(KnowledgeEdge).where(
            KnowledgeEdge.source_node_id == source,
            KnowledgeEdge.target_node_id == target,
            KnowledgeEdge.edge_type == edge_type,
        )
    )
    if existing.scalar_one_or_none():
        return 0

    edge = KnowledgeEdge(
        id=str(uuid.uuid4()),
        source_node_id=source,
        target_node_id=target,
        edge_type=edge_type,
        origin=origin,
    )
    db.add(edge)
    return 1


def _sanitize_json(obj):
    """Convert non-JSON-serializable objects (dates, etc.) to strings."""
    from datetime import date, datetime
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: _sanitize_json(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_sanitize_json(v) for v in obj]
    return obj


def _map_node_type(doc_type: str | None) -> str:
    """Map document type to knowledge node type."""
    mapping = {
        "moc": "course-moc",
        "concept": "concept",
        "formula": "formula",
        "example": "example",
        "mistake": "mistake",
        "extract": "extract",
        "source": "source",
        "project": "project",
        "self": "self-fact",
    }
    return mapping.get(doc_type or "", "concept")
