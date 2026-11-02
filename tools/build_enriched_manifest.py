# -*- coding: utf-8 -*-
"""Build a manifest and quality report for data/notes_enriched."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "data" / "notes_enriched"


def split_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n\n?", text, re.S)
    if not m:
        return {}, text
    try:
        return yaml.safe_load(m.group(1)) or {}, text[m.end():]
    except Exception:
        return {}, text[m.end():]


def section(body: str, name: str) -> str:
    m = re.search(rf"^##\s+{re.escape(name)}.*?$\n(.*?)(?=^##\s+|\Z)", body, re.M | re.S)
    return (m.group(1).strip() if m else "")


def count_points(text: str) -> int:
    return len(re.findall(r"^\s*(?:\d+[.、)]|[-*])\s+", text, re.M))


def main() -> None:
    rows = []
    index_rows = []
    quality = Counter()
    for p in sorted(ROOT.glob("*/*.md")):
        text = p.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        if not fm.get("id"):
            continue
        course = fm.get("course", p.parent.name)
        enr = fm.get("enrichment") or {}
        flags = list(enr.get("flags") or [])
        # formula_missing is a STEM dimension; humanities notes often have no
        # formulas by design and should not inflate the issue count.
        if course not in {"ALGO", "ASM", "CALCULUS", "CO", "CPP", "DB", "DISCRETE",
                          "DS", "EDA", "JAVA", "PHYSICS", "PROB", "RLMATH", "SE"}:
            flags = [f for f in flags if f != "formula_missing"]
        conflict = section(body, "冲突（保留）") or section(body, "冲突（已处理）") or section(body, "冲突")
        conflict_status = enr.get("conflict_status") or ("unresolved" if conflict else "")
        unresolved_conflict = conflict_status == "unresolved"
        conflict_items = len(re.findall(r"^\s*[-*]\s+", conflict, re.M)) if unresolved_conflict else 0
        if unresolved_conflict:
            conflict_items = max(1, conflict_items)
        if unresolved_conflict and "has_conflict" not in flags:
            flags.append("has_conflict")
        elif not unresolved_conflict:
            flags = [f for f in flags if f != "has_conflict"]
        formulas = count_points(section(body, "公式"))
        keypoints = count_points(section(body, "关键点"))
        formula_expected = enr.get("formula_expected", True)
        if formulas > 0:
            flags = [f for f in flags if f != "formula_missing"]
        elif course in {"ALGO", "ASM", "CALCULUS", "CO", "CPP", "DB", "DISCRETE",
                        "DS", "EDA", "JAVA", "PHYSICS", "PROB", "RLMATH", "SE"} and formula_expected:
            if "formula_missing" not in flags:
                flags.append("formula_missing")
        elif not formula_expected:
            flags = [f for f in flags if f != "formula_missing"]
        if not section(body, "定义") and "definition_missing" not in flags:
            flags.append("definition_missing")
        elif section(body, "定义"):
            flags = [f for f in flags if f != "definition_missing"]
        if not section(body, "例子") and "example_missing" not in flags:
            flags.append("example_missing")
        elif section(body, "例子"):
            flags = [f for f in flags if f != "example_missing"]
        if not section(body, "易错点") and "pitfall_missing" not in flags:
            flags.append("pitfall_missing")
        elif section(body, "易错点"):
            flags = [f for f in flags if f != "pitfall_missing"]
        for f in flags:
            quality[f] += 1
        sources = fm.get("source") or []
        rows.append({
            "note_id": fm.get("id", ""),
            "topic_id": fm.get("topic_id", ""),
            "course": course,
            "title": fm.get("title", ""),
            "path": str(p.relative_to(REPO)).replace("\\", "/"),
            "source_count": len(sources),
            "key_points": keypoints,
            "formulas": formulas,
            "conflicts": conflict_items,
            "confidence": fm.get("confidence", 0),
            "flags": ";".join(dict.fromkeys(flags)),
            "verification": fm.get("verification", ""),
            "source_chars": enr.get("source_chars", 0),
            "has_supplement": bool(enr.get("has_supplement")),
            "formula_support": sum(1 for x in (enr.get("formula_support") or []) if x.get("source_supported")),
        })
        index_rows.append({
            "note_id": fm.get("id", ""),
            "topic_id": fm.get("topic_id", ""),
            "course": course,
            "title": fm.get("title", ""),
            "path": str(p.relative_to(REPO)).replace("\\", "/"),
            "sources": sources,
            "key_points": keypoints,
            "formulas": formulas,
            "conflicts": conflict_items,
            "confidence": fm.get("confidence", 0),
            "verification": fm.get("verification", ""),
            "status": fm.get("status", ""),
        })

    with (ROOT / "_index.jsonl").open("w", encoding="utf-8") as f:
        for row in index_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    fields = ["note_id", "topic_id", "course", "title", "path", "source_count",
              "key_points", "formulas", "conflicts", "confidence", "flags",
              "verification", "source_chars", "has_supplement", "formula_support"]
    with (ROOT / "_manifest.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    meta = {
        "notes": len(rows),
        "formula_missing": quality.get("formula_missing", 0),
        "definition_missing": quality.get("definition_missing", 0),
        "example_missing": quality.get("example_missing", 0),
        "pitfall_missing": quality.get("pitfall_missing", 0),
        "has_conflict": quality.get("has_conflict", 0),
        "has_supplement": sum(1 for r in rows if r["has_supplement"]),
        "formula_support": sum(r["formula_support"] for r in rows),
        "flags": dict(quality),
    }
    (ROOT / "_quality_report.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    lines = [
        "# Enriched note quality",
        "",
        f"- notes: {meta['notes']}",
        f"- formula_missing: {meta['formula_missing']}",
        f"- definition_missing: {meta['definition_missing']}",
        f"- example_missing: {meta['example_missing']}",
        f"- pitfall_missing: {meta['pitfall_missing']}",
        f"- has_conflict: {meta['has_conflict']}",
        f"- has_supplement: {meta['has_supplement']}",
        f"- source-supported formulas: {meta['formula_support']}",
        "",
        "## Flags",
        "",
    ]
    lines += [f"- {k}: {v}" for k, v in sorted(quality.items(), key=lambda x: -x[1])]
    (ROOT / "_quality_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
