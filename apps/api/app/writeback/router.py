"""Writeback API — proposals, approval, validation, application."""

import re
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import get_db
from app.models.user import User
from app.models.vault import VaultDocument

router = APIRouter(prefix="/api/v1")

# ── State machine ────────────────────────────────────────

STATES = ["draft", "validating", "ready", "approved", "rejected", "applied"]
TRANSITIONS = {
    "draft": ["validating"],
    "validating": ["ready", "rejected"],
    "ready": ["approved", "rejected"],
    "approved": ["applied", "rejected"],
    "applied": [],
    "rejected": [],
}

# ── In-memory storage ────────────────────────────────────

_proposals: dict[str, dict] = {}


# ── Schemas ──────────────────────────────────────────────

class ProposalCreate(BaseModel):
    document_id: str
    new_content: str
    reason: str = ""


class ProposalUpdate(BaseModel):
    new_content: str | None = None
    reason: str | None = None


# ── Validation ───────────────────────────────────────────

def validate_patch(content: str, path: str) -> tuple[bool, str]:
    """Security checks on proposed content before writing."""
    if not content:
        return False, "内容不能为空"
    if len(content) > 500_000:
        return False, "内容超过 500KB 限制"
    if "\x00" in content:
        return False, "内容包含非法字符 (NULL byte)"
    # Check path safety (when applied to filesystem)
    if path.startswith("/") or path.startswith("\\"):
        return False, "禁止绝对路径"
    if ".." in path:
        return False, "禁止路径穿越"
    return True, "ok"


# ── CRUD ─────────────────────────────────────────────────


@router.get("/writebacks")
async def list_proposals(user: User = Depends(current_user)):
    return {"proposals": list(_proposals.values())}


@router.post("/writebacks")
async def create_proposal(
    body: ProposalCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    # Verify document exists
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == body.document_id)
    )
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    # Validate
    ok, msg = validate_patch(body.new_content, doc.relative_path)
    if not ok:
        raise HTTPException(status_code=400, detail=msg)

    pid = str(uuid.uuid4())
    p = {
        "id": pid,
        "document_id": body.document_id,
        "document_title": doc.title,
        "document_path": doc.relative_path,
        "old_content": doc.markdown_body or "",
        "new_content": body.new_content,
        "reason": body.reason,
        "status": "draft",
        "created_by": user.username,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _proposals[pid] = p
    return p


@router.get("/writebacks/{proposal_id}")
async def get_proposal(
    proposal_id: str,
    user: User = Depends(current_user),
):
    p = _proposals.get(proposal_id)
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")

    # Generate simple diff
    old_lines = p["old_content"].split("\n")
    new_lines = p["new_content"].split("\n")

    # Simple line diff
    diff = []
    max_len = max(len(old_lines), len(new_lines))
    for i in range(max_len):
        old_line = old_lines[i] if i < len(old_lines) else None
        new_line = new_lines[i] if i < len(new_lines) else None
        if old_line != new_line:
            if old_line and new_line:
                diff.append({"type": "changed", "line": i + 1, "old": old_line[:120], "new": new_line[:120]})
            elif new_line:
                diff.append({"type": "added", "line": i + 1, "new": new_line[:120]})
            elif old_line:
                diff.append({"type": "removed", "line": i + 1, "old": old_line[:120]})

    return {**p, "diff": diff[:50]}


# ── Approval ─────────────────────────────────────────────


@router.post("/writebacks/{proposal_id}/approve")
async def approve_proposal(
    proposal_id: str,
    user: User = Depends(current_user),
):
    p = _proposals.get(proposal_id)
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")
    if p["status"] not in ("ready", "draft", "validating"):
        raise HTTPException(status_code=400, detail=f"Cannot approve from status: {p['status']}")

    p["status"] = "approved"
    p["approved_by"] = user.username
    p["updated_at"] = datetime.now(timezone.utc).isoformat()
    return p


@router.post("/writebacks/{proposal_id}/reject")
async def reject_proposal(
    proposal_id: str,
    user: User = Depends(current_user),
):
    p = _proposals.get(proposal_id)
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")
    p["status"] = "rejected"
    p["updated_at"] = datetime.now(timezone.utc).isoformat()
    return p


# ── Apply ────────────────────────────────────────────────


@router.post("/writebacks/{proposal_id}/apply")
async def apply_proposal(
    proposal_id: str,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    p = _proposals.get(proposal_id)
    if not p:
        raise HTTPException(status_code=404, detail="Proposal not found")
    if p["status"] != "approved":
        raise HTTPException(status_code=400, detail="Must approve before applying")

    # Apply: update vault_document content
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == p["document_id"])
    )
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document no longer exists")

    doc.markdown_body = p["new_content"]
    await db.commit()

    p["status"] = "applied"
    p["applied_by"] = user.username
    p["updated_at"] = datetime.now(timezone.utc).isoformat()

    return {
        **p,
        "message": f"已应用提案到 {doc.relative_path}。本地同步代理将在下次同步时拉取此更改。",
    }


# ── Generate proposal from AI suggestion ─────────────────


class GenerateProposalRequest(BaseModel):
    document_id: str
    instruction: str = Field(..., max_length=500)


@router.post("/writebacks/generate")
async def generate_proposal(
    body: GenerateProposalRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Generate an improvement proposal for a document using AI."""
    result = await db.execute(
        select(VaultDocument).where(VaultDocument.id == body.document_id)
    )
    doc = result.scalar_one_or_none()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    from app.model_gateway.gateway import generate as gateway_generate
    from app.model_gateway.schemas import ModelMessage

    messages = [
        ModelMessage(role="system", content=(
            "你是一位知识编辑助手。根据用户的指令，改进以下文档的内容。"
            "保持原有结构和格式（Markdown + YAML frontmatter）。"
            "只输出改进后的完整文档内容。"
        )),
        ModelMessage(role="user", content=(
            f"文档路径: {doc.relative_path}\n"
            f"指令: {body.instruction}\n\n"
            f"原始内容:\n{doc.markdown_body}"
        )),
    ]

    try:
        response = await gateway_generate("evidence_qa.default", messages)
        new_content = response.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {e}")

    # Auto-create proposal
    pid = str(uuid.uuid4())
    p = {
        "id": pid,
        "document_id": body.document_id,
        "document_title": doc.title,
        "document_path": doc.relative_path,
        "old_content": doc.markdown_body or "",
        "new_content": new_content,
        "reason": f"AI生成: {body.instruction}",
        "status": "ready",
        "created_by": user.username,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    _proposals[pid] = p

    # Generate diff
    old_lines = p["old_content"].split("\n")
    new_lines = p["new_content"].split("\n")
    diff = []
    max_len = max(len(old_lines), len(new_lines))
    for i in range(max_len):
        old_line = old_lines[i] if i < len(old_lines) else None
        new_line = new_lines[i] if i < len(new_lines) else None
        if old_line != new_line:
            if old_line and new_line:
                diff.append({"type": "changed", "line": i + 1, "old": old_line[:120], "new": new_line[:120]})
            elif new_line:
                diff.append({"type": "added", "line": i + 1, "new": new_line[:120]})
            elif old_line:
                diff.append({"type": "removed", "line": i + 1, "old": old_line[:120]})

    return {**p, "diff": diff[:50]}
