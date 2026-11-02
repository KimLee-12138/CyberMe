# -*- coding: utf-8 -*-
"""Note browser API — list/search 433 generated notes and read one note."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from functools import lru_cache
from pathlib import Path

import yaml
from fastapi import APIRouter, Depends, HTTPException, Query

from app.auth.dependencies import current_user

router = APIRouter(
    prefix="/api/v1/notes",
    tags=["notes"],
    dependencies=[Depends(current_user)],
)

REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "data"
ENRICHED = DATA / "notes_enriched"
NOTES_DIR = ENRICHED if (ENRICHED / "_complete.json").exists() else (DATA / "notes")

COURSE_NAMES = {
    "DB": "数据库",
    "ALGO": "算法",
    "DS": "数据结构",
    "CO": "计算机组成原理",
    "SE": "软件工程",
    "EDA": "EDA",
    "ASM": "汇编",
    "JAVA": "Java",
    "PY": "Python",
    "CPP": "C++",
    "PROB": "概率论",
    "CALCULUS": "微积分",
    "LINALG": "线性代数",
    "DISCRETE": "离散数学",
    "PHYSICS": "大学物理",
    "MAYUAN": "马原",
    "MAOGAI": "毛概",
    "XIGAI": "习概",
    "HISTORY": "近代史",
    "SIXIANG": "思想与政治",
    "JUNLI": "军理",
    "RLMATH": "强化学习数学",
    "INFO": "信息导论",
    "ZHENGCE": "政策与形势",
}

FLAG_LABELS = {
    "formula_missing": "公式缺失",
    "no_definition": "缺定义",
    "has_conflict": "有冲突",
}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.S)
MATCH_RE = re.compile(r"[\s，。；：！？、,.!?;:（）()\[\]【】]+")


def _jsonable(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        return [_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}
    return str(value)


def _read_frontmatter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    body = text[m.end():].lstrip()
    # The page header shows the title, so drop the duplicate H1.
    if body.startswith("# "):
        body = body.split("\n", 1)[1].lstrip() if "\n" in body else ""
    return fm if isinstance(fm, dict) else {}, body


def _summary(body: str) -> str:
    m = re.search(r"^##\s*一句话\s*\n+(.+?)(?=\n##|\Z)", body, re.S | re.M)
    if m:
        text = m.group(1).strip()
    else:
        text = body[:260]
    return re.sub(r"\s+", " ", text).strip()


def _snippet(body: str, query: str) -> str:
    if not query:
        return _summary(body)
    lower = body.lower()
    terms = [t.lower() for t in MATCH_RE.split(query) if t.strip()]
    pos = -1
    for t in terms:
        pos = lower.find(t)
        if pos >= 0:
            break
    if pos < 0:
        return _summary(body)
    start = max(0, pos - 70)
    end = min(len(body), pos + 150)
    return re.sub(r"\s+", " ", body[start:end]).strip()


BAD_META = {"", "{", "}", "none", "null", "nan"}


def _chapter(value, sources: list[dict]) -> str:
    text = str(value or "").strip()
    if text.lower() not in BAD_META:
        return text
    for s in sources:
        title = (s.get("section_title") or "").strip()
        if title and title.lower() not in BAD_META:
            return title
    return ""


def _clean_tags(value) -> list[str]:
    if not isinstance(value, list):
        return []
    out = []
    for t in value:
        text = str(t).strip()
        if not text or text.lower() in BAD_META:
            continue
        if not re.search(r"[\u4e00-\u9fffA-Za-z0-9]", text):
            continue
        out.append(text)
    return list(dict.fromkeys(out))


def _csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


@lru_cache(maxsize=1)
def _dataset() -> dict:
    index = []
    for line in (NOTES_DIR / "_index.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            index.append(json.loads(line))
    manifest = {r["note_id"]: r for r in _csv(NOTES_DIR / "_manifest.csv") if r.get("note_id")}
    sources = {r["source_id"]: r for r in _csv(DATA / "clean" / "manifest.csv") if r.get("source_id")}

    sections = {}
    for line in (DATA / "sections" / "sections.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        p = json.loads(line)
        sid = p.get("section_id")
        if sid and sid not in sections:
            sections[sid] = p

    topics = {}
    for p in sorted((DATA / "topics").glob("*.jsonl")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                t = json.loads(line)
                if t.get("topic_id"):
                    topics[t["topic_id"]] = t

    records = {}
    for row in index:
        note_id = row.get("note_id")
        path = REPO / (row.get("path") or "")
        if not note_id or not path.exists():
            continue
        raw = path.read_text(encoding="utf-8-sig", errors="replace")
        fm, body = _read_frontmatter(raw)
        mf = manifest.get(note_id, {})
        flags = [x for x in (mf.get("flags") or "").split(";") if x]
        sources_out = []
        for s in row.get("sources") or []:
            sid = s.get("source_id", "")
            src = sources.get(sid, {})
            section = sections.get(s.get("section_id", "")) or {}
            heading_path = section.get("heading_path") or [""]
            sources_out.append({
                "source_id": sid,
                "rel": src.get("rel", ""),
                "doc_type": src.get("doc_type", ""),
                "source_pages": s.get("source_pages") or [],
                "section_id": s.get("section_id", ""),
                "section_title": heading_path[-1],
            })
        records[note_id] = {
            "note_id": note_id,
            "topic_id": row.get("topic_id", ""),
            "course": row.get("course", ""),
            "course_name": COURSE_NAMES.get(row.get("course", ""), row.get("course", "")),
            "title": fm.get("title") or row.get("title", ""),
            "chapter": _chapter(fm.get("chapter"), sources_out),
            "aliases": fm.get("aliases") or [],
            "tags": _clean_tags(fm.get("tags")),
            "confidence": float(fm.get("confidence") or row.get("confidence") or 0),
            "verification": fm.get("verification") or row.get("verification") or "",
            "unit_count": int(fm.get("unit_count") or 0),
            "key_points": int(row.get("key_points") or 0),
            "formulas": int(row.get("formulas") or 0),
            "conflicts": int(row.get("conflicts") or 0),
            "source_count": len(sources_out),
            "sources": sources_out,
            "flags": flags,
            "path": row.get("path", ""),
            "body": body,
            "summary": _summary(body),
            "frontmatter": fm,
            "topic": (topics.get(row.get("topic_id", "")) or {}).get("topic", {}),
        }

    # facets from all notes
    course_counts = Counter(r["course"] for r in records.values())
    flag_counts = Counter(f for r in records.values() for f in r["flags"])
    return {
        "records": records,
        "course_counts": course_counts,
        "flag_counts": flag_counts,
        "total": len(records),
    }


def _item(r: dict, q: str = "") -> dict:
    return {
        "note_id": r["note_id"],
        "topic_id": r["topic_id"],
        "course": r["course"],
        "course_name": r["course_name"],
        "title": r["title"],
        "chapter": r["chapter"],
        "aliases": r["aliases"],
        "tags": r["tags"],
        "confidence": r["confidence"],
        "verification": r["verification"],
        "unit_count": r["unit_count"],
        "key_points": r["key_points"],
        "formulas": r["formulas"],
        "conflicts": r["conflicts"],
        "source_count": r["source_count"],
        "flags": r["flags"],
        "path": r["path"],
        "summary": r["summary"],
        "snippet": _snippet(r["body"], q),
    }


@router.get("")
def list_notes(
    q: str = Query(default="", max_length=200),
    course: str | None = Query(default=None, max_length=20),
    flag: str | None = Query(default=None, max_length=40),
    limit: int = Query(default=500, ge=1, le=500),
    offset: int = Query(default=0, ge=0),
):
    d = _dataset()
    records = list(d["records"].values())
    query = q.strip().lower()

    def score(r: dict) -> int:
        if not query:
            return 0
        title = r["title"].lower()
        aliases = " ".join(str(x) for x in r["aliases"]).lower()
        if query in title:
            return 3
        if any(x in aliases for x in MATCH_RE.split(query) if x):
            return 2
        if query in r["body"].lower():
            return 1
        return 0

    if query:
        scored = [(score(r), r) for r in records]
        records = [r for s, r in scored if s > 0]
        records.sort(key=lambda r: (-score(r), r["course"], r["title"]))
    else:
        records.sort(key=lambda r: (r["course"], r["title"]))

    if course:
        code = course.upper()
        records = [r for r in records if r["course"] == code]
    if flag:
        records = [r for r in records if flag in r["flags"]]

    total = len(records)
    page = records[offset:offset + limit]
    courses = [
        {"course": c, "name": COURSE_NAMES.get(c, c), "count": n}
        for c, n in sorted(d["course_counts"].items(), key=lambda x: (-x[1], x[0]))
    ]
    flags = [
        {"flag": f, "label": FLAG_LABELS.get(f, f), "count": n}
        for f, n in sorted(d["flag_counts"].items(), key=lambda x: -x[1])
    ]
    return {
        "items": [_item(r, query) for r in page],
        "total": total,
        "offset": offset,
        "limit": limit,
        "stats": {
            "all_notes": d["total"],
            "filtered": total,
            "courses": len(courses),
            "formula_missing": sum(1 for r in d["records"].values() if "formula_missing" in r["flags"]),
            "conflicts": sum(1 for r in d["records"].values() if "has_conflict" in r["flags"]),
            "no_definition": sum(1 for r in d["records"].values() if "no_definition" in r["flags"]),
        },
        "courses": courses,
        "flags": flags,
    }


@router.get("/{note_id}")
def get_note(note_id: str):
    d = _dataset()
    r = d["records"].get(note_id)
    if not r:
        raise HTTPException(status_code=404, detail=f"note not found: {note_id}")
    return {
        **_item(r, ""),
        "body": r["body"],
        "frontmatter": _jsonable(r["frontmatter"]),
        "sources": r["sources"],
        "topic": _jsonable(r["topic"]),
    }
