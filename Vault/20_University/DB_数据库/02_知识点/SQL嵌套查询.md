---
id: db-sql-nested-query
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
  - subquery
---

# SQL嵌套查询

## 一句话解释

嵌套查询将一个查询块嵌套在另一个查询块的 WHERE 或 HAVING 子句中，实现分步求解。

## 核心原理

**不相关子查询**：子查询独立于外层，只执行一次
**相关子查询**：子查询引用外层表的列，对外层每一行重新执行

常用谓词：
- IN / NOT IN：判断值是否在子查询结果集中
- EXISTS / NOT EXISTS：判断子查询是否有返回行
- 比较运算符 + ANY/SOME/ALL：与子查询结果集比较

## 前置知识

- [[SQL单表查询]]

## 规则或公式

- = ANY(subquery) ≈ IN(subquery)
- > ALL(subquery)：大于子查询中所有值（即大于最大值）
- EXISTS 通常比 IN 效率更高（可短路）

## 完整例子

```sql
-- 不相关子查询：CS 系学生的选课记录
SELECT * FROM SC WHERE sno IN
  (SELECT sno FROM Student WHERE sdept = 'CS');

-- 相关子查询：成绩高于该课程平均分的学生
SELECT sno, cno, grade FROM SC x
WHERE grade > (SELECT AVG(grade) FROM SC y WHERE y.cno = x.cno);

-- EXISTS：至少选了一门课的学生
SELECT * FROM Student WHERE EXISTS
  (SELECT * FROM SC WHERE SC.sno = Student.sno);
```

## 容易出错的地方

- 子查询 SELECT 语句中不写 ORDER BY（无意义）
- 不相关子查询效率通常优于相关子查询
- 当子查询可能返回 NULL 时，NOT IN 会出问题（NULL 不属于任何集合）

## 与其他知识点的关系

- 前置：[[SQL单表查询]]
- 对比概念：[[SQL连接查询]]
- 后续：[[SQL聚合与分组]]
## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
