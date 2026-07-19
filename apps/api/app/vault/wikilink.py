"""Obsidian WikiLink parser.

Supports:
    [[Target]]
    [[Target|Alias]]
    [[Target#Heading]]
    [[Target#Heading|Alias]]
    [[Target#^block-id]]
"""

import re

# Matches [[target|alias#heading]] or any sub-combination
WIKILINK_PATTERN = re.compile(
    r"\[\["
    r"(?P<target>[^\]|#]+?)"        # Required: target path
    r"(?:#(?P<anchor>[^\]|]+?))?"   # Optional: #heading or #^block-id
    r"(?:\|(?P<alias>[^\]]+?))?"    # Optional: |alias
    r"\]\]"
)


def parse_wikilinks(text: str) -> list[dict]:
    """Extract all WikiLinks from text.

    Returns a list of dicts with keys: raw, target, alias, anchor.
    """
    links = []
    for match in WIKILINK_PATTERN.finditer(text):
        target = match.group("target").strip()
        alias = match.group("alias")
        anchor = match.group("anchor")

        links.append({
            "raw": match.group(0),
            "target": normalize_wikilink_target(target),
            "alias": alias.strip() if alias else None,
            "anchor": anchor.strip() if anchor else None,
        })
    return links


def normalize_wikilink_target(target: str) -> str:
    """Normalize a WikiLink target to a consistent format.

    Handles:
        - Trimming whitespace
        - Removing .md extension if present (will be re-added consistently)
        - Normalizing path separators
    """
    target = target.strip()
    # Remove .md extension for consistency
    if target.lower().endswith(".md"):
        target = target[:-3]
    # Normalize separators
    target = target.replace("\\", "/")
    # Resolve leading/trailing slashes
    target = target.strip("/")
    return target


def extract_wikilink_graph(text: str, source_path: str) -> list[dict]:
    """Extract WikiLinks and format as graph edges.

    Returns list of {"source": path, "target": target, "type": "wikilink"}.
    """
    links = parse_wikilinks(text)
    edges = []
    for link in links:
        edges.append({
            "source": source_path,
            "target": link["target"],
            "raw": link["raw"],
            "alias": link["alias"],
            "anchor": link["anchor"],
        })
    return edges
