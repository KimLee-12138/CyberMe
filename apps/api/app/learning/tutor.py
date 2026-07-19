"""Adaptive Tutor — 6 learning modes with session management."""

import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from app.model_gateway.gateway import generate as gateway_generate
from app.model_gateway.schemas import ModelMessage
from app.retrieval.engine import hybrid_search

# ── In-memory session store ─────────────────────────────

_sessions: dict[str, dict] = {}


def _new_session(mode: str, topic: str) -> dict:
    sid = str(uuid.uuid4())
    s = {
        "id": sid,
        "mode": mode,
        "topic": topic,
        "history": [],
        "state": {},
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _sessions[sid] = s
    return s


# ── Model messages helper ───────────────────────────────

def _msg(role: str, content: str) -> ModelMessage:
    return ModelMessage(role=role, content=content)


async def _search(db: AsyncSession, topic: str, top_k: int = 8) -> dict:
    return await hybrid_search(db, topic, top_k=top_k)


async def _generate(route: str, messages: list[ModelMessage], evidence: dict | None = None) -> str:
    resp = await gateway_generate(route=route, messages=messages, evidence=evidence)
    return resp.content


# ── Mode 1: 概念讲解 ─────────────────────────────────────

async def start_concept_explanation(
    db: AsyncSession, topic: str
) -> dict:
    evidence = await _search(db, topic, top_k=8)
    session = _new_session("concept", topic)
    session["state"]["evidence"] = evidence

    messages = [
        _msg("system",
            "你是一位耐心的个人导师。请按以下结构讲解概念：\n"
            "1. **一句话总结**\n"
            "2. **核心原理**\n"
            "3. **关键公式/规则**（如有）\n"
            "4. **具体例子**\n"
            "5. **容易出错的地方**\n\n"
            "讲解结束后，可以问一个检查理解的问题。"
        ),
        _msg("user", f"请讲解：{topic}"),
    ]

    answer = await _generate("tutor.concept", messages, evidence)
    session["history"].append({"role": "assistant", "content": answer})
    return {"session_id": session["id"], "mode": "concept", "content": answer, "complete": True}


# ── Mode 2: 苏格拉底追问 ────────────────────────────────

async def start_socratic(db: AsyncSession, topic: str) -> dict:
    evidence = await _search(db, topic, top_k=5)
    session = _new_session("socratic", topic)
    session["state"]["evidence"] = evidence
    session["state"]["round"] = 0

    messages = [
        _msg("system",
            "你是苏格拉底式导师。规则：\n"
            "1. 每次只问一个问题\n"
            "2. 根据学生的回答追问，引导深入思考\n"
            "3. 不要直接给出答案\n"
            "4. 3-5 轮后给出总结\n"
            "5. 如果学生回答正确，追问更深层的问题"
        ),
        _msg("user", f"我想学习：{topic}。请开始问我问题。"),
    ]

    response = await _generate("tutor.socratic", messages, evidence)
    session["history"].append({"role": "assistant", "content": response})
    return {"session_id": session["id"], "mode": "socratic", "content": response, "complete": False}


async def continue_socratic(session: dict, answer: str) -> dict:
    session["state"]["round"] = session["state"].get("round", 0) + 1
    round_num = session["state"]["round"]
    evidence = session["state"].get("evidence")

    messages = [
        _msg("system",
            "你是苏格拉底式导师。每次只问一个问题。"
            f"这是第 {round_num} 轮。"
            + ("如果已超过 3 轮，是时候给出总结了。" if round_num >= 3 else "")
        ),
    ]
    for h in session["history"]:
        messages.append(_msg(h["role"], h["content"]))
    messages.append(_msg("user", answer))

    response = await _generate("tutor.socratic", messages, evidence)
    session["history"].append(_msg("user", answer))
    session["history"].append(_msg("assistant", response))

    # Check if this is a summary/conclusion
    done = round_num >= 4
    return {"session_id": session["id"], "mode": "socratic", "content": response, "complete": done}


# ── Mode 3: 闭卷回忆 ─────────────────────────────────────

async def start_closed_book(db: AsyncSession, topic: str) -> dict:
    evidence = await _search(db, topic, top_k=5)
    session = _new_session("closed_book", topic)
    session["state"]["evidence"] = evidence

    messages = [
        _msg("system",
            "生成一个考察记忆的问题（不含答案）。"
            "问题应该要求学生回忆关键概念、公式或原理。"
            "同时请生成标准答案，格式为：\n"
            "---QUESTION---\n(问题内容)\n---ANSWER---\n(标准答案)"
        ),
        _msg("user", f"为知识点「{topic}」生成闭卷回忆问题"),
    ]

    response = await _generate("tutor.closed_book", messages, evidence)
    # Split question and answer
    parts = response.split("---ANSWER---")
    question = parts[0].replace("---QUESTION---", "").strip() if parts else response
    correct_answer = parts[1].strip() if len(parts) > 1 else ""

    session["state"]["question"] = question
    session["state"]["correct_answer"] = correct_answer
    session["history"].append({"role": "assistant", "content": question})

    return {
        "session_id": session["id"],
        "mode": "closed_book",
        "content": question,
        "complete": False,
    }


async def check_closed_book(session: dict, answer: str) -> dict:
    correct_answer = session["state"].get("correct_answer", "")

    messages = [
        _msg("system",
            "对比学生的回答和标准答案。指出遗漏、错误和亮点。用友好的语气。"
            "最后给出一个 1-10 的掌握度评分。"
        ),
        _msg("user",
            f"知识点：{session['topic']}\n\n"
            f"标准答案：\n{correct_answer}\n\n"
            f"学生的回答：\n{answer}"
        ),
    ]

    feedback = await _generate("tutor.closed_book", messages)

    return {
        "session_id": session["id"],
        "mode": "closed_book",
        "content": feedback,
        "correct_answer": correct_answer,
        "complete": True,
    }


# ── Mode 4: 分步做题 ─────────────────────────────────────

async def start_step_by_step(db: AsyncSession, topic: str) -> dict:
    evidence = await _search(db, topic, top_k=5)
    session = _new_session("step_by_step", topic)
    session["state"]["evidence"] = evidence
    session["state"]["steps_completed"] = 0

    messages = [
        _msg("system",
            "你是一位解题导师。请为以下知识点生成一道练习题，分 3 步引导学生解答。\n"
            "格式：\n"
            "---STEPS---\n"
            "步骤1: (第一步题目)\n"
            "步骤2: (第二步题目)\n"
            "步骤3: (第三步题目)\n"
            "---ANSWER---\n"
            "步骤1答案: (答案)\n"
            "步骤2答案: (答案)\n"
            "步骤3答案: (答案)\n"
            "现在请只输出步骤1的题目，不要输出答案。"
        ),
        _msg("user", f"为「{topic}」生成分步练习题"),
    ]

    response = await _generate("tutor.step_by_step", messages, evidence)

    # Parse steps
    steps_answer = response.split("---ANSWER---")
    steps_text = steps_answer[0].replace("---STEPS---", "").strip() if steps_answer else response
    answers_text = steps_answer[1].strip() if len(steps_answer) > 1 else ""

    # Extract step 1 question
    lines = steps_text.split("\n")
    step1 = ""
    step2 = ""
    step3 = ""
    current = ""
    for line in lines:
        if "步骤1" in line:
            current = "step1"
        elif "步骤2" in line:
            current = "step2"
        elif "步骤3" in line:
            current = "step3"
        elif current == "step1":
            step1 += line + "\n"
        elif current == "step2":
            step2 += line + "\n"
        elif current == "step3":
            step3 += line + "\n"

    session["state"]["steps"] = {"step1": step1.strip(), "step2": step2.strip(), "step3": step3.strip()}
    session["state"]["answers"] = answers_text
    session["state"]["current_step"] = "step1"

    return {
        "session_id": session["id"],
        "mode": "step_by_step",
        "content": step1.strip() or "第1步：请开始解题",
        "step": 1,
        "complete": False,
    }


async def continue_step(session: dict, answer: str) -> dict:
    step_map = {"step1": "步骤1", "step2": "步骤2", "step3": "步骤3"}
    current = session["state"]["current_step"]
    answers = session["state"].get("answers", "")

    # Check this step
    messages = [
        _msg("system",
            f"判断学生对{step_map[current]}的回答是否正确。如果错误，给简短提示。"
            "不要直接给出正确答案，而是引导思考。"
        ),
        _msg("user", f"{step_map[current]}参考答案：\n{answers}\n\n学生回答：\n{answer}"),
    ]

    feedback = await _generate("tutor.step_by_step", messages)

    # Move to next step
    steps = session["state"]["steps"]
    if current == "step1":
        next_step = "step2"
    elif current == "step2":
        next_step = "step3"
    else:
        # All done
        return {
            "session_id": session["id"],
            "mode": "step_by_step",
            "content": feedback + "\n\n🎉 所有步骤完成！做得很好。",
            "complete": True,
        }

    session["state"]["current_step"] = next_step
    next_content = steps.get(next_step, "下一步")

    return {
        "session_id": session["id"],
        "mode": "step_by_step",
        "content": feedback + "\n\n---\n\n" + next_content,
        "step": 2 if next_step == "step2" else 3,
        "complete": False,
    }


# ── Mode 5: 模拟考试 ─────────────────────────────────────

async def start_mock_exam(db: AsyncSession, topic: str, num: int = 3) -> dict:
    evidence = await _search(db, topic, top_k=8)
    session = _new_session("mock_exam", topic)
    session["state"]["evidence"] = evidence
    session["state"]["num_questions"] = num
    session["state"]["started_at"] = datetime.now(timezone.utc).isoformat()

    messages = [
        _msg("system",
            f"生成 {num} 道关于指定知识点的考试题。\n"
            "每道题包含：题目、题型（简答/判断/选择）。\n"
            "用 --- 分隔每道题。\n"
            "最后用 ---ANSWERS--- 分隔，列出每题的标准答案。"
        ),
        _msg("user", f"为「{topic}」生成 {num} 道考试题"),
    ]

    response = await _generate("tutor.mock_exam", messages, evidence)

    parts = response.split("---ANSWERS---")
    questions_text = parts[0].strip() if parts else response
    answers_text = parts[1].strip() if len(parts) > 1 else ""

    session["state"]["questions"] = questions_text
    session["state"]["answers"] = answers_text

    return {
        "session_id": session["id"],
        "mode": "mock_exam",
        "content": questions_text,
        "num_questions": num,
        "complete": False,
    }


async def submit_exam(session: dict, user_answers: str) -> dict:
    correct = session["state"].get("answers", "")

    messages = [
        _msg("system",
            "批改考试。按题号逐题评分，给出总分和评语。格式：\n"
            "每题：✅/❌ + 简短说明\n"
            "最后：总分 X/{n} + 总结"
        ),
        _msg("user",
            f"题目：\n{session['state']['questions']}\n\n"
            f"标准答案：\n{correct}\n\n"
            f"学生作答：\n{user_answers}"
        ),
    ]

    feedback = await _generate("tutor.mock_exam", messages)

    return {
        "session_id": session["id"],
        "mode": "mock_exam",
        "content": feedback,
        "complete": True,
    }


# ── Mode 6: 错题复训 ─────────────────────────────────────

async def start_mistake_retrain(db: AsyncSession, topic: str) -> dict:
    evidence = await _search(db, topic, top_k=5)
    session = _new_session("mistake_retrain", topic)
    session["state"]["evidence"] = evidence

    messages = [
        _msg("system",
            "基于指定知识点，生成 3 道变体练习题。\n"
            "要求：\n"
            "1. 每道题考察概念的不同角度\n"
            "2. 难度递进\n"
            "3. 避免与标准例题完全重复\n"
            "4. 包含一道易错陷阱题\n"
            "用 ---ANSWERS--- 分隔题目和答案。"
        ),
        _msg("user", f"为「{topic}」生成错题复训练习题"),
    ]

    response = await _generate("tutor.mistake_retrain", messages, evidence)

    parts = response.split("---ANSWERS---")
    questions = parts[0].strip() if parts else response
    answers = parts[1].strip() if len(parts) > 1 else ""

    session["state"]["questions"] = questions
    session["state"]["answers"] = answers

    return {
        "session_id": session["id"],
        "mode": "mistake_retrain",
        "content": questions,
        "complete": False,
    }
