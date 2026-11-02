# -*- coding: utf-8 -*-
"""CLI: query the RAG index and print evidence."""
import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from app.rag.retriever import RagIndex  # noqa: E402


def fmt_pages(pages) -> str:
    if not pages:
        return ""
    return ", ".join(f"p.{a}-{b}" if a != b else f"p.{a}" for a, b in pages)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--course", default=None)
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    index = RagIndex.load(rebuild=args.rebuild)
    if args.stats:
        print(json.dumps(index.stats(), ensure_ascii=False, indent=2))
        return
    if not args.query:
        ap.error("query is required unless --stats")

    results = index.search(args.query, top_k=args.top, course=args.course)
    if args.json:
        print(json.dumps({
            "query": args.query,
            "course": args.course,
            "stats": index.stats(),
            "results": results,
        }, ensure_ascii=False, indent=2))
        return

    print(f"query: {args.query}")
    print(f"chunks: {index.stats()['chunks']}  (notes={index.stats()['notes']}, sources={index.stats()['sources']})")
    if not results:
        print("no results")
        return
    for r in results:
        src = "; ".join(r["source_ids"])
        pages = fmt_pages(r["pages"])
        loc = " ".join(x for x in [src, pages] if x)
        print(f"\n[{r['rank']}] score={r['score']}  {r['kind']}  {r['course']}  {r['doc_id']}")
        print(f"    {r['title']}  § {r['heading']}")
        if loc:
            print(f"    来源: {loc}")
        print(f"    {r['snippet'][:220].replace(chr(10), ' ')}")


if __name__ == "__main__":
    main()
