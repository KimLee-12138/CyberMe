---
id: py-basics | type: concept | status: cleaned | course: PY
source: ["[[91_Raw-Archive/Registry/全量归档记录.json]]"] | source_pages: ["待核对"]
created: 2026-07-17 | updated: 2026-07-17 | verified_by: ""
mastery: unknown | importance: high | confidence: medium
verification: inferred | needs_review: true
review_reason: "AI深度蒸馏，需人工核对"
tags: [python]
---

# Python基础语法

## 一句话解释
Python是动态类型解释型语言，缩进定义代码块。六大核心数据结构：list(有序可变[])、tuple(有序不可变())、dict(键值对{}哈希表)、set(无序不重复{})、str(不可变字符序列)、bytes(二进制)。列表推导式`[x*2 for x in range(10) if x%2==0]`是Python的标志性语法。

## 核心原理
**动态类型**：变量无类型声明，类型在运行时确定。鸭子类型(Duck Typing)："如果它走路像鸭子、叫声像鸭子，那它就是鸭子"——不检查类型，只检查是否有需要的属性/方法。

**可变vs不可变**：list/dict/set可变(修改后id不变)；int/float/str/tuple不可变(每次"修改"实际创建新对象)。不可变对象可作dict的key(因为hash不变)。

**切片**：`s[start:stop:step]`。`s[::-1]`反转；`s[::2]`隔一个取一个。切片返回新对象(浅拷贝)。

**函数**：`def f(a, b=0, *args, **kwargs):`。默认参数在定义时求值(只求一次！坑：`def f(lst=[])`会记住上次的修改)。`*args`收集多余位置参数为tuple；`**kwargs`收集多余关键字参数为dict。

**装饰器**：本质是接受函数返回函数的函数。`@decorator`等价于`f=decorator(f)`。用于日志、计时、权限检查、缓存(如@lru_cache)。

**生成器**：用yield而非return。惰性求值→节省内存。`(x*2 for x in range(10))`生成器表达式。

**常用内置函数**：map/filter/zip/enumerate/sorted(有key参数)/lambda。

## 容易出错的地方
- 可变默认参数陷阱：`def f(lst=[])`每次调用共享同一个list
- is比较身份(地址)==比较值。小整数(-5~256)有缓存，is可能意外为True
- 浅拷贝(list.copy()/[:])vs深拷贝(copy.deepcopy)
- 课程导航：[[../00_python_课程MOC|python MOC]]


- 全局变量在函数内赋值需global声明(只读不需要)

## 与其他知识点的关系
- 相关：[[数据分析基础]]

- 列表推导→函数式编程(map/filter)
- 生成器→迭代器模式→内存优化


## 来源与依据
- [[91_Raw-Archive/Registry/全量归档记录.json]] | `needs_review: true`
