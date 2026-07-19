---
id: extract-asm-65af810b
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/PDF/ASM_2.寄存器.pdf_课件_未知日期_65af810b.pdf]]"
source_pages: all
source_hash: "65af810bee49941c0f452d46e354513eadaf74ca18b3f4806fd1f2d0ce25faf8"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 2.寄存器.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

2.寄存器  
CPU概述：  
CPU由运算器、控制器、寄存器等器件组成
8086CPU 有 14 个寄存器：（均为 16 位，可存放两个字节）
AX、 BX、 CX 、 DX 、 SI 、 DI 、 SP 、 BP 、 IP 、 CS 、 SS 、 DS 、 ES 、 PSW
通用寄存器  
AX， BX， CX ， DX
8086CPU 的物理地址转换方式  
8086有 20 位地址，总线可传送 20 位地址，寻址能力为 1M
8086内部为 16 位结构，它只能传送 16 位的地址，表现出的寻址能力却只有 64K
解决办法：采用一种在内部将两个 16 位地址合成的方法形成一个 20 位的物理地址
物理地址 = 段地址 *16（二进制数 *16相当于左移 4 位，变成 16 进制的话相当于左移 1 位） + 偏移地址
注意：
1. 段地址 ×16 必然是 16 的倍数，所以一个段的起始地址也一定是 16 的倍数
2. 偏移地址为 16 位， 16 位地址的寻址能力为 64K ，所以一个段的长度最大为 64K
段寄存器  
CS， DS， SS ， ES （提供段地址）
CS是提供代码段段地址
DS提供数据段段地址
SS提供堆栈段段地址
CS和 IP  
CS： IP指向 CPU 当前要读取指令的地址
CPU执行指令的过程（考）
1. 从CS:IP指向内存单元读取指令，读取的指令进入指令缓冲区
2. IP=IP+所读取指令的长度，从而指向下一条指令（ IP 的改变是发生在 “ 读取指令之后，执行指令之
前”的！这意味着，当指令真正在执行的时候， IP 已经指向了 下一条指令 的地址。）
3. 执行指令，转到步骤 1 ，重复这个过程
如何修改 CS 和 IP 实现指令的跳转？
不能通过 mov 指令来修改 CS 和 IP ！！！！只能用转移指令来修改
同时修改 CS 、 IP 的内容 :
jmp段地址 : 偏移地址
jmp 2AE3:3
jmp 3:0B16

## 第2页

功能 :用指令中给出的段地址修改
CS,偏移地址修改 IP 。
仅修改 IP 的内容 :
jmp某一合法寄存器
jmp ax (类似于 mov IP,ax ）
jmp bx
功能 :用寄存器中的值修改 IP 。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
