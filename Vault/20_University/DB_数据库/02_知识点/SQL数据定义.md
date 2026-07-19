---
id: db-sql-ddl
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
  - ddl
---

# SQL数据定义

## 一句话解释

SQL 数据定义语言（DDL）用于创建、修改和删除数据库对象（模式、表、视图、索引）。

## 核心原理

SQL 的三大组成部分：
- **DDL（Data Definition Language）**：CREATE, DROP, ALTER
- **DML（Data Manipulation Language）**：INSERT, UPDATE, DELETE, SELECT
- **DCL（Data Control Language）**：GRANT, REVOKE

## 前置知识

- [[三级模式与两级映像]]

## 规则或公式

| 操作对象 | CREATE | DROP | ALTER |
|---------|--------|------|-------|
| SCHEMA | CREATE SCHEMA | DROP SCHEMA | — |
| TABLE | CREATE TABLE | DROP TABLE | ALTER TABLE |
| VIEW | CREATE VIEW | DROP VIEW | — |
| INDEX | CREATE INDEX | DROP INDEX | ALTER INDEX |

常用数据类型：CHAR(n)（定长字符）, VARCHAR(n)（变长字符）, INT, FLOAT, DECIMAL(p,s), DATE, BOOLEAN

## 完整例子

```sql
CREATE TABLE Student (
    sno   CHAR(9) PRIMARY KEY,
    sname VARCHAR(20) NOT NULL,
    ssex  CHAR(2),
    sage  INT,
    sdept VARCHAR(20)
);

ALTER TABLE Student ADD sphone VARCHAR(20);
DROP TABLE Student;
```

## 容易出错的地方

- CHAR 和 VARCHAR 的区别：CHAR 定长（不足补空格），VARCHAR 变长
- DROP 和 DELETE 完全不同：DROP 删除表结构+数据，DELETE 只删数据
- 不同 DBMS 的 DDL 语法有细微差异

## 与其他知识点的关系

- 后续：[[SQL单表查询]]、[[SQL连接查询]]
- 进阶：[[视图]]


## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_e0ddeaf5.pdf]]"
  - "[[91_Raw-Archive/PDF/DB_03_SQL_课件_未知日期_a3a72c6e.pdf]]"
  - "[[91_Raw-Archive/PPT/DB_03_SQL_课件_未知日期_69fc8513.ppt]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
