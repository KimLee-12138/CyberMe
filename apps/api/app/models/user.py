"""User model."""

import uuid as _uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(_uuid.uuid4())
    )
    username: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False, index=True
    )
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    totp_secret_encrypted: Mapped[bytes | None] = mapped_column(
        nullable=True
    )
    timezone: Mapped[str] = mapped_column(
        String(50), default="Asia/Shanghai"
    )
    locale: Mapped[str] = mapped_column(
        String(10), default="zh-CN"
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username}>"
