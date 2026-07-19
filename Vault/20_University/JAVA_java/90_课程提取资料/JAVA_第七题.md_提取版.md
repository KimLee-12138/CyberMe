---
id: extract-java-cfe5400a
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第七题.md_笔记_未知日期_cfe5400a.md]]"
source_pages: all
source_hash: "cfe5400ac81cf6ae4e10b89451fe9cd54791c39dee312c390859631eb24f083f"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第七题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 第七题

键值对存储：Map接口用于存储键值对，有映射关系的数据

键唯一：Map中的键都是唯一的，不允许重复，每一个键最多映射到一个值

值可重复：Map中的值是可以重复的，不同的键可以指向相同的值

非Collection子接口：Map没有继承Collection接口，是一个独立的顶层接口

HashMap：

内部通过数组+链表实现，是无序的，其查找的时间复杂度为O(1)，支持一个NULL键和多个null值

TreeMap：

内部通过红黑树（一种自适应的平衡二叉树）来实现，是有序的，其查找的时间复杂度为O(logn)，不支持null键，但是允许null值





## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
