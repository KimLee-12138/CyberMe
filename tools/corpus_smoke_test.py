# -*- coding: utf-8 -*-
"""Smoke test the corpus data-quality API against frozen v1 counts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from types import SimpleNamespace  # noqa: E402

from app.auth.dependencies import current_user  # noqa: E402
from app.corpus.router import router  # noqa: E402


def main() -> None:
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[current_user] = lambda: SimpleNamespace(id="test", username="test")
    c = TestClient(app)

    stats = c.get("/api/v1/corpus/stats").json()
    courses = c.get("/api/v1/corpus/courses").json()
    issues = c.get("/api/v1/corpus/issues").json()

    checks = [
        ("funnel counts", [x["count"] for x in stats["funnel"]] == [868, 410, 309, 414, 4523, 433],
         str([x["count"] for x in stats["funnel"]])),
        ("quality status", [stats["quality"][k] for k in ["official", "review", "candidate", "duplicate", "quarantine"]] == [150, 233, 10, 15, 2],
         str([stats["quality"][k] for k in ["official", "review", "candidate", "duplicate", "quarantine"]])),
        ("indexable", stats["quality"]["indexable"] == 383, str(stats["quality"]["indexable"])),
        ("distill", stats["quality"]["distill"] == 309, str(stats["quality"]["distill"])),
        ("conflicts", len(issues["conflicts"]) == 2, str(len(issues["conflicts"]))),
        ("formula missing", len(issues["formula_missing"]) == 0, str(len(issues["formula_missing"]))),
        ("quarantine", len(issues["quarantine"]) == 2, str(len(issues["quarantine"]))),
        ("near duplicates", len(issues["near_duplicates"]) == 203, str(len(issues["near_duplicates"]))),
        ("near dup duplicate", issues["counts"]["near_duplicate_duplicate"] == 15, str(issues["counts"]["near_duplicate_duplicate"])),
        ("near dup parallel", issues["counts"]["near_duplicate_parallel"] == 172, str(issues["counts"]["near_duplicate_parallel"])),
        ("coverage", stats["coverage"]["coverage"] == 1.0 and stats["coverage"]["gaps"] == 0, str(stats["coverage"])),
        ("courses total", courses["total"] == 20, str(courses["total"])),
        ("course totals", courses["totals"] == {
            "included": 410, "distill": 309, "sections": 389,
            "units": 4523, "topics": 433, "formula_missing": 0, "conflicts": 2,
         }, json.dumps(courses["totals"], ensure_ascii=False)),
        ("writeback", stats["writeback"] == {
            "total": 433, "create": 400, "append_supplement": 28,
            "skip_duplicate": 5, "vault_modified": False,
         }, json.dumps(stats["writeback"], ensure_ascii=False)),
    ]

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, detail in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {detail}")
    print(f"\n{passed}/{len(checks)} passed")

    report = REPO / "data" / "corpus_smoke_report.md"
    lines = ["# Corpus quality smoke test", "", f"- passed: {passed}/{len(checks)}", "", "| check | result | detail |", "|---|---|---|"]
    for name, ok, detail in checks:
        lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {detail} |")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
