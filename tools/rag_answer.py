# -*- coding: utf-8 -*-
"""CLI: RAG answer with citations and refusal."""
import argparse
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from app.rag.answer import ask  # noqa: E402
from app.rag.retriever import RagIndex  # noqa: E402


def fmt_pages(pages) -> str:
    if not pages:
        return ""
    return ", ".join(f"p.{a}-{b}" if a != b else f"p.{a}" for a, b in pages)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--course", default=None)
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--evidence", action="store_true", default=True)
    ap.add_argument("--no-evidence", action="store_false", dest="evidence")
    args = ap.parse_args()

    key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set in the environment")

    index = RagIndex.load()
    result = ask(index, args.query, course=args.course, top_k=args.top)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"Q: {args.query}")
    print(f"course={args.course or '-'}  coverage={result.get('coverage')}  refused={result['refused']}")
    print("\nA:")
    print(result["answer"])
    if result["citations"]:
        print("\n引用:")
        for c in result["citations"]:
            pages = fmt_pages(c["pages"])
            print(f"  [{c['evidence_id']}] {c['doc_id']}  {c['title']} §{c['heading']}  {pages}")
    if args.evidence:
        print("\n证据:")
        for e in result["evidence"]:
            pages = fmt_pages(e["pages"])
            print(f"  [{e['evidence_id']}] score={e['score']} {e['kind']} {e['doc_id']} §{e['heading']} {pages}")
            print(f"      {e['snippet'][:160].replace(chr(10), ' ')}")
    if result.get("usage"):
        print(f"\nusage: {result['usage']}  latency={result.get('latency_ms')}ms")


if __name__ == "__main__":
    main()
