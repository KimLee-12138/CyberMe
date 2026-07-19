---
id: db-sql-select-single
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
  - query
---

# SQL单表查询

## 一句话解释

SELECT-FROM-WHERE 是 SQL 查询的基本结构，实现关系代数的选择、投影和排序。

## 核心原理

基本查询格式：
```sql
SELECT [DISTINCT] 列名/表达式
FROM 表名
WHERE 条件
[GROUP BY 列名 [HAVING 条件]]
[ORDER BY 列名 [ASC|DESC]];
```

执行顺序理解（逻辑顺序）：
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

常用 WHERE 条件：
- 比较：=, <>, <, >, <=, >=, BETWEEN, IN
- 模糊匹配：LIKE（% 任意多个字符，_ 单个字符）
- 空值判断：IS NULL, IS NOT NULL
- 逻辑组合：AND, OR, NOT

## 前置知识

- [[SQL数据定义]]

## 规则或公式

SELECT 子句中的 DISTINCT 消除重复行。没有 DISTINCT 时默认为 ALL（保留重复）。

## 完整例子

```sql
-- 查询 CS 系年龄小于 20 的学生姓名
SELECT sname FROM Student WHERE sdept = 'CS' AND sage < 20;

-- 查询姓名含"张"的学生（模糊查询）
SELECT * FROM Student WHERE sname LIKE '张%';

-- 查询有成绩的学生学号（去重）
SELECT DISTINCT sno FROM SC WHERE grade IS NOT NULL;

-- 按年龄降序排列
SELECT * FROM Student ORDER BY sage DESC;
```

## 容易出错的地方

- WHERE 和 HAVING 的区别：WHERE 过滤行（分组前），HAVING 过滤组（分组后）
- LIKE 区分大小写因 DBMS 而异
- NULL 不能用 = 判断，必须用 IS NULL
- ORDER BY 的默认排序是 ASC

## 与其他知识点的关系

- 进阶：[[SQL连接查询]]、[[SQL嵌套查询]]、[[SQL聚合与分组]]


## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
