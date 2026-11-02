# -*- coding: utf-8 -*-
"""Smoke test the RAG API with the six demo questions.

Usage:
  cd D:\\CyberMe\\repo
  $env:DEEPSEEK_API_KEY=[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY','User')
  python tools/rag_smoke_test.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from fastapi import FastAPI  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402
from types import SimpleNamespace  # noqa: E402

from app.auth.dependencies import current_user  # noqa: E402
from app.rag.router import router  # noqa: E402

CASES = [
    {"q": "什么是函数依赖？", "course": "DB", "expect_refused": False},
    {"q": "2NF 和 3NF 的区别是什么？", "course": "DB", "expect_refused": False},
    {"q": "0/1 背包为什么容量要逆序？", "course": "ALGO", "expect_refused": False},
    {"q": "栈和队列的区别是什么？", "course": "DS", "expect_refused": False},
    {"q": "数据库索引的原理是什么？", "course": "DB", "expect_refused": True},
    {"q": "量子纠缠在数据库中的应用", "course": "DB", "expect_refused": True},
]


def main() -> None:
    if not os.environ.get("DEEPSEEK_API_KEY", "").strip():
        raise SystemExit("DEEPSEEK_API_KEY is not set")

    app = FastAPI()
    app.include_router(router)
    app.dependency_overrides[current_user] = lambda: SimpleNamespace(id="test", username="test")
    client = TestClient(app)

    health = client.get("/api/v1/rag/health").json()
    print("health:", health)

    rows = []
    failures = 0
    for i, case in enumerate(CASES, 1):
        r = client.post("/api/v1/rag/ask", json={
            "query": case["q"], "course": case["course"], "top_k": 8,
        })
        ok_http = r.status_code == 200
        data = r.json() if ok_http else {}
        refused = bool(data.get("refused"))
        citations = data.get("citations", [])
        evidence = data.get("evidence", [])
        ev_ids = {e.get("evidence_id") for e in evidence}
        cit_ids = {c.get("evidence_id") for c in citations}
        checks = {
            "http_200": ok_http,
            "degraded_expected": bool(data.get("degraded")) == case["expect_refused"],
            "answer_nonempty": bool(data.get("answer")),
            "evidence_nonempty": len(evidence) > 0 if not case["expect_refused"] else True,
            "citations_when_answerable": (len(citations) > 0) if not case["expect_refused"] else (len(citations) == 0),
            "citation_ids_valid": cit_ids.issubset(ev_ids) if cit_ids else True,
        }
        passed = all(checks.values())
        if not passed:
            failures += 1
        rows.append({
            "n": i,
            "question": case["q"],
            "course": case["course"],
            "expected_refused": case["expect_refused"],
            "degraded": bool(data.get("degraded")),
            "citations": len(citations),
            "evidence": len(evidence),
            "coverage": data.get("coverage"),
            "answer": (data.get("answer") or "")[:300],
            "checks": checks,
            "passed": passed,
            "latency_ms": data.get("latency_ms"),
        })
        print(f"[{i}] {'PASS' if passed else 'FAIL'}  degraded={bool(data.get('degraded'))}  "
              f"citations={len(citations)}  evidence={len(evidence)}  {case['q']}")

    out_json = REPO / "data" / "rag" / "smoke_report.json"
    out_json.write_text(json.dumps({"health": health, "rows": rows}, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# RAG smoke test",
        "",
        f"- cases: {len(rows)}",
        f"- passed: {len(rows) - failures}",
        f"- failed: {failures}",
        "",
        "| # | question | expected degraded | degraded | citations | evidence | coverage | result |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ]
    for x in rows:
        cov = f"{x['coverage']:.2f}" if isinstance(x["coverage"], (int, float)) else "-"
        lines.append(
            f"| {x['n']} | {x['question']} | {x['expected_refused']} | {x['degraded']} | "
            f"{x['citations']} | {x['evidence']} | {cov} | {'PASS' if x['passed'] else 'FAIL'} |"
        )
    (REPO / "data" / "rag" / "smoke_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n{len(rows) - failures}/{len(rows)} passed")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
