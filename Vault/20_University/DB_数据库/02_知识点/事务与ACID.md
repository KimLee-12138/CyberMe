---
id: db-transaction-acid
type: concept
status: cleaned
course: DB
source:
  - "[[91_Raw-Archive/PDF/DB_10_事务与恢复_课件_未知日期_d6b3648c.pdf]]"
source_pages:
  - "待核对"
source_hash:
  - "d6b3648c1f2fdf59e5b9110ebbe7bf17dd713fdb79a18999d27ff07821ddb673"
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
  - transaction
  - acid
---

# 事务与ACID

## 一句话解释

事务是用户定义的一个数据库操作序列，这些操作要么全做要么全不做，ACID 是其四个基本特性。

## 核心原理

**事务（Transaction）**：一个不可分割的工作单位。以 BEGIN TRANSACTION 开始，以 COMMIT（提交）或 ROLLBACK（回滚）结束。

**ACID 特性**：
- **原子性（Atomicity）**：事务中所有操作要么全部执行，要么全部不执行
- **一致性（Consistency）**：事务执行前后数据库都处于一致性状态
- **隔离性（Isolation）**：并发事务之间互不干扰
- **持久性（Durability）**：已提交事务的结果永久保存

## 前置知识

- [[数据与数据库]]

## 规则或公式

事务状态变迁：
活动状态 →（最后一条语句）→ 部分提交状态 →（COMMIT）→ 提交状态
                                             →（故障）→ 失败状态 →（ROLLBACK）→ 中止状态

## 完整例子

银行转账（A 账户转 100 元到 B 账户）：
```sql
BEGIN TRANSACTION;
UPDATE account SET balance = balance - 100 WHERE id = 'A';
UPDATE account SET balance = balance + 100 WHERE id = 'B';
COMMIT;
```
- 两条 UPDATE 必须全部成功或全部失败（原子性）
- 转账前后总金额不变（一致性）
- 其他事务不会看到转账中间状态（隔离性）
- COMMIT 后即使系统崩溃也不丢失（持久性）

## 容易出错的地方

- ACID 各特性相互关联，不是孤立的
- 一致性主要靠程序员保证（写正确的事务逻辑）
- 隔离性有不同的级别（读未提交、读已提交、可重复读、可串行化）

## 与其他知识点的关系

- 并发问题：[[并发异常]]
- 恢复机制：[[数据库恢复]]


## 来源与依据

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

- 课程导航：[[../00_数据库课程MOC|数据库 MOC]]

  - "[[91_Raw-Archive/PDF/DB_10_事务与恢复_课件_未知日期_d6b3648c.pdf]]"

- 页码：待核对
- 核对说明：本笔记由 AI 从 `91_Raw-Archive` 第一批归档 PDF 的提取版和现有学生笔记蒸馏生成。所有事实、公式和例子需要在阶段五与原始课件逐项核对。当前 `needs_review: true`。
