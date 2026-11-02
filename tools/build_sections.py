# -*- coding: utf-8 -*-
"""Step 6 — build sections/parts and a coverage manifest.

Input : manifest.csv (distill=true) + clean/v1 + sections/{pages,headings}.jsonl
Output: data/sections/sections.jsonl      one row per part (with text)
        data/sections/coverage_manifest.json
        data/sections/section_report.md

Rules:
  - MD: heading blocks from headings.jsonl; preamble included; pack to 6k-12k chars
  - PDF: page blocks from pages.jsonl; pack to 6k-12k chars
  - section >12k -> split at paragraph boundary into <=8k parts, 200-char overlap
  - coverage is computed on non-whitespace, non-page-anchor characters
"""
from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path(r"D:\CyberMe\repo")
CLEAN = REPO / "data" / "clean" / "v1"
MANIFEST = REPO / "data" / "clean" / "manifest.csv"
SEC_DIR = REPO / "data" / "sections"
SEC_DIR.mkdir(parents=True, exist_ok=True)

PAGE_RE = re.compile(r"<!-- page: \d+ -->")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n\n?", re.S)
TARGET_MIN = 6000
TARGET_MAX = 12000
PART_MAX = 8000
OVERLAP = 200


def is_true(v) -> bool:
    return str(v).strip().lower() in ("true", "1", "yes")


def strip_fm(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def first_line(text: str) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s and not s.startswith("<!--"):
            return s[:80]
    return ""


def split_span(body: str, start: int, end: int, max_chars: int = PART_MAX, overlap: int = OVERLAP):
    text = body[start:end]
    if len(text) <= max_chars:
        return [(start, end)]
    spans = []
    pos = 0
    n = len(text)
    while pos < n:
        endpos = min(n, pos + max_chars)
        if endpos < n:
            cut = text.rfind("\n\n", pos + 2000, endpos)
            if cut > pos + 1000:
                endpos = cut
        spans.append((start + pos, start + endpos))
        if endpos >= n:
            break
        pos = max(pos + 1, endpos - overlap)
    return spans


def load_jsonl_by_source(path: Path, key: str = "source_id") -> dict[str, list[dict]]:
    out = defaultdict(list)
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        out[x.get(key, "")].append(x)
    return out


def main() -> None:
    rows = [r for r in csv.DictReader(MANIFEST.open(encoding="utf-8-sig")) if is_true(r.get("distill"))]
    heads = load_jsonl_by_source(SEC_DIR / "headings.jsonl")
    pages = load_jsonl_by_source(SEC_DIR / "pages.jsonl")
    print(f"distill files: {len(rows)}", flush=True)

    out_rows: list[dict] = []
    manifest: list[dict] = []

    for idx, r in enumerate(rows, 1):
        sid = r["source_id"]
        course = r["course"]
        text = (REPO / r["clean_path"]).read_text(encoding="utf-8")
        body = strip_fm(text)
        n = len(body)

        # build base blocks: (char_start, char_end, heading_path, page_start, page_end)
        blocks: list[tuple[int, int, list[str], int, int]] = []
        if int(float(r.get("pages") or 0)) > 0:
            plist = sorted(pages.get(sid, []), key=lambda x: x["page"])
            for p in plist:
                s, e = int(p["char_start"]), int(p["char_end"])
                if e <= s:
                    continue
                blocks.append((s, e, [first_line(body[s:e]) or f"第{p['page']}页"], int(p["page"]), int(p["page"])))
            if not blocks:
                blocks.append((0, n, [Path(r["rel"]).stem], 0, 0))
        else:
            hlist = sorted(heads.get(sid, []), key=lambda x: x["char_start"])
            if not hlist:
                blocks.append((0, n, [Path(r["rel"]).stem], 0, 0))
            else:
                if hlist[0]["char_start"] > 0:
                    blocks.append((0, int(hlist[0]["char_start"]), ["前言"], 0, 0))
                for i, h in enumerate(hlist):
                    s = int(h["char_start"])
                    e = int(hlist[i + 1]["char_start"]) if i + 1 < len(hlist) else n
                    if e > s:
                        blocks.append((s, e, list(h.get("heading_path") or [h.get("title", "")]), 0, 0))

        # pack blocks into sections 6k-12k
        sections = []
        cur: list[tuple[int, int, list[str], int, int]] = []
        cur_chars = 0
        for b in blocks:
            b_chars = b[1] - b[0]
            if cur and cur_chars + b_chars > TARGET_MAX and cur_chars >= TARGET_MIN:
                sections.append(cur)
                cur = []
                cur_chars = 0
            cur.append(b)
            cur_chars += b_chars
        if cur:
            sections.append(cur)

        parts_count = 0
        for s_idx, sec in enumerate(sections, 1):
            s_start = min(x[0] for x in sec)
            s_end = max(x[1] for x in sec)
            if s_end <= s_start:
                continue
            heading_path = sec[0][2]
            all_headings = []
            for x in sec:
                for h in x[2]:
                    if h and h not in all_headings:
                        all_headings.append(h)
            page_start = min((x[3] for x in sec if x[3] > 0), default=0)
            page_end = max((x[4] for x in sec if x[4] > 0), default=0)
            section_id = f"{sid}-SEC{s_idx:03d}"

            if s_end - s_start > TARGET_MAX:
                spans = split_span(body, s_start, s_end)
            else:
                spans = [(s_start, s_end)]
            for p_idx, (ps, pe) in enumerate(spans, 1):
                parts_count += 1
                page_map = []
                for b in sec:
                    bs = max(b[0], ps)
                    be = min(b[1], pe)
                    if be > bs and b[3] > 0:
                        page_map.append({
                            "page": b[3],
                            "char_start": bs - ps,
                            "char_end": be - ps,
                        })
                out_rows.append({
                    "part_id": f"{section_id}-P{p_idx:02d}",
                    "section_id": section_id,
                    "source_id": sid,
                    "course": course,
                    "heading_path": heading_path,
                    "headings": all_headings,
                    "char_start": ps,
                    "char_end": pe,
                    "chars": pe - ps,
                    "page_start": page_start,
                    "page_end": page_end,
                    "page_map": page_map,
                    "locator_kind": "page" if page_start else "section",
                    "part_index": p_idx,
                    "parts_total": len(spans),
                    "text": body[ps:pe],
                })

        # coverage on non-whitespace, non-anchor chars
        covered = bytearray(n)
        for x in out_rows:
            if x["source_id"] != sid:
                continue
            for i in range(x["char_start"], x["char_end"]):
                covered[i] = 1
        anchor_mask = bytearray(n)
        for m in PAGE_RE.finditer(body):
            for i in range(m.start(), m.end()):
                anchor_mask[i] = 1
        content_total = 0
        uncovered = 0
        gap_ranges = []
        in_gap = False
        gs = 0
        for i, ch in enumerate(body):
            if ch.isspace() or anchor_mask[i]:
                continue
            content_total += 1
            if not covered[i]:
                uncovered += 1
                if not in_gap:
                    in_gap = True
                    gs = i
            elif in_gap:
                gap_ranges.append([gs, i])
                in_gap = False
        if in_gap:
            gap_ranges.append([gs, n])
        coverage = 1 - uncovered / content_total if content_total else 1.0
        manifest.append({
            "source_id": sid,
            "course": course,
            "rel": r["rel"],
            "sections": len(sections),
            "parts": parts_count,
            "chars_total": n,
            "content_chars": content_total,
            "uncovered_content": uncovered,
            "coverage": round(coverage, 6),
            "gaps": gap_ranges[:10],
        })

        if idx % 50 == 0:
            print(f"  {idx}/{len(rows)}", flush=True)

    # write sections.jsonl
    with (SEC_DIR / "sections.jsonl").open("w", encoding="utf-8") as f:
        for x in out_rows:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    (SEC_DIR / "coverage_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # report
    covs = [x["coverage"] for x in manifest]
    gaps = [x for x in manifest if x["uncovered_content"] > 0]
    by_course = defaultdict(lambda: {"files": 0, "sections": 0, "parts": 0, "chars": 0})
    for x in manifest:
        c = by_course[x["course"]]
        c["files"] += 1
        c["sections"] += x["sections"]
        c["parts"] += x["parts"]
        c["chars"] += x["chars_total"]
    lines = [
        "# Step 6 — Section & coverage report",
        "",
        f"- distill files: {len(rows)}",
        f"- sections: {sum(x['sections'] for x in manifest)}",
        f"- parts: {len(out_rows)}",
        f"- chars in parts: {sum(x['chars'] for x in out_rows):,}",
        f"- coverage min / median: {min(covs):.6f} / {sorted(covs)[len(covs)//2]:.6f}",
        f"- files with uncovered content: {len(gaps)}",
        "",
        "## By course",
        "",
        "| course | files | sections | parts | chars |",
        "|---|---:|---:|---:|---:|",
    ]
    for c in sorted(by_course, key=lambda k: -by_course[k]["chars"]):
        d = by_course[c]
        lines.append(f"| {c} | {d['files']} | {d['sections']} | {d['parts']} | {d['chars']:,} |")
    if gaps:
        lines += ["", "## Files with gaps", "", "| course | source | coverage | uncovered | gaps |", "|---|---|---:|---:|---|"]
        for x in sorted(gaps, key=lambda y: y["coverage"])[:30]:
            lines.append(f"| {x['course']} | {x['source_id']} | {x['coverage']:.4f} | {x['uncovered_content']} | {x['gaps'][:3]} |")
    (SEC_DIR / "section_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "distill_files": len(rows),
        "sections": sum(x["sections"] for x in manifest),
        "parts": len(out_rows),
        "chars": sum(x["chars"] for x in out_rows),
        "coverage_min": min(covs),
        "coverage_median": sorted(covs)[len(covs)//2],
        "files_with_gaps": len(gaps),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
