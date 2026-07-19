"""SQLite database for offline queue, cursors, and configuration."""

import sqlite3
import json
from pathlib import Path
from datetime import datetime, timezone


DB_PATH = Path.home() / ".cyberme" / "sync-agent.db"


def get_db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db() -> None:
    """Create tables if they don't exist."""
    conn = get_db()
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS config (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS sync_events (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            client_event_id INTEGER NOT NULL,
            operation     TEXT NOT NULL,  -- upsert, move, delete
            relative_path TEXT NOT NULL,
            previous_hash TEXT,
            content_hash  TEXT,
            content       TEXT,
            occurred_at   TEXT NOT NULL,
            retries       INTEGER DEFAULT 0,
            status        TEXT DEFAULT 'pending',  -- pending, syncing, done, failed
            error         TEXT,
            created_at    TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS sync_cursor (
            device_id       TEXT PRIMARY KEY,
            server_event_seq INTEGER DEFAULT 0,
            client_event_seq INTEGER DEFAULT 0,
            manifest_version TEXT,
            updated_at      TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS device_info (
            id            TEXT PRIMARY KEY,
            name          TEXT NOT NULL,
            platform      TEXT NOT NULL,
            token         TEXT NOT NULL,
            api_base_url  TEXT NOT NULL,
            created_at    TEXT DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS writeback_patches (
            id            TEXT PRIMARY KEY,
            proposal_id   TEXT NOT NULL,
            target_path   TEXT NOT NULL,
            base_hash     TEXT NOT NULL,
            unified_diff  TEXT NOT NULL,
            status        TEXT DEFAULT 'pending',  -- pending, applying, applied, conflict, failed
            applied_at    TEXT,
            error         TEXT
        );
    """)
    conn.commit()
    conn.close()


# ── Config helpers ────────────────────────────────────

def get_config(key: str, default: str = "") -> str:
    conn = get_db()
    row = conn.execute("SELECT value FROM config WHERE key = ?", (key,)).fetchone()
    conn.close()
    return row["value"] if row else default


def set_config(key: str, value: str) -> None:
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO config (key, value) VALUES (?, ?)", (key, value)
    )
    conn.commit()
    conn.close()


# ── Device info ───────────────────────────────────────

def save_device_info(device_id: str, name: str, platform: str, token: str, api_url: str) -> None:
    conn = get_db()
    conn.execute(
        """INSERT OR REPLACE INTO device_info (id, name, platform, token, api_base_url)
           VALUES (?, ?, ?, ?, ?)""",
        (device_id, name, platform, token, api_url),
    )
    conn.commit()
    conn.close()


def get_device_info() -> dict | None:
    conn = get_db()
    row = conn.execute("SELECT * FROM device_info LIMIT 1").fetchone()
    conn.close()
    return dict(row) if row else None


# ── Sync events queue ─────────────────────────────────

def enqueue_event(
    client_event_id: int,
    operation: str,
    relative_path: str,
    previous_hash: str | None,
    content_hash: str,
    content: str | None = None,
) -> None:
    conn = get_db()
    conn.execute(
        """INSERT INTO sync_events (client_event_id, operation, relative_path,
           previous_hash, content_hash, content, occurred_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            client_event_id,
            operation,
            relative_path,
            previous_hash,
            content_hash,
            content,
            datetime.now(timezone.utc).isoformat(),
        ),
    )
    # Update cursor
    conn.execute(
        "INSERT OR REPLACE INTO sync_cursor (device_id, client_event_seq, updated_at) "
        "VALUES ('local', ?, ?)",
        (client_event_id, datetime.now(timezone.utc).isoformat()),
    )
    conn.commit()
    conn.close()


def get_pending_events(limit: int = 50) -> list[dict]:
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM sync_events WHERE status IN ('pending', 'failed') "
        "AND retries < 5 ORDER BY id LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def mark_event_status(event_id: int, status: str, error: str | None = None) -> None:
    conn = get_db()
    if status == "done":
        conn.execute(
            "UPDATE sync_events SET status = ?, retries = retries + 1 WHERE id = ?",
            (status, event_id),
        )
    else:
        conn.execute(
            "UPDATE sync_events SET status = ?, retries = retries + 1, error = ? WHERE id = ?",
            (status, error, event_id),
        )
    conn.commit()
    conn.close()


def get_stats() -> dict:
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) as c FROM sync_events").fetchone()["c"]
    pending = conn.execute(
        "SELECT COUNT(*) as c FROM sync_events WHERE status = 'pending'"
    ).fetchone()["c"]
    failed = conn.execute(
        "SELECT COUNT(*) as c FROM sync_events WHERE status = 'failed' AND retries >= 5"
    ).fetchone()["c"]
    patches = conn.execute(
        "SELECT COUNT(*) as c FROM writeback_patches WHERE status = 'pending'"
    ).fetchone()["c"]
    conn.close()
    return {
        "total_events": total,
        "pending_events": pending,
        "failed_events": failed,
        "pending_patches": patches,
    }
