---
id: db-chapter-03
type: chapter
status: cleaned
course: DB
chapter: 3
title: SQL语言
created: 2026-07-17
updated: 2026-07-17
mastery: unknown
needs_review: true
review_reason: "待与原始课件核对"
tags: [database, sql]
---

# 第3章 SQL 语言

> 本章是考试和应用的核心：写对 SQL 语句。

## 本章核心概念

| 概念 | 一句话 | 详情 |
|------|--------|------|
| DDL | CREATE/DROP/ALTER 定义数据库对象 | [[02_知识点/SQL数据定义]] |
| 单表查询 | SELECT-FROM-WHERE 基本结构 | [[02_知识点/SQL单表查询]] |
| 连接查询 | INNER/LEFT/RIGHT JOIN 多表查询 | [[02_知识点/SQL连接查询]] |
| 嵌套查询 | WHERE 子句中嵌套 SELECT | [[02_知识点/SQL嵌套查询]] |
| 聚合分组 | COUNT/SUM/AVG + GROUP BY + HAVING | [[02_知识点/SQL聚合与分组]] |
| 视图 | 基于查询的虚拟表 | [[02_知识点/视图]] |

## 复习要点

1. SQL 三大组成部分（DDL/DML/DCL）及对应动词
2. SELECT 语句的执行顺序（FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY）
3. WHERE vs HAVING
4. 内连接 vs 外连接（LEFT/RIGHT/FULL）
5. 不相关子查询 vs 相关子查询
6. IN vs EXISTS 的使用场景
7. 聚合函数与 GROUP BY：SELECT 中非聚合列必须出现在 GROUP BY 中
8. LIKE 模糊匹配、NULL 判断、DISTINCT 去重

## SQL 速查

```sql
-- 基本查询
SELECT [DISTINCT] 列 FROM 表 WHERE 条件 ORDER BY 列 [ASC|DESC];

-- 连接
SELECT ... FROM A JOIN B ON A.x = B.x;           -- 内连接
SELECT ... FROM A LEFT JOIN B ON A.x = B.x;      -- 左外连接

-- 子查询
SELECT ... FROM 表 WHERE 列 IN (SELECT ...);       -- IN子查询
SELECT ... FROM 表 WHERE EXISTS (SELECT ...);      -- EXISTS子查询

-- 聚合
SELECT 列, COUNT(*) FROM 表 GROUP BY 列 HAVING COUNT(*) > N;

-- 视图
CREATE VIEW 视图名 AS SELECT ...;
```

## 最容易出错的 SQL 写法

1. `WHERE grade = NULL` ❌ → `WHERE grade IS NULL` ✓
2. `WHERE AVG(grade) > 80` ❌ → `HAVING AVG(grade) > 80` ✓
3. `SELECT sno, AVG(grade) FROM SC` ❌ → 需要 `GROUP BY sno` ✓
4. 连接忘记 ON 条件 → 笛卡儿积爆炸

## 来源

- PDF：`DB_03_SQL_课件_未知日期_e0ddeaf5.pdf`
- PDF（旧版）：`DB_03_SQL_课件_未知日期_a3a72c6e.pdf`
- 学生笔记：`学生笔记_第三章 关系数据库标准语言（SQL）.md`

---
> 课程导航：[[../00_数据库课程MOC|数据库 MOC]]
