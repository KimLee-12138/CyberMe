"""Model Gateway — route configuration."""

from typing import Any

# Route definitions — all default to DeepSeek
ROUTES: dict[str, dict[str, Any]] = {
    "evidence_qa.default": {
        "description": "日常证据问答",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 4096,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.fallback",
    },
    "evidence_qa.fast": {
        "description": "轻量快速问答",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 2048,
        "timeout_seconds": 30,
        "fallback_route": None,
    },
    "evidence_qa.deep": {
        "description": "深度研究",
        "provider": "deepseek",
        "model": "deepseek-reasoner",
        "temperature": 0.2,
        "max_tokens": 8192,
        "timeout_seconds": 120,
        "fallback_route": "evidence_qa.default",
    },
    "evidence_qa.fallback": {
        "description": "降级路由（DeepSeek 重试）",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 4096,
        "timeout_seconds": 60,
        "fallback_route": None,
    },
    "tutor.socratic": {
        "description": "苏格拉底导师",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.7,
        "max_tokens": 1024,
        "timeout_seconds": 30,
        "fallback_route": "evidence_qa.default",
    },
    "tutor.concept": {
        "description": "概念讲解",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 2048,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "tutor.closed_book": {
        "description": "闭卷回忆",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 1024,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "tutor.step_by_step": {
        "description": "分步做题",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 512,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "tutor.mock_exam": {
        "description": "模拟考试",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 1024,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "tutor.mistake_retrain": {
        "description": "错题复训",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.5,
        "max_tokens": 1024,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "intent.classifier": {
        "description": "意图分类",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.0,
        "max_tokens": 512,
        "timeout_seconds": 15,
        "fallback_route": None,
    },
    "writing.personal": {
        "description": "个性化写作",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.5,
        "max_tokens": 4096,
        "timeout_seconds": 60,
        "fallback_route": "evidence_qa.default",
    },
    "reranker.light": {
        "description": "轻量重排器",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.0,
        "max_tokens": 1024,
        "timeout_seconds": 20,
        "fallback_route": None,
    },
    "distill.knowledge": {
        "description": "知识蒸馏",
        "provider": "deepseek",
        "model": "deepseek-reasoner",
        "temperature": 0.3,
        "max_tokens": 8192,
        "timeout_seconds": 180,
        "fallback_route": "distill.knowledge_fb",
    },
    "distill.knowledge_fb": {
        "description": "知识蒸馏回退",
        "provider": "deepseek",
        "model": "deepseek-chat",
        "temperature": 0.3,
        "max_tokens": 8192,
        "timeout_seconds": 120,
        "fallback_route": None,
    },
}


def get_route_config(route_name: str) -> dict[str, Any]:
    """Get configuration for a named route."""
    if route_name not in ROUTES:
        raise ValueError(
            f"Unknown route: {route_name}. Available: {list(ROUTES.keys())}"
        )
    return ROUTES[route_name]
