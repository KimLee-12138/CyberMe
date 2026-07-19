"""FastAPI dependencies for authentication."""

from fastapi import Cookie, Depends, HTTPException, Request
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.service import get_current_user
from app.auth.tokens import decode_token
from app.core.database import get_db
from app.models.device import Device
from app.models.user import User

SESSION_COOKIE = "cyberme_session"


async def get_session_token(
    request: Request,
    session: str | None = Cookie(default=None, alias=SESSION_COOKIE),
) -> str | None:
    """Extract session token from cookie or Authorization header."""
    if session:
        return session
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        return auth_header[7:]
    return None


async def current_user(
    db: AsyncSession = Depends(get_db),
    token: str | None = Depends(get_session_token),
) -> User:
    """Require valid session — returns current user or 401."""
    if not token:
        raise HTTPException(
            status_code=401,
            detail={"code": "AUTH_REQUIRED", "message": "请先登录"},
        )
    try:
        user = await get_current_user(db, token)
        return user
    except Exception:
        raise HTTPException(
            status_code=401,
            detail={"code": "AUTH_INVALID_SESSION", "message": "会话已过期，请重新登录"},
        )


async def current_device(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Device:
    """Require valid device token — for sync agent API access."""
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail={"code": "DEVICE_NOT_PAIRED", "message": "需要设备 Token"},
        )

    token = auth_header[7:]
    payload = decode_token(token)
    if not payload or payload.get("type") != "device":
        raise HTTPException(
            status_code=401,
            detail={"code": "DEVICE_NOT_PAIRED", "message": "设备 Token 无效"},
        )

    device_id = payload.get("device_id")
    result = await db.execute(
        select(Device).where(
            Device.id == device_id,
            Device.revoked_at.is_(None),
        )
    )
    device = result.scalar_one_or_none()
    if not device:
        raise HTTPException(
            status_code=401,
            detail={"code": "DEVICE_NOT_PAIRED", "message": "设备未配对或已被撤销"},
        )

    return device


async def optional_user(
    db: AsyncSession = Depends(get_db),
    token: str | None = Depends(get_session_token),
) -> User | None:
    """Get current user if authenticated, None otherwise."""
    if not token:
        return None
    try:
        return await get_current_user(db, token)
    except Exception:
        return None
