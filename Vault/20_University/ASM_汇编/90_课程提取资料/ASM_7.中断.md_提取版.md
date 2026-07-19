---
id: extract-asm-2c5bcd20
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/DOC/ASM_7.中断.md_笔记_未知日期_2c5bcd20.md]]"
source_pages: all
source_hash: "2c5bcd205f87e55b9001eff23cf4c441622c1a903d67cc9b3f96f80f95689132"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 7.中断.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 7.中断

## 概念

中断的分类：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NDE0Yjk1OTVjNzE0OWRlMmMzMjY4MWExYzRkNjI3MjVfbWFHSDhSbUx2dldkMnJFVUwyR1ZNSkpFZkFScllYMHdfVG9rZW46TktUNmI2Y1Nnb1FnRGZ4R3RvN2NSekNqbmplXzE3Nzc4OTk4NTQ6MTc3NzkwMzQ1NF9WNA)

中断向量表：在**内存**中保存，其中存放着**256**个中断源所对应的中断处理程序入口（0000:0000-0000:03FF的1024个单元，其中0000:0200~0000:02FF这256个字节空间对应的中断向量表的表项是空的）

0~255

中断过程：CPU硬件自动用中断类型码找到中断向量，**并用它设置CS和IP**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWZiNjM1M2MyM2U4ODAyODE3NTkxNjU3MjI5MDY5ZTdfQzVFTlFiblAzN1lyOU03N2N4MXhnOHVUdTNCTE9ndm9fVG9rZW46UnBwcGI3b2RQb240eWJ4NWNkOWNtUlRybnllXzE3Nzc4OTk4NTQ6MTc3NzkwMzQ1NF9WNA)

iret指令：iret指令用于从中断程序返回到源程序，相当于pop IP，pop CS，popf

学习“中断”机制是汇编语言中一个非常重要的分水岭，它标志着你从“顺着代码往下走”的线性思维，跨越到了“响应突发事件”的系统级思维。这个概念一开始听起来有点抽象，这是完全正常的。

我们先抛开复杂的代码，用最通俗的语言，把你 PPT 里的“概念部分”拆解清楚。

你可以把 CPU 想象成一个正在专心看书的人，而“中断”就是突然发生的、必须立刻去处理的突发事件（比如电话响了、或者书上发现个错别字）。

------

### 一、 什么是中断？它有哪些分类？

引起中断的事件，在专业术语里叫做“中断源” 。根据这个事件是从 CPU 内部发出的还是外部硬件发出的，中断被分成了两大类：  

- **内中断（软中断）：** 这是 CPU 自己内部产生的事件 。  
  - 比如你主动使用了 `INT` 指令 。  
  - 比如 CPU 算账算错了，出现了除法错误或者溢出（CPU 错） 。  
  - 再比如为了方便调试程序而专门设置的中断 。  
- **外中断（硬中断）：** 这是 CPU 外面的硬件设备发出的求救信号 。  
  - **可屏蔽中断：** 比如键盘、鼠标等外设发出的 I/O 请求 。CPU 如果此时很忙，可以暂时屏蔽（不理会）它们。  
  - **非屏蔽中断：** 发生了极其致命的硬件故障，比如电源突然掉电、或者内存出现奇偶校验错 。这种中断 CPU 是无法装作没看见的，必须立刻响应。  

### 二、 中断向量表：CPU 的“应急通讯录”

当突发事件（中断）发生时，CPU 怎么知道该去执行哪一段代码来解决问题呢？这就需要一本“通讯录”——也就是**中断向量表**。

- **它的位置与大小：** 这张表固定保存在内存的最底部，地址范围是从 `0000:0000` 到 `0000:03FF`，总共占据 1024 个字节 。  
- **它里面存了什么：** 里面保存着多达 256 个中断源（编号从 0 到 255）对应的**中断处理程序入口地址** 。每个入口地址包含两个部分：段地址（CS）和偏移地址（IP）。  
- **一个关键的“空位”：** 在这 1024 个字节中，从 `0000:0200` 到 `0000:02FF` 这 256 个字节对应的空间是空的 。**（这是一个非常重要的伏笔，以后我们要把自己写的中断程序偷偷塞进内存，借用的就是这段没人管的安全区。）**  

### 三、 8086 CPU 的中断全过程（核心机制）

当一个中断发生时，CPU 硬件会自动执行一套像机器一样死板但极其严密的 6 步动作。这个过程的核心目的就是：**找到通讯录里的新地址，并把现在的旧地址好好保存起来，方便以后回来** 。  

这 6 个步骤是 CPU 自动完成的，不需要你写代码控制：

1. **拿号码牌：** 从中断信息中取得中断类型码（比如 0 号中断、21H 号中断等） 。  
2. **保护现场（一）：** 将**标志寄存器**的值压入栈中保存（因为处理中断程序可能会改变各种标志位，所以得先存底） 。  
3. **关闭打扰：** 设置标志寄存器的第 8 位 TF 和第 9 位 IF 的值为 0（为了防止在处理当前中断时，又被别的突发事件打断） 。  
4. **保护现场（二）：** 把当前的 CS（代码段寄存器）内容入栈 。  
5. **保护现场（三）：** 把当前的 IP（指令指针寄存器）内容入栈 。  
6. **跳转新地址：** 根据第 1 步拿到的类型码，去中断向量表里查地址。从内存地址为 `中断类型码 * 4` 的地方读取字单元去设置 IP，从 `中断类型码 * 4 + 2` 的地方读取字单元去设置 CS 。  

完成这 6 步后，CPU 就已经跳到了专门处理这个中断的代码去执行了。

### 四、 iret 指令：顺利回老家

当中断处理程序执行完毕，总得回到当初被打断的地方继续工作。这时候就需要用到 **`iret` 指令**。

它的作用就是从中断程序返回到源程序，它的底层逻辑其实极其简单粗暴，就相当于逆向执行了刚才的保护现场操作：连续执行 `pop IP`、`pop CS`、`popf`（弹出标志寄存器） 。这样，一切都恢复了原样，就像什么都没发生过一样。  

## 例题1：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YWIzODczOTA3NTdiYTM1YmM3MWU4NWM2OTQ4ZmVjNzNfMFN6NXBic3VBd1ZIeENzU3Z4TUc3ZVc0Tko1NEE4dmlfVG9rZW46QVFFeWJ4QzFHb1B0Vmx4ZlZnOGM2OHFVblRjXzE3Nzc4OTk4NTQ6MTc3NzkwMzQ1NF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YjM4NzUwZTYxNzhlYzJjMjUyNWIzMTA1Y2EyNDI1NTNfRGk5SWFWWGMydVJubWFsVmVQWHRYV29lYUY3OGZEMmJfVG9rZW46U2d2T2JHbm1sb1RETDV4Vms3VmNadnVhbkdoXzE3Nzc4OTk4NTQ6MTc3NzkwMzQ1NF9WNA)

分析题目：

由题意知，当发生除法溢出时，跳到0号中断处理程序中（这里将这个中断程序命名为do0）；然后do0中断程序中要进行相关操作，在显示屏上显示“overflow”；接着返回源程序

那我们现在要做的是

1.编写好do0中断程序

2.然后将其放在内存（0000:0200~0000:02FF这段中断向量表为空的位置）当中（可以利用movsb指令，将do0代码传送到0000:0200处）（安装程序）

3.然后将这段内存的入口地址放在中断向量表0号表项中，方便CPU调入，执行程序

```Assembly
assume cs:codesg,ds:datasg
datasg segment
db "overflow!"
datasg ends

codesg segment
start:
;安装do0程序
mov ax,0000h
mov es,ax
mov ax,0200h
mov di,ax;用es：di指向目的地址
mov ax,cs
mov ds,ax
mov si,offset do0;用ds：si指向源地址
mov cx,offset do0end - offset do0;用cx设置传输长度
cld;设置传输方向为正
rep movsb

;设置中断向量表0号表项（对应的内存地址为0000:0000）中存放的值为do0的CS和IP
mov ax,0
mov es,ax
mov word ptr es:[0],0200h
mov word ptr es:[0*4+2],0000h;注意这个顺序：先设置IP后设置CS（由内存的结构决定，低位在上高位在下）这里为什么要*4？是因为每一号向量处都存放着一对CS和IP的值，一共占4个字节

int 0h
;编写do0中断程序：
do0:
mov ax,datasg
mov ds,ax
mov si,0
mov di,0
mov ax,0B800h
mov es,ax
mov cx,9
s:
mov al,[si]
mov es:[1990+di],al
mov byte ptr es:[1990+di+1],00000111b;设置属性为黑底白字
add di,2
inc si
loop s
iret;跳出中断返回主程序
do0end:nop

mov ax,4c00h
int 21h
codesg ends
end start
```

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
