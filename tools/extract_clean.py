# -*- coding: utf-8 -*-
"""Step 2 — extract full text from included PDF/Markdown into data/clean/v1.

Rules:
  - PDF: PyMuPDF, page by page, block order by (y, x); insert <!-- page: N -->
  - MD: read with utf-8-sig/utf-8/gb18030; strip old frontmatter; keep body whole
  - no truncation anywhere
  - write one .md per source with a metadata frontmatter
  - manifest.csv + extraction_report.md + failed.csv

Input : data/registry/included.csv
Output: data/clean/v1/{COURSE}/{source_id}.md
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import time
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import fitz
import yaml

REPO = Path(r"D:\CyberMe\repo")
REG = REPO / "data" / "registry"
OUT = REPO / "data" / "clean" / "v1"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True, exist_ok=True)


def read_md(p: Path) -> str:
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return p.read_text(encoding=enc)
        except UnicodeDecodeError:
            continue
    return p.read_text(encoding="utf-8", errors="replace")


def strip_frontmatter(text: str) -> tuple[str, bool]:
    if not text.startswith("---"):
        return text, False
    nl = text.find("\n")
    if nl < 0:
        return text, False
    rest = text[nl + 1:]
    m = re.search(r"^---\s*$", rest, re.MULTILINE)
    if not m:
        return text, False
    return rest[m.end():].lstrip("\n"), True


def pdf_body(p: Path) -> tuple[str, dict]:
    d = fitz.open(p)
    pages = d.page_count
    parts: list[str] = []
    texts: list[str] = []
    empty_pages = 0
    for i in range(pages):
        page = d[i]
        try:
            blocks = page.get_text("blocks")
            blocks.sort(key=lambda b: (round(b[1], 1), b[0]))
            text = "\n".join((b[4] or "").rstrip() for b in blocks).strip()
        except Exception:
            text = page.get_text("text").strip()
        if not text:
            empty_pages += 1
        texts.append(text)
        parts.append(f"<!-- page: {i + 1} -->\n\n{text}")
    d.close()
    body = "\n\n".join(parts).strip() + "\n"
    raw_ns = len(re.sub(r"\s", "", "\n".join(texts)))
    return body, {"pages": pages, "empty_pages": empty_pages, "raw_chars_ns": raw_ns}


def md_body(p: Path) -> tuple[str, dict]:
    raw = read_md(p)
    body, had_fm = strip_frontmatter(raw)
    return body, {"pages": 0, "empty_pages": 0, "had_frontmatter": had_fm,
                  "raw_chars_ns": len(re.sub(r"\s", "", body))}


def main() -> None:
    rows = list(csv.DictReader((REG / "included.csv").open(encoding="utf-8-sig")))
    rows.sort(key=lambda r: (r["course"], r["rel"]))
    print(f"extracting {len(rows)} files -> {OUT}", flush=True)

    registry: list[dict] = []
    failed: list[dict] = []
    t0 = time.time()
    for idx, r in enumerate(rows, 1):
        course = r["course"]
        source_id = f"SRC-{course}-{idx:03d}"
        rel = r["rel"]
        p = Path(r["path"])
        out_dir = OUT / course
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f"{source_id}.md"

        try:
            if r["ext"] == ".pdf":
                body, extra = pdf_body(p)
                locator_kind = "page"
                extractor = "pymupdf"
            else:
                body, extra = md_body(p)
                locator_kind = "section"
                extractor = "markdown"

            chars_raw = int(float(r.get("chars") or 0))
            body_text = re.sub(r"<!-- page: \d+ -->\n?", "", body)
            chars_body = len(body_text)
            chars_clean_ns = len(re.sub(r"\s", "", body_text))
            chars_raw_ns = int(extra.get("raw_chars_ns") or 0)
            ratio_ns = round(chars_clean_ns / chars_raw_ns, 4) if chars_raw_ns else 1.0
            ratio = round(chars_body / chars_raw, 4) if chars_raw else 1.0
            anchors = len(re.findall(r"<!-- page: \d+ -->", body))
            flags = []
            if r.get("flags"):
                flags.extend([x for x in r["flags"].split(";") if x])
            if extra.get("pages") and extra["empty_pages"] / extra["pages"] > 0.5:
                flags.append("mostly_empty_pages")
            if ratio_ns < 0.98:
                flags.append("char_loss")
            if chars_body < 1000:
                flags.append("short")
            if r["ext"] == ".md" and not re.search(r"^#{1,6}\s+", body, re.M):
                flags.append("no_headings")
            flags = sorted(set(flags))

            meta = {
                "source_id": source_id,
                "course": course,
                "doc_type": r["doc_type"],
                "original_path": rel,
                "sha256": r.get("sha256", ""),
                "pages": extra.get("pages", 0),
                "chars": chars_body,
                "locator_kind": locator_kind,
                "extractor": extractor,
                "extracted_at": datetime.now(timezone.utc).isoformat(),
                "flags": flags,
            }
            fm = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
            out_path.write_text(f"---\n{fm}\n---\n\n{body}", encoding="utf-8")

            registry.append({
                "source_id": source_id,
                "course": course,
                "doc_type": r["doc_type"],
                "rel": rel,
                "clean_path": str(out_path.relative_to(REPO)).replace("\\", "/"),
                "pages": extra.get("pages", 0),
                "empty_pages": extra.get("empty_pages", 0),
                "chars_raw": chars_raw,
                "chars_clean": chars_body,
                "ratio": ratio,
                "chars_raw_ns": chars_raw_ns,
                "chars_clean_ns": chars_clean_ns,
                "ratio_ns": ratio_ns,
                "anchors": anchors,
                "sha256": r.get("sha256", ""),
                "flags": ";".join(flags),
            })
        except Exception as e:
            failed.append({"rel": rel, "course": course, "error": f"{e}", "trace": traceback.format_exc()[-800:]})

        if idx % 50 == 0:
            print(f"  {idx}/{len(rows)}  {time.time() - t0:.0f}s", flush=True)

    # manifest
    fields = ["source_id", "course", "doc_type", "rel", "clean_path", "pages", "empty_pages",
              "chars_raw", "chars_clean", "ratio", "chars_raw_ns", "chars_clean_ns", "ratio_ns",
              "anchors", "sha256", "flags"]
    with (REPO / "data" / "clean" / "manifest.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(registry)

    # failed
    with (REPO / "data" / "clean" / "failed.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["course", "rel", "error"])
        w.writeheader()
        w.writerows([{k: x[k] for k in ("course", "rel", "error")} for x in failed])

    # report
    by_course = Counter()
    chars_by_course = Counter()
    pages_by_course = Counter()
    for x in registry:
        by_course[x["course"]] += 1
        chars_by_course[x["course"]] += x["chars_clean"]
        pages_by_course[x["course"]] += x["pages"]
    loss = [x for x in registry if x["ratio_ns"] < 0.98]
    mostly_empty = [x for x in registry if "mostly_empty_pages" in x["flags"]]
    no_headings = [x for x in registry if "no_headings" in x["flags"]]

    lines = [
        "# Step 2 — Extraction report",
        "",
        f"- extracted: {len(registry)} / {len(rows)}",
        f"- failed: {len(failed)}",
        f"- total pages: {sum(x['pages'] for x in registry):,}",
        f"- total chars: {sum(x['chars_clean'] for x in registry):,}",
        f"- page anchors: {sum(x['anchors'] for x in registry):,}",
        f"- char-loss (non-space <98%): {len(loss)}",
        f"- mostly empty pages: {len(mostly_empty)}",
        f"- MD without headings: {len(no_headings)}",
        "",
        "## By course",
        "",
        "| course | files | pages | chars |",
        "|---|---:|---:|---:|",
    ]
    for c in sorted(by_course, key=lambda x: -chars_by_course[x]):
        lines.append(f"| {c} | {by_course[c]} | {pages_by_course[c]} | {chars_by_course[c]:,} |")
    if loss:
        lines += ["", "## Char-loss files (non-space comparison)", "", "| course | source | rel | raw_ns | clean_ns | ratio_ns |", "|---|---|---|---:|---:|---:|"]
        for x in sorted(loss, key=lambda y: y["ratio_ns"])[:20]:
            lines.append(f"| {x['course']} | {x['source_id']} | {x['rel']} | {x['chars_raw_ns']} | {x['chars_clean_ns']} | {x['ratio_ns']} |")
    if failed:
        lines += ["", "## Failed", ""]
        for x in failed:
            lines.append(f"- {x['course']} {x['rel']}: {x['error']}")
    (REPO / "data" / "clean" / "extraction_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "extracted": len(registry),
        "failed": len(failed),
        "pages": sum(x["pages"] for x in registry),
        "chars": sum(x["chars_clean"] for x in registry),
        "anchors": sum(x["anchors"] for x in registry),
        "char_loss": len(loss),
        "mostly_empty": len(mostly_empty),
        "no_headings": len(no_headings),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
