---
id: extract-cpp-0a84226d
type: extract
status: extracted
course: CPP
source:
  - "[[91_Raw-Archive/DOC/CPP_4.指针常量.md_笔记_未知日期_0a84226d.md]]"
source_pages: all
source_hash: "0a84226d59a09d848f46c6eb70ae1aa10e915dbf1eb5a03ac7f16df37558e697"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 4.指针常量.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 指针与常量

**1.指针常量**

- 即指针的值是一个常量

  int * const p = &a；

**2.常量指针**

- 即指向常量的指针

  const int * p = &a ;

**3.常量指针常量**

- 即两边不能改变

  const int * const  p = &a;

| **指针常量**     | type* const            | 指针值是一个常量                 | 指针无法被赋值               |
| ---------------- | ---------------------- | -------------------------------- | ---------------------------- |
| **常量指针**     | **const type***        | **指向常量的指针**               | **指针解引用后无法被赋值**   |
| **常量指针常量** | **const type\* const** | **指针值和指针指向的值都是常量** | **指针和解引用都无法被赋值** |



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_C++_课程MOC|C++ MOC]]
