---
id: db-bcnf
type: concept
status: cleaned
course: DB
source:
  - "[[91_Raw-Archive/DOC/DB_06_关系数据理论_练习_未知日期_6fbbe6df.docx]]"
  - "[[91_Raw-Archive/DOC/DB_06_关系数据理论_练习_未知日期_3003fda0.docx]]"
  - "[[91_Raw-Archive/PDF/DB_06_关系数据理论_课件_未知日期_34513e15.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_06_关系数据理论_课件_未知日期_33aefea0.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_07_数据库设计_课件_未知日期_a1457c90.pdf]]"
source_pages:
  - "待核对"
source_hash:
  - "6fbbe6dfd6d75e22eeac74a55a8bba273b201c4a307ef7f82810ddb6811824f2"
  - "3003fda0076e6a410d500acce536851bf5f8443b3f45fc363ebb214642feabb6"
  - "34513e159595d3d968f24797d28c997a7360777e4c40ed5de5ab466283465cd6"
  - "33aefea097bbde08453eb393f483c82a8f074befc88876aafd64a50a84531757"
  - "a1457c90ade9e563ce4a4912a6b4ff4bc338ac9362132a972584b10b784df7a2"
created: 2026-07-16
updated: 2026-07-16
verified_by: ""
mastery: unknown
importance: high
confidence: medium
verification: inferred
needs_review: true
review_reason: "AI从提取版蒸馏生成，需人工与原课件核对事实、公式和例子"
tags:
  - database
  - normalization
  - bcnf
---

# BCNF

## 一句话解释

BCNF 是 3NF 的加强版，要求每个非平凡函数依赖的决定因素都是候选码（超码）。

## 核心原理

**BCNF（Boyce-Codd Normal Form）**：对 F 中每个非平凡函数依赖 X → Y，X 必须是超码（包含候选码）。

BCNF 消除了 3NF 中仍然可能存在的主属性对候选码的部分/传递依赖问题。

## 前置知识

- [[第三范式]]
- [[函数依赖]]

## 规则或公式

BCNF：∀ X → Y ∈ F⁺（X → Y 非平凡），X 必含候选码

**范式层级**：1NF ⊃ 2NF ⊃ 3NF ⊃ BCNF ⊃ 4NF

## 完整例子

R(sno, cno, tno)，假设一个老师只教一门课：
- F = {(sno, cno) → tno, tno → cno}
- 候选码：{sno, cno}, {sno, tno}
- 检查 tno → cno：tno 是决定因素但不是超码 → **不满足 BCNF**

分解为 BCNF：
- R1(tno, cno)，候选码 tno
- R2(sno, tno)，候选码 {sno, tno}

## 容易出错的地方

- 3NF 满足但 BCNF 不满足 → 存在主属性对候选码的部分/传递依赖
- 实际中大部分关系都能达到 BCNF，少数需要权衡（保持函数依赖 vs BCNF）
- BCNF 分解可能丢失函数依赖（这是 3NF 仍有价值的场景）

## 与其他知识点的关系

- 前置：[[第三范式]]
- 选择依据：[[数据库设计流程]]


## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/DOC/DB_06_关系数据理论_练习_未知日期_6fbbe6df.docx]]"
  - "[[91_Raw-Archive/DOC/DB_06_关系数据理论_练习_未知日期_3003fda0.docx]]"
  - "[[91_Raw-Archive/PDF/DB_06_关系数据理论_课件_未知日期_34513e15.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_06_关系数据理论_课件_未知日期_33aefea0.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_07_数据库设计_课件_未知日期_a1457c90.pdf]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
