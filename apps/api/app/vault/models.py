"""Pydantic models for parsed Markdown documents."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WikiLink(BaseModel):
    """A parsed Obsidian WikiLink."""
    raw: str                    # Original text: [[link|alias#heading]]
    target: str                 # Normalized target document path
    alias: str | None = None    # Display alias
    anchor: str | None = None   # Heading/block anchor


class SourceInfo(BaseModel):
    """Source attribution from YAML frontmatter."""
    source: str | None = None          # Source file name (e.g., "数据库系统概论.pdf")
    source_pages: str | None = None    # Page references (e.g., "312-315")
    source_hash: str | None = None     # Hash of the source file
    verification: str | None = None    # explicit / inferred
    confidence: float | None = None    # 0.0 - 1.0


class ParsedDocument(BaseModel):
    """A fully parsed Markdown document from the Vault."""

    # Identity
    document_id: str | None = None
    relative_path: str
    vault_id: str | None = None

    # Content
    title: str | None = None
    frontmatter: dict = Field(default_factory=dict)
    markdown_body: str = ""
    content_hash: str | None = None

    # Metadata from YAML
    document_type: str | None = None       # concept, moc, extract, example, mistake, etc.
    course_code: str | None = None         # DB, ALGO, etc.
    project_code: str | None = None
    status: str | None = None              # draft, reviewed, stable
    mastery: str | None = None             # unknown, learning, reviewing, mastered
    importance: str | None = None          # high, medium, low
    tags: list[str] = Field(default_factory=list)

    # Source attribution
    source_info: SourceInfo = Field(default_factory=SourceInfo)
    needs_review: bool = False

    # Structure
    headings: list[dict] = Field(default_factory=list)
    # [{"level": 1, "text": "...", "line": 10}, ...]

    wikilinks: list[WikiLink] = Field(default_factory=list)
    # All [[links]] found in the document

    # Computed
    modified_at_local: datetime | None = None
    parsed_at: datetime | None = None


class ChunkInfo(BaseModel):
    """A semantic chunk of a document."""
    chunk_id: str | None = None
    document_id: str
    heading_path: list[str] = Field(default_factory=list)  # ["课程", "章节", "小节"]
    ordinal: int = 0
    content: str
    token_count: int = 0
    page_ref: str | None = None
    content_hash: str | None = None
    metadata: dict = Field(default_factory=dict)
