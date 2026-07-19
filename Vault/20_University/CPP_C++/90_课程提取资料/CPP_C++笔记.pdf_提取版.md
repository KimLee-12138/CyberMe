---
id: extract-cpp-4a55d743
type: extract
status: extracted
course: CPP
source:
  - "[[91_Raw-Archive/PDF/CPP_C++笔记.pdf_课件_未知日期_4a55d743.pdf]]"
source_pages: all
source_hash: "4a55d7431131ed80962adde8182e0bf102b38dd3f56dd11fb383e3342f89418d"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# C++笔记.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

C++ 笔记  
静态数据成员：  
1. 概念：在  C++ 中，静态数据成员是类的一种特殊数据成员。它属于类本身，而不属于类的任何一
个具体对象。这意味着无论创建了多少个类的对象，静态数据成员在内存中只有一份副本。
2. 静态成员变量特性：
内存分配：静态数据成员在程序开始时就被分配内存，在程序结束时才释放内存，其生命周
期贯穿整个程序运行期间。
共享性：所有类的对象共享静态数据成员。
访问方式：可以通过类名直接访问静态数据成员，也可以通过类的对象来访问。
声明与初始化：类内声明，类外进行初始化
3. 静态成员函数特性：
所有对象共享同一份数据
静态成员函数只能访问静态成员变量
函数重载的依据：  
考虑因素：
1. 参数类型不同
2. 参数个数不同
3. 参数顺序不同
不考虑因素：
1. 返回值类型
友元函数：  
1. 特点和用途：
访问权限：友元函数能够访问类的私有成员和保护成员
不是成员函数：友元函数不是类的成员函数
灵活性：友元函数提供了一种灵活的方式来扩展类的功能。
2. 注意事项：
破坏封装性：由于友元函数可以访问类的私有和保护成员，过度使用友元函数可能会破坏类
的封装性。
单向访问：友元关系是单向的。
跨类访问：友元函数可以定义在不同的类中，也可以是全局函数。
3. 类型：
全局函数做友元
类做友元
成员函数做友元
不能被重载的运算符：  
1. 成员访问运算符（ . ）
2. 作用域解析运算符（ :: ）
3. 条件运算符（ ?: ）
4. sizeof 运算符

## 第2页

const 关键字：  
 可以修饰的：
1. 修饰变量
2. 修饰函数参数
3. 修饰函数返回值
4. 修饰成员函数
（不可以修饰类）
const 修饰成员函数：  
常函数：
成员函数后加 const 后我们称为这个函数为常函数
常函数内不可以修改成员属性
成员属性声明时加关键字 mutable 后，在常函数中依然可以修改
常对象：
声明对象前加 const 称该对象为常对象
常对象只能调用常函数
原因： this 指针的本质时指针常量  指针指向时不可以修改的，在成员函数后面加 const ，修饰的是 this 指
针，让指针指向的值也不可以修改
虚函数：  
1. 定义：虚函数是在基类中使用关键字  “virtual” 声明的成员函数。它的主要目的是实现多态性，允
许在派生类中重新定义（覆盖）该函数的行为，并且可以通过基类的指针或引用调用派生类中重新
定义的函数。
2. 纯虚函数和抽象类：
纯虚函数：是在基类中声明的虚函数，它在基类中没有定义具体的函数体，而是通过在函数
声明的结尾添加  “= 0” 来表示。包含纯虚函数的类称为抽象类。抽象类不能被实例化，它的主
要作用是为派生类提供一个统一的接口规范。派生类必须实现抽象类中的纯虚函数，否则派
生类也会成为抽象类
 
派生类的访问机制 :  
1. 公有继承：
public->public
protected->protected
private->private
2. 保护继承 :
public->protected
protected->protected
private->private
3. 私有继承：
public->private
protected->private

## 第3页

private->private
赋值兼容性规则：  
1. 派生类的对象可以作为基类的对象来使用
2. 只有公有继承才允许
构造函数的执行规则与顺序：  
构造函数的调用规则：
如果用户定义有参构造函数， C++ 不会再提供默认无参构造，但是会提供默认拷贝构造
如果用户定义拷贝构造函数， C++ 不会再提供其他构造函数
构造函数的执行顺序：
1. 调用基类的构造函数
2. 组合成员的所属类的构造函数
3. 调用对象成员所属类的构造函数
4. 执行派生类的构造函数体
（当其他类对象作为本类的成员，构造时先构造对象，再构造自身）
二义性的产生：  
1. 当一个派生类继承自两个或多个基类，而这些基类中存在同名的成员变量
2. 在派生类中访问该成员变量，会产生二义性
解决方法：
1. 使用类名来消除二义性
2. 出现菱形继承时，可以使用虚拟继承
常成员函数：  
 定义：在函数声明后加上 const
 特性：
1. 不修改对象数据
2. 常对象只能操作常成员函数
构造函数的调用时机：  
1. 对象创建时
2. 对象数组创建时
3. 使用动态分配创建对象（ new ）
不能被调用构造函数的情况：
1. 仅声明指针、引用或类型别名时
2. 使用类作为函数模版
拷贝构造函数的调用时机：  
1. 通过另一类型对象初始化一个对象
2. 对象作为函数参数传递时
3. 作为函数返回值时
转换构造函数：

## 第4页

形式：只有一个参数，它能够将参数类型的数据转化为类的对象
C++ 面向对象的三大特性 ;  
1. 封装
2. 继承
3. 多态
访问权限：  
1. public: 类内可以访问   类外可以访问   
2. protected: 类内可以访问   类外不可以访问   儿子可以访问父亲中的保护内容
3. private: 类内可以访问   类外不可以访问   儿子不可以访问父亲中的保护内容
struct 和 class 的区别：  
 在C++ 中 struct 和 class 的唯一区别是  其默认访问权限不同
struct 默认访问权限是公共 (public)
class 默认访问权限是私有 (private)
默认构造函数的调用：  
 调用默认构造函数时，不要加（）
 因为下面这行代码，编译器会认为是一个函数的声明，不会认为是在创建对象
 Person P1();
深拷贝与浅拷贝：  
 深拷贝：在堆区重新申请空间，进行拷贝操作
 浅拷贝：简单的赋值靠别操作
 （浅拷贝带来的问题是堆区的内存重复释放）
初始化列表：  
 语法：构造函数 (): 属性 1 （值 1 ），属性 2 （值 2 ） . 。。 {}
 #include <iostream>
class MyClass {
private:
    int* data;
public:
    MyClass() {
        data = new int(10);
    }
    // 深拷贝构造函数
    MyClass(const MyClass& other) {
        data = new int(*other.data);
    }
};

## 第5页

成员函数与成员变量：  
 在C++ 中，成员函数和成员变量时分开存储的
 C++ 编译器会给每个空对象也分配一个字节空间，是为了区分空对象占内存的位置且每个空对象也都
应该有一个独一无二的内存地址
非静态成员变量     属于类的对象上
静态成员变量         不属于类的对象上
非静态成员函数     不属于类的对象上
静态成员函数         不属于类的对象上
this 指针：  
 C++ 提供特殊的对象指针， this 指针，来指向被调用的成员函数所属的对象
 this 指针是隐含每一个非静态成员函数内的一种指针
 this 指针不需要定义，可以直接使用
 this 指针的用途：
当形参和成员变量同名时，可用 this 指针来区分
在类的非静态成员函数中返回对象本身，可以使用  return *this
 
 C++ 中空指针也可以调用成员函数，但是也要注意有没有使用到 this 指针，如果使用了 this 指针，需要
加以判断保证代码的健壮性
运算符重载：  
1. 加号运算符的重载：
2. 左移运算符的重载：class Person {
private:
    std::string name;
    int age;
public:
    // 带有形参的构造函数
    Person(const std::string& n, int a) : name(n), age(a) {
    }
    void display() {
        std::cout << "Name: " << name << ", Age: " << age << std::endl;
    }
};
 Complex operator+(const Complex& other) const {
        return Complex(real + other.real, imag + other.imag);
    }

## 第6页

3. 递增运算符的重载：
 
4. 赋值运算符的重载：
要注意深拷贝和浅拷贝
5. 关系运算符的重载：
继承：  
 语法： class 子类  : 继承方式  父类 1 ，继承方式   父类 2
 多继承可能会引发父类中有同名函数的出现，需要加作用域区分
菱形继承：  
 当菱形继承，两个父类拥有相同的数据，需要加作用域区分
 但这份数据我们知道，只有有一份就可以，菱形继承导致数据有两份，资源浪费
 所以需要利用虚继承，解决菱形继承的问题，继承之前，加上关键字 virtual ，变为虚继承
多态：  friend ostream& operator<<(ostream& os, const Person& p);
//声明
ostream& operator<<(ostream& os, const Person& p) {
    os << "Name: " << p.name << ", Age: " << p.age;
    return os;
}//类外的定义
 // 前置递增运算符重载
Counter& operator++() {
        ++count;
        return *this;
    }
 // 后置递增运算符重载
Counter operator++(int) {
        Counter temp(*this);
        ++count;
        return temp;
    }
 // 赋值运算符重载
    MyClass& operator=(const MyClass& other) {
        if (this!= &other) {  // 避免自我赋值
            value = other.value;
        }
        return *this;
    }
bool operator<(const Point& other) const {
        if (x < other.x) {
            return true;
            }

## 第7页

多态分为两类：
静态多态：函数重载和运算符重载属于静态多态，复用函数名
动态多态：派生类和虚函数实现运行时多态
静态多态和动态多态区别：
静态多态的函数地址早绑定：编译阶段确定函数地址
动态多态的函数地址晚绑定：运行阶段确定函数地址
动态多态的满足条件：
有继承关系
子类重写父类的虚函数
动态多态的使用：
父类的指针或者引用执行子类对象
例如：
#include <iostream>
using namespace std;
class Shape {
public:
    // 虚函数
    virtual void draw() {
        cout << "Drawing a Shape." << endl;
    }
};
class Circle : public Shape {
public:
    // 重写基类的虚函数
    void draw() override {
        cout << "Drawing a Circle." << endl;
    }
};
class Square : public Shape {
public:
    // 重写基类的虚函数
    void draw() override {
        cout << "Drawing a Square." << endl;
    }
};
int main() {
    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();
    // 调用虚函数，实现多态
    shape1->draw();
    shape2->draw();
    delete shape1;
    delete shape2;

## 第8页

纯虚函数和抽象类：  
再多态中，通常父类中虚函数的实现是毫无意义的，主要都是调用子类重写的内容
因此可以将虚函数改为纯虚函数
纯虚函数的语法： virtual  返回值类型    函数名  （参数列表） =  0 ；
当类中有了纯虚函数，这个类也称为抽象类
抽象类的特点：
无法实例化对象
子类必须重写抽象类中的纯虚函数，否则也属于抽象类    return 0;
}
#include <iostream>
using namespace std;
class Shape {
public:
    // 纯虚函数
    virtual void draw() = 0;
};
class Circle : public Shape {
public:
    // 实现纯虚函数
    void draw() override {
        cout << "Drawing a Circle." << endl;
    }
};
class Square : public Shape {
public:
    // 实现纯虚函数
    void draw() override {
        cout << "Drawing a Square." << endl;
    }
};
int main() {
    // 不能创建  Shape 类的对象，因为它包含纯虚函数
    // Shape shape;  // 错误：不能实例化抽象类
    Shape* shape1 = new Circle();
    Shape* shape2 = new Square();
    shape1->draw();
    shape2->draw();
    delete shape1;
    delete shape2;

## 第9页

函数模版  
函数模版作用：建立一个通用函数，其返回值类型和形参类型可以不具体制定，用一个虚拟的类型来表
示
语法： template
注意事项：
自动类型推导：必须推导出一直到数据类型 T 才可以使用
模版必须确定出 T 的数据类型，才可以使用
类模板  ：  
类模版的作用：建立一个通用类，类中的成员数据类型可以不具体确定，用一个虚拟的类型来代表
     return 0;
}
#include <iostream>
using namespace std;
// 函数模板
template <typename T>
T maxValue(T a, T b) {
    return (a > b)? a : b;
}
#include <iostream>
using namespace std;
// 类模板
template <typename T>
class MyPair {
public:
    T first;
    T second;
    MyPair(T a, T b) : first(a), second(b) {}
};

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_C++_课程MOC|C++ MOC]]
