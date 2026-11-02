# CyberMe 一页纸

## 把课程资料变成“可引用的知识图谱 + RAG”

**问题**：资料散落在 PDF/Markdown/笔记里，模型直接回答会编造，找不到出处。

**做法**：先把课程资料洗干净、分节、蒸馏成 433 篇可追溯笔记；再用 BM25 检索 + DeepSeek 生成带引用的回答；最后把课程/章节/主题/来源连成知识图谱。

---

## 1. 数据漏斗

```text
868 个 PDF/MD
  → 410 个纳入（去扫描件/乱码/项目文件/重复）
  → 309 个进入蒸馏
  → 414 个 section part
  → 4,523 个知识单元
  → 433 个 topic / 433 篇笔记
```

- 每篇笔记有 `source_id` + 页码范围；
- 383 篇 indexable，150 official / 233 review / 2 quarantine；
- 4 条冲突、73 篇公式缺失已标记；
- 人工抽查样本 48 篇。

---

## 2. RAG 纵切

```text
问题
  → BM25 检索 5,187 个块（笔记 2,632 + 来源 2,555）
  → top 8 证据
  → DeepSeek Flash 生成
  → 每个事实句带 [E1] 引用
  → 证据不足则拒答
  → 证据面板显示：标题 / 章节 / 页码 / 片段 / 分数
```

**烟测 6/6**：

| 问题 | 结果 |
|---|---|
| 什么是函数依赖 | 回答 + 6 引用 |
| 2NF 和 3NF 的区别 | 回答 + 3 引用 |
| 0/1 背包为什么容量逆序 | 回答 + 3 引用 |
| 栈和队列的区别 | 回答 + 2 引用 |
| 数据库索引的原理 | 拒答 |
| 量子纠缠在数据库中的应用 | 拒答 |

---

## 3. 知识图谱

```text
24 Course
  └─ 389 Section
       └─ 433 Topic
            └─ 309 Source

1,155 节点 / 2,095 边
18 条课程前置边
330 条 AI 候选边（默认关闭）
```

课程前置示例：

- 数据结构 ← C++ / Python
- 算法 ← 数据结构 / 离散数学
- 概率论 ← 微积分
- 强化学习数学 ← 微积分 / 概率论 / 线性代数
- 毛概 ← 马原；习概 ← 毛概

图谱页面：

- 默认 24 门课 + 18 条前置边；
- 点「数据库」展开 51 节点 / 83 边；
- 点 topic 显示 `note_path`、来源页码、关键点/公式数；
- AI 候选边用灰色虚线，单独开关；
- 结构校验：0 断边、0 自环、0 前置环。

---

## 3.5 笔记浏览器

- 433 篇笔记 / 20 门课程；
- 课程、flag（公式缺失 73 / 缺定义 51 / 冲突 3）、正文搜索；
- 详情显示来源文件 + 页码 + topic 关系 + Markdown 正文；
- 笔记 ↔ 图谱互跳：`/notes?note=DB-TOPIC-001`、`/graph?course=DB`；
- 只读，不修改 Vault。

---

## 4. 架构

```text
Vault / F:\学习
   │  离线流水线（10 步）
   ▼
data/clean → sections → units → topics → notes
   │                                   │
   │                                   ├─ data/kg/kg.json
   ▼                                   ▼
BM25 索引 (5,187 chunks)          KG API (/api/v1/kg/*)
   │                                   │
   └──────────┬────────────────────────┘
              ▼
        FastAPI (/api/v1/rag/ask)
              │
              ▼
        React ChatPage / GraphPage
```

- 检索不依赖 Postgres/pgvector，启动加载预构建索引，演示稳定；
- 云端可重建：派生索引都能从 Vault/data 重建；
- 证据可追溯：回答/图谱都能回到 source/page；
- 人在回路：写回 Vault 仍是 proposal，未自动执行。

---

## 5. 演示入口

| 页面 | 地址 |
|---|---|
| 数据质量 | `http://localhost:3000/quality` |
| 笔记浏览器 | `http://localhost:3000/notes` |
| RAG 问答 | `http://localhost:3000/ask` |
| 知识图谱 | `http://localhost:3000/graph` |
| 后端 | `http://127.0.0.1:8002` |

启动：

```powershell
cd D:\CyberMe\repo\apps\api
$env:DEEPSEEK_API_KEY=[Environment]::GetEnvironmentVariable('DEEPSEEK_API_KEY','User')
python -m uvicorn app.main:app --host 127.0.0.1 --port 8002

cd D:\CyberMe\repo\apps\web
npm run dev
```

---

## 6. 已知限制

1. 引用是 **section 级**，不是逐句精确页；
2. 部分 PDF 公式缺失（73 篇已标记，不补写）；
3. 97 个 topic 没有页码（Markdown 来源）；
4. 图谱没有独立 chapter 层，用 section 代替；
5. 候选边只匹配上 330 条，默认不展示；
6. 没有流式输出，回答等待 15–20 秒；
7. 会话不持久化；
8. 接口暂未鉴权，演示够用。

---

## 7. 下一步

1. 数据质量看板（868→433 漏斗、隔离/冲突/公式缺失）；
2. 60 题轻量实验：BM25 / Hybrid / Hybrid+KG；
3. 本地 `bge-small-zh` 向量 + RRF；
4. 逐句引用校验；
5. Vault 写回（人工审批）。

---

## 8. 一句话

> 我们不是做了一个“会聊天的模型”，而是做了一条 **从 868 个文件到 433 篇可引用笔记、再到 1,155 节点知识图谱** 的可追溯链路。
