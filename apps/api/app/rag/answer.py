# -*- coding: utf-8 -*-
"""Stage 2 — answer generation with citations and refusal."""
from __future__ import annotations

import json
import os
import re
import time
from typing import Any

import httpx

from app.core.config import settings
from app.rag.retriever import RagIndex, tokenize, STOP

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"

REFUSAL = (
    "我在当前知识库中没有找到足够依据。已检索到的相关内容是：{hint}。"
    "我不会用模型常识补写成你的知识库事实。"
)

SYSTEM_PROMPT = """你是 CyberMe 的课程知识库讲解助手。你的目标不是给一句结论，而是让用户真正理解。

回答规则：
1. 先给一句话结论，再讲“为什么/核心机制”，再讲步骤或公式，最后给易错点和关联概念。
2. 允许讲得详细、稍微复杂：把因果链、成立条件、变量含义、边界情况讲清楚；不要只堆术语。
3. 每个事实性句子可以在句末标注来源编号，例如 [1]、[2]；编号必须在证据范围内，不得虚构。
4. 不要在正文中写 SRC 编号、文件名、页码、证据编号或“来源：...”；来源由系统在回答下方展示。
5. 原文公式/变量缺失时，明确说“原文公式缺失”，不要补写；证据不足的部分不要伪装成原文。
6. 用中文回答，先给一句话结论，再分节解释；不要输出 JSON。
7. 结尾用一句自然的话问用户：“要不要我出 3 道题，检验一下刚才讲的内容？”不要输出其他内部字段。
"""

FALLBACK_SYSTEM_PROMPT = """你是 CyberMe 的学习讲解助手。当前用户的私人知识库没有检索到足够资料，必须降级使用你自身的模型知识回答。

降级规则：
1. 回答开头必须明确写：“【降级回答】本地知识库没有检索到足够资料，以下使用 DeepSeek 模型知识回答，不代表你的课程资料。”
2. 讲透彻：定义 → 为什么/机制 → 步骤或公式（逐项解释变量和条件）→ 一个具体例子 → 易错点/边界 → 与相邻概念的区别。
3. 不要编造“你的资料里写了……”，不要伪造引用、页码或 SRC。
4. 如果问题本身无法确定，先说明假设，再给出条件性回答。
5. 结尾自然地问：“要不要我出 3 道题，检验一下刚才讲的内容？”
6. 用中文，结构化 Markdown，但不要输出 JSON 或内部字段。
"""


def build_evidence(results: list[dict]) -> list[dict]:
    ev = []
    for i, r in enumerate(results, 1):
        ev.append({
            "evidence_id": f"E{i}",
            "doc_id": r["doc_id"],
            "kind": r["kind"],
            "course": r["course"],
            "title": r["title"],
            "heading": r["heading"],
            "pages": r["pages"],
            "source_ids": r["source_ids"],
            "score": r["score"],
            "snippet": r["snippet"],
        })
    return ev


def evidence_prompt(ev: list[dict]) -> str:
    lines = []
    for e in ev:
        pages = ""
        if e["pages"]:
            pages = ", ".join(f"p.{a}-{b}" if a != b else f"p.{a}" for a, b in e["pages"])
        loc = " ".join(x for x in ["; ".join(e["source_ids"]), pages] if x)
        lines.append(
            f"[{e['evidence_id']}] ({e['kind']}, {e['course']}, {loc})\n"
            f"标题: {e['title']} § {e['heading']}\n"
            f"内容: {e['snippet']}\n"
        )
    return "\n".join(lines)


def query_coverage(query: str, results: list[dict]) -> float:
    q = set(tokenize(query))
    if not q:
        return 0.0
    text = " ".join(f"{r['title']} {r['heading']} {r['snippet']}" for r in results[:5])
    e = set(tokenize(text))
    return len(q & e) / len(q)


QUESTION_STOP = {
    "什么", "怎么", "为什么", "如何", "哪些", "哪个", "区别", "原理", "应用", "作用",
    "介绍", "一下", "是否", "可以", "需要", "关系", "方法", "步骤", "过程", "场景",
    "具体", "相关", "进行", "实现", "理解", "解释", "说说", "讲讲", "请", "我",
}


def unsupported_query_terms(query: str, results: list[dict],
                            vocabulary: set[str] | None = None) -> list[str]:
    """Terms that occur in the question but nowhere in the retrieved context.

    This prevents a fluent generic answer from being presented as grounded when
    the actual subject (e.g. 量子纠缠) is absent from the corpus.
    """
    q = {
        t for t in tokenize(query)
        if len(t) >= 2 and t not in STOP and t not in QUESTION_STOP
    }
    text = " ".join(
        f"{r.get('title', '')} {r.get('heading', '')} {r.get('snippet', '')}"
        for r in results[:8]
    )
    seen = set(tokenize(text))
    if vocabulary:
        seen |= vocabulary
    return sorted(t for t in q if t not in seen)


CITE_RE = re.compile(r"\[(?:E)?(\d+)\]")
SOURCE_RE = re.compile(r"[（(]\s*来源\s*[:：][^）)]{0,160}[）)]")


def extract_citations(answer: str, ev: list[dict]) -> list[dict]:
    ids = CITE_RE.findall(answer or "")
    out = []
    seen = set()
    for x in ids:
        eid = f"E{x}"
        if eid in seen:
            continue
        seen.add(eid)
        for e in ev:
            if e["evidence_id"] == eid:
                item = dict(e)
                item["citation_id"] = f"E{x}"
                out.append(item)
                break
    return out


def clean_answer(answer: str) -> str:
    """Remove internal citation markers and note-level source strings.

    The API still returns structured citations; the prose should be readable
    without [E1]/[1] or (来源：SRC-...) appearing in the middle of a sentence.
    """
    text = CITE_RE.sub("", answer or "")
    text = SOURCE_RE.sub("", text)
    text = re.sub(r"[ \t]+([，。；：、！？])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def is_refusal(answer: str) -> bool:
    keys = ["没有找到足够依据", "没有足够依据", "无法回答", "证据不足", "未找到", "不能回答"]
    return any(k in (answer or "") for k in keys)


def call_model(query: str, ev: list[dict], system_prompt: str = SYSTEM_PROMPT,
               fallback: bool = False) -> dict:
    key = (os.environ.get("DEEPSEEK_API_KEY", "") or settings.deepseek_api_key).strip()
    if not key:
        raise RuntimeError("DEEPSEEK_API_KEY not set")
    if fallback:
        user = f"问题：{query}\n\n本地知识库没有检索到足够资料；请按降级规则回答。"
    else:
        user = f"问题：{query}\n\n证据：\n{evidence_prompt(ev)}\n请基于以上证据回答。引用时只用 [1] 这样的编号；不要在正文中写来源编号、文件名、页码或内部字段。"
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user},
        ],
        "temperature": 0.2 if fallback else 0,
        "max_tokens": 1800,
        "thinking": {"type": "disabled"},
        "stream": False,
    }
    t0 = time.time()
    resp = httpx.post(
        API_URL,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json=payload,
        timeout=120,
    )
    latency = int((time.time() - t0) * 1000)
    if resp.status_code != 200:
        raise RuntimeError(f"DeepSeek HTTP {resp.status_code}: {resp.text[:300]}")
    data = resp.json()
    return {
        "content": data["choices"][0]["message"]["content"],
        "usage": data.get("usage", {}),
        "latency_ms": latency,
        "model": data.get("model", MODEL),
    }


def _fallback(query: str, course: str | None, reason: str,
              ev: list[dict], coverage: float | None = None) -> dict:
    """Use model knowledge only when local evidence is insufficient.

    The result is explicitly marked so the UI can show a downgrade banner and
    so callers never mistake it for a grounded answer.
    """
    try:
        resp = call_model(query, [], FALLBACK_SYSTEM_PROMPT, fallback=True)
        content = clean_answer(resp["content"]).strip()
        if content and not content.startswith("【降级回答】"):
            content = "【降级回答】本地知识库没有检索到足够资料，以下使用 DeepSeek 模型知识回答，不代表你的课程资料。\n\n" + content
        return {
            "query": query,
            "course": course,
            "answer": content,
            "citations": [],
            "evidence": ev,
            "refused": False,
            "degraded": True,
            "degraded_reason": reason,
            "coverage": round(coverage, 3) if coverage is not None else None,
            "model": resp["model"],
            "usage": resp["usage"],
            "latency_ms": resp["latency_ms"],
        }
    except Exception as exc:
        return {
            "query": query,
            "course": course,
            "answer": (
                "【降级失败】本地知识库没有检索到足够资料，"
                f"DeepSeek 降级回答也不可用：{type(exc).__name__}。"
            ),
            "citations": [],
            "evidence": ev,
            "refused": True,
            "degraded": True,
            "degraded_reason": "fallback_unavailable",
            "coverage": round(coverage, 3) if coverage is not None else None,
            "model": None,
            "usage": {},
            "latency_ms": 0,
        }


def ask(index: RagIndex, query: str, course: str | None = None, top_k: int = 8) -> dict[str, Any]:
    results = index.search(query, top_k=top_k, course=course)
    ev = build_evidence(results)

    if not results:
        return _fallback(query, course, "no_results", [])

    coverage = query_coverage(query, results)
    missing_terms = unsupported_query_terms(query, results)
    if coverage < 0.55 or (missing_terms and coverage < 0.9):
        reason = f"low_query_coverage:{coverage:.2f}"
        if missing_terms:
            reason = f"unsupported_terms:{','.join(missing_terms[:4])}"
        return _fallback(query, course, reason, ev, coverage)

    resp = call_model(query, ev)
    raw_answer = (resp["content"] or "").strip()
    citations = extract_citations(raw_answer, ev)
    answer = clean_answer(raw_answer)
    # A refusal is detected from the opening; a later caveat like
    # "某一部分资料没有找到" must not turn a cited answer into a refusal.
    head = answer[:120]
    refused = is_refusal(head) or (is_refusal(answer) and not citations)
    if refused:
        # If the evidence was weak enough that the model refused, downgrade
        # explicitly instead of showing a dead end.
        return _fallback(query, course, "model_refusal", ev, coverage)
    if not citations:
        # An answer with no traceable local source is not a grounded answer.
        return _fallback(query, course, "no_local_citations", ev, coverage)

    return {
        "query": query,
        "course": course,
        "answer": answer,
        "citations": citations,
        "evidence": ev,
        "refused": False,
        "degraded": False,
        "degraded_reason": "",
        "coverage": round(coverage, 3),
        "model": resp["model"],
        "usage": resp["usage"],
        "latency_ms": resp["latency_ms"],
    }
