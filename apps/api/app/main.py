"""CyberMe OS — FastAPI Application."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.auth.router import router as auth_router
from app.chat.router import router as chat_router
from app.core.config import settings
from app.core.database import engine
from app.core.security import (
    RateLimitMiddleware,
    SecurityHeadersMiddleware,
)
from app.sync.router import router as sync_router
from app.knowledge.router import router as knowledge_router
from app.learning.router import router as learning_router
from app.projects.router import router as projects_router
from app.self_model.router import router as self_model_router
from app.evaluation.router import router as evaluation_router
from app.writeback.router import router as writeback_router
from app.github_proxy.router import router as github_router
from app.distill_router import router as distill_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown
    await engine.dispose()


app = FastAPI(
    title="CyberMe OS API",
    description="CyberMe 个人学习操作系统 — 后端 API",
    version="0.1.0",
    docs_url="/docs" if settings.is_development else None,
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security: Rate limiting (100 req/min per IP)
app.add_middleware(RateLimitMiddleware)

# Security: Response headers (CSP, X-Frame-Options, etc.)
app.add_middleware(SecurityHeadersMiddleware)

# Register routers
app.include_router(auth_router)
app.include_router(sync_router)
app.include_router(knowledge_router)
app.include_router(chat_router)
app.include_router(learning_router)
app.include_router(projects_router)
app.include_router(self_model_router)
app.include_router(evaluation_router)
app.include_router(writeback_router)
app.include_router(github_router)
app.include_router(distill_router)


@app.get("/health/live")
async def health_live():
    return {"status": "ok"}


@app.get("/health/ready")
async def health_ready():
    db_status = "disconnected"
    redis_status = "disconnected"

    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"

    try:
        import redis.asyncio as aioredis
        r = aioredis.from_url(settings.redis_url)
        await r.ping()
        await r.close()
        redis_status = "connected"
    except Exception:
        redis_status = "disconnected"

    overall = "ok" if db_status == "connected" else "degraded"
    return {
        "status": overall,
        "database": db_status,
        "redis": redis_status,
    }


@app.get("/api/v1/status")
async def api_status():
    return {
        "version": "0.1.0",
        "status": "running",
    }
