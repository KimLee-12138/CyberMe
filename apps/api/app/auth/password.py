"""Password hashing with Argon2id."""

from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

_password_hash = PasswordHash([Argon2Hasher()])


def hash_password(password: str) -> str:
    """Hash a plaintext password with Argon2id."""
    return _password_hash.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """Verify a plaintext password against its hash."""
    return _password_hash.verify(password, password_hash)
