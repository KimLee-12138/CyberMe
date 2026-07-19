---
id: extract-java-b42647d9
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/PDF/JAVA_汇总.pdf_课件_未知日期_b42647d9.pdf]]"
source_pages: all
source_hash: "b42647d9ec437e5162b39f85c7ce4a8fc9ad2e3d02a341b5ad914f5db42f3791"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 汇总.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

汇总
Java语⾔的特点
跨平台：引⼊字节码和 Java 虚拟机（ JVM ），实现⼀次编写，到处运⾏
可移植性 : 不受具体平台架构的影响
⾯向对象：提供对封装、继承、多态等机制的⽀持
简单安全：消除指针，接⼝机制等
多线程：提供多线程⽀持
JDK、 JRE 、 JVM 的含义、联系与区别
JDK:⽤于编写、编译和调试 Java 程序 ( 开发，⾯向开发者 )
JRE:Java 运⾏环境 ( 运⾏，⾯向⽤户 )
JVM：运⾏ Java 程序的虚拟机， Java 跨平台的核⼼
联系
JDK包含 JRE,JVM 是 JRE 的核⼼组件
Java数据类型
基本数据类型
整型、浮点、字符、字符串、布尔 (boolean)
引⽤类型
类类型
接⼝类型
数组类型
Java的整型溢出
由于 Java 的各类整型有相应的取值范围 (8,16,32,64), 在进⾏加减乘等算术运算以及类型间的转
换时，容易发⽣整型溢出
处理：进⾏模运算（取余），将结果环绕到有效范围内
基本类型对应的包装类以及包装类的作⽤
int----Integer char----Character 其它⾸字⺟⼤写
包装类的作⽤
获取相应基本类型的取值范围
Integer.MAX_VALUE Integer.MIN_VALUE
实现不同数据类型之间的转化
int a=Interger.parseInt(“123”) 字符串 -> 整型
⾃动装箱与⾃动拆箱  int 与 Integer 的相互转化
⾃动装箱：基本数据类型转换为对应的包装类

## 第2页

Integer a=100 等价于 Integer a=Interger.valueOf(100) Integer a=new Integer(num)
⾃动拆箱：包装类转换为基本数据类型
int b=a 等价于  int b=a.intValue()
逻辑运算符 & 与 && 的区别  位运算符 & 与逻辑运算符 & 的区别
逻辑运算符 && 在 & 的基础上，引⼊ “ 短路 ” 机制，提升运算速度
位运算符 & 表示按位与，对应位同时为 1 才为 1
Java中跳出多重循环的语句
break lab 跳出多重循环的外层循环 ( 需要 lab 标记 )
continue lab 跳出外层循环的本册循环，继续外层下⼀次循环（需要 lab 标记）
return
对象和对象引⽤的区别
存储地址：对象分配在堆内存上，使⽤ new 关键词进⾏创建，对象引⽤分配在栈内存上，是
指向对象的引⽤变量。通常通过对象引⽤来访问对象的属性和⽅法
存储内容：对象存储的是实际的属性和⽅法，⽽对象引⽤存储指向的对象的内存地址
⼀个对象可以有多个引⽤，⽽⼀个对象引⽤只能指向⼀个对象
对象作为参数传递的特点
对象作为参数传递时，实际上是对象引⽤的值传递（传递对象引⽤的副本），副本指向堆内
存的对象 , 对象本身不会被修改
对象的初始化顺序
对数据成员进⾏默认的初始化
执⾏数据成员定义处的初始化语句
调⽤构造⽅法为数据成员指定初值
static修饰符的特点与使⽤场景
特点
地址： static ⽤来修饰的数据成员，被保存在类的公共区中，不属于任何⼀个类的具体对
象
权限： static 修饰的代码块，不能直接访问类中的⾮ static 属性或⽅法
使⽤场景：某⼀变量为类的对象所共有，或者仅仅在类加载时进⾏⼀次初始化
final修饰符的作⽤
修饰属性
属性为常量
修饰⽅法
⽅法在⼦类中不能被覆盖，保证程序的安全性和正确性
修饰类
类不能被继承

## 第3页

(抽象类、接⼝不能⽤ final 修饰 )
数组对象的创建和初始化⽅法
基本数据类型和引⽤类型的区别
基本数据类型存储在栈空间中，具有固定的内存⼤⼩（由于建⽴在栈空间上，访问速度更
快）
引⽤类型的变量存储的是对象的引⽤，指向堆空间，动态分配内存，⼤⼩不固定。 当引⽤类
型的对象不再被使⽤时，会被垃圾回收器回收
Java的访问控制权限
public:公共访问权限，可以被任何其他类访问
protected ：继承访问权限，可以被同⼀包内的类以及不同包的⼦类或⼦类对象访问
包访问权限 : 默认的访问权限，⽆修饰符，只能被统⼀包中的类访问
private：类内部访问权限，只能被定义它的类访问
⼦类继承⽗类  extends
可⻅的属性与⽅法
只有 public 、 protected 的属性和⽅法在⼦类是可⻅的
⼦类构造⽅法实现顺序
传参
第⼀个可执⾏语句，利⽤ super 显式调⽤⽗类构造⽅法或者默认调⽤⽗类⽆参构造访案发
按照定义顺序，执⾏⼦类新增属性的初始化语句
执⾏⼦类构造⽅法的剩余代码
内存布局图的绘制
this与 super 的⽤法
this
this()，调⽤当前类的构造⽅法
this.名称，调⽤本类的属性或⽅法，⽤来区别同名形参或⽅法
super
super(参数列表 )
调⽤⽗类的构造⽅法，对⼦类从⽗类继承过来的数据成员进⾏初始化
super.数据成员， super. 成员⽅法  区分⼦类与⽗类中同名属性或⽅法
重载
定义：同⼀作⽤域内，有多个同名⽅法存在，这些⽅法具有不同参数类型或参数个数
作⽤：编译时多态的提现。在不同情形下，调⽤同名⽅法，可以实现函数⾏为的多态，提⾼
⽅法的通⽤性
覆写
⼦类在继承⽗类时，对⽗类中的某⼀⽅法进⾏覆盖重写

## 第4页

条件：⼦类的访问权限不能变⼩。⽅法名称、参数类型及个数必须严格⼀致。只能针对⾮静
态、⾮ final 、⾮构造⽅法
作⽤：运⾏时多态的体现。⼦类向上转型为⽗类时，提供⼀种统⼀的⽅式处理不同类型的对
象
组合和继承的区别以及使⽤场景
组合是 has-a 包含关系，指的是在⼀个类的实现中，以另⼀个类的对象作为数据成员。当⼀个
对象需要另⼀个对象的功能时 / 降低代码复杂度，常⽤组合
继承是 is-a 关系，体现的是⼀般与特殊的关系，耦合度较⾼。需要拓展⼀个类的功能，或者⼀
个类是另外⼀个类的特殊类型时，常⽤继承
Java运⾏时多态的含义
提供⼀种统⼀的⽅式处理对象，在运⾏时确定⽅法的具体实现。⽅法的覆写，抽象类、接⼝
的多重继承，均体现运⾏时多态
抽象类和接⼝的异同
同：
都具有抽象⽅法，均不能实例化，但可以作引⽤声明
抽象类：含有抽象⽅法的类，体现的是 is-a 关系
类中可以既含有抽象⽅法，也可以含有具体⽅法实现。
可以含有构造函数
只允许单⼀继承
关键字： abstract extends
接⼝：体现 can-do 关系  interface implements
接⼝中的⽅法均为抽象⽅法，只含有静态属性
允许多重继承
不能有构造函数
关键字  interface implements
内部类的定义和作⽤  匿名内部类的使⽤
在类的内部，再定义⼀个类，内部类可以直接访问外部类的所有成员
作⽤：隐藏底层实现细节
匿名内部类
匿名对象的使⽤场景
⼀个对象只需要进⾏⼀次⽅法调⽤
只作为参数传给⼀个函数使⽤
Throwable 的两个异常⼦类以及区别
Error：致命异常，如 StackOverflowError( 栈溢出异常 ) 、 OutOfMemoryError( 内存超出异常 ) ，程
序⽆法处理的异常，只能⼈⼯介⼊
Exception: ⾮致命异常

## 第5页

Exception 的分类
checked异常  受检异常
受到编译器检测
需要显式调⽤ throws 语句
分类
IO异常、线程中断异常 (Interrupted) 类定义异常 ...
unchecked 异常  ⾮受检异常
运⾏时异常  不受编译器检测
可以不显示调⽤ throws 语句
分类
空指针异常
算术异常
数组越界异常
⾮法传参异常
类转换异常 ....
异常处理的两种⽅式以及区别
throws语句
写在⽅法声明处，讲异常抛给调⽤⽅
try-catch-finally 语句
写在⽅法内，在本级抛出
结合 try-with-resource 语句块  声明需要关闭的资源
throw语句与 throws 语句的区别
throw语句⽤来⾃定义异常
throw new 异常类
finally⼦句的作⽤
finally⼦句必被执⾏，主要⽤于处理资源释放、设置返回值等作⽤
String,StringBuﬀer,StringBuilder 的异同
相同点：
都是字符串类，封装了对字符串的处理
可以⾃动检测数组越界等运⾏时异常
不同点
String内容不可变，具有线程安全性
StringBuﬀer 内容可变，是线程安全的
StringBuilder 内容可变，是⾮线程安全的，但在单线程中运算速度⽐ StringBuﬀer ⾼
不建议在 for 循环中使⽤ “+” 进⾏字符串拼接

## 第6页

与String的性质有关
创建线程的⽅法
继承 Thread 类（本质也是实现了 Runable 接⼝）
⽆法继承其他类
实现 Runnable 接⼝
主要是实现 run() ⽅法
⽅式更加灵活，多个线程共享某个对象的资源
volatile关键字的作⽤
禁⽤ CPU 缓存，保证⼀个线程对资源修改后其他线程⽴即可⻅
volatile修饰的变量，对其的操作都会在内存中进⾏
Java实现互斥的同步机制
synchronized 关键字
代码块： synchronized(it){...}, 锁 it
⽅法：锁 this 对象
静态⽅法：锁类
锁类
ReentrantLock 类
Java中流的分类
按⽅向：输⼊流  输出流
按读取类型：字节流  字符流
按发⽣源头：节点流  过滤流
InputStream 和 OutputStream 的⼦类
FileInputStream,PipedInputStream,ByteArrayInputStream,FilterInputStream,ObjectInputStream
....
字节流和字符流的转化
输⼊字节流转化为字符流 ( 读 )
InputStreamReader
InputStreamBuﬀer a=new InputStreamBuﬀer(System.in)
InputStreamBuﬀer a=new InpuStreamBuﬀer(new FileInputStream("example.txt"))
输出字符流转化为字节流（写）
OutputStreamWriter /PrintWriter
Java中的过滤流
作⽤：对节点流进⾏装配，提⾼读写效率，实现数据筛选、数据转换、提供缓冲等功能
常⽤过滤流
InputStreamBuﬀer OutputStreamBuﬀer

## 第7页

添加缓存区，提⾼读写性能
DateIputStream DateOutputStream
从字节流中读取写⼊基本数据类型
对象的序列化和反序列化
将实现了Serializable的对象的状态信息转换为字节流进⾏存储、传输 , 称为序列化。将字节序
列恢复为原对象，称为反序列化
Java的⽀持： ObjectInputStream ObjectOutputStream
使⽤情形：需要将对象进⾏持久化  ⽹络传输
Java中的 File 类（⽂件路径的抽象表示）
表示系统的⽂件或⽬录
getName() getPath()
Java对⽂件读写的⽀持
FileInputStream FileReader
FileOutputStream FileWriter
RandomAccessFile
TCP与 UDP 的区别
TCP在传输数据之前必然要建⽴连接，且传输量⼤， ServerSoket 、 Socket
UDP是不可靠协议，未建⽴连接，数据传输有⼤⼩限制，但传输效率⾼
DatagramSocket,DatagramPacket
ArrayList和 LinkedList 的区别
两者都是有序，元素可重复的对象集合
Linkedlist 的实现基于动态链表，查找元素时，必须从表头开始访问，查找效率低，但插⼊、
删除效率⾼。元素个数⼤于初始容量时，会⾃动扩容 50%
ArrayList的实现基于动态数组，通过索引直接定位，查找效率⾼，但增删改效率低
Vector和 ArrayList 的区别
两者都是 List 的实现类，元素有序、可重复
Vector使⽤ synchronized ⽅法，是线程安全的。当元素数量超过 Vector 初始⼤⼩时， Vector 会将
容量翻倍
ArrayList的⽅法不是同步的。当元素数量超出时，会将容量提升 50%
Map和 Collection 的区别
Map是双列的， Collecion 是单列的
Map的键是唯⼀的， Collection 中 Set 是唯⼀的
TreeMap和 HashMap 的区别
两者都可以实现 key 和 value 之间的映射
HashMap 没有按照关键字顺序排列， TreeMap 内部实现基于⼆叉查找树，返回排序的关键字
其它易错易漏

## 第8页

注意 Java 包的导⼊
Java.net.* Java.util.* Java.io.* Java.lang.*
java.lang 包有 Thread 类、 Runable 接⼝
整数变量 byte 的取值范围： -2^7 到 2^7-1 8 位
两个 byte 或 short 整数相加，默认转换为 int
char[] str="perkin" 会报错  不⽀持字符串类型到字符数组类型的转换
instanceof 对象运算符  Java 中的算术运算主要依靠 Math 类的静态⽅法  Math.sqrt() ，
Math.round(),Math.ceil(),Math.floor()
与C++不同， boolean 中的 true 和 false 不对应任何整数
数组初始化时的 foreach 语法
for(int x:arr)
for(int x[] arr1:arr)
for(int i:arr1)
在类的⽅法中，如何获取类的名称：
getClass().getName()
e.g
class A {
int x=4;int y=1;
public void print(){
    System.out.println("class name:"+getClass().getName());
 }
} 
对⼀个类进⾏分析，⻆度
数据成员的特点
构造函数
继承
多重继承？继承权限？
覆写  向上转型
实例化
接⼝：可以多重继承
try-catch-finally 和 try-with-resource 的使⽤
e.printStackTrace()
e.getMessage
注意多 catch 情况的顺序

## 第9页

String对象的构造和初始化
常量池  堆分配
Thread类的⽅法
start() wait() join() sleep()
关于 Callable
泛型接⼝，允许在调⽤ call ⽅法时返回类型
流的序列化
集合框架 -> 集合接⼝，常⽤集合类
集合接⼝ Collection
常⽤⽅法
增——add(object o) addAll(Collection c)
使⽤ add⽅法时，不需要强制类型转换
删------remove(..) removeAll(...)
遍历 -----iterator接⼝  ⽅法调⽤ ---iterator()
如何遍历：获取迭代器对象，通过 hasNext() 判断，使⽤ next() 元素获取
Iterator it=a.iterator while(it.hasNext){System.out.printLn(it.next())}
排序 -----Comparable 接⼝  ⽅法调⽤ ----sort()
⼦接⼝
List 有序可重复
实现类： ArrayList ， LinkList,Vector---->Stack
Set ⽆序  不重复
实现类： HashSet,TreeSet
Map接⼝
实现类 :HashMap,TreeMap
关于 URL
从URL访问资源

## 第10页

openStream ⽅法
从URLConection 访问资源
openConnection ⽅法  然后调⽤ getOutputStream ⽅法
关于从输⼊流中读数据
⼀⾏⼀⾏读
String inputLine
while((inputLine=in.readLine())!=null){System.out.println(inputLine)}
关于写数据到输出流
out.prinln("...")
out.writer(....)
out.writerDouble(...)
⼀些输出流
字节输出流
OutputStream->BuﬀeredOutputStream->DataOutputStream
println() write() writeInt()
字符输出流
FileWriter->(BuﬀeredWriter)->PrintWriter
⽂件输出流
FileOutputStream ：字节流的形式写⽂件
->DataOutputStream
FileWriter: 以字符流的形式写⽂件
->PrintWriter
过滤输出流
BuﬀeredOutputStream
DataOutputStream-> 字节流
DataOutputStream dos=new DataOutputStream(new
BuﬀeredOutputStream(new FileOutputStream("test.txt")))
与之类似的： PrintWriter() 向字符流写⼊ java 基本数据类型  具有简化和缓冲的
功能  相当于结合了 FileOutputStream 和 FileWriter
对象序列化 -> 字节流
ObjectOutputStream
关于 socket 套接字
ServerSocket
accept()⽅法
Socket

## 第11页

代码设计
使⽤接⼝，在原始图形类的基础上，求三⻆形、正⽅形、圆形的⾯积与周⻓
⾃⼰设计⼀个异常类，发⽣异常时抛出对应语句，结合 try-resource 语句
通过线程的互斥机制与同步通信，实现特定功能
基于 Socket 套接字的通讯
import java.lang.*;
import java.io.*;
import java.net.*;
public class server {
public static void main(String[] args)throws IOException {//throws 声明语句⼀定要写
//创建套接字
ServerSocket ss=null;
try{
ss=new ServerSocket(4700);
}catch(IOException e){
e.printStackTrace();
}
Socket s=null;
try{
s=ss.accept();
}catch (IOException e){
System.out.println("Error:"+e.getMessage());
}
//创建输⼊输出流
DataInputStream in= new DataInputStream(s.getInputStream());

## 第12页

DataOutputStream os=new DataOutputStream(s.getOutputStream());
DataInputStream sin=new DataInputStream(System.in);
//读写输⼊输出流
double side=in.readDouble();
double area=side*side;
writetofile(area);
os.writeDouble(area);
//关闭  标准输⼊流不关
in.close();
os.close();
s.close();
ss.close();
}
private static void writetofile(double area){
try(PrintWriter out=new PrintWriter(new BuﬀeredWriter(new FileWriter("D:/ca/txt"))))
{
out.println(area);
}catch(IOException e){
System.out.println("Error:"+e.getMessage());
}
}
}
import java.lang.*;
import java.io.*;
import java.net.*;
public class client {
public static void main(String[] args)throws IOException{
//创建套接字 , 注意写在外⾯
Socket s=null;
try{
s=new Socket("127.0.0.1",4700);
}catch(IOException e){
System.out.println("Error ： "+e.getMessage());
}
//创建输⼊输出流

## 第13页

DataInputStream sin=new DataInputStream(System.in);
DataInputStream in=new DataInputStream(s.getInputStream());
DataOutputStream os=new DataOutputStream(s.getOutputStream());
//写输⼊输出流
double side=sin.readDouble();
os.writeDouble(side);
double area=in.readDouble();
System.out.println("Area:"+area);
//关闭输⼊输出流
os.close();
in.close();
s.close();
}
}

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
