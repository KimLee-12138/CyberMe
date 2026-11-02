# -*- coding: utf-8 -*-
"""Build the deterministic knowledge graph: Course -> Section -> Topic -> Source.

Outputs:
  data/kg/kg.json
  data/kg/kg_report.md
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "data"
OUT = DATA / "kg"
OUT.mkdir(parents=True, exist_ok=True)

COURSE_NAMES = {
    "DB": "数据库",
    "ALGO": "算法",
    "DS": "数据结构",
    "CO": "计算机组成原理",
    "SE": "软件工程",
    "EDA": "EDA",
    "ASM": "汇编",
    "JAVA": "Java",
    "PY": "Python",
    "CPP": "C++",
    "PROB": "概率论",
    "CALCULUS": "微积分",
    "LINALG": "线性代数",
    "DISCRETE": "离散数学",
    "PHYSICS": "大学物理",
    "MAYUAN": "马原",
    "MAOGAI": "毛概",
    "XIGAI": "习概",
    "HISTORY": "近代史",
    "SIXIANG": "思想与政治",
    "JUNLI": "军理",
    "RLMATH": "强化学习数学",
    "INFO": "信息导论",
    "ZHENGCE": "政策与形势",
}

# Curated course-level prerequisites.
# Direction is prerequisite -> course (edge type "prerequisite_of").
# Foundational courses (calculus, linear algebra, discrete math, programming,
# history, military theory) intentionally have no incoming prerequisite.
COURSE_PREREQUISITES = {
    "DS": ["CPP", "PY"],
    "ALGO": ["DS", "DISCRETE"],
    "CO": ["DS", "EDA"],
    "DB": ["DS"],
    "SE": ["DS", "DB"],
    "PROB": ["CALCULUS"],
    "PHYSICS": ["CALCULUS"],
    "RLMATH": ["CALCULUS", "PROB", "LINALG"],
    "ASM": ["CO"],
    "MAOGAI": ["MAYUAN"],
    "XIGAI": ["MAOGAI"],
    "SIXIANG": ["MAYUAN"],
}


def norm_title(t: str) -> str:
    t = re.sub(r"[（(].*?[)）]", "", str(t))
    t = re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]+", "", t)
    return t.lower()


def load_topics() -> list[dict]:
    rows = []
    for p in sorted((DATA / "topics").glob("*.jsonl")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows


def load_sections() -> dict[str, dict]:
    sections = {}
    for line in (DATA / "sections" / "sections.jsonl").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        p = json.loads(line)
        sid = p.get("section_id")
        if not sid:
            continue
        if sid not in sections:
            sections[sid] = {
                "section_id": sid,
                "course": p.get("course", ""),
                "source_id": p.get("source_id", ""),
                "heading_path": p.get("heading_path") or [],
                "chars": 0,
                "page_start": 10**9,
                "page_end": 0,
                "parts": 0,
            }
        s = sections[sid]
        s["chars"] += int(p.get("chars") or 0)
        s["parts"] += 1
        if p.get("page_start"):
            s["page_start"] = min(s["page_start"], int(p["page_start"]))
            s["page_end"] = max(s["page_end"], int(p.get("page_end") or p["page_start"]))
    for s in sections.values():
        if s["page_start"] == 10**9:
            s["page_start"] = 0
    return sections


def load_sources() -> dict[str, dict]:
    rows = {}
    for r in csv.DictReader((DATA / "clean" / "manifest.csv").open(encoding="utf-8-sig")):
        rows[r["source_id"]] = r
    return rows


def load_notes() -> dict[str, dict]:
    out = {}
    path = DATA / "notes" / "_index.jsonl"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                out[r.get("topic_id", "")] = r
    return out


def main() -> None:
    topics = load_topics()
    sections = load_sections()
    sources = load_sources()
    notes = load_notes()

    nodes = {}
    edges = []
    edge_seen = set()

    def add_node(nid, ntype, label, props=None, document_id=None):
        if nid in nodes:
            return
        nodes[nid] = {
            "id": nid,
            "node_type": ntype,
            "label": label,
            "document_id": document_id,
            "properties": props or {},
        }

    def add_edge(source, target, etype, origin="derived", confidence=None):
        if source not in nodes or target not in nodes or source == target:
            return
        eid = f"{source}|{target}|{etype}"
        if eid in edge_seen:
            return
        edge_seen.add(eid)
        edges.append({
            "id": eid,
            "source": source,
            "target": target,
            "edge_type": etype,
            "origin": origin,
            "confidence": confidence,
        })

    # referenced source ids
    referenced_sources = set()
    for t in topics:
        for s in t["topic"].get("sources") or []:
            if s.get("source_id"):
                referenced_sources.add(s["source_id"])
    for s in sections.values():
        if s.get("source_id"):
            referenced_sources.add(s["source_id"])

    # course nodes: include the full curriculum map, even courses with no
    # distilled content yet (PY / LINALG / INFO / ZHENGCE), so prerequisite
    # edges are complete.
    course_codes = sorted(set(COURSE_NAMES.keys()) |
                          {t.get("course") for t in topics if t.get("course")} |
                          {s.get("course") for s in sections.values() if s.get("course")})
    for code in course_codes:
        add_node(f"course:{code}", "course", COURSE_NAMES.get(code, code), {
            "code": code,
            "name": COURSE_NAMES.get(code, code),
        })

    # course-level prerequisite edges (curated)
    for target, prereqs in COURSE_PREREQUISITES.items():
        if target not in course_codes:
            continue
        for p in prereqs:
            if p not in course_codes:
                continue
            add_edge(f"course:{p}", f"course:{target}", "prerequisite_of", origin="curated")
            tnode = nodes[f"course:{target}"]
            pnode = nodes[f"course:{p}"]
            tnode["properties"].setdefault("prerequisites", [])
            pnode["properties"].setdefault("unlocks", [])
            if p not in tnode["properties"]["prerequisites"]:
                tnode["properties"]["prerequisites"].append(p)
            if target not in pnode["properties"]["unlocks"]:
                pnode["properties"]["unlocks"].append(target)

    # section nodes
    for sid, s in sections.items():
        label = (s["heading_path"][-1] if s["heading_path"] else sid)
        add_node(f"section:{sid}", "section", label, {
            "section_id": sid,
            "course": s["course"],
            "source_id": s["source_id"],
            "heading_path": s["heading_path"],
            "page_start": s["page_start"],
            "page_end": s["page_end"],
            "chars": s["chars"],
        }, document_id=None)

    # source nodes
    for source_id in sorted(referenced_sources):
        r = sources.get(source_id, {})
        rel = r.get("rel", "")
        label = Path(rel).stem if rel else source_id
        add_node(f"source:{source_id}", "source", label, {
            "source_id": source_id,
            "course": r.get("course", ""),
            "rel": rel,
            "doc_type": r.get("doc_type", ""),
            "pages": r.get("pages", 0),
            "chars": r.get("chars_norm", 0),
            "quality_status": r.get("quality_status", ""),
            "sha256": r.get("sha256", ""),
        }, document_id=None)

    # topic nodes
    topic_by_course_title = defaultdict(list)
    for t in topics:
        topic = t.get("topic") or {}
        tid = t.get("topic_id", "")
        title = topic.get("title") or tid
        note = notes.get(tid, {})
        sources_list = []
        for s in topic.get("sources") or []:
            sid = s.get("source_id")
            if sid and sid not in [x["source_id"] for x in sources_list]:
                sources_list.append({
                    "source_id": sid,
                    "page_start": s.get("page_start", 0),
                    "page_end": s.get("page_end", 0),
                    "section_id": s.get("section_id", ""),
                })
        add_node(f"topic:{tid}", "topic", title, {
            "topic_id": tid,
            "section_id": t.get("section_id", ""),
            "course": t.get("course", ""),
            "unit_count": t.get("unit_count", 0),
            "key_points": len(topic.get("key_points") or []),
            "formulas": len(topic.get("formulas") or []),
            "conflicts": len(topic.get("conflicts") or []),
            "confidence": topic.get("confidence", 0),
            "sources": sources_list,
            "note_id": note.get("note_id", ""),
            "note_path": note.get("path", ""),
        }, document_id=None)
        topic_by_course_title[(t.get("course", ""), norm_title(title))].append(tid)

    # derived edges
    for t in topics:
        tid = t.get("topic_id", "")
        course = t.get("course", "")
        sid = t.get("section_id", "")
        tn = f"topic:{tid}"
        if course:
            add_edge(tn, f"course:{course}", "belongs_to")
        if sid and f"section:{sid}" in nodes:
            add_edge(tn, f"section:{sid}", "part_of")
        for s in t.get("topic", {}).get("sources") or []:
            src = s.get("source_id")
            if src and f"source:{src}" in nodes:
                add_edge(tn, f"source:{src}", "derived_from")

    for sid, s in sections.items():
        if s["course"]:
            add_edge(f"section:{sid}", f"course:{s['course']}", "part_of")
        if s["source_id"] and f"source:{s['source_id']}" in nodes:
            add_edge(f"section:{sid}", f"source:{s['source_id']}", "derived_from")

    # candidate edges from topic relations
    candidate = []
    cand_seen = set()
    unmatched = 0
    for t in topics:
        tid = t.get("topic_id", "")
        course = t.get("course", "")
        for rel in (t.get("topic") or {}).get("relations") or []:
            if not isinstance(rel, dict):
                continue
            rtype = (rel.get("type") or "related_to").lower()
            target = rel.get("target") or ""
            if not target:
                continue
            key = (course, norm_title(target))
            candidates = topic_by_course_title.get(key, [])
            if not candidates:
                # fuzzy fallback within course
                nt = norm_title(target)
                for (c, nt2), tids in topic_by_course_title.items():
                    if c != course:
                        continue
                    if nt and (nt in nt2 or nt2 in nt):
                        candidates = tids
                        break
            if not candidates:
                unmatched += 1
                continue
            target_tid = candidates[0]
            if target_tid == tid:
                continue
            eid = f"topic:{tid}|topic:{target_tid}|{rtype}"
            if eid in cand_seen:
                continue
            cand_seen.add(eid)
            candidate.append({
                "id": eid,
                "source": f"topic:{tid}",
                "target": f"topic:{target_tid}",
                "edge_type": rtype,
                "origin": "ai_candidate",
                "confirmed": False,
            })

    # stats
    topic_count_by_course = Counter(t.get("course") for t in topics)
    section_count_by_course = Counter(s.get("course") for s in sections.values())
    source_count_by_course = Counter()
    for sid in referenced_sources:
        source_count_by_course[sources.get(sid, {}).get("course", "")] += 1
    for code in course_codes:
        node = nodes[f"course:{code}"]
        node["properties"]["topic_count"] = topic_count_by_course.get(code, 0)
        node["properties"]["section_count"] = section_count_by_course.get(code, 0)
        node["properties"]["source_count"] = source_count_by_course.get(code, 0)
        node["properties"]["has_content"] = topic_count_by_course.get(code, 0) > 0

    # validation
    ids = list(nodes)
    dup_ids = [x for x, c in Counter(ids).items() if c > 1]
    missing_targets = [e for e in edges if e["source"] not in nodes or e["target"] not in nodes]
    course_prereq_edges = [e for e in edges if e["edge_type"] == "prerequisite_of"]
    topic_nodes = {n for n in nodes if n.startswith("topic:")}
    topic_with_edges = {e["source"] for e in edges if e["source"] in topic_nodes} | {e["target"] for e in edges if e["target"] in topic_nodes}
    orphan_topics = topic_nodes - topic_with_edges
    section_nodes = {n for n in nodes if n.startswith("section:")}
    section_with_edges = {e["source"] for e in edges if e["source"] in section_nodes} | {e["target"] for e in edges if e["target"] in section_nodes}
    orphan_sections = section_nodes - section_with_edges

    graph = {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "course_names": COURSE_NAMES,
        "course_prerequisites": COURSE_PREREQUISITES,
        "stats": {
            "nodes": len(nodes),
            "edges": len(edges),
            "candidate_edges": len(candidate),
            "courses": len(course_codes),
            "sections": len(sections),
            "topics": len(topics),
            "sources": len(referenced_sources),
            "orphan_topics": len(orphan_topics),
            "orphan_sections": len(orphan_sections),
            "course_prerequisite_edges": len(course_prereq_edges),
            "candidate_unmatched": unmatched,
        },
        "nodes": list(nodes.values()),
        "edges": edges,
        "candidate_edges": candidate,
    }
    (OUT / "kg.json").write_text(json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8")

    # report
    lines = [
        "# Knowledge Graph — build report",
        "",
        f"- generated: {graph['generated_at']}",
        f"- nodes: {len(nodes)}",
        f"- edges: {len(edges)}",
        f"- candidate edges: {len(candidate)}",
        f"- courses: {len(course_codes)}",
        f"- sections: {len(sections)}",
        f"- topics: {len(topics)}",
        f"- sources: {len(referenced_sources)}",
        f"- orphan topics: {len(orphan_topics)}",
        f"- orphan sections: {len(orphan_sections)}",
        f"- course prerequisite edges: {len(course_prereq_edges)}",
        f"- duplicate node ids: {len(dup_ids)}",
        f"- edges with missing endpoints: {len(missing_targets)}",
        f"- candidate unmatched: {unmatched}",
        "",
        "## By course",
        "",
        "| course | name | topics | sections | sources |",
        "|---|---|---:|---:|---:|",
    ]
    for code in course_codes:
        lines.append(f"| {code} | {COURSE_NAMES.get(code, code)} | {topic_count_by_course.get(code,0)} | "
                     f"{section_count_by_course.get(code,0)} | {source_count_by_course.get(code,0)} |")
    lines += ["", "## Course prerequisites", "", "| course | prerequisites |", "|---|---|"]
    for code in course_codes:
        prereqs = nodes[f"course:{code}"]["properties"].get("prerequisites", [])
        lines.append(f"| {code} | {', '.join(prereqs) if prereqs else '—'} |")
    (OUT / "kg_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(graph["stats"], ensure_ascii=False, indent=2))
    print("duplicate ids:", len(dup_ids), "missing endpoints:", len(missing_targets))


if __name__ == "__main__":
    main()
