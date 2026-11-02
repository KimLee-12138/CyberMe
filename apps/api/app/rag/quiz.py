# -*- coding: utf-8 -*-
"""Generate a short multiple-choice quiz from an answered RAG turn."""
from __future__ import annotations

import json
import os
import re
import time

import httpx

from app.core.config import settings

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"

SYSTEM_PROMPT = """你是课程助教，负责根据一段讲解生成检验理解的选择题。
只输出严格 JSON，不要 Markdown 代码块，不要解释。

要求：
1. 生成 3 道单选题，每题 4 个选项，只有一个正确答案。
2. 题目考“理解、因果、边界、易错点”，不要考无意义的记忆碎片。
3. 不要出现“以上都对/以上都不对”。
4. explanation 说明正确答案为什么对，并指出一个常见误区。
5. 不要编造原文没有的页码或来源。

JSON 结构：
{
  "questions": [
    {
      "question": "题干",
      "options": ["A 内容", "B 内容", "C 内容", "D 内容"],
      "answer_index": 0,
      "explanation": "解析"
    }
  ]
}
"""


def _parse(content: str) -> dict:
    content = (content or "").strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    return json.loads(content)


def _normalize(obj: dict) -> list[dict]:
    questions = []
    for i, q in enumerate((obj or {}).get("questions") or [], 1):
        if not isinstance(q, dict):
            continue
        text = str(q.get("question") or "").strip()
        options = q.get("options") or []
        if not text or not isinstance(options, list) or len(options) != 4:
            continue
        options = [str(x).strip() for x in options]
        if any(not x for x in options):
            continue
        try:
            answer = int(q.get("answer_index"))
        except Exception:
            continue
        if answer < 0 or answer > 3:
            continue
        questions.append({
            "id": f"q{i}",
            "question": text[:500],
            "options": [x[:300] for x in options],
            "answer_index": answer,
            "explanation": str(q.get("explanation") or "").strip()[:800],
        })
        if len(questions) >= 3:
            break
    return questions


def generate_quiz(query: str, answer: str, count: int = 3) -> dict:
    key = (os.environ.get("DEEPSEEK_API_KEY", "") or settings.deepseek_api_key).strip()
    if not key:
        raise RuntimeError("DEEPSEEK_API_KEY not set")
    user = (
        f"问题：{query}\n\n"
        f"刚才的讲解：\n<<<\n{answer[:5000]}\n>>>\n\n"
        f"请生成 {max(1, min(count, 5))} 道单选题。"
    )
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        "temperature": 0.3,
        "max_tokens": 1600,
        "thinking": {"type": "disabled"},
        "response_format": {"type": "json_object"},
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
    questions = _normalize(_parse(data["choices"][0]["message"]["content"]))
    if not questions:
        raise RuntimeError("model returned no valid questions")
    return {
        "questions": questions,
        "model": data.get("model", MODEL),
        "usage": data.get("usage", {}),
        "latency_ms": latency,
    }
