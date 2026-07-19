"""Knowledge API routes — courses, documents, search, graph."""

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field
from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import get_db
from app.models.knowledge import Course, DocumentChunk, KnowledgeEdge, KnowledgeNode
from app.models.user import User
from app.models.vault import DocumentVersion, VaultDocument

router = APIRouter(prefix="/api/v1")


# ── Courses ───────────────────────────────────────────


@router.get("/courses")
async def list_courses(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """List all courses with stats."""
    result = await db.execute(
        select(Course).order_by(Course.code)
    )
    courses = result.scalars().all()
    return {
        "courses": [
            {
                "id": c.id,
                "code": c.code,
                "name": c.name,
                "knowledge_count": c.knowledge_count,
                "extract_count": c.extract_count,
                "last_indexed_at": c.last_indexed_at.isoformat() if c.last_indexed_at else None,
            }
            for c in courses
        ]
    }


@router.get("/courses/{course_id}")
async def get_course(
    course_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Get a single course with its documents."""
    result = await db.execute(select(Course).where(Course.id == course_id))
    course = result.scalar_one_or_none()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Get documents for this course
    docs = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.course_code == course.code,
            VaultDocument.deleted_at.is_(None),
        )
        .order_by(VaultDocument.document_type, VaultDocument.title)
    )
    documents = docs.scalars().all()

    return {
        "id": course.id,
        "code": course.code,
        "name": course.name,
        "knowledge_count": course.knowledge_count,
        "documents": [
            {
                "id": d.id,
                "title": d.title,
                "relative_path": d.relative_path,
                "document_type": d.document_type,
                "status": d.status,
                "mastery": d.mastery,
                "importance": d.importance,
            }
            for d in documents
        ],
    }


# ── Documents ─────────────────────────────────────────


@router.get("/documents/{document_id}")
async def get_document(
    document_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Get a document with full content and metadata."""
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == document_id)
    )
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # Get graph node for relationships
    node_result = await db.execute(
        select(KnowledgeNode).where(KnowledgeNode.document_id == document_id)
    )
    node = node_result.scalar_one_or_none()

    # Get edges
    edges = []
    if node:
        edge_result = await db.execute(
            select(KnowledgeEdge).where(
                (KnowledgeEdge.source_node_id == node.id)
                | (KnowledgeEdge.target_node_id == node.id)
            ).limit(50)
        )
        for e in edge_result.scalars().all():
            # Get target node label
            target_id = (
                e.target_node_id
                if e.source_node_id == node.id
                else e.source_node_id
            )
            target_node = await db.execute(
                select(KnowledgeNode).where(KnowledgeNode.id == target_id)
            )
            target = target_node.scalar_one_or_none()
            edges.append({
                "edge_type": e.edge_type,
                "origin": e.origin,
                "target_label": target.label if target else "?",
                "target_node_id": target_id,
            })

    return {
        "id": doc.id,
        "title": doc.title,
        "relative_path": doc.relative_path,
        "document_type": doc.document_type,
        "course_code": doc.course_code,
        "status": doc.status,
        "mastery": doc.mastery,
        "importance": doc.importance,
        "needs_review": doc.needs_review,
        "frontmatter": doc.frontmatter,
        "markdown_body": doc.markdown_body,
        "content_hash": doc.content_hash,
        "indexed_at": doc.indexed_at.isoformat() if doc.indexed_at else None,
        "edges": edges,
    }


# ── Search ────────────────────────────────────────────


@router.get("/search")
async def search_documents(
    q: str = Query(..., min_length=1),
    course_code: str | None = None,
    document_type: str | None = None,
    limit: int = Query(default=20, le=100),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Full-text search across Vault documents."""
    # Simple LIKE search (upgrade to TSVECTOR when FTS is configured)
    conditions = [VaultDocument.deleted_at.is_(None)]
    if course_code:
        conditions.append(VaultDocument.course_code == course_code)
    if document_type:
        conditions.append(VaultDocument.document_type == document_type)

    # Search in title and body
    search_term = f"%{q}%"
    query = (
        select(VaultDocument)
        .where(
            *conditions,
            (VaultDocument.title.ilike(search_term))
            | (VaultDocument.markdown_body.ilike(search_term)),
        )
        .order_by(VaultDocument.title)
        .limit(limit)
    )

    result = await db.execute(query)
    docs = result.scalars().all()

    return {
        "query": q,
        "results": [
            {
                "id": d.id,
                "title": d.title,
                "relative_path": d.relative_path,
                "document_type": d.document_type,
                "course_code": d.course_code,
                "status": d.status,
                "mastery": d.mastery,
                "snippet": (d.markdown_body or "")[:200] if d.markdown_body else "",
            }
            for d in docs
        ],
        "total": len(docs),
    }


# ── Graph ─────────────────────────────────────────────


@router.get("/graph")
async def get_graph(
    node_type: str | None = None,
    course_code: str | None = None,
    limit: int = Query(default=200, le=1000),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Get the knowledge graph (nodes + edges)."""
    # Filter nodes
    node_query = select(KnowledgeNode)
    if node_type:
        node_query = node_query.where(KnowledgeNode.node_type == node_type)
    if course_code:
        node_query = node_query.where(
            KnowledgeNode.properties["course_code"].as_string() == course_code
        )
    node_query = node_query.limit(limit)

    nodes_result = await db.execute(node_query)
    nodes = nodes_result.scalars().all()

    # Get edges for these nodes
    node_ids = [n.id for n in nodes]
    edges = []
    if node_ids:
        edge_result = await db.execute(
            select(KnowledgeEdge).where(
                KnowledgeEdge.source_node_id.in_(node_ids)
                | KnowledgeEdge.target_node_id.in_(node_ids)
            ).limit(limit * 3)
        )
        for e in edge_result.scalars().all():
            edges.append({
                "id": e.id,
                "source": e.source_node_id,
                "target": e.target_node_id,
                "edge_type": e.edge_type,
                "origin": e.origin,
                "confidence": e.confidence,
            })

    return {
        "nodes": [
            {
                "id": n.id,
                "node_type": n.node_type,
                "label": n.label,
                "document_id": n.document_id,
                "properties": n.properties,
            }
            for n in nodes
        ],
        "edges": edges,
    }


@router.get("/graph/neighborhood/{node_id}")
async def get_neighborhood(
    node_id: str,
    depth: int = Query(default=1, ge=1, le=3),
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Get a node and its neighborhood up to `depth` hops."""
    node_result = await db.execute(
        select(KnowledgeNode).where(KnowledgeNode.id == node_id)
    )
    node = node_result.scalar_one_or_none()
    if not node:
        raise HTTPException(status_code=404, detail="Node not found")

    # Collect edges recursively
    visited = {node_id}
    all_nodes = {node_id: node}
    all_edges = []

    frontier = {node_id}
    for _ in range(depth):
        if not frontier:
            break
        edges_result = await db.execute(
            select(KnowledgeEdge).where(
                KnowledgeEdge.source_node_id.in_(list(frontier))
                | KnowledgeEdge.target_node_id.in_(list(frontier))
            )
        )
        new_frontier = set()
        for e in edges_result.scalars().all():
            all_edges.append({
                "id": e.id,
                "source": e.source_node_id,
                "target": e.target_node_id,
                "edge_type": e.edge_type,
                "origin": e.origin,
            })
            for nid in (e.source_node_id, e.target_node_id):
                if nid not in visited:
                    visited.add(nid)
                    new_frontier.add(nid)
        frontier = new_frontier

        # Fetch new nodes
        if frontier:
            batch = await db.execute(
                select(KnowledgeNode).where(
                    KnowledgeNode.id.in_(list(frontier))
                )
            )
            for n in batch.scalars().all():
                all_nodes[n.id] = n

    return {
        "center": {
            "id": node.id,
            "node_type": node.node_type,
            "label": node.label,
        },
        "nodes": [
            {"id": n.id, "node_type": n.node_type, "label": n.label}
            for n in all_nodes.values()
        ],
        "edges": all_edges,
    }


@router.get("/graph/orphans")
async def get_orphans(
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Find nodes with no edges (orphans)."""
    result = await db.execute(
        select(KnowledgeNode).where(
            ~KnowledgeNode.id.in_(
                select(KnowledgeEdge.source_node_id).union(
                    select(KnowledgeEdge.target_node_id)
                )
            )
        ).limit(100)
    )
    orphans = result.scalars().all()
    return {
        "orphans": [
            {"id": n.id, "node_type": n.node_type, "label": n.label}
            for n in orphans
        ],
        "total": len(orphans),
    }


# ── Document metadata update ────────────────────────────


class UpdateDocumentRequest(BaseModel):
    status: str | None = Field(default=None, max_length=50)
    mastery: str | None = Field(default=None, max_length=50)
    importance: str | None = Field(default=None, max_length=20)


@router.patch("/documents/{document_id}")
async def update_document_metadata(
    document_id: str,
    body: UpdateDocumentRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Update document metadata (status, mastery, importance)."""
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == document_id)
    )
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    if body.status is not None:
        doc.status = body.status
    if body.mastery is not None:
        doc.mastery = body.mastery
    if body.importance is not None:
        doc.importance = body.importance

    await db.commit()
    return {
        "id": doc.id,
        "status": doc.status,
        "mastery": doc.mastery,
        "importance": doc.importance,
    }


# ── Document version history ────────────────────────────


@router.get("/documents/{document_id}/versions")
async def get_document_versions(
    document_id: str,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """List version history for a document."""
    result = await db.execute(
        select(DocumentVersion)
        .where(DocumentVersion.document_id == document_id)
        .order_by(DocumentVersion.created_at.desc())
        .limit(20)
    )
    versions = result.scalars().all()
    return {
        "versions": [
            {
                "id": v.id,
                "content_hash": v.content_hash,
                "created_at": v.created_at.isoformat() if v.created_at else None,
                "source_device_id": v.source_device_id,
            }
            for v in versions
        ]
    }


# ── WikiLink resolution ─────────────────────────────────


class ResolveWikiLinkRequest(BaseModel):
    wikilink: str = Field(..., min_length=1, max_length=200)


@router.post("/documents/resolve-wikilink")
async def resolve_wikilink(
    body: ResolveWikiLinkRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Resolve a WikiLink [[target]] to a document ID."""
    # Clean the link: remove alias part after | and anchor after #
    target = body.wikilink.split("|")[0].split("#")[0].strip()

    if not target:
        raise HTTPException(status_code=400, detail="Empty wikilink target")

    # Search by exact title first, then by relative_path
    result = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.deleted_at.is_(None),
            VaultDocument.title.ilike(target),
        )
        .limit(1)
    )
    doc = result.scalar_one_or_none()

    if not doc:
        # Fuzzy: search by relative_path containing the target
        result = await db.execute(
            select(VaultDocument)
            .where(
                VaultDocument.deleted_at.is_(None),
                VaultDocument.relative_path.ilike(f"%{target}%"),
            )
            .limit(1)
        )
        doc = result.scalar_one_or_none()

    if not doc:
        # As last resort: title contains target
        result = await db.execute(
            select(VaultDocument)
            .where(
                VaultDocument.deleted_at.is_(None),
                VaultDocument.title.ilike(f"%{target}%"),
            )
            .limit(1)
        )
        doc = result.scalar_one_or_none()

    if not doc:
        raise HTTPException(status_code=404, detail=f"WikiLink target not found: {target}")

    return {
        "document_id": doc.id,
        "title": doc.title,
        "path": doc.relative_path,
    }
