# AGENTS.md — CyberMe OS 开发指南

## 项目定位

CyberMe 是个人学习操作系统。`CyberMe-Vault`（Obsidian 知识库）是唯一事实源，云端系统负责索引、检索、学习运行状态、AI 编排与经确认的写回提案。

## 核心原则

1. **Vault 是唯一事实源** — 稳定知识、个人事实和规则只在 Vault 中持久保存
2. **云端可重建** — 派生索引（chunks、embeddings、图谱）可从 Vault 重建
3. **人在回路** — 修改 Vault、确认推断、写回操作必须用户审批
4. **证据可追溯** — 每个结论定位到文件、页码或标记为模型知识
5. **本地可独立** — 云端不可用时 Vault 仍可完整使用

## 技术决策

- 前端路由使用 React Router v6
- 服务端状态用 TanStack Query，UI 状态用 Zustand
- 后端模块通过 service 接口通信，禁止跨模块直接操作数据表
- Celery 只做可重试后台工作，核心状态变更由事务服务控制
- 数据库主键统一 UUIDv7，时间 UTC，接口返回 ISO-8601
- API 基础路径 `/api/v1`，JSON 字段使用 snake_case

## 开发约定

- 先在开发分支工作，每步完成后验证再合并
- 数据库迁移只前进，不在生产环境手改表
- 提交信息格式：`type(scope): description`
- 禁止在代码中硬编码密钥、路径和模型名称
- 环境变量通过 `.env` 注入，`.env.example` 只放占位符
