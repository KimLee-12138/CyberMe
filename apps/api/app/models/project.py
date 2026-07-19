"""Project, Hypothesis, Experiment, Risk models."""

import uuid as _uuid

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin


class Project(Base, TimestampMixin):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(_uuid.uuid4()))
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(300), nullable=False)
    goal: Mapped[str | None] = mapped_column(Text, nullable=True)
    success_criteria: Mapped[str | None] = mapped_column(Text, nullable=True)
    constraints: Mapped[str | None] = mapped_column(Text, nullable=True)
    deadline: Mapped[str | None] = mapped_column(String(30), nullable=True)  # ISO date string
    status: Mapped[str] = mapped_column(String(20), default="active")  # active/completed/archived
    knowledge_tags: Mapped[dict] = mapped_column(JSONB, default=dict)  # {course_codes: [...], topics: [...]}

    def __repr__(self) -> str:
        return f"<Project {self.title}>"


class Hypothesis(Base, TimestampMixin):
    __tablename__ = "hypotheses"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(_uuid.uuid4()))
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    statement: Mapped[str] = mapped_column(Text, nullable=False)
    verification_criteria: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="proposed")  # proposed/testing/confirmed/rejected
    evidence_for: Mapped[str | None] = mapped_column(Text, nullable=True)
    evidence_against: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Hypothesis {self.statement[:50]}>"


class Experiment(Base, TimestampMixin):
    __tablename__ = "experiments"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(_uuid.uuid4()))
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    design: Mapped[str | None] = mapped_column(Text, nullable=True)
    environment: Mapped[str | None] = mapped_column(Text, nullable=True)
    code_version: Mapped[str | None] = mapped_column(String(100), nullable=True)
    parameters: Mapped[dict] = mapped_column(JSONB, default=dict)
    metrics: Mapped[dict] = mapped_column(JSONB, default=dict)
    result: Mapped[dict] = mapped_column(JSONB, default=dict)
    failed: Mapped[bool] = mapped_column(Boolean, default=False)
    lessons_learned: Mapped[str | None] = mapped_column(Text, nullable=True)

    def __repr__(self) -> str:
        return f"<Experiment id={self.id}>"


class Risk(Base, TimestampMixin):
    __tablename__ = "risks"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(_uuid.uuid4()))
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    probability: Mapped[float] = mapped_column(Float, default=0.5)
    impact: Mapped[str] = mapped_column(String(20), default="medium")  # low/medium/high/critical
    trigger_signals: Mapped[str | None] = mapped_column(Text, nullable=True)
    mitigation: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(20), default="open")  # open/monitoring/resolved

    def __repr__(self) -> str:
        return f"<Risk {self.description[:50]}>"
