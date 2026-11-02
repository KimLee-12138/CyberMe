# -*- coding: utf-8 -*-
"""Offline API regression tests (no Postgres/Redis/LLM)."""
from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

DATA_NOTES = Path(__file__).resolve().parents[1] / "data" / "notes" / "_index.jsonl"
pytestmark = pytest.mark.skipif(
    not DATA_NOTES.exists(),
    reason="private study corpus is not included in the public repository",
)

from app.auth.dependencies import current_user
from app.corpus.router import router as corpus_router
from app.kg.router import router as kg_router
from app.notes.router import router as notes_router
from app.rag.router import router as rag_router


def _client(router) -> TestClient:
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[current_user] = lambda: SimpleNamespace(id="test", username="test")
    return TestClient(app)


def test_notes_total() -> None:
    r = _client(notes_router).get("/api/v1/notes")
    assert r.status_code == 200
    data = r.json()
    assert data["total"] == 433
    assert data["stats"]["courses"] == 20
    assert data["stats"]["formula_missing"] == 0


def test_notes_search_and_detail() -> None:
    c = _client(notes_router)
    search = c.get("/api/v1/notes", params={"q": "函数依赖"}).json()
    assert search["total"] == 2
    detail = c.get("/api/v1/notes/DB-TOPIC-001").json()
    assert "数据库基础" in detail["title"]
    assert detail["sources"][0]["source_pages"] == [1, 4]
    assert detail["chapter"]


def test_corpus_funnel() -> None:
    data = _client(corpus_router).get("/api/v1/corpus/stats").json()
    assert [x["count"] for x in data["funnel"]] == [868, 410, 309, 414, 4523, 433]
    assert data["quality"]["official"] == 150
    assert data["quality"]["formula_missing_notes"] == 0
    assert data["coverage"]["coverage"] == 1.0


def test_kg_overview() -> None:
    data = _client(kg_router).get("/api/v1/kg/graph").json()
    assert len(data["nodes"]) == 24
    assert len(data["edges"]) == 18
    validate = _client(kg_router).get("/api/v1/kg/validate").json()
    assert validate["ok"] is True


def test_rag_health() -> None:
    data = _client(rag_router).get("/api/v1/rag/health").json()
    assert data["chunks"] == 2599
    assert data["notes"] == 433


def test_notes_requires_auth() -> None:
    app = FastAPI()
    app.include_router(notes_router)
    r = TestClient(app).get("/api/v1/notes")
    assert r.status_code == 401
