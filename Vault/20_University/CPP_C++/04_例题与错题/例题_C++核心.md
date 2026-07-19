---
id: cpp-problems-例题_C++核心
type: problem-set
status: cleaned
course: CPP
created: 2026-07-17
updated: 2026-07-17
needs_review: true
problem_origin: ai-generated
tags: [CPP, 练习]
---

# 例题_C++核心

## 例题1：指针运算

**题目**：int arr[]={10,20,30,40,50}; int* p=arr+2; 求*(p+1)和p[-1]的值。

**答案**：*(p+1)=arr[3]=40。p[-1]=arr[1]=20（等价于*(p-1)）。

## 例题2：常量指针辨析

**题目**：const int* p 和 int* const p 和 const int* const p 分别是什么意思？

**答案**：const int* p：指向常量的指针（不能通过p修改指向的值，但p可指向别处）。int* const p：常量指针（p不能指向别处，但可修改指向的值）。const int* const p：两者都不能改。

## 例题3：虚函数

**题目**：基类Base有virtual void f()，派生类Derived重写了f()。Base* b=new Derived(); b->f()调用哪个版本？如果Base的f()不是virtual呢？

**答案**：是virtual → 调用Derived::f()（动态绑定）。不是virtual → 调用Base::f()（静态绑定，编译时确定）。

## 例题4：智能指针

**题目**：shared_ptr和unique_ptr有什么区别？什么场景用哪个？

**答案**：unique_ptr独占所有权，不可拷贝(move)；shared_ptr共享所有权，引用计数。unique_ptr用于明确唯一所有权(如工厂函数返回值)；shared_ptr用于多个所有者(如多个容器共享一个对象)。

---
> 课程导航：[[../00_C++_课程MOC|C++ MOC]]
