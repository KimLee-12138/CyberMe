"""TOTP (Time-based One-Time Password) utilities."""

import pyotp


def generate_totp_secret() -> str:
    """Generate a new TOTP secret key."""
    return pyotp.random_base32()


def get_totp_uri(secret: str, username: str, issuer: str = "CyberMe") -> str:
    """Generate a provisioning URI for an authenticator app."""
    return pyotp.totp.TOTP(secret).provisioning_uri(
        name=username, issuer_name=issuer
    )


def verify_totp(secret: str, code: str) -> bool:
    """Verify a TOTP code against the secret."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code)
