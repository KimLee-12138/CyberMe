"""Writing Studio — AI draft generation + fact auditing."""

from sqlalchemy.ext.asyncio import AsyncSession

from app.model_gateway.gateway import generate as gateway_generate
from app.model_gateway.schemas import ModelMessage
from app.retrieval.engine import hybrid_search


async def generate(
    db: AsyncSession,
    topic: str,
    output_type: str = "report",
    scope: dict | None = None,
) -> dict:
    """Generate a draft document based on personal knowledge base."""

    type_prompts = {
        "report": "实验报告（含目的、方法、结果、讨论）",
        "summary": "学习总结（核心概念、关键公式、个人理解）",
        "essay": "课程论文（论点清晰、论据来自知识库、有引用）",
        "presentation": "PPT 大纲（每页标题 + 3-5 个要点）",
        "resume": "简历项目描述（STAR 法则、量化成果）",
    }

    evidence = await hybrid_search(db, topic, top_k=10, scope=scope)

    messages = [
        ModelMessage(role="system", content=(
            f"你是一位个人写作助手。基于用户知识库中的信息，撰写一份{type_prompts.get(output_type, output_type)}。\n"
            "要求：\n"
            "1. 所有事实性陈述必须引用知识库证据（标注 [证据 N]）\n"
            "2. 如果没有足够证据，用 [待补充] 标记\n"
            "3. 模型通用知识用 [通用知识] 标记\n"
            "4. 输出结构清晰，使用 Markdown 格式"
        )),
        ModelMessage(role="user", content=f"题目：{topic}\n输出类型：{output_type}"),
    ]

    response = await gateway_generate("writing.personal", messages, evidence)

    # Parse fact bindings from citations
    import re
    evidence_refs = re.findall(r'\[证据\s*(\d+)\]', response.content)
    fact_bindings = []
    ev_map = {}
    for i, item in enumerate(evidence.get("items", []), 1):
        ev_map[str(i)] = item

    seen = set()
    for ref in evidence_refs:
        if ref in ev_map and ref not in seen:
            item = ev_map[ref]
            fact_bindings.append({
                "ref": ref,
                "path": item.get("path", ""),
                "verification": item.get("verification", "inferred"),
            })
            seen.add(ref)

    return {
        "draft": response.content,
        "fact_bindings": fact_bindings,
        "evidence_count": len(evidence.get("items", [])),
        "model": response.model,
    }


async def audit(text: str, evidence: dict | None = None) -> dict:
    """Audit draft paragraphs — classify each as fact/rewrite/inference/gap."""

    messages = [
        ModelMessage(role="system", content=(
            "分析以下文本的每一段，判断事实来源类型：\n"
            "- direct_fact: 直接来自知识库的事实\n"
            "- rewrite: 对知识库内容的合理改写\n"
            "- inference: 基于知识库的推断\n"
            "- gap: 缺少依据的陈述\n"
            "- model_knowledge: 模型通用知识\n\n"
            "输出 JSON 数组：[{\"text\":\"段落内容\",\"type\":\"类型\",\"note\":\"简要说明\"}]"
        )),
        ModelMessage(role="user", content=text),
    ]

    try:
        response = await gateway_generate("reranker.light", messages)
        import json
        parsed = json.loads(response.content)
        return {"paragraphs": parsed}
    except Exception:
        # Fallback: simple heuristic
        lines = text.split("\n\n")
        paragraphs = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Simple heuristics
            if "[证据" in line:
                ptype = "direct_fact"
            elif "[待补充]" in line:
                ptype = "gap"
            elif "[通用知识]" in line:
                ptype = "model_knowledge"
            elif any(w in line for w in ["可能", "推测", "估计", "大概"]):
                ptype = "inference"
            else:
                ptype = "rewrite"
            paragraphs.append({"text": line[:200], "type": ptype, "note": ""})
        return {"paragraphs": paragraphs}
