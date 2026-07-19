---
id: extract-asm-dd10e093
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/DOC/ASM_4.寻址.md_笔记_未知日期_dd10e093.md]]"
source_pages: all
source_hash: "dd10e0937f810bc6eab066c85f0c83487238311ef63d3c24ab1a2781a351bab1"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 4.寻址.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 4.寻址

## **寄存器间接寻址**

形式类似如下：

Mov ax,[bx]将bx中存放的数据作为一个偏移地址

即（ax）=（ds*16+（bx））

**bx，si，di，bp这些寄存器都可用于寄存器间接寻址**

**用法和区别：**

| 寄存器 | 默认段寄存器 | 主要用途                        | 典型场景          |
| ------ | ------------ | ------------------------------- | ----------------- |
| BX     | DS           | 基址寻址（如数组或结构体基址）  | mov ax, [bx]      |
| SI     | DS           | 源变址寻址（字符串/数据操作）   | movsb（源地址）   |
| DI     | DS           | 目的变址寻址（字符串/数据操作） | movsb（目标地址） |
| BP     | SS           | 堆栈帧基址（访问参数/局部变量） | mov ax, [bp+4]    |

- **允许的组合**：
  - **BX + SI**（如 `[bx+si]`）
  - **BX + DI**（如 `[bx+di]`）
  - **BP + SI**（如 `[bp+si]`）
  - **BP + DI**（如 `[bp+di]`）
- **禁止的组合**：
  - **SI + DI**（非法）
  - **BX + BP**（非法）

仅允许基址（BX/BP）+ 变址（SI/DI）的组合。

## loop指令

**例题：**计算FFFF:0到FFFF:B单元中的数据的和结果存储在DX中

解决这个问题的时候我们要考虑如下问题：

- ffff：0~ffff：b单元中的数据之和会不会超出了dx的存储范围
  - 不会。因为一个单元存储一个字节8位，在0~255之间。而dx是16位寄存器，最大存储范围是65535。255*12<65535
- 我们能不能将ffff：0~ffff：b单元直接累加到dx中？
  - 不行！！！！因为每个单元中的数据是8位，而dx是16位寄存器。位数不匹配
- 能不能将ffff：0~ffff：b单元累加到dl中，并设置dh=0从而实现累加到dx中的目标呢
  - 不行，因为dl的最大存储范围是255，强行累加会导致进位丢失，造成数据损失

**解决办法：**

我们将内存地址中的8位数据复制到一个16位寄存器AX中，再将AX中的数据加到DX上，从而使两个运算对象的类型匹配，并且结果不会超界

**代码：**

```asm
mov ax,ffffh
mov ds,ax;
mov bx,0;//用【bx】表示偏移地址
mov cx,12
s:
mov al,[bx]
mov ah,0
add dx,ax
inc bx
loop s
```

## and和or指令

(1)and指令:逻辑与指令,按位进行与运算。如:

mov al,01100011B
and al, 00111011B

执行后:al=00100011B
通过该指令可将操作对象的相应位设为0,其他位不变。(全为1即为1，其余全为0)

(2)or指令:逻辑或指令,按位进行或运算。如:

mov al,01100011B
or al, 00111011B
执行后:al=01111011B
通过该指令可将操作对象的相应位设为1,其他位不变。(有1即为1，其余全为0)

**应用：大小写转换（掌握，可能会考到）**

大写变为小写：将第6个数字变成1，就变成小写了 所以可以**or 00100000**

小写变为大写：将第6个数字变成0，就变成大写了 所以可以 **and 11011111**

## 寄存器相对寻址

在前面,我们可以用[bx]的方式来指明一个内存单元,我们还可以用一种更为灵活的方式来指明内存单元:

[bx+idata]表示一个内存单元,它的偏移地址为(bx)+idata(bx中的数值加上idata)。

**题目 ：**

在codesg中填写代码,将datasg中定义的第一个字符串,转化为大写,第二个字符串转化为小写。
assume cs:codesg,ds:datasg
datasg segment
	db 'BaSiC'
	db 'MinIX'
datasg ends
codesg segment
start: 

​	......
codesg ends
end start

**分析：**转换为大写要and 11011111，转换为小写要or 00100000

同时由数据段的定义可知，每一个字符是一db即一个字节

```asm
mov ax,datasg
mov ds,ax
mov bx,0
mov cx,5

s:
mov al,[bx]
and al,11011111b//因为一个字符是一个字节，所以用al来暂时存储
mov [bx],al
mov al,[bx+5]//idata=5
or al,00100000b
mov [bx+5],al
inc bx
loop s
```

## SI和DI

si和di和bx功能相近，用于变址寻址。但是si和di不能分为两个8位寄存器来使用

通常si用于源变址寻址，di用于目的变址寻址

例题：

用寄存器SI和DI实现将字符串
复制到它后welcome to masm!面的数据区中。
assume cs:codesg,ds:datasg
datasg segment
	db 'welcome to masm!'
	db '...............
datasg ends

```asm
assume ds:datasg,cs:codesg
datasg segment
db 'welcome to masm!'
db '................'
datasg ends

codesg segment
start:
mov ax,datasg
mov ds,ax
mov si,0
mov di,16
mov cx,8

s:
mov ax,[si]//ax是16位两个字节，所以一次复制两个字节
mov [di],ax
add si,2
add di,2
loop s

mov ax,4c00h
int 21h
codesg ends
end start
```

## (相对)基址变址寻址

用[bx+si+idata]和[bx+di+idata]的方式

基址变址寻址有四种组合方式：基址+变址

bs+si,bx+di,bp+si,bp+di

**例题：**

编程,将datasg段中每个单词的头一个字母改为大写字母。
assume cs:codesg,ds:datasg
datasg segment
db '1. file
db '2. edit
db '3. search
db '4. view
db '5. options
db '6. help
datasg ends
codesg segment
start:......
codesg ends
end start

![image-20260502200604470](C:\Users\22067\AppData\Roaming\Typora\typora-user-images\image-20260502200604470.png)

```ASM
assume cs:codesg,ds:datasg
datasg segment
db '1. file          '
db '2. edit          '
db '3. search        '
db '4. view          '
db '5. options       '
db '6. help          '//每一行都有16个字节
datasg ends

codesg segment
start:
mov ax,datasg
mov ds,ax
mov cx,6
mov bx,3

s:
mov al,[bx]
and al,11011111b
mov [bx],al
add bx,16
loop s

mov ax,4c00h
int 21h
codesg ends
end start
```



## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
