---
id: extract-eda-a674b913
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_EDA第七次实验报告.docx_资料_未知日期_a674b913.docx]]"
source_pages: all
source_hash: "a674b913b7ea03e009a029f87bfec5402b2ef95834eadd48f7aecabdc8c17375"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# EDA第七次实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

《ＥＤＡ技术》试验

实验七

复杂系统设计与实现 1

专业：    计算机科学与技术

姓名：    李尚凯

学号：    2024317220214

班级：    计科 2401 班

报告撰写时间：2026 年 5 月 26 日

任务一：32 位超前进位加法器

1. 实验目的

1. 理解超前进位加法器的产生/传播逻辑。

2. 掌握从小位宽模块逐级扩展到 32 位的方法。

3. 练习复杂组合系统的层次化设计与仿真分析。

2. 实验任务及要求

1. 设计 32 位超前进位加法器。

2. 输入为 a[31:0]、b[31:0] 和 ci，输出为 s[31:0] 与 co。

3. 要求能讲清楚分层设计思路。

3. 实验过程

3.1 实验设计思路与实现步骤

超前进位加法器的核心是为每一位产生 g=a&b 和传播 p=a|b，再用组进位模块提前计算高位需要的进位。设计从 1 位 add 开始，组合成 2 位 cla_2、4 位 cla_4，再在顶层中定义 8 位、16 位、32 位结构。这样能减少串行进位带来的延迟。

实现步骤为：先验证 1 位加法单元；编写 g_p 组进位公式；逐级例化构造 2 位和 4 位 CLA；在 sy78.v 中继续构造 8 位、16 位和 32 位；仿真选取普通加法、带进位加法、全 1 溢出等测试样例，检查 s 和 co。

源程序清单：add.v

module add (

    input  a,

    input  b,

    input  c,

    output g,

    output p,

    output s

);

    assign s = a ^ b ^ c;

    assign g = a & b;

    assign p = a | b;

endmodule

源程序清单：g_p.v

module g_p (

    input  [1:0] g,

    input  [1:0] p,

    input        c_in,

    output       g_out,

    output       p_out,

    output       c_out

);

    assign g_out = g[1] | (p[1] & g[0]);

    assign p_out = p[1] & p[0];

    assign c_out = g[0] | (p[0] & c_in);

endmodule

源程序清单：cla_2.v

module cla_2 (

    input  [1:0] a,

    input  [1:0] b,

    input        c_in,

    output       g_out,

    output       p_out,

    output [1:0] s

);

    wire [1:0] g, p;

    wire       c_out;

    add add0 (.a(a[0]), .b(b[0]), .c(c_in),  .g(g[0]), .p(p[0]), .s(s[0]));

    add add1 (.a(a[1]), .b(b[1]), .c(c_out), .g(g[1]), .p(p[1]), .s(s[1]));

    g_p g_p0 (.g(g), .p(p), .c_in(c_in), .g_out(g_out), .p_out(p_out), .c_out(c_out));

endmodule

源程序清单：cla_4.v

module cla_4 (

    input  [3:0] a,

    input  [3:0] b,

    input        c_in,

    output       g_out,

    output       p_out,

    output [3:0] s

);

    wire [1:0] g, p;

    wire       c_out;

    cla_2 cla0 (.a(a[1:0]), .b(b[1:0]), .c_in(c_in),  .g_out(g[0]), .p_out(p[0]), .s(s[1:0]));

    cla_2 cla1 (.a(a[3:2]), .b(b[3:2]), .c_in(c_out), .g_out(g[1]), .p_out(p[1]), .s(s[3:2]));

    g_p g_p0 (.g(g), .p(p), .c_in(c_in), .g_out(g_out), .p_out(p_out), .c_out(c_out));

endmodule

源程序清单：sy78.v

module sy78 (

    input  [31:0] a,

    input  [31:0] b,

    input         ci,

    output [31:0] s,

    output        co

);

    wire g_out, p_out;

    cla_16 cla0 (.a(a[15:0]),  .b(b[15:0]),  .c_in(ci),    .g_out(g_out0), .p_out(p_out0), .s(s[15:0]));

    cla_16 cla1 (.a(a[31:16]), .b(b[31:16]), .c_in(c_out1), .g_out(g_out1), .p_out(p_out1), .s(s[31:16]));

    g_p g_p1 (.g({g_out1, g_out0}), .p({p_out1, p_out0}), .c_in(ci),

              .g_out(g_out), .p_out(p_out), .c_out(c_out1));

    assign co = g_out | (p_out & ci);

endmodule

// 下面是内部用到的 8/16 位模块，直接放在顶层文件最下面即可

module cla_8 (

    input  [7:0] a,

    input  [7:0] b,

    input        c_in,

    output       g_out,

    output       p_out,

    output [7:0] s

);

    wire [1:0] g, p;

    wire       c_out;

    cla_4 cla0 (.a(a[3:0]), .b(b[3:0]), .c_in(c_in), .g_out(g[0]), .p_out(p[0]), .s(s[3:0]));

    cla_4 cla1 (.a(a[7:4]), .b(b[7:4]), .c_in(c_out), .g_out(g[1]), .p_out(p[1]), .s(s[7:4]));

    g_p g_p0 (.g(g), .p(p), .c_in(c_in), .g_out(g_out), .p_out(p_out), .c_out(c_out));

endmodule

module cla_16 (

    input  [15:0] a,

    input  [15:0] b,

    input         c_in,

    output        g_out,

    output        p_out,

    output [15:0] s

);

    wire [1:0] g, p;

    wire       c_out;

    cla_8 cla0 (.a(a[7:0]), .b(b[7:0]), .c_in(c_in), .g_out(g[0]), .p_out(p[0]), .s(s[7:0]));

    cla_8 cla1 (.a(a[15:8]), .b(b[15:8]), .c_in(c_out), .g_out(g[1]), .p_out(p[1]), .s(s[15:8]));

    g_p g_p0 (.g(g), .p(p), .c_in(c_in), .g_out(g_out), .p_out(p_out), .c_out(c_out));

endmodule

图：32 位超前进位加法器仿真结果一

图：32 位超前进位加法器仿真结果二

3.2 实验结果与分析

仿真波形分析：正确结果应满足 {co,s}=a+b+ci。例如 a=0、b=0、ci=1 时 s=1；a=32'hFFFF_FFFF、b=1、ci=0 时 s=0 且 co=1。截图中若不同测试向量的和与数学加法一致，则说明分层进位链正确。若低 16 位正确而高 16 位错误，应重点检查 c_out1 是否正确传入高 16 位；若所有高层进位错误，应检查 g_p 的组产生和组传播公式。

DE2-115 开发板分析：32 位输入输出位数较多，不适合直接完整接到开关和 LED，主要通过仿真验证。若需要硬件调试，可选择低位子集或用 SignalTap 观察内部 g/p/c_out，避免仅凭少量 LED 判断完整 32 位功能。

4. 实验体会与讨论

这个任务让我体会到复杂组合电路必须分层设计。只要每一级模块接口清楚，就能把 1 位加法逐步扩展到 32 位，并且仿真时也能按层定位问题。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
