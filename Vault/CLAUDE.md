@AGENTS.md

# Claude Code / Claude 桌面版 专属指令

> 公共规则见 `AGENTS.md`。本文件仅包含 Claude 产品特有的操作规则，不复制 AGENTS.md 的内容。

## Plan Mode（计划模式）

- 大规模操作（涉及 >3 个文件或 >1 个目录的修改）默认先进入 Plan Mode。
- Plan Mode 下只探索代码库、设计方案，不执行修改。
- 获得用户批准后才退出 Plan Mode 并开始实施。

## Skill 使用

- 优先使用已经存在的 Skill（`.claude/skills/`），不临时发明相互冲突的流程。
- 可通过 Skill 工具调用：
  - `ingest-material`：资料导入
  - `distill-course`：知识蒸馏
  - `explain-like-my-tutor`：个性化解释
  - `write-like-me`：风格仿写
  - `weekly-review`：周复盘
  - `audit-vault`：Vault 审计

## 子代理（Sub-agent）使用

- 需要遍历大量文件时使用 Explore 子代理，隔离检索结果，避免污染主任务上下文。
- 子代理不得执行写操作，只做研究和报告。

## 权限与确认

- 未经用户确认**不允许**：批量归档、覆盖正式知识笔记、更新正式个人档案。
- 绝对禁止使用绕过权限检查的模式（如 `dangerouslyDisableSandbox` 不经用户同意就使用）。
- 每次任务结束列出：读取依据、修改文件清单、待人工核对项、未完成项。

## 上下文管理

- 回答课程问题时优先读取对应课程 MOC，而非遍历全部文件。
- 读取大文件时按需分段（通过 offset/limit），避免一次加载过多内容。
- 临时脚本执行完毕后清理，不保留在 Vault 内。

## 与 Codex 的差异

见 `01_Home/代理兼容说明.md`。
