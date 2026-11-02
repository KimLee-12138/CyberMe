<div align="center">

<img src="apps/web/public/app-icon.png" width="96" alt="CyberMe Logo">

# CyberMe OS

### 个人学习操作系统

从课程资料 → AI 蒸馏 → 知识图谱 → RAG 问答 → 间隔复习

[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)](https://fastapi.tiangolo.com)
[![Tailwind](https://img.shields.io/badge/Tailwind-4.3-38BDF8?logo=tailwindcss)](https://tailwindcss.com)
[![DeepSeek](https://img.shields.io/badge/AI-DeepSeek-536DFE)](https://deepseek.com)
[![Android](https://img.shields.io/badge/Android-Capacitor%208-3DDC84?logo=android)](https://capacitorjs.com)

[快速开始](#-快速开始) · [环境变量](#-环境变量) · [Android App](#-android-app) · [架构](#-架构) · [数据管线](#-数据管线)

</div>

---

## 这是什么？

CyberMe 不是“上传文档然后聊天”的通用 RAG 页面。

它围绕**个人长期学习**，把课程资料变成可检索、可追溯、可复习的知识资产：

- 课程 PDF / Markdown 导入；
- AI 蒸馏成结构化知识点笔记；
- 清洗公式、定义、冲突、重复与来源噪声；
- RAG 问答，带人类可读的来源卡片；
- 本地资料不足时**明确降级**到 DeepSeek，不伪装成课程资料；
- 回答后可直接生成 3 道选择题检验；
- FSRS-5 间隔复习 + 知识图谱 + 雨课堂只读同步。

> 这个仓库不包含个人 `data/` 语料或雨课堂 session。  
> Vault 中的个人学习内容属于作者自己的数据资产；如果你 fork 这个项目，建议先清空/替换 `Vault/` 或把仓库设为私有。
> 你自己放入 `data/` 后即可运行完整的 RAG / 数据质量页。

---

## ✨ 功能

### 📚 课程知识库

- 20 门有内容课程；
- 433 篇清洗后的知识点笔记；
- 2,599 个 RAG chunk；
- 来源页码、section、来源哈希可追溯；
- 公式、定义、易错点、关系、例子结构化。

### 🧹 数据质量

- 公式缺失：**73 → 0**；
- 定义缺失：**51 → 0**；
- 原始来源串：**1,804 → 3**；
- 冲突：4 条 → 1 条已解决、1 条非冲突、2 条保留（原文自身矛盾）；
- 203 组来源近重复不进入 RAG；
- 2 个低质来源隔离；
- 原始 source chunk 2,555 → 0，避免代码/封面/OCR 噪声污染回答。

### 🤖 RAG 问答

- BM25 检索 2,599 个清洗 chunk；
- 课程内/跨课程检索，相关性过滤，避免用无关课程凑数；
- 来源编号在正文中剥离，前端显示“来源 1 · 标题 · 章节 · 页码”；
- 本地证据不足、核心词缺失、模型拒答或无 citation 时，自动降级 DeepSeek；
- 降级回答固定提示：

> 未检索到足够的本地资料，已降级使用 DeepSeek 模型知识回答；以下内容不是你的课程资料。

### 🧠 讲透模式

回答按“结论 → 机制 → 公式/步骤 → 例子 → 易错点 → 关联概念”组织：

- 允许讲得详细、稍复杂；
- 要求解释变量、条件、边界；
- 不把模型常识伪装成课程原文；
- 结尾询问是否出题。

### 🎯 出题检验

- 每条回答下可生成 3 道四选一题；
- 选项卡片、提交、正确/错误标记、逐题解析、得分；
- 可再生成一组。

### 🕸️ 知识图谱

- 1,155 节点 / 2,095 边；
- 24 门课程、389 个 section、433 个 topic、309 个 source；
- 力导向图，点击课程展开章节/主题/来源；
- 节点颜色：课程前置、所属课程、章节、来源、AI 候选。

### 🔁 复习与同步

- FSRS-5 间隔复习；
- 4 级评分；
- 雨课堂只读同步：课程、作业、课件；
- 单节课课件 PDF 导出，Android 保存到 `Documents/CyberMe/`。

### 📱 多端

- 桌面 Web；
- 手机 PWA / 响应式；
- Android Capacitor App（内置前端 APK）；
- 自定义 Select / Checkbox / Confirm，无系统原生下拉框。

---

## 🚀 快速开始

### 前置要求

| 依赖 | 版本 |
|---|---|
| Python | 3.12+ |
| Node.js | 22+ |
| Docker | 最新版 |
| PostgreSQL | pgvector（compose 已包含） |
| Redis | 7+（compose 已包含） |
| Android 构建 | JDK 21 + Android SDK 35（可选） |

### 1. 克隆

```bash
git clone https://github.com/KimLee-12138/CyberMe.git
cd CyberMe
```

### 2. 启动数据库

```bash
docker compose up -d postgres redis
```

本项目默认：

- Postgres：`127.0.0.1:15432`（Windows 的 5432 常被系统保留）；
- Redis：`127.0.0.1:6379`；
- 两者只绑定 loopback，不对局域网开放。

### 3. 配置环境变量

```bash
cp .env.example .env
```

至少填写：

```dotenv
SECRET_KEY=换成一个随机字符串
DEEPSEEK_API_KEY=你的_DeepSeek_Key
```

其余保持 `.env.example` 默认即可；完整说明见 [环境变量](#-环境变量)。

### 4. 后端

```bash
cd apps/api
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
# source .venv/bin/activate

pip install -r requirements.txt
alembic upgrade head

cd ../..
python tools/seed_demo_user.py

cd apps/api
uvicorn app.main:app --host 0.0.0.0 --port 8002
```

默认 demo 账号：`demo / cyberme2026`（可用 `DEMO_PASSWORD` 覆盖）。

### 5. 前端

```bash
cd apps/web
npm ci
npm run dev
```

打开 `http://localhost:3000`。

Vite 会把 `/api` 代理到 `http://127.0.0.1:8002`。

### 6. 数据（可选但推荐）

仓库不包含私人课程语料。把你自己的资料按现有 pipeline 放到 `data/`，或者直接使用空知识库：

- 没有 `data/` 时，笔记页/数据质量页为空；
- RAG 检索不到本地内容时，会自动降级 DeepSeek，并在回答中明确提示。

完整重建命令见 [数据管线](#-数据管线)。

---

## 🔐 环境变量

配置文件：仓库根目录 `.env`（由 `.env.example` 复制）。

### 必需

| 变量 | 示例 | 说明 |
|---|---|---|
| `APP_ENV` | `development` | `development` 会启用本地 CORS / 非 Secure cookie |
| `APP_BASE_URL` | `http://localhost:3000` | 生产环境前端 origin |
| `SECRET_KEY` | 随机 32+ 字符 | JWT / session 签名，必须换 |
| `DATABASE_URL` | `postgresql+asyncpg://cyberme:password@127.0.0.1:15432/cyberme` | Postgres + pgvector |
| `REDIS_URL` | `redis://127.0.0.1:6379/0` | Redis |
| `DEEPSEEK_API_KEY` | `sk-...` | RAG 讲解、蒸馏、降级回答、出题 |

### 可选

| 变量 | 说明 |
|---|---|
| `DEEPSEEK_BASE_URL` | 默认 `https://api.deepseek.com/v1` |
| `GITHUB_TOKEN` | 导入 GitHub 项目 |
| `YKT_REGION` | 默认 `changjiang` |
| `YKT_SESSIONID` | 长江雨课堂 sessionid；也可在 `/yuketang` 页面写入 |
| `YKT_REFRESH_MINUTES` | 同步/缓存刷新间隔 |
| `S3_ENDPOINT` / `S3_BUCKET` / `S3_ACCESS_KEY` / `S3_SECRET_KEY` | 对象存储（可选） |
| `OPENAI_API_KEY` / `ANTHROPIC_API_KEY` | 其他模型 provider（可选） |
| `MONTHLY_BUDGET_LIMIT` | 月度预算，默认 50 |
| `SYNC_MAX_FILE_MB` | 同步单文件上限，默认 10 |
| `RAW_ARCHIVE_UPLOAD` | 是否上传原始归档，默认 false |

### 前端变量

`apps/web/.env.example`：

| 变量 | 说明 |
|---|---|
| `VITE_API_BASE_URL` | 默认 `/api/v1`；内置 APK 构建时设成绝对地址 |

### 安全提醒

- `.env` 已被 `.gitignore` 忽略，不要提交；
- 雨课堂 session 会加密保存在 `data/integrations/yuketang/`，不在仓库中；
- 内置 APK 使用 Bearer token 登录，token 存在本机 localStorage；
- 公网部署请使用 HTTPS，并把 `APP_ENV=production`。

---

## 📱 Android App

### 直接下载

最新内置前端 APK：

**[下载 CyberMe-android-bundled.apk](https://github.com/KimLee-12138/CyberMe/releases/latest/download/CyberMe-android-bundled.apk)**

安装：

```bash
adb install -r CyberMe-android-bundled.apk
```

或在手机浏览器打开上面的 Release 链接下载安装。

### 使用条件

- 手机和电脑在**同一个 Wi-Fi**；
- 后端必须监听 `0.0.0.0:8002`；
- 当前发布包的 API 固定为：

```text
http://192.168.31.244:8002/api/v1
```

如果你的电脑 IP 不是这个，需要重新打包：

```powershell
cd CyberMe
powershell -ExecutionPolicy Bypass -File scripts\build-android.ps1 -ApiHost <你的局域网IP> -Bundled
```

产物：

```text
apps/web/android/app/build/outputs/apk/debug/app-debug.apk
```

### 两种 Android 模式

| 模式 | 命令 | 说明 |
|---|---|---|
| 内置前端 | `scripts\build-android.ps1 -Bundled` | APK 内置 `dist/`，API 走绝对地址 + Bearer token |
| 远程 SPA | `scripts\build-android.ps1` | WebView 打开 `http://<IP>:8002`，同源 cookie |

内置模式不使用 WebView 远程 SPA，因此更适合“打开就有界面”的自用场景。

---

## 🏗️ 架构

```text
┌─────────────────────────────────────────────────────┐
│                     Web / Android                    │
│   React 19 + TypeScript + Tailwind 4 + Capacitor     │
│   自定义 Select / Checkbox / Confirm / 出题卡片       │
└───────────────────────┬─────────────────────────────┘
                        │ /api/v1
┌───────────────────────▼─────────────────────────────┐
│                     FastAPI                          │
│  Auth │ Notes │ RAG │ KG │ Corpus │ Learning │ YKT   │
│  ├─ RAG: BM25 2599 chunks → DeepSeek → 来源卡片      │
│  ├─ 降级: 本地证据不足 → DeepSeek + degraded banner   │
│  ├─ Quiz: 3 道四选一题                               │
│  └─ 雨课堂: 只读 sessionid，加密保存                  │
└──────────────┬──────────────────────┬────────────────┘
               │                      │
        PostgreSQL + pgvector       Redis
        Vault / 课程 / 笔记          缓存 / 队列
```

---

## 🧪 数据管线

原始语料 → 清洗 → 分节 → 蒸馏 → 主题 → 笔记 → 增强 → RAG。

```bash
# 1. 构建语料
python tools/build_registry.py
python tools/extract_clean.py
python tools/normalize_clean.py
python tools/dedup_near.py
python tools/quality_score.py
python tools/build_sections.py
python tools/map_distill.py --concurrency 8
python tools/merge_topics.py --concurrency 8
python tools/generate_notes.py
python tools/freeze_v1.py

# 2. v2 AI enrichment（不覆盖 data/notes/）
python tools/enrich_notes.py --mode all --concurrency 8
python tools/supplement_formulas.py
python tools/supplement_definitions.py
python tools/resolve_conflicts.py
python tools/build_enriched_manifest.py

# 3. 重建 RAG
cd apps/api
python -m app.rag.loader
cd ../..
```

`data/notes_enriched/_complete.json` 存在时，运行时优先使用 enriched notes。

原始 source chunk 默认不进入 RAG：

```bash
# 只有确认原文干净时才开启
CYBERME_INCLUDE_SOURCE_CHUNKS=1
```

---

## 🧪 测试

```bash
# 后端离线测试
pytest -q

# 数据质量烟测
python tools/corpus_smoke_test.py

# RAG 六问烟测（需要 DEEPSEEK_API_KEY）
python tools/rag_smoke_test.py

# 前端构建
cd apps/web
npm run build
```

CI（`.github/workflows/ci.yml`）会跑：

- 后端 `pytest`（没有私有 `data/` 时自动跳过语料测试）；
- 前端 `npm ci && npm run build`。

---

## 📁 项目结构

```text
CyberMe/
├── apps/
│   ├── api/                 # FastAPI
│   │   ├── app/
│   │   │   ├── auth/        # 登录 / TOTP / token
│   │   │   ├── rag/         # BM25、回答、降级、quiz
│   │   │   ├── notes/       # 笔记浏览器
│   │   │   ├── corpus/      # 数据质量看板
│   │   │   ├── integrations/yuketang/
│   │   │   └── ...
│   │   └── requirements.txt
│   └── web/                 # React + Vite + Capacitor
│       ├── src/
│       ├── public/
│       └── android/
├── tools/                   # 数据管线 / enrichment / smoke tests
├── tests/                   # 后端测试
├── docs/                    # 说明文档
├── scripts/build-android.ps1
├── docker-compose.yml
└── .env.example
```

---

## 🧭 常用页面

| 页面 | 地址 |
|---|---|
| 登录 | `http://localhost:3000/login` |
| 驾驶舱 | `http://localhost:3000/` |
| 问答 | `http://localhost:3000/ask` |
| 笔记 | `http://localhost:3000/notes` |
| 知识图谱 | `http://localhost:3000/graph` |
| 数据质量 | `http://localhost:3000/quality` |
| 雨课堂 | `http://localhost:3000/yuketang` |
| 复习 | `http://localhost:3000/review` |

---

## ⚠️ 已知边界

- 个人语料不进入仓库；RAG 在无本地资料时会降级 DeepSeek。
- `PROB-TOPIC-005` 的 2 条冲突来自原文自身矛盾，笔记保留，但不进入 RAG。
- 193 篇无“例子”、55 篇无“易错点”属于可选字段，没有强行编造。
- 167 篇标记 `source_noisy`：原文有 OCR/封面/代码噪声，正文与 RAG 已清洗。
- 内置 APK 的 API 地址是打包时的局域网 IP，换网络需重打包。

---

## 🙏 说明

这是一个个人学习项目，不是通用 SaaS。  
代码、pipeline、schema 与可公开的文档保留在仓库；Vault 与 `data/` 中的个人学习资产请按需私有化或替换。

如果这个项目对你有启发，欢迎 Star ⭐
