---
id: extract-eda-55445685
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/PDF/EDA_14.时序逻辑电路设计.pdf_课件_未知日期_55445685.pdf]]"
source_pages: all
source_hash: "554456855c4204c1a6c0e3a1b71b9872ef338a138338761817822465fdea1432"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 14.时序逻辑电路设计.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

14.时序逻辑电路设计  
1. 触发器（边沿触发，受时钟信号控制）  
异步复位的触发器（复位信号不必等待时钟信号到来才能起作用）
同步复位的触发器（复位信号需要等待时钟信号到来才能起作用）
举例：带异步清 0 和异步置 1 的 JK 触发器的 Verilog 代码
always@(posedge clk or negedge reset)
begin
if(~reset)
q=1'b0;
else 
q=data;
end
always@(posedge clk)// 注意，这里与异步信号不同
begin
if(~reset)
q=1'b0;
else 
q=data;
end
module JK(j,k,rs,set,clk,q);
input j,k,rs,set,clk;
output q;
always@(posedge clk or negedge rs or negedge set)
begin
if(~rs) q=0;
else if(~set) q=1;

## 第2页

1. 锁存器（受电平触发）  
8位数据锁存器
else
begin
case({j,k})
2'b00:q=q;
2'b01:q=0;
2'b10:q=1;
2'b11:q=~q;
default:q=1'bx;
endcase
end
end
endmodule
module tt1373();
input le,oe;
input [7:0]dn;
output reg [7:0]qn;
always@(le,oe,dn)
begin
if(oe)
qn=8'bz;
else if(~le)
qn=qn;
else
qn=dn;
end
endmodule

## 第3页

1. 寄存器（主要组成部分是触发器）  
存储数据并数据输出的功能
移位功能（实现数据的串行 - 并行转换和数值运算、数据处理等）
8位带锁存的移位寄存器，串入并出

## 第4页

1. 存储器（ FIFO ）（不要求掌握）  
数据先进先出， 基本单元是寄存器module shifter();
input din,clk,reset,en;
output reg [7:0]dout;
reg [7:0]temp;
always@(posedge clk)
begin
if(reset)
dout=8'b0;
else if(en)
dout=temp
else
begin
temp=temp<<1;//左移1 位
temp[0]=din;
end
end
endmodule

## 第5页

1. 计数器（重要！！！）  
计数器的用途：对 时钟脉冲计数 ，分频，定时，产生节拍脉冲和脉冲序列、数字运算

## 第6页

(1)带计数使能端和异步复位端的 8 位计数器  
module count8(clk,en,reset,out);
input clk,en,reset;
output reg [7:0]out;
always@(posedge clk or posedge reset)
begin
if(reset)
out=8'b0;
else if(en)
out=out+1;
else 
out=out;
end
endmodudle

## 第7页

(2)带可设定计数输出和异步复位端的 8 位计数器  
module count8();
input load,clk,reset;
input [7:0]data;
output reg [7:0]out;
always@(posedge clk or posedge reset);
begin
if(reset)
out=8'b0;
else if(load)
out=data;
else 
out=out+1
end
endmodule

## 第8页

(3)带可设定计数输出并带使能端，进位端和异步复位端的 8 位计数器  
module count8(load,en,clk,reset,data,cout,out);
input load,en,clk,reset;
input [7:0]data;
output reg cout=0;
output reg [7:0] out;
always@(posedge clk or posedge reset)
begin
if(reset)
out=8'b0;
else if(load)
out=data;
else if(en)
begin
out=out+1;
cout=&out
if(cout)
out=8'b0;
end
else 
out=out;
end
endmodule

## 第9页

(4)模 200 的二进制加法计数器（重要！）  
(5)分频器  
相当于模 N=A/2B 的计数器
设计一个有 50MHz 时钟分频到 1MHz 的时钟（必考）
所以 50MHz=50*10^6Hz
则N=25*10^6module count200(clk,count);
input clk;
output reg [7:0]count=0;
always@(posedge clk)
begin
if(count==199)
count=0;
else 
count=count+1;
end
endmodule
module fp();
input clk50m;
output clk1;
reg [25:0]count=0;
always@(posedge clk)
begin
if(count=='d24_999_999)
begin
count=0;
clk1=~clk1;//翻转
end
else 
count=count+1;
end
endmodule

## 第10页

1. 练习题

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
