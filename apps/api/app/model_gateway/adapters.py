"""Model Gateway — provider adapters for DeepSeek, OpenAI, and Anthropic."""

import time
from typing import Any

import httpx
from app.core.config import settings

from app.model_gateway.schemas import ModelMessage, ModelResponse, ModelUsage


class ProviderError(Exception):
    def __init__(self, provider: str, status: int, detail: str):
        self.provider = provider
        self.status = status
        self.detail = detail
        super().__init__(f"[{provider}] HTTP {status}: {detail}")


class RateLimitError(ProviderError):
    pass


class ProviderTimeoutError(ProviderError):
    pass


def _build_system_prompt(evidence: dict[str, Any] | None) -> str:
    """Build a minimal system prompt with evidence injection."""
    base = (
        "你是 CyberMe 个人学习系统的 AI 助手。"
        "你的知识来源于用户个人知识库（Vault）。"
    )
    if evidence and evidence.get("items"):
        scope_str = ", ".join(evidence.get("scope", ["全部"]))
        base += f"\n\n当前检索范围：{scope_str}\n"
        base += "以下是从用户知识库中检索到的证据：\n\n"
        for i, item in enumerate(evidence["items"], 1):
            base += (
                f"[证据 {i}] ID: {item.get('evidence_id', '?')}\n"
                f"  来源: {item.get('path', '?')}"
            )
            if item.get("source_pages"):
                base += f" 页码: {item['source_pages']}"
            base += f"\n  内容: {item.get('content', '')}\n\n"
        base += (
            "请在回答中引用证据编号（如 [证据 1]）。"
            "如果证据不足以回答，请明确指出。"
            "不要编造知识库中不存在的信息。"
        )
    return base


async def _call_openai_compatible(
    provider_name: str,
    model: str,
    messages: list[ModelMessage],
    api_key: str,
    base_url: str,
    temperature: float = 0.3,
    max_tokens: int = 4096,
    timeout: int = 60,
    evidence: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> ModelResponse:
    """Call any OpenAI-compatible Chat Completion API (OpenAI, DeepSeek, etc.)."""
    start = time.monotonic()

    msgs: list[dict] = []
    sys_prompt = _build_system_prompt(evidence)
    if sys_prompt:
        msgs.append({"role": "system", "content": sys_prompt})
    for m in messages:
        msgs.append({"role": m.role, "content": m.content})

    body: dict[str, Any] = {
        "model": model,
        "messages": msgs,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    # DeepSeek doesn't support strict JSON schema; skip response_format for it
    if response_schema and provider_name != "deepseek":
        body["response_format"] = {
            "type": "json_schema",
            "json_schema": {
                "name": "response",
                "schema": response_schema,
                "strict": True,
            },
        }

    url = f"{base_url.rstrip('/')}/chat/completions"

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(timeout)) as client:
            resp = await client.post(
                url,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                json=body,
            )

        if resp.status_code == 429:
            raise RateLimitError(provider_name, 429, resp.text[:500])
        if resp.status_code >= 500:
            raise ProviderError(provider_name, resp.status_code, resp.text[:500])
        if resp.status_code != 200:
            raise ProviderError(provider_name, resp.status_code, resp.text[:500])

        data = resp.json()
        choice = data["choices"][0]
        usage_data = data.get("usage", {})

        return ModelResponse(
            content=choice["message"]["content"],
            model=data.get("model", model),
            usage=ModelUsage(
                prompt_tokens=usage_data.get("prompt_tokens", 0),
                completion_tokens=usage_data.get("completion_tokens", 0),
                total_tokens=usage_data.get("total_tokens", 0),
            ),
            finish_reason=choice.get("finish_reason", "stop"),
            latency_ms=(time.monotonic() - start) * 1000,
        )
    except (httpx.TimeoutException, httpx.ReadTimeout):
        raise ProviderTimeoutError(provider_name, 0, "Request timed out")


async def call_deepseek(
    model: str,
    messages: list[ModelMessage],
    api_key: str,
    temperature: float = 0.3,
    max_tokens: int = 4096,
    timeout: int = 60,
    evidence: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> ModelResponse:
    """Call DeepSeek Chat Completion API (OpenAI-compatible)."""
    return await _call_openai_compatible(
        provider_name="deepseek",
        model=model,
        messages=messages,
        api_key=api_key,
        base_url=settings.deepseek_base_url,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        evidence=evidence,
        response_schema=response_schema,
    )


async def call_openai(
    model: str,
    messages: list[ModelMessage],
    api_key: str,
    temperature: float = 0.3,
    max_tokens: int = 4096,
    timeout: int = 60,
    evidence: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> ModelResponse:
    """Call OpenAI Chat Completion API."""
    return await _call_openai_compatible(
        provider_name="openai",
        model=model,
        messages=messages,
        api_key=api_key,
        base_url="https://api.openai.com/v1",
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        evidence=evidence,
        response_schema=response_schema,
    )


async def call_anthropic(
    model: str,
    messages: list[ModelMessage],
    api_key: str,
    temperature: float = 0.3,
    max_tokens: int = 4096,
    timeout: int = 60,
    evidence: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> ModelResponse:
    """Call Anthropic Messages API."""
    start = time.monotonic()

    system_text = _build_system_prompt(evidence)

    msgs: list[dict] = []
    for m in messages:
        msgs.append({"role": m.role, "content": [{"type": "text", "text": m.content}]})

    body: dict[str, Any] = {
        "model": model,
        "messages": msgs,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if system_text:
        body["system"] = system_text

    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json",
    }

    if response_schema:
        schema_text = f"\n\n请以 JSON 格式回复，字段结构必须符合以下 Schema:\n```json\n{response_schema}\n```"
        if "system" in body:
            body["system"] += schema_text
        else:
            body["system"] = schema_text

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(timeout)) as client:
            resp = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers=headers,
                json=body,
            )

        if resp.status_code == 429:
            raise RateLimitError("anthropic", 429, resp.text[:500])
        if resp.status_code >= 500:
            raise ProviderError("anthropic", resp.status_code, resp.text[:500])
        if resp.status_code != 200:
            raise ProviderError("anthropic", resp.status_code, resp.text[:500])

        data = resp.json()
        content_blocks = data.get("content", [])
        text = "".join(
            block.get("text", "") for block in content_blocks if block.get("type") == "text"
        )
        usage_data = data.get("usage", {})

        return ModelResponse(
            content=text,
            model=data.get("model", model),
            usage=ModelUsage(
                prompt_tokens=usage_data.get("input_tokens", 0),
                completion_tokens=usage_data.get("output_tokens", 0),
                total_tokens=(
                    usage_data.get("input_tokens", 0)
                    + usage_data.get("output_tokens", 0)
                ),
            ),
            finish_reason=data.get("stop_reason", "stop"),
            latency_ms=(time.monotonic() - start) * 1000,
        )
    except (httpx.TimeoutException, httpx.ReadTimeout):
        raise ProviderTimeoutError("anthropic", 0, "Request timed out")


async def call_provider(
    provider: str,
    model: str,
    messages: list[ModelMessage],
    temperature: float,
    max_tokens: int,
    timeout: int,
    evidence: dict[str, Any] | None = None,
    response_schema: dict[str, Any] | None = None,
) -> ModelResponse:
    """Dispatch to the appropriate provider adapter."""
    if provider == "deepseek":
        return await call_deepseek(
            model=model,
            messages=messages,
            api_key=settings.deepseek_api_key,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            evidence=evidence,
            response_schema=response_schema,
        )
    elif provider == "openai":
        return await call_openai(
            model=model,
            messages=messages,
            api_key=settings.openai_api_key,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            evidence=evidence,
            response_schema=response_schema,
        )
    elif provider == "anthropic":
        return await call_anthropic(
            model=model,
            messages=messages,
            api_key=settings.anthropic_api_key,
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
            evidence=evidence,
            response_schema=response_schema,
        )
    else:
        raise ValueError(f"Unknown provider: {provider}")
