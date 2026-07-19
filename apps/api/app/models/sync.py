"""SyncCursor model — tracks per-device sync progress."""

import uuid as _uuid

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin


class SyncCursor(Base, TimestampMixin):
    __tablename__ = "sync_cursors"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    device_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("devices.id", ondelete="CASCADE"), nullable=False
    )
    # Server-side event sequence number the device has confirmed
    server_event_seq: Mapped[int] = mapped_column(Integer, default=0)
    # Client-side event sequence number last received
    client_event_seq: Mapped[int] = mapped_column(Integer, default=0)
    # Full manifest version / hash
    manifest_version: Mapped[str | None] = mapped_column(
        String(64), nullable=True
    )

    def __repr__(self) -> str:
        return f"<SyncCursor device_id={self.device_id} server_seq={self.server_event_seq}>"
