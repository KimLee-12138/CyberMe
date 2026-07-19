---
id: extract-java-86f80899
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第八题.md_笔记_未知日期_86f80899.md]]"
source_pages: all
source_hash: "86f808997362401dce285e9f4e46f3be9b39b511f90ab6a77c431e4eadbd03b7"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第八题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第八题

String是不可变的，一旦被创建，内容就无法修改，每次拼接和删除都是产生新的对象，StringBuilder是可变的，在被创建以后内部在维护一个可变的字符数组，直接在堆内存上进行修改，可以直接在原对象上进行修改，String的性能较低，因为在每次拼接时都会产生新对象，产生大量垃圾内存，但是因为StringBuilder都是在原对象上进行操作，内存占用小

推荐应用场景：
String是字符串常量，在少量字符串拼接时使用

StringBuilder可以在频繁拼接或者修改字符串的情况下使用，一般要在单线程环境下使用



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
