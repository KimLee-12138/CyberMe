"""Add document_chunks, knowledge_nodes, knowledge_edges, courses tables.

Revision ID: 003
Revises: 002
Create Date: 2026-07-17
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from pgvector.sqlalchemy import Vector

revision: str = "003"
down_revision: Union[str, None] = "002"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Enable pgvector extension
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")

    # ── Document Chunks ─────────────────────────────────
    op.create_table(
        "document_chunks",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "document_id",
            sa.String(36),
            sa.ForeignKey("vault_documents.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("heading_path", postgresql.JSONB(), server_default=sa.text("'[]'::jsonb")),
        sa.Column("ordinal", sa.Integer(), server_default=sa.text("0")),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("token_count", sa.Integer(), server_default=sa.text("0")),
        sa.Column("page_ref", sa.String(200), nullable=True),
        sa.Column("content_hash", sa.String(64), nullable=False),
        sa.Column("embedding", Vector(1536), nullable=True),
        sa.Column("search_vector", postgresql.TSVECTOR(), nullable=True),
        sa.Column("chunk_metadata", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb")),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # ── Knowledge Nodes ─────────────────────────────────
    op.create_table(
        "knowledge_nodes",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("node_type", sa.String(50), nullable=False, index=True),
        sa.Column("external_key", sa.String(500), nullable=True),
        sa.Column(
            "document_id",
            sa.String(36),
            sa.ForeignKey("vault_documents.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("label", sa.String(500), nullable=False),
        sa.Column("properties", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb")),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # ── Knowledge Edges ─────────────────────────────────
    op.create_table(
        "knowledge_edges",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "source_node_id",
            sa.String(36),
            sa.ForeignKey("knowledge_nodes.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column(
            "target_node_id",
            sa.String(36),
            sa.ForeignKey("knowledge_nodes.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("edge_type", sa.String(50), nullable=False),
        sa.Column("origin", sa.String(20), server_default="derived"),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.Column("evidence", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb")),
        sa.Column("confirmed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # ── Courses ─────────────────────────────────────────
    op.create_table(
        "courses",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("code", sa.String(50), unique=True, nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column(
            "moc_document_id",
            sa.String(36),
            sa.ForeignKey("vault_documents.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("knowledge_count", sa.Integer(), server_default=sa.text("0")),
        sa.Column("extract_count", sa.Integer(), server_default=sa.text("0")),
        sa.Column("last_indexed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )

    # Index for vector search
    op.execute(
        "CREATE INDEX IF NOT EXISTS ix_document_chunks_embedding "
        "ON document_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100)"
    )


def downgrade() -> None:
    op.drop_table("courses")
    op.drop_table("knowledge_edges")
    op.drop_table("knowledge_nodes")
    op.drop_table("document_chunks")
