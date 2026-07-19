---
id: java-io | type: concept | status: cleaned | course: JAVA
source: ["[[91_Raw-Archive/Registry/全量归档记录.json]]"] | source_pages: ["待核对"]
created: 2026-07-17 | updated: 2026-07-17 | verified_by: ""
mastery: unknown | importance: medium | confidence: medium
verification: inferred | needs_review: true
review_reason: "AI深度蒸馏，需人工核对"
tags: [java]
---

# IO流

## 一句话解释
Java IO分字节流(InputStream/OutputStream处理二进制)和字符流(Reader/Writer处理文本)。装饰器模式是核心设计——BufferedReader装饰FileReader增加缓冲。序列化(ObjectOutputStream)将对象转为字节序列，transient字段不参与序列化。

## 核心原理
**IO流分类**：字节流以Stream结尾→FileInputStream/BufferedInputStream/ObjectInputStream；字符流以Reader/Writer结尾→FileReader/BufferedReader/InputStreamReader(字节→字符桥梁)。

**装饰器模式**：`new BufferedReader(new FileReader("f.txt"))`。每个装饰器添加一层功能(缓冲/格式化/压缩)，可以任意组合。

**try-with-resources**(Java 7+)：自动关闭AutoCloseable资源。`try(BufferedReader br=new BufferedReader(...)){...}`——不再需要finally块手动close。

**序列化**：ObjectOutputStream.writeObject(obj)。类必须实现Serializable接口。serialVersionUID用于版本控制(不指定则自动生成，类改变则反序列化失败)。transient字段不序列化(恢复后为默认值)。

**NIO(New IO)**：Channel+Buffer模型，非阻塞IO。Files工具类(Java 7+)简化文件操作：Files.readAllLines()、Files.copy()。

## 容易出错的地方
- 流用完必须关闭→用try-with-resources自动关闭
- 字符流vs字节流：文本用Reader/Writer，二进制(图片/视频)用Stream
- transient字段反序列化后为默认值(int=0, 对象=null)
- 序列化是深拷贝的一种实现方式
- 课程导航：[[../00_java_课程MOC|java MOC]]



## 与其他知识点的关系
- 装饰器模式→设计模式→[[软件设计]]
- Python对比：with open()对应Java的try-with-resources


## 来源与依据
- [[91_Raw-Archive/Registry/全量归档记录.json]] | `needs_review: true`
