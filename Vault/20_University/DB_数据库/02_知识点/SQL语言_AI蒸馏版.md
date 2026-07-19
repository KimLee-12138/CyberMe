---
id: note-db-sql-ch3
type: knowledge-note
status: formal
course: DB
chapter: 3
title: 关系数据库标准语言（SQL）
created: 2026-07-16
updated: 2026-07-16
tags:
  - SQL
  - 关系数据库
  - 数据定义
  - 数据查询
---

# 第三章 关系数据库标准语言（SQL）

## 总结

SQL（Structured Query Language）是关系数据库的标准语言，集数据定义、数据操纵和数据控制于一体。本章系统介绍了SQL的基本概念、特点、数据定义功能（模式、基本表、索引的创建与删除）以及数据查询功能（SELECT语句的完整语法与使用）。SQL以其高度非过程化、面向集合的操作方式和简洁的语法结构，成为数据库操作的核心工具。掌握SQL是进行数据库应用开发的基础。

## 核心概念

- **SQL（结构化查询语言）**：关系数据库的标准语言，支持三级模式结构（外模式、模式、内模式）。
- **视图（View）**：从一个或几个基本表导出的虚表，只存储定义而不存储数据。
- **模式（Schema）**：数据库对象的命名空间，包含表、视图、索引等对象。
- **基本表（Base Table）**：独立存在的表，是数据库中实际存储数据的对象。
- **索引（Index）**：加快查询速度的数据结构，由DBMS自动维护。
- **聚簇索引（Cluster Index）**：改变表中数据物理存储顺序的索引，一个表只能有一个。
- **主码（Primary Key）**：唯一标识表中每一行记录的属性或属性组合，自动建立索引并包含非空约束。
- **外码（Foreign Key）**：引用其他表主码的属性，用于维护表之间的参照完整性。

## 知识点

### 1. SQL的特点

SQL具有五大特点：
- **综合统一**：集DDL、DML、DCL于一体
- **高度非过程化**：只需提出“做什么”，无需指明“怎么做”
- **面向集合的操作方式**：增删改查的对象可以是元组的集合
- **以同一种语法结构提供多种使用方式**：既可独立使用，也可嵌入高级语言
- **语言简洁，易学易用**：核心功能仅用9个动词

SQL功能与动词对应关系：

| SQL功能 | 动词 |
|:-------:|:----:|
| 数据查询 | SELECT |
| 数据定义 | CREATE、DROP、ALTER |
| 数据操纵 | INSERT、UPDATE、DELETE |
| 数据控制 | GRANT、REVOKE |

### 2. 数据定义

数据定义支持的操作对象及操作类型：

| 操作对象 | 创建 | 删除 | 修改 |
|:-------:|:----:|:----:|:----:|
| 模式 | ✓ | ✓ | |
| 表 | ✓ | ✓ | ✓ |
| 视图 | ✓ | ✓ | |
| 索引 | ✓ | ✓ | ✓ |

#### 模式的定义与删除

- 定义模式：`CREATE SCHEMA <模式名> AUTHORIZATION <用户名>`
  - 未指定模式名时，模式名隐含为用户名
- 删除模式：`DROP SCHEMA <模式名> <CASCADE | RESTRICT>`
  - `CASCADE`：级联删除模式及其所有对象
  - `RESTRICT`：有限制删除，存在依赖对象时拒绝删除

#### 基本表的定义与删除

**完整性约束**：
- `PRIMARY KEY`：主码约束，自动建立索引，包含非空约束
- `UNIQUE`：唯一性约束，允许为空
- `NOT NULL`：非空值约束
- `FOREIGN KEY`：外码约束，维护参照完整性

**示例**：学生-课程数据库基本表定义

```sql
CREATE TABLE Student(
    Sno CHAR(9) PRIMARY KEY,
    Sname CHAR(20) UNIQUE,
    Ssex CHAR(2),
    Sage SMALLINT,
    Sdept CHAR(20)
);

CREATE TABLE Course(
    Cno CHAR(4) PRIMARY KEY,
    Cname CHAR(40) NOT NULL,
    Cpno CHAR(4),  /* 先修课 */
    Ccredit SMALLINT,
    FOREIGN KEY (Cpno) REFERENCES Course(Cno)
);

CREATE TABLE SC(
    Sno CHAR(9),
    Cno CHAR(4),
    Grade SMALLINT,
    PRIMARY KEY (Sno, Cno),
    FOREIGN KEY (Sno) REFERENCES Student(Sno),
    FOREIGN KEY (Cno) REFERENCES Course(Cno)
);
```

**删除基本表**：`DROP TABLE [RESTRICT|CASCADE]`
- `RESTRICT`：默认选项，存在依赖对象时拒绝删除
- `CASCADE`：级联删除所有依赖对象

#### 索引的建立与删除

索引是加快查询速度的有效手段，由DBMS自动维护。

```sql
CREATE [UNIQUE] [CLUSTER] INDEX <索引名>
ON <表名> (<列名>[<次序>] [,<列名> [<次序>]] ...);
```

- `<次序>`：`ASC`（升序，默认）或 `DESC`（降序）
- `UNIQUE`：索引值唯一对应一条数据记录
- `CLUSTER`：建立聚簇索引，改变数据物理存储顺序

### 3. 数据查询（SELECT语句）

#### 语句格式

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>]
FROM <表名或视图名> [,<表名或视图名>]
[WHERE <条件表达式>]
[GROUP BY <列名1> [HAVING <条件表达式>]]
[ORDER BY <列名2> [ASC|DESC] [,<列名3> [ASC|DESC]]]
```

#### 选择表中的若干列

- 查询全部列：`SELECT * FROM <表名>`
- 目标列表达式可以是：
  - 算术表达式：`SELECT 2024-Sage FROM Student`（查询出生年份）
  - 字符串常量：`SELECT 'Name:', Sname FROM Student`
  - 函数：`SELECT LOWER(Sdept) FROM Student`
- 指定别名：`SELECT 2024-Sage BIRTHDAY FROM Student`

#### 选择表中的若干元组

**消除重复行**：`SELECT DISTINCT Sno FROM SC`

**WHERE子句查询条件**：

| 查询条件 | 谓词 |
|:--------:|:----:|
| 比较 | `=, >, <, >=, <=, !=, <>, !>, !<` |
| 确定范围 | `BETWEEN AND, NOT BETWEEN AND` |
| 确定集合 | `IN, NOT IN` |
| 字符匹配 | `LIKE, NOT LIKE` |
| 空值 | `IS NULL, IS NOT NULL` |
| 多重条件 | `AND, OR, NOT` |

**字符匹配（LIKE）**：
- 语法：`[NOT] LIKE '<匹配串>' [ESCAPE '<换码字符>']`
- 通配符：
  - `%`：代表任意长度（可为0）的字符串
  - `_`：代表任意单个字符
- 示例：
  - `SELECT * FROM Student WHERE Sname LIKE '刘%'`（所有刘姓同学）
  - `SELECT * FROM Student WHERE Sname LIKE '李_'`（李姓且名字为两个字）
- 转义字符：`ESCAPE`定义转义字符，使其后的通配符按原始字符匹配

## 易错点

1. **主码与UNIQUE的区别**：主码自动包含非空约束，而UNIQUE允许为空值。一个表只能有一个主码，但可以有多个UNIQUE约束。

2. **外码引用自身**：在Course表中，Cpno引用自身的Cno作为外码，表示先修课程关系。这种自引用需要特别注意参照完整性的维护。

3. **复合主码的定义**：当主码由多个属性构成时，必须使用表级完整性约束定义，如`PRIMARY KEY (Sno, Cno)`。

4. **DROP TABLE的级联删除**：使用`CASCADE`选项时，不仅删除表本身，还会删除所有依赖该表的视图、触发器、存储过程等对象，操作不可逆。

5. **DISTINCT的作用范围**：`DISTINCT`作用于SELECT后所有列的组合，而非单个列。例如`SELECT DISTINCT Sno, Cno`会消除Sno和Cno组合重复的行。

6. **LIKE通配符的转义**：当需要匹配包含`%`或`_`的字符串时，必须使用`ESCAPE`定义转义字符，否则通配符会被解释。

7. **BETWEEN AND的边界**：`BETWEEN 20 AND 23`包含边界值20和23，即`Sage >= 20 AND Sage <= 23`。

8. **NULL值的处理**：NULL不等于任何值，包括NULL本身。判断空值必须使用`IS NULL`或`IS NOT NULL`，不能使用`= NULL`或`!= NULL`。

9. **聚簇索引的限制**：一个表只能创建一个聚簇索引，因为数据物理存储顺序只能有一种。聚簇索引会改变数据在磁盘上的物理排列。

10. **视图与基本表的区别**：视图是虚表，不存储实际数据，只存储定义。对视图的查询最终会转换为对基本表的查询。