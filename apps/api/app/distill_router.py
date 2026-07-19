"""知识蒸馏 API — AI 将提取资料转化为正式知识点。支持单篇和批量 SSE 流式。"""

import asyncio
import json
import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import current_user
from app.core.database import get_db
from app.model_gateway.gateway import generate
from app.model_gateway.schemas import ModelMessage
from app.models.user import User

router = APIRouter(prefix="/api/v1/distill")

# ── Schemas ──────────────────────────────────────────────

class DistillRequest(BaseModel):
    course_code: str = Field(..., max_length=20)
    extract_id: str | None = None
    max_extracts: int = Field(default=3, ge=1, le=10)

# ── Prompt ───────────────────────────────────────────────

SYSTEM_PROMPT = """你是一个知识蒸馏专家。将粗糙的课程提取资料转化为结构化的正式知识笔记。

要求：
1. 输出完整 Markdown，包含 frontmatter (id/type/status/course/mastery/importance)
2. 结构：一句话总结 → 核心概念详解 → 关键公式/定理 → 例题 → 易错点 → 相关链接
3. LaTeX 写数学公式，中文
4. 内容详实：至少 800 字，有具体公式、定义、例子
5. type=concept, status=active, mastery=learning
6. 只输出 Markdown 正文，不要前导解释或后置评价"""

# ── Single distill ───────────────────────────────────────

@router.post("/extract-to-knowledge")
async def distill_single(
    body: DistillRequest,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """蒸馏单篇或少量提取资料。"""
    if body.extract_id:
        result = await db.execute(
            text("SELECT id, title, markdown_body, relative_path FROM vault_documents WHERE id=:id AND course_code=:cc AND document_type='extract' AND deleted_at IS NULL"),
            {"id": body.extract_id, "cc": body.course_code})
    else:
        result = await db.execute(
            text("SELECT id, title, markdown_body, relative_path FROM vault_documents WHERE course_code=:cc AND document_type='extract' AND deleted_at IS NULL ORDER BY length(markdown_body) DESC LIMIT :lim"),
            {"cc": body.course_code, "lim": body.max_extracts})

    extracts = result.fetchall()
    if not extracts:
        raise HTTPException(status_code=404, detail="未找到提取资料")

    results = []
    for ext in extracts:
        eid, title, content, path = ext
        if not content or len(content) < 100:
            continue
        user_prompt = f"请蒸馏以下课程资料。\n课程: {body.course_code}\n标题: {title or path}\n\n---资料---\n{content[:6000]}"
        try:
            resp = await generate(
                route="distill.knowledge_fb",
                messages=[ModelMessage(role="system", content=SYSTEM_PROMPT), ModelMessage(role="user", content=user_prompt)])
            generated = resp.content
        except Exception as e:
            generated = f"蒸馏失败: {e}"

        doc_title = title or "蒸馏知识点"
        if generated.startswith("---"):
            end = generated.find("---", 3)
            if end > 0:
                for line in generated[3:end].split("\n"):
                    if "title:" in line:
                        doc_title = line.split(":", 1)[1].strip()

        doc_id = str(uuid.uuid4())
        new_path = path.replace("90_课程提取资料", "02_知识点").replace("_提取版", "")
        await db.execute(text("""INSERT INTO vault_documents (id, vault_id, relative_path, title, course_code, document_type, markdown_body, status, created_at, updated_at)
            VALUES (:id, (SELECT vault_id FROM vault_documents WHERE course_code=:cc LIMIT 1), :p, :t, :cc, 'concept', :b, 'active', NOW(), NOW())"""),
            {"id": doc_id, "cc": body.course_code, "p": new_path, "t": doc_title, "b": generated})
        await db.commit()
        results.append({"extract_id": eid, "doc_id": doc_id, "title": doc_title, "path": new_path, "preview": generated[:200], "chars": len(generated)})

    return {"distilled": len(results), "results": results}


# ── Batch SSE streaming ──────────────────────────────────

@router.get("/batch")
async def distill_batch(
    course_code: str = Query(...),
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """SSE 流式批量蒸馏：一键处理整门课的所有提取资料。"""

    async def event_stream():
        try:
            async with async_session_factory() as s:
                r = await s.execute(text(
                    "SELECT id, title, markdown_body, relative_path FROM vault_documents WHERE course_code=:cc AND document_type='extract' AND deleted_at IS NULL ORDER BY length(markdown_body) DESC"),
                    {"cc": course_code})
                extracts = r.fetchall()

                if not extracts:
                    yield f"data: {json.dumps({'type': 'error', 'message': '未找到提取资料'})}\n\n"
                    return

                total = len(extracts)
                yield f"data: {json.dumps({'type': 'start', 'total': total})}\n\n"

                processed = 0
                for ext in extracts:
                    eid, title, content, path = ext
                    if not content or len(content) < 100:
                        yield f"data: {json.dumps({'type': 'skip', 'title': title or path, 'reason': '内容过短'})}\n\n"
                        processed += 1
                        continue

                    user_prompt = f"请蒸馏以下课程资料。\n课程: {course_code}\n标题: {title or path}\n\n---资料---\n{content[:6000]}"
                    try:
                        resp = await generate(
                            route="distill.knowledge_fb",
                            messages=[ModelMessage(role="system", content=SYSTEM_PROMPT), ModelMessage(role="user", content=user_prompt)])
                        generated = resp.content
                    except Exception as e:
                        yield f"data: {json.dumps({'type': 'error_item', 'title': title or path, 'error': str(e)})}\n\n"
                        processed += 1
                        continue

                    doc_title = title or "蒸馏知识点"
                    if generated.startswith("---"):
                        end = generated.find("---", 3)
                        if end > 0:
                            for line in generated[3:end].split("\n"):
                                if "title:" in line:
                                    doc_title = line.split(":", 1)[1].strip()

                    doc_id = str(uuid.uuid4())
                    new_path = path.replace("90_课程提取资料", "02_知识点").replace("_提取版", "")
                    await s.execute(text("""INSERT INTO vault_documents (id, vault_id, relative_path, title, course_code, document_type, markdown_body, status, created_at, updated_at)
                        VALUES (:id, (SELECT vault_id FROM vault_documents WHERE course_code=:cc LIMIT 1), :p, :t, :cc, 'concept', :b, 'active', NOW(), NOW())"""),
                        {"id": doc_id, "cc": course_code, "p": new_path, "t": doc_title, "b": generated})
                    await s.commit()

                    processed += 1
                    yield f"data: {json.dumps({'type': 'progress', 'done': processed, 'total': total, 'title': doc_title, 'path': new_path, 'chars': len(generated), 'preview': generated[:150]})}\n\n"

                yield f"data: {json.dumps({'type': 'done', 'total': processed})}\n\n"

        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'message': str(e)})}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")


# ── Pending ──────────────────────────────────────────────

@router.get("/pending/{course_code}")
async def list_pending_extracts(course_code: str, user: User = Depends(current_user), db: AsyncSession = Depends(get_db)):
    r = await db.execute(text("SELECT COUNT(*) FROM vault_documents WHERE course_code=:cc AND document_type='extract' AND deleted_at IS NULL"), {"cc": course_code})
    r2 = await db.execute(text("SELECT COUNT(*) FROM vault_documents WHERE course_code=:cc AND document_type='concept' AND deleted_at IS NULL"), {"cc": course_code})
    r3 = await db.execute(text("SELECT id, title, length(markdown_body) as blen, relative_path FROM vault_documents WHERE course_code=:cc AND document_type='extract' AND deleted_at IS NULL ORDER BY length(markdown_body) DESC LIMIT 20"), {"cc": course_code})
    return {"course_code": course_code, "extract_count": r.scalar(), "concept_count": r2.scalar(),
            "extracts": [{"id": e[0], "title": e[1], "chars": e[2], "path": e[3]} for e in r3.fetchall()]}

# Import here to avoid circular
from app.core.database import async_session_factory
