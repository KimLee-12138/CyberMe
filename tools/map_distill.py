# -*- coding: utf-8 -*-
"""Step 7 — Map distillation: extract knowledge units from each section part.

Model: deepseek-flash, non-thinking, JSON output, temperature 0.
Input : data/sections/sections.jsonl (414 parts)
Output: data/units/{course}/{part_id}.json
        data/units/usage.csv
        data/units/failed.jsonl
        data/units/map_report.md

No truncation: the whole part text is sent (parts are already <=12k chars).
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

REPO = Path(r"D:\CyberMe\repo")
SEC = REPO / "data" / "sections" / "sections.jsonl"
OUT = REPO / "data" / "units"
OUT.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"
ALLOWED_TYPES = {"definition", "formula", "example", "procedure", "pitfall", "comparison", "fact"}

SYSTEM_PROMPT = """你是课程知识工程师。你的任务是从给定的课程资料片段中抽取“可复习、可引用”的知识单元。
只输出一个 JSON 对象，不要输出 Markdown 代码块、解释或前后缀。

硬性规则：
1. 只能依据给定原文，不得使用模型自身知识补充原文没有的公式、数值、结论、例子。
2. 原文公式或变量缺失时，unit 的 formula 置空并标 formula_missing=true；不要猜。
3. 私用区字符（\\uf000-\\uf8ff）是字体映射噪声，不要当作公式；若因此无法还原公式，标 formula_missing=true。
4. 每个 unit 必须能定位：page_start/page_end 必须在给定页码范围；Markdown 片段用 section_id。
5. 原文没有知识点（目录、页眉、水印、空页）时，has_knowledge=false，并给出 reason。
6. type 只能是：definition, formula, example, procedure, pitfall, comparison, fact。
7. units 最多 12 个；没有就空数组。
8. 输出必须是合法 JSON，字段齐全。

JSON 结构：
{
  "part_id": "原样返回输入 part_id",
  "has_knowledge": true,
  "reason": "",
  "summary": "2-3 句话概括本片段",
  "units": [
    {
      "type": "definition|formula|example|procedure|pitfall|comparison|fact",
      "title": "短标题",
      "statement": "完整陈述，只依据原文",
      "formula": "原文中的公式；没有则空字符串",
      "formula_missing": false,
      "conditions": ["适用条件"],
      "key_terms": ["关键词"],
      "page_start": 1,
      "page_end": 2,
      "section_id": "",
      "confidence": 0.9
    }
  ],
  "prerequisites": ["前置知识"],
  "open_questions": []
}
"""


def user_prompt(part: dict) -> str:
    return f"""课程: {part['course']}
part_id: {part['part_id']}
section_id: {part['section_id']}
标题路径: {' > '.join(part.get('heading_path') or [])}
页码范围: {part.get('page_start', 0)}-{part.get('page_end', 0)}
定位类型: {part.get('locator_kind', 'section')}

原文:
<<<
{part['text']}
>>>
"""


def parse_json(content: str):
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    return json.loads(content)


def normalize_result(obj: dict, part: dict) -> dict:
    if not isinstance(obj, dict):
        raise ValueError("not a JSON object")
    obj["part_id"] = part["part_id"]
    if "has_knowledge" not in obj:
        raise ValueError("missing has_knowledge")
    if not isinstance(obj["has_knowledge"], bool):
        raise ValueError("has_knowledge must be bool")
    if not obj["has_knowledge"]:
        if not obj.get("reason"):
            raise ValueError("has_knowledge=false without reason")
        obj.setdefault("units", [])
        return obj

    units = obj.get("units")
    if not isinstance(units, list) or not units:
        raise ValueError("has_knowledge=true but units empty")
    if len(units) > 12:
        units = units[:12]
    p_start = int(part.get("page_start") or 0)
    p_end = int(part.get("page_end") or 0)
    page_map = part.get("page_map") or []
    cleaned = []
    for u in units:
        if not isinstance(u, dict):
            raise ValueError("unit is not an object")
        t = u.get("type")
        if t not in ALLOWED_TYPES:
            raise ValueError(f"bad unit type: {t}")
        if not str(u.get("title", "")).strip() or not str(u.get("statement", "")).strip():
            raise ValueError("unit missing title/statement")
        # normalize locator
        ps = u.get("page_start")
        pe = u.get("page_end")
        if p_start and p_end:
            try:
                ps = int(ps) if ps not in (None, "") else p_start
                pe = int(pe) if pe not in (None, "") else p_end
            except Exception:
                ps, pe = p_start, p_end
            ps = min(max(ps, p_start), p_end)
            pe = min(max(pe, p_start), p_end)
            if pe < ps:
                ps, pe = pe, ps
        else:
            ps, pe = 0, 0
        u["page_start"], u["page_end"] = ps, pe
        u["section_id"] = u.get("section_id") or part["section_id"]

        # Map the unit statement back to the source page when possible.
        page_source = "section"
        if page_map:
            stmt = str(u.get("statement") or "")
            off = -1
            for probe_len in (40, 25, 15):
                probe = stmt[:probe_len]
                if probe:
                    off = part["text"].find(probe)
                    if off >= 0:
                        break
            if off >= 0:
                for pm in page_map:
                    if pm["char_start"] <= off < pm["char_end"]:
                        u["page_start"] = u["page_end"] = pm["page"]
                        page_source = "text_match"
                        break
                else:
                    u["page_start"], u["page_end"] = p_start, p_end
                    page_source = "section_range"
            else:
                u["page_start"], u["page_end"] = p_start, p_end
                page_source = "section_range"
        u["page_source"] = page_source

        u["formula_missing"] = bool(u.get("formula_missing", False))
        u["formula"] = str(u.get("formula") or "")
        u["conditions"] = u.get("conditions") or []
        u["key_terms"] = u.get("key_terms") or []
        try:
            u["confidence"] = float(u.get("confidence", 0.8))
        except Exception:
            u["confidence"] = 0.8
        cleaned.append(u)
    obj["units"] = cleaned
    obj.setdefault("summary", "")
    obj.setdefault("prerequisites", [])
    obj.setdefault("open_questions", [])
    return obj


async def call_one(client: httpx.AsyncClient, part: dict, key: str, sem: asyncio.Semaphore,
                   attempts: int = 3) -> dict:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt(part)},
        ],
        "temperature": 0,
        "max_tokens": 6000,
        "response_format": {"type": "json_object"},
        "thinking": {"type": "disabled"},
        "stream": False,
    }
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    last_err = ""
    for attempt in range(1, attempts + 1):
        t0 = time.time()
        try:
            async with sem:
                resp = await client.post(API_URL, headers=headers, json=payload)
            latency = int((time.time() - t0) * 1000)
            if resp.status_code == 429:
                await asyncio.sleep(5 * attempt)
                last_err = "429"
                continue
            if resp.status_code >= 500:
                await asyncio.sleep(3 * attempt)
                last_err = f"{resp.status_code}"
                continue
            if resp.status_code != 200:
                last_err = f"HTTP {resp.status_code}: {resp.text[:300]}"
                continue
            data = resp.json()
            choice = data["choices"][0]
            if choice.get("finish_reason") == "length":
                last_err = "output truncated (finish_reason=length)"
                continue
            content = choice["message"]["content"]
            try:
                obj = parse_json(content)
            except Exception:
                raw_dir = OUT / "_failed_raw"
                raw_dir.mkdir(parents=True, exist_ok=True)
                (raw_dir / f"{part['part_id']}.txt").write_text(content, encoding="utf-8")
                raise
            obj = normalize_result(obj, part)
            usage = data.get("usage", {}) or {}
            return {
                "ok": True,
                "part": part,
                "result": obj,
                "usage": usage,
                "latency_ms": latency,
                "attempts": attempt,
                "model": data.get("model", MODEL),
                "finish_reason": choice.get("finish_reason"),
                "raw_content": content,
            }
        except Exception as e:
            last_err = str(e)[:300]
            if attempt < attempts:
                await asyncio.sleep(2 * attempt)
    return {"ok": False, "part": part, "error": last_err}


async def main_async(limit: int | None, concurrency: int) -> None:
    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set in the environment")

    parts = [json.loads(x) for x in SEC.read_text(encoding="utf-8").splitlines() if x.strip()]
    if limit:
        parts = parts[:limit]
    print(f"parts: {len(parts)}  model={MODEL}  concurrency={concurrency}", flush=True)

    sem = asyncio.Semaphore(concurrency)
    done = 0
    lock = asyncio.Lock()
    usage_rows = []
    failures = []

    async with httpx.AsyncClient(timeout=httpx.Timeout(180.0, connect=30.0)) as client:
        async def worker(part):
            nonlocal done
            out_path = OUT / part["course"] / f"{part['part_id']}.json"
            if out_path.exists():
                try:
                    old = json.loads(out_path.read_text(encoding="utf-8"))
                    if old.get("part_id") == part["part_id"] and isinstance(old.get("result"), dict):
                        async with lock:
                            done += 1
                        return
                except Exception:
                    pass
            res = await call_one(client, part, key, sem)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            if res["ok"]:
                envelope = {
                    "part_id": part["part_id"],
                    "section_id": part["section_id"],
                    "source_id": part["source_id"],
                    "course": part["course"],
                    "heading_path": part.get("heading_path", []),
                    "page_start": part.get("page_start", 0),
                    "page_end": part.get("page_end", 0),
                    "model": res["model"],
                    "usage": res["usage"],
                    "latency_ms": res["latency_ms"],
                    "attempts": res["attempts"],
                    "distilled_at": datetime.now(timezone.utc).isoformat(),
                    "result": res["result"],
                }
                tmp = out_path.with_suffix(".tmp")
                tmp.write_text(json.dumps(envelope, ensure_ascii=False, indent=2), encoding="utf-8")
                tmp.replace(out_path)
                async with lock:
                    usage_rows.append({
                        "part_id": part["part_id"],
                        "course": part["course"],
                        "input_tokens": res["usage"].get("prompt_tokens", 0),
                        "output_tokens": res["usage"].get("completion_tokens", 0),
                        "total_tokens": res["usage"].get("total_tokens", 0),
                        "latency_ms": res["latency_ms"],
                        "attempts": res["attempts"],
                    })
                    done += 1
                    if done % 10 == 0:
                        print(f"  {done}/{len(parts)}", flush=True)
            else:
                async with lock:
                    failures.append({"part_id": part["part_id"], "course": part["course"],
                                     "error": res["error"]})
                    done += 1
                    if done % 10 == 0:
                        print(f"  {done}/{len(parts)}  failures={len(failures)}", flush=True)

        await asyncio.gather(*(worker(p) for p in parts))

    # usage csv
    usage_path = OUT / "usage.csv"
    write_header = not usage_path.exists()
    with usage_path.open("a", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["part_id", "course", "input_tokens", "output_tokens", "total_tokens", "latency_ms", "attempts"])
        if write_header:
            w.writeheader()
        w.writerows(usage_rows)

    # failures
    if failures:
        with (OUT / "failed.jsonl").open("a", encoding="utf-8") as f:
            for x in failures:
                f.write(json.dumps(x, ensure_ascii=False) + "\n")

    # report
    all_files = list(OUT.glob("*/*.json"))
    ok = 0
    no_knowledge = 0
    unit_total = 0
    for p in all_files:
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
            r = d.get("result", {})
            ok += 1
            if not r.get("has_knowledge"):
                no_knowledge += 1
            unit_total += len(r.get("units", []))
        except Exception:
            pass
    inp = sum(x["input_tokens"] for x in usage_rows)
    out = sum(x["output_tokens"] for x in usage_rows)
    lines = [
        "# Step 7 — Map distillation report",
        "",
        f"- parts requested: {len(parts)}",
        f"- completed outputs: {ok}",
        f"- failed: {len(failures)}",
        f"- has_knowledge=false: {no_knowledge}",
        f"- knowledge units: {unit_total}",
        f"- input tokens: {inp:,}",
        f"- output tokens: {out:,}",
        f"- total tokens: {inp + out:,}",
        "",
        "## Failed",
        "",
    ]
    for x in failures[:50]:
        lines.append(f"- {x['course']} {x['part_id']}: {x['error']}")
    (OUT / "map_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "requested": len(parts),
        "completed": ok,
        "failed": len(failures),
        "no_knowledge": no_knowledge,
        "units": unit_total,
        "input_tokens": inp,
        "output_tokens": out,
    }, ensure_ascii=False, indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()
    asyncio.run(main_async(args.limit, args.concurrency))


if __name__ == "__main__":
    main()
