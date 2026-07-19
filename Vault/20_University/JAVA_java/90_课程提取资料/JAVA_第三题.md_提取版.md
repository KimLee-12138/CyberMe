---
id: extract-java-6d05529d
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第三题.md_笔记_未知日期_6d05529d.md]]"
source_pages: all
source_hash: "6d05529dda27951a7e36ee4d52190a5246dcd16c5a35250d870358d50c012749"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第三题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 第三题

我会选择LinkedList类来存储这些订单，因为ArrayList内部的实现是依靠动态数组来实现的，数据之间的地址都是连续的，当做出插入或者删除这种需要断开连续地址的操作时，为了保持连续性，需要去改变数组中的其他数据的地址，使其统一向前或者向后移动地址，这就需要大量的内存复制操作，时间复杂度为O(n)，效率低

但是LinkedList的内部是通过双向链表来实现的，每一个节点都包含指向前一个和后一个地址的引用（指针），在进行添加和删除操作的时候只需要修改对应节点的引用指向，不需要大量的内存复制操作，时间复杂度为O(1)，效率大大降低



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
