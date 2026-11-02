# -*- coding: utf-8 -*-
"""Create the local demo user (idempotent).

Usage:
  python tools/seed_demo_user.py
  $env:DEMO_PASSWORD='...'; python tools/seed_demo_user.py
"""
from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "apps" / "api"))

from sqlalchemy import select  # noqa: E402

from app.auth.password import hash_password  # noqa: E402
from app.core.database import async_session_factory  # noqa: E402
from app.models.user import User  # noqa: E402


async def main() -> None:
    username = os.environ.get("DEMO_USERNAME", "demo")
    password = os.environ.get("DEMO_PASSWORD", "cyberme2026")

    async with async_session_factory() as db:
        existing = (await db.execute(select(User).where(User.username == username))).scalar_one_or_none()
        if existing:
            print(f"user already exists: {username}")
            return
        user = User(
            username=username,
            password_hash=hash_password(password),
            timezone="Asia/Shanghai",
            locale="zh-CN",
        )
        db.add(user)
        await db.commit()
        print(f"created demo user: {username}")


if __name__ == "__main__":
    asyncio.run(main())
