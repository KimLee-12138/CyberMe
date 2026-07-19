---
id: ds-字符串匹配-kmpalgo
type: concept
status: cleaned
course: DS
source:
  - "[[91_Raw-Archive/PDF/DS_DataStructure(1).pdf_课件_未知日期_dfdfb9d1.pdf]]"
  - "[[91_Raw-Archive/PDF/DS_Algorithm(1).pdf_课件_未知日期_5a3c8b71.pdf]]"
source_pages:
  - "DataStructure(1).pdf 第1-4页"
source_hash:
  - "dfdfb9d1a55f31860372071bd64a7bae3f8ed59c546a312928550a9a4baa05e4"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
mastery: unknown
importance: high
confidence: medium
verification: inferred
needs_review: true
review_reason: "AI 从提取版蒸馏生成，需人工与原始课件核对代码和公式"
tags:
  - 数据结构
---

# 字符串匹配与KMP算法

## 一句话解释

字符串匹配是找模式串在主串中出现的位置。BF算法暴力比较O(mn)，KMP利用已匹配信息将复杂度降到O(m+n)。

## 核心原理

**BF 算法（Brute Force）**：主串每一位作为起点，与模式串逐字符比较。失配时主串回退 i=i-j+1，模式串回退 j=0。

**KMP 算法**：失配时主串不回退，模式串根据 next 数组决定回退位置。
- **next[j]**：模式串第 j 位失配时，j 应回退到的位置（前缀和后缀的最长公共长度）
- 例如模式串 "ABABC"，next = [-1, 0, 0, 1, 2]
- next 数组求解本身也是 KMP 思想的应用（模式串自匹配）

## 规则或公式

next 数组递推公式：
- next[0] = -1
- 若 P[k] == P[j]：next[j+1] = k+1
- 若 P[k] != P[j]：k = next[k]（递归回溯），直到 k=-1 或匹配

KMP 时间复杂度：主串扫描 O(n) + next 数组 O(m) = **O(n+m)**

## 容易出错的地方

- next 数组的第一个值（next[0]）是 -1 还是 0，取决于实现
- KMP 的优势在模式串有重复前缀时明显（如 "ABCABD"），随机字符串优势不大
- BF 在实际中可能更快（常数小，现代 CPU 缓存友好）


## 来源与依据

- 课程导航：[[../00_数据结构_课程MOC|数据结构 MOC]]

- 课程导航：[[../00_数据结构_课程MOC|数据结构 MOC]]

- 来源文件：[[91_Raw-Archive/PDF/DS_DataStructure(1).pdf_课件_未知日期_dfdfb9d1.pdf]]
- 页码：DataStructure(1).pdf（99页完整讲义，作者 LI LIANGJI）
- 核对说明：本笔记基于提取版 PDF 内容蒸馏。所有代码示例和公式来自原始课件，需人工核对。当前 `needs_review: true`。
