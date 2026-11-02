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

### 📚 20 门课程知识库
涵盖数据结构、算法、计组、数据库、微积分、概率论、近代史等，**433 篇可追溯知识点笔记**，带来源页码与数据质量标记。

### 🔗 知识图谱可视化
力导向图展示知识点之间的关联——前置知识、对比关系、应用场景。点击节点直接跳转，支持拖拽和缩放。

### 🤖 RAG 增强 AI 问答
问课程问题 → 系统检索 433 篇清洗笔记 → DeepSeek 结合你的资料生成透彻讲解 → 人类可读的来源卡片。**本地资料不足时会明确降级到 DeepSeek，不伪装成课程资料。**

### 📝 FSRS-5 间隔复习
基于遗忘曲线的科学复习系统。4 级评分（完全忘了/勉强记得/正确回忆/非常轻松），自动计算最优复习间隔。复习统计面板实时显示记忆保持率。

### 🔄 Obsidian 双向同步
用 Obsidian 编辑笔记 → 一键同步到网页端。sync-agent 自动检测文件变更，上传到服务器。

### 📱 PWA 移动端支持
可安装到手机主屏幕；Android debug APK 已可构建与安装（JDK 21 + WebView 111+）。暗色模式、打印样式、离线缓存齐备。

## 🏗️ 技术架构

```
┌─────────────────────────────────────────────────────┐
│                    前端 (apps/web)                    │
│          React 19 + TypeScript + Tailwind 4           │
│        Vite PWA · Lucide Icons · Force-Graph        │
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
docker compose up -d postgres redis
```

本项目默认：

- Postgres：`127.0.0.1:15432`（Windows 的 5432 常被系统保留）
- Redis：`127.0.0.1:6379`
- 两者都只绑定 loopback，不对局域网开放

### 3. 配置环境变量

```bash
cp .env.example .env
```

在**仓库根目录**的 `.env` 中填写：

- `SECRET_KEY` — 随机字符串
- `DEEPSEEK_API_KEY` — DeepSeek API Key（RAG 必需）
- `DATABASE_URL` / `REDIS_URL` — 默认就是本地 compose 的地址

后端和 Alembic 都会读取仓库根目录的 `.env`。

### 4. 启动后端

```bash
cd apps/api
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
cd ../..
python tools/seed_demo_user.py
cd apps/api
uvicorn app.main:app --reload --port 8002
```

默认 demo 账号：`demo / cyberme2026`（可用 `DEMO_PASSWORD` 覆盖）。

### 5. 启动前端

```bash
cd apps/web
npm install
npm run dev                  # http://localhost:3000
```

Vite 代理 `/api` 到 `http://127.0.0.1:8002`。
手机浏览器临时调试可显式开启（Android APK 不需要 Vite，见下一节）：

```powershell
$env:VITE_DEV_HOST='0.0.0.0'
npm run dev
```

### 6. 构建 Android debug APK

前置：**JDK 21**（JDK 17 编不过 Capacitor 8）、Android SDK 35、手机 Android WebView 111+。

后端必须对手机所在的局域网可见，并由它同时托管构建好的前端（同源 Cookie 登录）：

```powershell
cd apps/api
uvicorn app.main:app --host 0.0.0.0 --port 8002
```

另开一个终端：

```powershell
cd apps/web
npm run android:debug
# 或指定 IP
powershell -ExecutionPolicy Bypass -File ..\..\scripts\build-android.ps1 -ApiHost 192.168.31.244
```

脚本会：构建前端 → `cap sync` → Gradle 打 debug APK。

产物：

```text
apps/web/android/app/build/outputs/apk/debug/app-debug.apk
```

安装：

```powershell
adb install -r apps/web/android/app/build/outputs/apk/debug/app-debug.apk
```

说明：

- WebView 直接打开 `http://<LAN-IP>:8002`，API 与页面同源，**HttpOnly session cookie 可用**；
- debug manifest 仅 debug 允许 cleartext；生产请用 HTTPS 并设置 `CAP_SERVER_URL=https://...`；
- IP 变化后重新运行脚本；
- Android 15 模拟器已实测：登录、驾驶舱、笔记、质量、图谱、RAG + 证据面板。

详见 [`docs/android.md`](docs/android.md)。

### 7. 长江雨课堂只读同步

浏览器打开 `http://127.0.0.1:8002/yuketang`（手机同一 Wi-Fi 用 `http://192.168.31.244:8002/yuketang`）。

1. 登录 `changjiang.yuketang.cn`；
2. F12 → Application → Cookies → 复制 `sessionid`；
3. 粘贴到 CyberMe 页面，点「保存并同步」。

会同步课程、作业、公告、截止时间和课件；每 15 分钟自动刷新，不做签到/答题/提交。

详见 [`docs/yuketang.md`](docs/yuketang.md)。

### 8. 配合同步代理

```bash
cd apps/sync-agent
pip install -r requirements.txt
python main.py pair          # 输入配对码和 Vault 路径
python main.py now           # 全量同步
python main.py watch         # 监听模式
```

### Docker 一键启动

```bash
docker compose up -d
```

## 🎯 使用指南

| 你想做什么 | 去哪里 | 怎么做 |
|-----------|--------|--------|
| 浏览 433 篇笔记 | `http://localhost:3000/notes` | 课程/flag 筛选 → 搜索 → 看正文/来源页码 |
| 看数据质量 | `http://localhost:3000/quality` | 漏斗 → 质量分级 → 冲突/隔离/公式缺失 |
| AI 问答（引用笔记） | `http://localhost:3000/ask` | 输入问题 → 等待 RAG 回答 → 看证据 |
| 知识图谱 | `http://localhost:3000/graph` | 24 课程 → 点课程展开 → 点主题看来源 |
| 搜索笔记 | 顶部搜索框 | 输入关键词 → 点结果跳到 `/notes` |
| 间隔复习 | `http://localhost:3000/review` | 看卡片 → 点评分按钮 |
| AI 蒸馏提取资料 | `http://localhost:3000/distill` | 选课 → 一键蒸馏 |
| 导入 GitHub 项目 | `http://localhost:3000/projects` | 点"GitHub" → 点"导入" |
| 在 Obsidian 中编辑 | Vault 目录 | 用 Obsidian 打开 → 编辑 → `python main.py now` |

## 🔑 核心 Feat

- **RAG 问答** — 2,599 块清洗笔记检索 → DeepSeek 透彻讲解 → 人类可读来源卡片；本地证据不足时标记 `degraded` 并降级 DeepSeek
- **笔记浏览器** — 433 篇 / 20 门课；课程、flag、正文搜索；来源页码；笔记 ↔ 图谱互跳
- **数据质量看板** — 868→410→309→414→4,523→433；公式缺失 0、冲突处理、隔离、来源去重
- **知识图谱** — 1,155 节点 / 2,095 边；24 课程 / 389 section / 433 topic / 309 source；18 条课程前置边
- **出题检验** — 每条回答可生成 3 道四选一题，作答后给分与逐题解析
- **FSRS-5 间隔复习** — 17 参数模型，stability/difficulty 追踪，4 级评分，自动排期
- **AI 知识蒸馏** — SSE 流式批量处理，deepseek-reasoner 深度推理
- **GitHub 集成** — OAuth Token 代理，仓库列表 + 一键导入为项目
- **sync-agent** — SHA-256 哈希比对，增量事件队列，冲突检测
- **20 门课程** — 433 篇清洗笔记，LaTeX 公式，来源可追溯
- **暗色模式** — `.dark` CSS 类全局适配
- **PWA / Android** — Service Worker 离线缓存；内置前端 APK 与 Bearer token 登录

## 🔒 关于私有语料

这个仓库不提交 `data/`（个人课程 PDF/笔记/雨课堂 session）和 `Vault/` 中的个人内容。运行 RAG/数据质量页需要在本机放入自己的 `data/`；代码、schema、pipeline 与前端均可独立构建。

## 📊 规模

| 指标 | 数量 |
|------|------|
| 课程 | 20 门（有内容） |
| 知识笔记 | 433 篇 |
| 清洗 RAG chunk | 2,599 块 |
| 数据来源 | 309 个蒸馏文件 / 414 section part |
| 知识图谱节点 | 1,155 |
| 知识图谱边 | 2,095 |
| 前端页面 | 19+ 个 |

## 许可证

MIT License

---

<div align="center">
<sub>Built with ❤️ by KimLee + Claude Opus 4.6</sub>
</div>
