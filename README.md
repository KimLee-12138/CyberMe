<div align="center">

<img src="apps/web/public/favicon.svg" width="80" alt="CyberMe OS Logo">

# CyberMe OS

### 个人学习操作系统

*围绕长期学习构建的认知基础设施——不只是笔记工具，是第二大脑。*

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.139-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Tailwind](https://img.shields.io/badge/Tailwind-4.3-38BDF8?logo=tailwindcss)](https://tailwindcss.com)
[![DeepSeek](https://img.shields.io/badge/AI-DeepSeek-536DFE)](https://deepseek.com)

</div>

---

## 这是什么？

CyberMe OS 不是"上传文档然后聊天"的通用 RAG 页面。它是一个**围绕个人长期学习构建的认知操作系统**——从资料导入、AI 蒸馏、知识图谱，到 FSRS-5 间隔复习和 RAG 问答，覆盖学习的完整闭环。

## ✨ 核心功能

### 🧠 AI 知识蒸馏
将课件 PDF、学生笔记等原始资料，通过 DeepSeek AI 自动蒸馏为结构化知识笔记。支持单篇和**一键批量蒸馏整门课**。

### 📚 25 门课程知识库
涵盖数据结构、算法、计组、数据库、微积分、线性代数、概率论等，**228+ 篇正式知识点文档，约 24 万字**。

### 🔗 知识图谱可视化
力导向图展示知识点之间的关联——前置知识、对比关系、应用场景。点击节点直接跳转，支持拖拽和缩放。

### 🤖 RAG 增强 AI 问答
问课程问题 → 系统检索知识库中的相关文档 → DeepSeek 结合你的笔记生成回答 → 标注引用来源。**不是通用 AI，是用你的资料回答。**

### 📝 FSRS-5 间隔复习
基于遗忘曲线的科学复习系统。4 级评分（完全忘了/勉强记得/正确回忆/非常轻松），自动计算最优复习间隔。复习统计面板实时显示记忆保持率。

### 🔄 Obsidian 双向同步
用 Obsidian 编辑笔记 → 一键同步到网页端。sync-agent 自动检测文件变更，上传到服务器。

### 📱 PWA 移动端支持
可安装到手机主屏幕，Android 已配 Capacitor 打包配置。暗色模式、打印样式、离线缓存齐备。

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────┐
│                    前端 (apps/web)                    │
│          React 19 + TypeScript + Tailwind 4           │
│        Vite PWA · Phosphor Icons · Force-Graph        │
├─────────────────────────────────────────────────────┤
│                   API 网关 (8000)                     │
├──────────────┬──────────────┬─────────────────────────┤
│   Chat/RAG    │   Learning   │      Knowledge          │
│  问答引擎     │  FSRS 复习   │  课程/文档/图谱          │
├──────────────┼──────────────┼─────────────────────────┤
│  Model Gateway│  Retrieval   │      Projects           │
│ DeepSeek/OpenAI│ 混合检索    │  GitHub 集成            │
├──────────────┴──────────────┴─────────────────────────┤
│                    数据层                              │
│        PostgreSQL + pgvector · Redis · MinIO          │
├─────────────────────────────────────────────────────┤
│               Sync Agent (apps/sync-agent)            │
│         本地 Vault 扫描 · 文件监听 · 增量同步           │
└─────────────────────────────────────────────────────┘
```

### 技术栈

| 层 | 技术 |
|---|------|
| **前端** | React 19 · TypeScript · Tailwind CSS v4 · Vite · PWA · Capacitor |
| **后端** | FastAPI · SQLAlchemy · asyncpg · Redis · Celery |
| **AI** | DeepSeek (deepseek-chat / deepseek-reasoner) · 意图分类 · 混合检索 · RAG |
| **复习** | FSRS-5 算法 · 稳定性/难度追踪 · 遗忘曲线 · 记忆保持率 |
| **同步** | watchdog · SHA-256 哈希 · 增量事件队列 · JWT 认证 |
| **基础设施** | Docker · Caddy · Nginx · Systemd |

## 📂 项目结构

```
cyberme-os/
├── apps/
│   ├── web/                # React PWA 前端 (19 页面)
│   │   ├── src/
│   │   │   ├── components/ # 布局 + UI 组件
│   │   │   ├── pages/      # 19 个页面组件
│   │   │   ├── api/        # API 客户端
│   │   │   ├── stores/     # Zustand 状态管理
│   │   │   └── lib/        # 工具函数 + 枚举映射
│   │   ├── android/         # Capacitor Android 配置
│   │   └── public/          # 静态资源 + PWA manifest
│   ├── api/                 # FastAPI 后端
│   │   ├── app/
│   │   │   ├── chat/        # RAG 问答引擎
│   │   │   ├── knowledge/   # 课程/文档/图谱 API
│   │   │   ├── learning/    # FSRS 复习 + 导师 + 写作
│   │   │   ├── model_gateway/ # DeepSeek/OpenAI 网关
│   │   │   ├── retrieval/   # 混合检索 (FTS + 向量 + 图谱)
│   │   │   ├── projects/    # 项目管理 CRUD
│   │   │   ├── github_proxy/ # GitHub API 代理
│   │   │   ├── sync/        # 同步协议 API
│   │   │   └── distill_router.py  # AI 知识蒸馏
│   │   └── infra/migrations/    # 数据库迁移
│   └── sync-agent/          # 本地同步代理
│       ├── agent/           # 扫描/监听/推送
│       ├── main.py          # CLI 入口 (pair/now/watch)
│       └── sync-policy.yaml # 同步策略配置
├── Vault/                   # 知识库 (896 篇 Markdown)
│   ├── 20_University/       # 25 门课程笔记
│   ├── 01_Home/             # 首页/任务/变更日志
│   └── 10_Self/             # 个人模型/风格样本
├── infra/                   # Caddy · Docker · 备份
├── docker-compose.yml
└── docs/                    # 文档
```

## 🚀 快速开始

### 前置要求

- Python 3.12+
- Node.js 20+
- PostgreSQL 15+ (需 pgvector 扩展)
- Redis (可选，用于 Celery)

### 1. 克隆仓库

```bash
git clone https://github.com/KimLee-12138/CyberMe.git
cd CyberMe
```

### 2. 启动数据库

```bash
docker-compose up -d postgres redis
```

### 3. 配置环境变量

```bash
cp .env.example .env
```

必填：
- `DATABASE_URL` — PostgreSQL 连接串
- `DEEPSEEK_API_KEY` — DeepSeek API Key（AI 功能必需）
- `GITHUB_TOKEN` — GitHub Personal Token（项目导入可选）

### 4. 启动后端

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

### 5. 启动前端

```bash
cd apps/web
npm install
npm run dev                  # http://localhost:3000
```

### 6. 配合同步代理

```bash
cd apps/sync-agent
pip install -r requirements.txt
python main.py pair          # 输入配对码和 Vault 路径
python main.py now           # 全量同步
python main.py watch         # 监听模式
```

### Docker 一键启动

```bash
docker-compose up -d
```

## 🎯 使用指南

| 你想做什么 | 去哪里 | 怎么做 |
|-----------|--------|--------|
| 浏览/复习笔记 | `http://localhost:3000/courses` | 选课 → 点知识点 |
| AI 问答（引用笔记） | `http://localhost:3000/ask` | 输入问题 → 等待 RAG 回答 |
| 间隔复习 | `http://localhost:3000/review` | 看卡片 → 点评分按钮 |
| 知识图谱 | `http://localhost:3000/graph` | 拖拽节点 → 点击跳转 |
| AI 蒸馏提取资料 | `http://localhost:3000/distill` | 选课 → 一键蒸馏 |
| 导入 GitHub 项目 | `http://localhost:3000/projects` | 点"GitHub" → 点"导入" |
| 搜索笔记 | 顶部搜索框 | 输入关键词 → 点结果跳转 |
| 导出笔记 | 文档详情页 | 点"📥 下载 .md"或"🖨️ 打印" |
| 在 Obsidian 中编辑 | Vault 目录 | 用 Obsidian 打开 → 编辑 → `python main.py now` |

## 🔑 核心 Feat

- **RAG 问答引擎** — 意图分类 → 混合检索(FTS+向量+图谱) → DeepSeek → 引用标注
- **FSRS-5 间隔复习** — 17 参数模型，stability/difficulty 追踪，4 级评分，自动排期
- **AI 知识蒸馏** — SSE 流式批量处理，deepseek-reasoner 深度推理
- **知识图谱** — 876 节点 / 935 边，力导向可视化，D3 + ForceGraph
- **GitHub 集成** — OAuth Token 代理，仓库列表 + 一键导入为项目
- **sync-agent** — SHA-256 哈希比对，增量事件队列，冲突检测
- **25 门课程** — 896 篇 Markdown，24 万字，中英双语，LaTeX 公式
- **暗色模式** — `.dark` CSS 类全局适配
- **PWA** — Service Worker 离线缓存，Capacitor Android 打包

## 📊 规模

| 指标 | 数量 |
|------|------|
| 课程 | 25 门 |
| 知识文档 | 896 篇 Markdown |
| 总字数 | ~36 万 |
| 代码文件 | 373 个 |
| 知识图谱节点 | 876 |
| 知识图谱边 | 935 |
| 复习卡片 | 60 张 |
| 前端页面 | 19 个 |

## 许可证

MIT License

---

<div align="center">
<sub>Built with ❤️ by KimLee + Claude Opus 4.6</sub>
</div>
