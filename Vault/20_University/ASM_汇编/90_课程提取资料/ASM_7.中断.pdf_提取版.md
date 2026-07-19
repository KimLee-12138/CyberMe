---
id: extract-asm-3db4b5e3
type: extract
status: extracted
course: ASM
source:
  - "[[91_Raw-Archive/PDF/ASM_7.中断.pdf_课件_未知日期_3db4b5e3.pdf]]"
source_pages: all
source_hash: "3db4b5e3fb7493bca671542c748d735435a35cb1142d31c5f70bd8be921fc506"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 7.中断.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

7.中断  
概念  
中断的分类：
中断向量表：在 内存中保存，其中存放着 256个中断源所对应的中断处理程序入口（ 0000:00000000:03FF
的1024个单元，其中 0000:02000000:02FF 这 256 个字节空间对应的中断向量表的表项是空的）
0~255
中断过程： CPU 硬件自动用中断类型码找到中断向量， 并用它设置 CS 和 IP
iret指令： iret 指令用于从中断程序返回到源程序，相当于 pop IP ， pop CS ， popf

## 第2页

1. 例题 1：  
分析题目：
由题意知，当发生除法溢出时，跳到 0 号中断处理程序中（这里将这个中断程序命名为 do0 ）；然后 do0
中断程序中要进行相关操作，在显示屏上显示 “overflow” ；接着返回源程序
那我们现在要做的是
1.编写好 do0 中断程序
2.然后将其放在内存（ 0000:0200~0000:03FF 这段中断向量表为空的位置）当中（可以利用 movsb 指
令，将 do0 代码传送到 0000:0200 处）（安装程序）
3.然后将这段内存的入口地址放在中断向量表 0 号表项中，方便 CPU 调入，执行程序
assume cs:codesg,ds:datasg
datasg segment
db "overflow!"
datasg ends
codesg segment
start:
;安装do0 程序
mov ax,0000h
mov es,ax
mov ax,0200h
mov di,ax;用es：di 指向目的地址
mov ax,cs

## 第3页

mov ds,ax
mov si,offset do0;用ds：si 指向源地址
mov cx,offset do0end-offset do0;用cx设置传输长度
cld;设置传输方向为正
rep movsb
;设置中断向量表 0 号表项（对应的内存地址为 0000:0000 ）中存放的值为 do0 的 CS 和 IP
mov ax,0
mov es,ax
mov word ptr es:[0],0200h
mov word ptr es:[0*4+2],0000h;注意这个顺序：先设置 IP 后设置 CS （由内存的结构决定，低位在上高
位在下）这里为什么要 *4 ？是因为每一号向量处都存放着一对 CS 和 IP 的值，一共占 4 个字节
int 0h
;编写do0 中断程序：
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

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_汇编_课程MOC|汇编 MOC]]
