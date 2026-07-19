"""Model Gateway — budget tracking and cost control."""

import asyncio
from datetime import datetime, timezone
from typing import Any

from app.core.config import settings

# In-memory budget tracking (reset on restart; persist to DB later)
_budget_state: dict[str, Any] = {
    "daily_tokens": 0,
    "monthly_tokens": 0,
    "daily_cost_estimate": 0.0,
    "monthly_cost_estimate": 0.0,
    "last_reset_day": datetime.now(timezone.utc).day,
    "last_reset_month": datetime.now(timezone.utc).month,
    "lock": asyncio.Lock(),
}

# Approximate cost per 1K tokens (USD)
COST_PER_1K = {
    # DeepSeek
    "deepseek-chat": {"input": 0.00027, "output": 0.00110},
    "deepseek-reasoner": {"input": 0.00055, "output": 0.00219},
    # Anthropic
    "claude-haiku-4-5": {"input": 0.001, "output": 0.005},
    "claude-sonnet-4-6": {"input": 0.003, "output": 0.015},
    "claude-opus-4-6": {"input": 0.015, "output": 0.075},
    # OpenAI
    "gpt-4o": {"input": 0.0025, "output": 0.010},
    "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},
}


def _estimate_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    """Estimate USD cost for a model call."""
    rates = COST_PER_1K.get(model, {"input": 0.001, "output": 0.005})
    return (prompt_tokens / 1000) * rates["input"] + (completion_tokens / 1000) * rates["output"]


async def _reset_if_needed():
    """Reset daily/monthly counters on boundary."""
    now = datetime.now(timezone.utc)
    if now.day != _budget_state["last_reset_day"]:
        _budget_state["daily_tokens"] = 0
        _budget_state["daily_cost_estimate"] = 0.0
        _budget_state["last_reset_day"] = now.day
    if now.month != _budget_state["last_reset_month"]:
        _budget_state["monthly_tokens"] = 0
        _budget_state["monthly_cost_estimate"] = 0.0
        _budget_state["last_reset_month"] = now.month


async def check_budget(model: str, prompt_tokens: int, max_completion_tokens: int) -> bool:
    """Check if the call fits within budget. Raises exception if not."""
    async with _budget_state["lock"]:
        await _reset_if_needed()

        est_cost = _estimate_cost(model, prompt_tokens, max_completion_tokens)
        current_monthly = _budget_state["monthly_cost_estimate"]
        limit = settings.monthly_budget_limit

        if current_monthly + est_cost > limit:
            raise BudgetExceededError(
                f"月预算 ${limit:.2f} 已接近上限 "
                f"(已用 ${current_monthly:.2f}，本次预估 ${est_cost:.2f})"
            )

        # Soft daily cap: $5
        daily_limit = 5.0
        current_daily = _budget_state["daily_cost_estimate"]
        if current_daily + est_cost > daily_limit:
            raise BudgetExceededError(
                f"日预算 ${daily_limit:.2f} 已用尽 "
                f"(已用 ${current_daily:.2f}，本次预估 ${est_cost:.2f})"
            )

        return True


class BudgetExceededError(Exception):
    pass


async def record_usage(model: str, prompt_tokens: int, completion_tokens: int) -> None:
    """Record token usage for cost tracking."""
    async with _budget_state["lock"]:
        await _reset_if_needed()
        cost = _estimate_cost(model, prompt_tokens, completion_tokens)
        _budget_state["daily_tokens"] += prompt_tokens + completion_tokens
        _budget_state["monthly_tokens"] += prompt_tokens + completion_tokens
        _budget_state["daily_cost_estimate"] += cost
        _budget_state["monthly_cost_estimate"] += cost


def get_budget_status() -> dict[str, Any]:
    """Return current budget usage (non-async for health checks)."""
    return {
        "daily_cost_estimate": round(_budget_state["daily_cost_estimate"], 4),
        "monthly_cost_estimate": round(_budget_state["monthly_cost_estimate"], 4),
        "monthly_budget_limit": settings.monthly_budget_limit,
        "daily_tokens": _budget_state["daily_tokens"],
        "monthly_tokens": _budget_state["monthly_tokens"],
    }
