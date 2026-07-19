---
id: extract-java-92e3845f
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_第九题.md_笔记_未知日期_92e3845f.md]]"
source_pages: all
source_hash: "92e3845f345b18352f3d55de88d2b3c01c92de94261287fe45e4c1b90f4c05fe"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 第九题.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 第九题

因为该自定义异常SelfException类继承自Exception，是检查型异常，方法called()在声明的时候抛出了SelfException，这就要求主函数必须对该异常进行处理，否则编译不会通过

```java
public static void main(String args[]) throws SelfException {
    called();
}

public static void main(String args[]){
    try(SelfException e){
        called();
    }catch{
        e.printStackTrace();
        System.out.println("捕获到了异常"+ e.getMessage());
    }
}
```



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
