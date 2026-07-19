"""Chat — Q&A engine: orchestrate intent → retrieval → generation → citations."""

import json
import re
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.chat.intent import classify_intent, resolve_scope
from app.model_gateway.gateway import generate as gateway_generate
from app.model_gateway.schemas import ModelMessage
from app.retrieval.engine import hybrid_search


async def ask(
    db: AsyncSession,
    query: str,
    history: list[dict[str, str]] | None = None,
    scope_override: dict[str, Any] | None = None,
    mode: str = "normal",
) -> dict[str, Any]:
    """Non-streaming Q&A — full pipeline.

    Args:
        db: Database session
        query: User's question
        history: Previous messages in this conversation
        scope_override: User-selected scope filters
        mode: Answer mode — "normal", "evidence_only", "deep_research", "dual_model"

    Returns:
        Dict with answer, citations, evidence, and metadata
    """
    # 1. Classify intent
    if scope_override and "mode" not in scope_override:
        scope_override["mode"] = mode
    intent = classify_intent(query, scope_override)

    # 2. Resolve search scope
    scope = resolve_scope(intent)

    # 3. Hybrid search
    evidence = await hybrid_search(
        db,
        query=query,
        scope=scope,
        top_k=20 if mode != "deep_research" else 40,
    )

    # 4. Build messages for model
    messages = _build_messages(query, history, evidence, intent)

    # 5. Route selection
    route = _select_route(intent, mode)

    # 6. Generate response
    try:
        response = await gateway_generate(
            route=route,
            messages=messages,
            evidence=evidence,
            trace_id=None,
        )
    except Exception as e:
        # Fallback: return a graceful error with evidence
        return {
            "answer": f"抱歉，AI 服务暂时不可用。以下是检索到的相关知识：\n\n"
            + "\n\n".join(
                f"- **{item['heading'] or item['path']}**: {item['content'][:200]}..."
                for item in evidence["items"][:5]
            ),
            "citations": [],
            "evidence": evidence,
            "mode": mode,
            "answer_source": "retrieval_only",
        }

    # 7. Extract citations from response
    citations = _extract_citations(response.content, evidence)

    # 8. Check if evidence_only mode and low coverage
    answer_source = "model_with_evidence"
    if mode == "evidence_only" and evidence["coverage"] < 0.3:
        answer_source = "insufficient_evidence"

    return {
        "answer": response.content,
        "citations": citations,
        "evidence": evidence,
        "mode": mode,
        "model": response.model,
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "total_tokens": response.usage.total_tokens,
        },
        "latency_ms": response.latency_ms,
        "answer_source": answer_source,
    }


# ── SSE helpers ──────────────────────────────────────


async def ask_stream(
    db: AsyncSession,
    query: str,
    history: list[dict[str, str]] | None = None,
    scope_override: dict[str, Any] | None = None,
    mode: str = "normal",
) -> AsyncGenerator[str, None]:
    """Streaming Q&A — yields SSE event strings."""
    import asyncio

    # 1. Emit: intent
    intent = classify_intent(query, scope_override)
    yield _sse_event("intent", json.dumps(intent, ensure_ascii=False))

    # 2. Emit: searching
    yield _sse_event("status", json.dumps({"stage": "searching", "message": "正在检索知识库..."}, ensure_ascii=False))

    scope = resolve_scope(intent)
    evidence = await hybrid_search(
        db,
        query=query,
        scope=scope,
        top_k=20 if mode != "deep_research" else 40,
    )
    yield _sse_event(
        "evidence_summary",
        json.dumps({
            "total_items": len(evidence["items"]),
            "coverage": evidence["coverage"],
            "conflicts": len(evidence["conflicts"]),
        }, ensure_ascii=False),
    )

    # 3. Emit: thinking
    yield _sse_event("status", json.dumps({"stage": "thinking", "message": "正在生成回答..."}, ensure_ascii=False))

    # 4. Build messages and stream
    messages = _build_messages(query, history, evidence, intent)
    route = _select_route(intent, mode)

    try:
        response = await gateway_generate(
            route=route,
            messages=messages,
            evidence=evidence,
        )

        # Stream tokens (simulate by sending chunks)
        answer = response.content
        chunk_size = 10
        for i in range(0, len(answer), chunk_size):
            chunk = answer[i : i + chunk_size]
            yield _sse_event("token", json.dumps({"text": chunk}, ensure_ascii=False))
            await asyncio.sleep(0.01)  # Small delay for visual streaming

        # 5. Emit citations
        citations = _extract_citations(answer, evidence)
        yield _sse_event(
            "citations",
            json.dumps(citations, ensure_ascii=False),
        )

    except Exception as e:
        yield _sse_event(
            "error",
            json.dumps({"message": f"生成回答失败: {str(e)}"}, ensure_ascii=False),
        )
        # Return evidence as fallback
        for item in evidence["items"][:5]:
            yield _sse_event(
                "evidence_fallback",
                json.dumps(item, ensure_ascii=False),
            )

    # 6. Done
    yield _sse_event("done", json.dumps({"complete": True}))


def _sse_event(event_type: str, data: str) -> str:
    """Format an SSE event."""
    return f"event: {event_type}\ndata: {data}\n\n"


# ── Helpers ──────────────────────────────────────────


def _build_messages(
    query: str,
    history: list[dict[str, str]] | None,
    evidence: dict[str, Any],
    intent: dict[str, Any],
) -> list[ModelMessage]:
    """Build the message list for the model."""
    messages: list[ModelMessage] = []

    # Context from history (last 5 exchanges)
    if history:
        for msg in history[-10:]:
            messages.append(ModelMessage(role=msg["role"], content=msg["content"]))

    # Current query with intent context
    prefix = ""
    if intent["answer_mode"] == "evidence_only":
        prefix = "【模式：只查资料】请仅使用提供的证据回答，如果证据不足请明确说明。\n\n"
    elif intent["answer_mode"] == "deep_research":
        prefix = "【模式：深度研究】请综合分析所有证据，给出尽可能全面深入的回答。\n\n"

    messages.append(ModelMessage(role="user", content=prefix + query))

    return messages


def _select_route(intent: dict[str, Any], mode: str) -> str:
    """Select the appropriate model route."""
    if mode == "evidence_only":
        return "evidence_qa.fast"
    elif mode == "deep_research":
        return "evidence_qa.deep"
    elif intent["risk"] == "high":
        return "evidence_qa.deep"
    return "evidence_qa.default"


def _extract_citations(
    answer: str, evidence: dict[str, Any]
) -> list[dict[str, Any]]:
    """Extract citation references from model response and link to evidence."""
    citations = []

    # Look for [证据 N] patterns
    evidence_refs = re.findall(r'\[证据\s*(\d+)\]', answer)

    # Map evidence items by index
    ev_map = {}
    for i, item in enumerate(evidence.get("items", []), 1):
        ev_map[str(i)] = item

    seen = set()
    for ref in evidence_refs:
        if ref in ev_map and ref not in seen:
            item = ev_map[ref]
            citations.append({
                "citation_id": ref,
                "evidence_id": item.get("evidence_id", f"ev_{ref}"),
                "document_id": item.get("document_id", ""),
                "path": item.get("path", ""),
                "heading": item.get("heading", ""),
                "source": item.get("source", ""),
                "source_pages": item.get("source_pages", ""),
                "content_snippet": (item.get("content", "") or "")[:300],
                "verification": item.get("verification", "inferred"),
                "score": item.get("score", 0),
            })
            seen.add(ref)

    return citations
