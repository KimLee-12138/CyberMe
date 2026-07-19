"""Chat — intent classification and scope resolution."""

from typing import Any


# Pre-compiled intent patterns for fast classification without API call
INTENT_PATTERNS = {
    "knowledge_qa": [
        "是什么", "什么意思", "定义", "区别", "区别是什么",
        "如何理解", "怎么理解", "解释", "简述", "说明",
        "事务", "隔离", "索引", "查询", "范式", "锁",
    ],
    "review_question": [
        "考试", "考", "题目", "答案", "选择", "判断",
        "历年", "真题", "模拟", "试卷",
    ],
    "writing_task": [
        "写", "编辑", "修改", "生成", "创建", "输出",
        "报告", "总结", "文章", "简历",
    ],
    "system_command": [
        "同步", "设置", "配对", "备份", "撤销",
    ],
    "learning_help": [
        "怎么学", "学习路径", "学习方法", "建议",
        "计划", "复习", "掌握",
    ],
}


def classify_intent(
    query: str,
    scope_override: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Classify user intent with rule-based pattern matching.

    Falls back to "knowledge_qa" as default. In production, this can be
    upgraded to use the model gateway for more accurate classification.

    Returns structured intent dict:
    {
        "task_type": str,
        "scope": dict,
        "answer_mode": str,
        "requires_personal_context": bool,
        "risk": str,
    }
    """
    query_lower = query.lower()

    # Determine task type by pattern matching
    task_type = "knowledge_qa"  # default
    max_matches = 0
    for intent_type, patterns in INTENT_PATTERNS.items():
        matches = sum(1 for p in patterns if p in query)
        if matches > max_matches:
            max_matches = matches
            task_type = intent_type

    # Resolve scope from user override
    scope = scope_override or {"courses": [], "projects": [], "document_types": []}

    # Determine answer mode
    answer_mode = "normal"
    if scope_override and scope_override.get("mode") == "evidence_only":
        answer_mode = "evidence_only"
    elif "只查资料" in query or "只从笔记" in query:
        answer_mode = "evidence_only"
    elif "深度研究" in query or "深入研究" in query:
        answer_mode = "deep_research"

    # Risk assessment
    risk = "low"
    if any(w in query_lower for w in ["密码", "密钥", "删除全部", "重置"]):
        risk = "high"
    elif task_type in ("writing_task",):
        risk = "medium"

    return {
        "task_type": task_type,
        "scope": scope,
        "answer_mode": answer_mode,
        "requires_personal_context": task_type in ("writing_task", "learning_help"),
        "risk": risk,
        "time_filter": None,
    }


def resolve_scope(
    intent: dict[str, Any],
    user_courses: list[str] | None = None,
) -> dict[str, Any]:
    """Resolve the search scope from intent + user context.

    Priority:
    1. User explicit selection (highest)
    2. Intent classifier inference
    3. All available courses (lowest — but safe default)
    """
    scope = intent.get("scope", {})
    if scope.get("courses"):
        return scope  # User explicitly selected

    # No explicit scope — search everything the user has
    return {
        "courses": user_courses or [],
        "projects": scope.get("projects", []),
        "document_types": scope.get("document_types", []),
    }
