"""Vault file watcher using watchdog."""

import os
import time
import threading
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from agent.db import enqueue_event
from agent.policy import load_policy, should_sync
from agent.scanner import compute_hash


class VaultEventHandler(FileSystemEventHandler):
    """Handles file system events and enqueues sync operations."""

    def __init__(self, vault_root: str, policy: dict):
        self.vault_root = Path(vault_root).resolve()
        self.policy = policy
        self._event_counter = 0
        self._pending: dict[str, tuple[str, float]] = {}  # path → (operation, timestamp)
        self._debounce_seconds = 2.0
        self._timer: threading.Timer | None = None

    def on_modified(self, event):
        if event.is_directory:
            return
        self._handle_event(event.src_path, "upsert")

    def on_created(self, event):
        if event.is_directory:
            return
        self._handle_event(event.src_path, "upsert")

    def on_moved(self, event):
        if event.is_directory:
            return
        # Record the new path
        self._handle_event(event.dest_path, "move")

    def on_deleted(self, event):
        if event.is_directory:
            return
        self._handle_event(event.src_path, "delete")

    def _handle_event(self, file_path: str, operation: str):
        """Debounce and enqueue the event."""
        # Check if file should be synced
        allowed, reason = should_sync(file_path, self.policy, str(self.vault_root))
        if not allowed:
            return

        # Debounce: store latest event for this path
        self._pending[file_path] = (operation, time.time())

        # Reset debounce timer
        if self._timer:
            self._timer.cancel()
        self._timer = threading.Timer(self._debounce_seconds, self._flush)
        self._timer.start()

    def _flush(self):
        """Flush debounced events to the queue."""
        pending = dict(self._pending)
        self._pending.clear()

        for file_path, (operation, timestamp) in pending.items():
            try:
                current_hash = compute_hash(file_path)
                previous_hash = None  # Would need to track previous state

                # Get relative path
                try:
                    rel_path = os.path.relpath(file_path, str(self.vault_root))
                    rel_path = rel_path.replace("\\", "/")
                except ValueError:
                    continue

                # Read content
                content = None
                if operation in ("upsert", "move"):
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()
                    except Exception:
                        continue

                self._event_counter += 1
                enqueue_event(
                    client_event_id=self._event_counter,
                    operation=operation,
                    relative_path=rel_path,
                    previous_hash=previous_hash,
                    content_hash=current_hash,
                    content=content if operation != "delete" else None,
                )
            except OSError:
                # File deleted or inaccessible after event — skip
                continue


def start_watcher(vault_root: str, policy_path: str | None = None):
    """Start the file watcher in a background thread."""
    policy = load_policy(policy_path)
    handler = VaultEventHandler(vault_root, policy)
    observer = Observer()
    observer.schedule(handler, str(vault_root), recursive=True)
    observer.start()
    return observer, handler
