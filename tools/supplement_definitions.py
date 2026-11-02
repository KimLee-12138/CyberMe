# -*- coding: utf-8 -*-
"""Fill missing definitions in enriched notes, clearly marking AI additions."""
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

SYSTEM = """你是课程笔记编辑。给你旧笔记 (NOTE)、原文 (SOURCE) 和一个缺失的“定义”字段。
只输出严格 JSON：
{"definition": "定义", "from_source": true, "confidence": 0.0}
要求：
1. 能从 SOURCE 找到定义时，from_source=true，尽量保留原文措辞；
2. 找不到时，才用模型知识写一个准确、简洁的定义，from_source=false；
3. 不要写来源编号、页码、Markdown 标题；不超过 200 字。"""


def parse_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def clean(text: str) -> str:
    text = re.sub(r"<!-- page: \d+ -->", "", text or "")
    text = re.sub(r"[（(]\s*来源\s*[:：][^）)]{0,200}[）)]", "", text)
    text = re.sub(r"\bSRC-[A-Z]+-\d+(?:-SEC\d+)?\b", "", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def split(text: str):
    m = re.match(r"^---\n(.*?)\n---\n\n?", text, re.S)
    if not m:
        return {}, text
    return yaml.safe_load(m.group(1)) or {}, text[m.end():]


def has_section(body: str, name: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(name)}", body, re.M))


def insert_definition(body: str, definition: str, from_source: bool) -> str:
    suffix = "" if from_source else "（AI 补充，非原文）"
    block = f"## 定义\n{definition}{suffix}\n\n"
    if has_section(body, "定义"):
        return re.sub(r"^##\s+定义.*?$\n(.*?)(?=^##\s+|\Z)", block, body, count=1, flags=re.M | re.S)
    anchor = "## 关键点"
    if anchor in body:
        return body.replace(anchor, block + anchor, 1)
    return body.rstrip() + "\n\n" + block


async def main() -> None:
    key = (os.environ.get("DEEPSEEK_API_KEY", "") or "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set")
    by_source: dict[str, list[dict]] = {}
    for line in SECTIONS.read_text(encoding="utf-8").splitlines():
        if line.strip():
            p = json.loads(line)
            by_source.setdefault(p.get("source_id", ""), []).append(p)

    paths = []
    for p in sorted(ROOT.glob("*/*.md")):
        fm, body = split(p.read_text(encoding="utf-8"))
        if not has_section(body, "定义") and fm.get("enrichment"):
            paths.append(p)
    print("candidates", len(paths), flush=True)
    sem = asyncio.Semaphore(6)
    results = []

    async with httpx.AsyncClient(timeout=120) as client:
        async def one(path: Path):
            text = path.read_text(encoding="utf-8")
            fm, body = split(text)
            sources = fm.get("source") or []
            src = []
            for s in sources:
                for part in by_source.get(s.get("source_id", ""), []):
                    src.append(clean(part.get("text", ""))[:3000])
            source_text = "\n\n".join(src)[:5000]
            user = f"课程：{fm.get('course')}\n标题：{fm.get('title')}\n\n旧笔记：\n<<<\n{body[:2500]}\n>>>\n\n原文：\n<<<\n{source_text}\n>>>\n\n请补一个定义。"
            try:
                async with sem:
                    resp = await client.post(
                        API_URL,
                        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                        json={
                            "model": MODEL,
                            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                            "temperature": 0,
                            "max_tokens": 500,
                            "thinking": {"type": "disabled"},
                            "response_format": {"type": "json_object"},
                            "stream": False,
                        },
                    )
                if resp.status_code != 200:
                    raise RuntimeError(resp.text[:200])
                obj = parse_json(resp.json()["choices"][0]["message"]["content"])
                definition = clean(str(obj.get("definition") or ""))[:600]
                if not definition:
                    results.append({"note_id": fm.get("id"), "status": "empty"})
                    return
                from_source = bool(obj.get("from_source", False))
                body2 = insert_definition(body, definition, from_source)
                enr = dict(fm.get("enrichment") or {})
                enr["flags"] = [x for x in (enr.get("flags") or []) if x != "definition_missing"]
                enr["definition_from_source"] = from_source
                fm["enrichment"] = enr
                fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
                path.write_text(f"---\n{fm_text}\n---\n\n{body2.lstrip()}", encoding="utf-8")
                results.append({"note_id": fm.get("id"), "status": "filled", "from_source": from_source})
                print(fm.get("id"), "filled", from_source, flush=True)
            except Exception as e:
                results.append({"note_id": fm.get("id"), "status": "error", "error": str(e)[:200]})

        await asyncio.gather(*(one(p) for p in paths))

    (ROOT / "_definition_repair.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "items": results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"filled": sum(1 for r in results if r['status'] == 'filled'),
                      "empty": sum(1 for r in results if r['status'] == 'empty'),
                      "errors": sum(1 for r in results if r['status'] == 'error')}, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())
