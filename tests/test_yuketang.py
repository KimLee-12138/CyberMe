"""Offline tests for the read-only Yuketang adapter (no network/session)."""

from __future__ import annotations

from pathlib import Path
import time

import pytest

from app.integrations.yuketang import service as service_mod


class FakeClient:
    def __init__(self, sessionid: str, region: str):
        self.sessionid = sessionid
        self.region = region

    async def verify(self):
        return {"name": "测试同学", "school": "测试大学", "user_id": "u1"}

    async def list_courses(self):
        return [
            {
                "classroom_id": "c1",
                "course_id": "course1",
                "name": "数据库",
                "class_name": "数据库-1班",
                "teacher": "张老师",
                "term": 202601,
            }
        ]

    async def list_activities(self, classroom_id: str):
        return [
            {
                "id": "a1",
                "type": 19,
                "type_name": "章节作业",
                "title": "第三章作业",
                "courseware_id": "",
                "create_time": 1_700_000_000_000,
                "deadline": int(time.time() * 1000) + 86_400_000,
                "status": 1,
                "unfinished": 1,
                "progress": 0,
                "score": None,
                "finished": False,
            },
            {
                "id": "a2",
                "type": 14,
                "type_name": "上课记录",
                "title": "第一节课",
                "courseware_id": "lesson1",
                "create_time": 1_700_000_000_000,
                "deadline": 0,
                "status": 2,
                "unfinished": 0,
                "progress": 1,
                "score": None,
                "finished": True,
            },
            {
                "id": "a3",
                "type": 9,
                "type_name": "公告",
                "title": "课程公告",
                "courseware_id": "",
                "create_time": 1_700_000_000_000,
                "deadline": 0,
                "status": 2,
                "unfinished": 0,
                "progress": 1,
                "score": None,
                "finished": True,
            },
        ]

    async def get_progress(self, classroom_id: str, course_id: str):
        return [
            {
                "name": "第三章作业",
                "leaf_id": "l1",
                "leaf_type": 19,
                "status": "undone",
                "deadline": 1_800_000_000_000,
            }
        ]

    async def get_lesson_info(self, lesson_id: str):
        return {
            "lesson_id": lesson_id,
            "title": "第一节课",
            "course_name": "数据库",
            "classroom_name": "数据库-1班",
            "teacher": "张老师",
            "presentation_ids": ["p1"],
        }

    async def get_lesson_summary(self, lesson_id: str):
        return {
            "title": "第一节课",
            "presentations": [
                {
                    "id": "p1",
                    "title": "第一章",
                    "cover": "https://cdn.example/p1.jpg",
                    "slides_count": 2,
                }
            ],
        }

    async def list_slides(self, presentation_id: str, lesson_id: str):
        return [
            {"index": 1, "image": "https://cdn.example/s1.jpg"},
            {"index": 2, "image": "https://cdn.example/s2.jpg"},
        ]


@pytest.fixture()
def ykt(tmp_path: Path, monkeypatch):
    monkeypatch.setattr(service_mod, "DATA_DIR", tmp_path)
    monkeypatch.setattr(service_mod, "CACHE_FILE", tmp_path / "cache.json")
    monkeypatch.setattr(service_mod, "SESSION_FILE", tmp_path / "session.enc")
    monkeypatch.setattr(service_mod, "COURSEWARE_DIR", tmp_path / "courseware")
    monkeypatch.setattr(service_mod, "YktClient", FakeClient)
    svc = service_mod.YuketangService()
    svc._session = "test-session-123"
    return svc


@pytest.mark.asyncio
async def test_overview_groups_assignments_and_lessons(ykt):
    data = await ykt.get_overview(force=True)
    assert data["configured"] is True
    assert data["account"]["name"] == "测试同学"
    assert len(data["courses"]) == 1
    assert len(data["assignments"]) == 1
    assert data["assignments"][0]["course_name"] == "数据库"
    assert data["assignments"][0]["finished"] is False
    assert data["courses"][0]["pending_count"] == 1
    assert data["courses"][0]["lessons"][0]["courseware_id"] == "lesson1"
    assert data["courses"][0]["deadlines"][0]["leaf_id"] == "l1"


@pytest.mark.asyncio
async def test_courseware_returns_slides_and_caches(ykt):
    data = await ykt.get_courseware("lesson1")
    assert data["title"] == "第一节课"
    assert data["presentations"][0]["slides"][1]["image"].endswith("s2.jpg")
    assert (service_mod.COURSEWARE_DIR / "lesson1.json").exists()
