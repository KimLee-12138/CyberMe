"""Unit tests for authentication module."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from app.auth.password import hash_password, verify_password
from app.auth.totp import generate_totp_secret, verify_totp
from app.auth.tokens import create_session_token, decode_token


class TestPasswordHashing:
    def test_hash_and_verify(self):
        pw = "test-password-123"
        hashed = hash_password(pw)
        assert hashed != pw
        assert verify_password(pw, hashed)

    def test_wrong_password(self):
        hashed = hash_password("correct")
        assert not verify_password("wrong", hashed)

    def test_different_hashes(self):
        """Same password should produce different hashes (salting)."""
        h1 = hash_password("mypassword")
        h2 = hash_password("mypassword")
        assert h1 != h2
        assert verify_password("mypassword", h1)
        assert verify_password("mypassword", h2)


class TestTOTP:
    def test_generate_secret(self):
        secret = generate_totp_secret()
        assert len(secret) >= 16

    def test_verify_invalid_code(self):
        secret = generate_totp_secret()
        assert not verify_totp(secret, "000000")


class TestTokens:
    def test_create_and_decode_session_token(self):
        token = create_session_token("user-123", "testuser")
        payload = decode_token(token)
        assert payload is not None
        assert payload["sub"] == "user-123"
        assert payload["username"] == "testuser"
        assert payload["type"] == "session"

    def test_decode_invalid_token(self):
        payload = decode_token("not.a.valid.token")
        assert payload is None

    def test_decode_expired_token(self):
        """Token with past expiry should be invalid."""
        from app.auth.tokens import jwt, datetime, timedelta, timezone, ALGORITHM
        from app.core.config import settings

        now = datetime.now(timezone.utc)
        expired = jwt.encode(
            {"sub": "u1", "type": "session", "exp": now - timedelta(hours=1)},
            settings.secret_key,
            algorithm=ALGORITHM,
        )
        assert decode_token(expired) is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
