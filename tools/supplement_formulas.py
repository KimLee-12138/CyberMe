# -*- coding: utf-8 -*-
"""Second pass: fill formulas for formula-missing enriched notes.

Formulas extracted from SOURCE are marked source-supported. If the model has
to use general knowledge, the formula is explicitly marked "AI 补充，需核对".
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
STEM = {"ALGO", "ASM", "CALCULUS", "CO", "CPP", "DB", "DISCRETE", "DS", "EDA",
        "JAVA", "PHYSICS", "PROB", "RLMATH", "SE"}

SYSTEM = """你是课程公式整理员。给你旧笔记 (NOTE) 和原文 (SOURCE)，请找出该主题真正需要的公式。
只输出严格 JSON：
{
  "has_formula_topic": true,
  "formulas": [
    {"formula": "公式", "meaning": "变量/条件/用途", "from_source": true}
  ]
}
规则：
1. 先判断主题是否真的存在公式/定量关系；纯概念、流程、历史、管理类主题 has_formula_topic=false，返回空数组，不要硬塞公式。
2. 能从 SOURCE 找到的公式，from_source=true；SOURCE 没有、但该主题确实需要公式时，可用模型知识给出，from_source=false，不得伪造原文。
3. 公式必须带变量含义/适用条件；不确定就不要写。
4. 不要输出 Markdown 代码块或解释。"""


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


def get_section(body: str, name: str) -> str:
    m = re.search(rf"^##\s+{re.escape(name)}.*?$\n(.*?)(?=^##\s+|\Z)", body, re.M | re.S)
    return (m.group(1).strip() if m else "")


def set_formula_section(body: str, formulas: list[dict]) -> str:
    lines = ["## 公式", ""]
    for f in formulas:
        suffix = "" if f.get("from_source") else "（AI 补充，需核对）"
        lines.append(f"- `{f['formula']}`：{f.get('meaning', '')}{suffix}".rstrip("："))
    lines.append("")
    block = "\n".join(lines)
    if re.search(r"^##\s+公式.*?$", body, re.M):
        return re.sub(r"^##\s+公式.*?$\n(.*?)(?=^##\s+|\Z)", block, body, count=1, flags=re.M | re.S)
    # insert before examples/pitfalls if possible
    for anchor in ("## 例子", "## 易错点", "## 关系", "## 来源"):
        if anchor in body:
            return body.replace(anchor, block + "\n" + anchor, 1)
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
        if fm.get("course") not in STEM:
            continue
        flags = (fm.get("enrichment") or {}).get("flags") or []
        if "formula_missing" in flags and not get_section(body, "公式"):
            paths.append(p)

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
            source_text = "\n\n".join(src)[:5500]
            note = body[:3500]
            user = f"课程：{fm.get('course')}\n标题：{fm.get('title')}\n\n旧笔记：\n<<<\n{note}\n>>>\n\n原文：\n<<<\n{source_text}\n>>>"
            try:
                async with sem:
                    resp = await client.post(
                        API_URL,
                        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                        json={
                            "model": MODEL,
                            "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                            "temperature": 0,
                            "max_tokens": 900,
                            "thinking": {"type": "disabled"},
                            "response_format": {"type": "json_object"},
                            "stream": False,
                        },
                    )
                if resp.status_code != 200:
                    raise RuntimeError(resp.text[:200])
                obj = parse_json(resp.json()["choices"][0]["message"]["content"])
                formulas = []
                for f in obj.get("formulas") or []:
                    if not isinstance(f, dict):
                        continue
                    formula = clean(str(f.get("formula") or ""))
                    if not formula or len(formula) > 500:
                        continue
                    formulas.append({
                        "formula": formula,
                        "meaning": clean(str(f.get("meaning") or ""))[:700],
                        "from_source": bool(f.get("from_source", False)),
                    })
                    if len(formulas) >= 6:
                        break
                if not formulas:
                    enr = dict(fm.get("enrichment") or {})
                    enr["formula_expected"] = False
                    enr["flags"] = [x for x in (enr.get("flags") or []) if x != "formula_missing"]
                    fm["enrichment"] = enr
                    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
                    path.write_text(f"---\n{fm_text}\n---\n\n{body.lstrip()}", encoding="utf-8")
                    results.append({"note_id": fm.get("id"), "status": "no_formula_topic"})
                    return
                body2 = set_formula_section(body, formulas)
                enr = dict(fm.get("enrichment") or {})
                enr["formula_expected"] = True
                enr["flags"] = [x for x in (enr.get("flags") or []) if x != "formula_missing"]
                enr["formula_support"] = [
                    {"formula": f["formula"], "source_supported": f["from_source"]} for f in formulas
                ]
                enr["formula_repair"] = "enrich-v1"
                fm["enrichment"] = enr
                fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
                path.write_text(f"---\n{fm_text}\n---\n\n{body2.lstrip()}", encoding="utf-8")
                results.append({"note_id": fm.get("id"), "status": "filled", "count": len(formulas),
                                "source_supported": sum(1 for f in formulas if f["from_source"])})
                print(fm.get("id"), "filled", len(formulas), flush=True)
            except Exception as e:
                results.append({"note_id": fm.get("id"), "status": "error", "error": str(e)[:200]})

        await asyncio.gather(*(one(p) for p in paths))

    (ROOT / "_formula_repair.json").write_text(
        json.dumps({"generated_at": datetime.now(timezone.utc).isoformat(), "items": results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Formula repair", ""]
    for r in results:
        lines.append(f"- {r['note_id']}: {r['status']} {r.get('count', '')} {r.get('source_supported', '')}")
    (ROOT / "_formula_repair.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"candidates": len(paths), "filled": sum(1 for r in results if r['status'] == 'filled'),
                      "no_formula": sum(1 for r in results if r['status'] == 'no_formula_topic'),
                      "errors": sum(1 for r in results if r['status'] == 'error')}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
