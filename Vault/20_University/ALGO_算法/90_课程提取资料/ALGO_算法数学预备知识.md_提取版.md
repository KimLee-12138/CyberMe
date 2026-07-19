---
id: extract-algo-79cdf309
type: extract
status: extracted
course: ALGO
source:
  - "[[91_Raw-Archive/DOC/ALGO_算法数学预备知识.md_笔记_未知日期_79cdf309.md]]"
source_pages: all
source_hash: "79cdf309d8fd68ecba317b38d5940772fdd6524b32c956414e24947af8208fcb"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 算法数学预备知识.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 算法数学预备知识

> cover：小孩不哭站起来

## 一、基本数学知识

老师PPT中大多展示的是离散数学的基本内容，在此不做讲解

## 二、巢鸽原理

**基本原理：**

- 简单形式：如果K+1个或更多的物体放入K个盒子，那么至少有一个盒子含2个或更多的物体。
  - 例1：在13个人中存在两个人，他们的生日在同一月份里
  - 例2：设有n对已婚夫妇。为保证有一对夫妇被选出，至少要从这2n个人中选出多少人？（n+1）

**推广的鸽巢原理**：

如果把n个球分别放在m个盒子中，那么：

- 存在一个盒子，必定至少装$\left\lceil n/m\right\rceil$个球；
- 存在一个盒子，必定最多装$\lfloor n/m\rfloor$ 个球。
- 等同于：当盒子仅有n个，而球的数目大于n*m时，则必有一个盒子中至少有m+1或多于m+1个物体。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_算法_课程MOC|算法 MOC]]
