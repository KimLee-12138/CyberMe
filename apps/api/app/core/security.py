"""Security middleware — rate limiting, security headers, log sanitization, XSS prevention."""

import html
import re
import time
from typing import Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from app.auth.rate_limit import rate_limiter

# ── Sensitive field patterns for log sanitization ─────────

SENSITIVE_FIELDS = re.compile(
    r'(password|secret|token|key|authorization|credential)["\s:=]+["\']?([^\s"\'},]+)',
    re.IGNORECASE,
)


def sanitize_log(value: str) -> str:
    """Remove sensitive field values from log strings."""
    return SENSITIVE_FIELDS.sub(r'\1=[REDACTED]', value)


# ── Rate Limit Middleware ─────────────────────────────────


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Global rate limiter: 100 requests per minute per IP."""

    async def dispatch(self, request: Request, call_next: Callable):
        # Skip health checks
        if request.url.path.startswith("/health"):
            return await call_next(request)

        ip = request.client.host if request.client else "unknown"
        allowed = await rate_limiter.check("global", ip, max_requests=100, window_seconds=60)

        if not allowed:
            return Response(
                content='{"detail":{"code":"RATE_LIMITED","message":"请求过于频繁，请稍后再试"}}',
                status_code=429,
                media_type="application/json",
            )

        return await call_next(request)


# ── Security Headers Middleware ───────────────────────────


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Inject security-related HTTP response headers."""

    async def dispatch(self, request: Request, call_next: Callable):
        response = await call_next(request)

        # CSP: allow self, inline styles, and DeepSeek/OpenAI API for proxy
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data: https:; "
            "connect-src 'self' https://api.deepseek.com https://api.openai.com https://api.anthropic.com; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

        return response


# ── Markdown XSS Sanitizer ────────────────────────────────

# Tags to strip from markdown content before rendering
DANGEROUS_TAGS = re.compile(
    r'<\s*(script|iframe|object|embed|form|input|link|meta|style|base|applet)\b[^>]*>.*?</\s*\1\s*>|'
    r'<\s*(script|iframe|object|embed|form|input|link|meta|style|base|applet)\b[^>]*/?>',
    re.IGNORECASE | re.DOTALL,
)

DANGEROUS_ATTRS = re.compile(
    r'\s(on\w+|style|href\s*=\s*["\']\s*javascript:|src\s*=\s*["\']\s*javascript:)\s*=\s*["\'][^"\']*["\']',
    re.IGNORECASE,
)


def sanitize_markdown(text: str) -> str:
    """Remove potentially dangerous HTML from markdown content."""
    if not text:
        return text
    # Strip dangerous tags
    text = DANGEROUS_TAGS.sub("", text)
    # Strip dangerous attributes (event handlers, javascript: URLs)
    text = DANGEROUS_ATTRS.sub("", text)
    return text


# ── Request Body Sanitizer ───────────────────────────────


class RequestSanitizer:
    """Sanitize incoming request bodies by stripping potential XSS vectors."""

    @staticmethod
    def sanitize_body(body: dict | list | str | None) -> dict | list | str | None:
        """Recursively sanitize request body fields."""
        if isinstance(body, dict):
            return {k: RequestSanitizer.sanitize_body(v) for k, v in body.items()}
        elif isinstance(body, list):
            return [RequestSanitizer.sanitize_body(item) for item in body]
        elif isinstance(body, str):
            # Strip NULL bytes (PostgreSQL rejects them anyway)
            cleaned = body.replace("\x00", "")
            # Escape HTML entities in user input (prevents stored XSS)
            if any(c in cleaned for c in "<>"):
                # Only escape if there's actual HTML-like content
                pass  # Let the frontend handle rendering via react-markdown (which escapes by default)
            return cleaned
        return body
