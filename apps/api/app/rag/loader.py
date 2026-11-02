# -*- coding: utf-8 -*-
"""Load notes/sections and build retrieval chunks for the RAG vertical slice."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Iterable

import yaml

REPO = Path(__file__).resolve().parents[4]
ENRICHED = REPO / "data" / "notes_enriched"
DEFAULT_NOTES = ENRICHED if (ENRICHED / "_complete.json").exists() else REPO / "data" / "notes"
NOTES = Path(os.environ.get("CYBERME_NOTES_DIR", str(DEFAULT_NOTES)))
SECTIONS = REPO / "data" / "sections" / "sections.jsonl"
OUT = REPO / "data" / "rag"
OUT.mkdir(parents=True, exist_ok=True)
INCLUDE_SOURCE_CHUNKS = os.environ.get("CYBERME_INCLUDE_SOURCE_CHUNKS", "0") == "1"

FM_RE = re.compile(r"^---\n(.*?)\n---\n\n?", re.S)
H2_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
PAGE_RE = re.compile(r"<!-- page: \d+ -->")
SOURCE_REF_RE = re.compile(r"[（(]\s*来源\s*[:：][^）)]{0,200}[）)]")
SRC_ID_RE = re.compile(r"\bSRC-[A-Z]+-\d+(?:-SEC\d+)?\b")
PLACEHOLDER_LINE_RE = re.compile(
    r"^.*(?:本节.*(?:公式|变量).*缺失|原文.*(?:公式|变量).*缺失|未补写|待补充|暂无内容).*$",
    re.M,
)
PLACEHOLDER_RE = re.compile(r"(缺失|未补写|待补充|暂无数据|暂无内容)")


def clean_note_text(text: str) -> str:
    """Remove retrieval-noise from prose while keeping the claim itself."""
    text = PAGE_RE.sub("", text or "")
    text = SOURCE_REF_RE.sub("", text)
    text = SRC_ID_RE.sub("", text)
    text = PLACEHOLDER_LINE_RE.sub("", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()



def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8-sig", errors="replace")


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, text[m.end():]


def split_paragraphs(text: str, max_chars: int = 800, min_chars: int = 120) -> list[str]:
    text = PAGE_RE.sub("", text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if not paras:
        return []
    chunks: list[str] = []
    buf = ""
    for p in paras:
        if buf and len(buf) + len(p) + 2 > max_chars:
            if len(buf) >= min_chars:
                chunks.append(buf)
                buf = p
            else:
                buf = f"{buf}\n\n{p}"
        else:
            buf = f"{buf}\n\n{p}" if buf else p
        # a single huge paragraph: hard split
        while len(buf) > max_chars * 2:
            chunks.append(buf[:max_chars])
            buf = buf[max_chars:]
    if buf.strip():
        chunks.append(buf)
    return chunks


def pages_of(page_map: list[dict], start: int, end: int) -> list[list[int]]:
    pages = []
    for pm in page_map or []:
        if pm.get("char_end", 0) > start and pm.get("char_start", 0) < end:
            p = int(pm.get("page") or 0)
            if p > 0:
                pages.append(p)
    if not pages:
        return []
    return [[min(pages), max(pages)]]


def load_note_chunks() -> list[dict]:
    chunks = []
    for p in sorted(NOTES.glob("*/*.md")):
        fm, body = split_frontmatter(read_text(p))
        if not fm.get("id"):
            continue
        note_id = fm["id"]
        course = fm.get("course") or p.parent.name
        title = fm.get("title") or p.stem
        chapter = fm.get("chapter") or ""
        sources = fm.get("source") or []
        source_ids = []
        pages = []
        section_ids = []
        for s in sources:
            if not isinstance(s, dict):
                continue
            if s.get("source_id"):
                source_ids.append(s["source_id"])
            if s.get("source_pages"):
                sp = s["source_pages"]
                if isinstance(sp, list) and len(sp) >= 2:
                    pages.append([int(sp[0]), int(sp[1])])
                elif isinstance(sp, list) and len(sp) == 1:
                    pages.append([int(sp[0]), int(sp[0])])
            if s.get("section_id"):
                section_ids.append(s["section_id"])
        source_ids = list(dict.fromkeys(source_ids))
        section_ids = list(dict.fromkeys(section_ids))

        # split by H2
        matches = list(H2_RE.finditer(body))
        blocks = []
        if not matches:
            blocks.append(("正文", body))
        else:
            for i, m in enumerate(matches):
                start = m.end()
                end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
                blocks.append((m.group(1).strip(), body[start:end].strip()))

        idx = 0
        for heading, block in blocks:
            # Source lists and unresolved/processed conflict blocks are
            # metadata, not answers. Keeping conflict text out of retrieval
            # prevents an unresolved source contradiction from being cited as
            # a clean fact.
            if heading.strip() in {"来源", "參考文獻", "参考文献", "冲突", "冲突（保留）", "冲突（已处理）"}:
                continue
            for part in split_paragraphs(block, max_chars=700, min_chars=100):
                idx += 1
                text = clean_note_text(part)
                if len(text) < 30:
                    continue
                # Do not retrieve a placeholder as if it were a fact.
                if PLACEHOLDER_RE.search(text) and len(text) < 260:
                    continue
                chunks.append({
                    "chunk_id": f"{note_id}-C{idx:02d}",
                    "kind": "note",
                    "course": course,
                    "doc_id": note_id,
                    "title": title,
                    "heading": heading,
                    "heading_path": [chapter, heading] if chapter else [heading],
                    "text": text,
                    "source_ids": source_ids,
                    "pages": pages,
                    "section_ids": section_ids,
                    "chars": len(text),
                })
    return chunks


def load_source_chunks() -> list[dict]:
    """Raw source sections are opt-in.

    The raw corpus still contains covers, course jokes, OCR gaps and code
    fragments. They are useful as enrichment input, but unsafe as direct RAG
    evidence until an AI-cleaned source layer exists.
    """
    if not INCLUDE_SOURCE_CHUNKS:
        return []
    chunks = []
    if not SECTIONS.exists():
        return chunks
    for line in SECTIONS.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        part = json.loads(line)
        course = part.get("course", "")
        sid = part.get("source_id", "")
        part_id = part.get("part_id", "")
        heading_path = part.get("heading_path") or []
        title = heading_path[-1] if heading_path else sid
        page_map = part.get("page_map") or []
        text = part.get("text") or ""
        idx = 0
        for sub in split_paragraphs(text, max_chars=800, min_chars=120):
            idx += 1
            sub = sub.strip()
            if len(sub) < 40:
                continue
            # approximate page range: locate substring in part text
            start = text.find(sub[:60]) if sub[:60] else -1
            if start < 0:
                start = 0
            pages = pages_of(page_map, start, start + len(sub))
            chunks.append({
                "chunk_id": f"{part_id}-C{idx:02d}",
                "kind": "source",
                "course": course,
                "doc_id": sid,
                "title": title,
                "heading": title,
                "heading_path": heading_path,
                "text": sub,
                "source_ids": [sid] if sid else [],
                "pages": pages,
                "section_ids": [part.get("section_id", "")] if part.get("section_id") else [],
                "part_id": part_id,
                "chars": len(sub),
            })
    return chunks


def build_chunks() -> list[dict]:
    chunks = load_note_chunks() + load_source_chunks()
    with (OUT / "chunks.jsonl").open("w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    meta = {
        "chunks": len(chunks),
        "notes": len({c["doc_id"] for c in chunks if c["kind"] == "note"}),
        "note_chunks": sum(1 for c in chunks if c["kind"] == "note"),
        "sources": len({c["doc_id"] for c in chunks if c["kind"] == "source"}),
        "source_chunks": sum(1 for c in chunks if c["kind"] == "source"),
        "courses": sorted({c["course"] for c in chunks if c.get("course")}),
    }
    (OUT / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))
    return chunks


if __name__ == "__main__":
    build_chunks()
