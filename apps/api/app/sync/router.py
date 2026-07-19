"""Sync API routes — /api/v1/sync/*."""

import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_device
from app.core.database import get_db
from app.models.device import Device
from app.models.vault import DocumentVersion, VaultDocument

router = APIRouter(prefix="/api/v1/sync")


# ── Request Schemas ────────────────────────────────────


class FileEntry(BaseModel):
    relative_path: str
    hash: str
    size_bytes: int


class ManifestRequest(BaseModel):
    vault_id: str
    files: list[FileEntry]


class SyncEvent(BaseModel):
    client_event_id: int
    operation: str  # upsert, move, delete
    relative_path: str
    previous_hash: str | None = None
    content_hash: str
    content: str | None = None
    occurred_at: str


class BatchEventsRequest(BaseModel):
    events: list[SyncEvent]


class UpsertRequest(BaseModel):
    relative_path: str
    previous_hash: str | None = None
    content_hash: str
    content: str | None = None


class MoveRequest(BaseModel):
    relative_path: str
    previous_hash: str | None = None
    content_hash: str


class DeleteMarkerRequest(BaseModel):
    relative_path: str
    content_hash: str


# ── Endpoints ──────────────────────────────────────────


@router.post("/manifests")
async def upload_manifest(
    body: ManifestRequest,
    request: Request,
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """First sync: upload full file manifest, get diff back."""
    existing = await db.execute(
        select(VaultDocument.relative_path, VaultDocument.content_hash).where(
            VaultDocument.vault_id == body.vault_id,
            VaultDocument.deleted_at.is_(None),
        )
    )
    existing_map = {row[0]: row[1] for row in existing.fetchall()}

    new_files = []
    updated_files = []
    unchanged = 0

    for f in body.files:
        current_hash = existing_map.pop(f.relative_path, None)
        if current_hash is None:
            new_files.append(f.relative_path)
        elif current_hash != f.hash:
            updated_files.append(f.relative_path)
        else:
            unchanged += 1

    # Files in existing_map but not in manifest → deleted locally
    deleted_locally = list(existing_map.keys())

    # Update device last_seen
    device.last_seen_at = datetime.now(timezone.utc)

    return {
        "new_count": len(new_files),
        "updated_count": len(updated_files),
        "unchanged_count": unchanged,
        "deleted_locally_count": len(deleted_locally),
        "new_files": new_files[:100],
        "updated_files": updated_files[:100],
        "cursor": int(datetime.now(timezone.utc).timestamp()),
    }


@router.post("/events:batch")
async def batch_events(
    body: BatchEventsRequest,
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """Process a batch of sync events."""
    results = []
    for event in body.events:
        try:
            await _process_event(db, event, device)
            results.append({"client_event_id": event.client_event_id, "status": "ok"})
        except Exception as e:
            results.append({
                "client_event_id": event.client_event_id,
                "status": "error",
                "error": str(e),
            })

    device.last_seen_at = datetime.now(timezone.utc)
    await db.flush()

    return {"results": results}


@router.post("/documents:upsert")
async def upsert_document(
    body: UpsertRequest,
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """Upsert a single document."""
    doc = await _upsert_document(db, body, device.id)
    return {"document_id": doc.id, "status": "ok"}


@router.post("/documents:move")
async def move_document(
    body: MoveRequest,
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """Handle a document being moved/renamed."""
    result = await db.execute(
        select(VaultDocument).where(
            VaultDocument.relative_path == body.relative_path,
            VaultDocument.deleted_at.is_(None),
        )
    )
    doc = result.scalar_one_or_none()

    if doc:
        doc.previous_hash = body.previous_hash
        await db.flush()
        return {"document_id": doc.id, "status": "already_exists"}
    else:
        # Try to find by content_hash (the file was renamed)
        result2 = await db.execute(
            select(VaultDocument).where(
                VaultDocument.content_hash == body.content_hash,
                VaultDocument.deleted_at.is_(None),
            )
        )
        existing = result2.scalar_one_or_none()
        if existing:
            existing.relative_path = body.relative_path
            await db.flush()
            return {"document_id": existing.id, "status": "renamed"}

    return {"status": "not_found"}


@router.post("/documents:delete-marker")
async def delete_marker(
    body: DeleteMarkerRequest,
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """Mark a document as deleted (tombstone)."""
    result = await db.execute(
        select(VaultDocument).where(
            VaultDocument.relative_path == body.relative_path,
            VaultDocument.deleted_at.is_(None),
        )
    )
    doc = result.scalar_one_or_none()
    if doc:
        now = datetime.now(timezone.utc)
        doc.deleted_at = now

    return {"status": "ok"}


@router.get("/status")
async def sync_status(
    device: Device = Depends(current_device),
    db: AsyncSession = Depends(get_db),
):
    """Return current sync status."""
    total = await db.execute(
        select(VaultDocument).where(VaultDocument.deleted_at.is_(None))
    )
    count = len(total.fetchall())

    return {
        "device_name": device.name,
        "last_seen": device.last_seen_at.isoformat() if device.last_seen_at else None,
        "total_documents": count,
    }


# ── Internal helpers ───────────────────────────────────


async def _process_event(db: AsyncSession, event: SyncEvent, device: Device) -> None:
    """Process a single sync event."""
    if event.operation == "upsert":
        await _upsert_document(
            db,
            UpsertRequest(
                relative_path=event.relative_path,
                previous_hash=event.previous_hash,
                content_hash=event.content_hash,
                content=event.content,
            ),
            device.id,
        )
    elif event.operation == "move":
        await _process_move(db, event)
    elif event.operation == "delete":
        now = datetime.now(timezone.utc)
        result = await db.execute(
            select(VaultDocument).where(
                VaultDocument.relative_path == event.relative_path,
                VaultDocument.deleted_at.is_(None),
            )
        )
        doc = result.scalar_one_or_none()
        if doc:
            doc.deleted_at = now


async def _upsert_document(
    db: AsyncSession, body: UpsertRequest, device_id: str
) -> VaultDocument:
    """Create or update a vault document."""
    result = await db.execute(
        select(VaultDocument).where(
            VaultDocument.relative_path == body.relative_path,
            VaultDocument.deleted_at.is_(None),
        )
    )
    doc = result.scalar_one_or_none()

    if doc:
        prev_hash = doc.content_hash
        doc.content_hash = body.content_hash
        if body.content is not None:
            doc.markdown_body = body.content
        doc.modified_at_local = datetime.now(timezone.utc)
    else:
        # Check if previously deleted — restore
        result2 = await db.execute(
            select(VaultDocument).where(
                VaultDocument.relative_path == body.relative_path,
            )
        )
        doc = result2.scalar_one_or_none()
        if doc and doc.deleted_at:
            doc.deleted_at = None
            doc.content_hash = body.content_hash
            if body.content is not None:
                doc.markdown_body = body.content
            prev_hash = None
        else:
            prev_hash = None
            doc = VaultDocument(
                id=str(uuid.uuid4()),
                vault_id="default",
                relative_path=body.relative_path,
                title=body.relative_path.split("/")[-1].replace(".md", ""),
                content_hash=body.content_hash,
                markdown_body=body.content,
                modified_at_local=datetime.now(timezone.utc),
            )
            db.add(doc)

    await db.flush()

    # Create version record if hash changed
    if prev_hash and prev_hash != body.content_hash:
        version = DocumentVersion(
            id=str(uuid.uuid4()),
            document_id=doc.id,
            content_hash=prev_hash,
            markdown_body=doc.markdown_body,
            source_device_id=device_id,
        )
        db.add(version)

    return doc


async def _process_move(db: AsyncSession, event: SyncEvent) -> None:
    """Handle a move/rename event."""
    result = await db.execute(
        select(VaultDocument).where(
            VaultDocument.content_hash == event.content_hash,
            VaultDocument.deleted_at.is_(None),
        )
    )
    doc = result.scalar_one_or_none()
    if doc:
        doc.relative_path = event.relative_path
        await db.flush()
