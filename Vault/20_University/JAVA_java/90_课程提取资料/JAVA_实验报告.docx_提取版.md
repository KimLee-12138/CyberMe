---
id: extract-java-566d0c27
type: extract
status: extracted
course: JAVA
source:
  - "[[91_Raw-Archive/DOC/JAVA_实验报告.docx_资料_未知日期_566d0c27.docx]]"
source_pages: all
source_hash: "566d0c27a5365cfd0e8bc8b7bb0da678db0f0f8b3df41c50efa47d667a886e72"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

1.项目概览

本项目旨在利用Java网络编程技术（Socket API）构建一个功能齐全的多人聊天室系统。项目采用C/S（客户端/服务器）架构，基于TCP协议保证数据的可靠传输。系统核心功能主要包括用户注册登录、群聊文本消息广播、文件传输、在线用户列表实时同步及系统通知。

2.通用协议

通信协议是系统的核心。本项目定义了一套基于 Java 对象序列化（Serialization）的通用消息协议，确保服务端与客户端能准确解析数据意图。 

2.1消息实体 (Message.java) 

消息类实现了 Serializable 接口，封装了通信所需的所有元数据： 

Type: 消息指令类型（枚举）。 

Sender/Receiver: 发送者与接收者标识。 

Content: 文本内容或系统提示信息。 

FileData: 字节数组（byte[]），用于承载小文件数据。 

Timestamp: 消息生成时间。  

2.2消息类型定义 (MessageType.java) 

LOGIN: 登录请求（客户端发起连接验证）。 

REGISTER: 注册请求（新用户创建账号）。 

TEXT: 文本消息（用户发送群聊内容）。 

FILE: 文件传输（用户发送文件数据）。 

SYSTEM: 系统通知（服务器推送，如 Server 关闭）。 

USERS: 列表同步（用户上线/下线时广播最新名单）。 

LOGOUT: 退出指令（用户主动断开连接）。

服务器端

服务器采用多线程阻塞 I/O 模型，由以下核心组件构成：

 		ServerApp (入口): 负责初始化数据库/文件存储接口。 启动 ServerSocket 	监听指定端口。 主线程循环调用 accept()，为每个新连接分配独立的 	ClientHandler 线程。 

ClientHandler (工作线程): 生命周期管理：负责处理单一客户端从登录到断开的全过程。 消息分发：解析接收到的 Message 对象，根据 Type 调用相应逻辑（如转发文本、保存文件）。 

ServerState (全局状态): 维护线程安全的在线用户集合（如 ConcurrentHashMap 或同步列表）。 提供 broadcast() 方法，遍历所有活跃连接实现消息群发。

客户端

客户端采用 Swing 构建 GUI，并使用后台守护线程处理网络 I/O，防止界面卡顿。

 		ClientConnection: 封装 Socket 和 Object流，提供 sendMessage() 	和 receiveMessage() 接口。 

UI 层 (LoginFrame & ChatFrame): LoginFrame: 处理用户输入验证，发起 LOGIN/REGISTER 请求。 

ChatFrame: 聊天主界面。启动后台线程循环读取服务器消息，并根据类型更新 UI（追加文本、刷新右侧用户列表、弹窗提示文件下载）。

单文件版本

Main.java 包含服务器、客户端、UI、协议和用户存储等全部内容，是一个无外部依赖的简化教学示例。UserStore 使用文本文件存储用户信息。Server 和 ClientThread 实现用户注册、登录、消息广播、文件发送和退出。

关键交互流程

(1) 连接建立：客户端启动，输入 IP 和端口，Socket 连接握手成功。 

(2) 身份认证： - 客户端发送 LOGIN 包。 - 服务端比对存储数据，返回成功/	失败 Message。 - 若成功，服务端将该用户加入 ServerState，并向所有在线用户广播 USERS 消息刷新列表。 

(3) 消息广播：用户发送 TEXT 消息 -> 服务端接收 -> 遍历在线列表 -> 写入所有客户端输出流。

 (4) 文件传输： - 发送方将文件转为 byte[] 封装进 Message (Type=FILE)。 - 服务端透传该对象。 - 接收方客户端识别类型，自动将 byte[] 写入本地 downloads 目录。 

(5) 会话结束：窗口关闭或点击退出 -> 发送 LOGOUT -> 服务端移除连接 -> 广播更新后的 USERS 列表。

并发与线程模型

服务器主线程负责 accept() 等待客户端连接，每个连接单独分配线程处理。
客户端启动后台守护线程持续监听服务器推送数据。ServerState 通过同步方法避免并发冲突。

错误处理与安全边界

现状：密码明文存储/传输；缺乏 SSL/TLS 加密，易被抓包。 

文件处理：当前一次性加载文件到内存（byte[]），仅适用于 KB/MB 级小文件。传输 GB 级文件会导致 OutOfMemoryError。 

异常处理：虽然捕获了 IO 异常，但部分场景下缺乏断线重连机制。

实验与设计分析

基于 Message 与 MessageType 的协议设计简单清晰，扩展性强。线程模型采用“一连接一线程”，适用于小规模用户；在高并发场景应引入线程池或 NIO。文本存储易上手但缺乏一致性保障；SQLite 结构更规范，但当前仍未进行密码加密。Swing 图形界面清晰分层，基本功能完整。

改进建议

增加服务器端日志与调试输出。用户密码使用加密哈希（如 BCrypt）。
使用线程池或 NIO 提升并发性能。文件传输增加校验、分片与失败重传。
增强协议的错误码与边界处理。保持包结构版为主版本，简化单文件版为演示用途。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_java_课程MOC|java MOC]]
