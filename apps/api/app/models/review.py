"""ReviewCard and ReviewEvent models for FSRS spaced repetition."""

import uuid as _uuid

from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin


class ReviewCard(Base, TimestampMixin):
    __tablename__ = "review_cards"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    knowledge_node_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("knowledge_nodes.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    card_type: Mapped[str] = mapped_column(
        String(20), default="recall", nullable=False
    )  # recall / concept / problem / application

    front: Mapped[str] = mapped_column(Text, nullable=False)
    back: Mapped[str] = mapped_column(Text, nullable=False)

    state: Mapped[str] = mapped_column(
        String(20), default="new", nullable=False
    )  # new / learning / review / relearning

    due_at: Mapped[str] = mapped_column(
        String(35), nullable=False
    )  # ISO-8601 datetime string (TZ-aware)

    stability: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    difficulty: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    reps: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    lapses: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    def __repr__(self) -> str:
        return f"<ReviewCard id={self.id} state={self.state}>"


class ReviewEvent(Base, TimestampMixin):
    __tablename__ = "review_events"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    card_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("review_cards.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    rating: Mapped[int] = mapped_column(Integer, nullable=False)  # 1-4

    state_before: Mapped[str] = mapped_column(String(20), nullable=False)
    state_after: Mapped[str] = mapped_column(String(20), nullable=False)
    stability_before: Mapped[float] = mapped_column(Float, default=0.0)
    stability_after: Mapped[float] = mapped_column(Float, default=0.0)
    difficulty_before: Mapped[float] = mapped_column(Float, default=0.0)
    difficulty_after: Mapped[float] = mapped_column(Float, default=0.0)

    time_spent_ms: Mapped[int | None] = mapped_column(Integer, nullable=True)

    def __repr__(self) -> str:
        return f"<ReviewEvent card={self.card_id} rating={self.rating}>"
