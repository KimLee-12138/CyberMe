# -*- coding: utf-8 -*-
"""Step 10 — freeze v1, build final manifest and writeback proposal.

Outputs:
  data/manifest_v1.json
  data/README.md
  data/notes/_writeback_proposal.json
  data/notes/_freeze_report.md
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"D:\CyberMe\repo")
DATA = REPO / "data"
VAULT = REPO / "Vault"
NOTES = DATA / "notes"

DIRS = [
    "registry",
    "clean/v1",
    "sections",
    "units",
    "topics",
    "notes",
]


def tree_hash(path: Path) -> dict:
    if not path.exists():
        return {"files": 0, "bytes": 0, "sha256": ""}
    h = hashlib.sha256()
    n = 0
    total = 0
    for p in sorted(x for x in path.rglob("*") if x.is_file()):
        rel = p.relative_to(path).as_posix()
        b = p.read_bytes()
        n += 1
        total += len(b)
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(hashlib.sha256(b).digest())
    return {"files": n, "bytes": total, "sha256": h.hexdigest()}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def course_folder_map() -> dict[str, str]:
    out = {}
    uni = VAULT / "20_University"
    if not uni.exists():
        return out
    for d in uni.iterdir():
        if d.is_dir() and "_" in d.name:
            code = d.name.split("_", 1)[0]
            out.setdefault(code, d.name)
    return out


def safe_name(title: str) -> str:
    s = re.sub(r'[\\/:*?"<>|]', " ", title)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:80] or "未命名"


def main() -> None:
    # counts
    raw = list(csv.DictReader((DATA / "registry" / "raw_inventory.csv").open(encoding="utf-8-sig")))
    clean = list(csv.DictReader((DATA / "clean" / "manifest.csv").open(encoding="utf-8-sig")))
    distill = [r for r in clean if str(r.get("distill")).lower() == "true"]
    quality = Counter(r.get("quality_status") for r in clean)
    sections = [json.loads(x) for x in (DATA / "sections" / "sections.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    units = []
    for p in (DATA / "units").glob("*/*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        r = d.get("result", {})
        if r.get("has_knowledge"):
            units.extend(r.get("units", []))
    topics = []
    for p in (DATA / "topics").glob("*.jsonl"):
        topics.extend(json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip())
    notes = list(csv.DictReader((NOTES / "_manifest.csv").open(encoding="utf-8-sig")))
    merges = list(csv.DictReader((NOTES / "_merge_suggestions.csv").open(encoding="utf-8-sig")))
    merge_counts = Counter(m["action"] for m in merges)

    # token usage
    unit_usage = list(csv.DictReader((DATA / "units" / "usage.csv").open(encoding="utf-8-sig")))
    u_in = sum(int(x["input_tokens"]) for x in unit_usage)
    u_out = sum(int(x["output_tokens"]) for x in unit_usage)
    t_in = sum(int(t.get("usage", {}).get("prompt_tokens", 0)) for t in topics)
    t_out = sum(int(t.get("usage", {}).get("completion_tokens", 0)) for t in topics)
    in_tok, out_tok = u_in + t_in, u_out + t_out

    funnel = {
        "raw_files": len(raw),
        "included_files": len(clean),
        "distill_files": len(distill),
        "section_parts": len(sections),
        "knowledge_units": len(units),
        "topics": len(topics),
        "notes": len(notes),
    }
    quality_summary = {
        "official": quality.get("official", 0),
        "review": quality.get("review", 0),
        "candidate": quality.get("candidate", 0),
        "duplicate": quality.get("duplicate", 0),
        "quarantine": quality.get("quarantine", 0),
        "indexable": sum(1 for r in clean if str(r.get("indexable")).lower() == "true"),
        "distill": len(distill),
        "conflicts": sum(len(t["topic"].get("conflicts") or []) for t in topics),
        "formula_missing_notes": sum(1 for n in notes if "formula_missing" in (n.get("flags") or "")),
        "merge_duplicate": merge_counts.get("duplicate", 0),
        "merge_supplement": merge_counts.get("supplement", 0),
        "merge_new": merge_counts.get("new", 0),
    }
    cost = {
        "step7_input_tokens": u_in,
        "step7_output_tokens": u_out,
        "step8_input_tokens": t_in,
        "step8_output_tokens": t_out,
        "total_input_tokens": in_tok,
        "total_output_tokens": out_tok,
        "total_tokens": in_tok + out_tok,
        "flash_offpeak_usd": round(in_tok / 1_000_000 * 0.15 + out_tok / 1_000_000 * 0.60, 4),
        "flash_peak_usd": round(in_tok / 1_000_000 * 0.30 + out_tok / 1_000_000 * 1.20, 4),
    }

    dirs = {d: tree_hash(DATA / d) for d in DIRS}
    manifest = {
        "version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "vault": "Vault/ (unchanged; notes are proposals only)",
        "funnel": funnel,
        "quality": quality_summary,
        "cost": cost,
        "directories": dirs,
        "scripts": [
            "tools/build_registry.py",
            "tools/extract_clean.py",
            "tools/normalize_clean.py",
            "tools/dedup_near.py",
            "tools/quality_score.py",
            "tools/build_sections.py",
            "tools/map_distill.py",
            "tools/merge_topics.py",
            "tools/generate_notes.py",
            "tools/freeze_v1.py",
        ],
    }
    (DATA / "manifest_v1.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # writeback proposal
    cf = course_folder_map()
    proposal = []
    for n in notes:
        m = next((x for x in merges if x["note_id"] == n["note_id"]), None)
        action = m["action"] if m else "new"
        target_folder = cf.get(n["course"], f"{n['course']}_未分类")
        if action in ("supplement", "duplicate") and m.get("existing_path"):
            target = m["existing_path"]
            base = sha256_file(REPO / target) if (REPO / target).exists() else ""
        else:
            target = f"Vault/20_University/{target_folder}/02_知识点/{safe_name(n['title'])}.md"
            base = ""
        proposal.append({
            "note_id": n["note_id"],
            "course": n["course"],
            "title": n["title"],
            "source_note": n["path"],
            "action": {"new": "create", "supplement": "append_supplement", "duplicate": "skip_duplicate"}.get(action, "create"),
            "target_path": target,
            "base_hash": f"sha256:{base}" if base else None,
            "requires_approval": True,
        })
    (NOTES / "_writeback_proposal.json").write_text(
        json.dumps({"version": 1, "generated_at": manifest["generated_at"], "items": proposal}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # README
    readme = f"""# CyberMe Corpus v1

Generated: {manifest['generated_at']}

## Funnel

| stage | count |
|---|---:|
| raw PDF/MD | {funnel['raw_files']} |
| included | {funnel['included_files']} |
| distill | {funnel['distill_files']} |
| section parts | {funnel['section_parts']} |
| knowledge units | {funnel['knowledge_units']} |
| topics | {funnel['topics']} |
| notes | {funnel['notes']} |

## Layout

```text
data/
├─ registry/       # source inventory, decisions, quality, canonical
├─ clean/v1/       # normalized full text with page/section anchors
├─ sections/       # sections.jsonl, pages.jsonl, headings.jsonl, coverage
├─ units/          # 414 JSON outputs from Map distillation
├─ topics/         # 433 topic JSONL
├─ notes/          # 433 Markdown notes + manifests + writeback proposal
└─ manifest_v1.json
```

## Quality

- official: {quality_summary['official']}
- review: {quality_summary['review']}
- candidate: {quality_summary['candidate']}
- duplicate: {quality_summary['duplicate']}
- quarantine: {quality_summary['quarantine']}
- conflicts: {quality_summary['conflicts']}
- notes with formula_missing: {quality_summary['formula_missing_notes']}

## Rebuild

```bash
cd D:\\CyberMe\\repo
python tools/build_registry.py
python tools/extract_clean.py
python tools/normalize_clean.py
python tools/dedup_near.py
python tools/quality_score.py
python tools/build_sections.py
python tools/map_distill.py --concurrency 8
python tools/merge_topics.py --concurrency 8
python tools/generate_notes.py
python tools/freeze_v1.py
```
"""
    (DATA / "README.md").write_text(readme, encoding="utf-8")

    # freeze report
    lines = [
        "# Step 10 — Freeze report",
        "",
        f"- generated: {manifest['generated_at']}",
        f"- raw: {funnel['raw_files']}",
        f"- included: {funnel['included_files']}",
        f"- distill: {funnel['distill_files']}",
        f"- section parts: {funnel['section_parts']}",
        f"- units: {funnel['knowledge_units']}",
        f"- topics: {funnel['topics']}",
        f"- notes: {funnel['notes']}",
        "",
        "## Directory hashes",
        "",
        "| dir | files | bytes | sha256 |",
        "|---|---:|---:|---|",
    ]
    for d, h in dirs.items():
        lines.append(f"| {d} | {h['files']} | {h['bytes']} | {h['sha256'][:16]}... |")
    lines += [
        "",
        "## Cost",
        "",
        f"- total tokens: {cost['total_tokens']:,}",
        f"- flash off-peak: ${cost['flash_offpeak_usd']}",
        f"- flash peak: ${cost['flash_peak_usd']}",
        "",
        "## Writeback",
        "",
        f"- proposal items: {len(proposal)}",
        f"- create: {sum(1 for x in proposal if x['action'] == 'create')}",
        f"- append_supplement: {sum(1 for x in proposal if x['action'] == 'append_supplement')}",
        f"- skip_duplicate: {sum(1 for x in proposal if x['action'] == 'skip_duplicate')}",
        "- Vault was NOT modified.",
        "",
    ]
    (NOTES / "_freeze_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "funnel": funnel,
        "quality": quality_summary,
        "cost": cost,
        "writeback_items": len(proposal),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
