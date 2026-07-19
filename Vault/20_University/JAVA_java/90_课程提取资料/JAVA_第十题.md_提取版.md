---
id: extract-java-7e44bb7a
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第十题.md_笔记_未知日期_7e44bb7a.md]]"
source_pages: all
source_hash: "7e44bb7a705d20e5d0aebb97d80fff99bd183c4ca69a2df3f0d0f1ec3ee14fc5"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第十题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第十题

在该题中this.i是表示该类中的自己的成员变量i

super.i表示Construct类的父类的Pare的i的那个成员变量



该方法有错误

因为在pare中添加了有参的构造函数，导致无参构造方法失效，并且没有再补写无参构造方法，当子类Construct在调用自己的构造函数时，因为没有显式的调用父类的构造函数，所以默认要调用父类的无参构造函数，但是因为父类无参构造函数已经失效，所以会导致编译失败

可以在Construct(int num)第一行添加代码

super(num);

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
