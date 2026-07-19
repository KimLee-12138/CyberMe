---
id: extract-asm-e1ff791a
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/DOC/ASM_6.转移指令.md_笔记_未知日期_e1ff791a.md]]"
source_pages: all
source_hash: "e1ff791a58394a74dc96c99c793195f150d14fce4152ef62475df762a6e6073c"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 6.转移指令.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 6.转移指令

> 转移指令分类：
>
> 无条件转移（如jmp）
>
> 条件转移指令
>
> 循环指令（loop）
>
> 过程
>
> **中断（重要！）**

## 转移的距离

| **段间远转移** | far ptr，既修改了CS又修改了IP，在段间指令之间跳转       |
| -------------- | ------------------------------------------------------- |
| **段内短转移** | short，同一个CS，IP的变换范围是-128~127（八位）         |
| **段内近转移** | near ptr,同一个CS，IP的变换范围是-32768~32767（十六位） |

### 第一派：段内转移（只修改 IP，不修改 CS）

**情景：** 你现在在 1号楼（`CS` 不变），要去 1号楼的其他房间。

既然不出这栋楼，你根本不需要大声喊“我要去 1号楼 xxx 房间”，你只需要说“往前走 5 个房间”或者“往后退 10 个房间”。

这就是段内转移的核心硬件逻辑：**机器码中保存的不是目标地址，而是“位移量”（Displacement）。**

执行时的计算公式永远是：

$$新 IP = 当前 IP + 位移量$$

*(注：这里的当前 IP 是指 CPU 读取完该跳转指令后，自动加法更新后的 IP 值)*

根据位移量的大小，又细分为两种：

#### 1. 段内短转移 (`short`) —— 节约内存的典范

- **指令格式：** `jmp short 标号`
- **位移量宽度：** 8 位（1 个字节）。
- **寻址范围：** -128 到 127 个字节。
- **底层思考：** 为什么有了 16 位的转移，还要设计 8 位的短转移？因为在实际写代码时，绝大多数的 `if` 分支或 `loop` 循环，代码跨度都很小（只有几十个字节）。如果强行用 16 位来存位移量，会浪费极其宝贵的内存和指令读取时间。**编译器通常会自动将近距离跳转优化为短转移。**

#### 2. 段内近转移 (`near ptr`) —— 本楼宇内的全图通行

- **指令格式：** `jmp near ptr 标号`
- **位移量宽度：** 16 位（2 个字节）。
- **寻址范围：** -32768 到 32767 个字节。
- **底层思考：** 8086 的一个段最大恰好就是 64KB（$2^{16}$ 字节）。用 16 位的有符号数，足以从段内的任何一个角落，向前或向后跳到段内的另一个角落。

------

### 第二派：段间转移（同时修改 CS 和 IP）

**情景：** 你现在在 1号楼的 101 房间，你要去 5号楼的 808 房间。

这时候再说“往前走几个房间”已经没用了，你必须给出**绝对坐标**。

#### 段间远转移 (`far ptr`) —— 绝对空降

- **指令格式：** `jmp far ptr 标号`
- **底层逻辑：** 与段内转移截然不同，远转移的机器码中**包含了明确的目的段地址和偏移地址**。CPU 在执行这条指令时，不会去做加法位移运算，而是**简单粗暴地直接覆盖**：
  - 把指令中携带的新段地址，直接塞进 `CS` 寄存器。
  - 把指令中携带的新偏移地址，直接塞进 `IP` 寄存器。
- **应用场景：** 通常用于调用操作系统底层的系统程序、跨模块调用，或者处理内存中距离极远的庞大代码库。

## jmp指令

- Jmp short/near ptr/far ptr 标号（直接跳转到标号处）

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YzMyNDAwMGJmOTQyMzlmMGI5MGQwMzRmYmM4ZTg0OTRfRlBjSkJnQTY1NGRtOHZGdUQ1SmdyaU02cUR1cVlhVTVfVG9rZW46QUxtVmJhV1hwbzE0Ulh4RVJWdWNQZmsybkhlXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

- Jmp 16位寄存器（这里IP=（16位寄存器），直接跳转到该IP处，即目的地址处）
  - Jmp word ptr 内存单元地址（段内转移）
  - ![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MDJkNDNmYzhjYTEzMDdjMDQwMDRmN2I2M2NjMjVkYWFfZHlXcm9Ba3pqYTZwaFBTRzFTWXdpOHhVbEM1QzdzdEpfVG9rZW46UXgwUmJhNXphb3VMaW14RTJnZ2NXQmRxbkdkXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)
  - ![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NzM4MjFlMzA3Njc3MDUwODhlMzMxY2FlNGRiMDU2MzFfSmtFM2JsaXhhMUs3bWJMYXQxQlpuOExRWURyR21IMzJfVG9rZW46QlVlUGJTcHlxb210UkF4UGdLVmNNTU1nbmxOXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)
  - Jmp dword ptr 内存单元地址（段间转移）
  - ![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NWFhZmFkNmY3OGQyNDJiNmE0ZTY5NmFmNmRjNTUxYmFfOHc1VGRvdm5TS052SmIwVnhKVkNMWmsxYWFvZTBKS0tfVG9rZW46WjF3R2JlOW93b3dRMVZ4MGNRd2NnY0VzbkZkXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

​      场景设定：黑客的传送门

假设你现在正在执行一段代码，当前的地址是 `CS = 1000H`, `IP = 0000H`（你在 1000号大楼，0号房间）。

由于某些原因，你必须立刻跳转到一个极其遥远的隐藏区域去执行另一段机密代码，那个目标地址是：**`CS = 7788H`, `IP = 1122H`**（你要去 7788号大楼的 1122号房间）。

但是，你不能直接在代码里写死这个地址，你必须把这个地址拆解后，藏在数据段（DS）的内存里，然后让 CPU 自己去内存里摸索并跳过去。

### 第一步：把目标地址藏进内存（布置案发现场）

一个内存单元（1个字节）只能装两位十六进制数。我们要藏的地址有 4 个部分（`77`、`88`、`11`、`22`），所以需要 4 个字节的空间。

我们用汇编代码把它存放到 `DS:0` 开始的 4 个格子中。**注意 8086 的硬性规矩（小端法）：低地址放 IP，高地址放 CS。**

代码段

```
; 假设 DS 已经设置好，指向数据段
mov word ptr ds:[0], 1122H   ; 前 2 个字节（低地址），存入目标 IP
mov word ptr ds:[2], 7788H   ; 后 2 个字节（高地址），存入目标 CS
```

执行完这两句后，物理内存 `DS:0` 到 `DS:3` 这 4 个格子里的真实情况是这样的：

- `ds:[0]` 里面装的是：`22H` （1122H 的低 8 位）
- `ds:[1]` 里面装的是：`11H` （1122H 的高 8 位）
- `ds:[2]` 里面装的是：`88H` （7788H 的低 8 位）
- `ds:[3]` 里面装的是：`77H` （7788H 的高 8 位）

这就是一个完整的 `dword`（双字，4个字节）。

### 第二步：触发传送门 (`jmp dword ptr`)

现场布置好了，接下来你只需要写下这极其霸道的一句指令：

代码段

```
jmp dword ptr ds:[0]
```

当 CPU 读到这句指令时，它的内心戏和物理动作是完全按固定程序触发的：

1. **看到 `jmp`**：CPU 知道，“哦，我要准备跑路换地方了。”
2. **看到 `dword ptr`**：CPU 明白，“这次跑路规模很大，我要换大楼（改 CS）还要换房间（改 IP）。我需要去内存里连续读取 **4个字节** 的情报。”
3. **看到 `ds:[0]`**：CPU 得到情报的起点。它立刻跑到数据段 `0` 号地址的储物柜前。
4. **【高潮动作一】拿 IP：** CPU 优先打开前两个柜子 `[0]` 和 `[1]`，拿出里面的拼图 `1122H`，“啪”的一下直接塞进自己的 `IP` 寄存器里！此时 `IP = 1122H`。
5. **【高潮动作二】拿 CS：** CPU 接着打开后面两个柜子 `[2]` 和 `[3]`，拿出拼图 `7788H`，“啪”的一下直接覆盖掉自己的 `CS` 寄存器！此时 `CS = 7788H`。

在这个瞬间，这句指令执行完毕。CPU 猛地一抬头，发现自己的 CS 和 IP 全变了，它已经被瞬间传送到了 **`7788H:1122H`**，并开始乖乖地执行那个新地方的代码。

### 总结与对比：为什么会有 `word ptr` 和 `dword ptr` 的区别？

- 如果你写的是 `jmp word ptr ds:[0]`：CPU 会说：“你只让我读一个字（2个字节）”。它就只拿走前两个柜子的 `1122H` 去改 `IP`。`CS` 原封不动。结果跳到了 `1000H:1122H`（还在原来的大楼）。
- 如果你写的是 `jmp dword ptr ds:[0]`：CPU 会连掏 4 个柜子，把 `IP` 和 `CS` 连锅端掉，彻底实现跨段跳跃。

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NTE2YTM5ZmE0NjU0NTdkOTc1ZWMyNTNiY2YzYTNmNjRfTGYwaFlFelpRekxLdWFIYndMRlZZZWhDQkMxWWNCTmZfVG9rZW46QnJSeGJYc0tYb1Y5a1p4WXAxWGNqb3kxbmltXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

## 条件转移指令

**所有的条件转移指令都是短转移**

无符号数的比较：

| 指令        |                                                              |                                                              |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| JCXZ 标号   | 如果cx=0，跳转到标号处，当cx！=0时，什么也不做，程序向下执行 |                                                              |
| JA/JNBE(>)  | CF=0 AND ZF=0                                                | 通常是和cmp语句搭配使用如mov ax, 100       ; 无符号数 A = 100mov bx, 50        ; 无符号数 B = 50cmp ax, bx        ; 比较 A 和 B（结果：100 > 50）ja  Label1        ; 条件满足，跳转到 Label1; 不执行此处代码Label1:; 执行跳转后的操作 |
| JAE/JNB(>=) | CF=0 OR ZF=1                                                 |                                                              |
| JB/JNAE(<)  | CF=1 AND ZF=0                                                |                                                              |
| JBE/JNA(<=) | CF=1 OR ZF=1                                                 |                                                              |

有符号数的比较：

| 指令    | 转移条件      | 意义（有符号数比较） |
| ------- | ------------- | -------------------- |
| JG/JNLE | ZF=0 且 SF=OF | A > B                |
| JGE/JNL | SF=OF 或 ZF=1 | A >= B               |
| JL/JNGE | SF≠OF 且 ZF=0 | A < B                |
| JLE/JNG | SF≠OF 或 ZF=1 | A <= B               |

## 循环指令（如loop）

**所有循环指令都是短指令**

## 子程序

### ret和retf指令（可实现近转移，短转移，远转移）（return，用于返回源程序）

ret用栈中的数据修改IP的值，实现近转移（读取一个地址通常是占一个字即两个字节，所以SP+2，栈中的数据调用后会弹出

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=Y2ZlZmQxM2M4ODI0YmU0ZDcwYTA3OWI3MTc3ZWQ0ZTlfUDQydTloZmdvaXFpNE5oQ3hjNkFwWXlMd0dNelFzUUFfVG9rZW46TkdTRmJaMGVsb3lTT0l4VjBZQmM0ZmxEbkVmXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

- **一句话总结：** `ret` 在底层完全等价于一句 **`pop IP`**（虽然汇编语法里不允许直接写 pop IP，但物理机制是一模一样的）。

retf用栈中的数据修改IP和CS的值，实现远转移

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=OGY4MTM1ZjAwZTcwYWUzYzY2N2NjYmFkNGIyYTgzNzRfMm1FNWZlOE1GOWg0MHNPT2ZEMlJ2WkFjMFRwQzhlR3VfVG9rZW46R25Pb2JudXdxb0JBYWt4UUM2UGN3anNHbnJjXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

- **一句话总结：** `retf` 在底层完全等价于 **先 `pop IP`，紧接着 `pop CS`**。

### call指令（用于跳转到子程序中）（可实现近转移，远转移）

#### **(1) 压栈保存返回地址**

- **操作**：将当前 `IP` 的值压入栈中，以便子程序执行完毕后能返回到调用点。
  - **步骤**：
    - **栈指针下移**：`SP = SP - 2`（栈向下增长，腾出2字节空间）。
    - **写入返回地址**：将 `IP` 的值存入栈顶位置 `SS:SP`。

#### **(2) 跳转到标号处**

- **操作**：通过 **16位位移** 修改 `IP`，使程序跳转到标号对应的地址。
  - **计算公式**： `IP = IP + 16位位移` （位移是标号地址与当前指令下一条指令地址的差值，由汇编器自动计算）。

其实就是相当于push IP

Jmp near ptr 标号

**expand1：call far ptr 标号 实现的是段间的转移**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=OGM0ODQ2OWI5YzM4MTM3NGE5ODdmNzc3NjEyZDQ3ODRfWGpWVGgzWXBZSUF0bTA5VmlydkJoSDd2V2ZON25iZDdfVG9rZW46S2d4QWJ0Y1FHb2xCT1d4WFJacmNtQmIwblllXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ODY1YTc4N2Q4YmNiMGE0ZjY1MDYwOWYxYWY4ZmJjNWFfTDRwTHVDZjZ5dmFiQldWMndwMkJMVHVnbWU4enZDc05fVG9rZW46UGNpb2JraG5pb1dTMEd4SEdZZ2NXUEM0bmVnXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

执行 `call far ptr 标号`，完全等价于依次执行了下面三条指令：

代码段

```asm
push CS             ; 先留大楼号
push IP             ; 再留房间号
jmp far ptr 标号    ; 跨段传送过去
```

**expand2：call 16位寄存器**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NWJmMjJhZGJmOTk5MjQ4YTAxZGUxZjFiNWFiNTE5N2FfdHVSR0Rkc3VPMVZoOTQwdkM4MEo3WTZJSk4wOE95dWRfVG9rZW46Vkt3T2IzTUZEb2JOaGt4V0NTWWNyUmwzbkllXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NjQzYmE1NmE2NDQ4YTFjOGJhMDk5N2QxMTgzYWFiMzVfTEd1N1NobVZCSWNGT04xcHVKSHd5eVBRU3RXYkx5UDNfVG9rZW46VFZGeWJzU1Fyb3k5Tk14dVl5VmNEcG04bkRkXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MTA5Y2Y0NTg1NjVjYjI2ZjNlYjdjOGEyNTk2ODgwN2ZfQ0JhOGJ4UkVQRzh6TEI2NXdnSjZQNEF1amFBRFJZQzhfVG9rZW46VTcydmJRVk5Qb3NOWWF4b1FBMWNTUHlLbkZmXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YTk0MTgyZWNlNWI2OGZjMGUzYzg2ZTQ3MDkxODNmMGJfcWVmR1VlWmlQQUhjbkg0bVJvSHVJTlBzR2FwVFZHa2JfVG9rZW46RkxDZGJoVW9yb1k5SHp4UEt2eGNydmJOblNiXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWUxZDc0NzJjNjdjODIzMWE0ZTlmODIxOWI4OGVkNTRfM3FETWoxUHREUGtINEpMZ3RZUzdYOEZSRlhLVFNUWVFfVG9rZW46QmRyMWJVelNVbzNkdEZ4ZWxlc2N1QVRDblBkXzE3Nzc4OTk3ODA6MTc3NzkwMzM4MF9WNA)

> 注意一下这里word ptr的使用，word表示字型占16位两个字节，ptr表示pointer。这个通常使用在内存单元地址的前面，在使用内存单元地址的时候，必须要把要取的数据长度（如word，dword，byte）说明清楚，同时要用ptr指向内存单元地址。
>
> 如call word ptr ds：[0]表示将ds：[0]指向的内存单元中的两个字节调用出来作为IP（IP通常都是XXXXh，占两个字节16位），便于call指令push和跳转
>
> 同理，call dword ptr ds：[0]表示将ds：[0]指向的内存单元中的4个字节调用出来作为CS和IP
>
> 又如mov word ptr ds:[0],85 表示向ds;[0]指向的内存单元中写入16位的85
>
> 因此是可以直接向内存单元中写入数值的，但是一定要表明数据类型和ptr

这是非常正常的学习瓶颈！只看寄存器和内存的推演确实会觉得像在“纸上谈兵”。这些底层的汇编指令，其实完美对应了现代高级语言（如 C/C++）里的**函数指针**、**Switch-Case 语句**、以及**操作系统 API 调用**。

为了让你彻底看清它们的实战价值，我们把这四位“大将”代入到真实的编程场景中，并为你配上可以直接运行（在思维中）的完整 8086 汇编代码。

------

### 1. `call 16位寄存器` (如 `call ax`)

**💡 对应现代概念：** 运行时动态计算的**函数指针**。

**🎬 应用场景：动态行为分配。** 假设你在写一个游戏，主角吃到不同的道具会触发不同的效果。效果的内存地址可以在运行时算出来，放到 `AX` 里，然后直接调用。

**💻 汇编代码示例：**

代码段

```
assume cs:code

code segment
start:
    ; 假设根据用户的输入，我们算出了要执行哪个技能
    ; 此时我们将目标子程序的偏移地址存入 AX
    mov ax, offset skill_fire  ; 把“火球术”的地址给 AX

    ; 【出击！】间接调用 AX 里的地址
    call ax                    ; 等价于 push IP, jmp ax

    ; 接下来可能换另一个技能
    mov ax, offset skill_ice
    call ax

    mov ax, 4c00h
    int 21h

; --- 子程序区 (同一个段内) ---
skill_fire:
    ; (释放火球的代码...)
    ret                        ; 近调用，必须用 ret 返回

skill_ice:
    ; (释放冰冻的代码...)
    ret
code ends
end start
```

------

### 2. `call word ptr [内存]`

**💡 对应现代概念：** **Switch-Case 跳转表** 或 **简单对象的方法表**。

**🎬 应用场景：菜单选择系统。** 假设你的程序有个主菜单：按 0 开始游戏，按 1 打开设置，按 2 退出。聪明的程序员不会写一堆 `if-else`，而是会把这些函数的地址放到一个“数组（表格）”里，用户输入几，就去数组的第几个格子里拿地址并执行。

**💻 汇编代码示例：**

代码段

```
assume cs:code, ds:data

data segment
    ; 这是一个“函数地址表”（数组）。每个地址占 2 个字节 (word)
    func_table dw offset do_play      ; 索引 0
               dw offset do_setting   ; 索引 2 (因为一个字占2字节)
               dw offset do_exit      ; 索引 4
data ends

code segment
start:
    mov ax, data
    mov ds, ax

    ; 假设用户按下了 '1'，我们经过计算，将查找偏移量赋给 BX
    ; 用户选选项 1 (设置)，对应的表格偏移量是 2
    mov bx, 2 

    ; 【出击！】去内存表格里查地址并调用
    ; 去 ds:[2] 读取两个字节（do_setting 的地址），并跳过去
    call word ptr ds:[bx]      ; 等价于 push IP, jmp word ptr ds:[bx]

    mov ax, 4c00h
    int 21h

; --- 子程序区 ---
do_play:
    ; (开始游戏...)
    ret
do_setting:
    ; (打开设置...)
    ret
do_exit:
    ; (退出逻辑...)
    ret
code ends
end start
```

------

### 3. `call far ptr 标号`

**💡 对应现代概念：** **静态链接库**跨模块调用。

**🎬 应用场景：大型项目的跨段调用。** 你的程序太大了，一个 64KB 的代码段根本装不下！你必须把核心逻辑写在 `code1` 段，把沉重的数学计算库写在 `code2` 段。此时，你必须显式地告诉 CPU 跨段跳跃。

**💻 汇编代码示例：**

代码段

```
; --- 沉重的数学库段 ---
math_lib segment
calc_sin:
    ; (复杂的正弦计算...)
    retf                       ; 【重点】跨段调用，回来必须用 retf (弹 IP 和 CS)
math_lib ends

; --- 主程序段 ---
main_code segment
assume cs:main_code
start:
    ; 准备好参数
    mov ax, 90 

    ; 【出击！】跨段直接调用。编译器会在机器码里直接写死目标的大楼号和房间号
    call far ptr calc_sin      ; 等价于 push CS, push IP, jmp 目标地址

    mov ax, 4c00h
    int 21h
main_code ends
end start
```

------

### 4. `call dword ptr [内存]`

**💡 对应现代概念：** **操作系统 API (系统调用)**、**C++ 虚函数表 (多态)**、硬件中断。

**🎬 应用场景：调用操作系统的底层服务。** 假设你想调用显卡驱动在屏幕上画个圆。显卡驱动的代码在内存的哪里？你在写程序时根本不可能知道！只有当操作系统启动后，它才会把显卡驱动的 **32位绝对地址（CS:IP）** 登记在内存的一个固定位置（比如 `DS:[100]`）。你只能去那个固定的柜子里摸出地址来执行。

**💻 汇编代码示例：**

代码段

```
assume cs:code, ds:data

data segment
    ; 假设操作系统启动时，在这个位置悄悄填入了显卡画图程序的真实 32位地址
    ; 我们预留 4 个字节的空间 (双字 dword)
    os_draw_api dd 0           ; dd 定义双字，初始为 0
data ends

code segment
start:
    mov ax, data
    mov ds, ax

    ; (模拟操作系统初始化：把真实地址 8000H:0150H 填入内存)
    ; 低位字填 IP，高位字填 CS (小端法)
    mov word ptr ds:[0], 0150H ; 目标 IP
    mov word ptr ds:[2], 8000H ; 目标 CS

    ; ---------------- 你的业务代码开始 ----------------
    
    ; 你想画图，但你不知道画图代码在哪，你只知道地址存在 ds:[0] 处
    ; 【出击！】终极跨段间接调用
    call dword ptr ds:[0]      ; 等价于 push CS, push IP, jmp dword ptr ds:[0]

    ; ---------------- 你的业务代码结束 ----------------
    mov ax, 4c00h
    int 21h
code ends
end start

; (操作系统的画图代码，存放在 8000H:0150H，执行完后会调用 retf 返回你的主程序)
```

**终极总结：**

- **1 和 2 是近战武器：** 在自己的一亩三分地（当前段）里玩耍，灵活多变，用来实现高级语言的控制流。
- **3 和 4 是远程导弹：** 跨越段的物理隔离去调用其他模块。特别是 `call dword ptr`，它是所有现代操作系统提供给用户程序“底层服务接口”的物理鼻祖！

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
