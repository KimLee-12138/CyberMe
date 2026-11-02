# -*- coding: utf-8 -*-
"""Smoke test the note browser API."""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from types import SimpleNamespace  # noqa: E402

from app.auth.dependencies import current_user  # noqa: E402
from app.notes.router import router  # noqa: E402


def main() -> None:
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[current_user] = lambda: SimpleNamespace(id="test", username="test")
    c = TestClient(app)

    all_notes = c.get("/api/v1/notes").json()
    db = c.get("/api/v1/notes", params={"course": "DB"}).json()
    search = c.get("/api/v1/notes", params={"q": "函数依赖"}).json()
    flagged = c.get("/api/v1/notes", params={"flag": "formula_missing"}).json()
    detail = c.get("/api/v1/notes/DB-TOPIC-001").json()
    missing = c.get("/api/v1/notes/NOT-A-NOTE")

    checks = [
        ("total 433", all_notes["total"] == 433, str(all_notes["total"])),
        ("20 courses", all_notes["stats"]["courses"] == 20, str(all_notes["stats"]["courses"])),
        ("formula 73", all_notes["stats"]["formula_missing"] == 73, str(all_notes["stats"]["formula_missing"])),
        ("conflicts 3", all_notes["stats"]["conflicts"] == 3, str(all_notes["stats"]["conflicts"])),
        ("DB 16", db["total"] == 16, str(db["total"])),
        ("search 2", search["total"] == 2, str(search["total"])),
        ("flag 73", flagged["total"] == 73, str(flagged["total"])),
        ("detail title", "数据库基础" in detail.get("title", ""), detail.get("title", "")),
        ("detail body", len(detail.get("body", "")) > 1000, str(len(detail.get("body", "")))),
        ("detail source pages", detail["sources"][0]["source_pages"] == [1, 4], str(detail["sources"][0]["source_pages"])),
        ("detail chapter", bool(detail.get("chapter")), detail.get("chapter", "")),
        ("404", missing.status_code == 404, str(missing.status_code)),
    ]

    passed = sum(1 for _, ok, _ in checks if ok)
    for name, ok, d in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {d}")
    print(f"\n{passed}/{len(checks)} passed")

    report = REPO / "data" / "notes_smoke_report.md"
    lines = ["# Notes browser smoke test", "", f"- passed: {passed}/{len(checks)}", "", "| check | result | detail |", "|---|---|---|"]
    for name, ok, d in checks:
        lines.append(f"| {name} | {'PASS' if ok else 'FAIL'} | {d} |")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
