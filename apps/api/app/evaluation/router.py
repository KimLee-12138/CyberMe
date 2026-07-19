"""Evaluation API — test suites, runs, scoring."""

import uuid
import time
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.chat.engine import ask
from app.core.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/v1")

# ── In-memory storage ────────────────────────────────────

_suites: dict[str, dict] = {}
_runs: list[dict] = []


# ── Schemas ──────────────────────────────────────────────

class EvalCaseCreate(BaseModel):
    question: str = Field(..., max_length=500)
    reference_answer: str = ""
    scope_courses: list[str] = []
    expected_document_ids: list[str] = []


class SuiteCreate(BaseModel):
    name: str = Field(..., max_length=200)
    description: str = ""
    cases: list[EvalCaseCreate] = []


class SuiteUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


# ── Suite CRUD ──────────────────────────────────────────


@router.get("/evaluations/suites")
async def list_suites(user: User = Depends(current_user)):
    return {"suites": list(_suites.values())}


@router.post("/evaluations/suites")
async def create_suite(body: SuiteCreate, user: User = Depends(current_user)):
    sid = str(uuid.uuid4())
    s = {
        "id": sid,
        "name": body.name,
        "description": body.description,
        "cases": [{"id": str(uuid.uuid4()), **c.model_dump()} for c in body.cases],
        "case_count": len(body.cases),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _suites[sid] = s
    return s


@router.delete("/evaluations/suites/{suite_id}")
async def delete_suite(suite_id: str, user: User = Depends(current_user)):
    if suite_id not in _suites:
        raise HTTPException(status_code=404, detail="Suite not found")
    del _suites[suite_id]
    return {"status": "deleted"}


# ── Run evaluation ──────────────────────────────────────


@router.post("/evaluations/suites/{suite_id}/run")
async def run_evaluation(
    suite_id: str,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    suite = _suites.get(suite_id)
    if not suite:
        raise HTTPException(status_code=404, detail="Suite not found")

    run_id = str(uuid.uuid4())
    started = time.monotonic()
    case_results = []

    for case in suite["cases"]:
        case_start = time.monotonic()
        try:
            scope = {"courses": case.get("scope_courses", [])} if case.get("scope_courses") else None

            result = await ask(
                db=db,
                query=case["question"],
                scope_override=scope,
                mode="normal",
            )

            # Score: did the answer reference expected documents?
            answer_ids = {c["document_id"] for c in result.get("citations", [])}
            expected_ids = set(case.get("expected_document_ids", []))
            recall = len(answer_ids & expected_ids) / len(expected_ids) if expected_ids else 1.0

            # Score: did we find ANY evidence?
            has_evidence = len(result.get("evidence", {}).get("items", [])) > 0

            # Score: citation count
            citation_count = len(result.get("citations", []))

            case_results.append({
                "case_id": case["id"],
                "question": case["question"][:100],
                "pass": has_evidence and (recall > 0 or not expected_ids),
                "has_evidence": has_evidence,
                "recall": round(recall, 2),
                "citation_count": citation_count,
                "latency_ms": round((time.monotonic() - case_start) * 1000),
                "model": result.get("model", ""),
            })
            await db.commit()
        except Exception as e:
            case_results.append({
                "case_id": case["id"],
                "question": case["question"][:100],
                "pass": False,
                "error": str(e)[:200],
                "latency_ms": round((time.monotonic() - case_start) * 1000),
            })

    total = len(case_results)
    passed = sum(1 for c in case_results if c.get("pass"))
    avg_recall = sum(c.get("recall", 0) for c in case_results) / total if total else 0
    avg_latency = sum(c.get("latency_ms", 0) for c in case_results) / total if total else 0

    run = {
        "id": run_id,
        "suite_id": suite_id,
        "suite_name": suite["name"],
        "total": total,
        "passed": passed,
        "pass_rate": round(passed / total, 2) if total else 0,
        "avg_recall": round(avg_recall, 2),
        "avg_latency_ms": round(avg_latency),
        "total_latency_ms": round((time.monotonic() - started) * 1000),
        "case_results": case_results,
        "run_at": datetime.now(timezone.utc).isoformat(),
    }
    _runs.append(run)
    return run


@router.get("/evaluations/runs")
async def list_runs(user: User = Depends(current_user)):
    return {"runs": sorted(_runs, key=lambda r: r["run_at"], reverse=True)}


@router.get("/evaluations/runs/{run_id}")
async def get_run(run_id: str, user: User = Depends(current_user)):
    for r in _runs:
        if r["id"] == run_id:
            return r
    raise HTTPException(status_code=404, detail="Run not found")
