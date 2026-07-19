"""Semantic chunker — splits Markdown documents into searchable chunks."""

import hashlib
import re
from typing import Optional

# Matches headings for boundary detection
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

# Max chunk size in characters (roughly ~500 tokens for Chinese)
MAX_CHUNK_CHARS = 2000
CHUNK_OVERLAP = 200


def chunk_document(content: str, heading_path: list[str] | None = None) -> list[dict]:
    """
    Split a Markdown document into semantic chunks.

    Boundaries: headings, code blocks, list groups, paragraphs.
    Returns list of {content, heading_path, ordinal, page_ref, token_estimate}.
    """
    if heading_path is None:
        heading_path = []

    chunks = []
    current_headings = list(heading_path)
    current_chunk_lines: list[str] = []
    current_char_count = 0
    ordinal = 0

    lines = content.split("\n")
    in_code_block = False

    def _flush_chunk():
        nonlocal ordinal
        text = "\n".join(current_chunk_lines).strip()
        if not text:
            return

        content_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
        token_estimate = _estimate_tokens(text)

        chunks.append({
            "content": text,
            "heading_path": list(current_headings),
            "ordinal": ordinal,
            "content_hash": content_hash,
            "token_count": token_estimate,
        })
        ordinal += 1

    for i, line in enumerate(lines):
        # Track code blocks — don't break chunks inside them
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            current_chunk_lines.append(line)
            current_char_count += len(line)
            continue

        # Heading detection
        if not in_code_block:
            m = HEADING_RE.match(line)
            if m:
                level = len(m.group(1))
                heading_text = m.group(2).strip()

                # Flush current chunk at heading boundary
                if current_chunk_lines:
                    _flush_chunk()
                    current_chunk_lines = []
                    current_char_count = 0

                # Update heading path
                current_headings = current_headings[: level - 1]
                current_headings.append(heading_text)
                current_chunk_lines.append(line)
                current_char_count += len(line)
                continue

        # Add line to current chunk
        current_chunk_lines.append(line)
        current_char_count += len(line)

        # Flush if chunk is large enough and we're at a clean break
        if current_char_count >= MAX_CHUNK_CHARS:
            # Look for a clean break point (blank line, list end, paragraph end)
            clean_break = (
                not line.strip()  # blank line
                or line.rstrip().endswith(".")  # sentence end
                or line.rstrip().endswith("。)")
                or line.rstrip().endswith("）")
            )
            if clean_break:
                _flush_chunk()
                # Keep overlap for continuity
                if len(current_chunk_lines) > 3:
                    current_chunk_lines = current_chunk_lines[-3:]
                else:
                    current_chunk_lines = []
                current_char_count = sum(len(l) for l in current_chunk_lines)

    # Flush remaining content
    if current_chunk_lines:
        _flush_chunk()

    return chunks


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~1.5 chars per token for Chinese, ~4 for English."""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    other_chars = len(text) - chinese_chars
    return int(chinese_chars / 1.5 + other_chars / 4)
