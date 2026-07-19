"""JWT token creation and verification for sessions and devices."""

from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from app.core.config import settings

ALGORITHM = "HS256"
SESSION_EXPIRE_HOURS = 24
SESSION_REFRESH_DAYS = 7
DEVICE_TOKEN_EXPIRE_DAYS = 365


def create_session_token(user_id: str, username: str) -> str:
    """Create a short-lived user session token (browser cookie)."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "username": username,
        "type": "session",
        "iat": now,
        "exp": now + timedelta(hours=SESSION_EXPIRE_HOURS),
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def create_refresh_token(user_id: str) -> str:
    """Create a longer-lived refresh token."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "type": "refresh",
        "iat": now,
        "exp": now + timedelta(days=SESSION_REFRESH_DAYS),
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def create_device_token(device_id: str, user_id: str) -> str:
    """Create a long-lived device token for the sync agent."""
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "device_id": device_id,
        "type": "device",
        "iat": now,
        "exp": now + timedelta(days=DEVICE_TOKEN_EXPIRE_DAYS),
    }
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_token(token: str) -> dict | None:
    """Decode and validate a JWT token. Returns None if invalid or expired."""
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
