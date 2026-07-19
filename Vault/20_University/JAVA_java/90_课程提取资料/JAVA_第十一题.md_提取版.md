---
id: extract-java-73371b6d
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第十一题.md_笔记_未知日期_73371b6d.md]]"
source_pages: all
source_hash: "73371b6dbe998da13dc102c6040cae6fcc618e1b163bc098db2890b86217beb7"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第十一题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 第十一题

不能

因为现在的操作不是原子性的，会产生并发冲突

这行代码的执行分为三步……

修改方案：

添加synchronized关键字

```java
public synchronized void addChar(char c ){
    data[size++]=c;
}
```

这样当进程一进入该方法时会获取当前对象的锁，此时进程二想要进入该方法就会被挡在外面等待，直到进程一实现完毕释放掉这个锁，这样就保证读取、赋值、自增操作是按照顺序安全操作的，是原子性的



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
