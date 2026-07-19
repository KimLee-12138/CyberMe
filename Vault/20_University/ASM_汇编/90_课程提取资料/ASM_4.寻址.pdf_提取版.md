---
id: extract-asm-df347c64
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/PDF/ASM_4.寻址.pdf_课件_未知日期_df347c64.pdf]]"
source_pages: all
source_hash: "df347c64d08b54a922fa65c25d5b843308f13230e46aa9636cc9092fff7419c3"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 4.寻址.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

寄存器 默认段寄存器 主要用途 典型场景
BX DS 基址寻址（如数组或结构体基址） mov ax, [bx]
SI DS 源变址寻址（字符串 / 数据操作） movsb（源地址）
DI DS 目的变址寻址（字符串 / 数据操作） movsb（目标地址）
BP SS 堆栈帧基址（访问参数 / 局部变量） mov ax, [bp+4]4.寻址  
寄存器间接寻址  
形式类似如下：
Mov ax,[bx] 将 bx 中存放的数据作为一个偏移地址
即（ ax） = （ ds*16+ （ bx ））
bx， si， di ， bp 这些寄存器都可用于寄存器间接寻址
用法和区别：
允许的组合 ：
BX + SI（如  [bx+si]）
BX + DI（如  [bx+di]）
BP + SI（如  [bp+si]）
BP + DI（如  [bp+di]）
禁止的组合 ：
SI + DI（非法）
BX + BP（非法）
仅允许基址（ BX/BP ） + 变址（ SI/DI ）的组合。
loop指令  
例题：计算 FFFF:0 到 FFFF:B 单元中的数据的和结果存储在 DX 中
解决这个问题的时候我们要考虑如下问题：
ffff： 0~ffff ： b 单元中的数据之和会不会超出了 dx 的存储范围
不会。因为一个单元存储一个字节 8 位，在 0~255 之间。而 dx 是 16 位寄存器，最大存储范围是
65535。 255*12<65535
我们能不能将 ffff ： 0~ffff ： b 单元直接累加到 dx 中？
不行！！！！因为每个单元中的数据是 8 位，而 dx 是 16 位寄存器。位数不匹配
能不能将 ffff ： 0~ffff ： b 单元累加到 dl 中，并设置 dh=0 从而实现累加到 dx 中的目标呢
不行，因为 dl 的最大存储范围是 255 ，强行累加会导致进位丢失，造成数据损失
解决办法：

## 第2页

我们将内存地址中的 8 位数据复制到一个 16 位寄存器 AX 中，再将 AX 中的数据加到 DX 上，从而使两个运算
对象的类型匹配，并且结果不会超界
代码：
and和 or 指令  
(1)and指令 : 逻辑与指令 , 按位进行与运算。如 :
mov al,01100011B
and al, 00111011B
执行后 :al=00100011B
通过该指令可将操作对象的相应位设为 0, 其他位不变。 ( 全为 1 即为 1 ，其余全为 0)
(2)or指令 : 逻辑或指令 , 按位进行或运算。如 :
moval,01100011B
or al, 00111011B
执行后 :al=01111011B
通过该指令可将操作对象的相应位设为 1, 其他位不变。 ( 有 1 即为 1 ，其余全为 0)
应用：大小写转换（掌握，可能会考到）
大写变为小写：将第 6 个数字变成 1 ，就变成小写了  所以可以 or 00100000
小写变为大写：将第 6 个数字变成 0 ，就变成大写了  所以可以  and 11011111
寄存器相对寻址  
在前面 ,我们可以用 [bx] 的方式来指明一个内存单元 , 我们还可以用一种更为灵活的方式来指明内存单元 :
[bx+idata] 表示一个内存单元 , 它的偏移地址为 (bx)+idata(bx 中的数值加上 idata) 。
题目  ：
在codesg 中填写代码 , 将 datasg 中定义的第一个字符串 , 转化为大写 , 第二个字符串转化为小写。
assume cs:codesg,ds:datasg
datasg segment
db 'BaSiC'
db 'MinIX'
datasg ends
codesg segment
start: mov ax,ffffh
mov ds,ax;
mov bx,0;//用【bx 】表示偏移地址
mov cx,12
s:
mov al,[bx]
mov ah,0
add dx,ax
inc bx
loop s

## 第3页

......
codesg ends
end start
分析：转换为大写要 and 11011111 ，转换为小写要 or 00100000
同时由数据段的定义可知，每一个字符是一 db 即一个字节
SI和DI  
si和di和 bx 功能相近，用于变址寻址。但是 si 和 di 不能分为两个 8 位寄存器来使用
通常 si用于源变址寻址， di 用于目的变址寻址
例题：
用寄存器 SI 和 DI 实现将字符串
复制到它后 welcome to masm! 面的数据区中。
assume cs:codesg,ds:datasg
datasg segment
db 'welcome to masm!'
db '...............
datasg endsmov ax,datasg
mov ds,ax
mov bx,0
mov cx,5
s:
mov al,[bx]
and al,11011111b// 因为一个字符是一个字节，所以用 al 来暂时存储
mov [bx],al
mov al,[bx+5]//idata=5
or al,00100000b
mov [bx+5],al
inc bx
loop s
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

## 第4页

(相对 )基址变址寻址  
用[bx+si+idata] 和 [bx+di+idata] 的方式
基址变址寻址有四种组合方式：基址 + 变址
bs+si,bx+di,bp+si,bp+di
例题：
编程 ,将 datasg 段中每个单词的头一个字母改为大写字母。
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
end startmov [di],ax
add si,2
add di,2
loop s
mov ax,4c00h
int 21h
codesg ends
end start

## 第5页

assume cs:codesg,ds:datasg
datasg segment
db '1. file          '
db '2. edit          '
db '3. search        '
db '4. view          '
db '5. options       '
db '6. help          '// 每一行都有 16 个字节
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

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
