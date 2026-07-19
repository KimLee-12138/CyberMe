---
id: extract-eda-ebff5044
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_EDA第二次实验报告.docx_资料_未知日期_ebff5044.docx]]"
source_pages: all
source_hash: "ebff5044d74a7476cb4734476ac8926feca137f6fa597b261296a096e75b3be5"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# EDA第二次实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

《ＥＤＡ技术》试验

实验二

Quartus II 软件和 DE2-115

开发板使用入门

（二）

专业：    计算机科学与技术

姓名：    李尚凯

学号：    2024317220214

班级：    计科 2401 班

报告撰写时间：2026 年 5 月 26 日

任务一：SW17 控制 LEDR17

1. 实验目的

1. 继续熟悉文本输入设计流程。

2. 练习高位拨动开关和高位 LED 的管脚分配。

3. 巩固编译、下载和硬件观察方法。

2. 实验任务及要求

1. 用 SW17 控制 LEDR17。

2. SW17 为 1 时 LEDR17 点亮，否则熄灭。

3. 需要在 DE2-115 开发板上验证。

3. 实验过程

3.1 实验设计思路与实现步骤

本任务与实验一 SW0 控制 LEDR0 的逻辑相同，但更换了输入输出资源。设计仍采用连续赋值，重点在于正确选择 SW17 和 LEDR17 的管脚。仓库中的 sy25.v 已把输入分配到 Y23，输出分配到 H15。

实现步骤为：新建 sy25 工程；编写 Verilog 文件；完成编译；下载到 DE2-115；拨动 SW17 并观察 LEDR17。由于逻辑只有一条直连线，若出现错误，主要从管脚和下载流程排查。

源程序清单：sy25.v

module sy25(

	(*chip_pin="Y23"*)input in,

	(*chip_pin="H15"*)output out

);

	assign out=in;

endmodule

3.2 实验结果与分析

仿真波形分析：功能仿真时 out 应与 in 同步变化。若 in=0 时 out=1 或 in=1 时 out=0，说明赋值方向或端口极性理解有误，应检查代码是否被写成取反。如果波形中 out 为高阻或未知值，应检查输出是否声明正确、文件是否设为顶层。

DE2-115 开发板分析：SW17 拨到 1 时 LEDR17 点亮，拨到 0 时熄灭，说明代码、管脚和下载均正确。若仿真正确但 LED 不亮，应重点检查 LEDR17 的管脚是否和开发板手册一致，或者工程顶层是否仍然指向旧模块。

4. 实验体会与讨论

这个任务看似重复，但训练的是避免管脚分配错误。后续复杂实验中输入输出更多，只有先养成检查 QSF 和开发板手册的习惯，才能减少硬件调试时间。

任务二：SignalTap 正弦信号发生器观察

1. 实验目的

1. 学习嵌入式逻辑分析仪 SignalTap 的使用。

2. 理解查找表方式产生离散正弦数据。

3. 掌握在开发板上抓取内部信号的方法。

2. 实验任务及要求

1. 以正弦信号发生器为例建立工程。

2. 用 SignalTap 观察 cnt、dout、clk_6m 等信号。

3. 分析抓取数据是否呈周期性正弦变化。

3. 实验过程

3.1 实验设计思路与实现步骤

该任务的核心不是把信号显示到 LED，而是在 FPGA 内部产生周期性数据，再用 SignalTap 抓取。sy261.v 先用 count8 对 50MHz 时钟进行节拍划分，产生较慢的 clk_6m 采样信号；在 clk_6m 上升沿，计数器 cnt 递增；case(cnt) 输出 0 到 255 范围内的查找表数据 dout，这些数据近似一个正弦周期。

实现步骤为：建立工程并编译；打开 SignalTap，添加 cnt、dout、clk_6m、clr 等节点；设置采样时钟和触发条件；下载到开发板后运行采样；观察数据是否从中值逐渐上升到最大、再下降到最小、最后回到中值。

源程序清单：sy261.v

module sy261 ( clock , clr , dout , clk_6m);

 (*chip_pin="AB28"*)input clr;

 (*chip_pin="Y2"*)input clock;

 output reg clk_6m;

 output reg [7:0] dout ;

 reg [6:0] cnt ;

 reg [2:0]count8;

 always @( posedge clock )

     begin if (count8==7)

          begin count8<=0; clk_6m<=1; end

          else begin count8<=count8+1; clk_6m<=0; end end

 always @( posedge clk_6m or negedge clr )

 begin

 if (! clr ) cnt <=0; else cnt <= cnt +1;

 case ( cnt )

0: dout <=127;1:dout<=134;2: dout <=140;3: dout <=146;4: dout <=152;

5: dout <=159;6: dout <=165;7: dout <=171;8: dout <=176;9: dout <=182;

10:dout<=188;11:dout<=193;12:dout<=199;13: dout <=204;14: dout <=209;

15:dout<=213;16:dout<=218;17: dout <=222;18: dout <=226;19: dout <=230;

20: dout <=234;21: dout <=237;22: dout <=240;23: dout <=243;24: dout <=246;

25: dout <=248;26:dout<=250;27:dout<=252;28: dout <=253;29: dout <=254;

30: dout <=255;31:dout<=255;32: dout <=255;33: dout <=255;34: dout <=255;

35: dout <=254;36: dout <=253;37: dout <=252;38: dout <=250;39: dout <=248;

40: dout <=246;41: dout <=243;42: dout <=240;43: dout <=237;44:dout<=234;

45: dout <=230;46: dout <=226;47: dout <=222;48: dout <=218;49: dout <=213;

50: dout <=209;51:dout<=204;52: dout <=199;53: dout <=193;54: dout <=188;

55:dout<=182;56:dout<=176;57:dout<=171;58: dout <=165;59: dout <=159;

60:dout<=152;61:dout<=146;62: dout <=140;63: dout <=134;64: dout <=128;

65: dout <=121;66: dout <=115;67: dout <=109;68:dout<=103;69:dout<=96;

70:dout<=90;71: dout <=84;72: dout <=79;73: dout <=73;74: dout <=67;

75: dout <=62;76:dout<=56;77: dout <=51;78: dout <=46;79: dout <=42;

80: dout <=37;81: dout <=33;82: dout <=29;83: dout <=25;84: dout <=21;

85: dout <=18;86:dout<=15;87: dout <=12;88: dout <=9;89: dout <=7;

90: dout <=5;91: dout <=3;92: dout <=2;93: dout <=1;94: dout <=0;

95:dout<=0;96:dout<=0;97: dout <=0;98: dout <=0;99: dout <=1;

100: dout <=2;101: dout <=3;102: dout <=5;103: dout <=7;104: dout <=9;

105:dout<=12;106:dout<=15;107:dout<=18;108: dout <=21;109: dout <=25;

110:dout<=29;111:dout<=33;112:dout<=37;113: dout <=42;114: dout <=46;

115:dout<=51;116:dout<=56;117:dout<=62;118:dout<=67;119: dout <=73;

120:dout<=79;121: dout <=84;122: dout <=90;123: dout <=96;124:dout<=103;

125: dout <=109;126: dout <=115;127: dout <=121;

endcase end   endmodule

图：SignalTap 正弦信号观察结果

3.2 实验结果与分析

仿真波形分析：若用仿真观察，clk_6m 应按 count8 的计数周期产生脉冲，cnt 只在 clk_6m 有效边沿递增，dout 应按查找表顺序变化。截图中如果 dout 呈现先增后减的周期性规律，就说明查找表和计数逻辑正确。如果 dout 卡在某个数值，常见原因是复位 clr 一直有效或 clk_6m 没有翻转；如果波形跳变顺序错乱，应检查 case(cnt) 是否覆盖完整地址，或者 cnt 位宽是否足够。

DE2-115 开发板分析：SignalTap 抓取到的内部数据若与仿真规律一致，说明硬件中时钟、复位和查找表逻辑都正常。若仿真正确而 SignalTap 数据不动，应检查采样时钟选择是否正确、节点是否被优化、工程是否启用了 SignalTap 文件。

4. 实验体会与讨论

SignalTap 让我看到 LED 无法直接反映的内部状态。以后遇到开发板现象不明显的问题，可以优先抓取关键寄存器和状态信号，而不是盲目改代码。

任务三：PLL 实现 50MHz 到 5MHz 分频

1. 实验目的

1. 巩固 PLL IP 核的生成和调用。

2. 理解输入时钟周期与输出分频关系。

3. 练习用仿真或 SignalTap 验证时钟频率。

2. 实验任务及要求

1. 使用 altpll 宏功能模块实现 50MHz 到 5MHz 分频。

2. 输入时钟周期按 20ns 设置。

3. 完成波形仿真，并可用 SignalTap 分析。

3. 实验过程

3.1 实验设计思路与实现步骤

本任务使用 Pll IP 核完成十分频。输入时钟 inclk0 来自 DE2-115 的 50MHz 时钟，周期为 20ns；输出 c0 目标频率为 5MHz，周期为 200ns。工程中 areset 分配到 AB28，输入时钟分配到 Y2。

实现步骤为：打开 PLL 配置向导；设置输入时钟为 50MHz；配置输出 c0 为 5MHz；生成 Pll.v 等文件；建立仿真波形，给 inclk0 20ns 周期时钟，并让 areset 释放；观察 c0 周期是否约为输入的 10 倍，locked 是否稳定有效。

module Pll (

    areset,

    inclk0,

    c0,

    locked

);

图：PLL 50MHz 到 5MHz 仿真结果

图：PLL 分频 SignalTap 或工程结果

3.2 实验结果与分析

仿真波形分析：正确波形应满足 inclk0 每 20ns 翻转一个完整输入周期，c0 的完整周期约为 200ns，即输出频率为 5MHz。locked 在复位释放后经过锁定时间变为有效。如果 c0 没有输出，应检查 areset 是否保持有效；如果输出周期不是 200ns，应回到 PLL 参数界面检查分频/倍频设置；如果 locked 抖动，可能是输入时钟不连续或复位信号设置不合理。

DE2-115 开发板分析：上板时可用 SignalTap 抓取 c0 与 locked。若仿真正确而板上不正确，应检查输入时钟管脚 Y2 是否分配到 inclk0，复位按键是否释放，以及下载的 SOF 是否为包含 PLL 的工程。

4. 实验体会与讨论

通过本任务，我进一步理解了时钟 IP 的使用边界。时钟分频虽然也能用计数器实现，但 PLL 能提供更准确、更适合 FPGA 时钟网络的输出。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
