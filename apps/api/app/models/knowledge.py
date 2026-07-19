"""DocumentChunk, KnowledgeNode, KnowledgeEdge, and Course models."""

import uuid as _uuid

from pgvector.sqlalchemy import Vector
from sqlalchemy import String, Integer, Float, ForeignKey, Text, DateTime
from sqlalchemy.dialects.postgresql import JSONB, TSVECTOR
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin


class DocumentChunk(Base, TimestampMixin):
    __tablename__ = "document_chunks"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    document_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("vault_documents.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    heading_path: Mapped[list] = mapped_column(JSONB, default=list)  # ["课程", "章节", "小节"]
    ordinal: Mapped[int] = mapped_column(Integer, default=0)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    token_count: Mapped[int] = mapped_column(Integer, default=0)
    page_ref: Mapped[str | None] = mapped_column(String(200), nullable=True)
    content_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(1536), nullable=True
    )  # OpenAI text-embedding-3-small = 1536 dims
    search_vector: Mapped[str | None] = mapped_column(
        TSVECTOR, nullable=True
    )  # PostgreSQL full-text search
    chunk_metadata: Mapped[dict] = mapped_column(
        JSONB, default=dict
    )  # source, status, credibility

    def __repr__(self) -> str:
        return f"<DocumentChunk doc={self.document_id} ord={self.ordinal}>"


class KnowledgeNode(Base, TimestampMixin):
    __tablename__ = "knowledge_nodes"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    node_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True
    )  # vault-map, course-moc, chapter, concept, formula, example, mistake, extract, source, project, self-fact, inference
    external_key: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )  # External identifier (e.g. "DB_数据库" for course-moc)
    document_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("vault_documents.id", ondelete="SET NULL"),
        nullable=True,
    )
    label: Mapped[str] = mapped_column(String(500), nullable=False)
    properties: Mapped[dict] = mapped_column(JSONB, default=dict)

    def __repr__(self) -> str:
        return f"<KnowledgeNode type={self.node_type} label={self.label[:30]}>"


class KnowledgeEdge(Base, TimestampMixin):
    __tablename__ = "knowledge_edges"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    source_node_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("knowledge_nodes.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    target_node_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("knowledge_nodes.id", ondelete="CASCADE"),
        nullable=False, index=True,
    )
    edge_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # belongs_to, prerequisite_of, contrasts_with, applies_to, example_of, sourced_from, conflicts_with, related_to, candidate_link
    origin: Mapped[str] = mapped_column(
        String(20), default="derived"
    )  # vault, derived, ai_candidate
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)
    evidence: Mapped[dict] = mapped_column(JSONB, default=dict)
    confirmed_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"<KnowledgeEdge {self.edge_type}>"


class Course(Base, TimestampMixin):
    __tablename__ = "courses"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    moc_document_id: Mapped[str | None] = mapped_column(
        String(36), ForeignKey("vault_documents.id", ondelete="SET NULL"),
        nullable=True,
    )
    knowledge_count: Mapped[int] = mapped_column(Integer, default=0)
    extract_count: Mapped[int] = mapped_column(Integer, default=0)
    last_indexed_at: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    def __repr__(self) -> str:
        return f"<Course {self.code} — {self.name}>"
