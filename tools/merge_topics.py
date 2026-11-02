# -*- coding: utf-8 -*-
"""Step 8 — merge knowledge units into section-level topics.

Input : data/units/{course}/*.json + data/sections/sections.jsonl
Output: data/topics/{course}.jsonl
        data/topics/_topic_map.csv
        data/topics/topic_report.md

Strategy:
  - group units by section_id
  - dedupe identical units inside a section
  - 1 topic for <=12 units; 2 for 13-20; 3 for >20 (sorted by base title)
  - one DeepSeek Flash call per topic group (JSON, non-thinking)
  - sources are normalized to the union of input unit sources
"""
from __future__ import annotations

import argparse
import asyncio
import csv
import json
import math
import os
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import httpx

REPO = Path(r"D:\CyberMe\repo")
UNITS = REPO / "data" / "units"
SEC = REPO / "data" / "sections" / "sections.jsonl"
OUT = REPO / "data" / "topics"
OUT.mkdir(parents=True, exist_ok=True)

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"

SYSTEM_PROMPT = """你是课程知识编辑。把同一小节的知识单元合并成一篇可复习的主题笔记。
只输出一个 JSON 对象，不要输出 Markdown 代码块、解释或前后缀。

硬性规则：
1. 只能使用输入 units 的信息，不得补充外部知识、公式、数值或例子。
2. 合并重复项；保留所有不同的 key point；不要丢失输入中的事实。
3. 公式原样保留；input 中 formula_missing=true 的不要猜，保留标记。
4. sources 只使用输入中出现的 source_id / page / section_id，不得虚构。
5. units 之间有矛盾时写入 conflicts，不要静默选择。
6. title 用最具体的主题名；aliases 列别名。
7. 输出必须是合法 JSON，字段齐全。

JSON 结构：
{
  "title": "主题名",
  "aliases": ["别名"],
  "summary": "3-5 句话概括",
  "definition": "核心定义；没有则空字符串",
  "key_points": ["要点1", "要点2"],
  "formulas": [
    {"formula": "公式", "meaning": "含义", "page_start": 1, "page_end": 1}
  ],
  "examples": ["例子"],
  "pitfalls": ["易错点"],
  "relations": [
    {"type": "prerequisite_of|contrasts_with|related_to", "target": "另一个主题"}
  ],
  "sources": [
    {"source_id": "SRC-...", "page_start": 1, "page_end": 2, "section_id": "..."}
  ],
  "conflicts": ["冲突说明"],
  "confidence": 0.9
}
"""


def base_title(t: str) -> str:
    t = re.sub(r"^[\d一二三四五六七八九十]+[\.、_\- ]*", "", str(t)).strip()
    t = re.sub(r"[（(].*?[)）]", "", t)
    t = re.sub(r"(的定义|概念|性质|定理|公式|例题|题解|详解|总结|应用|优化|复杂度|"
               r"遍历顺序|状态定义|转移方程|实现|代码|模板|步骤|方法|区别|比较|关系|作用|特点|分类|计算|推导|证明)$", "", t)
    t = re.sub(r"的$", "", t)
    return t.strip() or str(t)


def unit_prompt(course: str, section_id: str, heading_path: list[str], units: list[dict]) -> str:
    payload = []
    for u in units:
        payload.append({
            "unit_id": u["unit_id"],
            "type": u.get("type"),
            "title": u.get("title"),
            "statement": u.get("statement"),
            "formula": u.get("formula"),
            "formula_missing": u.get("formula_missing"),
            "key_terms": u.get("key_terms", []),
            "page_start": u.get("page_start"),
            "page_end": u.get("page_end"),
            "page_source": u.get("page_source"),
            "source_id": u.get("source_id"),
        })
    return f"""课程: {course}
section_id: {section_id}
标题路径: {' > '.join(heading_path or [])}

知识单元（JSON）:
{json.dumps(payload, ensure_ascii=False, indent=1)}
"""


def parse_json(content: str):
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    return json.loads(content)


def norm_sources(units: list[dict]) -> list[dict]:
    out = {}
    for u in units:
        sid = u.get("source_id") or ""
        ps = int(u.get("page_start") or 0)
        pe = int(u.get("page_end") or 0)
        sec = u.get("section_id") or ""
        key = (sid, ps, pe, sec)
        out[key] = {"source_id": sid, "page_start": ps, "page_end": pe, "section_id": sec}
    return list(out.values())


def normalize_topic(obj: dict, units: list[dict], course: str, section_id: str, heading_path: list[str]) -> dict:
    if not isinstance(obj, dict):
        raise ValueError("not an object")
    title = str(obj.get("title") or "").strip()
    if not title:
        title = (heading_path[-1] if heading_path else "") or (units[0].get("title") or "未命名主题")
    key_points = obj.get("key_points") or []
    if not isinstance(key_points, list):
        key_points = [str(key_points)]
    if not key_points:
        key_points = [u["statement"] for u in units if u.get("statement")]
    formulas = obj.get("formulas") or []
    if not isinstance(formulas, list):
        formulas = []
    examples = obj.get("examples") or []
    pitfalls = obj.get("pitfalls") or []
    relations = obj.get("relations") or []
    conflicts = obj.get("conflicts") or []
    try:
        confidence = float(obj.get("confidence", 0.8))
    except Exception:
        confidence = 0.8
    return {
        "title": title,
        "aliases": obj.get("aliases") or [],
        "summary": obj.get("summary") or "",
        "definition": obj.get("definition") or "",
        "key_points": [str(x) for x in key_points][:30],
        "formulas": formulas[:20],
        "examples": [str(x) for x in examples][:20],
        "pitfalls": [str(x) for x in pitfalls][:20],
        "relations": relations[:20],
        "sources": norm_sources(units),
        "conflicts": [str(x) for x in conflicts][:10],
        "confidence": confidence,
        "section_id": section_id,
        "course": course,
    }


def fallback_topic(units: list[dict], course: str, section_id: str, heading_path: list[str]) -> dict:
    return {
        "title": (heading_path[-1] if heading_path else "") or (units[0].get("title") or "未命名主题"),
        "aliases": [],
        "summary": "",
        "definition": "",
        "key_points": [u["statement"] for u in units if u.get("statement")][:30],
        "formulas": [
            {"formula": u.get("formula"), "meaning": "", "page_start": u.get("page_start", 0), "page_end": u.get("page_end", 0)}
            for u in units if u.get("formula")
        ][:20],
        "examples": [u["statement"] for u in units if u.get("type") == "example"][:20],
        "pitfalls": [u["statement"] for u in units if u.get("type") == "pitfall"][:20],
        "relations": [],
        "sources": norm_sources(units),
        "conflicts": [],
        "confidence": 0.5,
        "section_id": section_id,
        "course": course,
        "fallback": True,
    }


async def call_topic(client: httpx.AsyncClient, key: str, course: str, section_id: str,
                     heading_path: list[str], units: list[dict], sem: asyncio.Semaphore,
                     attempts: int = 3) -> dict:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": unit_prompt(course, section_id, heading_path, units)},
        ],
        "temperature": 0,
        "max_tokens": 4000,
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
                last_err = "truncated"
                continue
            content = choice["message"]["content"]
            try:
                obj = parse_json(content)
            except Exception:
                raw_dir = OUT / "_failed_raw"
                raw_dir.mkdir(parents=True, exist_ok=True)
                (raw_dir / f"{section_id}.txt").write_text(content, encoding="utf-8")
                raise
            topic = normalize_topic(obj, units, course, section_id, heading_path)
            return {"ok": True, "topic": topic, "usage": data.get("usage", {}),
                    "latency_ms": latency, "attempts": attempt, "model": data.get("model", MODEL)}
        except Exception as e:
            last_err = str(e)[:300]
            if attempt < attempts:
                await asyncio.sleep(2 * attempt)
    return {"ok": False, "error": last_err}


def load_units() -> tuple[list[dict], dict[str, dict]]:
    sections = {}
    for line in SEC.read_text(encoding="utf-8").splitlines():
        if line.strip():
            s = json.loads(line)
            sections[s["part_id"]] = s
    units = []
    for p in UNITS.glob("*/*.json"):
        d = json.loads(p.read_text(encoding="utf-8"))
        r = d.get("result", {})
        if not r.get("has_knowledge"):
            continue
        part_id = d["part_id"]
        meta = sections.get(part_id, {})
        for i, u in enumerate(r.get("units", []), 1):
            units.append({
                **u,
                "unit_id": f"{part_id}-U{i:02d}",
                "part_id": part_id,
                "section_id": d.get("section_id") or meta.get("section_id") or "",
                "source_id": d.get("source_id") or meta.get("source_id") or "",
                "course": d.get("course") or meta.get("course") or "",
                "heading_path": meta.get("heading_path") or d.get("heading_path") or [],
                "section_page_start": meta.get("page_start", 0),
                "section_page_end": meta.get("page_end", 0),
            })
    return units, sections


def dedupe_units(units: list[dict]) -> list[dict]:
    out = {}
    for u in units:
        key = (re.sub(r"\s+", "", str(u.get("title", ""))), re.sub(r"\s+", "", str(u.get("statement", ""))))
        if key not in out:
            out[key] = u
        else:
            old = out[key]
            old["key_terms"] = list(dict.fromkeys((old.get("key_terms") or []) + (u.get("key_terms") or [])))
            old["confidence"] = max(float(old.get("confidence", 0)), float(u.get("confidence", 0)))
    return list(out.values())


async def main() -> None:
    units, sections = load_units()
    print(f"units: {len(units)}", flush=True)

    by_section = defaultdict(list)
    for u in units:
        by_section[u["section_id"]].append(u)
    print(f"sections with units: {len(by_section)}", flush=True)

    groups = []  # (section_id, course, heading_path, units)
    for sid, us in sorted(by_section.items()):
        us = dedupe_units(us)
        us.sort(key=lambda u: base_title(u.get("title", "")))
        n = 1 if len(us) <= 12 else (2 if len(us) <= 20 else 3)
        if n == 1:
            groups.append((sid, us[0]["course"], us[0]["heading_path"], us))
        else:
            size = math.ceil(len(us) / n)
            for i in range(0, len(us), size):
                chunk = us[i:i + size]
                if chunk:
                    groups.append((sid, chunk[0]["course"], chunk[0]["heading_path"], chunk))
    print(f"topic groups: {len(groups)}", flush=True)

    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--concurrency", type=int, default=8)
    args = ap.parse_args()
    if args.limit:
        groups = groups[:args.limit]

    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY not set")

    sem = asyncio.Semaphore(args.concurrency)
    results = []
    failures = []
    done = 0

    async with httpx.AsyncClient(timeout=httpx.Timeout(180.0, connect=30.0)) as client:
        async def worker(idx, group):
            nonlocal done
            sid, course, heading_path, us = group
            res = await call_topic(client, key, course, sid, heading_path, us, sem)
            if res["ok"]:
                results.append({
                    "topic_id": f"TOP-{course}-{idx:04d}",
                    "course": course,
                    "section_id": sid,
                    "heading_path": heading_path,
                    "unit_ids": [u["unit_id"] for u in us],
                    "unit_count": len(us),
                    "model": res["model"],
                    "usage": res["usage"],
                    "latency_ms": res["latency_ms"],
                    "attempts": res["attempts"],
                    "distilled_at": datetime.now(timezone.utc).isoformat(),
                    "topic": res["topic"],
                })
            else:
                topic = fallback_topic(us, course, sid, heading_path)
                results.append({
                    "topic_id": f"TOP-{course}-{idx:04d}",
                    "course": course,
                    "section_id": sid,
                    "heading_path": heading_path,
                    "unit_ids": [u["unit_id"] for u in us],
                    "unit_count": len(us),
                    "model": "fallback",
                    "usage": {},
                    "latency_ms": 0,
                    "attempts": 0,
                    "distilled_at": datetime.now(timezone.utc).isoformat(),
                    "topic": topic,
                })
                failures.append({"section_id": sid, "course": course, "error": res["error"]})
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{len(groups)}", flush=True)

        await asyncio.gather(*(worker(i + 1, g) for i, g in enumerate(groups)))

    # write per-course jsonl
    by_course = defaultdict(list)
    for r in results:
        by_course[r["course"]].append(r)
    for course, rows in by_course.items():
        rows.sort(key=lambda x: x["topic_id"])
        with (OUT / f"{course}.jsonl").open("w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # unit -> topic map
    with (OUT / "_topic_map.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["topic_id", "course", "section_id", "unit_id", "source_id", "title"])
        for r in results:
            for uid in r["unit_ids"]:
                w.writerow([r["topic_id"], r["course"], r["section_id"], uid, "", r["topic"].get("title", "")])

    # report
    total_units = sum(r["unit_count"] for r in results)
    fallback = sum(1 for r in results if r.get("topic", {}).get("fallback"))
    lines = [
        "# Step 8 — Topic merge report",
        "",
        f"- units: {len(units)}",
        f"- sections with units: {len(by_section)}",
        f"- topics: {len(results)}",
        f"- units assigned: {total_units}",
        f"- fallback topics: {fallback}",
        f"- failed calls: {len(failures)}",
        "",
        "## Topics by course",
        "",
        "| course | topics | units |",
        "|---|---:|---:|",
    ]
    for c in sorted(by_course):
        lines.append(f"| {c} | {len(by_course[c])} | {sum(x['unit_count'] for x in by_course[c])} |")
    if failures:
        lines += ["", "## Failed sections", ""]
        for x in failures[:50]:
            lines.append(f"- {x['course']} {x['section_id']}: {x['error']}")
    (OUT / "topic_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "units": len(units),
        "sections": len(by_section),
        "topics": len(results),
        "units_assigned": total_units,
        "fallback": fallback,
        "failed": len(failures),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
