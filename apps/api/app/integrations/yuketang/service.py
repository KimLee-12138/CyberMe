"""Yuketang sync/cache service (read-only)."""

from __future__ import annotations

import asyncio
import base64
import hashlib
import io
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from cryptography.fernet import Fernet
from PIL import Image, UnidentifiedImageError

from app.core.config import REPO_ROOT, settings
from app.integrations.yuketang.client import (
    REGION_NAMES,
    YktClient,
    YktError,
    get_http_client,
)

DATA_DIR = REPO_ROOT / "data" / "integrations" / "yuketang"
CACHE_FILE = DATA_DIR / "cache.json"
SESSION_FILE = DATA_DIR / "session.enc"
COURSEWARE_DIR = DATA_DIR / "courseware"
PDF_DIR = DATA_DIR / "pdf"
CACHE_VERSION = 2

SESSION_RE = re.compile(r"^[A-Za-z0-9._-]{8,512}$")


def _fernet() -> Fernet:
    key = base64.urlsafe_b64encode(
        hashlib.sha256(settings.secret_key.encode("utf-8")).digest()
    )
    return Fernet(key)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_private(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(data, encoding="utf-8")
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    tmp.replace(path)


def _write_private_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    tmp.replace(path)


class YuketangService:
    def __init__(self) -> None:
        self.region = (settings.ykt_region or "changjiang").strip()
        self._lock = asyncio.Lock()
        self._cache: dict[str, Any] | None = self._load_cache()
        self._courseware: dict[str, dict[str, Any]] = {}
        self._session: str | None = None
        self._account: dict[str, Any] | None = None
        self._last_error: str | None = None
        self._task: asyncio.Task | None = None
        self._sync_task: asyncio.Task | None = None

    # ── session ─────────────────────────────────────────────
    def _env_session(self) -> str:
        return (settings.ykt_sessionid or "").strip()

    def get_session(self) -> str | None:
        if self._session:
            return self._session
        env = self._env_session()
        if env and SESSION_RE.match(env):
            self._session = env
            return env
        if not SESSION_FILE.exists():
            return None
        try:
            raw = _fernet().decrypt(SESSION_FILE.read_bytes()).decode("utf-8")
        except Exception:
            return None
        raw = raw.strip()
        if not SESSION_RE.match(raw):
            return None
        self._session = raw
        return raw

    async def set_session(self, sessionid: str) -> dict:
        sessionid = (sessionid or "").strip()
        if not SESSION_RE.match(sessionid):
            raise YktError("sessionid 格式不正确", status_code=400)
        client = YktClient(sessionid, self.region)
        account = await client.verify()
        DATA_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
        _write_private(SESSION_FILE, _fernet().encrypt(sessionid.encode()).decode())
        self._session = sessionid
        self._account = account
        self._last_error = None
        self._cache = None
        # Verify is fast; the full course/activity sync is not. Return now
        # and let the page show progress instead of holding the HTTP request.
        self._sync_task = asyncio.create_task(self._sync_after_login())
        return account

    async def _sync_after_login(self) -> None:
        try:
            await self.get_overview(force=True)
        except asyncio.CancelledError:
            raise
        except Exception as exc:
            self._last_error = str(exc)

    def snapshot(self) -> dict:
        if self._cache:
            return self._cache
        return {
            "schema": CACHE_VERSION,
            "configured": bool(self.get_session()),
            "region": self.region,
            "region_name": REGION_NAMES.get(self.region, self.region),
            "account": self._account,
            "last_sync": None,
            "last_error": None,
            "syncing": bool(self._lock.locked() or self._sync_task and not self._sync_task.done()),
            "courses": [],
            "assignments": [],
        }

    def clear_session(self) -> None:
        self._session = None
        self._account = None
        if self._sync_task and not self._sync_task.done():
            self._sync_task.cancel()
        self._sync_task = None
        for path in (SESSION_FILE, CACHE_FILE):
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
        paths = COURSEWARE_DIR.glob("*.json") if COURSEWARE_DIR.exists() else []
        for path in paths:
            try:
                path.unlink()
            except OSError:
                pass
        pdf_paths = PDF_DIR.glob("*.pdf") if PDF_DIR.exists() else []
        for path in pdf_paths:
            try:
                path.unlink()
            except OSError:
                pass
        self._cache = None
        self._courseware.clear()

    def status(self) -> dict:
        session = self.get_session()
        cache = self._cache or {}
        syncing = bool(
            self._lock.locked()
            or (self._sync_task is not None and not self._sync_task.done())
        )
        return {
            "configured": bool(session),
            "region": self.region,
            "region_name": REGION_NAMES.get(self.region, self.region),
            "account": self._account or cache.get("account"),
            "last_sync": cache.get("last_sync"),
            "last_error": self._last_error or cache.get("last_error"),
            "refreshing": syncing,
            "syncing": syncing,
        }

    # ── cache ───────────────────────────────────────────────
    def _load_cache(self) -> dict[str, Any] | None:
        if not CACHE_FILE.exists():
            return None
        try:
            data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            if not isinstance(data, dict) or data.get("schema") != CACHE_VERSION:
                return None
            return data
        except Exception:
            return None

    def _save_cache(self, data: dict[str, Any]) -> None:
        _write_private(CACHE_FILE, json.dumps(data, ensure_ascii=False))
        self._cache = data

    def _cache_fresh(self) -> bool:
        if not self._cache:
            return False
        try:
            last = datetime.fromisoformat(str(self._cache.get("last_sync", "")))
        except ValueError:
            return False
        age = (datetime.now(timezone.utc) - last).total_seconds()
        return age < max(60, settings.ykt_refresh_minutes * 60)

    async def get_overview(self, force: bool = False) -> dict:
        session = self.get_session()
        if not session:
            return {
                "configured": False,
                "region": self.region,
                "region_name": REGION_NAMES.get(self.region, self.region),
                "account": None,
                "last_sync": None,
                "last_error": None,
                "courses": [],
                "assignments": [],
            }
        if not force and self._cache and self._cache_fresh():
            return self._cache
        if not force and self._cache and self._lock.locked():
            # A background refresh is running; serve the old snapshot.
            return self._cache
        if not force and not self._cache and (
            self._lock.locked()
            or (self._sync_task is not None and not self._sync_task.done())
        ):
            return self.snapshot()

        async with self._lock:
            if not force and self._cache and self._cache_fresh():
                return self._cache
            client = YktClient(session, self.region)
            try:
                account = await client.verify()
                self._account = account
                courses = await client.list_courses()

                # Publish the course list immediately. The page can render
                # courses while activities are still being fetched.
                clean_courses: list[dict] = [
                    {
                        **course,
                        "activities": [],
                        "assignments": [],
                        "lessons": [],
                        "announcements": [],
                        "pending_count": 0,
                        "deadlines": [],
                    }
                    for course in courses
                ]
                partial = {
                    "schema": CACHE_VERSION,
                    "configured": True,
                    "region": self.region,
                    "region_name": REGION_NAMES.get(self.region, self.region),
                    "account": account,
                    "last_sync": None,
                    "last_error": None,
                    "syncing": True,
                    "courses": clean_courses,
                    "assignments": [],
                }
                self._save_cache(partial)

                semaphore = asyncio.Semaphore(8)
                max_term = max((c.get("term", 0) for c in courses), default=0)
                now_ms = int(time.time() * 1000)

                def classify_assignment(item: dict) -> dict:
                    done = (
                        item.get("finished") is True
                        or item.get("status") in (2, 3)
                        or item.get("progress") == 1
                        or item.get("score") is not None
                    )
                    deadline = int(item.get("deadline") or 0)
                    expired = deadline > 0 and deadline < now_ms
                    pending = deadline > now_ms and not done
                    return {
                        **item,
                        "finished": done,
                        "expired": expired,
                        "pending": pending,
                    }

                def aggregate() -> list[dict]:
                    rows = []
                    for course in clean_courses:
                        for item in course["assignments"]:
                            rows.append(
                                {
                                    **item,
                                    "course_name": course["name"],
                                    "classroom_id": course["classroom_id"],
                                }
                            )
                    rows.sort(key=lambda x: x.get("create_time") or 0, reverse=True)
                    return rows

                async def enrich(index: int) -> None:
                    course = clean_courses[index]
                    async with semaphore:
                        result = dict(course)
                        try:
                            activities = await client.list_activities(
                                course["classroom_id"]
                            )
                        except Exception as exc:
                            activities = []
                            result["activity_error"] = str(exc)
                        result["activities"] = activities
                        result["assignments"] = [
                            classify_assignment(a) for a in activities if a["type"] in (5, 19)
                        ]
                        result["lessons"] = [a for a in activities if a["type"] == 14]
                        result["announcements"] = [
                            a for a in activities if a["type"] == 9
                        ]
                        result["pending_count"] = sum(
                            1 for a in result["assignments"] if a["pending"]
                        )
                        # Progress is the slowest endpoint. Fetch it only for
                        # the current term; old terms remain browsable.
                        if course.get("term") == max_term:
                            try:
                                leaves = await client.get_progress(
                                    course["classroom_id"], course["course_id"]
                                )
                            except Exception:
                                leaves = []
                            result["deadlines"] = [
                                leaf
                                for leaf in leaves
                                if leaf["leaf_type"] in (5, 6, 19)
                                and leaf["deadline"] > 0
                            ]
                        clean_courses[index] = result
                        self._save_cache(
                            {
                                **partial,
                                "courses": clean_courses,
                                "assignments": aggregate(),
                            }
                        )

                await asyncio.gather(
                    *(enrich(i) for i in range(len(clean_courses))),
                    return_exceptions=True,
                )

                data = {
                    "schema": CACHE_VERSION,
                    "configured": True,
                    "region": self.region,
                    "region_name": REGION_NAMES.get(self.region, self.region),
                    "account": account,
                    "last_sync": _now_iso(),
                    "last_error": None,
                    "syncing": False,
                    "courses": clean_courses,
                    "assignments": aggregate(),
                }
                self._save_cache(data)
                self._last_error = None
                return data
            except Exception as exc:
                self._last_error = str(exc)
                if self._cache:
                    self._cache["last_error"] = str(exc)
                    self._cache["syncing"] = False
                    self._save_cache(self._cache)
                    return self._cache
                return {
                    "configured": True,
                    "region": self.region,
                    "region_name": REGION_NAMES.get(self.region, self.region),
                    "account": None,
                    "last_sync": None,
                    "last_error": str(exc),
                    "syncing": False,
                    "courses": [],
                    "assignments": [],
                }

    # ── courseware ──────────────────────────────────────────
    def _courseware_cache_path(self, lesson_id: str) -> Path:
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", lesson_id)[:120]
        return COURSEWARE_DIR / f"{safe}.json"

    async def get_courseware(self, lesson_id: str, force: bool = False) -> dict:
        session = self.get_session()
        if not session:
            raise YktError("尚未配置雨课堂 sessionid", status_code=400)
        lesson_id = (lesson_id or "").strip()
        if not lesson_id:
            raise YktError("缺少 lesson_id", status_code=400)

        if not force and lesson_id in self._courseware:
            return self._courseware[lesson_id]
        path = self._courseware_cache_path(lesson_id)
        if not force and path.exists():
            try:
                cached = json.loads(path.read_text(encoding="utf-8"))
                if cached.get("lesson_id") == lesson_id:
                    self._courseware[lesson_id] = cached
                    return cached
            except Exception:
                pass

        client = YktClient(session, self.region)
        info = await client.get_lesson_info(lesson_id)
        summary = await client.get_lesson_summary(lesson_id)
        presentations = summary.get("presentations") or []
        if not presentations and info.get("presentation_ids"):
            presentations = [
                {"id": pid, "title": info.get("title", ""), "cover": "", "slides_count": 0}
                for pid in info["presentation_ids"]
            ]

        result = {
            "lesson_id": lesson_id,
            "title": info.get("title") or summary.get("title") or "",
            "course_name": info.get("course_name", ""),
            "teacher": info.get("teacher", ""),
            "presentations": [],
            "fetched_at": _now_iso(),
        }
        for presentation in presentations[:8]:
            slides = await client.list_slides(
                presentation.get("id", ""), lesson_id
            )
            result["presentations"].append(
                {
                    **presentation,
                    "slides": slides,
                }
            )
        _write_private(path, json.dumps(result, ensure_ascii=False))
        self._courseware[lesson_id] = result
        return result

    # ── PDF export ──────────────────────────────────────────
    def _pdf_path(self, lesson_id: str) -> Path:
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", lesson_id)[:120]
        return PDF_DIR / f"{safe}.pdf"

    async def get_courseware_pdf(self, lesson_id: str, force: bool = False) -> Path:
        data = await self.get_courseware(lesson_id, force=False)
        path = self._pdf_path(lesson_id)
        if path.exists() and not force:
            return path

        urls = [
            slide.get("image")
            for presentation in data.get("presentations", [])
            for slide in presentation.get("slides", [])
            if slide.get("image")
        ]
        if not urls:
            raise YktError("该节课没有可导出的课件图片", status_code=400)

        http = await get_http_client()
        semaphore = asyncio.Semaphore(6)

        async def fetch_image(url: str) -> Image.Image | None:
            async with semaphore:
                try:
                    response = await http.get(url, timeout=20.0)
                    if response.status_code != 200:
                        return None
                    image = Image.open(io.BytesIO(response.content)).convert("RGB")
                    return image.copy()
                except (Exception, UnidentifiedImageError):
                    return None

        images = await asyncio.gather(*(fetch_image(url) for url in urls))
        pages = [image for image in images if image is not None]
        if not pages:
            raise YktError("课件图片下载失败，无法导出 PDF", status_code=502)
        buffer = io.BytesIO()
        pages[0].save(
            buffer,
            format="PDF",
            save_all=True,
            append_images=pages[1:],
            resolution=100.0,
        )
        _write_private_bytes(path, buffer.getvalue())
        return path

    # ── periodic ────────────────────────────────────────────
    async def refresh_loop(self) -> None:
        interval = max(60, settings.ykt_refresh_minutes * 60)
        while True:
            try:
                if self.get_session():
                    await self.get_overview(force=True)
            except asyncio.CancelledError:
                raise
            except Exception as exc:
                self._last_error = str(exc)
            await asyncio.sleep(interval)

    def start(self) -> None:
        if self._task is None or self._task.done():
            self._task = asyncio.create_task(self.refresh_loop())

    async def stop(self) -> None:
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
            self._task = None


ykt_service = YuketangService()
