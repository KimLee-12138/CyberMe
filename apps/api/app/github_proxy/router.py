"""GitHub integration — proxy API calls, store annotations."""

import uuid
from datetime import datetime, timezone

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.config import settings
from app.core.database import get_db
from app.models.user import User

router = APIRouter(prefix="/api/v1/github")

# ── Schemas ──────────────────────────────────────────────

class RepoNote(BaseModel):
    repo_full_name: str = Field(..., max_length=300)
    note: str = Field(default="", max_length=5000)

class ImportRepo(BaseModel):
    repo_full_name: str
    note: str = ""

# ── Simple in-memory note store ─────────────────────────
# In production, use a DB table; for now, per-user dict

_repo_notes: dict[str, list[dict]] = {}  # {user_id: [{repo_full_name, note}]}

def _notes_for(user_id: str) -> list[dict]:
    if user_id not in _repo_notes:
        _repo_notes[user_id] = []
    return _repo_notes[user_id]

# ── Endpoints ────────────────────────────────────────────

@router.get("/repos")
async def list_github_repos(
    page: int = 1,
    per_page: int = 30,
    user: User = Depends(current_user),
):
    """Fetch user's GitHub repos via GitHub API (token from settings)."""
    token = settings.github_token
    if not token:
        raise HTTPException(status_code=400, detail="未配置 GitHub Token，请在 .env 中设置 GITHUB_TOKEN")

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.get(
            "https://api.github.com/user/repos",
            headers=headers,
            params={"per_page": per_page, "page": page, "sort": "updated", "type": "owner"},
        )
        if resp.status_code == 401:
            raise HTTPException(status_code=401, detail="GitHub Token 无效或已过期")
        if resp.status_code != 200:
            raise HTTPException(status_code=502, detail=f"GitHub API 错误: {resp.status_code}")

        repos = resp.json()
        notes = _notes_for(user.id)
        notes_map = {n["repo_full_name"]: n["note"] for n in notes}

        return {
            "repos": [
                {
                    "id": r["id"],
                    "full_name": r["full_name"],
                    "name": r["name"],
                    "description": r.get("description"),
                    "html_url": r["html_url"],
                    "language": r.get("language"),
                    "stargazers_count": r.get("stargazers_count", 0),
                    "updated_at": r.get("updated_at"),
                    "topics": r.get("topics", []),
                    "note": notes_map.get(r["full_name"], ""),
                }
                for r in repos
            ],
        }


@router.post("/notes")
async def save_repo_note(
    body: RepoNote,
    user: User = Depends(current_user),
):
    """Save a personal note for a GitHub repo."""
    notes = _notes_for(user.id)
    for n in notes:
        if n["repo_full_name"] == body.repo_full_name:
            n["note"] = body.note
            return {"status": "saved"}
    notes.append({"repo_full_name": body.repo_full_name, "note": body.note})
    return {"status": "saved"}


@router.post("/import")
async def import_repo_as_project(
    body: ImportRepo,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """Import a GitHub repo as a CyberMe project."""
    from app.models.project import Project

    # Check if already imported
    existing = await db.execute(
        select(Project).where(Project.title == body.repo_full_name)
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=409, detail="该项目已导入")

    project = Project(
        id=str(uuid.uuid4()),
        user_id=user.id,
        title=body.repo_full_name,
        goal=body.note or None,
        status="active",
    )
    db.add(project)
    await db.commit()
    return {"id": project.id, "title": project.title}


@router.get("/health")
async def github_health(user: User = Depends(current_user)):
    """Check if GitHub token is configured and valid."""
    token = settings.github_token
    if not token:
        return {"configured": False, "message": "未配置 GITHUB_TOKEN"}
    try:
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        }
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get("https://api.github.com/user", headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return {"configured": True, "user": data.get("login"), "avatar": data.get("avatar_url")}
            return {"configured": True, "error": f"Token 无效 ({resp.status_code})"}
    except Exception as e:
        return {"configured": True, "error": str(e)}
