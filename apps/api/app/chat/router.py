"""Chat API routes — conversations, messages, SSE streaming."""

import asyncio
import json as json_mod
import re
import uuid
from datetime import datetime, timezone
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user, optional_user
from app.chat.engine import ask, ask_stream
from app.core.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/v1")


# ── Request / Response schemas ─────────────────────────


class CreateConversationRequest(BaseModel):
    title: str | None = None


class SendMessageRequest(BaseModel):
    content: str
    mode: str = Field(default="normal", pattern="^(normal|evidence_only|deep_research|dual_model)$")
    scope: dict[str, Any] | None = None  # {"courses": [...], "projects": [...]}


class MessageResponse(BaseModel):
    id: str
    role: str
    content: str
    citations: list[dict] | None = None
    created_at: str


class ConversationResponse(BaseModel):
    id: str
    title: str
    created_at: str
    updated_at: str


# ── In-memory storage (replace with DB models when steps 4.4 tables added) ──

_conversations: dict[str, dict] = {}
_messages: dict[str, list[dict]] = {}


# ── Conversation Endpoints ─────────────────────────────


@router.post("/conversations")
async def create_conversation(
    body: CreateConversationRequest,
    user: User = Depends(current_user),
):
    """Create a new conversation."""
    conv_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()
    conv = {
        "id": conv_id,
        "user_id": user.id,
        "title": body.title or "新的对话",
        "created_at": now,
        "updated_at": now,
    }
    _conversations[conv_id] = conv
    _messages[conv_id] = []
    return conv


@router.get("/conversations")
async def list_conversations(
    user: User = Depends(current_user),
):
    """List all conversations for the current user."""
    user_convs = [
        c for c in _conversations.values() if c["user_id"] == user.id
    ]
    user_convs.sort(key=lambda c: c["updated_at"], reverse=True)
    return {"conversations": user_convs}


@router.get("/conversations/{conv_id}")
async def get_conversation(
    conv_id: str,
    user: User = Depends(current_user),
):
    """Get a conversation with messages."""
    conv = _conversations.get(conv_id)
    if not conv or conv["user_id"] != user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")

    msgs = _messages.get(conv_id, [])
    return {
        **conv,
        "messages": msgs,
    }


# ── Message Endpoints ──────────────────────────────────


@router.post("/conversations/{conv_id}/messages")
async def send_message(
    conv_id: str,
    body: SendMessageRequest,
    request: Request,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Send a message and get a response (non-streaming)."""
    conv = _conversations.get(conv_id)
    if not conv or conv["user_id"] != user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")

    # Save user message
    user_msg_id = str(uuid.uuid4())
    user_msg = {
        "id": user_msg_id,
        "role": "user",
        "content": body.content,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _messages.setdefault(conv_id, []).append(user_msg)

    # Get history
    history = [
        {"role": m["role"], "content": m["content"]}
        for m in _messages.get(conv_id, [])[-10:]
    ]

    # Ask
    result = await ask(
        db=db,
        query=body.content,
        history=history,
        scope_override=body.scope,
        mode=body.mode,
    )

    # Save assistant message
    assistant_msg_id = str(uuid.uuid4())
    assistant_msg = {
        "id": assistant_msg_id,
        "role": "assistant",
        "content": result["answer"],
        "citations": result["citations"],
        "evidence": result["evidence"],
        "usage": result.get("usage"),
        "model": result.get("model"),
        "latency_ms": result.get("latency_ms"),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _messages[conv_id].append(assistant_msg)

    # Update conversation
    _conversations[conv_id]["updated_at"] = datetime.now(timezone.utc).isoformat()
    if len(_messages[conv_id]) <= 2:  # Only first exchange
        _conversations[conv_id]["title"] = body.content[:50]

    return assistant_msg


@router.get("/conversations/{conv_id}/stream")
async def stream_message(
    conv_id: str,
    q: str = Query(..., min_length=1),
    mode: str = Query(default="normal"),
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Stream a response via SSE."""
    conv = _conversations.get(conv_id)
    if not conv or conv["user_id"] != user.id:
        raise HTTPException(status_code=404, detail="Conversation not found")

    # Get history
    history = [
        {"role": m["role"], "content": m["content"]}
        for m in _messages.get(conv_id, [])[-10:]
    ]

    # Add user message to history
    user_msg = {
        "id": str(uuid.uuid4()),
        "role": "user",
        "content": q,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _messages.setdefault(conv_id, []).append(user_msg)

    # Save assistant response chunks
    full_answer_parts = []

    async def event_stream():
        full = ""
        async for event in ask_stream(
            db=db,
            query=q,
            history=history,
            mode=mode,
        ):
            # Extract text from token events
            if "event: token" in event:
                match = re.search(r'data: (.+)', event)
                if match:
                    try:
                        data = json_mod.loads(match.group(1))
                        full += data.get("text", "")
                    except Exception:
                        pass
            yield event
            await asyncio.sleep(0)

        # Save full answer
        if full:
            assistant_msg = {
                "id": str(uuid.uuid4()),
                "role": "assistant",
                "content": full,
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
            _messages[conv_id].append(assistant_msg)
            _conversations[conv_id]["updated_at"] = datetime.now(timezone.utc).isoformat()
            if len(_messages[conv_id]) <= 2:
                _conversations[conv_id]["title"] = q[:50]

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


# ── Quick Ask (no conversation) ────────────────────────


@router.post("/ask")
async def quick_ask(
    body: SendMessageRequest,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(current_user),
):
    """Ask a question without creating a conversation."""
    result = await ask(
        db=db,
        query=body.content,
        scope_override=body.scope,
        mode=body.mode,
    )
    return result
