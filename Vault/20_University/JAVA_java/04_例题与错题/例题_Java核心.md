---
id: java-problems-例题_Java核心
type: problem-set
status: cleaned
course: JAVA
created: 2026-07-17
updated: 2026-07-17
needs_review: true
problem_origin: ai-generated
tags: [JAVA, 练习]
---

# 例题_Java核心

## 例题1：OOP应用

**题目**：设计一个简单的银行账户类，支持存款/取款/查询余额，取款时余额不足抛异常。

**答案**：Account类含balance字段(私有)+deposit/withdraw/getBalance方法。withdraw中检查balance<amount时throw new InsufficientFundsException()。

## 例题2：集合选择

**题目**：需要存储100万个不重复的URL并快速判断某个URL是否存在，选哪个集合？为什么？

**答案**：HashSet。O(1)的contains()判断。TreeSet是O(log n)，ArrayList的contains是O(n)。1M数据量差距巨大。

## 例题3：HashMap原理

**题目**：HashMap中两个key的hashCode相同但equals不同，会怎样？

**答案**：它们会放在同一个桶(bucket)中，以链表（或红黑树）形式存储。查找时先用hashCode定位桶，再用equals逐个比较找到正确的key。这就是哈希冲突的拉链法处理。

## 例题4：线程安全

**题目**：以下代码有什么问题？public void add(){ count++; } 两个线程同时调用1000次。

**答案**：count++不是原子操作（读-改-写三步）。可能导致最终count<2000。修复：方法加synchronized或使用AtomicInteger。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
