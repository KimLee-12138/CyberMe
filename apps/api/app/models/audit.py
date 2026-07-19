"""AuditEvent model — immutable audit trail."""

import uuid as _uuid
from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class AuditEvent(Base):
    __tablename__ = "audit_events"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    user_id: Mapped[str | None] = mapped_column(String(36), nullable=True, index=True)
    device_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    action: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True
    )  # e.g. login, logout, sync.upsert, writeback.approve
    resource_type: Mapped[str | None] = mapped_column(
        String(100), nullable=True
    )  # e.g. user, device, document
    resource_id: Mapped[str | None] = mapped_column(String(36), nullable=True)
    result: Mapped[str] = mapped_column(
        String(50), default="success"
    )  # success, failure, denied
    ip_summary: Mapped[str | None] = mapped_column(
        String(45), nullable=True
    )  # Hashed or truncated IP
    user_agent_summary: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    detail: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    occurred_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        index=True,
    )

    def __repr__(self) -> str:
        return f"<AuditEvent action={self.action} result={self.result}>"
