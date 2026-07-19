"""Authentication business logic."""

import uuid
from datetime import datetime, timedelta, timezone

from jose import jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.password import hash_password, verify_password
from app.auth.tokens import (
    ALGORITHM,
    create_device_token,
    create_refresh_token,
    create_session_token,
    decode_token,
)
from app.auth.totp import verify_totp
from app.core.config import settings
from app.models.audit import AuditEvent
from app.models.device import Device
from app.models.user import User


class AuthError(Exception):
    """Base authentication error."""

    def __init__(self, code: str, message: str, status: int = 401):
        self.code = code
        self.message = message
        self.status = status


class InvalidCredentials(AuthError):
    def __init__(self):
        super().__init__("AUTH_INVALID_CREDENTIALS", "用户名或密码错误", 401)


class TOTPRequired(AuthError):
    def __init__(self, temp_token: str):
        self.temp_token = temp_token
        super().__init__("AUTH_TOTP_REQUIRED", "需要 TOTP 二次验证", 401)


class TOTPInvalid(AuthError):
    def __init__(self):
        super().__init__("AUTH_TOTP_INVALID", "TOTP 验证码无效", 401)


class DeviceNotPaired(AuthError):
    def __init__(self):
        super().__init__("DEVICE_NOT_PAIRED", "设备未配对或已被撤销", 401)


async def login(
    db: AsyncSession,
    username: str,
    password: str,
    ip_summary: str | None = None,
    user_agent: str | None = None,
) -> dict:
    """Step 1: validate username + password. Returns temp token if TOTP needed."""
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if not user or not user.is_active:
        raise InvalidCredentials()

    if not verify_password(password, user.password_hash):
        _log_audit(db, user.id, None, "login", "failure", ip_summary, user_agent)
        raise InvalidCredentials()

    # If TOTP is configured, require second factor
    if user.totp_secret_encrypted is not None:
        now = datetime.now(timezone.utc)
        temp_token = jwt.encode(
            {
                "sub": user.id,
                "type": "totp_pending",
                "exp": now + timedelta(minutes=5),
                "iat": now,
            },
            settings.secret_key,
            algorithm=ALGORITHM,
        )
        _log_audit(db, user.id, None, "login.password_ok", "pending_totp", ip_summary, user_agent)
        raise TOTPRequired(temp_token)

    # No TOTP — issue full session
    return _issue_session(db, user, None, ip_summary, user_agent)


async def verify_totp_login(
    db: AsyncSession,
    temp_token: str,
    totp_code: str,
    ip_summary: str | None = None,
    user_agent: str | None = None,
) -> dict:
    """Step 2: verify TOTP code and issue session."""
    payload = decode_token(temp_token)
    if not payload or payload.get("type") != "totp_pending":
        raise TOTPInvalid()

    user_id = payload["sub"]
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user or not user.is_active or not user.totp_secret_encrypted:
        raise TOTPInvalid()

    if not verify_totp(user.totp_secret_encrypted.decode(), totp_code):
        _log_audit(db, user.id, None, "login.totp", "failure", ip_summary, user_agent)
        raise TOTPInvalid()

    return _issue_session(db, user, None, ip_summary, user_agent)


async def refresh_session(token: str) -> dict:
    """Refresh an expired session using a refresh token."""
    payload = decode_token(token)
    if not payload or payload.get("type") != "refresh":
        raise InvalidCredentials()

    return {
        "session_token": create_session_token(payload["sub"], ""),
        "user_id": payload["sub"],
    }


async def get_current_user(db: AsyncSession, token: str) -> User:
    """Validate a session token and return the user."""
    payload = decode_token(token)
    if not payload or payload.get("type") not in ("session", "device"):
        raise InvalidCredentials()

    result = await db.execute(select(User).where(User.id == payload["sub"]))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        raise InvalidCredentials()

    return user


async def pair_device(
    db: AsyncSession,
    user_id: str,
    device_name: str,
    platform: str,
) -> dict:
    """Register a new device and return a device token."""
    device_id = str(uuid.uuid4())
    device_token = create_device_token(device_id, user_id)

    from app.auth.password import hash_password
    token_hash = hash_password(device_token)

    device = Device(
        id=device_id,
        user_id=user_id,
        name=device_name,
        platform=platform,
        token_hash=token_hash,
    )
    db.add(device)
    await db.flush()

    return {
        "device_id": device_id,
        "device_token": device_token,
    }


async def revoke_device(db: AsyncSession, device_id: str) -> None:
    """Revoke a device token."""
    from datetime import datetime, timezone

    result = await db.execute(select(Device).where(Device.id == device_id))
    device = result.scalar_one_or_none()
    if device:
        device.revoked_at = datetime.now(timezone.utc)
        await db.flush()


def _issue_session(
    db: AsyncSession,
    user: User,
    device_id: str | None,
    ip_summary: str | None,
    user_agent: str | None,
) -> dict:
    """Issue session + refresh tokens."""
    session_token = create_session_token(user.id, user.username)
    refresh_token = create_refresh_token(user.id)
    _log_audit(db, user.id, device_id, "login", "success", ip_summary, user_agent)
    return {
        "user": {"id": user.id, "username": user.username},
        "session_token": session_token,
        "refresh_token": refresh_token,
    }


def _log_audit(
    db: AsyncSession,
    user_id: str,
    device_id: str | None,
    action: str,
    result: str,
    ip_summary: str | None,
    user_agent: str | None,
) -> None:
    """Create an audit event (fire and forget in the current tx)."""
    event = AuditEvent(
        id=str(uuid.uuid4()),
        user_id=user_id,
        device_id=device_id,
        action=action,
        result=result,
        ip_summary=ip_summary,
        user_agent_summary=(user_agent[:200] if user_agent else None),
    )
    db.add(event)
