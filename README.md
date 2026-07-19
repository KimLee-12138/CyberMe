# CyberMe OS — 个人学习操作系统

CyberMe 不是"上传文档后聊天"的通用 RAG 页面，而是围绕个人长期学习建立的认知操作系统。

## 项目结构

```
cyberme-os/
├── apps/
│   ├── web/          # React PWA 前端
│   ├── api/          # FastAPI HTTP/SSE/WebSocket 后端
│   ├── worker/       # Celery 异步任务
│   └── sync-agent/   # Windows 本地同步代理
├── packages/
│   ├── contracts/    # OpenAPI 生成类型、事件协议
│   ├── prompts/      # 版本化提示词和 Schema
│   ├── ui/           # 可复用 UI 组件
│   └── config/       # lint、format、类型配置
├── infra/
│   ├── docker/       # Docker 相关配置
│   ├── caddy/        # Caddy 反向代理配置
│   ├── migrations/   # 数据库迁移脚本
│   └── backup/       # 备份脚本
├── tests/            # 测试
└── docs/             # 文档
```

## 快速开始

### 前端

```bash
cd apps/web
npm install
npm run dev
```

### 后端

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up -d
```

## 环境变量

复制 `.env.example` 为 `.env` 并填入实际值。

## 技术栈

- **前端**: React + TypeScript + Vite + Tailwind CSS
- **后端**: FastAPI + PostgreSQL/pgvector + Redis + Celery
- **同步代理**: Python + watchdog + SQLite

## 许可证

Private — 个人使用
