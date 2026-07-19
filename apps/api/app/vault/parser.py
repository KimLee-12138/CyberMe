"""Markdown document parser — YAML frontmatter, WikiLinks, headings, tags."""

import hashlib
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import frontmatter

from app.vault.models import ParsedDocument, SourceInfo
from app.vault.wikilink import parse_wikilinks

# Matches markdown headings: ## Heading Text
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

# Matches inline #tags in body text (not in code blocks)
TAG_PATTERN = re.compile(r"(?<!\w)#([a-zA-Z\u4e00-\u9fff][\w\u4e00-\u9fff/-]*)")

# Document type inference from path patterns
DOCUMENT_TYPE_PATTERNS = [
    (r"(?:^|/)MOC[/-]|MOC\.md$|内容地图", "moc"),
    (r"知识点|concept|概念", "concept"),
    (r"例题|example|习题", "example"),
    (r"错题|mistake|错因", "mistake"),
    (r"公式|formula|定理", "formula"),
    (r"提取|extract|摘录|材料", "extract"),
    (r"项目|project|作战", "project"),
    (r"来源|source|原始", "source"),
    (r"个人|self|档案|规则|偏好|风格", "self"),
]


def parse_markdown(
    content: str,
    relative_path: str,
    vault_id: str | None = None,
    modified_at: datetime | None = None,
) -> ParsedDocument:
    """Parse a Markdown document's YAML frontmatter, body, and WikiLinks.

    Args:
        content: Raw Markdown text (UTF-8).
        relative_path: Vault-relative path (e.g., "20_University/DB/知识点/事务.md").
        vault_id: Optional vault identifier.
        modified_at: Optional local modification time.

    Returns:
        ParsedDocument with all extracted metadata.
    """
    # Compute content hash
    content_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()

    # Parse frontmatter and body
    try:
        post = frontmatter.loads(content)
        fm = dict(post.metadata) if post.metadata else {}
        body = post.content
    except Exception:
        fm = {}
        body = content

    # Extract title from YAML title, first H1, or filename
    title = fm.get("title")
    if not title:
        h1_match = HEADING_PATTERN.search(body)
        if h1_match:
            title = h1_match.group(2).strip()
    if not title:
        title = Path(relative_path).stem

    # Extract document type
    doc_type = fm.get("type") or _infer_document_type(relative_path, title, fm)

    # Extract source info (handle YAML lists vs strings)
    source_info = SourceInfo(
        source=_to_str(fm.get("source")),
        source_pages=_to_str(fm.get("source_pages") or fm.get("pages")),
        source_hash=_to_str(fm.get("source_hash")),
        verification=fm.get("verification"),
        confidence=_to_float(fm.get("confidence")),
    )

    # Extract tags
    yaml_tags = fm.get("tags", [])
    if isinstance(yaml_tags, str):
        yaml_tags = [t.strip() for t in yaml_tags.split(",")]
    body_tags = [m.group(1) for m in TAG_PATTERN.finditer(body)]
    all_tags = list(set(yaml_tags + body_tags))

    # Extract headings
    headings = []
    for m in HEADING_PATTERN.finditer(body):
        headings.append({
            "level": len(m.group(1)),
            "text": m.group(2).strip(),
            "line": body[: m.start()].count("\n") + 1,
        })

    # Extract WikiLinks
    wikilinks = parse_wikilinks(content)

    # Needs review
    needs_review = fm.get("needs_review", False)
    if isinstance(needs_review, str):
        needs_review = needs_review.lower() in ("true", "yes", "1")

    return ParsedDocument(
        document_id=fm.get("id"),  # If already assigned
        relative_path=relative_path,
        vault_id=vault_id,
        title=title,
        frontmatter=fm,
        markdown_body=body,
        content_hash=content_hash,
        document_type=doc_type,
        course_code=fm.get("course") or _infer_course_code(relative_path),
        project_code=fm.get("project"),
        status=fm.get("status"),
        mastery=fm.get("mastery"),
        importance=fm.get("importance"),
        tags=all_tags,
        source_info=source_info,
        needs_review=needs_review,
        headings=headings,
        wikilinks=wikilinks,
        modified_at_local=modified_at,
        parsed_at=datetime.now(timezone.utc),
    )


def _infer_document_type(relative_path: str, title: str, fm: dict) -> str | None:
    """Infer document type from path, title, or frontmatter."""
    combined = f"{relative_path} {title} {fm.get('course', '')}"
    for pattern, dtype in DOCUMENT_TYPE_PATTERNS:
        if re.search(pattern, combined, re.IGNORECASE):
            return dtype
    return "unknown"


def _infer_course_code(relative_path: str) -> str | None:
    """Infer course code from path like '20_University/DB_数据库/...'."""
    parts = relative_path.replace("\\", "/").split("/")
    for part in parts:
        # Match patterns like "DB_数据库" or "ALGO_算法"
        match = re.match(r"^([A-Z]+)_.*", part)
        if match:
            return match.group(1)
    return None


def _to_str(value) -> str | None:
    """Normalize YAML field that may be a string or list of strings."""
    if value is None:
        return None
    if isinstance(value, list):
        return ", ".join(str(v) for v in value if v)
    return str(value) if value else None


def _to_float(value) -> float | None:
    """Normalize YAML field that may be numeric or a confidence label."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    # Map confidence labels
    labels = {"high": 0.9, "medium": 0.6, "low": 0.3,
              "explicit": 1.0, "inferred": 0.5}
    return labels.get(str(value).lower())


def compute_semantic_hash(content: str) -> str:
    """A hash that ignores minor formatting differences (for chunking decisions)."""
    normalized = content.replace("\r\n", "\n").strip()
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()
