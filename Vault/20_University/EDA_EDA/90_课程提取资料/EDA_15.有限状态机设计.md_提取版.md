---
id: extract-eda-f7557352
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_15.有限状态机设计.md_笔记_未知日期_f7557352.md]]"
source_pages: all
source_hash: "f7557352fd56dba23d7c426c90535261ebb20ca873c41bb05cf2a6b2228a0ddd"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 15.有限状态机设计.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 15.有限状态机设计

## 有限状态机的定义

状态机：表示有限个状态以及在这些状态之间的转移和动作等行为的数学模型（**重点是状态和状态的转移**）

有限状态机：时序电路设计中经常采用的一种方式，尤其适用于设计数字系统的控制模块

## 有限状态机的分类

摩尔型：输出只和当前状态有关

米里型：输出不仅仅和当前状态有关

## 状态机案例

### 模5计数器

```Assembly
module count5()；
input clk;时钟信号
input res;复位信号
output reg z;输出z
reg [2:0]cs;存储当前状态current state
reg [2:0]ns;存储下一个状态next state
parameter s0=0,s1=1,s2=2,s3=3,s4=4;模5计时器一共会有五个状态

always@(posedge clk，nesedge res);根据下一个时刻的状态修改当前状态
begin
if(~res)
cs=s0;复位信号起作用时，当前状态变为s0
else 
cs=ns;当上升沿信号来临时，当前状态转变为下一个时刻的状态
end

always@(cs);根据当前状态修改下一个时刻的状态
case(cs)
s0:ns=s1;
s1:ns=s2;
s2:ns=s3;
s3:ns=s4;
s4:ns=s0;
endcase
end

always@(cs);输出
if(cs=s4)
z=1
else 
z=0
end

endmodule
```

1. 状态机中最重要的就是**当前状态cs和后续状态ns**，这里没有使用计数器来计数，而是通过状态的迭代来实现模5的计数器功能 reg [2:0]cs;存储当前状态current state reg [2:0]ns;存储下一个状态next state
2. 可通过‘’parameter s0=0,s1=1,s2=2,s3=3,s4=4;模5计时器一共会有五个状态”来表示状态次序，简化状态表达，最后在输出中将状态换成相应输出即可
3. **有限状态机的Verilog编写通常有三个always语句块组成：**
   1. 第一个：修改当前状态的语句（上升沿来临时，当前状态的值会变为下一个状态的值），cs=ns
   2. 第二个：修改下一个状态的语句（如当前状态为s1时，ns应该为s2），case语句
   3. 第三个：输出语句（对应的状态分配对应的输出）

### “101”序列检测器（必考，图要考代码也要考，一般十几分）

题目：输入为一个时钟信号，一个复位信号，一个1位串行输入x。输出信号为z，当接收到输入序列为101时，z为1，否则z为0

分析：

1. 找出检测时序列一共有多少个可能的状态？ 无效状态（不可能出现的状态）：0 有效状态：“1”，“10”，“101” 所以一共有四种可能的状态
2. 要知道所有可能状态之间变换关系（会画图）

暂时无法在飞书文档外展示此内容

```Assembly
module test(clk,x,rst,z);
input clk;
input x;
input rst;
output reg z;
reg [2:0]cs;
reg [2:0]ns;
parameter s0=0,s1=1,s2=2,s3=3;//一共有四种状态

//设置当前状态变换
always@(posedge clk or posedge rst)
begin
if(rst)
cs=s0;复位
else
cs=ns;
end

//设置后续状态的变换
always@(cs,x)
begin
case(cs)
s0:begin ns= x?s1:s0; end
s1:begin ns= x?s1:s2; end
s2:begin ns= x?s3:s0; end
s3:begin ns= x?s1:s2; end
default: begin ns=s0; end
end

//设置输出
always@(cs)
begin
if(cs==s3)
z=1;
else 
x=0;
end
endmodule
```

### 用状态机设计流水灯

题目：

采用有限状态机设计一个彩灯控制器，要求控制18个LED灯实现如下的演示花型：

从两边往中间逐个亮；全灭；

从中间往两头逐个亮；全灭；

循环执行上述过程

分析：18个灯一对一对的亮起，所以一种有9+9+1=19种状态

```Assembly
module test(clk,rst,led);
input clk;
input rst;
output reg [17:0]led;//18个灯
reg [18:0]cs;
reg [18:0]ns;
parameter s0=0,s1=1,s2=2,……,s18=18;//19个状态,这里s0代表全灭，s18代表全亮

//设置cs变换
always@(posedge clk or posedge rst)
begin
if(rst)
cs=s0;
else
cs=ns;
end

//设置ns的变换
always@（cs）
begin
case(cs)
s0:ns=s1;//从两边向中间亮
s1:ns=s2;
……
s17:ns=s18;
s18:ns=s17;//从中间向两边亮
s17:ns=s16;
……
s1：ns=s0;
endcase
end

//设置输出
always@(cs)
begin
case(cs)
s0:led=18b'000000000000000000;
s1:led=18b'100000000000000001;
……
s18:led=18b'11111111111111111;
default:begin led=18b'000000000000000000; end
end

endmodule
```

# 练习题

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MWQ1MjVkNGQ1NzFkNDc1N2ZlOWEzOWVmMzAzOWU1MmNfZzk3V3ZxV3prTUcxblpXOVc5QllQUTJ1YlkyRU0yMkRfVG9rZW46UTVjdGJpZE8zb2dPUFB4WWNxMmNWdE5LbkFkXzE3Nzc5MDIyNTg6MTc3NzkwNTg1OF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=N2MyZDAxMjdmM2MwNjU0ZDZmNDdlYTYwMTViZThjY2RfdTFwTWYwSVlLRFZtR1V1Z0VnalVtRFU1WEZzQWM5OGpfVG9rZW46UmFpdGI2eEllbzRqU3d4RU1oVmNvMU1CbmdlXzE3Nzc5MDIyNTg6MTc3NzkwNTg1OF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=OTYxY2IxNmIwZjJlMTRkZmNiNmFiNWYxOGEwMGJjZmFfRzZqdGk4dU9tWW90UDdkREpacUV5MUpLN0JEbGFTNDlfVG9rZW46S1JjZWJIVzRabzc4RFZ4NXo0T2NrTzNjbkdNXzE3Nzc5MDIyNTg6MTc3NzkwNTg1OF9WNA)

8.4(这里默认clk信号都是1Hz的）

```Assembly
module traffic(clk,reset,ledA,ledB);
input clk，reset;
output reg [2:0]ledA;//2 1 0对应红黄绿
output reg [2:0]ledB;
reg [5:0]count=0;
parameter s0=0,s1=1,s2=2,s3=3;
always@(posedge clk)
begin
if(count==89)
count=0;
else
count=count+1;
end
//设置cs的变换状态
always@(count)
begin
if(reset)
cs=s0;
else if(count==39||count==44||count==84||count==89)
cs=ns;
else 
cs=cs;
end

//设置ns的值
always@(cs)
begin
case(cs)
s0:ns=s1;
s1:ns=s2;
s2:ns=s3;
s3:ns=s0;
default:ns=s0;
endcase
end

//设置输出逻辑
always@(cs)
begin
case(cs)
s0:begin ledA=3'b100;ledB=3'b001 end
s1:begin ledA=3'b100;ledB=3'b010 end
s2:begin ledA=3'b001;ledB=3'b100 end
s3:begin ledA=3'b010;ledB=3'b100 end
end

endmodule
```

**主要修正点：**

1. **同步设计：状态转换改为时钟驱动（同步时序逻辑），避免组合逻辑竞争。**
2. **计数器逻辑**：优化计数器复位逻辑，提高可读性。
3. **默认输出**：增加`default`分支确保输出稳定。

修正后代码：

```java
module traffic(clk, reset, ledA, ledB);
    input clk, reset;
    output reg [2:0] ledA; // 红黄绿：100-红 010-黄 001-绿
    output reg [2:0] ledB;
    reg [5:0] count;
    reg [1:0] cs, ns;
    parameter s0=0, s1=1, s2=2, s3=3;

    // 计数器逻辑（周期90秒）
    always @(posedge clk or posedge reset) begin
        if (reset) count <= 0;
        else count <= (count == 89) ? 0 : count + 1;
    end

    // 状态寄存器（同步时序）
    always @(posedge clk or posedge reset) begin
        if (reset) cs <= s0;
        else cs <= ns;
    end

    // 下一状态逻辑（组合）
    always @(cs) begin
        case (cs)
            s0: ns = (count == 39) ? s1 : s0; // 40秒后转s1
            s1: ns = (count == 44) ? s2 : s1; // 5秒后转s2
            s2: ns = (count == 84) ? s3 : s2;  // 40秒后转s3
            s3: ns = (count == 89) ? s0 : s3;  // 5秒后循环
            default: ns = s0;
        endcase
    end

    // 输出逻辑（组合）
    always @(*) begin
        case (cs)
            s0: {ledA, ledB} = {3'b100, 3'b001}; // A红，B绿
            s1: {ledA, ledB} = {3'b100, 3'b010}; // A红，B黄
            s2: {ledA, ledB} = {3'b001, 3'b100}; // A绿，B红
            s3: {ledA, ledB} = {3'b010, 3'b100}; // A黄，B红
            default: {ledA, ledB} = {3'b100, 3'b100}; // 安全模式
        endcase
    end
endmodule
```

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
