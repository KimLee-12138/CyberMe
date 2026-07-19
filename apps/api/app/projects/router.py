"""Project management API — CRUD for projects, hypotheses, experiments, risks."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import get_db
from app.models.project import Experiment, Hypothesis, Project, Risk
from app.models.user import User

router = APIRouter(prefix="/api/v1")

# ── Schemas ──────────────────────────────────────────────


class ProjectCreate(BaseModel):
    title: str = Field(..., max_length=300)
    goal: str | None = None
    success_criteria: str | None = None
    constraints: str | None = None
    deadline: str | None = None


class ProjectUpdate(BaseModel):
    title: str | None = None
    goal: str | None = None
    success_criteria: str | None = None
    constraints: str | None = None
    deadline: str | None = None
    status: str | None = None


class HypothesisCreate(BaseModel):
    statement: str
    verification_criteria: str | None = None


class HypothesisUpdate(BaseModel):
    statement: str | None = None
    verification_criteria: str | None = None
    status: str | None = None
    evidence_for: str | None = None
    evidence_against: str | None = None


class ExperimentCreate(BaseModel):
    design: str | None = None
    environment: str | None = None
    code_version: str | None = None
    parameters: dict | None = None
    metrics: dict | None = None
    result: dict | None = None
    failed: bool = False
    lessons_learned: str | None = None


class RiskCreate(BaseModel):
    description: str
    probability: float = Field(default=0.5, ge=0, le=1)
    impact: str = "medium"
    trigger_signals: str | None = None
    mitigation: str | None = None


class RiskUpdate(BaseModel):
    description: str | None = None
    probability: float | None = None
    impact: str | None = None
    trigger_signals: str | None = None
    mitigation: str | None = None
    status: str | None = None


# ── Projects CRUD ────────────────────────────────────────


@router.get("/projects")
async def list_projects(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Project)
        .where(Project.user_id == user.id)
        .order_by(Project.updated_at.desc())
    )
    projects = result.scalars().all()

    # Get counts for each project
    project_ids = [p.id for p in projects]
    counts = {}
    if project_ids:
        for model, key in [(Hypothesis, "hypotheses"), (Experiment, "experiments"), (Risk, "risks")]:
            r = await db.execute(
                select(func.count()).select_from(model).where(model.project_id.in_(project_ids))
            )
            counts[key] = r.scalar() or 0

    return {
        "projects": [
            {
                "id": p.id,
                "title": p.title,
                "goal": p.goal,
                "status": p.status,
                "deadline": p.deadline,
                "created_at": p.created_at.isoformat() if p.created_at else None,
                "updated_at": p.updated_at.isoformat() if p.updated_at else None,
            }
            for p in projects
        ]
    }


@router.post("/projects")
async def create_project(
    body: ProjectCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    p = Project(
        id=str(uuid.uuid4()),
        user_id=user.id,
        title=body.title,
        goal=body.goal,
        success_criteria=body.success_criteria,
        constraints=body.constraints,
        deadline=body.deadline,
        status="active",
    )
    db.add(p)
    await db.commit()
    return {"id": p.id, "title": p.title, "status": p.status}


@router.get("/projects/{project_id}")
async def get_project(
    project_id: str,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    p = result.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")

    # Fetch sub-items
    h_result = await db.execute(
        select(Hypothesis).where(Hypothesis.project_id == project_id).order_by(Hypothesis.created_at.desc())
    )
    e_result = await db.execute(
        select(Experiment).where(Experiment.project_id == project_id).order_by(Experiment.created_at.desc())
    )
    r_result = await db.execute(
        select(Risk).where(Risk.project_id == project_id).order_by(Risk.created_at.desc())
    )

    return {
        "id": p.id,
        "title": p.title,
        "goal": p.goal,
        "success_criteria": p.success_criteria,
        "constraints": p.constraints,
        "deadline": p.deadline,
        "status": p.status,
        "created_at": p.created_at.isoformat() if p.created_at else None,
        "hypotheses": [
            {"id": h.id, "statement": h.statement, "verification_criteria": h.verification_criteria,
             "status": h.status, "evidence_for": h.evidence_for, "evidence_against": h.evidence_against}
            for h in h_result.scalars().all()
        ],
        "experiments": [
            {"id": e.id, "design": e.design, "environment": e.environment,
             "code_version": e.code_version, "parameters": e.parameters,
             "metrics": e.metrics, "result": e.result, "failed": e.failed,
             "lessons_learned": e.lessons_learned}
            for e in e_result.scalars().all()
        ],
        "risks": [
            {"id": r.id, "description": r.description, "probability": r.probability,
             "impact": r.impact, "trigger_signals": r.trigger_signals,
             "mitigation": r.mitigation, "status": r.status}
            for r in r_result.scalars().all()
        ],
    }


@router.patch("/projects/{project_id}")
async def update_project(
    project_id: str,
    body: ProjectUpdate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    p = result.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    for field in ["title", "goal", "success_criteria", "constraints", "deadline", "status"]:
        val = getattr(body, field, None)
        if val is not None:
            setattr(p, field, val)
    await db.commit()
    return {"id": p.id, "status": "updated"}


@router.delete("/projects/{project_id}")
async def delete_project(
    project_id: str,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    p = result.scalar_one_or_none()
    if not p:
        raise HTTPException(status_code=404, detail="Project not found")
    await db.delete(p)
    await db.commit()
    return {"status": "deleted"}


# ── Hypotheses ───────────────────────────────────────────


@router.post("/projects/{project_id}/hypotheses")
async def create_hypothesis(
    project_id: str, body: HypothesisCreate,
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db),
):
    h = Hypothesis(id=str(uuid.uuid4()), project_id=project_id, **body.model_dump())
    db.add(h)
    await db.commit()
    return {"id": h.id, "status": "created"}


@router.patch("/projects/{project_id}/hypotheses/{hypothesis_id}")
async def update_hypothesis(
    project_id: str, hypothesis_id: str, body: HypothesisUpdate,
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Hypothesis).where(Hypothesis.id == hypothesis_id, Hypothesis.project_id == project_id)
    )
    h = result.scalar_one_or_none()
    if not h:
        raise HTTPException(status_code=404, detail="Hypothesis not found")
    for f in ["statement", "verification_criteria", "status", "evidence_for", "evidence_against"]:
        val = getattr(body, f, None)
        if val is not None:
            setattr(h, f, val)
    await db.commit()
    return {"id": h.id, "status": "updated"}


# ── Experiments ──────────────────────────────────────────


@router.post("/projects/{project_id}/experiments")
async def create_experiment(
    project_id: str, body: ExperimentCreate,
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db),
):
    e = Experiment(id=str(uuid.uuid4()), project_id=project_id, **body.model_dump(exclude_none=True))
    db.add(e)
    await db.commit()
    return {"id": e.id, "status": "created"}


# ── Risks ────────────────────────────────────────────────


@router.post("/projects/{project_id}/risks")
async def create_risk(
    project_id: str, body: RiskCreate,
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db),
):
    r = Risk(id=str(uuid.uuid4()), project_id=project_id, **body.model_dump())
    db.add(r)
    await db.commit()
    return {"id": r.id, "status": "created"}


@router.patch("/projects/{project_id}/risks/{risk_id}")
async def update_risk(
    project_id: str, risk_id: str, body: RiskUpdate,
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Risk).where(Risk.id == risk_id, Risk.project_id == project_id)
    )
    r = result.scalar_one_or_none()
    if not r:
        raise HTTPException(status_code=404, detail="Risk not found")
    for f in ["description", "probability", "impact", "trigger_signals", "mitigation", "status"]:
        val = getattr(body, f, None)
        if val is not None:
            setattr(r, f, val)
    await db.commit()
    return {"id": r.id, "status": "updated"}
