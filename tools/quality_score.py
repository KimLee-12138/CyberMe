# -*- coding: utf-8 -*-
"""Step 5 — quality scoring and quarantine.

Input : data/clean/manifest.csv + data/clean/v1/
Output: data/registry/quality_scores.csv
        data/registry/quarantine.csv
        data/clean/quality_report.md
        manifest.csv + quality_score / quality_status / quality_reasons / indexable

Score (0-100):
  density 20 + locator 20 + structure 15 + noise 10 + encoding 15 + redundancy 10 + length 10
Status:
  official >=90 | review 75-89 | candidate 60-74 | quarantine <60
  duplicate files are marked "duplicate" (not indexable)
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(r"D:\CyberMe\repo")
CLEAN = REPO / "data" / "clean" / "v1"
MANIFEST = REPO / "data" / "clean" / "manifest.csv"
REG = REPO / "data" / "registry"
REG.mkdir(parents=True, exist_ok=True)

PAGE_RE = re.compile(r"<!-- page: \d+ -->")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n\n?", re.S)
PRIVATE_RE = re.compile(r"[\ue000-\uf8ff]")
HEADING_RE = re.compile(r"^#{1,6}\s+", re.M)


def density_score(pages: int, chars: int) -> int:
    if pages > 0:
        d = chars / pages
        if d >= 800: return 20
        if d >= 500: return 16
        if d >= 200: return 12
        if d >= 100: return 8
        if d >= 50: return 5
        return 0
    if chars >= 5000: return 20
    if chars >= 2000: return 16
    if chars >= 1000: return 12
    if chars >= 500: return 8
    return 4


def locator_score(pages: int, anchors: int, sections: int) -> int:
    if pages > 0:
        if anchors == pages and pages > 0: return 20
        if anchors > 0: return 15
        return 0
    if sections >= 2: return 20
    if sections == 1: return 12
    return 5


def structure_score(pages: int, anchors: int, headings: int) -> int:
    if pages > 0:
        if pages >= 3 and anchors == pages: return 15
        if pages >= 2: return 10
        return 5
    if headings >= 5: return 15
    if headings >= 1: return 12
    return 5


def encoding_score(private_ratio: float, low_content: bool) -> int:
    if low_content: return 0
    if private_ratio > 0.15: return 0
    if private_ratio > 0.08: return 5
    if private_ratio > 0.02: return 10
    return 15


def length_score(chars: int) -> int:
    if chars >= 5000: return 10
    if chars >= 2000: return 8
    if chars >= 1000: return 6
    if chars >= 500: return 4
    return 0


def redundancy_score(relation: str) -> int:
    if relation == "duplicate": return 0
    if relation == "parallel": return 5
    return 10


def main() -> None:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8-sig")))
    results = []
    for r in rows:
        p = REPO / r["clean_path"]
        text = p.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        body = text[m.end():] if m else text
        body_no_anchor = PAGE_RE.sub("", body)
        chars = len(body_no_anchor)
        pages = int(float(r.get("pages") or 0))
        anchors = int(float(r.get("anchors") or 0))
        sections = int(float(r.get("sections") or 0))
        headings = len(HEADING_RE.findall(body_no_anchor)) if pages == 0 else 0
        private = len(PRIVATE_RE.findall(body_no_anchor))
        private_ratio = private / max(1, len(body_no_anchor))
        flags = [x for x in str(r.get("flags") or "").split(";") if x]
        low_content = "low_content" in flags
        relation = r.get("relation") or "none"

        s_density = density_score(pages, chars)
        s_locator = locator_score(pages, anchors, sections)
        s_structure = structure_score(pages, anchors, headings)
        s_encoding = encoding_score(private_ratio, low_content)
        s_length = length_score(chars)
        s_redundancy = redundancy_score(relation)

        s_noise = 10
        if "normalization_loss" in flags: s_noise -= 4
        if "private_use_chars" in flags: s_noise -= 3
        if int(float(r.get("removed_header_lines") or 0)) > 20: s_noise -= 2
        if int(float(r.get("removed_page_numbers") or 0)) > 20: s_noise -= 1
        s_noise = max(0, s_noise)

        total = s_density + s_locator + s_structure + s_noise + s_encoding + s_redundancy + s_length

        reasons = []
        is_duplicate_copy = relation == "duplicate" and str(r.get("canonical")).lower() == "false"
        if is_duplicate_copy:
            status = "duplicate"
            reasons.append("duplicate_of:" + (r.get("duplicate_of") or ""))
        elif low_content or chars < 300:
            status = "quarantine"
            reasons.append("low_content" if low_content else "too_short")
        elif private_ratio > 0.15:
            status = "quarantine"
            reasons.append(f"private_use_ratio={private_ratio:.3f}")
        elif total >= 90:
            status = "official"
        elif total >= 75:
            status = "review"
        elif total >= 60:
            status = "candidate"
        else:
            status = "quarantine"
            reasons.append(f"score={total}")

        indexable = status in ("official", "review")
        if relation == "parallel" and indexable:
            reasons.append("parallel_with:" + (r.get("parallel_with") or ""))

        results.append({
            "source_id": r["source_id"],
            "course": r["course"],
            "rel": r["rel"],
            "pages": pages,
            "chars": chars,
            "density": round(chars / pages, 1) if pages else "-",
            "private_ratio": round(private_ratio, 4),
            "density_score": s_density,
            "locator_score": s_locator,
            "structure_score": s_structure,
            "noise_score": s_noise,
            "encoding_score": s_encoding,
            "redundancy_score": s_redundancy,
            "length_score": s_length,
            "quality_score": total,
            "quality_status": status,
            "relation": relation,
            "canonical": r.get("canonical", ""),
            "parallel_with": r.get("parallel_with", ""),
            "indexable": "true" if indexable else "false",
            "reasons": ";".join(reasons),
        })

    # distillation flag: one representative per duplicate/parallel cluster
    by_id = {x["source_id"]: x for x in results}
    for x in results:
        x["distill"] = "true" if x["indexable"] == "true" else "false"
    for x in results:
        if x["relation"] == "duplicate" and str(x["canonical"]).lower() == "true" and x["indexable"] == "true":
            x["distill"] = "true"
    seen_par = set()
    for x in results:
        if x["relation"] != "parallel" or not x["parallel_with"] or x["source_id"] in seen_par:
            continue
        partner = by_id.get(x["parallel_with"])
        if not partner:
            continue
        seen_par.add(x["source_id"])
        seen_par.add(partner["source_id"])
        if x["indexable"] != "true" or partner["indexable"] != "true":
            continue
        def rep_key(y):
            return (1 if y["pages"] > 0 else 0, y["quality_score"], y["chars"])
        if rep_key(x) >= rep_key(partner):
            x["distill"] = "true"
            partner["distill"] = "false"
        else:
            partner["distill"] = "true"
            x["distill"] = "false"

    # csv
    fields = list(results[0].keys())
    with (REG / "quality_scores.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(results)

    # quarantine
    q = [x for x in results if x["quality_status"] == "quarantine"]
    with (REG / "quarantine.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(q)

    # update manifest
    by_id = {x["source_id"]: x for x in results}
    mfields = list(rows[0].keys())
    for extra in ("quality_score", "quality_status", "quality_reasons", "indexable", "distill"):
        if extra not in mfields:
            mfields.append(extra)
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=mfields)
        w.writeheader()
        for r in rows:
            x = by_id[r["source_id"]]
            r.update({
                "quality_score": x["quality_score"],
                "quality_status": x["quality_status"],
                "quality_reasons": x["reasons"],
                "indexable": x["indexable"],
                "distill": x["distill"],
            })
            w.writerow(r)

    # report
    status_counts = Counter(x["quality_status"] for x in results)
    by_course = defaultdict(lambda: Counter())
    for x in results:
        by_course[x["course"]][x["quality_status"]] += 1
    scores = sorted(x["quality_score"] for x in results)
    lines = [
        "# Step 5 — Quality score & quarantine report",
        "",
        f"- documents: {len(results)}",
        f"- official (>=90): {status_counts.get('official', 0)}",
        f"- review (75-89): {status_counts.get('review', 0)}",
        f"- candidate (60-74): {status_counts.get('candidate', 0)}",
        f"- quarantine (<60): {status_counts.get('quarantine', 0)}",
        f"- duplicate: {status_counts.get('duplicate', 0)}",
        f"- indexable: {sum(1 for x in results if x['indexable'] == 'true')}",
        f"- distill (one per parallel/duplicate cluster): {sum(1 for x in results if x['distill'] == 'true')}",
        f"- score min / median / max: {scores[0]} / {scores[len(scores)//2]} / {scores[-1]}",
        "",
        "## By course",
        "",
        "| course | official | review | candidate | quarantine | duplicate |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for c in sorted(by_course):
        d = by_course[c]
        lines.append(f"| {c} | {d.get('official',0)} | {d.get('review',0)} | {d.get('candidate',0)} | {d.get('quarantine',0)} | {d.get('duplicate',0)} |")
    lines += ["", "## Quarantine", "", "| course | source | rel | score | reasons |", "|---|---|---|---:|---|"]
    for x in sorted(q, key=lambda y: y["quality_score"]):
        lines.append(f"| {x['course']} | {x['source_id']} | {x['rel']} | {x['quality_score']} | {x['reasons']} |")
    lines += ["", "## Lowest 15 scores (non-duplicate)", "", "| course | source | rel | score | status |", "|---|---|---|---:|---|"]
    for x in sorted([y for y in results if y["relation"] != "duplicate"], key=lambda y: y["quality_score"])[:15]:
        lines.append(f"| {x['course']} | {x['source_id']} | {x['rel']} | {x['quality_score']} | {x['quality_status']} |")
    (REPO / "data" / "clean" / "quality_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(dict(status_counts), ensure_ascii=False, indent=2))
    print("indexable:", sum(1 for x in results if x["indexable"] == "true"))
    print("distill:", sum(1 for x in results if x["distill"] == "true"))
    print("quarantine:", len(q))


if __name__ == "__main__":
    main()
