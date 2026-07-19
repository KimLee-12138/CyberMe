---
id: eda-v | type: concept | status: cleaned | course: EDA
source: ["学生MD笔记+课件"] | source_pages: ["待核对"]
created: 2026-07-17 | updated: 2026-07-17 | verified_by: ""
mastery: unknown | importance: high | confidence: medium
verification: inferred | needs_review: true
review_reason: "AI基于学生笔记深度蒸馏"
tags: [EDA]
---

# Verilog硬件描述语言

## 一句话解释
Verilog HDL是描述数字电路的硬件描述语言。module定义模块，wire连线，reg寄存器。assign=组合逻辑，always@(posedge clk)=时序逻辑。阻塞=用于组合，非阻塞<=用于时序。

## 核心原理


# 1.绪论

1. 什么是自上而下的设计方式？（重点）

> 将数字系统的整体分解为子系统和模块，若子系统较大还可以进一步分解为更小的子系统和模块，层层分解，直至整个系统中各个子系统关系合理，便于逻辑电路的设计和实现

1. 数字系统的实现方式有哪些？各有什么优缺点？

| 实现方式              | 优点                                 | 缺点                           |
| --------------------- | ------------------------------------ | ------------------------------ |
| 通用处理器（CPU）     | 高灵活性、支持复杂逻辑、生态系统成熟 | 串行处理瓶颈、功耗高、实时性差 |
| 微控制器（MCU）       | 集成度高、低功耗、成本低             | 处理能力弱、资源受限           |
| 数字信号处理器（DSP） | 硬件优化（如MAC）、实时性强          | 编程复杂、通用性差             |
| FPGA                  | 并行处理、可重构、灵活性高           | 开发复杂、功耗/成本较高        |
| ASIC                  | 性能极致、功耗极低、量产成本低       | 设计成本高、不可修改           |
| PLD（如CPLD）         | 开发快速、延迟确定                   | 资源有限、扩展性差             |
| SoC                   | 高度集成、能效比高                   | 设计复杂、验证困难             |
| GPU                   | 大规模并行计算、生态成熟             | 功耗极高、延迟较高             |

1. 用硬件描述语言设计数字电路有什么优势？

> 电路逻辑功能容易理解
>
> 可以将逻辑设计与具体电路的实现分为两个独立的阶段来操作
>
> 逻辑设计与实现的工艺无关
>
> 逻辑设计积累的资源可以重复利用，减少了设计时间

1. 基于FPGA/CPLD的数字系统设计流程包含哪些步骤

> ![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZGE0ZDgwMWRlYTNjMjA1MzY0NmNmMjEzYTVmMTE3ZWJfS2tsekswNDY5Zzk4dUtIenNXNkswYzFFaVVDSmVXbXFfVG9rZW46UFdod2J2b0p5bzIwb0x4ZVF2WGM3NU1LbmtnXzE3Nzc5MDEzOTM6MTc3NzkwNDk5M19WNA)

1. 什么是综合？什么是适配

> 综合是将设计者在EDA平台编辑的输入的HDL文件或者原理图的描述，与硬件挂钩，生成底层的便于可编程器件实现的电路网表文件
>
> 适配是将综合后的电路网表文件配置于指定的目标器件中，使之产生最终的下载文件如sof,pof。适配器的任务是完成目标系统在器件上的布线布局

1. 功能仿真和时序仿真的区别？

> 功能仿真：直接对HDL、原理图描述的逻辑设计的逻辑功能进行仿真，和器件无关
>
> 时序仿真：在选择具体器件并完成布线布局后进行包含延时的仿真。

# 10&11.组合逻辑电路&组合逻辑电路设计

题型1：由组合逻辑电路的功能画出电路图

步骤：

1. 分析功能寻找输入输出变量
2. 画真值表
3. 画卡诺图化简
4. 得逻辑表达式（能用公式化简的尽量化简，不能化简的就用与或式表达）
5. 画电路图

可能会考：

1. 8-3编码器
2. 3-8译码器
3. 数据选择器（2选1，四选一）

> 4选1数据选择器的逻辑表达式：
>
> Y=S[D0(A0'A1')+D1(A0'A1)+D2(A0A1')+D3(A0A1)]
>
> S控制是否工作

1. 加法器（全加器与半加器）

> 半加器：
>
> SUM=A⊕B
>
> CO=AB
>
> 全加器：
>
> SUM=A⊕B⊕CIN
>
> CO=AB+ACIN+BCIN

题型2：由组合逻辑电路写出Verilog代码

1. 基本门电路

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZThhNGNiM2M3ZmNjOGYxYzhjMjBiMmJiMGE0NGExMWRfWE44SVdTYmdWQldOUHpyd0k0eWdac0pKSXRNaGJuaVVfVG9rZW46TkdzeWJ2T01zb1BYd3B4UzNHQWM0TXVxbjdkXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

结构描述

```Assembly
module sy(A,B,C,D,F);
input A,B,C,D;
output reg F;
reg F1,F2,F3;
and a1(F2,B,C,D);
nand n1(F1,A,B);
or o1(F,F1,F2);
endmodule
```

数据流描述：

```Assembly
module sy(A,B,C,D,F);
input A,B,C,D;
output wire F;
assign F=(~(A&B))|(B&C&D);
endmodule
```

行为描述：

```Assembly
module sy(A,B,C,D,F);
input A,B,C,D;
output reg F;
always@(A,B,C,D)
begin
F=(~(A&B))|(B&C&D);
end
endmodule
```

1. 四位全加器

```Assembly
//有两个四位的加数a和b，一个一位的进位输入cin；一个四位的输出结果sum，一个一位的进位输出cout
module sy(a,b,cin,sum,cout);
input [3:0]a;
input [3:0]b;
input cin;
output reg [3:0]sun;
output reg cout;
always@(a,b,cin)
begin
{cout,sum}=a+b+cin;
end
endmodule
```

1. 比较器

题目：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=OGFlYWI1N2QxNWIyOTdiOTI5ZDc3ZDY5NDZiNzFmY2NfT0V0WFRmRTZwcnVvb212RG9rV0MyWmVOb3hjSktXNEVfVG9rZW46UUZqVWJlSzBZb1pRWER4RUFIamNEY3ZTbnNYXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

有三种情况：A>B,A=B,A<B

方法一：（不推荐😂复杂）

```Assembly
module sy(A,B,outcome);
input [3:0]A;
input [3:0]B;
output wire [2:0]outcome;//001表示A>B,010表示A=B，100表示A<B
wire [3:0]x;
assign x[0]=(A[0]&B[0])|(~A[0]&~B[0]);
assign x[1]=(A[1]&B[1])|(~A[1]&~B[1]);
assign x[2]=(A[2]&B[2])|(~A[2]&~B[2]);
assign x[3]=(A[3]&B[3])|(~A[3]&~B[3]);

assign outcome[0]=A[3]&~B[3]+x[3]&A[2]&~B[2]+x[3]&x[2]&A[1]&~B[1]+x[3]&x[2]&x[1]&A[0]&~B[0];
assign outcome[1]=x[0]&x[1]&x[2]&x[3];
assign outcome[2]=~A[3]&B[3]+x[3]&~A[2]&B[2]+x[3]&x[2]&~A[1]&B[1]+x[3]&x[2]&x[1]&~A[0]&B[0];

endmodule
```

方法2：

直接用逻辑比较运算符

```Assembly
module sy(A,B,outcome);
input [3:0]A;
input [3:0]B;
output wire [2:0]outcome;//001表示A>B,010表示A=B，100表示A<B
assign outcome[0]=(A>B);
assign outcome[1]=(A==B);
assign outcome[2]=(A<B);
endmodule
```

1. 多路数据选择器

用if-else语句设计四选一的多路选择器

```Assembly
module sy(sel,a,b,c,d,y);
input [1:0]sel;//两位的选择信号
input a,b,c,d;
output reg y;
always@(sel,a,b,c,d);
if(sel==2b'00) y=a;
else if(sel==2b'01) y=b;
else if(sel==2b'10) y=c;
else y=d;
end
endmodule
```

用case语句设计

```Assembly
module sy(sel,a,b,c,d,y);
input [1:0]sel;//两位的选择信号
input a,b,c,d;
output reg y;
always@(sel,a,b,c,d);
case(sel)
2b'00: y=a;
2b'01: y=b;
2b'10: y=c;
default: y=d;
end
endmodule
```

1. 奇偶校验位产生器

```Assembly
module sy(a,even_bit,odd_bit);
input [7:0]a;
output wire even_bit;
output wire odd_bit;
assign even_bit=^a;(当a中有奇数个1时，异或的结果为1）
assign odd_bit=~even_bit;
endmodule
```

1. 其他组合逻辑电路

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YTc2NTk5OGYzZTRiZGJhNzZmN2FjNDY1YjBmMmE4MTdfdHBQQ3FHSFh3QkdiS2FTYW1WMUFEdVRvYmllTGp5bXJfVG9rZW46UU53dmIxcE94b21aemN4SEx3bGN4TFNYbm5lXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

```Assembly
module sy();
input [3:0]addrin;
output wire[7:0]out;
function[7:0] dataout;
input [3:0]addr
case(addr)
0:dataout=0;
1:dataout=1;
2:dataout=4;
3:dataout=9;
……
15：dataout=225；
default：dataout=8'hxx;
endcase
end function
assign out=dataout(addrin);
endmodule
```

1. 一般编码器（case语句）和优先编码器（用if-else if-else实现）

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=OGM0ZmE2N2U5MjQzMWQxMjBjZmI3MjAwMTk0YWZlMTlfb21BeU9CRnpUb1VFOTB6aVlpRklOMHpFYTNlWWRBR3hfVG9rZW46WHFndmI1eDFmbzF0Nmp4U0hXVmNxV3ZTbndiXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

一般编码器：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=YzgzN2M5OTU2MWI4ODZiODc2OGUwYTU5NDdhZTRiYjFfVHRJdFZkRVF0R3g1TzBUUzM0VTdpTVJBZW4wazdvWlpfVG9rZW46STE2S2JFcGxib2RsZm94elJDbmM2SXFEbmhZXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

优先编码器：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MzUzZTYzYWFlZjM3NzkyNTk3YzlmZWI5MDIxZTMwODZfTFRJa2h2RWhxNndZOUZoaUJaQTB4cUd5anVCaHVubVJfVG9rZW46VkljMWJyM1Zzb0FpSWR4WndUaGNTdDRYbnJjXzE3Nzc5MDIwNzI6MTc3NzkwNTY3Ml9WNA)

# 12.存储电路（各类触发器）

核心掌握三张图，其他不要求

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTdmYj
- 课程导航：[[../00_EDA_课程MOC|EDA MOC]]



## 容易出错的地方
- always中混用=和<=导致仿真综合不一致
- assign左值必须是wire
- 组合逻辑条件不完整会意外综合出latch

## 与其他知识点的关系

- 相关：[[数字电路基础]]

## 来源与依据
- 学生MD笔记 + 课件提取版 | `needs_review: true`
