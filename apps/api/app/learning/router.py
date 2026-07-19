"""Learning API — dashboard, reviews, FSRS, tutor sessions."""

import uuid
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import func, select, text

from app.learning import tutor
from app.learning import writing as writing_engine
from app.learning import decisions as decisions_engine
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import engine, get_db
from app.learning.fsrs import new_card, schedule
from app.model_gateway.budget import get_budget_status
from app.models.audit import AuditEvent
from app.models.device import Device
from app.models.knowledge import Course, DocumentChunk, KnowledgeEdge, KnowledgeNode
from app.models.review import ReviewCard, ReviewEvent
from app.models.user import User
from app.models.vault import VaultDocument

router = APIRouter(prefix="/api/v1")


@router.get("/learning/dashboard")
async def get_dashboard(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Return the full dashboard: actions, reviews, debt, health."""

    # ── Due Reviews (needs_review=True, sorted by importance) ──────
    due_review_count = await db.scalar(
        select(func.count()).select_from(VaultDocument).where(
            VaultDocument.needs_review == True,
            VaultDocument.deleted_at.is_(None),
        )
    ) or 0

    due_docs_result = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.needs_review == True,
            VaultDocument.deleted_at.is_(None),
        )
        .order_by(
            # Critical/high first, then by title
            func.coalesce(
                func.nullif(VaultDocument.importance, ""),
                "low",
            ).desc(),
            VaultDocument.title,
        )
        .limit(10)
    )
    due_docs = due_docs_result.scalars().all()

    due_reviews = {
        "count": due_review_count,
        "documents": [
            {
                "id": d.id,
                "title": d.title,
                "mastery": d.mastery or "unknown",
                "importance": d.importance or "medium",
                "course_code": d.course_code,
            }
            for d in due_docs
        ],
    }

    # ── Knowledge Debt ─────────────────────────────────────────────

    # High importance + low mastery
    high_important_low = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.importance.in_(["high", "critical"]),
            VaultDocument.deleted_at.is_(None),
        )
        .limit(10)
    )
    high_important_low_docs = high_important_low.scalars().all()

    high_important_low_count = await db.scalar(
        select(func.count()).select_from(VaultDocument).where(
            VaultDocument.importance.in_(["high", "critical"]),
            VaultDocument.deleted_at.is_(None),
        )
    ) or 0

    # Missing verification
    missing_verification_count = await db.scalar(
        select(func.count()).select_from(VaultDocument).where(
            VaultDocument.verification.is_(None),
            VaultDocument.deleted_at.is_(None),
        )
    ) or 0

    missing_ver_docs = await db.execute(
        select(VaultDocument)
        .where(
            VaultDocument.verification.is_(None),
            VaultDocument.deleted_at.is_(None),
        )
        .limit(5)
    )

    # Orphaned nodes
    orphaned_count = await db.scalar(
        select(func.count())
        .select_from(KnowledgeNode)
        .where(
            ~KnowledgeNode.id.in_(
                select(KnowledgeEdge.source_node_id).union(
                    select(KnowledgeEdge.target_node_id)
                )
            )
        )
    ) or 0

    knowledge_debt = {
        "high_importance_low_mastery": {
            "count": high_important_low_count,
            "documents": [
                {
                    "id": d.id,
                    "title": d.title,
                    "importance": d.importance,
                    "mastery": d.mastery or "unknown",
                }
                for d in high_important_low_docs
            ],
        },
        "missing_verification": {
            "count": missing_verification_count,
            "sample": [
                {"id": d.id, "title": d.title}
                for d in missing_ver_docs.scalars().all()
            ],
        },
        "orphaned_nodes": {"count": orphaned_count},
        "needs_review_total": due_review_count,
    }

    # ── Digital Twin ────────────────────────────────────────────────

    ai_candidate_edges = await db.scalar(
        select(func.count()).select_from(KnowledgeEdge).where(
            KnowledgeEdge.origin == "ai_candidate"
        )
    ) or 0

    yesterday = datetime.now(timezone.utc) - timedelta(hours=24)
    recent_audit_count = await db.scalar(
        select(func.count()).select_from(AuditEvent).where(
            AuditEvent.occurred_at >= yesterday,
        )
    ) or 0

    digital_twin = {
        "ai_candidate_edges": ai_candidate_edges,
        "recent_audit_count": recent_audit_count,
    }

    # ── System Health ──────────────────────────────────────────────

    doc_count = await db.scalar(
        select(func.count()).select_from(VaultDocument).where(
            VaultDocument.deleted_at.is_(None),
        )
    ) or 0

    chunk_count = await db.scalar(
        select(func.count()).select_from(DocumentChunk)
    ) or 0

    course_count = await db.scalar(
        select(func.count()).select_from(Course)
    ) or 0

    # Sync status
    sync_status = "no_devices"
    sync_last_seen = None
    devices_result = await db.execute(
        select(Device).where(
            Device.user_id == user.id,
            Device.revoked_at.is_(None),
        )
        .order_by(Device.last_seen_at.desc().nullslast())
        .limit(1)
    )
    device = devices_result.scalar_one_or_none()
    if device:
        sync_status = "connected"
        sync_last_seen = device.last_seen_at.isoformat() if device.last_seen_at else None

    # Budget
    budget = get_budget_status()

    # DB + Redis
    db_status = "disconnected"
    redis_status = "disconnected"
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        pass
    try:
        import redis.asyncio as aioredis
        from app.core.config import settings
        r = aioredis.from_url(settings.redis_url)
        await r.ping()
        await r.close()
        redis_status = "connected"
    except Exception:
        pass

    system_health = {
        "document_count": doc_count,
        "chunk_count": chunk_count,
        "course_count": course_count,
        "sync": {
            "status": sync_status,
            "last_seen": sync_last_seen,
        },
        "budget": budget,
        "database": db_status,
        "redis": redis_status,
    }

    # ── Top Actions ─────────────────────────────────────────────────

    top_actions: list[dict] = []

    # 1. Due reviews — top 3 by importance
    for d in due_docs[:3]:
        top_actions.append({
            "type": "review",
            "title": f"复习: {d.title or '未命名'}",
            "description": f"掌握度: {d.mastery or 'unknown'} | 课程: {d.course_code or '无'}",
            "priority": "critical" if d.importance == "high" else "warning",
            "link": f"/knowledge/{d.id}",
        })

    # 2. High-importance debt items — 2 items
    debt_displayed = {d.id for d in due_docs[:3]}
    for d in high_important_low_docs:
        if d.id in debt_displayed:
            continue
        if len([a for a in top_actions if a["type"] == "debt"]) >= 2:
            break
        top_actions.append({
            "type": "debt",
            "title": f"强化掌握: {d.title or '未命名'}",
            "description": f"重要程度: {d.importance} | 当前掌握: {d.mastery or 'unknown'}",
            "priority": "warning",
            "link": f"/knowledge/{d.id}",
        })

    # 3. Orphan nodes
    if orphaned_count > 0:
        top_actions.append({
            "type": "orphan",
            "title": f"整理孤立的 {orphaned_count} 个知识节点",
            "description": "这些节点没有关联任何其他知识，可能遗漏了课程归属或 WikiLink",
            "priority": "warning",
            "link": "/graph",
        })

    # 4. Missing verification
    if missing_verification_count > 100:
        top_actions.append({
            "type": "debt",
            "title": f"补充来源校验: {missing_verification_count} 篇文档缺少验证",
            "description": "大量文档未标注来源和验证状态，建议逐批次核对",
            "priority": "warning",
            "link": "/courses",
        })

    # 5. Pending inferences (stub)
    if ai_candidate_edges > 0:
        top_actions.append({
            "type": "inference",
            "title": f"待确认AI关联: {ai_candidate_edges} 条候选边",
            "description": "AI 发现的潜在知识关联等待您的确认",
            "priority": "info",
            "link": "/graph",
        })

    # ── Project Overview (real data) ───────────────────────────────
    from app.models.project import Project, Hypothesis, Risk

    proj_count = await db.scalar(select(func.count()).select_from(Project)) or 0
    hyp_result = await db.execute(
        select(Hypothesis).order_by(Hypothesis.created_at.desc()).limit(10))
    hypotheses = hyp_result.scalars().all()
    risk_result = await db.execute(
        select(Risk).where(Risk.status == 'open').order_by(Risk.impact.desc()).limit(5))
    open_risks = risk_result.scalars().all()
    proj_result = await db.execute(
        select(Project).order_by(Project.updated_at.desc()).limit(5))
    recent_projects = proj_result.scalars().all()

    project_risks = {
        "stub": False,
        "total_projects": proj_count,
        "total_hypotheses": len(hypotheses),
        "total_open_risks": len(open_risks),
        "recent_projects": [
            {"id": p.id, "title": p.title, "status": p.status, "deadline": p.deadline}
            for p in recent_projects
        ],
        "open_risks": [
            {"id": r.id, "description": r.description[:80], "impact": r.impact, "probability": r.probability}
            for r in open_risks
        ],
    }

    return {
        "top_actions": top_actions,
        "due_reviews": due_reviews,
        "knowledge_debt": knowledge_debt,
        "project_risks": project_risks,
        "digital_twin": digital_twin,
        "system_health": system_health,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


# ── Review API ───────────────────────────────────────────


class GradeRequest(BaseModel):
    rating: int = Field(..., ge=1, le=4)


CARD_TYPES = ["recall", "concept", "problem", "application"]


@router.get("/reviews/due")
async def get_due_reviews(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
    limit: int = 20,
):
    """Get due review cards. Auto-generates cards from knowledge nodes if none exist."""
    now = datetime.now(timezone.utc).isoformat()

    # Fetch due cards (state != 'new' or freshly generated)
    due_result = await db.execute(
        select(ReviewCard)
        .where(
            ReviewCard.user_id == user.id,
            ReviewCard.due_at <= now,
        )
        .order_by(ReviewCard.due_at.asc())
        .limit(limit)
    )
    due_cards = due_result.scalars().all()

    # Auto-generate new cards if none exist
    if not due_cards:
        # Check if user has any cards at all
        any_cards = await db.scalar(
            select(func.count()).select_from(ReviewCard).where(
                ReviewCard.user_id == user.id,
            )
        ) or 0

        if any_cards == 0:
            await _generate_cards(db, user.id)
            # Fetch the newly generated cards
            gen_result = await db.execute(
                select(ReviewCard)
                .where(ReviewCard.user_id == user.id)
                .order_by(ReviewCard.due_at.asc())
                .limit(limit)
            )
            due_cards = gen_result.scalars().all()

    total_due = await db.scalar(
        select(func.count()).select_from(ReviewCard).where(
            ReviewCard.user_id == user.id,
            ReviewCard.due_at <= now,
        )
    ) or 0

    # Also check if we need to generate more (existing cards low)
    if len(due_cards) < 5 and (await db.scalar(
        select(func.count()).select_from(ReviewCard).where(ReviewCard.user_id == user.id)
    ) or 0) > 0:
        await _ensure_cards(db, user.id, min_count=10)

    await db.commit()

    return {
        "cards": [
            {
                "id": c.id,
                "card_type": c.card_type,
                "front": c.front,
                "back": c.back,
                "state": c.state,
                "due_at": c.due_at,
                "stability": c.stability,
                "difficulty": c.difficulty,
                "reps": c.reps,
                "lapses": c.lapses,
            }
            for c in due_cards
        ],
        "total_due": total_due,
    }


@router.post("/reviews/{card_id}/grade")
async def grade_card(
    card_id: str,
    body: GradeRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Submit a review rating for a card."""
    result = await db.execute(
        select(ReviewCard).where(
            ReviewCard.id == card_id,
            ReviewCard.user_id == user.id,
        )
    )
    card = result.scalar_one_or_none()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    # Record pre-state
    state_before = card.state
    stability_before = card.stability
    difficulty_before = card.difficulty

    # Apply FSRS scheduling
    card_state = {
        "state": card.state,
        "stability": card.stability,
        "difficulty": card.difficulty,
        "reps": card.reps,
        "lapses": card.lapses,
        "due_at": card.due_at,
    }
    updated = schedule(card_state, body.rating)

    # Update card
    card.state = updated["state"]
    card.stability = updated["stability"]
    card.difficulty = updated["difficulty"]
    card.reps = updated["reps"]
    card.lapses = updated["lapses"]
    card.due_at = updated["due_at"]

    # Log event
    event = ReviewEvent(
        id=str(uuid.uuid4()),
        card_id=card_id,
        user_id=user.id,
        rating=body.rating,
        state_before=state_before,
        state_after=updated["state"],
        stability_before=stability_before,
        stability_after=updated["stability"],
        difficulty_before=difficulty_before,
        difficulty_after=updated["difficulty"],
    )
    db.add(event)
    await db.commit()

    return {
        "id": card.id,
        "card_type": card.card_type,
        "front": card.front,
        "back": card.back,
        "state": card.state,
        "due_at": card.due_at,
        "stability": card.stability,
        "difficulty": card.difficulty,
        "reps": card.reps,
        "lapses": card.lapses,
        "scheduled_interval": updated.get("interval_seconds", 0),
    }


# ── Review Stats ───────────────────────────────────────────

@router.get("/reviews/stats")
async def get_review_stats(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Return review statistics for dashboard display."""
    now = datetime.now(timezone.utc)
    today_start = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

    # Total cards
    total_cards = await db.scalar(
        select(func.count()).select_from(ReviewCard).where(ReviewCard.user_id == user.id)) or 0

    # Cards due today
    cards_due = await db.scalar(
        select(func.count()).select_from(ReviewCard).where(
            ReviewCard.user_id == user.id, ReviewCard.due_at <= now.isoformat())) or 0

    # Average stability
    avg_stab = await db.scalar(
        select(func.avg(ReviewCard.stability)).where(ReviewCard.user_id == user.id, ReviewCard.stability > 0)) or 0

    # Average difficulty
    avg_diff = await db.scalar(
        select(func.avg(ReviewCard.difficulty)).where(ReviewCard.user_id == user.id)) or 0

    # Today's reviews
    today_reviews = await db.scalar(
        select(func.count()).select_from(ReviewEvent).where(
            ReviewEvent.user_id == user.id,
            ReviewEvent.created_at >= today_start,
        )) or 0

    # State distribution
    state_result = await db.execute(
        select(ReviewCard.state, func.count()).where(ReviewCard.user_id == user.id).group_by(ReviewCard.state))
    states = {row[0]: row[1] for row in state_result.fetchall()}

    # Rating distribution (last 30 days)
    month_ago = (now.replace(hour=0, minute=0, second=0, microsecond=0) - __import__('datetime').timedelta(days=30)).isoformat()
    rating_result = await db.execute(
        select(ReviewEvent.rating, func.count()).where(
            ReviewEvent.user_id == user.id,
            ReviewEvent.created_at >= month_ago,
        ).group_by(ReviewEvent.rating))
    ratings = {row[0]: row[1] for row in rating_result.fetchall()}

    # Total reviews
    total_reviews = sum(ratings.values())

    # Retention rate: rating >= 3 means correct recall
    correct_recalls = sum(v for k, v in ratings.items() if k >= 3)
    total_with_rating = sum(ratings.values())
    retention = round(correct_recalls / total_with_rating * 100, 1) if total_with_rating > 0 else 0

    return {
        "total_cards": total_cards,
        "cards_due_today": cards_due,
        "reviews_today": today_reviews,
        "total_reviews_30d": total_reviews,
        "avg_stability": round(avg_stab, 2),
        "avg_difficulty": round(avg_diff, 2),
        "retention_rate": retention,
        "state_distribution": states,
        "rating_distribution_30d": ratings,
    }


# ── Card generation helpers ───────────────────────────────


async def _generate_cards(db: AsyncSession, user_id: str) -> None:
    """Generate review cards from knowledge nodes for a user."""
    # Get knowledge nodes that don't already have cards
    existing = await db.execute(
        select(ReviewCard.knowledge_node_id).where(ReviewCard.user_id == user_id)
    )
    existing_ids = {row[0] for row in existing.fetchall()}

    nodes_result = await db.execute(
        select(KnowledgeNode)
        .where(
            KnowledgeNode.node_type.in_(["concept", "formula", "example", "chapter"]),
            ~KnowledgeNode.id.in_(existing_ids) if existing_ids else True,
        )
        .limit(30)
    )
    nodes = nodes_result.scalars().all()

    for node in nodes:
        # Get document content for card back
        doc_content = ""
        if node.document_id:
            doc_result = await db.execute(
                select(VaultDocument).where(VaultDocument.id == node.document_id)
            )
            doc = doc_result.scalar_one_or_none()
            if doc and doc.markdown_body:
                doc_content = doc.markdown_body[:500]

        course_code = node.properties.get("course_code", "") if node.properties else ""

        card_type = "recall"
        if node.node_type == "example":
            card_type = "problem"
        elif node.node_type == "formula":
            card_type = "concept"

        card = ReviewCard(
            id=str(uuid.uuid4()),
            knowledge_node_id=node.id,
            user_id=user_id,
            card_type=card_type,
            front=f"【{course_code}】{node.label}" if course_code else node.label,
            back=doc_content or node.label,
            state="new",
            due_at=datetime.now(timezone.utc).isoformat(),
            stability=0.0,
            difficulty=0.0,
            reps=0,
            lapses=0,
        )
        db.add(card)


async def _ensure_cards(db: AsyncSession, user_id: str, min_count: int = 10) -> None:
    """Ensure the user has at least min_count review cards."""
    count = await db.scalar(
        select(func.count()).select_from(ReviewCard).where(ReviewCard.user_id == user_id)
    ) or 0
    if count < min_count:
        # Get more knowledge nodes
        existing = await db.execute(
            select(ReviewCard.knowledge_node_id).where(ReviewCard.user_id == user_id)
        )
        existing_ids = {row[0] for row in existing.fetchall()}

        nodes_result = await db.execute(
            select(KnowledgeNode)
            .where(
                KnowledgeNode.node_type.in_(["concept", "formula", "example", "chapter"]),
                ~KnowledgeNode.id.in_(existing_ids) if existing_ids else True,
            )
            .offset(count)
            .limit(min_count - count + 10)
        )
        nodes = nodes_result.scalars().all()

        for node in nodes:
            doc_content = ""
            if node.document_id:
                doc_result = await db.execute(
                    select(VaultDocument).where(VaultDocument.id == node.document_id)
                )
                doc = doc_result.scalar_one_or_none()
                if doc and doc.markdown_body:
                    doc_content = doc.markdown_body[:500]

            course_code = node.properties.get("course_code", "") if node.properties else ""

            card = ReviewCard(
                id=str(uuid.uuid4()),
                knowledge_node_id=node.id,
                user_id=user_id,
                card_type="recall",
                front=f"【{course_code}】{node.label}" if course_code else node.label,
                back=doc_content or node.label,
                state="new",
                due_at=datetime.now(timezone.utc).isoformat(),
                stability=0.0,
                difficulty=0.0,
                reps=0,
                lapses=0,
            )
            db.add(card)


# ── Tutor Session API ─────────────────────────────────────


class CreateSessionRequest(BaseModel):
    mode: str = Field(..., pattern="^(concept|socratic|closed_book|step_by_step|mock_exam|mistake_retrain)$")
    topic: str = Field(..., min_length=1, max_length=300)
    course_code: str | None = None
    num_questions: int = Field(default=3, ge=1, le=10)


class SessionResponse(BaseModel):
    session_id: str
    mode: str
    content: str
    complete: bool


@router.post("/learning/sessions")
async def create_session(
    body: CreateSessionRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new tutoring session."""
    if body.mode == "concept":
        return await tutor.start_concept_explanation(db, body.topic)
    elif body.mode == "socratic":
        return await tutor.start_socratic(db, body.topic)
    elif body.mode == "closed_book":
        return await tutor.start_closed_book(db, body.topic)
    elif body.mode == "step_by_step":
        return await tutor.start_step_by_step(db, body.topic)
    elif body.mode == "mock_exam":
        return await tutor.start_mock_exam(db, body.topic, body.num_questions)
    elif body.mode == "mistake_retrain":
        return await tutor.start_mistake_retrain(db, body.topic)
    else:
        raise HTTPException(status_code=400, detail=f"Unknown mode: {body.mode}")


@router.post("/learning/sessions/{session_id}/responses")
async def submit_response(
    session_id: str,
    body: dict,
    user: User = Depends(current_user),
):
    """Submit an answer to a tutoring session."""
    session = tutor._sessions.get(session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    answer = body.get("answer", "")
    if not answer:
        raise HTTPException(status_code=400, detail="Answer is required")

    mode = session["mode"]
    if mode == "socratic":
        return await tutor.continue_socratic(session, answer)
    elif mode == "closed_book":
        return await tutor.check_closed_book(session, answer)
    elif mode == "step_by_step":
        return await tutor.continue_step(session, answer)
    elif mode == "mock_exam":
        return await tutor.submit_exam(session, answer)
    elif mode == "mistake_retrain":
        # For mistake retrain, just check answer against stored answers
        return await tutor.check_closed_book(session, answer)
    else:
        raise HTTPException(status_code=400, detail=f"Mode {mode} doesn't accept responses")


@router.post("/learning/sessions/{session_id}/complete")
async def complete_session(
    session_id: str,
    user: User = Depends(current_user),
):
    """End a tutoring session."""
    session = tutor._sessions.pop(session_id, None)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return {
        "session_id": session_id,
        "mode": session["mode"],
        "topic": session["topic"],
        "rounds": len([h for h in session["history"] if h["role"] == "user"]),
        "completed_at": datetime.now(timezone.utc).isoformat(),
    }


# ── Writing Studio API ────────────────────────────────────


class WritingGenerateRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=300)
    output_type: str = Field(default="report", pattern="^(report|summary|essay|presentation|resume)$")
    course_code: str | None = None


class WritingAuditRequest(BaseModel):
    text: str = Field(..., min_length=1)


@router.post("/writing/generate")
async def generate_writing(
    body: WritingGenerateRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Generate a draft document based on knowledge base."""
    scope = {"courses": [body.course_code]} if body.course_code else None
    return await writing_engine.generate(db, body.topic, body.output_type, scope)


@router.post("/writing/audit")
async def audit_writing(
    body: WritingAuditRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Audit text for fact sources."""
    return await writing_engine.audit(body.text)


# ── Decision Lab API ──────────────────────────────────────


class DecisionCreateRequest(BaseModel):
    topic: str = Field(..., min_length=1, max_length=500)
    context: str = ""


@router.post("/decisions")
async def create_decision(
    body: DecisionCreateRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new decision analysis with four-role review."""
    return await decisions_engine.analyze(db, body.topic, body.context)


@router.get("/decisions")
async def list_decisions(
    user: User = Depends(current_user),
):
    """List all past decisions."""
    return {"decisions": decisions_engine.get_decisions()}


@router.get("/decisions/{decision_id}")
async def get_decision(
    decision_id: str,
    user: User = Depends(current_user),
):
    """Get a specific decision with analyses."""
    d = decisions_engine.get_decision(decision_id)
    if not d:
        raise HTTPException(status_code=404, detail="Decision not found")
    return d
