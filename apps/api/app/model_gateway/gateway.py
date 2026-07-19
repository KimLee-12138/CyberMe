"""Model Gateway — main orchestration: route → provider → call → result."""

import asyncio
import time
import uuid
from typing import Any

from app.model_gateway.adapters import (
    ProviderError,
    ProviderTimeoutError,
    RateLimitError,
    call_provider,
)
from app.model_gateway.budget import BudgetExceededError, check_budget, record_usage
from app.model_gateway.routes import get_route_config
from app.model_gateway.schemas import ModelMessage, ModelResponse


class GatewayError(Exception):
    def __init__(self, message: str, code: str = "GATEWAY_ERROR"):
        self.message = message
        self.code = code
        super().__init__(message)


MAX_RETRIES = 2
RETRY_BACKOFF_SECONDS = [1, 3]


async def generate(
    route: str,
    messages: list[ModelMessage],
    evidence: dict[str, Any] | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    response_schema: dict[str, Any] | None = None,
    trace_id: str | None = None,
) -> ModelResponse:
    """Main entry point: generate a response via the model gateway.

    Args:
        route: Named route key (e.g., "evidence_qa.default")
        messages: Conversation history
        evidence: Optional evidence bundle from retrieval
        temperature: Override route default
        max_tokens: Override route default
        response_schema: Optional JSON schema for structured output
        trace_id: Optional request tracing ID

    Returns:
        ModelResponse with content, usage, model info, and latency

    Raises:
        GatewayError: All providers failed and no fallback available
    """
    trace_id = trace_id or str(uuid.uuid4())[:8]
    route_cfg = get_route_config(route)

    temp = temperature if temperature is not None else route_cfg["temperature"]
    mt = max_tokens if max_tokens is not None else route_cfg["max_tokens"]

    # Estimate prompt tokens for budget check (rough: 1 token ≈ 4 chars)
    prompt_chars = sum(len(m.content) for m in messages)
    if evidence:
        for item in evidence.get("items", []):
            prompt_chars += len(item.get("content", ""))
    estimated_prompt_tokens = max(1, prompt_chars // 4)

    try:
        await check_budget(route_cfg["model"], estimated_prompt_tokens, mt)
    except BudgetExceededError as e:
        raise GatewayError(str(e), code="BUDGET_EXCEEDED")

    last_error = None
    current_route_cfg = route_cfg
    current_route_name = route

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await call_provider(
                provider=current_route_cfg["provider"],
                model=current_route_cfg["model"],
                messages=messages,
                temperature=temp,
                max_tokens=mt,
                timeout=current_route_cfg.get("timeout_seconds", 60),
                evidence=evidence,
                response_schema=response_schema,
            )
            response.route = current_route_name

            # Record usage
            await record_usage(
                model=response.model,
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
            )
            return response

        except (ProviderTimeoutError, RateLimitError, ProviderError) as e:
            last_error = e
            if attempt < MAX_RETRIES:
                await asyncio.sleep(RETRY_BACKOFF_SECONDS[attempt])

    # All retries exhausted — try fallback route
    fallback_route = current_route_cfg.get("fallback_route")
    if fallback_route:
        try:
            return await generate(
                route=fallback_route,
                messages=messages,
                evidence=evidence,
                temperature=temp,
                max_tokens=mt,
                response_schema=response_schema,
                trace_id=trace_id,
            )
        except Exception as fb_err:
            raise GatewayError(
                f"所有 Provider 调用失败，降级路由也失败: {fb_err}",
                code="ALL_PROVIDERS_FAILED",
            )

    raise GatewayError(
        f"所有 Provider 调用失败 (重试 {MAX_RETRIES} 次): {last_error}",
        code="ALL_PROVIDERS_FAILED",
    )
