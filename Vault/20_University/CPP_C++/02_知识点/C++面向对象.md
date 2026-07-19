---
id: cpp-oop | type: concept | status: cleaned | course: CPP
source: ["[[91_Raw-Archive/Registry/全量归档记录.json]]"] | source_pages: ["待核对"]
created: 2026-07-17 | updated: 2026-07-17 | verified_by: ""
mastery: unknown | importance: medium | confidence: medium
verification: inferred | needs_review: true
review_reason: "AI深度蒸馏，需人工核对"
tags: [C++]
---

# C++面向对象

## 一句话解释
C++ OOP比Java更灵活但更复杂：支持多继承、有析构函数、virtual显式声明多态。三大特性：封装(class+访问控制默认private)、继承(:public/protected/private)、多态(virtual+指针/引用→动态绑定)。**基类析构必须是virtual**，否则delete基类指针时派生类析构不被调用→资源泄漏。

## 核心原理
**类与对象**：构造器(可重载，初始化列表`:data(d){}`比在函数体内赋值更高效)、析构器(清理资源，基类必须virtual)、拷贝构造器(深拷贝vs浅拷贝)、赋值运算符(注意自赋值检查)。

**继承**：class D:public B(最常用)。C++支持多继承→菱形问题→虚继承(virtual public A)解决。派生类构造时先调基类构造。

**多态=虚函数(virtual)**：通过基类指针/引用调用虚函数→动态绑定到派生类实现。虚函数表(vtable)是底层实现机制——每个含虚函数的类有一个vtable，对象有一个vptr指向它。

**纯虚函数与抽象类**：`virtual void f()=0;`→抽象类，不能实例化。派生类必须实现所有纯虚函数才能实例化。C++没有interface关键字——用纯虚类模拟。

## 完整例子
```cpp
class Shape { public: virtual double area()const=0; virtual ~Shape(){} }; // 抽象+虚析构
class Circle:public Shape { double r; public: Circle(double r):r(r){} double area()const override{ return 3.14159*r*r; } };
Shape* s=new Circle(5.0); s->area(); // Circle::area()—多态
delete s; // ~Circle()→~Shape()—虚析构保证
```

## 容易出错的地方
- 基类析构不是virtual→delete基类指针时派生类析构不被调用→资源泄漏
- 对象切片：派生类对象赋值给基类对象→派生部分被切掉。用指针/引用避免
- 多继承的二义性→虚继承或明确指定
- 课程导航：[[../00_C++_课程MOC|C++ MOC]]


- 拷贝构造和赋值运算符的深拷贝——否则double free

## 与其他知识点的关系
- Java对比：Java单继承+多接口→[[面向对象编程]]
- 虚函数表→函数指针→[[指针]]


## 来源与依据
- [[91_Raw-Archive/Registry/全量归档记录.json]] | `needs_review: true`
