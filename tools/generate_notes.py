# -*- coding: utf-8 -*-
"""Step 9 — generate Vault-ready Markdown notes from topics.

Input : data/topics/*.jsonl + data/clean/manifest.csv + existing Vault notes
Output: data/notes/{course}/{note_id}.md
        data/notes/_manifest.csv
        data/notes/_index.jsonl
        data/notes/_merge_suggestions.csv
        data/notes/_review_sample.csv
        data/notes/note_quality_report.md

Notes are proposals only: they are NOT written into Vault.
"""
from __future__ import annotations

import csv
import difflib
import json
import random
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

REPO = Path(r"D:\CyberMe\repo")
TOPICS = REPO / "data" / "topics"
MANIFEST = REPO / "data" / "clean" / "manifest.csv"
OUT = REPO / "data" / "notes"
OUT.mkdir(parents=True, exist_ok=True)
VAULT = REPO / "Vault"

PAGE_RE = re.compile(r"<!-- page: \d+ -->")


def norm_title(t: str) -> str:
    t = re.sub(r"[（(].*?[)）]", "", str(t))
    t = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]+", "", t)
    return t.lower()


def first_sentence(s: str) -> str:
    s = (s or "").strip()
    if not s:
        return ""
    m = re.split(r"(?<=[。！？.!?])", s, maxsplit=1)
    return m[0].strip()


def merge_sources(sources: list[dict]) -> list[dict]:
    """Deduplicate by source_id, merging page ranges."""
    out = {}
    for s in sources:
        sid = s.get("source_id", "")
        if not sid:
            continue
        ps = int(s.get("page_start") or 0)
        pe = int(s.get("page_end") or 0)
        sec = s.get("section_id", "")
        if sid not in out:
            out[sid] = {"source_id": sid, "page_start": ps, "page_end": pe, "section_id": sec}
        else:
            o = out[sid]
            if ps > 0:
                o["page_start"] = min(o["page_start"], ps) if o["page_start"] > 0 else ps
                o["page_end"] = max(o["page_end"], pe)
            if sec and not o.get("section_id"):
                o["section_id"] = sec
    return list(out.values())


def cite(sources: list[dict]) -> str:
    parts = []
    for s in sources:
        sid = s.get("source_id", "")
        ps = int(s.get("page_start") or 0)
        pe = int(s.get("page_end") or 0)
        sec = s.get("section_id", "")
        if ps > 0:
            if pe and pe != ps:
                parts.append(f"{sid} p.{ps}–{pe}")
            else:
                parts.append(f"{sid} p.{ps}")
        elif sec:
            parts.append(f"{sid} §{sec}")
        elif sid:
            parts.append(sid)
    return "；".join(dict.fromkeys(parts))


def build_note(row: dict, note_id: str, hash_map: dict[str, str], today: str,
               formula_missing: bool = False) -> tuple[str, dict]:
    t = row["topic"]
    sources = merge_sources(t.get("sources") or [])
    c = cite(sources)
    title = t.get("title") or row.get("section_id") or "未命名主题"
    course = row["course"]
    heading_path = row.get("heading_path") or []
    chapter = heading_path[0] if heading_path else row.get("section_id", "")

    lines = [f"# {title}", ""]
    summary = t.get("summary") or ""
    one = first_sentence(summary) or summary
    if one:
        lines += ["## 一句话", one, ""]

    definition = (t.get("definition") or "").strip()
    if definition:
        lines += ["## 定义", f"{definition}（来源：{c}）" if c else definition, ""]

    kps = t.get("key_points") or []
    if kps:
        lines += ["## 关键点", ""]
        for i, kp in enumerate(kps, 1):
            suffix = f"（来源：{c}）" if c else ""
            lines.append(f"{i}. {kp}{suffix}")
        lines.append("")

    formulas = t.get("formulas") or []
    if formulas:
        lines += ["## 公式", ""]
        if formula_missing:
            lines += ["> ⚠️ 本节部分公式/变量在原文中缺失，未补写；引用时请回原文核对。", ""]
        for f in formulas:
            formula = f.get("formula") or ""
            meaning = f.get("meaning") or ""
            suffix = f"（来源：{c}）" if c else ""
            missing = " ⚠️原文公式/变量缺失" if f.get("formula_missing") else ""
            lines.append(f"- `{formula}`：{meaning}{missing}{suffix}")
        lines.append("")

    examples = t.get("examples") or []
    if examples:
        lines += ["## 例子", ""]
        for ex in examples:
            lines.append(f"- {ex}" + (f"（来源：{c}）" if c else ""))
        lines.append("")

    pitfalls = t.get("pitfalls") or []
    if pitfalls:
        lines += ["## 易错点", ""]
        for p in pitfalls:
            lines.append(f"- {p}" + (f"（来源：{c}）" if c else ""))
        lines.append("")

    relations = t.get("relations") or []
    if relations:
        lines += ["## 关系", ""]
        for rel in relations:
            typ = rel.get("type", "related_to")
            target = rel.get("target", "")
            if target:
                lines.append(f"- {typ}：{target}")
        lines.append("")

    conflicts = t.get("conflicts") or []
    if conflicts:
        lines += ["## 冲突", ""]
        for x in conflicts:
            lines.append(f"- {x}" + (f"（来源：{c}）" if c else ""))
        lines.append("")

    lines += ["## 来源", ""]
    for s in sources:
        sid = s.get("source_id", "")
        ps = int(s.get("page_start") or 0)
        pe = int(s.get("page_end") or 0)
        sec = s.get("section_id", "")
        if ps > 0:
            loc = f"p.{ps}–{pe}" if pe and pe != ps else f"p.{ps}"
        elif sec:
            loc = f"§{sec}"
        else:
            loc = ""
        lines.append(f"- [[{sid}]] {loc}".strip())
    lines.append("")

    fm_sources = []
    for s in sources:
        item = {"source_id": s.get("source_id", "")}
        ps = int(s.get("page_start") or 0)
        pe = int(s.get("page_end") or 0)
        if ps > 0:
            item["source_pages"] = [ps, pe or ps]
        if s.get("section_id"):
            item["section_id"] = s["section_id"]
        h = hash_map.get(item["source_id"])
        if h:
            item["source_hash"] = h
        fm_sources.append(item)

    tags = [course]
    for h in heading_path[:2]:
        if h and h not in tags:
            tags.append(h)
    tags = tags[:5]

    fm = {
        "schema_version": 2,
        "id": note_id,
        "topic_id": row.get("topic_id", ""),
        "type": "concept",
        "status": "distilled",
        "course": course,
        "chapter": chapter,
        "title": title,
        "aliases": t.get("aliases") or [],
        "source": fm_sources,
        "verification": "inferred",
        "needs_review": True,
        "confidence": t.get("confidence", 0.8),
        "tags": tags,
        "unit_count": row.get("unit_count", 0),
        "created": today,
        "updated": today,
    }
    import yaml
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    body = "\n".join(lines)
    return f"---\n{fm_text}\n---\n\n{body}", fm


def existing_notes() -> list[dict]:
    out = []
    for p in VAULT.glob("20_University/*/02_知识点/*.md"):
        out.append({"title": p.stem, "path": str(p.relative_to(REPO)).replace("\\", "/")})
    return out


def main() -> None:
    today = date.today().isoformat()
    rows = []
    for p in sorted(TOPICS.glob("*.jsonl")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    rows.sort(key=lambda r: (r["course"], r["topic_id"]))
    print(f"topics: {len(rows)}", flush=True)

    manifest = list(csv.DictReader(MANIFEST.open(encoding="utf-8-sig")))
    hash_map = {r["source_id"]: r.get("sha256", "") for r in manifest}
    unit_map = {}
    for p in (REPO / "data" / "units").glob("*/*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        r = d.get("result", {})
        if not r.get("has_knowledge"):
            continue
        for i, u in enumerate(r.get("units", []), 1):
            unit_map[f"{d['part_id']}-U{i:02d}"] = u
    old = existing_notes()
    print(f"existing Vault notes: {len(old)}", flush=True)

    counters = defaultdict(int)
    index_rows = []
    manifest_rows = []
    merge_rows = []
    for r in rows:
        course = r["course"]
        counters[course] += 1
        note_id = f"{course}-TOPIC-{counters[course]:03d}"
        formula_missing = any(unit_map.get(uid, {}).get("formula_missing") for uid in r.get("unit_ids", []))
        text, fm = build_note(r, note_id, hash_map, today, formula_missing=formula_missing)
        course_dir = OUT / course
        course_dir.mkdir(parents=True, exist_ok=True)
        path = course_dir / f"{note_id}.md"
        path.write_text(text, encoding="utf-8")

        t = r["topic"]
        flags = []
        if not fm["source"]:
            flags.append("no_source")
        if not t.get("key_points"):
            flags.append("no_key_points")
        if not t.get("definition"):
            flags.append("no_definition")
        if t.get("conflicts"):
            flags.append("has_conflict")
        if float(fm.get("confidence") or 0) < 0.6:
            flags.append("low_confidence")
        if any(f.get("formula_missing") for f in (t.get("formulas") or [])):
            flags.append("formula_missing")
        if formula_missing:
            flags.append("formula_missing")

        rel_path = str(path.relative_to(REPO)).replace("\\", "/")
        index_rows.append({
            "note_id": note_id,
            "topic_id": r["topic_id"],
            "course": course,
            "title": fm["title"],
            "path": rel_path,
            "sources": fm["source"],
            "key_points": len(t.get("key_points") or []),
            "formulas": len(t.get("formulas") or []),
            "conflicts": len(t.get("conflicts") or []),
            "confidence": fm["confidence"],
            "verification": "inferred",
            "status": "distilled",
        })
        manifest_rows.append({
            "note_id": note_id,
            "topic_id": r["topic_id"],
            "course": course,
            "title": fm["title"],
            "path": rel_path,
            "source_count": len(fm["source"]),
            "key_points": len(t.get("key_points") or []),
            "formulas": len(t.get("formulas") or []),
            "conflicts": len(t.get("conflicts") or []),
            "confidence": fm["confidence"],
            "flags": ";".join(flags),
        })

        # merge suggestion against existing Vault notes
        best = None
        nt = norm_title(fm["title"])
        for o in old:
            ratio = difflib.SequenceMatcher(None, nt, norm_title(o["title"])).ratio()
            if best is None or ratio > best[0]:
                best = (ratio, o)
        if best and best[0] >= 0.75:
            action = "duplicate" if best[0] >= 0.95 else "supplement"
            merge_rows.append({
                "note_id": note_id,
                "course": course,
                "new_title": fm["title"],
                "existing_title": best[1]["title"],
                "existing_path": best[1]["path"],
                "similarity": round(best[0], 4),
                "action": action,
            })
        else:
            merge_rows.append({
                "note_id": note_id,
                "course": course,
                "new_title": fm["title"],
                "existing_title": "",
                "existing_path": "",
                "similarity": "",
                "action": "new",
            })

    # write manifest / index
    with (OUT / "_manifest.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()))
        w.writeheader()
        w.writerows(manifest_rows)
    with (OUT / "_index.jsonl").open("w", encoding="utf-8") as f:
        for x in index_rows:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

    # merge suggestions
    with (OUT / "_merge_suggestions.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["note_id", "course", "new_title", "existing_title", "existing_path", "similarity", "action"])
        w.writeheader()
        w.writerows(merge_rows)

    # review sample: 10%, stratified by course
    random.seed(42)
    by_course = defaultdict(list)
    for x in index_rows:
        by_course[x["course"]].append(x)
    sample = []
    for course, items in by_course.items():
        k = max(1, round(len(items) * 0.10))
        sample.extend(random.sample(items, min(k, len(items))))
    with (OUT / "_review_sample.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["note_id", "course", "title", "path", "sources", "key_points", "formulas", "conflicts", "confidence"])
        for x in sample:
            w.writerow([x["note_id"], x["course"], x["title"], x["path"],
                        json.dumps(x["sources"], ensure_ascii=False), x["key_points"],
                        x["formulas"], x["conflicts"], x["confidence"]])

    # quality report
    no_source = [x for x in manifest_rows if x["source_count"] == 0]
    no_kp = [x for x in manifest_rows if x["key_points"] == 0]
    empty_title = [x for x in manifest_rows if not x["title"].strip()]
    low_conf = [x for x in manifest_rows if float(x["confidence"]) < 0.6]
    conflict = [x for x in manifest_rows if x["conflicts"] > 0]
    conflict_items = sum(int(x["conflicts"]) for x in manifest_rows)
    formula_missing = [x for x in manifest_rows if "formula_missing" in x["flags"]]
    dup = [x for x in merge_rows if x["action"] == "duplicate"]
    supp = [x for x in merge_rows if x["action"] == "supplement"]
    lines = [
        "# Step 9 — Note quality report",
        "",
        f"- topics: {len(rows)}",
        f"- notes generated: {len(manifest_rows)}",
        f"- review sample: {len(sample)} (10%)",
        f"- no source: {len(no_source)}",
        f"- no key points: {len(no_kp)}",
        f"- empty title: {len(empty_title)}",
        f"- low confidence (<0.6): {len(low_conf)}",
        f"- notes with conflicts: {len(conflict)}",
        f"- conflict items: {conflict_items}",
        f"- notes with formula_missing: {len(formula_missing)}",
        f"- merge suggestions: duplicate={len(dup)}, supplement={len(supp)}, new={len(merge_rows)-len(dup)-len(supp)}",
        "",
        "## By course",
        "",
        "| course | notes |",
        "|---|---:|",
    ]
    c = Counter(x["course"] for x in manifest_rows)
    for k in sorted(c):
        lines.append(f"| {k} | {c[k]} |")
    lines += ["", "## Gates", ""]
    gates = [
        ("100% notes have source", len(no_source) == 0),
        ("100% notes have key points", len(no_kp) == 0),
        ("0 empty titles", len(empty_title) == 0),
        ("conflicts preserved", conflict_items == 4),
        ("review sample generated", len(sample) > 0),
    ]
    for name, ok in gates:
        lines.append(f"- {'✅' if ok else '❌'} {name}")
    if no_source or no_kp or empty_title:
        lines += ["", "## Failing notes", ""]
        for x in (no_source + no_kp + empty_title)[:50]:
            lines.append(f"- {x['note_id']} {x['title']}: {x['flags']}")
    (OUT / "note_quality_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "topics": len(rows),
        "notes": len(manifest_rows),
        "review_sample": len(sample),
        "no_source": len(no_source),
        "no_kp": len(no_kp),
        "empty_title": len(empty_title),
        "conflicts": len(conflict),
        "formula_missing": len(formula_missing),
        "duplicate_suggestions": len(dup),
        "supplement_suggestions": len(supp),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
