# -*- coding: utf-8 -*-
"""Step 1 — inventory, classify, and decide inclusion for the CyberMe corpus.

Scope (confirmed by user):
  - only CORE Chinese course review materials under F:\\学习
  - PDF + Markdown only (no PPT/DOCX, no OCR)
  - exclude English textbooks, academic English, 团课, projects, scans, garbled, duplicates

Outputs under <repo>/data/registry/:
  raw_inventory.csv   every PDF/MD found (except 数字图像处理)
  decisions.csv       one row per file with status/reason/tier
  included.csv        status == include
  excluded.csv        status == exclude
  scanned.csv         no text layer
  garbled.csv         CID/mojibake suspects
  duplicates.csv      exact duplicate groups
  course_map.csv      folder -> course code
  summary.json / summary.md
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from collections import Counter, defaultdict
from pathlib import Path

import fitz  # PyMuPDF

ROOT = Path(r"F:\学习")
REPO = Path(r"D:\CyberMe\repo")
OUT = REPO / "data" / "registry"
OUT.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------- scope
EXCLUDE_DIRS = {"数字图像处理"}
EXCLUDE_COURSES = {
    "英语",              # 6 English novels, 3.77M chars
    "综合实训",          # project docs
    "学生工作证明材料",
    "社会实践",
    "四六级",
    "学术英语",
    "团课",
    "Book-Mathematical-Foundation-of-Reinforcement-Learning-main",  # English RL textbook
}

TOP_COURSE = {
    "数据库": "DB",
    "算法": "ALGO",
    "数据结构": "DS",
    "计算机组成原理": "CO",
    "软件工程": "SE",
    "EDA": "EDA",
    "汇编": "ASM",
    "java": "JAVA",
    "python": "PY",
    "C++": "CPP",
    "概率论": "PROB",
    "微积分": "CALCULUS",
    "线性代数": "LINALG",
    "离散数学": "DISCRETE",
    "大学物理": "PHYSICS",
    "马原": "MAYUAN",
    "毛概": "MAOGAI",
    "习概": "XIGAI",
    "近代史": "HISTORY",
    "思想与政治": "SIXIANG",
    "军理": "JUNLI",
    "党校": "DANGXIAO",
    "强化学习": "RLMATH",
    "信息导论": "INFO",
    "政策与形势": "ZHENGCE",
}
UMBRELLA = {
    "大一上": {
        "C++": "CPP", "C C++": "CPP", "微积分": "CALCULUS", "思政": "SIXIANG",
        "离散数学": "DISCRETE", "线性代数": "LINALG", "近代史": "HISTORY",
    },
    "大一下": {
        "python": "PY", "军理": "JUNLI", "数据结构": "DS",
        "离散数学": "DISCRETE", "近代史": "HISTORY",
    },
}
TIER1 = {"DB", "ALGO", "DS", "CO", "SE", "EDA", "ASM", "JAVA", "CPP", "PY",
         "PROB", "CALCULUS", "LINALG", "DISCRETE", "PHYSICS", "RLMATH", "INFO", "ZHENGCE"}
TIER2 = {"MAYUAN", "MAOGAI", "XIGAI", "HISTORY", "SIXIANG", "JUNLI", "DANGXIAO"}

# Content-based corrections for clearly mislabeled folders/files.
# Keep these explicit and logged; do not silently guess.
COURSE_OVERRIDES = [
    ("大一上/微积分/思维导图", "SIXIANG"),  # 人生观/理想信念/中国精神 = 思政
    ("大学物理/大物复习/华中农业大学《概率论与数理统计》", "PROB"),
    ("毛概/毛概习思", "XIGAI"),  # 习思想学习手册放在毛概目录下
]

CJK = re.compile(r"[\u4e00-\u9fff]")
# CID/mojibake suspects: private use, replacement, CJK Ext-A, compatibility ideographs,
# and stray Cyrillic in Chinese text.
RARE = re.compile(r"[\ue000-\uf8ff\ufffd\u3400-\u4dbf\uf900-\ufaff\u0400-\u04ff]")
# Characters that are expected in a readable Chinese/English study document.
GOOD = re.compile(
    r"[\u4e00-\u9fffA-Za-z0-9"
    r"\u03b1-\u03c9\u0391-\u03a9"  # Greek letters
    r"，。！？；：、（）《》“”‘’—…·"
    r".,;:!?()\[\]{}<>/\\%+\-*=<>≤≥≠→←↑↓∈∑∫√±×÷°"
    r"]"
)

PROJECT_HINTS = ("实验", "大作业", "课程设计", "项目", "实训", "报告", "源码", "代码", "src", "code")
DEPENDENCY_RE = re.compile(r"(^|/)(\.venv|venv|site-packages|dist-info|node_modules|__pycache__|\.git)(/|$)|(^|/)(LICENSE|COPYING|NOTICE)(\.|$)", re.I)


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def course_code(rel: str) -> tuple[str, str]:
    """Return (top_folder, course_code_or_empty)."""
    parts = rel.split("/")
    top = parts[0]
    for prefix, code in COURSE_OVERRIDES:
        if rel.startswith(prefix):
            return top, code
    if top in UMBRELLA and len(parts) > 1:
        return top, UMBRELLA[top].get(parts[1], "")
    return top, TOP_COURSE.get(top, "")


def classify_kind(rel: str, ext: str) -> str:
    s = rel.lower()
    if re.search(r"准考证|名单|成绩单|证明|通知|报名|汇总表|统计表|学生工作|评语|鉴定", s):
        return "admin"
    if re.search(r"试卷|试题|考题|期末|期中|考试|答案|真题|[AB]卷", s):
        return "exam"
    if re.search(r"习题|练习|题库|课后题", s):
        return "exercise"
    if re.search(r"实验|大作业|课程设计|项目|实训|报告|源码|code|src|作业|说明书|设计文档|需求规格|概要设计|详细设计|团队提交|SignalTap|测试案例|测试用例|调试详细教程", s):
        return "project"
    if re.search(r"课件|ppt|幻灯片|lecture|slides|讲义", s):
        kind = "slides"
    elif re.search(r"笔记|总结|复习|知识点|提纲|梳理|note|summary", s):
        kind = "notes"
    elif re.search(r"教材|教程|textbook", s):
        kind = "textbook"
    elif re.search(r"第[一二三四五六七八九十0-9\-]+章", s):
        kind = "slides" if ext == ".pdf" else "notes"
    else:
        kind = "other"
    # Markdown lecture notes are notes, not slides.
    if ext == ".md" and kind == "slides":
        return "notes"
    return kind


def pdf_stats(p: Path) -> dict:
    d = fitz.open(p)
    pages = d.page_count
    texts = []
    for i in range(pages):
        try:
            texts.append(d[i].get_text("text"))
        except Exception:
            texts.append("")
    d.close()
    text = "\n".join(texts)
    chars = len(text)
    cjk = len(CJK.findall(text))
    rare = len(RARE.findall(text))
    good = len(GOOD.findall(text))
    first = ""
    for t in texts:
        s = t.strip().replace("\n", " ")
        if s:
            first = s[:160]
            break
    return {
        "pages": pages,
        "chars": chars,
        "chars_per_page": round(chars / pages, 1) if pages else 0,
        "cjk_ratio": round(cjk / chars, 4) if chars else 0,
        "rare_ratio": round(rare / chars, 4) if chars else 0,
        "good_ratio": round(good / chars, 4) if chars else 0,
        "first_line": first,
    }


def md_stats(p: Path) -> dict:
    t = p.read_text(encoding="utf-8-sig", errors="replace")
    chars = len(t)
    cjk = len(CJK.findall(t))
    rare = len(RARE.findall(t))
    good = len(GOOD.findall(t))
    code_chars = sum(len(m) for m in re.findall(r"```.*?```", t, re.S))
    headings = len(re.findall(r"^#{1,6}\s+", t, re.M))
    first = next((l.strip() for l in t.splitlines() if l.strip()), "")[:160]
    return {
        "pages": 0,
        "chars": chars,
        "chars_per_page": 0,
        "cjk_ratio": round(cjk / chars, 4) if chars else 0,
        "rare_ratio": round(rare / chars, 4) if chars else 0,
        "good_ratio": round(good / chars, 4) if chars else 0,
        "code_ratio": round(code_chars / chars, 4) if chars else 0,
        "headings": headings,
        "first_line": first,
    }


def main() -> None:
    files: list[tuple[Path, str]] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if p.suffix.lower() not in {".pdf", ".md"}:
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel.split("/")[0] in EXCLUDE_DIRS:
            continue
        files.append((p, rel))

    print(f"found {len(files)} PDF/MD files", flush=True)
    rows: list[dict] = []
    t0 = time.time()
    for i, (p, rel) in enumerate(files, 1):
        top, code = course_code(rel)
        kind = classify_kind(rel, p.suffix.lower())
        rec = {
            "path": str(p),
            "rel": rel,
            "top_folder": top,
            "course": code,
            "ext": p.suffix.lower(),
            "doc_type": kind,
            "size_kb": round(p.stat().st_size / 1024, 1),
        }
        try:
            rec["sha256"] = sha256(p)
            rec.update(pdf_stats(p) if p.suffix.lower() == ".pdf" else md_stats(p))
        except Exception as e:
            rec["error"] = str(e)[:200]
            rec["sha256"] = ""
            rec.update({"pages": 0, "chars": 0, "chars_per_page": 0,
                        "cjk_ratio": 0, "rare_ratio": 0, "good_ratio": 0, "first_line": ""})

        chars = rec.get("chars", 0) or 0
        rec["scanned"] = rec["ext"] == ".pdf" and (rec.get("chars_per_page", 0) or 0) < 50
        rec["garbled"] = chars > 200 and (
            (rec.get("good_ratio", 1) or 0) < 0.40
            or (rec.get("rare_ratio", 0) or 0) > 0.10
        )
        rec["too_short"] = chars < 500
        rec["code_ratio"] = rec.get("code_ratio", 0) or 0
        rec["code_heavy"] = rec["code_ratio"] > 0.6
        rec["project_like"] = kind == "project" or any(h in rel.lower() for h in PROJECT_HINTS)
        rec["tier"] = 1 if code in TIER1 else (2 if code in TIER2 else 0)
        rec["course_override"] = next((pre for pre, _ in COURSE_OVERRIDES if rel.startswith(pre)), "")
        rows.append(rec)
        if i % 100 == 0:
            print(f"  {i}/{len(files)}  {time.time()-t0:.0f}s", flush=True)

    # exact duplicates: keep the richest version
    by_hash: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r.get("sha256"):
            by_hash[r["sha256"]].append(r)
    dup_groups = {h: g for h, g in by_hash.items() if len(g) > 1}
    canonical: dict[str, str] = {}
    for h, g in dup_groups.items():
        g.sort(key=lambda r: (r.get("chars", 0), r.get("chars_per_page", 0), r.get("pages", 0)), reverse=True)
        canonical[h] = g[0]["rel"]
        for r in g[1:]:
            r["duplicate_of"] = g[0]["rel"]

    # decisions
    for r in rows:
        reasons = []
        out_of_scope = r["top_folder"] in EXCLUDE_COURSES
        if out_of_scope:
            reasons.append("course_out_of_scope")
        elif not r.get("course"):
            reasons.append("unmapped_course")
        if r.get("error"):
            reasons.append("extract_error")
        if r.get("scanned"):
            reasons.append("scanned_no_text")
        if r.get("garbled"):
            reasons.append("garbled_encoding")
        if r.get("too_short"):
            reasons.append("too_short")
        if r.get("duplicate_of"):
            reasons.append("exact_duplicate")
        if r["doc_type"] == "admin":
            reasons.append("admin_document")
        if DEPENDENCY_RE.search(r["rel"]):
            reasons.append("dependency_or_license")
        if r.get("project_like") and r["doc_type"] in {"project"}:
            reasons.append("project_or_code")
        if r.get("code_heavy"):
            reasons.append("pure_code_md")

        if reasons:
            r["status"] = "exclude"
            r["reason"] = ";".join(dict.fromkeys(reasons))
        else:
            r["status"] = "include"
            r["reason"] = "core_knowledge"
        flags = []
        if r.get("scanned"): flags.append("scanned")
        if r.get("garbled"): flags.append("garbled")
        if r.get("code_heavy"): flags.append("code_heavy")
        if 50 <= (r.get("chars_per_page", 0) or 0) < 150 and r["ext"] == ".pdf": flags.append("sparse")
        if r["doc_type"] in {"exam", "exercise"}: flags.append(r["doc_type"])
        if r["doc_type"] == "slides": flags.append("slides")
        if r["doc_type"] == "notes": flags.append("notes")
        r["flags"] = ";".join(flags)
        r["canonical"] = r.get("sha256") in dup_groups and r["rel"] == canonical.get(r.get("sha256", ""), "")

    # write raw inventory
    raw_fields = ["path", "rel", "top_folder", "course", "ext", "doc_type", "size_kb",
                  "sha256", "pages", "chars", "chars_per_page", "cjk_ratio", "rare_ratio",
                  "good_ratio", "code_ratio", "headings", "scanned", "garbled", "too_short",
                  "code_heavy", "project_like", "tier", "course_override", "first_line", "error"]
    write_csv(OUT / "raw_inventory.csv", rows, raw_fields)

    dec_fields = ["path", "rel", "top_folder", "course", "ext", "doc_type", "tier",
                  "pages", "chars", "chars_per_page", "cjk_ratio", "rare_ratio", "good_ratio",
                  "code_ratio", "headings", "scanned", "garbled", "too_short", "project_like",
                  "status", "reason", "flags", "canonical", "duplicate_of", "course_override",
                  "sha256", "first_line"]
    write_csv(OUT / "decisions.csv", rows, dec_fields)
    write_csv(OUT / "included.csv", [r for r in rows if r["status"] == "include"], dec_fields)
    write_csv(OUT / "excluded.csv", [r for r in rows if r["status"] == "exclude"], dec_fields)
    write_csv(OUT / "scanned.csv", [r for r in rows if r.get("scanned")], dec_fields)
    write_csv(OUT / "garbled.csv", [r for r in rows if r.get("garbled")], dec_fields)
    write_csv(OUT / "duplicates.csv", [r for r in rows if r.get("duplicate_of")], dec_fields)

    # review queue: largest excluded + random included
    import random
    inc_tmp = [r for r in rows if r["status"] == "include"]
    exc_tmp = [r for r in rows if r["status"] == "exclude" and r["top_folder"] not in EXCLUDE_COURSES]
    review = []
    for r in sorted(exc_tmp, key=lambda x: -x.get("chars", 0))[:30]:
        review.append({**r, "review_type": "excluded_large"})
    random.seed(42)
    for r in random.sample(inc_tmp, min(30, len(inc_tmp))):
        review.append({**r, "review_type": "included_random"})
    write_csv(OUT / "review_queue.csv", review, dec_fields + ["review_type"])

    # course map
    map_rows = [{"top_folder": k, "course": v} for k, v in TOP_COURSE.items()]
    for parent, m in UMBRELLA.items():
        for sub, code in m.items():
            map_rows.append({"top_folder": f"{parent}/{sub}", "course": code})
    write_csv(OUT / "course_map.csv", map_rows, ["top_folder", "course"])

    # summary
    inc = [r for r in rows if r["status"] == "include"]
    exc = [r for r in rows if r["status"] == "exclude"]
    by_course = defaultdict(lambda: Counter())
    for r in inc:
        c = by_course[r["course"]]
        c["files"] += 1
        c["pages"] += r.get("pages", 0)
        c["chars"] += r.get("chars", 0)
    reason_counts = Counter()
    for r in exc:
        for x in r["reason"].split(";"):
            reason_counts[x] += 1
    summary = {
        "raw_files": len(rows),
        "raw_pdf": sum(1 for r in rows if r["ext"] == ".pdf"),
        "raw_md": sum(1 for r in rows if r["ext"] == ".md"),
        "raw_pages": sum(r.get("pages", 0) for r in rows),
        "raw_chars": sum(r.get("chars", 0) for r in rows),
        "included_files": len(inc),
        "included_pdf": sum(1 for r in inc if r["ext"] == ".pdf"),
        "included_md": sum(1 for r in inc if r["ext"] == ".md"),
        "included_pages": sum(r.get("pages", 0) for r in inc),
        "included_chars": sum(r.get("chars", 0) for r in inc),
        "excluded_files": len(exc),
        "duplicate_groups": len(dup_groups),
        "duplicate_files": sum(len(g) - 1 for g in dup_groups.values()),
        "by_course": {k: dict(v) for k, v in sorted(by_course.items(), key=lambda x: -x[1]["chars"])},
        "exclude_reasons": dict(reason_counts.most_common()),
        "tier_counts": dict(Counter(r["tier"] for r in inc)),
        "doc_type_counts": dict(Counter(r["doc_type"] for r in inc)),
    }
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    exc_review = [r for r in exc if r["top_folder"] not in EXCLUDE_COURSES]
    (OUT / "summary.md").write_text(render_summary(summary, inc, exc_review), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k not in {"by_course", "exclude_reasons"}},
                     ensure_ascii=False, indent=2))
    print("\nby_course:")
    for k, v in summary["by_course"].items():
        print(f"  {k:8s} files={v['files']:3d} pages={v['pages']:4d} chars={v['chars']:7d}")
    print("\nexclude reasons:", summary["exclude_reasons"])


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def render_summary(summary: dict, inc: list[dict], exc: list[dict]) -> str:
    lines = [
        "# Step 1 — Corpus inventory & inclusion decisions",
        "",
        "## Scope",
        "- CORE Chinese course materials only",
        "- PDF + Markdown only; no PPT/DOCX, no OCR",
        "- English textbooks, academic English, 团课 excluded",
        "",
        "## Raw",
        f"- files: {summary['raw_files']} (PDF {summary['raw_pdf']}, MD {summary['raw_md']})",
        f"- pages: {summary['raw_pages']:,}",
        f"- chars: {summary['raw_chars']:,}",
        "",
        "## Included",
        f"- files: {summary['included_files']} (PDF {summary['included_pdf']}, MD {summary['included_md']})",
        f"- pages: {summary['included_pages']:,}",
        f"- chars: {summary['included_chars']:,}",
        "",
        "### By course",
        "",
        "| course | files | pages | chars |",
        "|---|---:|---:|---:|",
    ]
    for k, v in summary["by_course"].items():
        lines.append(f"| {k} | {v['files']} | {v['pages']} | {v['chars']:,} |")
    lines += [
        "",
        "## Excluded",
        f"- files: {summary['excluded_files']}",
        f"- reasons: {summary['exclude_reasons']}",
        f"- exact duplicate groups: {summary['duplicate_groups']} ({summary['duplicate_files']} extra files)",
        "",
        "## Included doc types",
        f"- {summary['doc_type_counts']}",
        "",
        "## Notes",
        "- Scanned files are excluded, not OCR'd (user decision).",
        "- PPT/DOCX are out of scope (user decision).",
        "- Near-duplicate detection is Step 4; this step only removes exact SHA-256 duplicates.",
        "",
    ]
    # largest included
    lines += ["## Largest included files", "", "| course | file | chars | pages |", "|---|---|---:|---:|"]
    for r in sorted(inc, key=lambda x: -x.get("chars", 0))[:15]:
        lines.append(f"| {r['course']} | {r['rel']} | {r['chars']:,} | {r.get('pages',0)} |")
    lines += ["", "## Largest excluded files (manual review candidates)", "", "| course | file | chars | reason |", "|---|---|---:|---|"]
    for r in sorted(exc, key=lambda x: -x.get("chars", 0))[:15]:
        lines.append(f"| {r.get('course','')} | {r['rel']} | {r.get('chars',0):,} | {r['reason']} |")
    lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    main()
