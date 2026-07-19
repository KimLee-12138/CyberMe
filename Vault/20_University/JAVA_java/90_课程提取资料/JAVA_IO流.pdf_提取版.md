---
id: extract-java-3fdba04f
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/PDF/JAVA_IO流.pdf_课件_未知日期_3fdba04f.pdf]]"
source_pages: all
source_hash: "3fdba04fa6864ffb369879a1f90b10e027db9b752720b4b8eec370dab305b2a0"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# IO流.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

IO流
流的分类
输⼊流  输出流
输⼊输出是相对程序 / 系统⽽⾔的
标准输⼊输出流
System.in
byte[] buﬀer=new byte[512]
count=System.in.read(buﬀer)
Scanner读取终端输⼊
Scanner scan=new Scanner(System.in)
System.out
区别 println 与 print
⽂件输⼊输出流 (File....)
FileInputStream
FileInputStream(String name)
name为⽂件路径名，是⽂件输⼊流的数据源
FileOutputStream
FileOutputStream(String name)
name为⽂件路径名，是⽂件输出流的接受者
没有该路径，则会新建
字符数组输⼊输出流 (ByteArray....)
将字节数组作为字节流的数据源
byte[]的作⽤
-128到 127 的取值范围，常⽤于处理⼆进制数据
将⼆进制数据转换为 ASCII 存储起来
管道输⼊输出流
字节流  字符流
O->M->O
字节流
InputStream （从流读数据）
⽤法： ....=new InputStream(M)
Read(byte b[],int oﬀ,int len)
从输⼊流读数据，写到 b 中 , 从 oﬀ 开始写，写 len 个

## 第2页

返回值为读取的字节个数
OutputStream （写给流）
write(byte b[],int oﬀ,int len)
从b从 oﬀ位置开始，写 len 个，到流中
字符流
Reader
BuﬀerReader
CharArrayReader
InputStreamReader
FileReader
PipedReader
Writer
PrintWriter
可以向字符流中写⼊ Java 基本数据类型
⼆者的转换 ( 可理解为装配 )
推荐过程：字节流 -> ⾮缓存字符流 -> 缓存字符流（ BuﬀeredReader 、 BuﬀeredWriter ）
InputStreamReader
输⼊字节流转换为字符流 ()
OutputStreamWriter
输出字符流转换为字节流 ( 可以将字符数据写⼊到字节流中了 )
节点流  过滤流
过滤流 -> 流的装配
流的装配，实际上就是给流添加更多的功能
BuﬀerReader
⽤于缓存字符流，可以⼀⾏⼀⾏读
DataInputStream,DataOutputStream
从字节流中写⼊、读取基本数据类型
流与对象 -> 流的序列化
序列化 :将实现了 Serializable 接⼝的对象转换为⼀个字节序列。
作⽤
对象持久化
⽹络传输
实现：
ObjectInputStream
ObjectOutputStream

## 第3页

需要通过类似的装配过程来实现

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
