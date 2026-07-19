"""Read and apply sync-policy.yaml."""

import fnmatch
import os
from pathlib import Path

import yaml

DEFAULT_POLICY = {
    "include": ["**/*.md"],
    "exclude": [
        "91_Raw-Archive/**",
        "**/.git/**",
        "**/.obsidian/**",
        "**/node_modules/**",
        "**/.venv/**",
        "**/__pycache__/**",
    ],
    "max_file_size_mb": 10,
    "allowed_attachment_extensions": [],
    "sensitive_patterns": [
        "**/password*",
        "**/secret*",
        "**/credential*",
        "**/api_key*",
    ],
}


def load_policy(policy_path: str | None = None) -> dict:
    """Load sync policy from a YAML file, or return defaults."""
    if policy_path is None:
        candidates = [
            Path(__file__).parent.parent / "sync-policy.yaml",
            Path(os.getcwd()) / "sync-policy.yaml",
        ]
        for p in candidates:
            if p.exists():
                policy_path = str(p)
                break

    if policy_path and Path(policy_path).exists():
        with open(policy_path, "r", encoding="utf-8") as f:
            user_policy = yaml.safe_load(f) or {}
        policy = {**DEFAULT_POLICY, **user_policy}
    else:
        policy = DEFAULT_POLICY

    return policy


def should_sync(file_path: str, policy: dict, vault_root: str | None = None) -> tuple[bool, str | None]:
    """Check if a file should be synced. Returns (allowed, reason_if_blocked)."""
    rel_path = file_path.replace("\\", "/")

    # If given an absolute path, make it relative to vault_root
    if vault_root and os.path.isabs(file_path):
        try:
            rel_path = os.path.relpath(file_path, vault_root).replace("\\", "/")
        except ValueError:
            pass

    if rel_path.startswith("./"):
        rel_path = rel_path[2:]

    # Check file size
    try:
        size_mb = os.path.getsize(file_path) / (1024 * 1024)
        if size_mb > policy.get("max_file_size_mb", 10):
            return False, f"File too large: {size_mb:.1f}MB > {policy['max_file_size_mb']}MB"
    except OSError:
        return False, "Cannot read file"

    # Check sensitive patterns
    for pattern in policy.get("sensitive_patterns", []):
        if fnmatch.fnmatch(rel_path, pattern):
            return False, f"Matches sensitive pattern: {pattern}"

    # Check exclude
    for pattern in policy.get("exclude", []):
        if fnmatch.fnmatch(rel_path, pattern):
            return False, f"Excluded by pattern: {pattern}"

    # Check include (expand ** patterns for fnmatch compatibility)
    for pattern in policy.get("include", []):
        # Generate both shallow and deep patterns:
        # "dir/**/*.md" → match "dir/file.md" AND "dir/sub/file.md"
        patterns_to_check = [pattern]
        if "/**/" in pattern:
            # Also match files directly in the directory (no subdirectory)
            patterns_to_check.append(pattern.replace("/**/", "/"))
        for p in patterns_to_check:
            if fnmatch.fnmatch(rel_path, p):
                ext = os.path.splitext(rel_path)[1].lower()
                if ext and ext != ".md":
                    allowed = policy.get("allowed_attachment_extensions", [])
                    if ext not in allowed:
                        return False, f"Attachment type not allowed: {ext}"
                return True, None

    return False, "Does not match any include pattern"
