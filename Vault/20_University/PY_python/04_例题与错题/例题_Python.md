---
id: py-probs
type: problem-set | status: cleaned | course: PY
created: 2026-07-17 | updated: 2026-07-17
needs_review: true | problem_origin: ai-generated
tags: [PY, 练习]
---

# 例题_Python

## 例题1

**题目**：用列表推导式生成 [1,4,9,16,25,36,49,64,81,100]。

**答案**：[x**2 for x in range(1, 11)]。

## 例题2

**题目**：统计字符串 "hello world" 中每个字符的出现次数。

**答案**：from collections import Counter; Counter('hello world')。或手写: d={{}}; for c in s: d[c]=d.get(c,0)+1

## 例题3

**题目**：以下代码有什么问题？f=open("a.txt"); data=f.read(); f.close(); 若read()抛异常呢？

**答案**：若read()抛异常，f.close()不会执行→文件泄漏。应用 with open() 保证关闭。

---
> 课程导航：[[../00_python_课程MOC|python MOC]]
