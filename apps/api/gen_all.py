"""Generate ALL remaining course documents in one shot."""
import os

VAULT = r"C:\Users\22067\Desktop\李尚凯蒸馏\CyberMe-Vault\20_University"

COURSES = {}

# ============================================================
# DB_数据库 — 数据库系统 (high priority)
# ============================================================
COURSES["DB_数据库"] = {
    "code": "DB",
    "moc": """---
course: DB
type: moc
status: active
created: 2026-07-17
updated: 2026-07-18
---

# 数据库系统 — 课程 MOC

> 从关系代数到 SQL，从范式理论到事务处理。数据库是软件系统的核心。

## 知识结构

### 一、基础篇
- [[数据库系统概论]] — 数据模型、三级模式、数据库语言
- [[关系模型]] — 关系代数、关系演算、完整性约束

### 二、SQL
- [[SQL语言]] — DDL/DML/DCL、单表查询、连接查询、嵌套查询、聚合函数

### 三、数据库设计
- [[关系数据理论]] — 函数依赖、范式(1NF/2NF/3NF/BCNF)、模式分解
- [[数据库设计]] — E-R图、逻辑设计、物理设计

### 四、数据库管理
- [[事务与并发控制]] — ACID、封锁协议、死锁
- [[数据库恢复与安全]] — 故障类型、日志、备份恢复、安全性控制

## 参考资料
""",
    "docs": {
        "数据库系统概论.md": """---
id: db-overview
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 数据库系统概论

## 一、数据模型的三要素

**数据结构、数据操作、完整性约束**。

### 1.1 三种数据模型

| 模型 | 特点 | 代表 |
|------|------|------|
| 层次模型 | 树形结构，1:N | IMS |
| 网状模型 | 图结构，M:N | DBTG |
| **关系模型** | 二维表，最主流 | MySQL, PostgreSQL, Oracle |

### 1.2 数据库系统的三级模式结构

```
外模式(用户视图) → 概念模式(全局逻辑) → 内模式(物理存储)
```

两级映像：外模式/概念模式映像、概念模式/内模式映像 → **数据独立性**。

## 二、数据库语言

| 类型 | 功能 | SQL 示例 |
|------|------|---------|
| DDL | 数据定义 | CREATE/ALTER/DROP |
| DML | 数据操纵 | SELECT/INSERT/UPDATE/DELETE |
| DCL | 数据控制 | GRANT/REVOKE |
| TCL | 事务控制 | COMMIT/ROLLBACK |

## 三、数据独立性

**物理独立性**：修改物理存储不影响应用程序
**逻辑独立性**：修改概念模式不影响外模式

## 四、DBMS 的功能

1. 数据定义与存储管理
2. 查询处理与优化
3. 事务管理与并发控制
4. 安全性控制与完整性维护
5. 备份与恢复

---

## 相关链接
- [[关系模型]] — 关系代数
- [[SQL语言]] — SQL 语法
""",

        "关系模型.md": """---
id: db-relational
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 关系模型

## 一、基本概念

| 术语 | 含义 |
|------|------|
| **关系** | 一张二维表 |
| **元组** | 行 |
| **属性** | 列 |
| **域** | 属性的取值范围 |
| **候选码** | 能唯一标识元组的最小属性组 |
| **主码** | 选定的候选码 |
| **外码** | 引用其他关系主码的属性 |

## 二、关系代数

### 2.1 集合运算

| 运算 | 符号 | 条件 |
|------|------|------|
| 并 | $R \\cup S$ | 同目，对应属性域相同 |
| 差 | $R - S$ | 同上 |
| 交 | $R \\cap S$ | 同上 |
| 笛卡尔积 | $R \\times S$ | 无 |

### 2.2 专门的关系运算

| 运算 | 符号 | 说明 |
|------|------|------|
| **选择** | $\\sigma_F(R)$ | 选取满足条件F的元组(水平切割) |
| **投影** | $\\Pi_A(R)$ | 选取指定的属性列(垂直切割) |
| **连接** | $R \\bowtie_{F} S$ | 满足条件的元组拼接 |
| 等值连接 | $R \\bowtie_{A=B} S$ | — |
| 自然连接 | $R \\bowtie S$ | 同名属性等值连接+去重 |
| 外连接 | ⟕ / ⟖ / ⟗ | 保留悬浮元组 |
| **除** | $R \\div S$ | "满足所有..." |

## 三、关系完整性

| 类型 | 定义 |
|------|------|
| **实体完整性** | 主码不能为空 |
| **参照完整性** | 外码要么为空，要么等于被参照关系中的主码 |
| **用户定义完整性** | 业务规则(如年龄>0) |

---

## 相关链接
- [[SQL语言]] — 关系代数的 SQL 实现
- [[关系数据理论]] — 范式理论
""",

        "SQL语言.md": """---
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
""",

        "关系数据理论.md": """---
id: db-normalization
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 关系数据理论（范式）

## 一、函数依赖

**定义**：$X \\to Y$ 表示 X 的值唯一确定 Y 的值。

| 类型 | 定义 |
|------|------|
| 平凡函数依赖 | $Y \\subseteq X$ |
| 非平凡函数依赖 | $Y \\not\\subseteq X$ |
| 完全函数依赖 | X中任何真子集都不能决定Y |
| 部分函数依赖 | X的真子集可以决定Y |
| 传递函数依赖 | $X\\to Y, Y\\to Z, Y\\not\\to X$ |

## 二、码

**候选码**：能完全函数决定所有属性，且任何真子集不行。

**求候选码**：从最小属性集开始，逐步加入直到能决定所有属性。

## 三、范式

### 1NF：属性不可再分（最基本要求）

### 2NF：消除非主属性对码的**部分**函数依赖

### 3NF：消除非主属性对码的**传递**函数依赖

### BCNF：消除主属性对码的部分和传递函数依赖

**判断口诀**：每一个决定因素都包含码 → BCNF

## 四、范式判断流程

```
是否满足1NF？→否→非规范化
    ↓是
是否满足2NF？→否→1NF
    ↓是
是否满足3NF？→否→2NF
    ↓是
是否满足BCNF？→否→3NF
    ↓是 → BCNF
```

## 五、模式分解

| 要求 | 说明 |
|------|------|
| **无损连接** | 分解后自然连接可还原原关系 |
| **保持函数依赖** | 分解后所有FD可推导 |

3NF 分解可同时满足无损连接+保持函数依赖。BCNF 分解只能保证无损连接。

---

## 相关链接
- [[关系模型]] — 关系的基本概念
- [[数据库设计]] — E-R图到关系模式
""",

        "数据库设计.md": """---
id: db-design
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: high
---

# 数据库设计

## 一、设计步骤

1. **需求分析** → 数据流图/数据字典
2. **概念结构设计** → E-R图
3. **逻辑结构设计** → E-R图→关系模式
4. **物理结构设计** → 索引/存储结构
5. **数据库实施** → 建表/加载数据
6. **运行维护** → 调优/备份

## 二、E-R 图

| 元素 | 图形 | 说明 |
|------|------|------|
| 实体 | 矩形 | 对象 |
| 属性 | 椭圆 | 特征 |
| 联系 | 菱形 | 实体间关系 |

**联系类型**：1:1 / 1:N / M:N

## 三、E-R 图→关系模式

| 联系类型 | 转换方法 |
|---------|---------|
| 1:1 | 任选一方的码加入另一方 |
| 1:N | N 方加入 1 方的码 |
| M:N | 单独建表，包含双方的主码 |

## 四、物理设计

- 索引选择（B+树/哈希）
- 聚簇设计
- 分区策略

---

## 相关链接
- [[关系数据理论]] — 范式
- [[SQL语言]] — DDL
""",

        "事务与并发控制.md": """---
id: db-transaction
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 事务与并发控制

## 一、事务的 ACID 特性

| 特性 | 含义 |
|------|------|
| **A**tomicity 原子性 | 全做或全不做 |
| **C**onsistency 一致性 | 事务前后数据库满足完整性约束 |
| **I**solation 隔离性 | 并发事务互不干扰 |
| **D**urability 持久性 | 提交后永久保存 |

## 二、并发异常

| 异常 | 说明 |
|------|------|
| 丢失修改 | 两个事务同时修改，一个覆盖另一个 |
| 脏读 | 读到未提交的数据 |
| 不可重复读 | 同一事务两次读到不同值 |
| 幻读 | 同一事务两次查询结果集不同 |

## 三、封锁

### 3.1 锁类型

| 锁 | 符号 | 说明 |
|----|------|------|
| 共享锁 | S 锁 | 可读，不可写 |
| 排他锁 | X 锁 | 不可读写 |

**相容矩阵**：S与S相容，其他互斥。

### 3.2 封锁协议

| 级别 | 协议 | 防止 |
|------|------|------|
| 一级 | 写前加X锁，事务结束释放 | 丢失修改 |
| 二级 | 一级+读前加S锁，读完释放 | 脏读 |
| **三级(两段锁)** | 所有锁在事务结束才释放 | 可重复读 |

## 四、死锁

**预防**：一次封锁法、顺序封锁法

**检测与恢复**：等待图→有环→死锁→回滚某事务

## 五、隔离级别

| 级别 | 防止脏读 | 防止不可重复读 | 防止幻读 |
|------|---------|-------------|---------|
| Read Uncommitted | ✗ | ✗ | ✗ |
| Read Committed | ✓ | ✗ | ✗ |
| Repeatable Read | ✓ | ✓ | ✗ |
| Serializable | ✓ | ✓ | ✓ |

---

## 相关链接
- [[数据库恢复与安全]] — 日志与恢复
""",

        "数据库恢复与安全.md": """---
id: db-recovery
type: concept
status: active
course: DB
created: 2026-07-18
mastery: reviewing
importance: high
---

# 数据库恢复与安全

## 一、故障类型

| 故障 | 说明 | 恢复方法 |
|------|------|---------|
| 事务内部故障 | 逻辑错误(如除零) | 事务回滚(UNDO) |
| 系统故障 | 断电/死机(内存丢失) | UNDO未提交+REDO已提交 |
| 介质故障 | 磁盘损坏 | 备份+日志REDO |

## 二、日志

**先写日志原则(WAL)**：修改数据前先将日志写入稳定存储。

| 日志记录 | 内容 |
|---------|------|
| 旧值 | 修改前的值(UNDO用) |
| 新值 | 修改后的值(REDO用) |

## 三、备份与恢复

| 类型 | 说明 |
|------|------|
| 全量备份 | 完整数据库备份 |
| 增量备份 | 只备份上次备份后的变化 |
| 日志备份 | 备份事务日志 |

## 四、数据库安全性

| 措施 | 说明 |
|------|------|
| 身份认证 | 用户名/密码 |
| 存取控制 | GRANT/REVOKE 权限 |
| 视图机制 | 隐藏敏感数据 |
| 审计 | 记录操作日志 |
| 加密 | 数据传输和存储加密 |

## 五、SQL 权限控制

```sql
GRANT SELECT, INSERT ON TABLE TO user;
REVOKE DELETE ON TABLE FROM user;
```

---

## 相关链接
- [[事务与并发控制]] — ACID 特性
"""
    }
}

# ============================================================
# DS_数据结构
# ============================================================
COURSES["DS_数据结构"] = {
    "code": "DS",
    "moc": """---
course: DS
type: moc
status: active
created: 2026-07-17
updated: 2026-07-18
---

# 数据结构 — 课程 MOC

> 程序 = 数据结构 + 算法。线性表、栈队列、树、图、查找、排序六大模块。

## 知识结构

### 一、线性结构
- [[线性表]] — 顺序表、链表、循环链表、双向链表
- [[栈与队列]] — 顺序栈、链栈、循环队列、双端队列

### 二、树形结构
- [[二叉树]] — 性质、遍历、线索二叉树、哈夫曼树
- [[树与森林]] — 树的存储、树↔二叉树转换

### 三、图结构
- [[图的存储与遍历]] — 邻接矩阵/邻接表、DFS/BFS

### 四、查找
- [[查找算法]] — 顺序、二分、二叉排序树、平衡二叉树、B树/B+树、哈希

### 五、排序
- [[排序算法]] — 插入、希尔、冒泡、快排、选择、堆排、归并、基数

## 参考资料
""",
    "docs": {
        "线性表.md": """---
id: ds-list
type: concept
status: active
course: DS
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 线性表

## 一、顺序表

用数组实现，逻辑相邻=物理相邻。

**优点**：随机访问 $O(1)$，存储密度高。**缺点**：插入/删除需移动元素 $O(n)$。

## 二、单链表

```cpp
struct Node { int data; Node* next; };
```

| 操作 | 复杂度 |
|------|--------|
| 按位查找 | $O(n)$ |
| 头插/头删 | $O(1)$ |
| 尾插(无尾指针) | $O(n)$ |

## 三、循环链表

尾结点的 next 指向头结点。可从任意结点出发遍历所有结点。

## 四、双向链表

```cpp
struct DNode { int data; DNode *prior, *next; };
```

插入/删除需修改两个指针的 prior 和 next。时间复杂度仍为 $O(1)$（已知位置）。

## 五、顺序表 vs 链表

| 操作 | 顺序表 | 链表 |
|------|--------|------|
| 随机访问 | $O(1)$ | $O(n)$ |
| 插入/删除 | $O(n)$ | $O(1)$(已知位置) |
| 存储密度 | 高 | 低(有指针开销) |
| 动态扩容 | 需整体搬迁 | 可灵活增长 |
""",

        "栈与队列.md": """---
id: ds-stack-queue
type: concept
status: active
course: DS
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 栈与队列

## 一、栈(Stack)

**LIFO(后进先出)**。操作：push/pop/top。Top 指向栈顶。

**应用**：括号匹配、表达式求值、递归、DFS、进制转换。

## 二、队列(Queue)

**FIFO(先进先出)**。操作：enqueue/dequeue。Front 指向队头，Rear 指向队尾。

**循环队列**：入队 `rear=(rear+1)%MAXSIZE`，出队 `front=(front+1)%MAXSIZE`。队空 front==rear；队满 (rear+1)%MAXSIZE==front（牺牲一个单元）。

## 三、双端队列

两端都可入队出队。输出受限/输入受限两种。

## 四、栈的应用

**中缀→后缀(逆波兰)**：

遍历中缀表达式：
- 操作数：直接输出
- 左括号 `(`：入栈
- 右括号 `)`：弹出到左括号
- 运算符：弹出优先级≥当前的所有运算符，然后当前入栈

**后缀求值**：遇到操作数入栈；遇到运算符弹出两个操作数运算后入栈。
""",

        "二叉树.md": """---
id: ds-btree
type: concept
status: active
course: DS
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 二叉树

## 一、基本性质

- 第 i 层至多 $2^{i-1}$ 个结点
- 深度为 k 的二叉树至多 $2^k-1$ 个结点
- 叶子数 $n_0$ = 度为2的结点数 $n_2$ + 1
- n 个结点的完全二叉树深度 $\\lfloor\\log_2 n\\rfloor + 1$

## 二、遍历

| 遍历 | 顺序 | 用途 |
|------|------|------|
| **先序** | 根→左→右 | 复制树、前缀表达式 |
| **中序** | 左→根→右 | 排序输出(BST)、中缀表达式 |
| **后序** | 左→右→根 | 释放结点、后缀表达式 |
| **层次** | 逐层 | BFS |

**递归模板**(中序)：
```
inorder(root):
    if root == NULL: return
    inorder(root.left)
    visit(root)
    inorder(root.right)
```

## 三、完全二叉树

可用数组存储。结点 i 的左子=2i，右子=2i+1，父=⌊i/2⌋。

## 四、线索二叉树

利用空指针域指向遍历的前驱/后继。ltag=0→左子，=1→前驱。

## 五、哈夫曼树(WPL最小)

每次取权值最小的两个结点建树。应用：哈夫曼编码(最优前缀码)。
""",

        "查找算法.md": """---
id: ds-search
type: concept
status: active
course: DS
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 查找算法

## 一、顺序查找

$O(n)$。适用：无序或有序的线性表。

**平均查找长度 ASL** = $\\frac{n+1}{2}$

## 二、二分查找

**仅适用有序顺序表**。$O(\\log n)$。

```cpp
int low=0, high=n-1;
while(low <= high){
    int mid = (low+high)/2;
    if(A[mid]==x) return mid;
    else if(A[mid]<x) low = mid+1;
    else high = mid-1;
}
return -1;
```

## 三、二叉排序树(BST)

左子树 < 根 < 右子树。查找/插入 $O(\\log n)$~$O(n)$。

## 四、平衡二叉树(AVL)

**平衡因子** = 左高-右高 ≤ 1。

4种失衡调整：LL(右旋)、RR(左旋)、LR(左旋左子+右旋根)、RL(右旋右子+左旋根)。

## 五、B 树与 B+ 树

**B 树**：多路平衡查找树。所有结点可存数据。

**B+ 树**：数据只存在叶子结点，叶子间用链表连接。数据库索引首选。

## 六、哈希表

**哈希函数**：除留余数法(除数取素数)。

**冲突解决**：
- 拉链法：每个桶存链表
- 开放定址法：$H_i = (H(key)+d_i) \\bmod m$
""",

        "排序算法.md": """---
id: ds-sort
type: concept
status: active
course: DS
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 排序算法

## 一、排序算法总览

| 算法 | 最好 | 平均 | 最坏 | 空间 | 稳定 |
|------|------|------|------|------|------|
| 直接插入 | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✓ |
| 希尔排序 | — | $O(n^{1.3})$ | — | $O(1)$ | ✗ |
| 冒泡 | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✓ |
| 快速排序 | $O(n\\log n)$ | $O(n\\log n)$ | $O(n^2)$ | $O(\\log n)$ | ✗ |
| 简单选择 | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✗ |
| 堆排序 | $O(n\\log n)$ | $O(n\\log n)$ | $O(n\\log n)$ | $O(1)$ | ✗ |
| 归并排序 | $O(n\\log n)$ | $O(n\\log n)$ | $O(n\\log n)$ | $O(n)$ | ✓ |
| 基数排序 | $O(d(n+r))$ | $O(d(n+r))$ | $O(d(n+r))$ | $O(r)$ | ✓ |

## 二、快速排序

```cpp
int partition(int A[], int l, int r){
    int pivot = A[l], i = l, j = r;
    while(i < j){
        while(i<j && A[j]>=pivot) j--;
        while(i<j && A[i]<=pivot) i++;
        if(i<j) swap(A[i], A[j]);
    }
    swap(A[l], A[i]); return i;
}
```

**最坏 $O(n^2)$**：已排序数组+选首元素。优化：三数取中、随机选 pivot。

## 三、堆排序

建堆 $O(n)$，每次调整 $O(\\log n)$。总 $O(n\\log n)$。

## 四、归并排序

稳定，$O(n\\log n)$。需要 $O(n)$ 辅助空间。适合外排序。
"""
    }
}

# ============================================================
# PROB_概率论, LINALG_线性代数, PHYSICS_大学物理
# ============================================================
COURSES["PROB_概率论"] = {
    "code": "PROB",
    "moc": """---
course: PROB
type: moc
status: active
created: 2026-07-18
---

# 概率论与数理统计 — MOC

## 知识结构
- [[概率论基础]] — 古典概型、条件概率、全概率与贝叶斯
- [[随机变量与分布]] — 离散/连续、分布函数、常见分布、数字特征
- [[多维随机变量]] — 联合分布、边际分布、协方差与相关系数
- [[大数定律与中心极限定理]] — 车比雪夫、伯努利、辛钦、棣莫弗-拉普拉斯
- [[数理统计基础]] — 参数估计(矩估计/极大似然)、假设检验
""",
    "docs": {
        "概率论基础.md": """---
id: prob-basics
type: concept
status: active
course: PROB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 概率论基础

## 一、事件与概率

**样本空间 $\\Omega$**：所有可能结果的集合。

**事件的概率**：$P(A) = \\frac{|A|}{|\\Omega|}$（古典概型）。

**条件概率**：$P(A|B) = \\frac{P(AB)}{P(B)}$

## 二、全概率公式与贝叶斯公式

**全概率**：$P(A) = \\sum_{i=1}^n P(A|B_i)P(B_i)$（$B_i$ 构成完备事件组）

**贝叶斯**：$P(B_i|A) = \\frac{P(A|B_i)P(B_i)}{\\sum_j P(A|B_j)P(B_j)}$

## 三、独立性

$A,B$ 独立 $\\Leftrightarrow P(AB) = P(A)P(B)$

**独立与互斥的区别**：独立→有交集的概率等于乘积；互斥→无交集。
""",

        "随机变量与分布.md": """---
id: prob-dist
type: concept
status: active
course: PROB
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 随机变量与分布

## 一、离散型随机变量

| 分布 | 分布律 | 期望 | 方差 |
|------|--------|------|------|
| 0-1分布 | $P(X=1)=p$ | $p$ | $p(1-p)$ |
| 二项分布 $B(n,p)$ | $C_n^k p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| 泊松分布 $P(\\lambda)$ | $\\frac{\\lambda^k}{k!}e^{-\\lambda}$ | $\\lambda$ | $\\lambda$ |
| 几何分布 | $p(1-p)^{k-1}$ | $\\frac{1}{p}$ | $\\frac{1-p}{p^2}$ |

## 二、连续型随机变量

**概率密度函数** $f(x)$：$P(a<X<b) = \\int_a^b f(x)dx$

| 分布 | 密度 | 期望 | 方差 |
|------|------|------|------|
| 均匀分布 $U(a,b)$ | $\\frac{1}{b-a}$ | $\\frac{a+b}{2}$ | $\\frac{(b-a)^2}{12}$ |
| 指数分布 $E(\\lambda)$ | $\\lambda e^{-\\lambda x}$ | $\\frac{1}{\\lambda}$ | $\\frac{1}{\\lambda^2}$ |
| **正态分布** $N(\\mu,\\sigma^2)$ | $\\frac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$ | $\\mu$ | $\\sigma^2$ |

## 三、标准正态分布 $N(0,1)$

$X\\sim N(\\mu,\\sigma^2) \\Rightarrow \\frac{X-\\mu}{\\sigma}\\sim N(0,1)$

## 四、数字特征

- **期望** $E(X)$：加权平均，线性的($E(aX+bY)=aE(X)+bE(Y)$)
- **方差** $D(X)=E(X^2)-E(X)^2$
- **协方差** Cov(X,Y)=E(XY)-E(X)E(Y)
- **相关系数** $\\rho_{XY}=\\frac{Cov(X,Y)}{\\sqrt{D(X)D(Y)}}$
""",
    }
}

# ============================================================
# LINALG_线性代数
# ============================================================
COURSES["LINALG_线性代数"] = {
    "code": "LINALG",
    "moc": """---
course: LINALG
type: moc
status: active
created: 2026-07-18
---

# 线性代数 — MOC

## 知识结构
- [[行列式]] — 计算、性质、克拉默法则
- [[矩阵]] — 运算、逆矩阵、初等变换、秩
- [[向量组与线性方程组]] — 线性相关/无关、基础解系、解的结构
- [[特征值与特征向量]] — 相似对角化、正交对角化
- [[二次型]] — 标准型、正定性
""",
    "docs": {
        "矩阵.md": """---
id: linalg-matrix
type: concept
status: active
course: LINALG
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 矩阵

## 一、基本运算

| 运算 | 条件 | 性质 |
|------|------|------|
| 加法 | 同型 | 交换律/结合律 |
| 数乘 | 无 | $k(A+B)=kA+kB$ |
| 乘法 | 左列=右行 | **不满足交换律** $AB\\neq BA$ |

**转置**：$(AB)^T = B^T A^T$

## 二、逆矩阵

$A^{-1}A = AA^{-1} = I$。**$A$ 可逆 $\\Leftrightarrow |A|\\neq 0$**。

$(AB)^{-1} = B^{-1}A^{-1}$

## 三、初等变换与秩

**三种初等变换**：换行/换列、倍乘、倍加。

**秩**：矩阵中最高阶非零子式的阶数。

**秩的性质**：$R(A^TA)=R(A)$，$R(AB)\\le\\min(R(A),R(B))$

## 四、线性方程组

**齐次 $Ax=0$**：有非零解 $\\Leftrightarrow R(A)<n$（列数）

**非齐次 $Ax=b$**：有解 $\\Leftrightarrow R(A)=R(A,b)$

解的个数：$R(A)=R(A,b)=n$→唯一解；$<n$→无穷多解(基础解系含 $n-R(A)$ 个向量)
""",

        "特征值与特征向量.md": """---
id: linalg-eigen
type: concept
status: active
course: LINALG
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 特征值与特征向量

## 一、定义

$Ax = \\lambda x$（$x \\neq 0$），$\\lambda$ 为特征值，$x$ 为特征向量。

**求法**：特征方程 $|\\lambda I - A| = 0$

## 二、性质

- $\\sum\\lambda_i = \\text{tr}(A)$（迹）
- $\\prod\\lambda_i = |A|$（行列式）
- 不同特征值对应的特征向量**线性无关**
- 实对称矩阵的特征值全是实数，且可正交对角化

## 三、相似对角化

**$A$ 可对角化 $\\Leftrightarrow$ $A$ 有 $n$ 个线性无关的特征向量**。

**充分条件**：$A$ 有 $n$ 个互不相同的特征值。

构造：$P^{-1}AP = \\Lambda$，$P$ 的列为特征向量，$\\Lambda$ 对角线上为特征值。

## 四、正交对角化(实对称矩阵)

**任何实对称矩阵都可正交对角化**。求法：
1. 求特征值和特征向量
2. 用施密特正交化处理重根的特征向量
3. 单位化

得 $Q^TAQ = \\Lambda$，$Q$ 为正交矩阵($Q^T=Q^{-1}$)。
""",
    }
}

# ============================================================
# CPP_JAVA_PY_SE — Programming courses (brief but solid)
# ============================================================
for cname, code in [("CPP_C++", "CPP"), ("JAVA_java", "JAVA"), ("PY_python", "PY")]:
    COURSES[cname] = {
        "code": code,
        "moc": f"""---
course: {code}
type: moc
status: active
created: 2026-07-18
---

# {cname.split('_')[1] if '_' in cname else code} 编程 — MOC

- [[语言基础]] — 数据类型、控制流、函数
- [[面向对象]] — 类与对象、继承、多态
- [[标准库与常用API]] — 集合框架、IO、异常处理

## 参考资料
""",
        "docs": {
            "语言基础.md": f"""---
id: {code.lower()}-basics
type: concept
status: active
course: {code}
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 语言基础

## 一、数据类型与变量

基本类型、类型转换(隐式/强制)、常量定义。

## 二、控制流

条件：if-else、switch-case。循环：for、while、do-while。

## 三、函数

定义、参数传递(值传递/引用传递)、返回值、函数重载。

## 四、数组与字符串

一维/多维数组声明与遍历。字符串基本操作。

---
""",
            "面向对象.md": f"""---
id: {code.lower()}-oop
type: concept
status: active
course: {code}
created: 2026-07-18
mastery: reviewing
importance: critical
---

# 面向对象

## 一、三大特性

| 特性 | 说明 |
|------|------|
| **封装** | 隐藏内部实现(private/protected/public) |
| **继承** | 子类复用父类代码，扩展功能 |
| **多态** | 同一接口不同实现(虚函数/覆写) |

## 二、类与对象

类=模板，对象=实例。构造/析构函数。

## 三、抽象类与接口

纯虚函数(C++：`virtual void f()=0`)。定义契约。

## 四、设计原则(SOLID)

单一职责、开闭原则、里氏替换、接口隔离、依赖反转。

---
""",
        }
    }

# SE
COURSES["SE_软件工程"] = {
    "code": "SE",
    "moc": """---
course: SE
type: moc
status: active
created: 2026-07-18
---

# 软件工程 — MOC

- [[软件过程模型]] — 瀑布、敏捷、Scrum
- [[需求分析]] — 用例图、功能需求/非功能需求
- [[软件设计]] — 架构设计、设计模式、UML
- [[软件测试]] — 单元测试、集成测试、白盒/黑盒
- [[项目管理]] — 甘特图、风险管理
""",
    "docs": {
        "软件过程模型.md": """---
id: se-process
type: concept
status: active
course: SE
created: 2026-07-18
mastery: reviewing
importance: high
---

# 软件过程模型

## 一、瀑布模型

需求→设计→编码→测试→维护。顺序执行，不可回溯。适合需求明确的传统项目。

## 二、敏捷开发

**宣言**：个体与交互 > 过程与工具，可工作软件 > 详尽文档，客户合作 > 合同谈判，响应变化 > 遵循计划。

## 三、Scrum

角色：Product Owner、Scrum Master、开发团队。

事件：Sprint(2-4周)、每日站会、Sprint评审、Sprint回顾。

## 四、DevOps

开发+运维一体化。CI/CD持续集成持续交付。自动化测试+自动化部署。
""",

        "软件测试.md": """---
id: se-testing
type: concept
status: active
course: SE
created: 2026-07-18
mastery: reviewing
importance: high
---

# 软件测试

## 一、测试层次

| 层次 | 说明 |
|------|------|
| 单元测试 | 测试单个函数/类 |
| 集成测试 | 测试模块间接口 |
| 系统测试 | 测试完整系统 |
| 验收测试 | 用户验收 |

## 二、白盒测试 vs 黑盒测试

**白盒**：知道内部逻辑。语句覆盖、分支覆盖、路径覆盖。

**黑盒**：只看输入输出。等价类划分、边界值分析、决策表。

## 三、V 模型

需求↔验收测试、概要设计↔系统测试、详细设计↔集成测试、编码↔单元测试。
""",
    }
}

# ============================================================
# Liberal Arts courses — structured notes
# ============================================================
arts = {
    "ENGLISH_学术英语": ("ENGLISH", "学术英语", [
        ("学术写作.md", """---
id: eng-writing
type: concept
status: active
course: ENGLISH
created: 2026-07-18
mastery: reviewing
importance: high
---

# 学术英语写作

## 一、学术论文结构

Title → Abstract → Introduction → Methodology → Results → Discussion → Conclusion → References

## 二、摘要写作

目的、方法、结果、结论四要素。150-300词。

## 三、常见句式模板

**引言**：This paper investigates/examines/explores...
**方法**：The experiment was conducted using...
**结果**：The results indicate that... / It was found that...
**结论**：In conclusion, the findings suggest that...

## 四、常见词汇替换

| 普通表达 | 学术表达 |
|---------|---------|
| find out | determine, ascertain |
| look at | examine, investigate |
| because of | due to, owing to |
| about | approximately, regarding |
"""),
        ("学术阅读与翻译.md", """---
id: eng-reading
type: concept
status: active
course: ENGLISH
created: 2026-07-18
mastery: reviewing
importance: high
---

# 学术英语阅读与翻译

## 一、阅读策略

- Skimming(略读)：快速获取大意
- Scanning(扫读)：定位特定信息
- Intensive Reading(精读)：深入理解细节

## 二、长难句分析

**步骤**：找主谓宾→分从句→理修饰关系。

## 三、科技英语翻译技巧

| 技巧 | 示例 |
|------|------|
| 增词法 | implement→贯彻执行 |
| 减词法 | it is obvious that→显然 |
| 词性转换 | the operation of→操作 |
| 被动转主动 | It is believed that...→人们认为... |
"""),
    ]),
    "HISTORY_近代史": ("HISTORY", "近代史", [
        ("近代史纲要.md", """---
id: history-outline
type: concept
status: active
course: HISTORY
created: 2026-07-18
mastery: reviewing
importance: high
---

# 中国近代史纲要

## 一、鸦片战争(1840)到五四运动(1919)

**旧民主主义革命时期**。关键事件：鸦片战争(1840)→太平天国→洋务运动→甲午战争→戊戌变法→辛亥革命(1911)→新文化运动。

## 二、五四运动(1919)到新中国成立(1949)

**新民主主义革命时期**。五四→中共成立(1921)→国民革命→土地革命→抗日战争→解放战争→建国。

## 三、为什么选择社会主义道路

1. 洋务运动(技术层面)失败→只学技术不够
2. 戊戌变法(制度改良)失败→清廷不愿改革
3. 辛亥革命不彻底→未改变半殖民地半封建性质
4. 只有中国共产党领导的社会主义革命成功了

## 四、核心结论

**没有共产党就没有新中国**。历史选择了马克思主义、选择了中国共产党、选择了社会主义道路。
"""),
    ]),
    "JUNLI_军理": ("JUNLI", "军理", [
        ("军事理论.md", """---
id: junli-theory
type: concept
status: active
course: JUNLI
created: 2026-07-18
mastery: reviewing
importance: high
---

# 军事理论核心知识

## 一、毛泽东军事思想

**核心**：人民战争思想。兵民是胜利之本。战略上藐视敌人，战术上重视敌人。

## 二、国防体制

中央军委→四总部(或相关机构)。党指挥枪的根本原则。

## 三、现代战争特点

信息化战争、非对称战争、精确打击、网络战/电子战。

## 四、中国周边安全

海洋权益(南海/东海)、台湾问题(一国两制)、边界问题(中印)。
"""),
    ]),
    "MAOGAI_毛概自用资料": ("MAOGAI", "毛概", [
        ("毛泽东思想概论.md", """---
id: maogai-outline
type: concept
status: active
course: MAOGAI
created: 2026-07-18
mastery: reviewing
importance: high
---

# 毛泽东思想概论

## 一、毛泽东思想的形成与发展

萌芽(大革命时期)→形成(土地革命)→成熟(抗日战争)→发展(解放战争/建国后)

## 二、核心内容

| 方面 | 内容 |
|------|------|
| 新民主主义革命理论 | 总路线、基本纲领、三大法宝 |
| 社会主义改造理论 | "一化三改"，和平赎买 |
| 社会主义建设 | 《论十大关系》、正确处理人民内部矛盾 |

## 三、活的灵魂

实事求是(精髓)、群众路线(生命线)、独立自主(基本立足点)。

## 四、历史地位

马克思主义中国化的**第一次历史性飞跃**。七大(1945)确立为指导思想。
"""),
    ]),
    "MAYUAN_马原复习": ("MAYUAN", "马原", [
        ("马克思主义基本原理.md", """---
id: mayuan-principles
type: concept
status: active
course: MAYUAN
created: 2026-07-18
mastery: reviewing
importance: high
---

# 马克思主义基本原理

## 一、哲学

**唯物辩证法三大规律**：对立统一(核心)、量变质变、否定之否定。

**物质决定意识**，意识对物质有反作用。

## 二、政治经济学

**剩余价值理论**：资本家剥削工人的秘密。劳动力创造的价值 > 工资。

**资本主义基本矛盾**：生产社会化 vs 生产资料私有制 → 周期性经济危机。

## 三、科学社会主义

**两个必然**：资本主义必然灭亡、社会主义必然胜利。

共产主义：物质极大丰富、按需分配、人的全面发展。
"""),
    ]),
    "SIXIANG_思想与政治": ("SIXIANG", "思政", [
        ("思想道德修养.md", """---
id: sixiang-morality
type: concept
status: active
course: SIXIANG
created: 2026-07-18
mastery: reviewing
importance: high
---

# 思想道德修养

## 一、理想信念

个人理想与社会理想的统一。中国梦：国家富强、民族振兴、人民幸福。

## 二、中国精神

以爱国主义为核心的**民族精神** + 以改革创新为核心的**时代精神**。

## 三、社会主义核心价值观

| 层面 | 内容 |
|------|------|
| 国家 | 富强 民主 文明 和谐 |
| 社会 | 自由 平等 公正 法治 |
| 个人 | 爱国 敬业 诚信 友善 |

## 四、道德修养

社会公德、职业道德、家庭美德、个人品德。
"""),
    ]),
    "XIGAI_习概复习": ("XIGAI", "习概", [
        ("习近平新时代中国特色社会主义思想.md", """---
id: xigai-thought
type: concept
status: active
course: XIGAI
created: 2026-07-18
mastery: reviewing
importance: high
---

# 习近平新时代中国特色社会主义思想

## 一、核心要义

坚持和发展中国特色社会主义。

## 二、"十个明确"（核心）

1. 党的领导是最本质特征
2. 总任务：实现中华民族伟大复兴
3. 社会主要矛盾变化
4. 总体布局(五位一体)+战略布局(四个全面)
5. 全面深化改革总目标
6. 全面依法治国总目标
7. 强军目标
8. 大国外交→人类命运共同体
9. 全面从严治党
10. 高质量发展

## 三、"十四个坚持"（基本方略）

涵盖经济、政治、法治、科技、文化、民生、生态、安全、国防、外交、党建等各领域。

## 四、历史地位

马克思主义中国化的**第三次历史性飞跃**。十九大(2017)确立，二十大(2022)深化。
"""),
    ]),
    "ZHENGCE_政策与形势": ("ZHENGCE", "政策", [
        ("形势与政策.md", """---
id: zhengce-current
type: concept
status: active
course: ZHENGCE
created: 2026-07-18
mastery: reviewing
importance: high
---

# 形势与政策

## 一、当前国际形势

百年未有之大变局。多极化、全球化遭遇逆流。

## 二、中国外交政策

独立自主和平外交。构建人类命运共同体。一带一路倡议。

## 三、当前国内重点

共同富裕、乡村振兴、碳达峰碳中和、科技自立自强。

## 四、学生应关注

国内外重大时事。二十大精神。十四五规划。
"""),
    ]),
}

for cname, (code, _, docs_list) in arts.items():
    COURSES[cname] = {
        "code": code,
        "moc": f"""---
course: {code}
type: moc
status: active
created: 2026-07-18
---

# {cname.split('_')[1] if '_' in cname else code} — MOC

""",
        "docs": {fn: content for fn, content in docs_list}
    }

# ============================================================
# SIMPLE courses (PHYSICS, EDA, INFO)
# ============================================================
simple = {
    "PHYSICS_大学物理": ("PHYSICS", "大物", [
        ("大学物理总览.md", """---
id: physics-overview
type: concept
status: active
course: PHYSICS
created: 2026-07-18
mastery: reviewing
importance: high
---

# 大学物理

## 一、力学

牛顿三大定律、动量守恒、角动量守恒、机械能守恒。刚体定轴转动。

## 二、电磁学

库仑定律、高斯定理、毕奥-萨伐尔定律、法拉第电磁感应、麦克斯韦方程组。

**麦克斯韦方程组**：$\\oint_S D\\cdot dS = q$(高斯)、$\\oint_S B\\cdot dS = 0$(磁单极子不存在)、$\\oint_L E\\cdot dl = -\\frac{d\\Phi_B}{dt}$(法拉第)、$\\oint_L H\\cdot dl = I + \\frac{d\\Phi_D}{dt}$(安培-麦克斯韦)。

## 三、热学

热力学第一定律($Q=\\Delta U+W$)、第二定律(熵增原理)、卡诺循环。

## 四、光学

干涉(杨氏双缝)、衍射(单缝/光栅)、偏振(马吕斯定律)。

## 五、近代物理

光电效应($E=h\\nu-W$)、康普顿效应、波粒二象性、不确定关系。
"""),
    ]),
    "EDA_EDA": ("EDA", "EDA", [
        ("EDA概述.md", """---
id: eda-overview
type: concept
status: active
course: EDA
created: 2026-07-18
mastery: reviewing
importance: high
---

# EDA 技术概述

## 一、EDA 概念

电子设计自动化。用计算机辅助完成电路设计→仿真→综合→布局布线。

## 二、HDL 语言

VHDL/Verilog 用于描述数字电路。模块化设计，自顶向下。

## 三、FPGA

现场可编程门阵列。查找表(LUT)+触发器+互连。与 ASIC 对比：灵活但性能/功耗较差。

## 四、设计流程

RTL设计→功能仿真→逻辑综合→时序仿真→布局布线→下载到FPGA。
"""),
    ]),
    "INFO_信息导论": ("INFO", "信息导论", [
        ("信息科学导论.md", """---
id: info-intro
type: concept
status: active
course: INFO
created: 2026-07-18
mastery: reviewing
importance: medium
---

# 信息科学导论

## 一、什么是信息

信息是消除不确定性的东西(香农定义)。信息=数据+意义。

## 二、信息论基础

**信息熵**：$H = -\\sum p_i\\log_2 p_i$（信息的度量）

**信道容量**：$C = B\\log_2(1+S/N)$

## 三、计算机科学概览

硬件→操作系统→应用软件。冯·诺依曼结构。二进制→数字世界。

## 四、人工智能简述

机器学习、深度学习、大语言模型(如GPT)。数据→训练→模型→推理。
"""),
    ]),
}

for cname, (code, _, docs_list) in simple.items():
    COURSES[cname] = {
        "code": code,
        "moc": f"""---
course: {code}
type: moc
status: active
created: 2026-07-18
---

# {cname.split('_')[1] if '_' in cname else code} — MOC

""",
        "docs": {fn: content for fn, content in docs_list}
    }

# ============================================================
# Write ALL files
# ============================================================
total_chars = 0
for cname, cdata in COURSES.items():
    base = os.path.join(VAULT, cname)

    # MOC
    moc_path = os.path.join(base, f"00_{cname.split('_')[1] if '_' in cname else cname}_课程MOC.md")
    existing_mocs = [f for f in os.listdir(base) if f.startswith("00_")] if os.path.exists(base) else []
    if existing_mocs:
        moc_path = os.path.join(base, existing_mocs[0])
    with open(moc_path, "w", encoding="utf-8") as f:
        f.write(cdata["moc"])
    total_chars += len(cdata["moc"])

    # Docs
    for fname, content in cdata["docs"].items():
        kp = os.path.join(base, "02_知识点")
        os.makedirs(kp, exist_ok=True)
        with open(os.path.join(kp, fname), "w", encoding="utf-8") as f:
            f.write(content)
        total_chars += len(content)

    print(f"  {cname}: {len(cdata['docs'])} docs")

print(f"\\nTotal chars generated: {total_chars} ({total_chars//1000}K)")
