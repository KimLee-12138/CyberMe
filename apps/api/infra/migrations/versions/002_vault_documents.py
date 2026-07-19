"""Add vault_documents and document_versions tables.

Revision ID: 002
Revises: 001
Create Date: 2026-07-17
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "002"
down_revision: Union[str, None] = "001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "vault_documents",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("vault_id", sa.String(36), nullable=False, index=True),
        sa.Column("relative_path", sa.String(1000), unique=True, nullable=False),
        sa.Column("title", sa.String(500), nullable=True),
        sa.Column("document_type", sa.String(50), nullable=True),
        sa.Column("course_code", sa.String(50), nullable=True),
        sa.Column("project_code", sa.String(50), nullable=True),
        sa.Column("status", sa.String(50), nullable=True),
        sa.Column("mastery", sa.String(50), nullable=True),
        sa.Column("importance", sa.String(20), nullable=True),
        sa.Column("verification", sa.String(50), nullable=True),
        sa.Column("needs_review", sa.Boolean(), server_default=sa.text("false")),
        sa.Column("content_hash", sa.String(64), nullable=False),
        sa.Column("frontmatter", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb")),
        sa.Column("markdown_body", sa.Text(), nullable=True),
        sa.Column("modified_at_local", sa.DateTime(timezone=True), nullable=True),
        sa.Column("indexed_at", sa.DateTime(timezone=True), nullable=True),
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
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.create_table(
        "document_versions",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "document_id",
            sa.String(36),
            sa.ForeignKey("vault_documents.id", ondelete="CASCADE"),
            nullable=False,
            index=True,
        ),
        sa.Column("content_hash", sa.String(64), nullable=False),
        sa.Column("frontmatter", postgresql.JSONB(), server_default=sa.text("'{}'::jsonb")),
        sa.Column("markdown_body", sa.Text(), nullable=True),
        sa.Column("source_device_id", sa.String(36), nullable=True),
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


def downgrade() -> None:
    op.drop_table("document_versions")
    op.drop_table("vault_documents")
