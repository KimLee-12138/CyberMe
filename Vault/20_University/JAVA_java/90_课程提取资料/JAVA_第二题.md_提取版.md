---
id: extract-java-8a0aa1b7
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第二题.md_笔记_未知日期_8a0aa1b7.md]]"
source_pages: all
source_hash: "8a0aa1b780d596b158759af0813ceedb91ab6b4992b3a4b8ee81ec8c3f0226ed"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第二题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 第二题

共同点：
都可以定义抽象方法，都不可以实例化，都可以有自己的声明，去引用子类或实现类对象

不同点：
属性：抽象类：可以有变量

​			接口：变量全部都为静态常量

成员方法：抽象类：可以有普通方法，也可以有抽象方法，并且普通方法可以调用自己的抽象方法

​					接口：内部所有的类全部都为抽象方法

实现策略：抽象类：必须有子类继承

​					接口：要有对应的实现类去实现

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
