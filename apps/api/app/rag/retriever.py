# -*- coding: utf-8 -*-
"""BM25 retrieval over notes + source sections."""
from __future__ import annotations

import json
import logging
import os
import re
import warnings
from pathlib import Path

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message=".*pkg_resources.*")

import jieba
import numpy as np
from rank_bm25 import BM25Okapi

jieba.setLogLevel(logging.ERROR)

REPO = Path(__file__).resolve().parents[4]
RAG = REPO / "data" / "rag"
CHUNKS = RAG / "chunks.jsonl"
INCLUDE_SOURCE_CHUNKS = os.environ.get("CYBERME_INCLUDE_SOURCE_CHUNKS", "0") == "1"

STOP = set("""
的 了 和 是 在 有 与 及 对 中 为 等 也 就 都 而 及 其 这 那 一个 一种 我们 你们 他们
什么 怎么 为什么 如何 哪些 哪个 可以 需要 进行 通过 以及 但是 如果 因为 所以
the a an of to in on for and or is are be with by as at from that this it
""".split())

TOKEN_RE = re.compile(r"[\u4e00-\u9fffA-Za-z0-9]+")

HEADING_BOOST = {
    "定义": 1.15,
    "关键点": 1.10,
    "易错点": 1.12,
    "公式": 1.05,
    "例子": 1.03,
    "一句话": 1.00,
    "冲突": 0.90,
    "来源": 0.35,
    "关系": 0.55,
}


def tokenize(text: str) -> list[str]:
    text = (text or "").lower()
    out = []
    for w in jieba.lcut_for_search(text):
        w = w.strip()
        if not w:
            continue
        if w in STOP:
            continue
        if not TOKEN_RE.search(w):
            continue
        out.append(w)
    if not out:
        out = TOKEN_RE.findall(text)
    return out


class RagIndex:
    def __init__(self, chunks: list[dict]):
        self.chunks = chunks
        self.corpus = [
            tokenize(f"{c.get('title','')} {c.get('heading','')} {' '.join(c.get('heading_path') or [])} {c.get('text','')}")
            for c in chunks
        ]
        self.bm25 = BM25Okapi(self.corpus) if self.corpus else None
        self.vocabulary = set().union(*self.corpus) if self.corpus else set()

    @classmethod
    def load(cls, rebuild: bool = False) -> "RagIndex":
        if rebuild or not CHUNKS.exists():
            from app.rag.loader import build_chunks
            chunks = build_chunks()
        else:
            chunks = [json.loads(x) for x in CHUNKS.read_text(encoding="utf-8").splitlines() if x.strip()]
        if not INCLUDE_SOURCE_CHUNKS:
            chunks = [c for c in chunks if c.get("kind") != "source"]
        return cls(chunks)

    def stats(self) -> dict:
        return {
            "chunks": len(self.chunks),
            "notes": len({c["doc_id"] for c in self.chunks if c["kind"] == "note"}),
            "note_chunks": sum(1 for c in self.chunks if c["kind"] == "note"),
            "sources": len({c["doc_id"] for c in self.chunks if c["kind"] == "source"}),
            "source_chunks": sum(1 for c in self.chunks if c["kind"] == "source"),
            "courses": sorted({c["course"] for c in self.chunks if c.get("course")}),
        }

    def search(self, query: str, top_k: int = 8, course: str | None = None) -> list[dict]:
        if not self.bm25 or not query.strip():
            return []
        q = tokenize(query)
        if not q:
            return []
        scores = np.asarray(self.bm25.get_scores(q), dtype=float)
        # small heuristic boosts: prefer definitions/key points over link lists
        for i, c in enumerate(self.chunks):
            hb = HEADING_BOOST.get((c.get("heading") or "").strip(), 1.0)
            kb = 1.08 if c.get("kind") == "note" else 1.0
            scores[i] *= hb * kb
        if course:
            for i, c in enumerate(self.chunks):
                if c.get("course") != course:
                    scores[i] = -1.0
        order = np.argsort(scores)[::-1]
        top_score = float(scores[order[0]]) if len(order) else 0.0
        # A weak lexical match is often an unrelated course/code fragment.
        # Keep the result set anchored to the best match instead of padding
        # to top_k with noise.
        min_score = max(1.0, top_score * 0.55)
        out = []
        per_doc = {}
        for rank, i in enumerate(order, 1):
            if scores[i] <= 0 or scores[i] < min_score:
                break
            c = self.chunks[i]
            doc = c["doc_id"]
            if per_doc.get(doc, 0) >= 2:
                continue
            per_doc[doc] = per_doc.get(doc, 0) + 1
            out.append({
                "rank": len(out) + 1,
                "score": round(float(scores[i]), 4),
                "kind": c["kind"],
                "course": c.get("course", ""),
                "doc_id": doc,
                "chunk_id": c["chunk_id"],
                "title": c.get("title", ""),
                "heading": c.get("heading", ""),
                "heading_path": c.get("heading_path", []),
                "snippet": c.get("text", "")[:320],
                "source_ids": c.get("source_ids", []),
                "pages": c.get("pages", []),
                "section_ids": c.get("section_ids", []),
            })
            if len(out) >= top_k:
                break
        # If one course clearly dominates, don't pad the evidence with
        # unrelated courses just to reach top_k.
        if out:
            top_course = out[0]["course"]
            same = [r for r in out if r["course"] == top_course]
            others = [r for r in out if r["course"] != top_course]
            if len(same) >= 2 and others:
                best_other = max(r["score"] for r in others)
                if out[0]["score"] >= best_other * 1.3:
                    out = same
        return out
