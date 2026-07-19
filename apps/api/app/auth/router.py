"""Authentication API routes — /api/v1/auth/* and /api/v1/devices/*."""

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import SESSION_COOKIE, current_user
from app.auth.rate_limit import rate_limiter
from app.auth.service import (
    AuthError,
    InvalidCredentials,
    TOTPRequired,
    TOTPInvalid,
    login as login_service,
    verify_totp_login,
    refresh_session,
    pair_device,
    revoke_device,
)
from app.core.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/v1")

# ── Request / Response schemas ─────────────────────────


class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=150)
    password: str = Field(..., min_length=1)


class TOTPVerifyRequest(BaseModel):
    temp_token: str
    code: str = Field(..., min_length=6, max_length=6)


class RefreshRequest(BaseModel):
    refresh_token: str


class SessionResponse(BaseModel):
    user: dict | None
    authenticated: bool


class PairingCodeRequest(BaseModel):
    pass  # Future: TTL config


class DevicePairRequest(BaseModel):
    pairing_code: str
    device_name: str = Field(..., min_length=1, max_length=200)
    platform: str = Field(..., min_length=1, max_length=50)


# ── Auth Endpoints ─────────────────────────────────────


def _get_client_info(request: Request) -> tuple[str | None, str | None]:
    ip = request.headers.get("X-Forwarded-For", request.client.host if request.client else None)
    ua = request.headers.get("User-Agent", "")
    return ip, ua[:200] if ua else None


@router.post("/auth/login")
async def login(
    request: Request,
    body: LoginRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    """Step 1: username + password. Returns session or requires TOTP."""
    ip, ua = _get_client_info(request)

    # Rate limit: 10 attempts per minute per IP
    identifier = ip or "unknown"
    if not await rate_limiter.check("login", identifier, 10, 60):
        raise HTTPException(
            status_code=429,
            detail={"code": "RATE_LIMITED", "message": "登录尝试过于频繁，请稍后再试"},
        )

    try:
        tokens = await login_service(db, body.username, body.password, ip, ua)
    except TOTPRequired as e:
        return {
            "status": "totp_required",
            "temp_token": e.temp_token,
        }
    except InvalidCredentials:
        raise HTTPException(
            status_code=401,
            detail={"code": "AUTH_INVALID_CREDENTIALS", "message": "用户名或密码错误"},
        )

    # Set session cookie
    response.set_cookie(
        key=SESSION_COOKIE,
        value=tokens["session_token"],
        httponly=True,
        secure=False,  # Set True in production with HTTPS
        samesite="lax",
        max_age=86400,  # 24 hours
    )

    return {
        "status": "authenticated",
        "user": tokens["user"],
        "refresh_token": tokens["refresh_token"],
    }


@router.post("/auth/totp/verify")
async def verify_totp(
    request: Request,
    body: TOTPVerifyRequest,
    response: Response,
    db: AsyncSession = Depends(get_db),
):
    """Step 2: verify TOTP code and issue session."""
    ip, ua = _get_client_info(request)

    try:
        tokens = await verify_totp_login(db, body.temp_token, body.code, ip, ua)
    except TOTPInvalid:
        raise HTTPException(
            status_code=401,
            detail={"code": "AUTH_TOTP_INVALID", "message": "TOTP 验证码无效或已过期"},
        )

    response.set_cookie(
        key=SESSION_COOKIE,
        value=tokens["session_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,
    )

    return {
        "status": "authenticated",
        "user": tokens["user"],
        "refresh_token": tokens["refresh_token"],
    }


@router.post("/auth/logout")
async def logout(response: Response):
    """Clear the session cookie."""
    response.delete_cookie(SESSION_COOKIE)
    return {"status": "logged_out"}


@router.get("/auth/session")
async def get_session(user: User = Depends(current_user)):
    """Return the current session user."""
    return SessionResponse(
        user={"id": user.id, "username": user.username},
        authenticated=True,
    )


@router.post("/auth/refresh")
async def refresh(body: RefreshRequest, response: Response):
    """Refresh an expiring session."""
    try:
        tokens = await refresh_session(body.refresh_token)
    except InvalidCredentials:
        raise HTTPException(
            status_code=401,
            detail={"code": "AUTH_INVALID_REFRESH", "message": "refresh_token 无效或已过期"},
        )

    response.set_cookie(
        key=SESSION_COOKIE,
        value=tokens["session_token"],
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=86400,
    )

    return {"status": "refreshed"}


# ── Device Endpoints ───────────────────────────────────


@router.get("/devices")
async def list_devices(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """List paired devices for the current user."""
    from sqlalchemy import select
    from app.models.device import Device

    result = await db.execute(
        select(Device).where(Device.user_id == user.id, Device.revoked_at.is_(None))
    )
    devices = result.scalars().all()
    return {
        "devices": [
            {
                "id": d.id,
                "name": d.name,
                "platform": d.platform,
                "last_seen_at": d.last_seen_at.isoformat() if d.last_seen_at else None,
            }
            for d in devices
        ]
    }


@router.post("/devices/pairing-codes")
async def create_pairing_code(
    user: User = Depends(current_user),
):
    """Generate a one-time pairing code (6 digits, 10 min TTL)."""
    import secrets
    import redis.asyncio as aioredis

    from app.core.config import settings as cfg

    code = str(secrets.randbelow(900000) + 100000)  # 6 digits
    r = aioredis.from_url(cfg.redis_url, decode_responses=True)
    key = f"pairing:{user.id}:{code}"
    await r.set(key, user.id, ex=600)  # 10 minutes
    await r.close()

    return {"pairing_code": code, "expires_in": 600}


@router.post("/devices/pair")
async def pair_device_endpoint(
    body: DevicePairRequest,
    db: AsyncSession = Depends(get_db),
):
    """Register a device using a pairing code."""
    import redis.asyncio as aioredis

    from app.core.config import settings as cfg

    r = aioredis.from_url(cfg.redis_url, decode_responses=True)

    # Scan all pairing keys to find the matching code
    user_id = None
    cursor = 0
    while True:
        cursor, keys = await r.scan(cursor, match="pairing:*")
        for k in keys:
            key_str = k.decode() if isinstance(k, bytes) else k
            if key_str.endswith(f":{body.pairing_code}"):
                user_id = await r.get(k)
                await r.delete(k)
                break
        if user_id or cursor == 0:
            break

    await r.close()

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail={"code": "DEVICE_INVALID_PAIRING_CODE", "message": "配对码无效或已过期"},
        )

    tokens = await pair_device(db, user_id, body.device_name, body.platform)
    return {
        "device_id": tokens["device_id"],
        "device_token": tokens["device_token"],
    }


@router.delete("/devices/{device_id}")
async def delete_device(
    device_id: str,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Revoke a paired device."""
    await revoke_device(db, device_id)
    return {"status": "revoked"}
