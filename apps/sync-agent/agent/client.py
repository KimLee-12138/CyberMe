"""HTTP client for communicating with the CyberMe cloud API."""

import json
import time

import httpx

from agent.db import get_device_info, get_pending_events, mark_event_status


def _get_client() -> httpx.Client | None:
    """Create an authenticated HTTP client."""
    info = get_device_info()
    if not info or not info["token"]:
        return None
    return httpx.Client(
        base_url=info["api_base_url"].rstrip("/"),
        headers={
            "Authorization": f"Bearer {info['token']}",
            "Content-Type": "application/json",
        },
        timeout=30.0,
    )


def pair_device(pairing_code: str, device_name: str, platform: str, api_base_url: str) -> dict:
    """Register this device with the cloud using a pairing code."""
    client = httpx.Client(base_url=api_base_url.rstrip("/"), timeout=30.0)
    try:
        resp = client.post(
            "/api/v1/devices/pair",
            json={
                "pairing_code": pairing_code,
                "device_name": device_name,
                "platform": platform,
            },
        )
        if resp.status_code != 200:
            error = resp.json().get("detail", {}).get("message", resp.text)
            raise RuntimeError(f"Pairing failed: {error}")
        data = resp.json()
        return data
    finally:
        client.close()


def upload_manifest(vault_id: str, files: list[dict]) -> dict | None:
    """Upload a full file manifest to get initial sync diff."""
    client = _get_client()
    if not client:
        return None
    try:
        resp = client.post(
            "/api/v1/sync/manifests",
            json={"vault_id": vault_id, "files": files},
        )
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPError as e:
        print(f"Upload manifest failed: {e}")
        return None
    finally:
        client.close()


def push_events(events: list[dict]) -> dict | None:
    """Push a batch of sync events to the server."""
    client = _get_client()
    if not client:
        return None
    try:
        resp = client.post(
            "/api/v1/sync/events:batch",
            json={"events": events},
        )
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPError as e:
        print(f"Push events failed: {e}")
        return None
    finally:
        client.close()


def push_document(
    operation: str,
    relative_path: str,
    content: str | None,
    previous_hash: str | None,
    content_hash: str,
) -> bool:
    """Push a single document change."""
    client = _get_client()
    if not client:
        return False
    try:
        if operation == "upsert":
            resp = client.post(
                "/api/v1/sync/documents:upsert",
                json={
                    "relative_path": relative_path,
                    "previous_hash": previous_hash,
                    "content_hash": content_hash,
                    "content": content,
                },
            )
        elif operation == "move":
            resp = client.post(
                "/api/v1/sync/documents:move",
                json={
                    "relative_path": relative_path,
                    "previous_hash": previous_hash,
                    "content_hash": content_hash,
                },
            )
        elif operation == "delete":
            resp = client.post(
                "/api/v1/sync/documents:delete-marker",
                json={
                    "relative_path": relative_path,
                    "content_hash": content_hash,
                },
            )
        else:
            return False
        resp.raise_for_status()
        return True
    except httpx.HTTPError as e:
        print(f"Push document failed: {e}")
        return False
    finally:
        client.close()


def flush_pending_events() -> dict:
    """Push all pending events from the queue. Returns summary."""
    events = get_pending_events(limit=50)
    if not events:
        return {"synced": 0, "failed": 0}

    batch = []
    for evt in events:
        batch.append({
            "client_event_id": evt["client_event_id"],
            "operation": evt["operation"],
            "relative_path": evt["relative_path"],
            "previous_hash": evt.get("previous_hash"),
            "content_hash": evt["content_hash"],
            "content": evt.get("content"),
            "occurred_at": evt["occurred_at"],
        })

    result = push_events(batch)
    if result:
        for evt in events:
            mark_event_status(evt["id"], "done")
        return {"synced": len(events), "failed": 0}
    else:
        for evt in events:
            mark_event_status(evt["id"], "failed", "Network error")
        return {"synced": 0, "failed": len(events)}


def check_server_health() -> bool:
    """Check if the cloud API is reachable."""
    client = _get_client()
    if not client:
        return False
    try:
        resp = client.get("/health/live")
        return resp.status_code == 200
    except httpx.HTTPError:
        return False
    finally:
        client.close()


def fetch_writeback_patches() -> list[dict]:
    """Fetch pending writeback patches from the server."""
    client = _get_client()
    if not client:
        return []
    try:
        resp = client.get("/api/v1/writebacks?status=approved")
        resp.raise_for_status()
        return resp.json().get("proposals", [])
    except httpx.HTTPError:
        return []
    finally:
        client.close()


def report_patch_result(patch_id: str, success: bool, error: str | None = None) -> None:
    """Report the result of applying a writeback patch."""
    client = _get_client()
    if not client:
        return
    try:
        resp = client.post(
            f"/api/v1/writebacks/{patch_id}/application-result",
            json={"success": success, "error": error},
        )
        resp.raise_for_status()
    except httpx.HTTPError as e:
        print(f"Report patch result failed: {e}")
    finally:
        client.close()
