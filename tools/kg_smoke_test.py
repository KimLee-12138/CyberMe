# -*- coding: utf-8 -*-
"""Smoke test the knowledge graph API (no LLM, fast)."""
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
from app.kg.router import router  # noqa: E402


def check(name: str, cond: bool, detail: str = "") -> dict:
    return {"name": name, "passed": bool(cond), "detail": detail}


def main() -> None:
    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[current_user] = lambda: SimpleNamespace(id="test", username="test")
    client = TestClient(app)

    checks: list[dict] = []

    overview = client.get("/api/v1/kg/graph").json()
    ids = {n["id"] for n in overview["nodes"]}
    checks.append(check("overview 24 courses", len(overview["nodes"]) == 24, str(len(overview["nodes"]))))
    checks.append(check("overview 18 prerequisites", len(overview["edges"]) == 18, str(len(overview["edges"]))))
    checks.append(check(
        "overview edges endpoints valid",
        all(e["source"] in ids and e["target"] in ids for e in overview["edges"]),
    ))

    db = client.get("/api/v1/kg/graph", params={"course": "DB"}).json()
    db_ids = {n["id"] for n in db["nodes"]}
    checks.append(check("DB expanded >= 40 nodes", len(db["nodes"]) >= 40, str(len(db["nodes"]))))
    checks.append(check("DB expanded >= 70 edges", len(db["edges"]) >= 70, str(len(db["edges"]))))
    checks.append(check(
        "DB edges endpoints valid",
        all(e["source"] in db_ids and e["target"] in db_ids for e in db["edges"]),
    ))

    db_cand = client.get("/api/v1/kg/graph", params={"course": "DB", "include_candidates": "true"}).json()
    checks.append(check("DB candidate edges > 0", len(db_cand.get("candidate_edges", [])) > 0,
                        str(len(db_cand.get("candidate_edges", [])))))

    val = client.get("/api/v1/kg/validate").json()
    checks.append(check("validation ok", val.get("ok") is True, json.dumps(val.get("counts", {}), ensure_ascii=False)))
    checks.append(check("no dangling edges", val["counts"]["dangling_edges"] == 0))
    checks.append(check("no prerequisite cycles", val["counts"]["cycles"] == 0))

    topic = client.get("/api/v1/kg/node/topic:TOP-DB-0093").json()
    node = topic.get("node", {})
    checks.append(check("topic node found", bool(node), node.get("label", "")))
    checks.append(check("topic has note_path", bool(node.get("properties", {}).get("note_path")),
                        node.get("properties", {}).get("note_path", "")))
    checks.append(check("topic has source pages",
                        bool(node.get("properties", {}).get("sources")),
                        str(node.get("properties", {}).get("sources", []))[:120]))

    passed = sum(1 for c in checks if c["passed"])
    total = len(checks)
    for c in checks:
        print(f"[{'PASS' if c['passed'] else 'FAIL'}] {c['name']} {c['detail']}")
    print(f"\n{passed}/{total} passed")

    out = REPO / "data" / "kg" / "smoke_report.md"
    lines = [
        "# KG smoke test",
        "",
        f"- passed: {passed}/{total}",
        "",
        "| check | result | detail |",
        "|---|---|---|",
    ]
    for c in checks:
        lines.append(f"| {c['name']} | {'PASS' if c['passed'] else 'FAIL'} | {c['detail']} |")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
