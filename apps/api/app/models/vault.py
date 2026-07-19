"""VaultDocument and DocumentVersion models."""

import uuid as _uuid
from datetime import datetime, timezone

from sqlalchemy import String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin, SoftDeleteMixin


class VaultDocument(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "vault_documents"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    vault_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    relative_path: Mapped[str] = mapped_column(
        String(1000), unique=True, nullable=False
    )
    title: Mapped[str | None] = mapped_column(String(500), nullable=True)
    document_type: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )  # concept, moc, extract, example, etc.
    course_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    project_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status: Mapped[str | None] = mapped_column(String(50), nullable=True)
    mastery: Mapped[str | None] = mapped_column(String(50), nullable=True)
    importance: Mapped[str | None] = mapped_column(String(20), nullable=True)
    verification: Mapped[str | None] = mapped_column(String(50), nullable=True)
    needs_review: Mapped[bool] = mapped_column(Boolean, default=False)

    content_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    frontmatter: Mapped[dict] = mapped_column(JSONB, default=dict)
    markdown_body: Mapped[str | None] = mapped_column(Text, nullable=True)

    modified_at_local: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )
    indexed_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"<VaultDocument {self.relative_path}>"


class DocumentVersion(Base, TimestampMixin):
    __tablename__ = "document_versions"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    document_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("vault_documents.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    content_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    frontmatter: Mapped[dict] = mapped_column(JSONB, default=dict)
    markdown_body: Mapped[str | None] = mapped_column(Text, nullable=True)
    source_device_id: Mapped[str | None] = mapped_column(String(36), nullable=True)

    def __repr__(self) -> str:
        return f"<DocumentVersion doc={self.document_id} hash={self.content_hash[:12]}>"
