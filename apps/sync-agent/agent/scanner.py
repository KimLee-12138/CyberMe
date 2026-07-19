"""Vault file scanner — computes hashes and builds file manifests."""

import hashlib
import os
from pathlib import Path

from agent.policy import load_policy, should_sync


def compute_hash(file_path: str) -> str:
    """Compute SHA-256 hash of a file's contents."""
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            sha.update(chunk)
    return sha.hexdigest()


def scan_vault(vault_root: str, policy_path: str | None = None) -> dict:
    """
    Scan the vault directory and return a manifest of files to sync.

    Returns:
        {
            "vault_id": "...",
            "files": [{"relative_path": "...", "hash": "...", "size_bytes": ...}],
            "skipped": [{"path": "...", "reason": "..."}],
            "stats": {"total": N, "synced": M, "skipped": K}
        }
    """
    policy = load_policy(policy_path)
    vault_path = Path(vault_root).resolve()

    files = []
    skipped = []

    for root, dirs, filenames in os.walk(str(vault_path)):
        # Filter directories by exclude rules
        dirs[:] = [d for d in dirs if not d.startswith(".") or d == ".obsidian"]

        for fname in filenames:
            full_path = os.path.join(root, fname)
            try:
                rel_path = os.path.relpath(full_path, str(vault_path))
            except ValueError:
                skipped.append({"path": full_path, "reason": "Outside vault root"})
                continue

            allowed, reason = should_sync(str(full_path), policy, str(vault_path))
            if not allowed:
                skipped.append({"path": rel_path, "reason": reason or "Policy excluded"})
                continue

            try:
                file_hash = compute_hash(str(full_path))
                size = os.path.getsize(str(full_path))
                files.append({
                    "relative_path": rel_path.replace("\\", "/"),
                    "hash": file_hash,
                    "size_bytes": size,
                })
            except OSError as e:
                skipped.append({"path": rel_path, "reason": f"Read error: {e}"})

    return {
        "vault_id": _get_or_create_vault_id(str(vault_path)),
        "vault_root": str(vault_path),
        "files": sorted(files, key=lambda x: x["relative_path"]),
        "skipped": sorted(skipped, key=lambda x: x["path"]),
        "stats": {
            "total": len(files) + len(skipped),
            "synced": len(files),
            "skipped": len(skipped),
            "total_size_mb": round(sum(f["size_bytes"] for f in files) / (1024 * 1024), 2),
        },
    }


def _get_or_create_vault_id(vault_root: str) -> str:
    """Get or create a persistent vault UUID stored in .cyberme/vault-id."""
    config_dir = Path(vault_root) / ".cyberme"
    config_dir.mkdir(exist_ok=True)
    vault_id_file = config_dir / "vault-id"

    if vault_id_file.exists():
        return vault_id_file.read_text().strip()

    import uuid
    vault_id = str(uuid.uuid4())
    vault_id_file.write_text(vault_id)
    return vault_id
