"""Read-only Changjiang Yuketang (长江雨课堂) client.

The platform has no public API. This uses the same read-only web endpoints
as the browser session. It never signs in, checks in, submits homework, or
performs any write action.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Any

import httpx

REGION_HOSTS = {
    "standard": "www.yuketang.cn",
    "hetang": "pro.yuketang.cn",
    "changjiang": "changjiang.yuketang.cn",
    "huanghe": "huanghe.yuketang.cn",
}

REGION_NAMES = {
    "standard": "雨课堂",
    "hetang": "荷塘雨课堂",
    "changjiang": "长江雨课堂",
    "huanghe": "黄河雨课堂",
}

ACTIVITY_TYPE_NAMES = {
    5: "试卷作业",
    9: "公告",
    14: "上课记录",
    19: "章节作业",
}

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)


class YktError(Exception):
    def __init__(self, message: str, status_code: int = 502):
        super().__init__(message)
        self.status_code = status_code


# Creating httpx.AsyncClient is surprisingly expensive on Windows (SSL
# context + proxy transport). Do it once, off the event loop, and reuse it.
# This is the difference between a responsive API and a blocked event loop
# when a student has dozens of courses.
_http_client: httpx.AsyncClient | None = None
_http_lock = asyncio.Lock()


def _make_http_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(
        timeout=httpx.Timeout(30.0, connect=5.0),
        follow_redirects=True,
    )


async def get_http_client() -> httpx.AsyncClient:
    global _http_client
    if _http_client is None:
        async with _http_lock:
            if _http_client is None:
                _http_client = await asyncio.to_thread(_make_http_client)
    return _http_client


def _s(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float)):
        return str(value)
    return ""


def _n(value: Any) -> int:
    if isinstance(value, (int, float)):
        return int(value)
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _arr(value: Any) -> list:
    return value if isinstance(value, list) else []


def _obj(value: Any) -> dict:
    return value if isinstance(value, dict) else {}


def _unwrap(payload: Any) -> Any:
    if not isinstance(payload, dict):
        raise YktError("雨课堂返回格式异常")
    code = payload.get("code")
    if code not in (0, "0", None):
        raise YktError(f"雨课堂错误：{payload.get('msg') or code}")
    if "errcode" in payload and payload.get("errcode") not in (0, "0"):
        raise YktError(f"雨课堂错误：{payload.get('errmsg') or payload.get('errcode')}")
    if "data" in payload:
        return payload["data"]
    return payload


def _abs_url(value: Any, base: str) -> str:
    url = _s(value)
    if url.startswith("//"):
        return "https:" + url
    if url.startswith("/"):
        return base + url
    return url


@dataclass
class YktClient:
    sessionid: str
    region: str = "changjiang"

    def __post_init__(self) -> None:
        self.sessionid = (self.sessionid or "").strip()
        if len(self.sessionid) < 8 or len(self.sessionid) > 512:
            raise YktError("sessionid 格式不正确")
        if self.region not in REGION_HOSTS:
            raise YktError("不支持的雨课堂区域")

    @property
    def base(self) -> str:
        return f"https://{REGION_HOSTS[self.region]}"

    async def _get(
        self,
        path: str,
        params: dict[str, Any] | None = None,
        timeout: float = 30.0,
    ) -> Any:
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Cookie": f"sessionid={self.sessionid}",
            "User-Agent": UA,
            "Referer": f"{self.base}/web",
            "xtbz": "ykt",
        }
        try:
            client = await get_http_client()
            response = await client.get(
                f"{self.base}{path}",
                params=params,
                headers=headers,
                timeout=httpx.Timeout(timeout, connect=5.0),
            )
        except httpx.HTTPError as exc:
            raise YktError(f"连接雨课堂失败：{exc}", status_code=502) from exc

        if response.status_code != 200:
            raise YktError(
                f"雨课堂 HTTP {response.status_code}",
                status_code=401 if response.status_code in (401, 403) else 502,
            )
        try:
            payload = response.json()
        except ValueError as exc:
            raise YktError("雨课堂返回不是 JSON") from exc
        return _unwrap(payload)

    async def verify(self) -> dict:
        data = await self._get("/api/v3/user/basic-info", timeout=10.0)
        data = _obj(data)
        return {
            "name": _s(data.get("name")),
            "school": _s(data.get("school")),
            "user_id": _s(data.get("user_id") or data.get("userId")),
        }

    async def list_courses(self) -> list[dict]:
        data = _obj(await self._get("/v2/api/web/courses/list", {"identity": 2}))
        courses = []
        for raw in _arr(data.get("list")):
            item = _obj(raw)
            course = _obj(item.get("course"))
            courses.append(
                {
                    "classroom_id": _s(item.get("classroom_id")),
                    "course_id": _s(course.get("id")),
                    "name": _s(course.get("name")) or _s(item.get("name")),
                    "class_name": _s(item.get("name")),
                    "teacher": _s(_obj(item.get("teacher")).get("name")),
                    "term": _n(item.get("term")),
                }
            )
        return [c for c in courses if c["classroom_id"]]

    async def list_activities(
        self, classroom_id: str, page: int = 0, size: int = 100
    ) -> list[dict]:
        data = _obj(
            await self._get(
                f"/v2/api/web/logs/learn/{classroom_id}",
                {"actype": -1, "page": page, "offset": size, "sort": -1},
            )
        )
        result = []
        for raw in _arr(data.get("activities")):
            item = _obj(raw)
            activity_type = _n(item.get("type"))
            result.append(
                {
                    "id": _s(item.get("id")),
                    "type": activity_type,
                    "type_name": ACTIVITY_TYPE_NAMES.get(
                        activity_type, f"类型{activity_type}"
                    ),
                    "title": _s(item.get("title")),
                    "courseware_id": _s(item.get("courseware_id")),
                    "create_time": _n(item.get("create_time")),
                    "deadline": _n(item.get("deadline")),
                    "status": _n(item.get("status")),
                    "unfinished": _n(item.get("unfinished")),
                    "progress": _n(item.get("progress")),
                    "score": item.get("score"),
                    "finished": item.get("is_finished") is True,
                }
            )
        return result

    async def get_progress(self, classroom_id: str, course_id: str) -> list[dict]:
        data = _obj(
            await self._get(
                "/c27/online_courseware/schedule/course/progress/",
                {"classroom_id": classroom_id, "course_id": course_id},
            )
        )
        leaves = []
        for section in _arr(data.get("course_progress")):
            for raw in _arr(_obj(section).get("section_leaf_list")):
                leaf = _obj(raw)
                progress = _obj(leaf.get("progress"))
                leaves.append(
                    {
                        "name": _s(leaf.get("name")),
                        "leaf_id": _s(leaf.get("id")),
                        "leaf_type": _n(leaf.get("leaf_type")),
                        "status": _s(progress.get("status")),
                        "deadline": _n(leaf.get("score_deadline")),
                        "score": progress.get("user_score"),
                        "total_score": progress.get("total_score"),
                    }
                )
        return leaves

    async def get_lesson_info(self, lesson_id: str) -> dict:
        data = _obj(
            await self._get(
                "/api/v3/classroom-report/student/lesson-info",
                {"lesson_id": lesson_id},
            )
        )
        return {
            "lesson_id": _s(data.get("lessonId")) or lesson_id,
            "title": _s(data.get("lessonName")),
            "course_name": _s(data.get("courseName")),
            "classroom_name": _s(data.get("classroomName")),
            "teacher": _s(data.get("teacherName")),
            "presentation_ids": [_s(x) for x in _arr(data.get("presentationIds"))],
        }

    async def get_lesson_summary(self, lesson_id: str) -> dict:
        data = _obj(
            await self._get(
                "/api/v3/lesson-summary/student", {"lesson_id": lesson_id}
            )
        )
        presentations = []
        for raw in _arr(data.get("presentations")):
            item = _obj(raw)
            presentations.append(
                {
                    "id": _s(item.get("id")),
                    "title": _s(item.get("title")),
                    "cover": _abs_url(item.get("cover"), self.base),
                    "slides_count": _n(item.get("slidesCount")),
                }
            )
        return {
            "title": _s(_obj(data.get("lesson")).get("title")),
            "presentations": presentations,
        }

    async def list_slides(self, presentation_id: str, lesson_id: str) -> list[dict]:
        data = _obj(
            await self._get(
                "/api/v3/lesson-summary/student/presentation",
                {"presentation_id": presentation_id, "lesson_id": lesson_id},
            )
        )
        slides = []
        for index, raw in enumerate(_arr(data.get("slides")), start=1):
            item = _obj(raw)
            slides.append(
                {
                    "index": _n(item.get("index")) or index,
                    "image": _abs_url(item.get("cover"), self.base),
                }
            )
        return sorted(slides, key=lambda x: x["index"])

    async def list_announcements(self, classroom_id: str) -> list[dict]:
        data = _obj(
            await self._get(
                "/v/discussion/v2/announcements/",
                {"cid": classroom_id, "limit": 20, "offset": 0, "type": 9},
            )
        )
        return [_obj(x) for x in _arr(data.get("data"))]
