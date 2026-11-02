# -*- coding: utf-8 -*-
"""Step 3 — normalize extracted text and build page/section indexes.

Input : data/clean/v1/{course}/{source_id}.md  (Step 2 output)
Backup: data/clean/v1_raw/                    (copy of Step 2 output)
Output: data/clean/v1/                        (normalized, overwritten)
        data/sections/pages.jsonl             (PDF page index)
        data/sections/headings.jsonl          (MD heading/section index)
        data/clean/normalization_report.md
"""
from __future__ import annotations

import csv
import json
import math
import re
import shutil
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import yaml

REPO = Path(r"D:\CyberMe\repo")
CLEAN = REPO / "data" / "clean" / "v1"
BACKUP = REPO / "data" / "clean" / "v1_raw"
MANIFEST = REPO / "data" / "clean" / "manifest.csv"
SECTIONS = REPO / "data" / "sections"
SECTIONS.mkdir(parents=True, exist_ok=True)

PAGE_RE = re.compile(r"<!-- page: (\d+) -->")
PAGENUM_RES = [
    re.compile(r"^\d{1,3}$"),
    re.compile(r"^第\s*\d+\s*页(\s*共\s*\d+\s*页)?$"),
    re.compile(r"^【\s*第\s*\d+\s*页.*】$"),
    re.compile(r"^-\s*\d+\s*-$"),
    re.compile(r"^\d+\s*/\s*\d+$"),
    re.compile(r"^Page\s*\d+(\s*of\s*\d+)?$", re.I),
]
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n\n?", re.S)
SENTENCE_END = ("。", "；", "，", "！", "？", ".", ";", ",")


def is_page_number(s: str) -> bool:
    return any(r.match(s) for r in PAGENUM_RES)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_pages(body: str) -> list[tuple[int | None, str]]:
    matches = list(PAGE_RE.finditer(body))
    if not matches:
        return [(None, body)]
    pages = []
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        pages.append((int(m.group(1)), body[start:end]))
    return pages


def header_candidate(s: str) -> bool:
    if not (0 < len(s) <= 60):
        return False
    if is_page_number(s):
        return False
    if s.endswith(SENTENCE_END):
        return False
    if re.match(r"^(例|解|证明|答|注|定义|定理|设|已|由|则|所以|其中|图|表)", s):
        return False
    if not re.search(r"[\u4e00-\u9fffA-Za-z]", s):
        return False
    return True


def detect_repeated_headers(pages: list[tuple[int | None, str]]) -> set[str]:
    """Only consider the first/last 3 non-empty lines; require >=70% of pages.

    This avoids deleting repeated body lines in the middle of a page.
    """
    n = len(pages)
    if n < 4:
        return set()
    top_counts = Counter()
    bottom_counts = Counter()
    for _, text in pages:
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        for s in lines[:3]:
            if header_candidate(s):
                top_counts[s] += 1
        for s in lines[-3:]:
            if header_candidate(s):
                bottom_counts[s] += 1
    threshold = max(3, math.ceil(n * 0.7))
    headers = {s for s, c in top_counts.items() if c >= threshold}
    headers |= {s for s, c in bottom_counts.items() if c >= threshold}
    return headers


def clean_page_text(text: str, headers: set[str], protect: bool = True) -> tuple[str, int, int]:
    """Remove repeated headers/footers and page numbers only in top/bottom zones."""
    lines = text.split("\n")
    nonempty = [i for i, line in enumerate(lines) if line.strip()]
    top = set(nonempty[:3])
    bottom = set(nonempty[-3:])
    zone = top | bottom

    out: list[str] = []
    removed_headers = 0
    removed_pagenums = 0
    in_code = False
    in_math = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if s.startswith("$$"):
            in_math = not in_math
            out.append(line)
            continue
        if protect and (in_code or in_math or s.startswith("|")):
            out.append(line)
            continue
        if i in zone and is_page_number(s):
            removed_pagenums += 1
            continue
        if i in zone and s and s in headers:
            removed_headers += 1
            continue
        out.append(line)
    return "\n".join(out), removed_headers, removed_pagenums


def parse_clean_file(p: Path) -> tuple[dict, str]:
    text = p.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, text[m.end():]


def write_clean_file(p: Path, fm: dict, body: str) -> None:
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    p.write_text(f"---\n{fm_text}\n---\n\n{body}", encoding="utf-8")


def build_md_sections(source_id: str, body: str, fallback_title: str) -> list[dict]:
    lines = body.split("\n")
    # char offsets per line
    offsets = []
    pos = 0
    for line in lines:
        offsets.append(pos)
        pos += len(line) + 1

    heads = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))

    if not heads:
        return [{
            "section_id": f"{source_id}-S001",
            "source_id": source_id,
            "level": 1,
            "title": fallback_title,
            "heading_path": [fallback_title],
            "line_start": 1,
            "line_end": len(lines),
            "char_start": 0,
            "char_end": len(body),
            "locator_kind": "section",
        }]

    # determine end of each heading: next heading with level <= current, or EOF
    sections = []
    stack: list[tuple[int, str]] = []
    for idx, (line_no, level, title) in enumerate(heads):
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        path = [t for _, t in stack]
        char_start = offsets[line_no]
        char_end = len(body)
        for j in range(idx + 1, len(heads)):
            if heads[j][1] <= level:
                char_end = offsets[heads[j][0]]
                break
        sections.append({
            "section_id": f"{source_id}-S{idx + 1:03d}",
            "source_id": source_id,
            "level": level,
            "title": title,
            "heading_path": path,
            "line_start": line_no + 1,
            "line_end": body[:char_end].count("\n") + 1,
            "char_start": char_start,
            "char_end": char_end,
            "locator_kind": "section",
        })
    return sections


def main() -> None:
    # idempotent: always start from the pristine Step 2 backup
    if BACKUP.exists():
        shutil.rmtree(CLEAN)
        shutil.copytree(BACKUP, CLEAN)
    else:
        shutil.copytree(CLEAN, BACKUP)
    print(f"raw backup: {BACKUP}", flush=True)

    manifest = list(csv.DictReader(MANIFEST.open(encoding="utf-8-sig")))
    by_id = {r["source_id"]: r for r in manifest}

    page_index: list[dict] = []
    heading_index: list[dict] = []
    report_rows: list[dict] = []
    failures: list[dict] = []

    for i, r in enumerate(manifest, 1):
        sid = r["source_id"]
        p = REPO / r["clean_path"]
        try:
            fm, body = parse_clean_file(p)
            chars_before = len(re.sub(r"<!-- page: \d+ -->\n?", "", body))
            before_ns = len(re.sub(r"\s", "", re.sub(r"<!-- page: \d+ -->\n?", "", body)))

            if r["doc_type"] == "slides" or int(float(r["pages"] or 0)) > 0:
                pages = split_pages(body)
                headers = detect_repeated_headers(pages)
                new_pages = []
                removed_h = removed_pn = 0
                for num, text in pages:
                    cleaned, rh, rp = clean_page_text(text, headers)
                    removed_h += rh
                    removed_pn += rp
                    new_pages.append((num, normalize_text(cleaned)))
                body_norm = "\n\n".join(
                    f"<!-- page: {num} -->\n\n{text}" if num is not None else text
                    for num, text in new_pages
                ).strip() + "\n"
                # page index
                page_matches = list(PAGE_RE.finditer(body_norm))
                for j, m in enumerate(page_matches):
                    end = page_matches[j + 1].start() if j + 1 < len(page_matches) else len(body_norm)
                    page_index.append({
                        "source_id": sid,
                        "course": r["course"],
                        "page": int(m.group(1)),
                        "char_start": m.end(),
                        "char_end": end,
                        "locator_kind": "page",
                    })
            else:
                body_norm = normalize_text(body) + "\n"
                removed_h = removed_pn = 0
                secs = build_md_sections(sid, body_norm, r["rel"].split("/")[-1].removesuffix(".md"))
                heading_index.extend([{"course": r["course"], **s} for s in secs])

            after_ns = len(re.sub(r"\s", "", re.sub(r"<!-- page: \d+ -->\n?", "", body_norm)))
            ratio_ns = round(after_ns / before_ns, 4) if before_ns else 1.0
            chars_after = len(re.sub(r"<!-- page: \d+ -->\n?", "", body_norm))
            anchors_before = len(PAGE_RE.findall(body))
            anchors_after = len(PAGE_RE.findall(body_norm))
            if anchors_before != anchors_after:
                raise ValueError(f"page anchors changed: {anchors_before} -> {anchors_after}")

            raw_flags = fm.get("flags") or []
            if isinstance(raw_flags, list):
                flags = [str(x) for x in raw_flags if x]
            elif isinstance(raw_flags, str):
                flags = [x for x in raw_flags.split(";") if x]
            else:
                flags = []
            if ratio_ns < 0.95:
                flags.append("normalization_loss")
            if removed_h:
                flags.append("header_cleaned")
            if removed_pn:
                flags.append("pagenum_cleaned")
            dot_ratio = body_norm.count("....") / max(1, len(body_norm))
            private_ratio = len(re.findall(r"[\ue000-\uf8ff]", body_norm)) / max(1, len(body_norm))
            if int(float(r["pages"] or 0)) > 0 and (
                after_ns < 500 or (ratio_ns < 0.5 and after_ns < 2000)
            ):
                flags.append("low_content")
            if private_ratio > 0.005:
                flags.append("private_use_chars")
            flags = sorted(set(flags))

            fm.update({
                "chars": chars_after,
                "normalized": True,
                "normalized_at": datetime.now(timezone.utc).isoformat(),
                "removed_header_lines": removed_h,
                "removed_page_numbers": removed_pn,
                "flags": flags,
            })
            write_clean_file(p, fm, body_norm)

            rec = {
                "source_id": sid,
                "course": r["course"],
                "chars_before": chars_before,
                "chars_after": chars_after,
                "before_ns": before_ns,
                "after_ns": after_ns,
                "ratio_ns": ratio_ns,
                "removed_header_lines": removed_h,
                "removed_page_numbers": removed_pn,
                "pages": int(float(r["pages"] or 0)),
                "sections": len(build_md_sections(sid, body_norm, "")) if int(float(r["pages"] or 0)) == 0 else 0,
                "flags": flags,
            }
            report_rows.append(rec)
            by_id[sid].update({
                "chars_norm": chars_after,
                "ratio_norm": ratio_ns,
                "removed_header_lines": removed_h,
                "removed_page_numbers": removed_pn,
                "sections": rec["sections"],
                "flags": ";".join(flags),
            })
        except Exception as e:
            failures.append({"source_id": sid, "course": r["course"], "rel": r["rel"], "error": str(e)})

        if i % 50 == 0:
            print(f"  {i}/{len(manifest)}", flush=True)

    # write indexes
    with (SECTIONS / "pages.jsonl").open("w", encoding="utf-8") as f:
        for x in page_index:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    with (SECTIONS / "headings.jsonl").open("w", encoding="utf-8") as f:
        for x in heading_index:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")

    # manifest
    fields = list(manifest[0].keys())
    for extra in ("chars_norm", "ratio_norm", "removed_header_lines", "removed_page_numbers", "sections"):
        if extra not in fields:
            fields.append(extra)
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(manifest)

    # report
    ratios = [x["ratio_ns"] for x in report_rows]
    total_removed_h = sum(x["removed_header_lines"] for x in report_rows)
    total_removed_pn = sum(x["removed_page_numbers"] for x in report_rows)
    loss = [x for x in report_rows if x["ratio_ns"] < 0.95]
    low_content = [x for x in report_rows if "low_content" in x.get("flags", [])]
    private_use = [x for x in report_rows if "private_use_chars" in x.get("flags", [])]
    lines = [
        "# Step 3 — Normalization report",
        "",
        f"- files normalized: {len(report_rows)} / {len(manifest)}",
        f"- failures: {len(failures)}",
        f"- pages indexed: {len(page_index):,}",
        f"- MD sections indexed: {len(heading_index):,}",
        f"- removed header lines: {total_removed_h:,}",
        f"- removed page-number lines: {total_removed_pn:,}",
        f"- retention min/median: {min(ratios) if ratios else 1.0} / {sorted(ratios)[len(ratios)//2] if ratios else 1.0}",
        f"- files with retention <95%: {len(loss)}",
        f"- low-content files (TOC/image-only): {len(low_content)}",
        f"- files with private-use font chars: {len(private_use)}",
        "",
        "## Files with retention <95%",
        "",
    ]
    if loss:
        lines += ["| course | source | rel | before_ns | after_ns | ratio | removed_h | removed_pn |",
                  "|---|---|---|---:|---:|---:|---:|---:|"]
        for x in sorted(loss, key=lambda y: y["ratio_ns"])[:20]:
            lines.append(f"| {x['course']} | {x['source_id']} | {by_id[x['source_id']]['rel']} | "
                         f"{x['before_ns']} | {x['after_ns']} | {x['ratio_ns']} | "
                         f"{x['removed_header_lines']} | {x['removed_page_numbers']} |")
    else:
        lines.append("None.")
    if low_content:
        lines += ["", "## Low-content files (quarantine candidates)", "",
                  "| course | source | rel | after_ns | ratio | flags |",
                  "|---|---|---|---:|---:|---|"]
        for x in sorted(low_content, key=lambda y: y["after_ns"])[:30]:
            lines.append(f"| {x['course']} | {x['source_id']} | {by_id[x['source_id']]['rel']} | "
                         f"{x['after_ns']} | {x['ratio_ns']} | {';'.join(x['flags'])} |")
    if failures:
        lines += ["", "## Failures", ""]
        for x in failures:
            lines.append(f"- {x['course']} {x['rel']}: {x['error']}")
    (REPO / "data" / "clean" / "normalization_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "files": len(report_rows),
        "failures": len(failures),
        "pages_indexed": len(page_index),
        "sections_indexed": len(heading_index),
        "removed_headers": total_removed_h,
        "removed_pagenums": total_removed_pn,
        "retention_min": min(ratios) if ratios else 1.0,
        "loss_files": len(loss),
        "low_content": len(low_content),
        "private_use": len(private_use),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
