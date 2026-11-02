# -*- coding: utf-8 -*-
"""Resolve the small set of preserved conflicts in enriched notes.

This is intentionally conservative: if the model cannot resolve a conflict from
the cited source, it stays visible instead of being silently deleted.
"""
from __future__ import annotations

import asyncio
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import httpx
import yaml

REPO = Path(__file__).resolve().parents[1]
ROOT = REPO / "data" / "notes_enriched"
SECTIONS = REPO / "data" / "sections" / "sections.jsonl"
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"

SYSTEM = """你是课程资料的事实核对员。给你一条旧笔记中保留的冲突 (CONFLICT) 和它引用的原文 (SOURCE)。
请判断：
- resolved：原文足够判断哪一个是笔误/哪个是权威表述；
- non_conflict：两句话其实不矛盾，是笔记误报；
- unresolved：原文本身矛盾或信息不足，不能裁决。
只输出 JSON：
{"status":"resolved|non_conflict|unresolved","resolution":"处理结论（1-3 句）","confidence":0.0}
不要编造原文没有的事实。"""


def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def clean(text: str) -> str:
    text = re.sub(r"<!-- page: \d+ -->", "", text)
    text = re.sub(r"[（(]\s*来源\s*[:：][^）)]{0,200}[）)]", "", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


async def main() -> None:
    key = (os.environ.get("DEEPSEEK_API_KEY", "") or "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set")
    by_source: dict[str, list[dict]] = {}
    for line in SECTIONS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            p = json.loads(line)
            by_source.setdefault(p.get("source_id", ""), []).append(p)

    results = []
    async with httpx.AsyncClient(timeout=120) as client:
        for path in sorted(ROOT.glob("*/*.md")):
            text = path.read_text(encoding="utf-8")
            m = re.match(r"^---\n(.*?)\n---\n\n?", text, re.S)
            if not m:
                continue
            fm = yaml.safe_load(m.group(1)) or {}
            body = text[m.end():]
            cm = re.search(r"^##\s+冲突（保留）\s*$\n(.*?)(?=^##\s+|\Z)", body, re.M | re.S)
            if not cm:
                continue
            conflict = clean(cm.group(1))
            sources = fm.get("source") or []
            src = []
            for s in sources:
                for part in by_source.get(s.get("source_id", ""), []):
                    src.append(clean(part.get("text", ""))[:3000])
            source_text = "\n\n".join(src)[:6000]
            user = f"冲突：\n{conflict}\n\n原文：\n<<<\n{source_text}\n>>>"
            try:
                resp = await client.post(
                    API_URL,
                    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                    json={
                        "model": MODEL,
                        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                        "temperature": 0,
                        "max_tokens": 700,
                        "thinking": {"type": "disabled"},
                        "response_format": {"type": "json_object"},
                        "stream": False,
                    },
                )
                if resp.status_code != 200:
                    raise RuntimeError(resp.text[:200])
                obj = parse_json(resp.json()["choices"][0]["message"]["content"])
            except Exception as e:
                obj = {"status": "unresolved", "resolution": f"自动核对失败：{e}", "confidence": 0}

            status = obj.get("status") if obj.get("status") in {"resolved", "non_conflict", "unresolved"} else "unresolved"
            resolution = clean(str(obj.get("resolution") or ""))[:1000]
            if status == "non_conflict":
                body = re.sub(r"^##\s+冲突（保留）\s*$\n(.*?)(?=^##\s+|\Z)", "", body, flags=re.M | re.S)
            elif status == "resolved":
                body = re.sub(
                    r"^##\s+冲突（保留）\s*$\n(.*?)(?=^##\s+|\Z)",
                    f"## 冲突（已处理）\n\n{resolution}\n\n> 原文保留：{conflict}\n\n",
                    body, count=1, flags=re.M | re.S,
                )
            else:
                body = re.sub(
                    r"^##\s+冲突（保留）\s*$\n(.*?)(?=^##\s+|\Z)",
                    f"## 冲突（保留）\n\n{conflict}\n\n> 核对结论：{resolution or '原文不足，保留待人工核对。'}\n\n",
                    body, count=1, flags=re.M | re.S,
                )
            enr = dict(fm.get("enrichment") or {})
            enr["conflict_status"] = status
            enr["conflict_resolution"] = resolution
            fm["enrichment"] = enr
            fm["status"] = "enriched"
            fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
            path.write_text(f"---\n{fm_text}\n---\n\n{body.lstrip()}", encoding="utf-8")
            results.append({"note_id": fm.get("id"), "status": status, "resolution": resolution})
            print(fm.get("id"), status, resolution[:100], flush=True)

    (ROOT / "_conflict_resolution.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "items": results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Conflict resolution", ""]
    for r in results:
        lines += [f"## {r['note_id']} — {r['status']}", "", r["resolution"], ""]
    (ROOT / "_conflict_resolution.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"count": len(results), "status": [r["status"] for r in results]}, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
