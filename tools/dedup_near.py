# -*- coding: utf-8 -*-
"""Step 4 — near-duplicate detection and canonical selection.

Input : data/clean/manifest.csv + data/clean/v1/
Output: data/registry/near_duplicates.csv
        data/registry/canonical.csv
        data/clean/duplicate_report.md
        manifest.csv updated with cluster_id / relation / canonical / duplicate_of / similarity

Method:
  - 5-gram shingles over normalized text (CJK/alnum only)
  - 64-bit SimHash; Hamming <=8 is a candidate
  - exact Jaccard on shingle sets confirms duplicate (>=0.80) vs candidate (0.60-0.80)
  - cross-format (PDF vs MD) same-course pairs: title / first-300-char similarity -> "parallel"
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"D:\CyberMe\repo")
CLEAN = REPO / "data" / "clean" / "v1"
MANIFEST = REPO / "data" / "clean" / "manifest.csv"
REG = REPO / "data" / "registry"
REG.mkdir(parents=True, exist_ok=True)

PAGE_RE = re.compile(r"<!-- page: \d+ -->")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n\n?", re.S)
KEEP = re.compile(r"[^\u4e00-\u9fffA-Za-z0-9]+")

SHINGLE = 5
HEAD_CHARS = 300
QA_RE = re.compile(r"解析|答案|解答|参考答案|答案版")


def norm_text(body: str) -> str:
    body = PAGE_RE.sub("", body)
    body = KEEP.sub("", body)
    return body.lower()


def h64(s: str) -> int:
    return int.from_bytes(hashlib.blake2b(s.encode("utf-8"), digest_size=8).digest(), "big")


def shingle_hashes(text: str) -> set[int]:
    if len(text) < SHINGLE:
        return {h64(text)} if text else set()
    return {h64(text[i:i + SHINGLE]) for i in range(len(text) - SHINGLE + 1)}


def simhash(hashes: set[int]) -> int:
    if not hashes:
        return 0
    v = [0] * 64
    for h in hashes:
        for i in range(64):
            v[i] += 1 if (h >> i) & 1 else -1
    out = 0
    for i in range(64):
        if v[i] > 0:
            out |= 1 << i
    return out


def jaccard(a: set[int], b: set[int]) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a) + len(b) - inter
    return inter / union if union else 0.0


def title_sim(a: str, b: str) -> float:
    def clean(s: str) -> str:
        s = Path(s).stem
        s = re.sub(r"^\d+[_\-.、\s]*", "", s)
        s = re.sub(r"第[一二三四五六七八九十0-9]+[章讲节]", "", s)
        s = re.sub(r"(提取版|课件|笔记|复习|答案|试卷|习题|解析|版)", "", s)
        s = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]+", "", s).lower()
        return s
    ca, cb = clean(a), clean(b)
    if not ca or not cb:
        return 0.0
    # cheap character-level Dice
    common = sum((Counter(ca) & Counter(cb)).values())
    return 2 * common / (len(ca) + len(cb))


class UF:
    def __init__(self, n: int):
        self.p = list(range(n))

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[rb] = ra


def main() -> None:
    rows = list(csv.DictReader(MANIFEST.open(encoding="utf-8-sig")))
    print(f"loading {len(rows)} documents", flush=True)

    docs = []
    for r in rows:
        p = REPO / r["clean_path"]
        text = p.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        body = text[m.end():] if m else text
        norm = norm_text(body)
        hs = shingle_hashes(norm) if len(norm) >= 50 else set()
        head = norm[:HEAD_CHARS]
        head3 = {head[k:k + 3] for k in range(max(1, len(head) - 2))} if head else set()
        docs.append({
            "row": r,
            "source_id": r["source_id"],
            "course": r["course"],
            "doc_type": r["doc_type"],
            "ext": Path(r["rel"]).suffix.lower(),
            "rel": r["rel"],
            "norm": norm,
            "head": head,
            "head3": head3,
            "hashes": hs,
            "simhash": simhash(hs),
            "chars": int(float(r.get("chars_norm") or 0)),
            "pages": int(float(r.get("pages") or 0)),
        })

    n = len(docs)
    dup_edges = []
    cand_edges = []
    par_edges = []
    qa_pairs = []

    for i in range(n):
        a = docs[i]
        for j in range(i + 1, n):
            b = docs[j]
            # cross-format parallel: same course, one PDF one MD
            if a["course"] == b["course"] and a["ext"] != b["ext"]:
                ts = title_sim(a["rel"], b["rel"])
                hd = jaccard(a["head3"], b["head3"]) if a["head3"] and b["head3"] else 0.0
                if ts >= 0.75 or hd >= 0.55:
                    par_edges.append((i, j, round(max(ts, hd), 4), round(ts, 4), round(hd, 4)))
                continue

            if a["ext"] != b["ext"] or not a["hashes"] or not b["hashes"]:
                continue
            dist = (a["simhash"] ^ b["simhash"]).bit_count()
            if dist <= 8:
                jac = jaccard(a["hashes"], b["hashes"])
                if jac < 0.60:
                    continue
                # question vs answer/analysis are complementary, not duplicates
                if bool(QA_RE.search(a["rel"])) != bool(QA_RE.search(b["rel"])):
                    qa_pairs.append((i, j, round(jac, 4)))
                    continue
                # exams share templates; require much higher similarity
                if "exam" in (a["doc_type"], b["doc_type"]):
                    threshold = 0.95
                elif "exercise" in (a["doc_type"], b["doc_type"]):
                    threshold = 0.90
                else:
                    threshold = 0.80
                if jac >= threshold and dist <= 6:
                    dup_edges.append((i, j, dist, round(jac, 4)))
                else:
                    cand_edges.append((i, j, dist, round(jac, 4)))

    # duplicate clusters
    uf = UF(n)
    for i, j, _, _ in dup_edges:
        uf.union(i, j)
    dup_groups = defaultdict(list)
    for i in range(n):
        dup_groups[uf.find(i)].append(i)
    dup_groups = {k: v for k, v in dup_groups.items() if len(v) > 1}

    # canonical per duplicate cluster
    cluster_of = {}
    canonical_of = {}
    relation = {}
    duplicate_of = {}
    similarity = {}
    cluster_idx = 0
    for _, members in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
        cluster_idx += 1
        cid = f"DUP-{cluster_idx:03d}"
        def score(k):
            d = docs[k]
            return (1 if d["pages"] > 0 else 0, d["chars"], 1 if d["row"].get("doc_type") == "notes" else 0)
        canon = max(members, key=score)
        canonical_of[canon] = True
        for k in members:
            cluster_of[k] = cid
            relation[k] = "duplicate"
            if k != canon:
                duplicate_of[k] = docs[canon]["source_id"]
                canonical_of[k] = False
            else:
                canonical_of[k] = True
                duplicate_of[k] = ""
        # similarity: max jaccard inside cluster
        best = max((e[3] for e in dup_edges if e[0] in members and e[1] in members), default=1.0)
        for k in members:
            similarity[k] = best

    # parallel pairs: one PDF <-> one MD, same course, same chapter/title.
    # Do NOT use transitive closure: that merges different chapters into one giant group.
    parallel_with = {i: "" for i in range(n)}
    par_pairs = []
    used_par = set()
    for i, j, score, ts, hd in sorted(par_edges, key=lambda x: -x[2]):
        if i in cluster_of or j in cluster_of:
            continue
        if i in used_par or j in used_par:
            continue
        # require a real title match; head similarity alone is too weak
        if ts < 0.80 and not (ts >= 0.55 and hd >= 0.80):
            continue
        used_par.add(i)
        used_par.add(j)
        pid = f"PAR-{len(par_pairs) + 1:03d}"
        cluster_of[i] = cluster_of[j] = pid
        relation[i] = relation[j] = "parallel"
        canonical_of[i] = canonical_of[j] = True
        parallel_with[i] = docs[j]["source_id"]
        parallel_with[j] = docs[i]["source_id"]
        similarity[i] = similarity[j] = round(score, 4)
        par_pairs.append((i, j, pid, ts, hd))

    # fill singletons
    for i in range(n):
        cluster_of.setdefault(i, "")
        relation.setdefault(i, "none")
        canonical_of.setdefault(i, True)
        duplicate_of.setdefault(i, "")
        parallel_with.setdefault(i, "")
        similarity.setdefault(i, 1.0)

    # write near_duplicates.csv (all edges)
    with (REG / "near_duplicates.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["relation", "course", "source_a", "source_b", "rel_a", "rel_b", "hamming", "jaccard", "title_sim", "head_jaccard"])
        for i, j, dist, jac in dup_edges:
            w.writerow(["duplicate", docs[i]["course"], docs[i]["source_id"], docs[j]["source_id"],
                        docs[i]["rel"], docs[j]["rel"], dist, jac, "", ""])
        for i, j, dist, jac in cand_edges:
            w.writerow(["candidate", docs[i]["course"], docs[i]["source_id"], docs[j]["source_id"],
                        docs[i]["rel"], docs[j]["rel"], dist, jac, "", ""])
        for i, j, score, ts, hd in par_edges:
            w.writerow(["parallel", docs[i]["course"], docs[i]["source_id"], docs[j]["source_id"],
                        docs[i]["rel"], docs[j]["rel"], "", "", ts, hd])

    # update manifest
    fields = list(rows[0].keys())
    for extra in ("cluster_id", "relation", "canonical", "duplicate_of", "parallel_with", "similarity"):
        if extra not in fields:
            fields.append(extra)
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for i, r in enumerate(rows):
            r.update({
                "cluster_id": cluster_of[i],
                "relation": relation[i],
                "canonical": "true" if canonical_of[i] else "false",
                "duplicate_of": duplicate_of[i],
                "parallel_with": parallel_with[i],
                "similarity": similarity[i],
            })
            w.writerow(r)

    # canonical.csv
    with (REG / "canonical.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "course", "rel", "cluster_id", "relation", "canonical",
                    "duplicate_of", "parallel_with", "similarity"])
        for i, d in enumerate(docs):
            w.writerow([d["source_id"], d["course"], d["rel"], cluster_of[i], relation[i],
                        "true" if canonical_of[i] else "false", duplicate_of[i],
                        parallel_with[i], similarity[i]])

    # report
    dup_clusters = [v for v in dup_groups.values()]
    lines = [
        "# Step 4 — Near-duplicate & canonical report",
        "",
        f"- documents: {n}",
        f"- duplicate clusters: {len(dup_clusters)}",
        f"- files in duplicate clusters: {sum(len(v) for v in dup_clusters)}",
        f"- parallel pairs: {len(par_pairs)}",
        f"- files in parallel pairs: {2 * len(par_pairs)}",
        f"- question/answer pairs kept separate: {len(qa_pairs)}",
        f"- candidate pairs (not merged): {len(cand_edges)}",
        f"- canonical files: {sum(1 for i in range(n) if canonical_of[i])}",
        "",
        "## Duplicate clusters",
        "",
        "| cluster | canonical | members | max jaccard |",
        "|---|---|---:|---:|",
    ]
    for key, members in sorted(dup_groups.items(), key=lambda x: -len(x[1])):
        canon = max(members, key=lambda k: (1 if docs[k]["pages"] > 0 else 0, docs[k]["chars"]))
        lines.append(f"| {cluster_of[canon]} | {docs[canon]['rel']} | {len(members)} | {similarity[canon]} |")
    lines += ["", "## Parallel pairs (PDF <-> MD, same chapter)", "",
              "| pair | PDF/one side | MD/other side | title sim |", "|---|---|---|---:|"]
    for i, j, pid, ts, hd in par_pairs:
        lines.append(f"| {pid} | {docs[i]['rel']} | {docs[j]['rel']} | {ts} |")
    if cand_edges:
        lines += ["", "## Candidate pairs (review, not merged)", "", "| course | a | b | hamming | jaccard |", "|---|---|---|---:|---:|"]
        for i, j, dist, jac in sorted(cand_edges, key=lambda x: -x[3])[:20]:
            lines.append(f"| {docs[i]['course']} | {docs[i]['rel']} | {docs[j]['rel']} | {dist} | {jac} |")
    (REPO / "data" / "clean" / "duplicate_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "documents": n,
        "duplicate_clusters": len(dup_clusters),
        "duplicate_files": sum(len(v) for v in dup_clusters),
        "parallel_pairs": len(par_pairs),
        "qa_pairs": len(qa_pairs),
        "candidate_pairs": len(cand_edges),
        "canonical": sum(1 for i in range(n) if canonical_of[i]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
