"""Decision Lab — four-role analysis orchestration."""

import uuid
from datetime import datetime, timezone

from app.model_gateway.gateway import generate as gateway_generate
from app.model_gateway.schemas import ModelMessage


_decisions: dict[str, dict] = {}


ROLES = [
    {
        "key": "past_self",
        "label": "历史上的我",
        "icon": "📜",
        "system_prompt": (
            "你代表用户过去的决策偏好和经验。基于已有的决策日志和行动记录，"
            "分析这个决策与过去行为的一致性。"
            "注意：不要用事后结果改写理由。只基于当时已知的信息。"
        ),
    },
    {
        "key": "present_self",
        "label": "现在的我",
        "icon": "🎯",
        "system_prompt": (
            "你代表用户当前的目标、状态和明确偏好。"
            "分析这个决策是否符合当前的学习/工作目标。"
            "明确指出哪些因素是当前的优先考量。"
            "注意标记你的分析中哪些是明确的(explicit)，哪些是推断的(inferred)。"
        ),
    },
    {
        "key": "opponent",
        "label": "反对者",
        "icon": "⚔️",
        "system_prompt": (
            "你是一个刻意唱反调的反对者。你的职责：\n"
            "1. 寻找惯性思维——用户可能陷入的思维定式\n"
            "2. 发现遗漏——有什么重要因素被忽略了\n"
            "3. 提出反例——什么情况下这个决定会出问题\n"
            "4. 挑战假设——决策背后的隐含假设是否成立\n"
            "不要为了反对而反对，要提出有质量的异议。"
        ),
    },
    {
        "key": "auditor",
        "label": "证据审计者",
        "icon": "🔍",
        "system_prompt": (
            "你是一位严格的证据审计者。分析决策中涉及的陈述：\n"
            "1. 哪些陈述有事实依据（标注 [证据]）\n"
            "2. 哪些是主观判断（标注 [判断]）\n"
            "3. 哪些缺乏依据（标注 [无依据]）\n"
            "4. 如果有事实错误，明确指出（标注 [事实错误]）\n"
            "不要发表观点，只做事实核查。"
        ),
    },
]


async def analyze(db, topic: str, context: str = "") -> dict:
    """Run four-role analysis on a decision topic."""
    decision_id = str(uuid.uuid4())
    analyses = []

    for role in ROLES:
        messages = [
            ModelMessage(role="system", content=role["system_prompt"]),
            ModelMessage(role="user", content=(
                f"决策题目：{topic}\n\n"
                + (f"背景信息：{context}\n\n" if context else "")
                + f"请以「{role['label']}」的视角分析这个决策。"
            )),
        ]

        try:
            # Alternate providers to avoid rate limits and get diverse perspectives
            route = "evidence_qa.fast" if role["key"] in ("past_self", "opponent") else "evidence_qa.default"
            response = await gateway_generate(route=route, messages=messages)
            analyses.append({
                "role": role["key"],
                "label": role["label"],
                "icon": role["icon"],
                "content": response.content,
            })
        except Exception as e:
            analyses.append({
                "role": role["key"],
                "label": role["label"],
                "icon": role["icon"],
                "content": f"分析生成失败：{e}",
            })

    decision = {
        "id": decision_id,
        "topic": topic,
        "context": context,
        "analyses": analyses,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _decisions[decision_id] = decision
    return decision


def get_decisions() -> list:
    return sorted(_decisions.values(), key=lambda d: d["created_at"], reverse=True)


def get_decision(decision_id: str) -> dict | None:
    return _decisions.get(decision_id)
