"""Read-only Yuketang integration API."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from app.auth.dependencies import current_user
from app.integrations.yuketang.client import YktError
from app.integrations.yuketang.service import ykt_service

router = APIRouter(
    prefix="/api/v1/integrations/yuketang",
    tags=["yuketang"],
    dependencies=[Depends(current_user)],
)


class SessionIn(BaseModel):
    sessionid: str = Field(min_length=8, max_length=512)


@router.get("/status")
async def status():
    return ykt_service.status()


@router.get("/overview")
async def overview(force: bool = Query(default=False)):
    return await ykt_service.get_overview(force=force)


@router.post("/session")
async def save_session(payload: SessionIn):
    try:
        account = await ykt_service.set_session(payload.sessionid)
    except YktError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc
    return {"ok": True, "account": account, "overview": ykt_service.snapshot()}


@router.delete("/session")
async def clear_session():
    ykt_service.clear_session()
    return {"ok": True}


@router.post("/sync")
async def sync():
    try:
        return await ykt_service.get_overview(force=True)
    except YktError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc


@router.get("/courseware/{lesson_id}/pdf")
async def courseware_pdf(lesson_id: str, force: bool = Query(default=False)):
    try:
        path = await ykt_service.get_courseware_pdf(lesson_id, force=force)
    except YktError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc
    return FileResponse(
        path,
        media_type="application/pdf",
        filename=f"yuketang-{lesson_id}.pdf",
    )


@router.get("/courseware/{lesson_id}")
async def courseware(lesson_id: str, force: bool = Query(default=False)):
    try:
        return await ykt_service.get_courseware(lesson_id, force=force)
    except YktError as exc:
        raise HTTPException(status_code=exc.status_code, detail=str(exc)) from exc
