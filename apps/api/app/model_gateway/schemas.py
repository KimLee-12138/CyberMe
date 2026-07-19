"""Model Gateway — Pydantic schemas."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class ModelMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class ModelUsage(BaseModel):
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class ModelResponse(BaseModel):
    content: str
    model: str
    usage: ModelUsage
    finish_reason: str = "stop"
    latency_ms: float = 0
    route: str = ""


class ModelGenerateRequest(BaseModel):
    route: str = "evidence_qa.default"
    messages: list[ModelMessage]
    evidence: dict[str, Any] | None = None
    temperature: float | None = None
    max_tokens: int | None = None
    response_schema: dict[str, Any] | None = None
    trace_id: str | None = None


class ProviderConfig(BaseModel):
    name: str  # "openai" | "anthropic"
    base_url: str
    api_key: str
    default_model: str
    timeout_seconds: int = 60
