---
id: extract-asm-3d8ab77a
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/PDF/ASM_附：功能调用.pdf_课件_未知日期_3d8ab77a.pdf]]"
source_pages: all
source_hash: "3d8ab77ae40ccef959fa23fa17792883b8392513d7e46fbc56a9c7c087b15a1a"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 附：功能调用.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

1. 单个字符显示  (AH = 02H)  
当你不需要打印一长串，只想在屏幕上输出一个字符（比如换行符，或者循环打印出来的单个数字）
时，用这个最轻量级。
所需参数：  将要打印的字符的  ASCII 码放入  DL 寄存器。
代码模板：
代码段
(注：汇编中经常用这个功能打印换行，需要连续调用两次：先打印回车符  0DH，再打印换行符  0AH)
2. 键盘输入单个字符并回显  (AH = 01H)  
当你的程序需要暂停，等待用户敲击一下键盘（比如 “ 按任意键继续 ” ，或者输入一个选项  Y/N）时使
用。
所需参数：  无需提前准备参数。
执行结果：  DOS 会挂起程序，等你按键。按完后，这个字符会显示在屏幕上，并且它的  ASCII 码会
被自动存入  AL 寄存器。
代码模板：
代码段
3. 键盘输入一整行字符串  (AH = 0AH)  
这是最复杂、但也最强大的一个功能。相当于  C 语言里的  scanf。它要求你必须提前在内存里建好一个
特定格式的缓冲区（ Buffer ）。
缓冲区格式要求（必须连续分配  3 个部分）：
1. 第 1 个字节：你允许用户输入的最大长度（你定）。
2. 第 2 个字节：用户实际输入的长度（ DOS 帮你填）。
3. 第 3 个字节开始：真正存放用户敲进去的字符的地方。
所需参数：  将这个缓冲区的首地址（偏移地址）放入  DX 寄存器。
代码模板：
代码段mov dl, 'A'    ; 把字符  'A' 放入  DL ( 也可以直接写  41H)
mov ah, 2      ; 准备调用  2 号功能  ( 显示单个字符 )
int 21h        ; 呼叫  DOS 执行
mov ah, 1      ; 准备调用  1 号功能  ( 等待输入 )
int 21h        ; 呼叫  DOS 执行。此时屏幕光标闪烁，等待敲击
               ; 用户按下  'B' 后， AL 寄存器里就会变成  42H ('B' 的 ASCII 码 )
assume cs:code, ds:data

## 第2页

4. 打印字符串  (AH = 09H)  
为了保证完整性，我们把你刚才学的也总结进来。
所需参数：  将字符串的首地址（偏移地址）放入  DX 寄存器。
极易踩坑点：  字符串在内存的末尾 必须以  $ 结束！
代码模板：
代码段data segment
    ; 构建缓冲区 : 允许输入 10 个字符，实际长度预留 0 ，后面留 10 个空位
    buffer db 10, 0, 10 dup(0) 
data ends
code segment
start:
    mov ax, data
    mov ds, ax
    
    mov dx, offset buffer  ; 把缓冲区的首地址给  DX
    mov ah, 0Ah            ; 准备调用  0A 号功能  ( 输入字符串 )
    int 21h                ; 呼叫  DOS 。用户开始打字，按回车结束
    
    mov ax, 4c00h
    int 21h
code ends
end start
mov dx, offset mesg    ; DX 指向字符串开头
mov ah, 9              ; 准备调用  9 号功能
int 21h                ; 执行打印，直到遇到  '$' 停止

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
