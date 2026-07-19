---
id: db-sql-join
type: concept
status: cleaned
course: DB
source:
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"
source_pages:
  - "待核对"
source_hash:
  - "e0ddeaf5f016da34ee5e7939aa12e78382df1f7a9e6aecb0eb1c078fe18173bc"
  - "a3a72c6ec0ddb226f6aebf5cdd0db9cdac7a87eb16489e3799034df9f26e4716"
  - "69fc8513539e37a6ba5959cd7c52687f95e2d9b669fac3c0cb308cc50354d54a"
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
  - sql
  - join
---

# SQL连接查询

## 一句话解释

连接查询从多个表中获取数据，通过连接条件将相关联的行组合在一起。

## 核心原理

**内连接（INNER JOIN）**：只返回满足连接条件的行
**外连接（OUTER JOIN）**：
- LEFT JOIN：保留左表所有行，右表无匹配时填 NULL
- RIGHT JOIN：保留右表所有行，左表无匹配时填 NULL
- FULL JOIN：保留两表所有行

**自然连接（NATURAL JOIN）**：自动在公共属性上做等值连接并去重

**自连接**：表与自身连接，需要使用别名区分

## 前置知识

- [[SQL单表查询]]
- [[关系代数基本运算]]

## 规则或公式

内连接语法：
```sql
SELECT ... FROM 表1 [INNER] JOIN 表2 ON 连接条件
```
等价于：
```sql
SELECT ... FROM 表1, 表2 WHERE 连接条件
```

## 完整例子

```sql
-- 查询学生姓名及选课成绩（内连接）
SELECT sname, cno, grade
FROM Student INNER JOIN SC ON Student.sno = SC.sno;

-- 左外连接：所有学生（含未选课的）
SELECT sname, cno, grade
FROM Student LEFT JOIN SC ON Student.sno = SC.sno;

-- 自连接：查找同名不同学号的学生
SELECT a.sno, a.sname FROM Student a, Student b
WHERE a.sname = b.sname AND a.sno <> b.sno;
```

## 容易出错的地方

- 忘记连接条件 → 笛卡儿积（结果爆炸）
- 多表连接时列名冲突 → 必须用 表名.列名 或 别名.列名
- LEFT JOIN 和 RIGHT JOIN 不对称（ON 只影响连接，WHERE 影响最终结果）

## 与其他知识点的关系

- 理论基础：[[关系代数基本运算]]
- 子查询替代：[[SQL嵌套查询]]


## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
