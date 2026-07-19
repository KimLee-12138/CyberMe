"""CLI utilities for CyberMe OS management."""

import asyncio
import secrets

import click

from app.core.config import settings
from app.core.database import async_session_factory, engine
from app.models import *  # noqa


@click.group()
def cli():
    """CyberMe OS — 管理命令行工具"""
    pass


@cli.command()
@click.option("--username", prompt=True, help="管理员用户名")
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True, help="管理员密码")
def create_admin(username: str, password: str):
    """创建管理员用户."""
    asyncio.run(_create_admin(username, password))


async def _create_admin(username: str, password: str):
    from pwdlib import PasswordHash
    from pwdlib.hashers.argon2 import Argon2Hasher
    from sqlalchemy import select

    from app.models.user import User

    pw_hash_obj = PasswordHash([Argon2Hasher()])
    password_hash = pw_hash_obj.hash(password)

    async with async_session_factory() as session:
        existing = await session.execute(
            select(User).where(User.username == username)
        )
        if existing.scalar_one_or_none():
            click.echo(f"错误：用户名 '{username}' 已存在。")
            return

        import uuid

        user = User(
            id=str(uuid.uuid4()),
            username=username,
            password_hash=password_hash,
            is_active=True,
        )
        session.add(user)
        await session.commit()

        click.echo(f"管理员 '{username}' 创建成功！")
        click.echo("请妥善保管密码和后续配置的 TOTP 恢复码。")


@cli.command()
def check_db():
    """检查数据库连接状态."""
    asyncio.run(_check_db())


async def _check_db():
    from sqlalchemy import text

    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            await result.fetchone()
        click.echo("数据库连接: OK")
    except Exception as e:
        click.echo(f"数据库连接失败: {e}")

    try:
        import redis.asyncio as aioredis

        r = aioredis.from_url(settings.redis_url)
        await r.ping()
        await r.close()
        click.echo("Redis 连接: OK")
    except Exception as e:
        click.echo(f"Redis 连接失败: {e}")


if __name__ == "__main__":
    cli()
