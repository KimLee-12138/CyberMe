# -*- coding: utf-8 -*-
"""Enrich generated notes from their original source sections.

This is deliberately separate from the original note generator:

- `data/notes/` stays untouched as the v1 artifact.
- The enrichment reads raw `data/sections/sections.jsonl` for the pages cited
  by each note, so it is not limited to the previous note text.
- Every output is marked `verification: ai_enriched` and keeps a list of
  fields that were source-supported vs. AI-supplemented.
- Missing source facts stay missing. The model is never asked to invent a
  formula or definition it cannot find in the source.

Usage:
  $env:DEEPSEEK_API_KEY=[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY','User')
  python tools/enrich_notes.py --limit 20 --concurrency 4
  python tools/enrich_notes.py --concurrency 8
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
import yaml

REPO = Path(__file__).resolve().parents[1]
NOTES = REPO / "data" / "notes"
SECTIONS = REPO / "data" / "sections" / "sections.jsonl"
OUT = REPO / "data" / "notes_enriched"
API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"

SECTION_LIMIT = 6500
NOTE_LIMIT = 3200
VERSION = "enrich-v1"
FORMULA_COURSES = {
    "ALGO", "ASM", "CALCULUS", "CO", "CPP", "DB", "DISCRETE",
    "DS", "EDA", "JAVA", "PHYSICS", "PROB", "RLMATH", "SE",
}

SYSTEM_PROMPT = """你是课程知识库的数据清洗与补全器。你面对一篇旧笔记 (NOTE) 和它引用的原文 (SOURCE)。
你的任务不是写一篇新文章，而是把旧笔记修成“可追溯、可复习、没有内部字段噪声”的知识卡。

硬性规则：
1. 只能依据 SOURCE 和 NOTE 中已有的事实。SOURCE 没有的公式、定义、数值、例子，一律留空，不要凭模型常识补写。
2. SOURCE 可能有封面、课程群名、水印、OCR 缺字、代码碎片。忽略与主题无关的内容。
3. 旧笔记里的“（来源：SRC-...）”“[E1]”“原文公式缺失”等是内部元数据，不要写进正文。
4. 如果有内容只能靠模型常识补充，放进 supplement，并明确写成“补充理解（非原文）”；不能混进 definition / formulas / examples。
5. 公式只从 SOURCE 或 NOTE 中抄录；公式缺变量时原样保留，不要造变量。
6. 输出严格 JSON，不要 Markdown 代码块、不要解释。

JSON 结构：
{
  "one_line": "一句话结论；没有就空字符串",
  "definition": "严格基于原文的定义；没有就空字符串",
  "key_points": ["3-8 条自包含的关键点，不要写来源编号"],
  "formulas": [
    {"formula": "原文公式", "meaning": "它表示什么；只依据原文", "source_supported": true}
  ],
  "examples": ["原文中的例子或例题；没有就空数组"],
  "pitfalls": ["易错点；只依据原文或旧笔记，没有就空数组"],
  "aliases": ["同义叫法；没有就空数组"],
  "supplement": "可选的补充理解；严格标注非原文，不能包含未经原文支持的事实；没有就空字符串",
  "source_supported": ["definition", "key_points", "formulas", "examples", "pitfalls"],
  "flags": ["definition_missing", "formula_missing", "example_missing", "source_noisy"],
  "confidence": 0.0
}
"""


def clean_text(text: str) -> str:
    """Remove internal metadata and page markers from prose."""
    text = str(text or "")
    text = re.sub(r"<!-- page: \d+ -->", "", text)
    text = re.sub(r"[（(]\s*来源\s*[:：][^）)]{0,200}[）)]", "", text)
    text = re.sub(r"\bSRC-[A-Z]+-\d+(?:-SEC\d+)?\b", "", text)
    text = re.sub(r"\[E\d+\]", "", text)
    text = re.sub(r"^.*(?:本节.*(?:公式|变量).*缺失|原文.*(?:公式|变量).*缺失|未补写|待补充).*$", "", text, flags=re.M)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n\n?", text, re.S)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = {}
    return fm, text[m.end():]


def parse_sections(body: str) -> dict[str, str]:
    out = {}
    for m in re.finditer(r"^##\s+(.+?)\s*$\n(.*?)(?=^##\s+|\Z)", body, re.M | re.S):
        key = m.group(1).strip()
        val = clean_text(m.group(2))
        if val:
            out[key] = val
    return out


def first_sentence(text: str) -> str:
    text = clean_text(text)
    if not text:
        return ""
    parts = re.split(r"(?<=[。！？.!?])\s*", text, maxsplit=1)
    return parts[0].strip()


def list_lines(text: str) -> list[str]:
    lines = []
    for line in clean_text(text).splitlines():
        line = re.sub(r"^\s*(?:\d+[.、)]|[-*•])\s*", "", line).strip()
        if line:
            lines.append(line)
    return lines


def source_text_for_sources(sources: list[dict], by_source: dict[str, list[dict]]) -> str:
    chosen: list[str] = []
    total = 0
    for src in sources:
        sid = str(src.get("source_id") or "")
        if not sid:
            continue
        parts = by_source.get(sid) or []
        # Prefer parts overlapping the note's cited page range.
        ranges = src.get("source_pages") or []
        ps = pe = 0
        if isinstance(ranges, list) and len(ranges) >= 2:
            try:
                ps, pe = int(ranges[0]), int(ranges[1])
            except Exception:
                ps = pe = 0
        selected = []
        for part in parts:
            p_start = int(part.get("page_start") or 0)
            p_end = int(part.get("page_end") or 0)
            if not ps or not p_start or not p_end or (p_end >= ps and p_start <= pe):
                selected.append(part)
        if not selected:
            selected = parts
        for part in selected:
            text = clean_text(part.get("text") or "")
            if not text:
                continue
            if total + len(text) > SECTION_LIMIT:
                text = text[: max(0, SECTION_LIMIT - total)]
            if not text:
                break
            chosen.append(f"[{sid}] {text}")
            total += len(text)
            if total >= SECTION_LIMIT:
                break
        if total >= SECTION_LIMIT:
            break
    return "\n\n".join(chosen)[:SECTION_LIMIT]


def build_user_prompt(title: str, course: str, existing: dict[str, str],
                      source_text: str) -> str:
    compact = {
        "title": title,
        "course": course,
        "existing": {
            "one_line": existing.get("一句话", "")[:500],
            "definition": existing.get("定义", "")[:1000],
            "key_points": list_lines(existing.get("关键点", ""))[:8],
            "formulas": list_lines(existing.get("公式", ""))[:8],
            "examples": list_lines(existing.get("例子", ""))[:6],
            "pitfalls": list_lines(existing.get("易错点", ""))[:6],
        },
    }
    return f"""课程: {course}
标题: {title}

现有笔记:
<<<NOTE
{json.dumps(compact, ensure_ascii=False)}
NOTE

原文证据（只能用来核对/补全；可能有 OCR 噪声）:
<<<SOURCE
{source_text or '（没有可用原文）'}
SOURCE

请输出 JSON。若原文没有定义/公式/例子，对应字段留空，不要编造。"""


def parse_json(content: str) -> dict:
    content = (content or "").strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
    return json.loads(content)


def normalize_for_match(text: str) -> str:
    text = clean_text(text).lower()
    text = text.replace("`", "").replace("\\", "")
    text = re.sub(r"\s+", "", text)
    return text


def source_supports_formula(formula: str, source_text: str,
                            existing_formulas: str) -> bool:
    """Best-effort provenance check for formulas.

    A formula can be written with LaTeX escapes/spacing differences, so exact
    string matching is too strict. We compare after removing common formatting
    characters and whitespace. If it is not in the source or old note, the
    formula is kept but marked "需核对" (do not silently drop a useful formula).
    """
    needle = normalize_for_match(formula)
    if len(needle) < 4:
        return False
    hay = normalize_for_match(source_text + "\n" + existing_formulas)
    if needle in hay:
        return True
    # Long formulas may have a source-side line break or omitted subscript.
    chunks = [c for c in re.split(r"[+\-=<>()（）,，;；]", needle) if len(c) >= 6]
    if chunks:
        return all(c in hay for c in chunks[:3])
    return False


def as_list(value: Any, limit: int = 10) -> list[str]:
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, dict):
                item = item.get("text") or item.get("formula") or ""
            item = clean_text(str(item))
            if item and item not in out:
                out.append(item)
            if len(out) >= limit:
                break
        return out
    if isinstance(value, str) and value.strip():
        return [clean_text(value)]
    return []


def normalize_result(raw: dict, existing: dict[str, str], title: str,
                     source_text: str = "", course: str = "") -> dict:
    if not isinstance(raw, dict):
        raise ValueError("not a JSON object")
    raw = dict(raw)

    def field(name: str, cap: int) -> str:
        v = clean_text(raw.get(name) or "")
        return v[:cap].strip()

    existing_formulas = "\n".join(list_lines(existing.get("公式", "")))
    formulas = []
    for item in raw.get("formulas") or []:
        if not isinstance(item, dict):
            continue
        formula = clean_text(str(item.get("formula") or ""))
        if not formula or any(x in formula for x in ("缺失", "未补写", "暂无")):
            continue
        supported = source_supports_formula(formula, source_text, existing_formulas)
        formulas.append({
            "formula": formula[:500],
            "meaning": clean_text(str(item.get("meaning") or ""))[:800],
            "source_supported": supported,
        })
        if len(formulas) >= 8:
            break
    # If the model returned no formula, keep formulas already present in the
    # old note (checked against source/old text, not blindly trusted).
    if not formulas:
        for line in list_lines(existing.get("公式", ""))[:8]:
            m = re.search(r"`([^`]+)`\s*[:：]?\s*(.*)", line)
            if m:
                formulas.append({
                    "formula": m.group(1).strip()[:500],
                    "meaning": m.group(2).strip()[:800],
                    "source_supported": source_supports_formula(m.group(1), source_text, existing_formulas),
                })

    def merge_field(name: str, key: str, cap: int) -> str:
        ai_value = field(key, cap)
        return ai_value or clean_text(existing.get(name, ""))[:cap]

    one_line = merge_field("一句话", "one_line", 500)
    definition = merge_field("定义", "definition", 1600)
    key_points = as_list(raw.get("key_points"), 10) or list_lines(existing.get("关键点", ""))[:8]
    examples = as_list(raw.get("examples"), 6) or list_lines(existing.get("例子", ""))[:5]
    pitfalls = as_list(raw.get("pitfalls"), 6) or list_lines(existing.get("易错点", ""))[:5]
    aliases = as_list(raw.get("aliases"), 8)
    supplement = field("supplement", 1600)
    # Drop meta-commentary such as "原文没有..." from the supplement field.
    if any(x in supplement for x in ("原文证据", "旧笔记", "未包含", "未直接出现", "仅依据旧笔记")):
        supplement = ""
    conflict = clean_text(existing.get("冲突", ""))[:1600]

    if not one_line:
        one_line = first_sentence(definition) or title

    flags = []
    if not definition:
        flags.append("definition_missing")
    if not formulas and course in FORMULA_COURSES:
        flags.append("formula_missing")
    if not examples:
        flags.append("example_missing")
    if not pitfalls:
        flags.append("pitfall_missing")
    raw_flags = as_list(raw.get("flags"), 10)
    for f in raw_flags:
        if f not in flags:
            flags.append(f)
    if conflict and "has_conflict" not in flags:
        flags.append("has_conflict")

    return {
        "one_line": one_line,
        "definition": definition,
        "key_points": key_points[:8],
        "formulas": formulas,
        "examples": examples[:5],
        "pitfalls": pitfalls[:5],
        "aliases": aliases,
        "supplement": supplement,
        "conflict": conflict,
        "flags": flags,
        "confidence": max(0.0, min(1.0, float(raw.get("confidence", 0.8) or 0.8))),
    }


def render_note(fm: dict, result: dict, existing_relations: str, source_lines: list[str]) -> str:
    title = str(fm.get("title") or "").strip()
    body = [f"# {title}", ""]
    if result["one_line"]:
        body += ["## 一句话", result["one_line"], ""]
    if result["definition"]:
        body += ["## 定义", result["definition"], ""]
    if result["key_points"]:
        body += ["## 关键点", ""]
        body += [f"{i}. {p}" for i, p in enumerate(result["key_points"], 1)]
        body += [""]
    if result["formulas"]:
        body += ["## 公式", ""]
        for f in result["formulas"]:
            suffix = "" if f.get("source_supported", True) else "（AI 补充，需核对）"
            body.append(f"- `{f['formula']}`：{f['meaning']}{suffix}".rstrip("："))
        body += [""]
    if result["examples"]:
        body += ["## 例子", ""]
        body += [f"- {e}" for e in result["examples"]]
        body += [""]
    if result["pitfalls"]:
        body += ["## 易错点", ""]
        body += [f"- {p}" for p in result["pitfalls"]]
        body += [""]
    if result.get("conflict"):
        body += ["## 冲突（保留）", result["conflict"], ""]
    if result["supplement"]:
        body += ["## 补充理解（AI 生成，非原文）", result["supplement"], ""]
    if existing_relations:
        body += ["## 关系", existing_relations, ""]
    if source_lines:
        body += ["## 来源", ""]
        body += [f"- [[{s}]]" for s in source_lines]
        body += [""]
    return "\n".join(body).rstrip() + "\n"


async def call_model(client: httpx.AsyncClient, key: str, user: str) -> tuple[dict, dict]:
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ],
        "temperature": 0,
        "max_tokens": 2200,
        "thinking": {"type": "disabled"},
        "response_format": {"type": "json_object"},
        "stream": False,
    }
    last = None
    for attempt in range(3):
        try:
            r = await client.post(
                API_URL,
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json=payload,
            )
            if r.status_code == 429:
                await asyncio.sleep(2 + attempt * 3)
                last = f"HTTP 429: {r.text[:200]}"
                continue
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
            data = r.json()
            content = data["choices"][0]["message"]["content"]
            return parse_json(content), data.get("usage", {})
        except Exception as e:
            last = str(e)
            if attempt < 2:
                await asyncio.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"model failed after retries: {last}")


def write_report(results: list[dict], meta: dict) -> None:
    out = OUT / "_enrichment_report.json"
    out.write_text(json.dumps({"meta": meta, "results": results}, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Note enrichment report",
        "",
        f"- generated_at: {meta['generated_at']}",
        f"- model: {meta['model']}",
        f"- notes: {meta['notes']}",
        f"- succeeded: {meta['succeeded']}",
        f"- failed: {meta['failed']}",
        f"- input_tokens: {meta['usage']['prompt_tokens']}",
        f"- output_tokens: {meta['usage']['completion_tokens']}",
        "",
        "| note | course | status | flags | source_chars |",
        "|---|---|---|---|---:|",
    ]
    for r in results[:1000]:
        lines.append(
            f"| {r['note_id']} | {r['course']} | {r['status']} | "
            f"{', '.join(r.get('flags') or [])} | {r.get('source_chars', 0)} |"
        )
    (OUT / "_enrichment_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


async def main_async(args: argparse.Namespace) -> None:
    key = (os.environ.get("DEEPSEEK_API_KEY", "") or "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set")

    by_source: dict[str, list[dict]] = {}
    if SECTIONS.exists():
        for line in SECTIONS.read_text(encoding="utf-8").splitlines():
            if line.strip():
                p = json.loads(line)
                by_source.setdefault(str(p.get("source_id") or ""), []).append(p)

    paths = sorted(NOTES.glob("*/*.md"))
    if args.courses:
        allowed = {c.strip() for c in args.courses.split(",") if c.strip()}
        paths = [p for p in paths if p.parent.name in allowed]
    if args.mode == "missing":
        def needs(p: Path) -> bool:
            try:
                fm, body = split_frontmatter(p.read_text(encoding="utf-8"))
                secs = parse_sections(body)
                return not secs.get("定义") or not secs.get("公式") or not secs.get("例子")
            except Exception:
                return True
        paths = [p for p in paths if needs(p)]
    if args.limit:
        paths = paths[: args.limit]

    OUT.mkdir(parents=True, exist_ok=True)
    started = datetime.now(timezone.utc)
    results: list[dict] = []
    usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    sem = asyncio.Semaphore(max(1, args.concurrency))
    lock = asyncio.Lock()

    async with httpx.AsyncClient(timeout=180) as client:
        async def one(path: Path) -> None:
            nonlocal usage
            note_id = path.stem
            course = path.parent.name
            status = "error"
            flags: list[str] = []
            source_chars = 0
            try:
                raw = path.read_text(encoding="utf-8")
                fm, body = split_frontmatter(raw)
                existing = parse_sections(body)
                sources = fm.get("source") or []
                src_text = source_text_for_sources(sources if isinstance(sources, list) else [], by_source)
                source_chars = len(src_text)
                title = str(fm.get("title") or note_id)
                user = build_user_prompt(title, course, existing, src_text)
                async with sem:
                    parsed, u = await call_model(client, key, user)
                async with lock:
                    usage["prompt_tokens"] += int(u.get("prompt_tokens") or 0)
                    usage["completion_tokens"] += int(u.get("completion_tokens") or 0)
                    usage["total_tokens"] += int(u.get("total_tokens") or 0)
                result = normalize_result(parsed, existing, title, src_text, course)
                # Preserve original relations; do not let the model invent graph edges.
                relations = existing.get("关系", "")
                source_lines = [str(s.get("source_id")) for s in sources if isinstance(s, dict) and s.get("source_id")]
                body_out = render_note(fm, result, relations, source_lines)
                fm_out = dict(fm)
                fm_out["schema_version"] = 3
                fm_out["verification"] = "ai_enriched"
                fm_out["status"] = "enriched"
                fm_out["aliases"] = result["aliases"] or fm.get("aliases") or []
                fm_out["enrichment"] = {
                    "version": VERSION,
                    "model": MODEL,
                    "generated_at": datetime.now(timezone.utc).isoformat(),
                    "source_chars": source_chars,
                    "flags": result["flags"],
                    "confidence": round(result["confidence"], 2),
                    "has_supplement": bool(result["supplement"]),
                    "has_conflict": bool(result.get("conflict")),
                    "formula_support": [
                        {"formula": f["formula"], "source_supported": f["source_supported"]}
                        for f in result["formulas"]
                    ],
                }
                fm_text = yaml.safe_dump(fm_out, allow_unicode=True, sort_keys=False).strip()
                out_path = OUT / course / path.name
                out_path.parent.mkdir(parents=True, exist_ok=True)
                out_path.write_text(f"---\n{fm_text}\n---\n\n{body_out}", encoding="utf-8")
                status = "ok"
                flags = result["flags"]
            except Exception as e:
                flags = [f"error:{type(e).__name__}"]
                # Keep a cleaned fallback so a failed API call does not create a gap.
                try:
                    raw = path.read_text(encoding="utf-8")
                    fm, body = split_frontmatter(raw)
                    existing = parse_sections(body)
                    fallback = normalize_result({}, existing, str(fm.get("title") or note_id), "", course)
                    srcs = fm.get("source") or []
                    body_out = render_note(fm, fallback, existing.get("关系", ""), [str(s.get("source_id")) for s in srcs if isinstance(s, dict) and s.get("source_id")])
                    fm_out = dict(fm)
                    fm_out["schema_version"] = 3
                    fm_out["verification"] = "cleaned_fallback"
                    fm_out["status"] = "cleaned_fallback"
                    fm_out["enrichment"] = {"version": VERSION, "model": MODEL, "error": str(e)[:300], "flags": ["fallback"]}
                    fm_text = yaml.safe_dump(fm_out, allow_unicode=True, sort_keys=False).strip()
                    out_path = OUT / course / path.name
                    out_path.parent.mkdir(parents=True, exist_ok=True)
                    out_path.write_text(f"---\n{fm_text}\n---\n\n{body_out}", encoding="utf-8")
                    status = "fallback"
                except Exception:
                    pass
            async with lock:
                results.append({
                    "note_id": note_id,
                    "course": course,
                    "status": status,
                    "flags": flags,
                    "source_chars": source_chars,
                })
                if len(results) % 10 == 0:
                    print(f"{len(results)}/{len(paths)} {note_id} {status} {flags}", flush=True)

        tasks = [asyncio.create_task(one(p)) for p in paths]
        await asyncio.gather(*tasks)

    results.sort(key=lambda r: (r["course"], r["note_id"]))
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "started_at": started.isoformat(),
        "model": MODEL,
        "version": VERSION,
        "notes": len(results),
        "succeeded": sum(1 for r in results if r["status"] == "ok"),
        "failed": sum(1 for r in results if r["status"] != "ok"),
        "usage": usage,
        "output": str(OUT),
        "elapsed_seconds": round((datetime.now(timezone.utc) - started).total_seconds(), 1),
    }
    write_report(results, meta)
    if args.mode == "all" and len(results) == len(paths) and not any(r["status"] != "ok" for r in results):
        (OUT / "_complete.json").write_text(
            json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    print(json.dumps(meta, ensure_ascii=False, indent=2), flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--courses", default="")
    ap.add_argument("--concurrency", type=int, default=4)
    ap.add_argument("--mode", choices=["all", "missing"], default="missing")
    args = ap.parse_args()
    asyncio.run(main_async(args))


if __name__ == "__main__":
    main()
