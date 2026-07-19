---
id: db-sql
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# SQL 语言

## 一、数据定义(DDL)

```sql
CREATE TABLE Student (
    Sno CHAR(9) PRIMARY KEY,
    Sname VARCHAR(20) NOT NULL,
    Sage INT CHECK(Sage>0),
    Sdept VARCHAR(20)
);
ALTER TABLE Student ADD Sphone CHAR(11);
DROP TABLE Student;
```

## 二、单表查询

```sql
SELECT [DISTINCT] 列名
FROM 表名
WHERE 条件
GROUP BY 列名 HAVING 分组条件
ORDER BY 列名 ASC/DESC;
```

**WHERE vs HAVING**：WHERE 作用于原始行，HAVING 作用于分组后的组。

## 三、连接查询

**自然连接**：`FROM A NATURAL JOIN B`

**内连接**：`FROM A INNER JOIN B ON A.x = B.y`

**外连接**：
- LEFT OUTER JOIN：保留左表所有行
- RIGHT OUTER JOIN：保留右表所有行
- FULL OUTER JOIN：保留两表所有行

## 四、嵌套查询

```sql
-- IN 子查询
SELECT Sname FROM Student WHERE Sno IN
    (SELECT Sno FROM SC WHERE Cno='1');

-- EXISTS 子查询(相关子查询)
SELECT Sname FROM Student WHERE EXISTS
    (SELECT * FROM SC WHERE SC.Sno=Student.Sno AND Cno='1');
```

**IN vs EXISTS**：IN 先执行子查询；EXISTS 是相关子查询，外层每行执行一次子查询。

## 五、聚合函数

| 函数 | 作用 |
|------|------|
| COUNT(*) | 计数 |
| SUM(col) | 求和 |
| AVG(col) | 平均值 |
| MAX/MIN | 最大/最小 |

## 六、数据更新

```sql
INSERT INTO Table VALUES (...);
UPDATE Table SET col=val WHERE ...;
DELETE FROM Table WHERE ...;
```

## 七、视图

```sql
CREATE VIEW ViewName AS SELECT ...;
```

视图是虚拟表，不存储实际数据。可简化复杂查询、提高安全性。

## 八、索引

```sql
CREATE INDEX idx ON Table(col);
```

**B+树索引**最常用。索引提高查询速度但降低增删改速度。

---

## 相关链接
- [[关系模型]] — SQL 的理论基础
- [[数据库设计]] — SQL DDL 建表
