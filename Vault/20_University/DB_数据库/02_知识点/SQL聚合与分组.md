---
id: db-sql-aggregation
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
  - aggregation
---

# SQL聚合与分组

## 一句话解释

聚合函数对一组值执行计算并返回单一值，GROUP BY 将数据按指定列分组后应用聚合函数。

## 核心原理

**聚合函数**：
- COUNT(*)：计数（含 NULL）
- COUNT(列名)：计数（不含 NULL）
- SUM(列名)：求和
- AVG(列名)：平均值
- MAX(列名)：最大值
- MIN(列名)：最小值

**GROUP BY**：按指定列的值分组，每组返回一个结果
**HAVING**：对分组结果进行过滤（类似 WHERE 对行过滤）

## 前置知识

- [[SQL单表查询]]

## 规则或公式

执行顺序：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
- WHERE 不能使用聚合函数（WHERE 在分组前执行）
- HAVING 可以使用聚合函数（HAVING 在分组后执行）

## 完整例子

```sql
-- 各系学生人数
SELECT sdept, COUNT(*) FROM Student GROUP BY sdept;

-- 平均分 >= 80 的课程（排除不及格后）
SELECT cno, AVG(grade) as avg_grade
FROM SC WHERE grade >= 60
GROUP BY cno HAVING AVG(grade) >= 80;

-- 最高分和最低分
SELECT cno, MAX(grade), MIN(grade) FROM SC GROUP BY cno;
```

## 容易出错的地方

- SELECT 子句中非聚合列必须出现在 GROUP BY 中
- WHERE vs HAVING 混淆
- COUNT(*) 和 COUNT(列名) 的区别（NULL 处理不同）
- AVG 自动忽略 NULL，SUM 也忽略 NULL

## 与其他知识点的关系

- 前置：[[SQL单表查询]]
- 前置：[[SQL嵌套查询]]
## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
