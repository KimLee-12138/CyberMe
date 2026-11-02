# -*- coding: utf-8 -*-
"""Stage 3 — FastAPI routes for the RAG vertical slice."""
from __future__ import annotations

import asyncio
import json
import threading
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from app.auth.dependencies import current_user
from app.rag.answer import ask
from app.rag.quiz import generate_quiz
from app.rag.retriever import RagIndex

router = APIRouter(
    prefix="/api/v1/rag",
    tags=["rag"],
    dependencies=[Depends(current_user)],
)

_index: RagIndex | None = None
_lock = threading.Lock()
META = Path(__file__).resolve().parents[4] / "data" / "rag" / "meta.json"


class AskRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500)
    course: str | None = Field(default=None, max_length=20)
    top_k: int = Field(default=8, ge=1, le=20)


class QuizRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=500)
    answer: str = Field(..., min_length=1, max_length=12000)
    count: int = Field(default=3, ge=1, le=5)


class AskResponse(BaseModel):
    query: str
    course: str | None = None
    answer: str
    citations: list[dict] = []
    evidence: list[dict] = []
    refused: bool = False
    degraded: bool = False
    degraded_reason: str = ""
    refusal_reason: str = ""
    coverage: float | None = None
    model: str | None = None
    usage: dict = {}
    latency_ms: int | None = None


def get_index() -> RagIndex:
    global _index
    if _index is None:
        with _lock:
            if _index is None:
                _index = RagIndex.load()
    return _index


@router.post("/ask", response_model=AskResponse)
async def rag_ask(req: AskRequest):
    try:
        index = await asyncio.to_thread(get_index)
        result = await asyncio.to_thread(
            ask, index, req.query, req.course, req.top_k
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG failed: {e}")


@router.post("/quiz")
async def rag_quiz(req: QuizRequest):
    try:
        return await asyncio.to_thread(
            generate_quiz, req.query, req.answer, req.count
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Quiz generation failed: {e}")


@router.get("/health")
async def rag_health():
    meta = {}
    if META.exists():
        try:
            meta = json.loads(META.read_text(encoding="utf-8"))
        except Exception:
            meta = {}
    return {
        "status": "ok",
        "index_loaded": _index is not None,
        "chunks": meta.get("chunks"),
        "notes": meta.get("notes"),
        "sources": meta.get("sources"),
    }
