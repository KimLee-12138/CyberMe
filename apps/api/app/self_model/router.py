"""Self Model API — personal facts, inferences, style samples."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import get_db
from app.models.knowledge import KnowledgeEdge, KnowledgeNode
from app.models.user import User
from app.models.vault import VaultDocument

router = APIRouter(prefix="/api/v1")

# ── In-memory style samples ──────────────────────────────

_style_samples: list[dict] = []


class StyleSampleCreate(BaseModel):
    content: str = Field(..., max_length=2000)
    sample_type: str = Field(default="approved", pattern="^(approved|rejected)$")
    note: str | None = None


# ── Main endpoint ────────────────────────────────────────


@router.get("/self")
async def get_self_model(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Aggregate the user's digital twin profile."""

    # 1. Explicit facts: verification=explicit documents + self-fact nodes
    explicit_docs = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.verification == "explicit",
            VaultDocument.deleted_at.is_(None),
        )
        .limit(20)
    )
    explicit_docs_list = explicit_docs.scalars().all()

    self_fact_nodes = await db.execute(
        select(KnowledgeNode)
        .where(KnowledgeNode.node_type.in_(["self-fact", "inference"]))
        .limit(20)
    )
    self_fact_list = self_fact_nodes.scalars().all()

    facts = []
    for d in explicit_docs_list:
        facts.append({
            "id": d.id,
            "type": "explicit_document",
            "title": d.title,
            "course_code": d.course_code,
            "verification": d.verification,
            "path": d.relative_path,
        })
    for n in self_fact_list:
        facts.append({
            "id": n.id,
            "type": "knowledge_node",
            "label": n.label,
            "node_type": n.node_type,
            "properties": n.properties,
        })

    # 2. Pending inferences: ai_candidate edges
    candidate_edges = await db.execute(
        select(KnowledgeEdge)
        .where(KnowledgeEdge.origin == "ai_candidate")
        .limit(20)
    )
    edges = candidate_edges.scalars().all()

    inferences = []
    for e in edges:
        # Get source and target node labels
        src = await db.scalar(
            select(KnowledgeNode.label).where(KnowledgeNode.id == e.source_node_id)
        )
        tgt = await db.scalar(
            select(KnowledgeNode.label).where(KnowledgeNode.id == e.target_node_id)
        )
        inferences.append({
            "id": e.id,
            "source_label": src or "?",
            "target_label": tgt or "?",
            "edge_type": e.edge_type,
            "confidence": e.confidence,
            "evidence": e.evidence,
        })

    # 3. Style samples
    return {
        "facts": facts,
        "facts_count": len(facts),
        "inferences": inferences,
        "inferences_count": len(inferences),
        "style_samples": _style_samples,
    }


# ── Style samples CRUD ──────────────────────────────────


@router.post("/self/style-samples")
async def add_style_sample(
    body: StyleSampleCreate,
    user: User = Depends(current_user),
):
    s = {
        "id": str(uuid.uuid4()),
        "content": body.content,
        "sample_type": body.sample_type,
        "note": body.note,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _style_samples.append(s)
    return s


@router.delete("/self/style-samples/{sample_id}")
async def remove_style_sample(
    sample_id: str,
    user: User = Depends(current_user),
):
    global _style_samples
    _style_samples = [s for s in _style_samples if s["id"] != sample_id]
    return {"status": "deleted"}
