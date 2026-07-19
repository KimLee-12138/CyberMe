"""Retrieval — hybrid search engine."""

import json
import uuid
from typing import Any

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.knowledge import DocumentChunk, KnowledgeEdge, KnowledgeNode
from app.models.vault import VaultDocument

# Default fusion weights (from design doc 9.3)
FUSION_WEIGHTS = {
    "fts": 0.30,
    "vector": 0.35,
    "graph": 0.15,
    "metadata": 0.10,
    "source_quality": 0.10,
}


async def hybrid_search(
    db: AsyncSession,
    query: str,
    scope: dict[str, Any] | None = None,
    top_k: int = 20,
    weights: dict[str, float] | None = None,
) -> dict[str, Any]:
    """Execute hybrid search across all four retrieval paths.

    Args:
        db: Database session
        query: Natural language query
        scope: Intent scope (courses, projects, document_types, etc.)
        top_k: Number of results to return
        weights: Custom fusion weights

    Returns:
        Evidence bundle dict with items, conflicts, and coverage score
    """
    w = weights or FUSION_WEIGHTS
    scope = scope or {}

    results: dict[str, dict[str, Any]] = {}
    all_ids: set[str] = set()

    # ── Path 1: Full-Text Search ──────────────────────
    fts_results = await _fts_search(db, query, scope, top_k * 2)
    for item in fts_results:
        pid = f"doc_{item['document_id']}"
        results[pid] = item
        results[pid]["_fts_score"] = item.get("score", 0)
        all_ids.add(pid)

    # ── Path 2: Vector Search ─────────────────────────
    vector_results = await _vector_search(db, query, scope, top_k * 2)
    for item in vector_results:
        pid = f"doc_{item['document_id']}"
        if pid in results:
            results[pid]["_vec_score"] = item.get("score", 0)
            # Keep highest-scoring chunk
            if item.get("score", 0) > results[pid].get("_vec_score", 0):
                results[pid].update(item)
        else:
            results[pid] = item
            results[pid]["_vec_score"] = item.get("score", 0)
        all_ids.add(pid)

    # ── Path 3: Graph Expansion ──────────────────────
    graph_results = await _graph_expand(db, results, scope)
    for item in graph_results:
        pid = f"doc_{item['document_id']}"
        if pid in results:
            results[pid]["_graph_score"] = item.get("score", 0)
        else:
            results[pid] = item
            results[pid]["_graph_score"] = item.get("score", 0)
        all_ids.add(pid)

    # ── Path 4: Metadata Boost ───────────────────────
    for pid, item in results.items():
        item["_meta_score"] = _metadata_boost(item, scope)

    # ── Fusion Scoring ───────────────────────────────
    scored_items = []
    for pid, item in results.items():
        fts = item.get("_fts_score", 0)
        vec = item.get("_vec_score", 0)
        graph = item.get("_graph_score", 0)
        meta = item.get("_meta_score", 0)
        quality = _source_quality_score(item)

        final_score = (
            w["fts"] * fts
            + w["vector"] * vec
            + w["graph"] * graph
            + w["metadata"] * meta
            + w["source_quality"] * quality
        )

        scored_items.append({
            "evidence_id": f"ev_{uuid.uuid4().hex[:8]}",
            "document_id": item.get("document_id", ""),
            "path": item.get("path", ""),
            "heading": item.get("heading", ""),
            "line_range": item.get("line_range", []),
            "source": item.get("source", ""),
            "source_pages": item.get("source_pages", ""),
            "verification": item.get("verification", "inferred"),
            "content": item.get("content", ""),
            "score": round(final_score, 4),
        })

    # Sort by final score
    scored_items.sort(key=lambda x: x["score"], reverse=True)

    # Deduplicate by document_id (keep best)
    seen_docs = set()
    deduped = []
    for item in scored_items:
        if item["document_id"] not in seen_docs:
            deduped.append(item)
            seen_docs.add(item["document_id"])

    deduped = deduped[:top_k]

    # ── Enrich with more chunks from same document ───────
    deduped = await _enrich_with_context(db, deduped)

    # ── Detect conflicts ─────────────────────────────
    conflicts = _detect_conflicts(deduped)

    # ── Coverage estimate ────────────────────────────
    coverage = min(1.0, len(deduped) / max(1, top_k))

    return {
        "query": query,
        "scope": [f"{k}:{v}" for k, v in scope.items()],
        "items": deduped,
        "conflicts": conflicts,
        "coverage": round(coverage, 2),
    }


# ── Individual search paths ─────────────────────────────


def _split_query_terms(query: str) -> list[str]:
    """Split a query into searchable terms.

    For Chinese text, generates character bigrams for higher precision.
    For English/numbers, splits on whitespace.
    """
    terms = []
    # Split on whitespace first
    parts = query.split()
    for part in parts:
        if not part:
            continue
        # Detect if part has Chinese characters
        has_chinese = any('\u4e00' <= c <= '\u9fff' for c in part)
        if has_chinese and len(part) <= 1:
            terms.append(part)
        elif has_chinese and len(part) >= 2:
            # Generate character bigrams for better precision
            for i in range(len(part) - 1):
                terms.append(part[i:i+2])
            # Also include individual characters for single-char matches
            for c in part:
                if c not in terms:
                    terms.append(c)
        else:
            # English/numbers — use as-is
            terms.append(part)
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for t in terms:
        if t not in seen:
            seen.add(t)
            unique.append(t)
    # Also keep original query for phrase matching
    if len(query) >= 4:
        unique.append(query)
    return unique


async def _fts_search(
    db: AsyncSession, query: str, scope: dict, limit: int
) -> list[dict]:
    """Full-text search using multi-term OR matching on document chunks."""
    terms = _split_query_terms(query)

    if not terms:
        return []

    # Build OR conditions for each term
    base_conditions = ["vd.deleted_at IS NULL"]
    params: dict[str, Any] = {"limit": limit}

    if scope.get("courses"):
        courses_list = scope["courses"] if isinstance(scope["courses"], list) else [scope["courses"]]
        base_conditions.append("vd.course_code = ANY(:courses)")
        params["courses"] = courses_list

    # Build per-term subquery and sum score
    # Content match: 1 point per term
    # Title match: 5 points per term (much stronger signal)
    # Exact phrase match in title: 10 bonus points
    term_scores = []
    title_scores = []
    params["exact_q"] = f"%{query}%"
    for i, term in enumerate(terms):
        param_name = f"t{i}"
        params[param_name] = f"%{term}%"
        term_scores.append(f"(CASE WHEN dc.content ILIKE :{param_name} THEN 1 ELSE 0 END)")
        title_scores.append(f"(CASE WHEN vd.title ILIKE :{param_name} THEN 5 ELSE 0 END)")

    score_expr = " + ".join(term_scores) + " + " + " + ".join(title_scores)
    score_expr += " + (CASE WHEN vd.title ILIKE :exact_q THEN 10 ELSE 0 END)"
    score_expr += " + (CASE WHEN dc.content ILIKE :exact_q THEN 3 ELSE 0 END)"
    where_base = " AND ".join(base_conditions)

    # Build OR conditions: content OR title must match at least one term
    content_ors = " OR ".join(f"dc.content ILIKE :t{i}" for i in range(len(terms)))
    title_ors = " OR ".join(f"vd.title ILIKE :t{i}" for i in range(len(terms)))

    sql = f"""
        SELECT * FROM (
            SELECT DISTINCT ON (vd.id)
                   dc.document_id,
                   dc.heading_path,
                   dc.content,
                   dc.page_ref,
                   dc.chunk_metadata,
                   vd.relative_path,
                   vd.title,
                   ({score_expr}) AS match_score
            FROM document_chunks dc
            JOIN vault_documents vd ON vd.id = dc.document_id
            WHERE {where_base}
              AND ({content_ors} OR {title_ors})
            ORDER BY vd.id, match_score DESC
        ) AS ranked
        ORDER BY match_score DESC
        LIMIT :limit
    """

    result = await db.execute(text(sql), params)
    rows = result.fetchall()

    # Normalize: title match 5pt, content 1pt, exact 13pt max bonus
    max_score = len(terms) * 6 + 13

    results = []
    for row in rows:
        content_preview = (row.content or "")[:500]
        score = row.match_score / max_score if max_score > 0 else 0.1

        results.append({
            "document_id": row.document_id,
            "path": row.relative_path,
            "heading": " > ".join(row.heading_path) if row.heading_path else "",
            "content": content_preview,
            "source": row.chunk_metadata.get("source", "") if row.chunk_metadata else "",
            "source_pages": row.page_ref or "",
            "verification": row.chunk_metadata.get("verification", "inferred") if row.chunk_metadata else "inferred",
            "score": round(score, 4),
        })

    return results


async def _vector_search(
    db: AsyncSession, query: str, scope: dict, limit: int
) -> list[dict]:
    """Vector similarity search using pgvector.

    Falls back gracefully to FTS if no embeddings exist or embedding API unavailable.
    """
    try:
        # Try to generate embedding
        embedding = await _get_embedding(query)
        if embedding is None:
            return []

        conditions = [
            "dc.embedding IS NOT NULL",
            "vd.deleted_at IS NULL",
        ]
        extra_params: dict[str, Any] = {"limit": limit}

        if scope.get("courses"):
            courses = scope["courses"] if isinstance(scope["courses"], list) else [scope["courses"]]
            conditions.append("vd.course_code = ANY(:courses)")
            extra_params["courses"] = courses

        where_clause = " AND ".join(conditions)

        # Build the vector query
        embedding_literal = "[" + ",".join(str(v) for v in embedding) + "]"

        sql = text(f"""
            SELECT dc.id, dc.document_id, dc.heading_path, dc.content, dc.page_ref,
                   dc.chunk_metadata, vd.relative_path, vd.title,
                   1 - (dc.embedding <=> :embedding) AS similarity
            FROM document_chunks dc
            JOIN vault_documents vd ON vd.id = dc.document_id
            WHERE {where_clause}
            ORDER BY dc.embedding <=> :embedding
            LIMIT :limit
        """)

        result = await db.execute(
            sql,
            {**extra_params, "embedding": embedding},
        )
        rows = result.fetchall()

        results = []
        for row in rows:
            results.append({
                "document_id": row.document_id,
                "path": row.relative_path,
                "heading": " > ".join(row.heading_path) if row.heading_path else "",
                "content": (row.content or "")[:500],
                "source": row.chunk_metadata.get("source", "") if row.chunk_metadata else "",
                "source_pages": row.page_ref or "",
                "verification": row.chunk_metadata.get("verification", "inferred") if row.chunk_metadata else "inferred",
                "score": round(float(row.similarity), 4),
            })
        return results

    except Exception:
        # Vector search unavailable — silently fall back to other paths
        return []


async def _get_embedding(text: str) -> list[float] | None:
    """Get embedding vector for text via OpenAI API."""
    import httpx

    if not settings.openai_api_key:
        return None

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://api.openai.com/v1/embeddings",
                headers={
                    "Authorization": f"Bearer {settings.openai_api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "text-embedding-3-small",
                    "input": text[:8000],
                },
            )
            if resp.status_code == 200:
                data = resp.json()
                return data["data"][0]["embedding"]
            return None
    except Exception:
        return None


async def _graph_expand(
    db: AsyncSession, current_results: dict, scope: dict
) -> list[dict]:
    """Expand search via knowledge graph — follow edges from high-scoring nodes."""
    if not current_results:
        return []

    # Get document IDs from top results
    top_doc_ids = [
        item["document_id"]
        for item in sorted(
            current_results.values(),
            key=lambda x: max(
                x.get("_fts_score", 0), x.get("_vec_score", 0)
            ),
            reverse=True,
        )[:5]
    ]

    # Find their knowledge nodes
    node_result = await db.execute(
        select(KnowledgeNode).where(KnowledgeNode.document_id.in_(top_doc_ids))
    )
    nodes = node_result.scalars().all()
    node_ids = [n.id for n in nodes]

    if not node_ids:
        return []

    # Get edges (1-hop neighborhood)
    edge_result = await db.execute(
        select(KnowledgeEdge).where(
            (KnowledgeEdge.source_node_id.in_(node_ids))
            | (KnowledgeEdge.target_node_id.in_(node_ids))
        ).limit(50)
    )
    edges = edge_result.scalars().all()

    # Collect neighbor node IDs
    neighbor_ids = set()
    for e in edges:
        if e.source_node_id in node_ids:
            neighbor_ids.add(e.target_node_id)
        else:
            neighbor_ids.add(e.source_node_id)
    neighbor_ids -= set(node_ids)

    if not neighbor_ids:
        return []

    # Fetch neighbor nodes and their documents
    neighbor_nodes = await db.execute(
        select(KnowledgeNode).where(KnowledgeNode.id.in_(list(neighbor_ids)))
    )
    neighbor_map = {n.id: n for n in neighbor_nodes.scalars().all()}

    # Get their documents
    doc_ids = [
        n.document_id
        for n in neighbor_map.values()
        if n.document_id
    ]
    if not doc_ids:
        return []

    docs_result = await db.execute(
        select(VaultDocument).where(
            VaultDocument.id.in_(doc_ids),
            VaultDocument.deleted_at.is_(None),
        )
    )
    docs = {d.id: d for d in docs_result.scalars().all()}

    results = []
    for node in neighbor_map.values():
        if not node.document_id or node.document_id not in docs:
            continue
        doc = docs[node.document_id]
        results.append({
            "document_id": doc.id,
            "path": doc.relative_path,
            "heading": node.label,
            "content": (doc.markdown_body or "")[:500],
            "source": node.properties.get("source", ""),
            "source_pages": "",
            "verification": node.properties.get("verification", "inferred"),
            "score": 0.3,  # Lower base score for graph-expanded items
        })

    return results


def _metadata_boost(item: dict, scope: dict) -> float:
    """Boost score based on metadata match with scope."""
    score = 0.0

    # Exact course match
    if scope.get("courses"):
        item_course = item.get("path", "").split("/")[0] if item.get("path") else ""
        if item_course in (
            scope["courses"] if isinstance(scope["courses"], list) else [scope["courses"]]
        ):
            score += 0.3

    # High-quality verification
    if item.get("verification") == "explicit":
        score += 0.2

    # Has source pages (more credible)
    if item.get("source_pages"):
        score += 0.1

    return min(score, 1.0)


def _source_quality_score(item: dict) -> float:
    """Score based on source quality indicators."""
    score = 0.0

    verification = item.get("verification", "inferred")
    if verification == "explicit":
        score += 0.5
    elif verification == "derived":
        score += 0.3

    if item.get("source"):
        score += 0.2
    if item.get("source_pages"):
        score += 0.2

    return min(score, 1.0)


async def _enrich_with_context(
    db: AsyncSession, items: list[dict]
) -> list[dict]:
    """For each evidence item, fetch more chunks from the same document.

    Without this, the model only sees one small chunk and may miss the full
    explanation that exists in nearby chunks of the same document.
    """
    if not items:
        return items

    doc_ids = list({item["document_id"] for item in items if item.get("document_id")})
    if not doc_ids:
        return items

    # Fetch all chunks for these documents, ordered by ordinal
    result = await db.execute(
        select(DocumentChunk)
        .where(DocumentChunk.document_id.in_(doc_ids))
        .order_by(DocumentChunk.document_id, DocumentChunk.ordinal)
    )
    all_chunks = result.scalars().all()

    # Group chunks by document_id
    doc_chunks: dict[str, list[DocumentChunk]] = {}
    for c in all_chunks:
        doc_chunks.setdefault(c.document_id, []).append(c)

    # Enrich each item with full document context
    for item in items:
        did = item.get("document_id", "")
        chunks = doc_chunks.get(did, [])
        if len(chunks) <= 1:
            continue

        # Find the matched chunk's ordinal
        matched_heading = item.get("heading", "")
        matched_ordinal = -1
        for c in chunks:
            heading_str = " > ".join(c.heading_path) if c.heading_path else ""
            if heading_str == matched_heading:
                matched_ordinal = c.ordinal
                break

        if matched_ordinal < 0:
            # Fallback: just concatenate all chunks
            full_text = "\n\n".join(c.content for c in chunks)
            item["content"] = full_text[:3000]
            continue

        # Include chunks around the matched one
        # Take chunks within +/- 2 range of the matched ordinal
        context_chunks = [
            c for c in chunks
            if abs(c.ordinal - matched_ordinal) <= 2
        ]
        context_chunks.sort(key=lambda c: c.ordinal)

        full_text = "\n\n".join(c.content for c in context_chunks)
        item["content"] = full_text[:3000]

    return items


def _detect_conflicts(items: list[dict]) -> list[dict]:
    """Detect contradictory statements between evidence items.

    Simple heuristic: items from different courses with similar headings
    """
    conflicts = []
    headings = {}
    for item in items:
        heading = item.get("heading", "")
        if heading:
            if heading in headings:
                conflicts.append({
                    "evidence_a": headings[heading]["evidence_id"],
                    "evidence_b": item["evidence_id"],
                    "topic": heading,
                })
            else:
                headings[heading] = item
    return conflicts
