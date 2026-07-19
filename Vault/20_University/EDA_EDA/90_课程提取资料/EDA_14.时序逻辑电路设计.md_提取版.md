---
id: extract-eda-a05c8741
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_14.时序逻辑电路设计.md_笔记_未知日期_a05c8741.md]]"
source_pages: all
source_hash: "a05c87418c1a8bb73e352e6e9053d953d89b88b41e847efe49c49edcadc12245"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 14.时序逻辑电路设计.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 14.时序逻辑电路设计

1. ## 触发器（边沿触发，受时钟信号控制）

异步复位的触发器（复位信号不必等待时钟信号到来才能起作用）

```Assembly
always@(posedge clk or negedge reset)
begin
if(~reset)
q=1'b0;
else 
q=data;
end
```

同步复位的触发器（复位信号需要等待时钟信号到来才能起作用）

```Assembly
always@(posedge clk)//注意，这里与异步信号不同
begin
if(~reset)
q=1'b0;
else 
q=data;
end
```

举例：带异步清0和异步置1的JK触发器的Verilog代码

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NWIxN2QzNjI3MzdmMmYwYmY4Zjg0MjM0MTQ2YjczNWRfZGxTb3ducWQ2TW1xUHNaRVZnd2drU21md3pYU2ZFVzJfVG9rZW46TldXZ2JtZzIwb1lPTWd4RGZEM2NZSGRjbmp3XzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
module JK(j,k,rs,set,clk,q);
input j,k,rs,set,clk;
output q;
always@(posedge clk or negedge rs or negedge set)
begin
if(~rs) q=0;
else if(~set) q=1;
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
```

1. ## 锁存器（受电平触发）

8位数据锁存器

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTEyOGY5NWJkYjIzMGFlZTFjYzVkNjI1NWE4MGVmNzZfZmc0dEpHRGp6UXVRREFHams3V21yMlc3ZDhFZ0R4VmhfVG9rZW46UHFwcGJ0Rklrb1ZkQzF4enRsTWNNQmppbjFiXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
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
```

1. ## 寄存器（主要组成部分是触发器）

存储数据并数据输出的功能

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NGQ0ODdjN2FmMDQyODk0ZWNjN2Y2ODIxNGNkZmY3NzVfOUlURnl0WUp4WTdkbW5FbHJZNEhad0pCYUJ6YVp5VmhfVG9rZW46VzRrM2I2UEQwb0JpbmV4d2oyOWNQTFFzbnFPXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

移位功能（实现数据的串行-并行转换和数值运算、数据处理等）

8位带锁存的移位寄存器，串入并出

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjM4ZDc3OGZjNzg4OGYyYjE5M2FjNTU4MmUzOWY1YzhfN20zSUtxVkl1akdUMzg1YVBDS0pteTNucTZza202VlBfVG9rZW46UUZhVWJRNTBab0xsZ3d4eHV4OGNWckZXbmxkXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
module shifter();
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
temp=temp<<1;//左移1位
temp[0]=din;
end
end
endmodule
```

1. ## 存储器（FIFO）（不要求掌握）

数据先进先出，**基本单元是寄存器**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YmFjZGJlZWE5ZWJkZDU3ODA5YmM1MjA2ZmE4ZTQ3YzJfVXNIR3g3ZGZYOWNoOW9OcTEyWFJCeHZ6bW5ORVlEUFhfVG9rZW46SThXcWJMWmY5b0UxZUN4aWpINGNMd1V5bnlkXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=M2E4M2MxMGYxMmQ1ZTFlMTkyMzA0Zjg1YThjMjA1NzlfdEhPMThyR3d3ck5jN2huWE8wYmJIT1BnVnIxM3V2eDFfVG9rZW46VG1VR2I4RXZOb1FWdVB4YzZ0T2NTOEczbmZkXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

1. ## 计数器（重要！！！）

计数器的用途：对**时钟脉冲计数**，**分频**，定时，产生节拍脉冲和脉冲序列、数字运算

### (1)带计数使能端和异步复位端的8位计数器

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGYxNTU4ZjE5ZGI5ZDJmMTZlOTRkZjRkMjU1YzNhODBfdEtueDYxRHdjczJEM2xKSTUyNzZiTEFTd2xVRlRnRVVfVG9rZW46WFNua2J0THNJbzRySlR4RUZRZmM5T3ljbjdkXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
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
```

### (2)带可设定计数输出和异步复位端的8位计数器

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDJkZWY4NzYwNmIzMjA5NmU3ZTQzZTU1MDkwNWU3NTdfNzdsanVXNXFqc3dRbmp6RklWQ1QxNlEwdEx1VFR1eDdfVG9rZW46UktQTGJ3djR2b1A1Tld4NlhqUmNIcGc1bjNmXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
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
```

### (3)带可设定计数输出并带使能端，进位端和异步复位端的8位计数器

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MGZiMWQ0YjdkNjhlMzQ4NmQ2NjBmOGU5NTg5NDNlYzNfN25abXNERTdnMzQ4NFBnQUFkclNBV1JEVVVlYkJGVlBfVG9rZW46WGxMZWJGQ2Jzb1NPd0t4enRwMmNjTXlybjVkXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

```Assembly
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
```

### (4)模200的二进制加法计数器（重要！）

```Assembly
module count200(clk,count);
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
```

### (5)分频器

相当于模N=A/2B的计数器

**设计一个有50MHz时钟分频到1MHz的时钟（必考）**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=NGFjMjkzYjU4NzY3MDUyZDBmNWRmNjJjNTYwM2Q5NGRfNjZKR2dpbVVQQXdtZXlENlFDVjl2Wm1SaHRNbDkzU0ZfVG9rZW46RGdBZWJxdjdLb0FXS2h4YmFremNZNzVZbjVTXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

所以50MHz=50*10^6Hz

则N=25*10^6

```Assembly
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
```

1. ## 练习题

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YzI3NjI1OTE2YmFiZGUzNjI0YmU2NmZiMGM0ODgzZmNfN1FrYnRpZ0pWMDJmVXpHWElIejhWaDNxOEtLam94SnFfVG9rZW46TEgzZGJwWEpsb1NOeWV4eVJ5NWNoZDFFbmdjXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGFiMDNlNDljMWFiNDRhY2VjNTkwYmIxMTllMTRiMzdfaW05U1RHUFJGb0J6N1lTbGNRc3QxWmNkZ0dYaE1yYlFfVG9rZW46WXpIbGJPR2IybzdyVEt4Z1BYYWNZbmxobkhjXzE3Nzc5MDIyMzE6MTc3NzkwNTgzMV9WNA)

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
