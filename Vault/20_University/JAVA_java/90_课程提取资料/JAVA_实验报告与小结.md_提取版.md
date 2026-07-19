---
id: extract-java-1df19e4f
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_实验报告与小结.md_笔记_未知日期_1df19e4f.md]]"
source_pages: all
source_hash: "1df19e4fcfe5b616b4071146f56ca7feef5a76d978ff4ed044813429ce27f91a"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 实验报告与小结.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 实验四：多线程与集合框架类实验报告

## 一、实验名称

多线程与集合框架类

## 二、实验目的

1. 掌握多线程的创建方式（`Thread`类继承、`Runnable`接口实现）及线程调度机制（优先级、睡眠）。
2. 理解线程同步的必要性，掌握`synchronized`关键字解决线程安全问题。
3. 熟悉 Java 集合框架常用类（`ArrayList`、`LinkedList`、`HashSet`、`HashMap`）的特性与用法。
4. 理解泛型的概念及应用，掌握集合类的遍历、增删改查等操作。
5. 对比不同集合类的差异，能根据场景选择合适的集合。

## 三、实验环境

- 操作系统：Windows 10
- JDK 版本：JDK 1.8
- 开发工具：Eclipse

## 四、实验内容与步骤、结果及分析

### 1. 线程优先级与睡眠实验

#### 实验内容：

- 编写两个线程分别输出 1 到 10，设置不同优先级，观察执行机会；
- 给线程添加睡眠属性，高优先级线程睡眠更长时间，观察运行速度。

#### 核心代码（简化）：

```java
// 线程类（含睡眠属性）
public class Test extends Thread {
    int sleepTime;
    public Test(String name, int t) { super(name); sleepTime = t; }
    public void run() {
        for (int k = 1; k <= 10; k++) {
            System.out.println(getName() + ":" + k);
            try { sleep(sleepTime); } catch (InterruptedException e) {}
        }
    }
    public static void main(String[] args) {
        Thread x1 = new Test("first", 5000); // 高优先级，睡眠5秒
        x1.setPriority(6);
        x1.start();
        new Test("second", 200).start(); // 低优先级，睡眠200毫秒
    }
}
```

#### 实验结果：

（1）未加睡眠时：高优先级线程（`first`）输出次数更多，执行机会更高。

（2）添加睡眠后：低优先级线程（`second`）因睡眠短，更快完成 1-10 的输出。

#### 分析：

- 线程优先级仅为系统提供调度提示，高优先级线程获得 CPU 时间片的概率更高，但不绝对。
- `sleep()`方法会让线程暂停指定时间，此时 CPU 会切换到其他线程，因此睡眠短的线程运行更快。

### 2. 基于 Runnable 接口的跳动小圆窗体

#### 实验内容：

用`Runnable`接口实现多线程，创建窗体绘制随机位置的跳动小圆。

#### 核心代码（简化）：

```java
public class Test2 extends Frame implements Runnable {
    public Test2() { setSize(300, 300); setVisible(true); new Thread(this).start(); }
    public void run() {
        while (true) { repaint(); try { Thread.sleep(1000); } catch (Exception e) {} }
    }
    public void paint(Graphics g) {
        int x = 10 + (int)(Math.random()*100);
        int y = 10 + (int)(Math.random()*100);
        g.fillOval(x, y, 100, 100); // 绘制随机位置的圆
    }
    public static void main(String[] args) { new Test2(); new Test2(); } // 两个窗口
}
```

#### 实验结果：

两个窗体各自每隔 1 秒刷新一次，圆的位置随机变化，实现 “跳动” 效果。

#### 分析：

- 通过`Runnable`接口实现多线程，避免了单继承限制，更灵活。
- `repaint()`触发`paint()`方法重绘，结合`Thread.sleep(1000)`实现定时刷新。

### 3. 模拟火车售票系统（线程不安全）

#### 实验内容：

5 个线程模拟 5 个售票窗口，发售 100 张火车票，观察线程安全问题。

#### 核心代码（简化）：

```java
class ThreadSale implements Runnable {
    private int tickets = 100;
    public void run() {
        while (true) {
            if (tickets > 0) {
                try { Thread.sleep((int)(10*Math.random())); } catch (Exception e) {}
                System.out.println(Thread.currentThread().getName() + "售票：" + tickets--);
            } else System.exit(0);
        }
    }
}
public class TicketSystem {
    public static void main(String[] args) {
        ThreadSale t = new ThreadSale();
        new Thread(t, "窗口1").start();
        // 启动窗口2-5线程...
    }
}
```

#### 实验结果：

出现重复售票（如两个窗口同时卖出第 50 号票）或负票（如卖出 0 号票）。

#### 分析：

多个线程同时操作共享变量`tickets`，导致指令交错执行，出现线程安全问题。

### 4. 线程安全的售票系统（同步控制）

#### 实验内容：

对售票逻辑加锁，解决重复售票问题。

#### 核心代码修改：

```java
public void run() {
    while (true) {
        synchronized (this) { // 同步代码块，锁定当前对象
            if (tickets > 0) {
                try { Thread.sleep((int)(10*Math.random())); } catch (Exception e) {}
                System.out.println(Thread.currentThread().getName() + "售票：" + tickets--);
            } else System.exit(0);
        }
    }
}
```

#### 实验结果：

无重复售票或负票，100 张票被正确分配。

#### 分析：

`synchronized`确保同一时间只有一个线程执行同步代码块，避免共享变量的并发冲突。

### 5. 泛型与集合差异实验

#### （1）泛型数组

修改代码用增强 for 循环遍历：

```java
public class MyArray<T> {
    private T[] obj;
    public MyArray(T[] obj) { this.obj = obj; }
    void output() {
        for (T item : obj) { System.out.print(" " + item); } // 增强for循环
        System.out.println();
    }
}
```

**结果**：正确输出字符串数组和整数数组，泛型保证了类型安全。

#### （2）ArrayList 与 HashSet 差异

- `ArrayList`代码输出：`[1, 3, 5, 1, 2, 3]`（有序、允许重复）。
- `HashSet`代码输出：`[1, 2, 3, 5]`（无序、自动去重）。

**分析**：

- `ArrayList`基于动态数组，保留插入顺序，允许重复元素。
- `HashSet`基于哈希表，不保证顺序，通过`equals()`和`hashCode()`去重。

#### （3）HashSet 生成不重复序列

原代码用`HashSet`会编译失败（`Collections.sort()`不支持`Set`），修改如下：

```java
HashSet<Integer> x = new HashSet<>();
while (x.size() < 10) { x.add((int)(Math.random()*30)); } // 循环添加直到10个元素
List<Integer> list = new ArrayList<>(x); // 转换为List再排序
Collections.sort(list);
```

**结果**：输出 10 个不重复的有序整数。

### 6. ArrayList 存储学生成绩

#### 实验内容：

用`ArrayList`存储成绩，求最高分和平均分。

#### 核心代码（简化）：

```java
ArrayList<Double> scores = new ArrayList<>();
// 随机生成成绩...
double max = scores.get(0), sum = 0;
for (double s : scores) { max = Math.max(max, s); sum += s; }
System.out.println("最高分：" + max + "，平均分：" + sum/scores.size());
```

#### 结果：

正确计算最高分和平均分。

#### 分析：

`ArrayList`适合存储有序、可重复的数据，支持索引访问，便于遍历计算。

### 7. LinkedList 存储学生信息

#### 实验内容：

用`LinkedList`实现学生信息的增、删、查。

#### 结果：

- 列出学生：按插入顺序输出所有学生信息。
- 增加学生：成功添加新学生（学号唯一校验）。
- 删除学生：按学号正确删除指定学生。

#### 分析：

`LinkedList`基于双向链表，增删元素效率高（无需移动大量数据），适合频繁修改的场景。

### 8. Map 存储月份与天数

#### 实验内容：

用`HashMap`存储月份英文与天数的映射，支持查询。

#### 结果：

输入 “January” 输出 “31 天”，输入 “February” 输出 “29 天”（2024 年闰年）。

#### 分析：

`Map`通过 “键 - 值” 对存储，查询效率高，适合需要快速通过键获取值的场景。

### 9. 中英文翻译程序（Map 实现）

#### 实验内容：

用两个`HashMap`分别存储 “英文 - 中文” 和 “中文 - 英文” 映射，支持双向查询。

#### 结果：

- 输入 “apple” 输出 “苹果”，输入 “苹果” 输出 “apple”。
- 中文乱码通过`-Dfile.encoding=gbk`解决。

#### 分析：

双向`Map`映射实现高效互查，`HashMap`的`put`和`get`方法保证操作便捷性。

### 10. HashMap 存储用户与电话号码

#### 实验内容：

用`HashMap<Long, String>`存储电话号码（键）和用户名（值），遍历输出。

#### 核心代码（遍历）：

```java
Set<Long> phones = userPhones.keySet();
for (long phone : phones) {
    System.out.println("电话：" + phone + "，用户：" + userPhones.get(phone));
}
```

#### 结果：

无序输出所有用户与电话号码的对应关系。

#### 分析：

`HashMap`键唯一（电话号码不重复），`keySet()`方法获取所有键，遍历效率高。

## 五、实验小结

1. **多线程**：
   - 线程创建有两种方式：继承`Thread`类和实现`Runnable`接口，后者更灵活（避免单继承限制）。
   - 线程优先级影响调度概率，但需结合`sleep()`等方法控制执行顺序；同步机制（如`synchronized`）是解决线程安全的关键。
2. **集合框架**：
   - `ArrayList`（动态数组）适合有序、可重复、随机访问的场景；`LinkedList`（链表）适合频繁增删的场景。
   - `HashSet`（哈希表）自动去重、无序；`HashMap`（键值对）适合快速查询，键唯一。
   - 泛型通过类型参数保证集合操作的类型安全，避免强制类型转换。
3. **问题与解决**：
   - 线程安全问题可通过同步代码块解决；
   - `HashSet`排序需先转换为`List`；
   - 中文乱码可通过 JVM 参数`-Dfile.encoding=gbk`调整。

通过本次实验，深入理解了多线程的调度机制和集合类的特性，能根据实际需求选择合适的线程实现方式和集合类，为后续 Java 编程打下坚实基础。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
