# -*- coding: utf-8 -*-
"""Stage 2 — knowledge graph API over data/kg/kg.json."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query

from app.auth.dependencies import current_user

router = APIRouter(
    prefix="/api/v1/kg",
    tags=["knowledge-graph"],
    dependencies=[Depends(current_user)],
)

KG_PATH = Path(__file__).resolve().parents[4] / "data" / "kg" / "kg.json"
_kg: dict | None = None
_nodes: dict[str, dict] = {}


def get_kg() -> dict:
    global _kg, _nodes
    if _kg is None:
        if not KG_PATH.exists():
            raise HTTPException(status_code=503, detail="kg.json not found; run tools/build_kg.py")
        _kg = json.loads(KG_PATH.read_text(encoding="utf-8"))
        _nodes = {n["id"]: n for n in _kg.get("nodes", [])}
    return _kg


def _edge_ok(e: dict, ids: set[str]) -> bool:
    return e.get("source") in ids and e.get("target") in ids


@router.get("/graph")
def kg_graph(
    course: str | None = Query(default=None, max_length=20),
    node_type: str | None = Query(default=None, max_length=20),
    include_candidates: bool = False,
    limit: int = Query(default=500, ge=10, le=2000),
):
    kg = get_kg()
    nodes = kg.get("nodes", [])
    edges = kg.get("edges", [])

    if not course:
        # course-level overview: 24 course nodes + prerequisite edges
        ids = {n["id"] for n in nodes if n.get("node_type") == "course"}
        out_nodes = [n for n in nodes if n["id"] in ids]
        out_edges = [e for e in edges if _edge_ok(e, ids)]
    else:
        code = course.upper()
        course_id = f"course:{code}"
        if course_id not in _nodes:
            raise HTTPException(status_code=404, detail=f"course not found: {code}")

        ids = {course_id}
        # one-hop course prerequisites / unlocks on both directions
        for e in edges:
            if e.get("edge_type") != "prerequisite_of":
                continue
            if e.get("source") == course_id or e.get("target") == course_id:
                ids.add(e["source"])
                ids.add(e["target"])

        # sections / topics of this course
        for n in nodes:
            if n.get("node_type") == "section" and n.get("properties", {}).get("course") == code:
                ids.add(n["id"])
            elif n.get("node_type") == "topic" and n.get("properties", {}).get("course") == code:
                ids.add(n["id"])

        # sources referenced by these topics / sections
        for n in nodes:
            if n["id"] not in ids:
                continue
            if n.get("node_type") == "topic":
                for s in n.get("properties", {}).get("sources") or []:
                    sid = s.get("source_id")
                    if sid and f"source:{sid}" in _nodes:
                        ids.add(f"source:{sid}")
            elif n.get("node_type") == "section":
                sid = n.get("properties", {}).get("source_id")
                if sid and f"source:{sid}" in _nodes:
                    ids.add(f"source:{sid}")

        out_nodes = [n for n in nodes if n["id"] in ids]
        out_edges = [e for e in edges if _edge_ok(e, ids)]

    if node_type:
        out_nodes = [n for n in out_nodes if n.get("node_type") == node_type]
        keep = {n["id"] for n in out_nodes}
        out_edges = [e for e in out_edges if _edge_ok(e, keep)]

    out_nodes = out_nodes[:limit]

    candidate = []
    if include_candidates:
        keep = {n["id"] for n in out_nodes}
        candidate = [e for e in kg.get("candidate_edges", []) if _edge_ok(e, keep)][:limit]

    return {
        "nodes": out_nodes,
        "edges": out_edges[:limit],
        "candidate_edges": candidate,
        "course": course.upper() if course else None,
        "course_names": kg.get("course_names", {}),
        "course_prerequisites": kg.get("course_prerequisites", {}),
        "stats": {
            "nodes": len(out_nodes),
            "edges": len(out_edges),
            "candidate_edges": len(candidate),
            "total_nodes": len(nodes),
            "total_edges": len(edges),
        },
    }


@router.get("/validate")
def kg_validate():
    """Structural validation for the knowledge graph."""
    kg = get_kg()
    nodes = kg.get("nodes", [])
    edges = kg.get("edges", [])
    candidates = kg.get("candidate_edges", [])
    ids = {n["id"] for n in nodes}

    degree = Counter()
    for e in edges:
        degree[e.get("source")] += 1
        degree[e.get("target")] += 1

    dangling = [e for e in edges if e.get("source") not in ids or e.get("target") not in ids]
    self_loops = [e for e in edges if e.get("source") == e.get("target")]
    dangling_candidates = [e for e in candidates if e.get("source") not in ids or e.get("target") not in ids]

    orphan_nodes = [n for n in nodes if degree.get(n["id"], 0) == 0]
    orphan_topics = [n["id"] for n in orphan_nodes if n.get("node_type") == "topic"]
    orphan_sections = [n["id"] for n in orphan_nodes if n.get("node_type") == "section"]
    orphan_courses_without_content = [
        n["id"] for n in orphan_nodes
        if n.get("node_type") == "course" and not n.get("properties", {}).get("has_content")
    ]

    label_groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for n in nodes:
        label_groups[(n.get("node_type", ""), n.get("label", ""))].append(n["id"])
    duplicate_groups = [
        {"node_type": k[0], "label": k[1], "count": len(v), "ids": v[:8]}
        for k, v in label_groups.items() if len(v) > 1
    ]
    duplicate_groups.sort(key=lambda x: x["count"], reverse=True)

    missing_note_path = [
        n["id"] for n in nodes
        if n.get("node_type") == "topic" and not n.get("properties", {}).get("note_path")
    ]
    missing_pages = []
    for n in nodes:
        if n.get("node_type") != "topic":
            continue
        sources = n.get("properties", {}).get("sources") or []
        if not sources or all(not s.get("page_start") and not s.get("page_end") for s in sources):
            missing_pages.append(n["id"])

    # course prerequisite cycles
    adj: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        if e.get("edge_type") == "prerequisite_of":
            adj[e["source"]].append(e["target"])
    color: dict[str, int] = {}
    cycles: list[list[str]] = []

    def dfs(u: str, stack: list[str]) -> None:
        color[u] = 1
        stack.append(u)
        for v in adj.get(u, []):
            if color.get(v, 0) == 0:
                dfs(v, stack)
            elif color.get(v) == 1:
                i = stack.index(v)
                cycles.append(stack[i:] + [v])
        stack.pop()
        color[u] = 2

    for n in nodes:
        if n.get("node_type") == "course" and color.get(n["id"], 0) == 0:
            dfs(n["id"], [])

    ok = not dangling and not self_loops and not dangling_candidates and not cycles

    return {
        "ok": ok,
        "counts": {
            "nodes": len(nodes),
            "edges": len(edges),
            "candidate_edges": len(candidates),
            "course_prerequisite_edges": sum(1 for e in edges if e.get("edge_type") == "prerequisite_of"),
            "orphan_nodes": len(orphan_nodes),
            "orphan_topics": len(orphan_topics),
            "orphan_sections": len(orphan_sections),
            "orphan_courses_without_content": len(orphan_courses_without_content),
            "duplicate_label_groups": len(duplicate_groups),
            "missing_note_path": len(missing_note_path),
            "missing_pages": len(missing_pages),
            "dangling_edges": len(dangling),
            "self_loops": len(self_loops),
            "dangling_candidates": len(dangling_candidates),
            "cycles": len(cycles),
        },
        "orphan_nodes": orphan_nodes[:50],
        "orphan_topics": orphan_topics[:50],
        "orphan_sections": orphan_sections[:50],
        "orphan_courses_without_content": orphan_courses_without_content[:50],
        "duplicate_label_groups": duplicate_groups[:30],
        "missing_note_path": missing_note_path[:50],
        "missing_pages": missing_pages[:50],
        "dangling_edges": dangling[:20],
        "self_loops": self_loops[:20],
        "dangling_candidates": dangling_candidates[:20],
        "course_prerequisite_cycles": cycles[:20],
    }


@router.get("/node/{node_id:path}")
def kg_node(node_id: str, include_candidates: bool = False):
    kg = get_kg()
    node = _nodes.get(node_id)
    if not node:
        raise HTTPException(status_code=404, detail=f"node not found: {node_id}")

    edges = [e for e in kg.get("edges", []) if e.get("source") == node_id or e.get("target") == node_id]
    neighbor_ids = set()
    for e in edges:
        neighbor_ids.add(e["source"])
        neighbor_ids.add(e["target"])
    neighbor_ids.discard(node_id)
    neighbors = [_nodes[x] for x in neighbor_ids if x in _nodes]

    candidate = []
    if include_candidates:
        candidate = [e for e in kg.get("candidate_edges", [])
                     if e.get("source") == node_id or e.get("target") == node_id]

    return {
        "node": node,
        "neighbors": neighbors,
        "edges": edges,
        "candidate_edges": candidate,
        "neighbor_count": len(neighbors),
    }


@router.get("/courses")
def kg_courses():
    kg = get_kg()
    courses = [n for n in kg.get("nodes", []) if n.get("node_type") == "course"]
    courses.sort(key=lambda n: n["properties"].get("code", ""))
    return {
        "courses": courses,
        "course_prerequisites": kg.get("course_prerequisites", {}),
        "total": len(courses),
    }


@router.get("/stats")
def kg_stats():
    kg = get_kg()
    nodes = kg.get("nodes", [])
    edges = kg.get("edges", [])
    return {
        "version": kg.get("version", 1),
        "generated_at": kg.get("generated_at"),
        "node_types": dict(Counter(n.get("node_type") for n in nodes)),
        "edge_types": dict(Counter(e.get("edge_type") for e in edges)),
        "candidate_edge_types": dict(Counter(e.get("edge_type") for e in kg.get("candidate_edges", []))),
        "course_prerequisites": kg.get("course_prerequisites", {}),
        "stats": kg.get("stats", {}),
        "total_nodes": len(nodes),
        "total_edges": len(edges),
    }
