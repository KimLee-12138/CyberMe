---
id: extract-java-0e5e84ca
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/PDF/JAVA_Java - 飞书云文档.pdf_课件_未知日期_0e5e84ca.pdf]]"
source_pages: all
source_hash: "0e5e84ca81c75c5e83124787f53b939eebee417a7807297d9f97673168d5b26a"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# Java - 飞书云文档.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

Java 
李尚凯
 今天修改
🤡1.值传递与引用传递  
①值传递是基本数据类型 的值给形参，在方法中对形参的修改将不会影响原来的变量
②引用传递 是对象引用，是把对象的地址传递给 形参，在方法体内对参数的修改会影响原来的对象
🤡2.抽象类与接口  
1.abstr act ：   
1.用abstract 修饰的类是 抽象类，用abstract 修饰的方法是抽象方法  
2.抽象类中可以有零个或多个抽象方法，抽象方法只指定方法名和具体类型，而不写实现代码；也可        以包含非抽象方法，非抽象方法
可以调用抽象方法
3.抽象类不能创建对象，必须派生子类，若子类是具体类，则具体类必须实现抽象类中所有抽象方法      （覆盖），若子类还是抽象类，
如果父类中已有同名 abstract 方法，则子类中不能再有同名的抽象方法  
4.抽象类可以有声明，声明能引用所有具体子类的对象  
 5.abstr act 不能与 final 并列修饰同一个类（逻辑矛盾，因为 abstract 类必须被 继承，而final 类不能被继   承）； abstract 不能与 private ，
static， final ， native 并列修饰同一个方法； abstract 类中不能有    priv ate 成员（因为 抽象类必须有子类，抽象类无法自己实例化对象，而子
类又无法访问 父类的private 成员）   
2.interf ace ：   
1.定义接口  
public interf ace m yinterf ace [extends f atherinterf ace]{  
static final int a=1;  
abstract int f unction(int a);  
} 
用关键字 interface 定义，要么 public 要么缺省  
内部数据类型 全是final static ，访问级别要么 public 要么缺省  
没有构造方法（因为不是类，没有用 class 定义，与 抽象类不同），但所有成员方法都是抽象方法（可以不用 abstract 修饰，但性质是抽象
方法）

## 第2页

接口可以通过 extends 关键字声明接口的父接口  
2.实现接口  
public void class A implements m yinterf ace{ 
public int f unction(int a){  
return a;  
} 
} 
在类中用 implements 关键字实现接口，一个类可以实现多个接口，一个接口也可以被多个类实现  
接口的实现类可以 继承接口中定义的静态常量
如果实现接口的类不是 抽象类，那么实现类中必须实现接口中的所有抽象方法；如果实现接口的是抽象类，那么它可以不实现该接口的所
有方法，但对抽象类的任何一个非抽象子类而言，接口中所有抽象方法必须被实现， 反正非抽象类中不能有抽象方法（ 继承了父类的抽象方法
必须具体实现）  
子类实现接口的抽象方法时必须显式使用 public 修饰符

## 第3页

🤡3.泛型与框架  
ArrayList  (基于数组 ) ： 
•内部结构 ：ArrayList 内部封装了一个 动态数组  (Object[])。数组在内存中是连续存储 的。 
•劣势：当进行 添加或删除 操作（特别是插入到中间或删除中间元素）时，为了保持 内存连续性，必须将操作点之后的所有元素 向后或向前
移动（System.arr aycopy ）。这需要大量的内存复制操作，时间复杂度为  $O(N)$ ，效率较低。  
LinkedList ( 基于链表)： 
•内部结构 ：LinkedList 内部是双向链表 结构。每个节点（ Node ）包含数据以及指向前一个节点（ prev ）和后一个节点（ next ）的引用（指
针）。
•优势：进行添加或删除 操作时，只需要 修改相关节点的引用指向 即可（断开旧链接，连上新链接），不需要移动任何其他元素。无论数据
量多大，该物理操作的时间复杂度都是  $O(1)$ ，因此在频繁增删的场景下性能远优于  ArrayList。
🤡4.final和 finally  
【final 的特点】  
1.修饰数据成员（变量）：  
◦该变量变为 常量，其值一旦初始化后就 不能被修改 。
2.修饰方法：  
◦该方法可以 被子类继承，但是不能被重载
3.修饰类：  
◦该类不能被继承（即不能有子类）
【finally 的用途】  
•用途：finally 只能配合  try-catch 语句块使用。  
•特点：无论  try 块中是否发生异常，也不管有没有  catch 住异常， finally 代码块中的代码 一定会被执行 。 
•场景：通常用于 释放资源 ，例如关闭数据库连接、关闭文件流（ IO ）、释放锁等操作，确保资源不会泄露。  
【static 】 
用static修饰的数据成员不属于任何一个类的具体对象，而是类的 静态数据 成员，一个类的任何对象访问它获取的都是相同的值  
用static修饰的方法，可以被所有对象访问， static 方法内部代码只能访问类中 static 属性或方法，不能访问类中非 static 属性或方法（因为
那是对象方法），但非 static 方法（对象方法）可以访问 static 数据成员  
🤡5.多线程  
线程和进程的区别
1.进程是独立执行的实体，一个执行中的程序，每个进程有独立的一块 内存空间代码，一组系统资源，每个进程内部数据与状态都独立
（程序的一次执行）  
2.线程是进程内的 执行单元 ，同类的多个线程共享一块 内存空间和系统资源， 多线程是指一个进程中运行多个不同的线程 （进程中程序代
码的一个执行序列）
1.代码实现
方法一：继承  Thread 类 
代码块
// 定义一个类继承  Thread
class SumThread extends Thread { 
    @Override 
    public void run() { 
        int sum = 0; 
        for (int i = 1; i <= 10000; i++) { 
            sum += i; 
        } 
        System.out.println("继承  Thread 方式计算结果 : " + sum); 
    }
} 1
2
3
4
5
6
7
8
9
10
11

## 第4页

public class TestThread { 
    public static void main(String[] args) { 
        // 启动线程  
        new SumThread().start(); 
    }
} 
🤡方法二：实现  Runnable 接口 
代码块
// 定义一个类实现  Runnable 接口 
class SumRunnable implements Runnable { 
    @Override 
    public void run() { 
        int sum = 0; 
        for (int i = 1; i <= 10000; i++) { 
            sum += i; 
        } 
        System.out.println("实现  Runnable 方式计算结果 : " + sum); 
    }
} 
public class TestRunnable { 
    public static void main(String[] args) { 
        // 创建任务对象  
        SumRunnable task = new SumRunnable(); 
        // 将任务交给  Thread 对象执行  
        new Thread(task).start(); 
    }
} 
🤡2.两种定义方式的区别
🤡3.场景回答
题目问：  如果该线程类已经继承了某个父类，那么应该使用哪种方法定义该线程？
回答：  应该使用  实现 Runnable 接口 的方法。  原因：  因为 Java 不支持多重继承 （即一个类不能同时继承两个父类）。如果该类已经继
承了某个业务父类，它就不能再继承  Thread 类了，但它可以实现  Runnable 接口，从而兼顾父类功能和多线程能力。  
💡4.死锁
一、 什么是死锁？ 
死锁是指两个或两个以上的线程在执行过程中，因 争夺资源 而造成的一种 互相等待 的现象。如果没有外力干涉，它们都将无法继续执行下去。
通俗比喻：  两个人过独木桥， A 在桥头要去  B 那边， B 在桥头要去  A 那边。桥很窄（资源 互斥），A 占着一边不退让（占有且等待）， B 也
占着一边不退让，且谁也推不动谁（不可抢占），结果两人大眼瞪小眼，谁也过不去。
二、 产生死锁的四个必要条件  
这四个条件 必须同时满足 才会发生 死锁。只要破坏其中任何一个，死锁就解除了。
1.互斥条件 (Mutual Exclusion ): 12
13
14
15
16
17
18
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

## 第5页

◦资源是独占的，同一时间只能被一个线程使用（如  synchronized 锁住的资源）。  
2.请求与保持条件  (Hold and Wait):  
◦线程已经持有了至少一个资源，但又提出了新的资源请求，而新资源被其他线程占有。此时该线程 保持对自己已获资源的占有，同时 等
待新资源。
3.不可剥夺条件  (No Preemption):  
◦线程已获得的资源在未使用完之前，不能被其他线程强行抢走（ synchronized 就是不可抢占的，除非线程自己释放）。  
4.循环等待条件  (Circular Wait):  
◦发生死锁时，必然存在一个进程 - 资源的环形链。例如：线程  A 等待  线程  B 的资源，线程  B 等待  线程  A 的资源。  
🤡6.覆盖与重载  
1.重载是在 一个类中方法名相同 ，但参数类型或者参数个数不同 的方法， 重载与修饰符，返回类型无关  
2.覆写是子类继承父类 中的方法， 方法名，参数类型和参数个数要和父类一样，而返回值类型以及抛出的异常类型，要么和父类相同，要么是
父类类型的子类，修饰符的限制需要大于父类的修饰符
3.static方法可以覆盖 static 方法，不能覆盖非 static 方法，也不能被非 static 方法覆盖  
4.方法前有 final 修饰符，则此方法不能在子类方法中进行覆盖  
5.抽象类中如果存在抽象方法，则具体子类中必须对抽象方法进行覆盖  
方法名称相同，参数名称相同，返回类型相同：覆盖
方法名称相同，参数名称不同：重载
方法名称相同，参数名称相同，返回类型不同：编译不能通过
💡7.Map接口 
以下是针对  第 7 题 的完整解答：  
题目内容
1.简述 Java 集合框架中  Map 接口的特点，并简述其两个实现类  HashMap 与  TreeMap 的区别。  
解答
1.Map 接口的特点  
•键值对存储 ：Map 接口用于存储键值对（ Key-Value Pair）映射关系的数据。  
•键（Key ）唯一：Map 中的键（ Key ）不允许重复，每个键最多只能映射到一个值。  
•值（Value ）可重复 ：Map 中的值（ Value ）可以重复，不同的键可以指向相同的值。  
•非 Collection 子接口：Map 接口没有 继承 Collection 接口，它是独立的一个顶层接口。

## 第6页

💡8.字符串  
1. 结果分析  
•程序一运行结果为  "a" 的原因：  
◦String 是不可变类  (Immutable) 。 
◦在 changePara 方法中，执行  s = s + "hello" 时，并没有修改原来的那个  "a" 对象，而是 在内存中创建了一个新的  String 
对象 "ahel lo"，并将方法内的 局部变量  s 指向了这个新对象。  
◦main 方法中的  s 依然指向原来的  "a" 对象，所以打印结果为  "a" 。 
•程序二运行结果为  "ahello" 的原因：  
◦StringBuilder 是可变类  (Mutable) 。 
◦在 changePara 方法中，执行  s.append("hello") 时，直接修改了堆内存中同一个  StringBuilder 对象的内容 。 
◦main 方法中的  s 指向的也是这个对象，所以打印结果为被修改后的  "ahel lo" 。 
2.知识总结  
1.string，stringbuf fer，stringbui lder实现都是基于 字符数组 ，都封装了对字符串的一系列操作， String内部实现基于常量字符数组， 是final类
型，不能被修改， StringBuilder 和 StringBuffer 内部实现基于普通字符数组， 可以修改，数组大小可以根据字符串实际长度实现自动扩容
2.字符串构建方法， 考最多创建几个对象  
//只有用引号包含文本的方式创建的 string 对象间使用 + 连接产生的新对象才会加入字符串池中  
//所有用 new 方式创建的新对象 + 连接的表达式所产生的新对象都不会被加入字符串池中

## 第8页

💡9.异常 
知识总结
1.Java 异常体系结构  (Hier archy) 
在 Java 中，所有的异常对象都 继承自一个共同的 父类：java.lang.Throwable。 
Throwable 分为两个大分支：  
1.Error (错误 )： 
◦含义：这是系统级的灾难，程序通常 无法恢复 。例如： JVM 内存溢出 (OutOfMemoryError)、栈溢出  (StackOverflowError)。 
◦处理：我们一般 不在代码里捕获处理它，因为处理不了。
2.Exception ( 异常 )： 
◦含义：程序运行时的逻辑错误或外部问题，程序 可以处理并恢复 。
◦分类：
▪受检异常  (Checked Exception) ：编译器强制要求你处理（如  IOException, SQLException）。如果你不处理，代码编译都
通不过。
▪非受检异常  (Unchecked/Runtime Exception) ：继承自 RuntimeException。通常是代码逻辑错误（如空指针  
NullPointerException、数组越界  IndexOutOfBoundsException）。编译器不强制要求处理。
2.捕获异常： try-catch-final ly 
这是我们处理异常的 “ 盾牌 ” 。 
•try：把可能发生异常的代码包起来。  
•catch：如果  try 里面出事了，在这里进行补救（捕获）。  
•finally：无论出没出事， 一定要执行的代码（通常用于关闭资源，如数据库连接、 IO流） 
3.自定义异常  (Custom Ex ception)  
Java 自带的异常（如空指针、数组越界）有时候不能准确描述具体的业务问题（比如 “ 余额不足 ” 、 “ 用户不存在 ” ）。这时我们需要自定义异
常。
步骤：
1.创建一个类。

## 第9页

2.继承 Exception (如果要强制处理 ) 或  RuntimeException (如果不需要强制处理 ) 。 
3.提供构造方法，调用 父类的 super(message)。
题目分析
问题所在 ： 代码中的  SelfException 继承自  Exception 类，属于  检查型异常  (Checked Exception) 。 方法  called() 声明抛出
了该异常  (throws SelfException)，因此在  main 方法中调用  called() 时，必须对该异常进行处理，否则编译器会报错（编译不
通过）。
解决方案
在 Java 中，处理检查型异常有两种方式，对于  main 方法，通常建议使用  try-catch 块 进行捕获处理。  
修正后的代码如下：
代码块
//方法一  
public static void main(String[] args) { 
    try { 
        // 尝试调用可能抛出异常的方法  
        called(); 
    } catch (SelfException e) { 
        // 捕获并处理异常  
        e.printStackTrace(); // 打印异常堆栈信息，或者输出自定义错误提示  
        System.out.println("捕获到了自定义异常 : " + e.getMessage()); 
    }
} 
//方法二  
public static void main(String[] args) throws SelfException {      
    called();  
} 
Try-catch-final l: 
代码块
public void readFile() { 
    try { 
        // 1. 尝试执行可能出错的代码  
        System.out.println("开始计算 ..."); 
        int result = 10 / 0; // 这里会发生  ArithmeticException 
        System.out.println("计算结果： " + result); // 这行不会执行  
         
    } catch (ArithmeticException e) { 
        // 2. 捕获特定的异常并处理  
        System.out.println("出错了：不能除以  0 ！ "); 
        e.printStackTrace(); // 打印错误堆栈信息  
         
    } catch (Exception e) { 
        // 3. 可以有多个  catch ，父类异常通常放在最后兜底  
        System.out.println("发生了其他未知异常 "); 
         
    } finally { 
        // 4. 无论是否发生异常，这里都会执行  
        System.out.println("计算结束，清理资源。 "); 
    }
} 
抛出异常： throw vs thr ows 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

## 第10页

代码块
// 使用  throws 声明该方法可能会抛出异常（甩锅给调用者）  
public void setAge(int age) throws IllegalArgumentException { 
    if (age < 0) { 
        // 使用  throw 真正地抛出一个异常对象（制造异常）  
        throw new IllegalArgumentException("年龄不能为负数 "); 
    }
    System.out.println("年龄设置为： " + age); 
} 
// 调用者必须处理这个异常  
public void main() { 
    try { 
        setAge(-5); 
    } catch (IllegalArgumentException e) { 
        System.out.println("设置失败： " + e.getMessage()); 
    }
} 
自定义异常
代码块
// 1. 定义一个 “ 余额不足异常 ” 
class InsufficientBalanceException extends RuntimeException { 
    public InsufficientBalanceException(String message) { 
        super(message); // 将错误信息传给父类  
    }
} 
// 2. 在业务中使用  
class BankAccount { 
    double balance = 100.0; 
    public void withdraw(double amount) { 
        if (amount > balance) { 
            // 抛出自定义异常  
            throw new InsufficientBalanceException("取款失败：余额不足，当前只有  " + 
        } 
        balance -= amount; 
        System.out.println("取款成功 "); 
    }
} 
// 3. 测试 
public class Test { 
    public static void main(String[] args) { 
        BankAccount account = new BankAccount(); 
        try { 
            account.withdraw(200); 
        } catch (InsufficientBalanceException e) {
            System.out.println("捕获到业务异常： " + e.getMessage()); 
        } 
    }
} 
💡10.super.i 和 this.i 的作用  1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

## 第11页

分析下列程序
1. this.i 和 super.i 分别是什么含义？  
•this.i：指的是 ** 当前类（子类  Construct）**中定义的成员变量  i。 
◦解析：由于子类  Construct 定义了一个与父类同名的变量  i，发生了 “ 变量遮蔽 ” (Shadowing) 。在子类中直接使用  i 或 
this.i 时，默认访问的是子类自己的那个变量。  
•super.i：指的是 ** 父类（ Pare）**中定义的成员变量  i。 
◦解析：关键字  super 用于显式访问被子类遮蔽的父类成员。
1.该程序是否有错误？  
•有错误（编译错误）。
错误原因：
•父类 Pare 定义了一个带参数的构造方法  Pare(int i)，这导致  Java 编译器不再自动提供 默认的无参构造方法  Pare()。 
•子类 Construct 的构造方法  Construct(int num) 中，没有显式调用父类的构造方法。此时， Java 编译器会默认尝试插入一句  
super(); 来调用父类的无参构造方法。  
•因为父类中 不存在无参构造方法，所以编译失败。
2.指出修改方案  
修改方法：  在子类  Construct 的构造方法的第一行， 显式调用 父类已存在的带参构造方法。  
代码修改示例：
Construct(int num) {  
    super(num); // 【新增这行】显式调用父类构造器  Pare(int i)  
    i = num;  
} 
💡1.知识总结（ this 的作用）：  
1.核心场景一：解决 “ 重名 ” 冲突（最常用）  
当局部变量 （比如方法参数）和 成员变量 （类里定义的属性）名字一样时， Java 会默认遵循 “就近原则 ”，使用局部变量。  这时，我们需要用  
this 来特指 “成员变量 ” 。 
•场景：构造方法或  Setter 方法中。  
•口诀：this.name 是我的属性， name 是别人传进来的参数  
代码块
public class Student { 
    String name; // 成员变量  
    // 构造方法  
    public Student(String name) { 
        // name = name;  <-- 错误！这是把自己赋值给自己，成员变量没变  
         
        this.name = name; // 正确！把参数  name 赋值给当前对象的成员变量  name 
    }
} 
💡2.核心场景二：构造方法 “ 偷懒 ” 互调（构造器链）  
如果一个类有多个构造方法（重载），我们不想在每个构造方法里都写一遍重复的初始化代码，可以用  this(...) 来调用本类的其他构造
方法。
•语法：this(参数 ...) 
•铁律：必须写在构造方法的第一行！
代码块1
2
3
4
5
6
7
8
9
10

## 第12页

public class Student { 
    String name; 
    int age; 
    // 1. 全参构造方法（干活最全的）  
    public Student(String name, int age) { 
        this.name = name; 
        this.age = age; 
    }
    // 2. 无参构造方法（偷懒的）  
    public Student() { 
        // 调用上面那个全参构造方法，给个默认值  
        // 相当于：我虽然没传参，但我委托全参构造器帮我初始化为  " 未知 ", 0 
        this("未知姓名 ", 0);  
    }
} 
💡3.核心场景三：把自己交出去（返回或传递）
有时候我们需要把 “ 我自己 ” （当前对象）作为一个参数传递给别的函数，或者作为返回值返回（常见于链式调用）。  
•用法：直接使用  this。 
代码块
public class Person { 
    // 1. 链式调用（ Builder 模式的基础）  
    public Person grow() { 
        this.age++; 
        return this; // 返回当前对象自己，这样可以一直  .grow().grow() 
    }
    // 2. 把自己传给别人  
    public void register() { 
        // 假设有一个登记册类  RegisterBook 
        // 把 “我 ” 传进去进行登记  
        RegisterBook.add(this);  
    }
} 
💡1.⚠ 一个致命禁区： Static 方法中不能用  this 
这是考试和面试的 超级坑点 。
•规则：静态方法 （static ）中绝对不能出现  this 关键字。  
💡11.多线程的互斥与同步  
1.结论 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
1
2
3
4
5
6
7
8
9
10
11
12
13
14

## 第13页

不能。 在多线程环境下，如果不采取同步措施， Sta 对象的  size 和 data 数据成员  不一定  能够得到预期的结果（即可能会出现数据
丢失或覆盖的情况）。
1.原因分析
根本原因在于  addChar 方法中的代码  data[size++] = c; 不是原子操作 。 
这行代码在  JVM 底层执行时，实际上包含了以下三个步骤：  
1.读取：读取当前  size 的值（例如  size = 0）。 
2.赋值：将字符  c 存入数组  data 的指定位置（ data[0] = c）。 
3.自增并写回 ：计算  size + 1 并将新值写回内存（ size 变为 1）。 
并发冲突场景：  假设线程  1 和线程  2 同时进入该方法：  
1.线程 1 读取了  size 为 0。 
2.线程 2 在同一时刻也读取了  size，因为线程  1 还没来得及修改，所以线程  2 读到的也是  0 。 
3.线程 1 将字符  'k' 写入  data[0]。 
4.线程 2 将字符  'h' 写入  data[0] —— 注意：这里发生了覆盖， 'k' 丢失了。  
5.线程 1 将  size 更新为  1 。 
6.线程 2 也将  size 更新为  1 。 
最终结果：  此时 size 为 1（预期应该是  2 ），且数组中只有  'h' （ 'k' 被覆盖）。这就是典型的 竞态条件  (Race Condition ) 问题。  
2.修改方案
要解决这个问题，必须保证  addChar 方法的操作是 原子性的，即同一时刻只能有一个线程执行该方法。  
最简单有效的方法是使用  synchronized 关键字修饰该方法。  
修改后的代码：
class Sta { 
    private int siz e = 0;  
    private char[] data = new char[10];  
    // 修改方案：添加  synchronized 关键字，使其成为同步方法  
    public synchr onized void addChar(char c) {  
        data[siz e++] = c;  
    } 
} 
修改后的效果：  当线程  1 进入  addChar 方法时，会获取当前对象的锁（ Monitor ）。此时线程  2 想要执行该方法，必须在外面等待，直到
线程 1 执行完毕并释放锁。这样就保证了  size 的读取、赋值和自增操作是按顺序安全执行的。

## 第14页

💡知识点
构造方法的 继承  
构造方法的 继承遵循以下的原则 : 
1.父类构造方法，子类可以在自己的构造方法中使用  super 来调用，但必须是子类构造方法的第一个可执行语句。  
2.若子类构造方法中没有显式调用 父类构造方法，也没有用 this 调用重载的其它构造方法，则在产生子类的对象时，系统在调用子类构造
方法的同时，默认调用父类无参构造方法。若子类构造方法中显式调用了父类构造方法，或使用了  this, 则不会默认调用父类无参构造方法。  
综上两点：子类的构造方法必定调用 父类的构造方法。如果不显式用 super 方法，必然隐含调用  super() 。 
创建对象时的初始化顺序 : 
1.系统会对数据成员进行默认初始化  
2.执行数据成员定义处的初始化语句  
3.调用构造方法为数据成员指定初值  
代码块
import java.util.ArrayList; 
import java.util.Collections; 
import java.util.Comparator; 
import java.util.List; 
public class Complex { 
    // (1) 定义  private 成员变量  
    private int real;   // 实部 
    private int imagin; // 虚部 
    // (2) 无参构造方法，初始化为  0 
    public Complex() { 
        this.real = 0; 
        this.imagin = 0; 
    }
    // (2) 带参构造方法，初始化实部和虚部  
    public Complex(int r, int i) { 
        this.real = r; 
        this.imagin = i; 
    }
    // (3) 定义  sub 方法，实现复数相减  
    public Complex sub(Complex a) { 
        // 新实部  = 当前实部  - 参数实部  1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第15页

int newReal = this.real - a.real; 
        // 新虚部  = 当前虚部  - 参数虚部  
        int newImagin = this.imagin - a.imagin; 
        // 返回一个新的  Complex 对象 
        return new Complex(newReal, newImagin); 
    }
    // 为了方便打印结果（如题目要求的  -3-5i ），重写  toString 方法 
    @Override 
    public String toString() { 
        if (imagin >= 0) { 
            return real + "+" + imagin + "i"; 
        } else { 
            return real + "" + imagin + "i"; // 虚部本身带负号，不需要加  "+" 
        } 
    }
     
    // 获取实部的方法，用于外部访问（排序时用到）  
    public int getReal() { 
        return real; 
    }
    public static void main(String[] args) { 
        // (4) 测试两个复数相减： (2+3i) - (5+8i) 
        Complex c1 = new Complex(2, 3); 
        Complex c2 = new Complex(5, 8); 
        Complex result = c1.sub(c2); 
         
        System.out.println("相减的结果 : " + result); // 输出应该为  -3-5i 
        // (5) ArrayList 存储并排序  
        List<Complex> list = new ArrayList<>(); 
        list.add(new Complex(-2, 3)); 
        list.add(new Complex(3, -5)); 
        list.add(new Complex(1, 4)); 
        System.out.println("排序前 : " + list); 
        // 使用  Collections.sort 和  Comparator 进行排序  
        // 按照实部从大到小排序  ( 降序 ) 
        Collections.sort(list, new Comparator<Complex>() { 
            @Override 
            public int compare(Complex o1, Complex o2) { 
                // 降序： o2 - o1 
                return o2.getReal() - o1.getReal(); 
            } 
        }); 
        System.out.println("排序后 ( 实部降序 ): " + list); 
    }
} 26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76

## 第16页

💡(1) 接口  Solid 、实现类  Cube 和  Cylinder 以及  Test 类 
代码块
// 1. 定义接口  Solid 
interface Solid { 
    public double calVol(); // 计算体积的抽象方法  
} 
// 2. 定义正方体类  Cube 实现  Solid 接口 
class Cube implements Solid { 
    private double side; // 边长 
    // 构造方法  
    public Cube(double side) { 
        this.side = side; 
    }
    // 实现  calVol 方法 
    @Override 
    public double calVol() { 
        return side * side * side; // 体积  = 边长 ^3 
    }
} 
// 3. 定义圆柱体类  Cylinder 实现  Solid 接口 
class Cylinder implements Solid { 
    private double radius; // 半径 
    private double height; // 高 
    // 构造方法  
    public Cylinder(double radius, double height) { 
        this.radius = radius; 
        this.height = height; 
    }
    // 实现  calVol 方法 
    @Override 
    public double calVol() { 
        return Math.PI * radius * radius * height; // 体积  = π  * r^2 * h 
    }
} 1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38

## 第17页

// 4. 定义测试类  Test 
public class Test { 
    // printVol 方法：利用多态，接收  Solid 接口类型  
    public void printVol(Solid solid) { 
        // 格式化输出，保留两位小数更美观（可选）  
        System.out.println("该图形的体积为 : " + String.format("%.2f", solid.calVol
    }
    public static void main(String[] args) { 
        Cube cube = new Cube(3.0); 
        Cylinder cylinder = new Cylinder(5.5, 4); 
         
        Test test = new Test(); 
        test.printVol(cube);      // 打印  Cube 的体积  
        test.printVol(cylinder);  // 打印  Cylinder 的体积  
    }
} 
💡(2) 设计  GraphCalcu 类 
代码块
// 5. 设计  GraphCalcu 类 
class GraphCalcu { 
    // 数据成员：持有  Solid 接口的引用  
    private Solid solid; 
    // 构造方法：接收任意  Solid 的实现类对象（ Cube 或  Cylinder ） 
    public GraphCalcu(Solid solid) { 
        this.solid = solid; 
    }
    // Calcu 方法：调用内部  shape 的  calVol 计算体积  
    public double Calcu() { 
        if (solid != null) { 
            return solid.calVol(); 
        } 
        return 0.0; 
    }
    // 题目给定的  main 方法用于测试  
    public static void main(String[] args) { 
        Cube cube = new Cube(3.0); 
        GraphCalcu gc = new GraphCalcu(cube); 
        System.out.println(gc.Calcu()); // 提供  Cube 的体积计算  
        Cylinder cylinder = new Cylinder(5.5, 4); 
        gc = new GraphCalcu(cylinder);  // 复用  gc 变量，指向新的对象  
        System.out.println(gc.Calcu()); // 提供  Cylinder 的体积计算  
    }
} 
服务端：39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

## 第18页

代码块import java.io.*; 
import java.net.ServerSocket; 
import java.net.Socket; 
public class ChatServer { 
    // 题目要求  (1): 监听本机  8377 端口 
    private static final int PORT = 8377; 
    // 题目要求  (3): 保存文件的路径  D 盘  chat.txt 
    private static final String FILE_PATH = "D:\\chat.txt"; 
     
    // 用于给客户编号，静态变量保证全局唯一且递增  
    private static int clientCount = 0; 
    public static void main(String[] args) { 
        System.out.println("服务器已启动，正在监听端口  " + PORT + "..."); 
         
        try (ServerSocket serverSocket = new ServerSocket(PORT)) { 
            while (true) { 
                // 题目要求  (1): 监听用户请求  
                Socket socket = serverSocket.accept(); 
                 
                // 客户编号  +1 
                clientCount++;
                System.out.println("客户端  " + clientCount + " 已连接 "); 
                // 题目要求  (1): 对于每一个用户请求，派发一个客户服务线程  
                ClientHandler handler = new ClientHandler(socket, clientCount); 
                new Thread(handler).start(); 
            } 
        } catch (IOException e) { 
            e.printStackTrace(); 
        } 
    }
    /** 
     * 题目要求  (3): 将接收到的消息保存到本地磁盘  D:\chat.txt
     * 注意：因为是多线程环境，写文件需要加锁  (synchronized) 防止数据 写入冲突  
     */ 
    public static synchronized void saveMessageToFile(String message) { 
        // 使用  FileWriter 的  append 模式  ( 第二个参数为  true) ，避免覆盖旧内 容 
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_PATH
            writer.write(message); 
            writer.newLine(); // 换行 
            writer.flush(); 
        } catch (IOException e) { 
            System.err.println("写入文件失败 : " + e.getMessage()); 
        } 
    }
    /** 
     * 内部类：专门处理单个客户端连接的线程  
     */ 
    private static class ClientHandler implements Runnable { 
        private Socket socket; 
        private int clientId; 
        public ClientHandler(Socket socket, int clientId) { 
            this.socket = socket; 
            this.clientId = clientId; 
        } 
        @Override 
        public void run() { 
            BufferedReader in = null; 
            PrintWriter out = null; 
            try { 
                // 获取输入流（读取客户端发来的消息）  
                in = new BufferedReader(new InputStreamReader(socket.getInputStr
                // 获取输出流（发送消息给客户端）， true 表示自动刷新缓冲区  1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71

## 第19页

out = new PrintWriter(socket.getOutputStream(), true); 
                String line; 
                // 题目要求  (2): 循环接收字符串消息  
                while ((line = in.readLine()) != null) { 
                    
                    // 题目要求  (4): 若消息为  "Bye" ，关闭连接并结束循环
                    if ("Bye".equalsIgnoreCase(line)) { 
                        System.out.println("客户端  " + clientId + " 断开连接 "); 
                        break; 
                    } 
                    // 题目要求  (3): 将接收到的消息保存到文件  
                    // 这里通常保存原始消息，也可以根据需求保存带编号的消息  
                    saveMessageToFile("Client" + clientId + ": " + line); 
                    // 题目要求  (2): 在消息前面加上客户编号发送给相应的用户  
//格式范例 :"Client1Hello"
客户端：
代码块
import java.io.*; 
import java.net.Socket; 
import java.util.Scanner; 
public class ChatClient { 
    public static void main(String[] args) { 
        // 连接本机的  8377 端口 
        try (Socket socket = new Socket("127.0.0.1", 8377); 
             BufferedReader in = new BufferedReader(new InputStreamReader(socket
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true); 
             Scanner scanner = new Scanner(System.in)) { 
            System.out.println("已连接到服务器！请输入消息（输入  Bye 退出）： "); 
            // 启动一个单独的线程负责接收服务器的回复  
            new Thread(() -> { 
                try { 
                    String fromServer; 
                    while ((fromServer = in.readLine()) != null) { 
                        System.out.println("收到服务器回复 : " + fromServer); 
                    } 
                } catch (IOException e) { 
                    System.out.println("服务器已断开。 "); 
                } 
            }).start(); 
            // 主线程负责读取键盘输入并发给服务器  
            while (scanner.hasNextLine()) { 
                String input = scanner.nextLine(); 
                out.println(input); // 发送给服务器  
                if ("Bye".equalsIgnoreCase(input)) { 
                    break; 
                } 
            } 
        } catch (IOException e) { 
            e.printStackTrace(); 
        } 
    }
} 
💡引用72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39

## 第20页

这个例子看一下， java 变量访问是基于声明的静态类型，而不是对象的实际类型， 父类声明指向子类对象，变量没有多态性，方法才会有多态性，
所以在子类对象中方法有重载

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
