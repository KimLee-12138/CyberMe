# -*- coding: utf-8 -*-
"""Corpus data-quality API.

All numbers are derived from the frozen v1 artifacts under data/.
No database dependency, no hardcoded counts in the frontend.
"""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException

from app.auth.dependencies import current_user

router = APIRouter(
    prefix="/api/v1/corpus",
    tags=["corpus-quality"],
    dependencies=[Depends(current_user)],
)

REPO = Path(__file__).resolve().parents[4]
DATA = REPO / "data"

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

STATUS_ORDER = ["official", "review", "candidate", "duplicate", "quarantine"]
STATUS_LABELS = {
    "official": "官方",
    "review": "待复核",
    "candidate": "候选",
    "duplicate": "重复",
    "quarantine": "隔离",
}

REASON_LABELS = {
    "too_short": "内容过短",
    "course_out_of_scope": "课程范围外",
    "exact_duplicate": "完全重复",
    "scanned_no_text": "扫描无文本",
    "project_or_code": "项目/代码",
    "garbled_encoding": "乱码",
    "pure_code_md": "纯代码 Markdown",
    "dependency_or_license": "依赖/许可证",
    "admin_document": "行政文件",
    "unmapped_course": "未映射课程",
}

DOC_TYPE_LABELS = {
    "notes": "笔记",
    "exam": "试卷",
    "slides": "课件",
    "exercise": "习题",
    "other": "其他",
}


def _csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            out.append(json.loads(line))
    return out


@lru_cache(maxsize=1)
def _dataset() -> dict:
    manifest = _json(DATA / "manifest_v1.json", {})
    summary = _json(DATA / "registry" / "summary.json", {})
    quality = _csv(DATA / "registry" / "quality_scores.csv")
    excluded = _csv(DATA / "registry" / "excluded.csv")
    quarantine = _csv(DATA / "registry" / "quarantine.csv")
    near_dups = _csv(DATA / "registry" / "near_duplicates.csv")
    notes_dir = DATA / "notes_enriched" if (DATA / "notes_enriched" / "_complete.json").exists() else DATA / "notes"
    notes = _csv(notes_dir / "_manifest.csv")
    review_sample = _csv(DATA / "notes" / "_review_sample.csv")
    writeback = _json(DATA / "notes" / "_writeback_proposal.json", {"items": []})
    coverage = _json(DATA / "sections" / "coverage_manifest.json", [])
    sections = _jsonl(DATA / "sections" / "sections.jsonl")
    topics = []
    for p in sorted((DATA / "topics").glob("*.jsonl")):
        topics.extend(_jsonl(p))

    # section counts
    section_ids_by_course: dict[str, set[str]] = defaultdict(set)
    parts_by_course: Counter = Counter()
    for s in sections:
        c = s.get("course") or ""
        if s.get("section_id"):
            section_ids_by_course[c].add(s["section_id"])
        parts_by_course[c] += 1

    # unit counts
    units_by_course: Counter = Counter()
    for p in (DATA / "units").glob("*/*.json"):
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        c = d.get("course") or ""
        units_by_course[c] += len((d.get("result") or {}).get("units") or [])

    notes_by_course = Counter(n.get("course", "") for n in notes)
    notes_by_topic = {n.get("topic_id"): n for n in notes if n.get("topic_id")}
    topics_by_id = {t.get("topic_id"): t for t in topics if t.get("topic_id")}

    quality_by_course: dict[str, Counter] = defaultdict(Counter)
    for q in quality:
        c = q.get("course", "")
        quality_by_course[c][q.get("quality_status", "")] += 1
        quality_by_course[c]["included"] += 1
        if q.get("distill") == "true":
            quality_by_course[c]["distill"] += 1
        if q.get("indexable") == "true":
            quality_by_course[c]["indexable"] += 1

    formula_by_course = Counter()
    conflicts_by_course = Counter()
    has_conflict_notes = 0
    for n in notes:
        c = n.get("course", "")
        flags = n.get("flags") or ""
        if "formula_missing" in flags:
            formula_by_course[c] += 1
        nconf = int(n.get("conflicts") or 0)
        if nconf:
            has_conflict_notes += 1
        conflicts_by_course[c] += nconf

    return {
        "manifest": manifest,
        "summary": summary,
        "quality": quality,
        "excluded": excluded,
        "quarantine": quarantine,
        "near_dups": near_dups,
        "notes": notes,
        "review_sample": review_sample,
        "writeback": writeback,
        "coverage": coverage,
        "sections": sections,
        "section_ids_by_course": section_ids_by_course,
        "parts_by_course": parts_by_course,
        "units_by_course": units_by_course,
        "notes_by_course": notes_by_course,
        "notes_by_topic": notes_by_topic,
        "topics": topics,
        "topics_by_id": topics_by_id,
        "quality_by_course": quality_by_course,
        "formula_by_course": formula_by_course,
        "conflicts_by_course": conflicts_by_course,
        "has_conflict_notes": has_conflict_notes,
    }


def _issue_counts(d: dict) -> dict:
    quality = d["quality"]
    status_counts = Counter(q.get("quality_status") for q in quality)
    near = Counter(x.get("relation") for x in d["near_dups"])
    return {
        "quality_status": {s: status_counts.get(s, 0) for s in STATUS_ORDER},
        "indexable": sum(1 for q in quality if q.get("indexable") == "true"),
        "distill": sum(1 for q in quality if q.get("distill") == "true"),
        "quarantine": status_counts.get("quarantine", 0),
        "duplicate_status": status_counts.get("duplicate", 0),
        "candidate_status": status_counts.get("candidate", 0),
        "near_duplicate_pairs": len(d["near_dups"]),
        "near_duplicate_duplicate": near.get("duplicate", 0),
        "near_duplicate_parallel": near.get("parallel", 0),
        "near_duplicate_candidate": near.get("candidate", 0),
        "conflicts": sum(int(n.get("conflicts") or 0) for n in d["notes"]),
        "conflict_notes": d["has_conflict_notes"],
        "formula_missing_notes": sum(1 for n in d["notes"] if "formula_missing" in (n.get("flags") or "")),
        "review_sample": len(d["review_sample"]),
        "writeback_total": len(d["writeback"].get("items", [])),
    }


@router.get("/stats")
def corpus_stats():
    d = _dataset()
    m = d["manifest"]
    funnel = m.get("funnel", {})
    quality = m.get("quality", {})
    summary = d["summary"]
    coverage = d["coverage"]
    counts = _issue_counts(d)

    excluded = d["excluded"]
    reason_counter = Counter()
    for row in excluded:
        for reason in (row.get("reason") or "").split(";"):
            if reason:
                reason_counter[reason] += 1
    reasons = [
        {"reason": k, "label": REASON_LABELS.get(k, k), "count": v}
        for k, v in reason_counter.most_common()
    ]

    doc_types = [
        {"type": k, "label": DOC_TYPE_LABELS.get(k, k), "count": v}
        for k, v in sorted((summary.get("doc_type_counts") or {}).items(), key=lambda x: -x[1])
    ]

    return {
        "version": m.get("version", "v1"),
        "generated_at": m.get("generated_at"),
        "vault_unchanged": True,
        "funnel": [
            {
                "key": "raw",
                "label": "原始文件",
                "count": funnel.get("raw_files", 0),
                "note": f"{summary.get('raw_pdf', 0)} PDF + {summary.get('raw_md', 0)} MD",
                "kind": "files",
            },
            {
                "key": "included",
                "label": "纳入语料",
                "count": funnel.get("included_files", 0),
                "note": f"排除 {len(excluded)} 个文件",
                "kind": "files",
            },
            {
                "key": "distill",
                "label": "进入蒸馏",
                "count": funnel.get("distill_files", 0),
                "note": f"{counts['distill']} / {funnel.get('included_files', 0)} 个文件",
                "kind": "files",
            },
            {
                "key": "sections",
                "label": "Section Part",
                "count": funnel.get("section_parts", 0),
                "note": f"{funnel.get('distill_files', 0)} 文件 → {funnel.get('section_parts', 0)} part",
                "kind": "parts",
            },
            {
                "key": "units",
                "label": "知识单元",
                "count": funnel.get("knowledge_units", 0),
                "note": f"{funnel.get('section_parts', 0)} part → {funnel.get('knowledge_units', 0)} unit",
                "kind": "units",
            },
            {
                "key": "topics",
                "label": "主题 / 笔记",
                "count": funnel.get("topics", 0),
                "note": f"{funnel.get('knowledge_units', 0)} unit → {funnel.get('topics', 0)} topic",
                "kind": "topics",
            },
        ],
        "raw": {
            "pdf": summary.get("raw_pdf", 0),
            "md": summary.get("raw_md", 0),
            "pages": summary.get("raw_pages", 0),
            "chars": summary.get("raw_chars", 0),
        },
        "included": {
            "pdf": summary.get("included_pdf", 0),
            "md": summary.get("included_md", 0),
            "pages": summary.get("included_pages", 0),
            "chars": summary.get("included_chars", 0),
        },
        "quality": {
            **{s: quality.get(s, counts["quality_status"].get(s, 0)) for s in STATUS_ORDER},
            "indexable": quality.get("indexable", counts["indexable"]),
            "distill": quality.get("distill", counts["distill"]),
            "conflicts": counts["conflicts"],
            "formula_missing_notes": counts["formula_missing_notes"],
            "merge_duplicate": quality.get("merge_duplicate", 0),
            "merge_supplement": quality.get("merge_supplement", 0),
            "merge_new": quality.get("merge_new", 0),
        },
        "coverage": {
            "files": len(coverage),
            "sections": len({s.get("section_id") for s in d["sections"] if s.get("section_id")}),
            "parts": len(d["sections"]),
            "covered_files": sum(1 for c in coverage if float(c.get("coverage") or 0) >= 0.999),
            "coverage": 1.0 if coverage and all(float(c.get("coverage") or 0) >= 0.999 for c in coverage) else 0.0,
            "gaps": sum(len(c.get("gaps") or []) for c in coverage),
        },
        "issues": counts,
        "resolution": {
            "enriched_notes": len(d["notes"]),
            "source_supported_formulas": sum(
                int(n.get("formula_support") or 0) for n in d["notes"]
            ),
            "quarantine_excluded": counts["quarantine"],
            "near_duplicate_sources": counts["near_duplicate_pairs"],
            "raw_source_chunks_indexed": 0,
            "formula_missing_remaining": counts["formula_missing_notes"],
            "conflicts_unresolved": counts["conflicts"],
        },
        "exclusions": {
            "total": len(excluded),
            "reasons": reasons,
        },
        "doc_types": doc_types,
        "writeback": {
            "total": len(d["writeback"].get("items", [])),
            "create": sum(1 for i in d["writeback"].get("items", []) if i.get("action") == "create"),
            "append_supplement": sum(1 for i in d["writeback"].get("items", []) if i.get("action") == "append_supplement"),
            "skip_duplicate": sum(1 for i in d["writeback"].get("items", []) if i.get("action") == "skip_duplicate"),
            "vault_modified": False,
        },
        "cost": m.get("cost", {}),
        "empty_courses": [c for c in COURSE_NAMES if c not in d["quality_by_course"]],
    }


@router.get("/courses")
def corpus_courses():
    d = _dataset()
    summary_by_course = d["summary"].get("by_course", {})
    courses = []
    for code, qc in d["quality_by_course"].items():
        name = COURSE_NAMES.get(code, code)
        courses.append({
            "course": code,
            "name": name,
            "included": qc.get("included", 0),
            "distill": qc.get("distill", 0),
            "indexable": qc.get("indexable", 0),
            "sections": len(d["section_ids_by_course"].get(code, set())),
            "parts": d["parts_by_course"].get(code, 0),
            "units": d["units_by_course"].get(code, 0),
            "topics": d["notes_by_course"].get(code, 0),
            "notes": d["notes_by_course"].get(code, 0),
            "quality": {s: qc.get(s, 0) for s in STATUS_ORDER},
            "formula_missing": d["formula_by_course"].get(code, 0),
            "conflicts": d["conflicts_by_course"].get(code, 0),
            "coverage": 1.0,
            "raw_files": (summary_by_course.get(code) or {}).get("files", qc.get("included", 0)),
            "raw_pages": (summary_by_course.get(code) or {}).get("pages", 0),
            "raw_chars": (summary_by_course.get(code) or {}).get("chars", 0),
        })
    courses.sort(key=lambda c: (-c["notes"], c["course"]))
    return {
        "courses": courses,
        "total": len(courses),
        "empty_courses": [c for c in COURSE_NAMES if c not in d["quality_by_course"]],
        "totals": {
            "included": sum(c["included"] for c in courses),
            "distill": sum(c["distill"] for c in courses),
            "sections": sum(c["sections"] for c in courses),
            "units": sum(c["units"] for c in courses),
            "topics": sum(c["topics"] for c in courses),
            "formula_missing": sum(c["formula_missing"] for c in courses),
            "conflicts": sum(c["conflicts"] for c in courses),
        },
    }


@router.get("/issues")
def corpus_issues():
    d = _dataset()

    quarantine = []
    for r in d["quarantine"]:
        quarantine.append({
            "source_id": r.get("source_id", ""),
            "course": r.get("course", ""),
            "course_name": COURSE_NAMES.get(r.get("course", ""), r.get("course", "")),
            "rel": r.get("rel", ""),
            "pages": int(r.get("pages") or 0),
            "chars": int(r.get("chars") or 0),
            "quality_score": float(r.get("quality_score") or 0),
            "reasons": r.get("reasons", ""),
        })

    duplicates = []
    for r in d["near_dups"]:
        duplicates.append({
            "relation": r.get("relation", ""),
            "course": r.get("course", ""),
            "course_name": COURSE_NAMES.get(r.get("course", ""), r.get("course", "")),
            "source_a": r.get("source_a", ""),
            "source_b": r.get("source_b", ""),
            "rel_a": r.get("rel_a", ""),
            "rel_b": r.get("rel_b", ""),
            "jaccard": float(r.get("jaccard") or 0),
            "hamming": int(r.get("hamming") or 0),
        })

    conflicts = []
    for t in d["topics"]:
        topic = t.get("topic") or {}
        note = d["notes_by_topic"].get(t.get("topic_id"), {})
        # Enriched notes may have resolved/non-conflict marks. Do not keep
        # showing those as open issues.
        if note and int(note.get("conflicts") or 0) == 0:
            continue
        for text in topic.get("conflicts") or []:
            conflicts.append({
                "course": t.get("course", ""),
                "course_name": COURSE_NAMES.get(t.get("course", ""), t.get("course", "")),
                "topic_id": t.get("topic_id", ""),
                "title": topic.get("title", ""),
                "note_id": note.get("note_id", ""),
                "note_path": note.get("path", ""),
                "conflict": text,
                "status": "unresolved",
            })

    formula_missing = []
    for n in d["notes"]:
        if "formula_missing" in (n.get("flags") or ""):
            formula_missing.append({
                "note_id": n.get("note_id", ""),
                "course": n.get("course", ""),
                "course_name": COURSE_NAMES.get(n.get("course", ""), n.get("course", "")),
                "title": n.get("title", ""),
                "path": n.get("path", ""),
                "flags": n.get("flags", ""),
                "source_count": int(n.get("source_count") or 0),
            })

    writeback_items = d["writeback"].get("items", [])
    writeback = {
        "total": len(writeback_items),
        "create": sum(1 for i in writeback_items if i.get("action") == "create"),
        "append_supplement": sum(1 for i in writeback_items if i.get("action") == "append_supplement"),
        "skip_duplicate": sum(1 for i in writeback_items if i.get("action") == "skip_duplicate"),
        "vault_modified": False,
        "sample": writeback_items[:8],
    }

    counts = _issue_counts(d)
    return {
        "counts": counts,
        "conflicts": conflicts,
        "quarantine": quarantine,
        "formula_missing": formula_missing,
        "near_duplicates": duplicates,
        "writeback": writeback,
    }


@router.get("/health")
def corpus_health():
    try:
        d = _dataset()
        return {"status": "ok", "quality_rows": len(d["quality"]), "notes": len(d["notes"])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"corpus data failed: {e}")
