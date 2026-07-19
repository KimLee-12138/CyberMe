"""Initial schema — users, devices, sync_cursors, audit_events

Revision ID: 001
Revises: None
Create Date: 2026-07-17
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ── Users ──────────────────────────────────────────────
    op.create_table(
        "users",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("username", sa.String(150), unique=True, nullable=False, index=True),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("totp_secret_encrypted", sa.LargeBinary(), nullable=True),
        sa.Column("timezone", sa.String(50), server_default="Asia/Shanghai"),
        sa.Column("locale", sa.String(10), server_default="zh-CN"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
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

    # ── Devices ────────────────────────────────────────────
    op.create_table(
        "devices",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "user_id",
            sa.String(36),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("platform", sa.String(50), nullable=False),
        sa.Column("token_hash", sa.String(255), nullable=False),
        sa.Column(
            "permissions",
            postgresql.JSONB(),
            server_default=sa.text(
                """'{"sync": true, "read": true, "writeback": true}'::jsonb"""
            ),
        ),
        sa.Column("last_seen_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("revoked_at", sa.DateTime(timezone=True), nullable=True),
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

    # ── Sync Cursors ───────────────────────────────────────
    op.create_table(
        "sync_cursors",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column(
            "device_id",
            sa.String(36),
            sa.ForeignKey("devices.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("server_event_seq", sa.Integer(), server_default=sa.text("0")),
        sa.Column("client_event_seq", sa.Integer(), server_default=sa.text("0")),
        sa.Column("manifest_version", sa.String(64), nullable=True),
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

    # ── Audit Events ───────────────────────────────────────
    op.create_table(
        "audit_events",
        sa.Column("id", sa.String(36), primary_key=True),
        sa.Column("user_id", sa.String(36), nullable=True, index=True),
        sa.Column("device_id", sa.String(36), nullable=True),
        sa.Column("action", sa.String(100), nullable=False, index=True),
        sa.Column("resource_type", sa.String(100), nullable=True),
        sa.Column("resource_id", sa.String(36), nullable=True),
        sa.Column("result", sa.String(50), server_default="success"),
        sa.Column("ip_summary", sa.String(45), nullable=True),
        sa.Column("user_agent_summary", sa.Text(), nullable=True),
        sa.Column("detail", postgresql.JSONB(), nullable=True),
        sa.Column(
            "occurred_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
            index=True,
        ),
    )

    # Indexes are created automatically via column-level unique=True / index=True


def downgrade() -> None:
    op.drop_table("audit_events")
    op.drop_table("sync_cursors")
    op.drop_table("devices")
    op.drop_table("users")
