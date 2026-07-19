---
id: extract-eda-93fedffb
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_EDA第六次实验报告.docx_资料_未知日期_93fedffb.docx]]"
source_pages: all
source_hash: "93fedffb5a787cf40eded14d2ed6000f52ab362cf083ae7d48b038d7c1762678"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# EDA第六次实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

《ＥＤＡ技术》试验

实验六

有限状态机设计与实现

专业：    计算机科学与技术

姓名：    李尚凯

学号：    2024317220214

班级：    计科 2401 班

报告撰写时间：2026 年 5 月 26 日

任务一：1011 序列检测器

1. 实验目的

1. 理解序列检测器的状态定义方法。

2. 掌握用 parameter 编码状态并实现状态转移。

3. 练习可重叠序列检测和开发板慢速采样。

2. 实验任务及要求

1. 检测输入序列中是否出现 1011。

2. 先仿真，再在开发板上加入使能开关和 0.25s 采样时钟。

3. 检测到完整序列时点亮 LEDR0。

3. 实验过程

3.1 实验设计思路与实现步骤

状态定义为：S0 未匹配，S1 已匹配 1，S2 已匹配 10，S3 已匹配 101。当处于 S3 且当前输入为 1 时，说明检测到 1011。开发板版本增加分频器和使能输入，避免开关输入变化太快或状态机在未使能时运行。

stateDiagram-v2

    [*] --> S0

    S0 --> S1: din=1

    S0 --> S0: din=0

    S1 --> S1: din=1

    S1 --> S2: din=0

    S2 --> S3: din=1

    S2 --> S0: din=0

    S3 --> S1: din=1 / led=1

    S3 --> S2: din=0

实现步骤为：先画状态图；编写状态寄存器、下一状态组合逻辑和输出逻辑；仿真输入序列如 1011011，检查是否在每次出现 1011 时输出；再编写 sy12.v，加入 4Hz 分频、使能开关和开发板 LED 输出。

源程序清单：sy1.v

module sy1(

    input         clk,

    input         rst_n,      // 同步复位

    input         din,        // 序列输入

    output reg    led         // 检测到1011输出1

);

// 状态编码

parameter S0 = 4'b0001;

parameter S1 = 4'b0010;

parameter S2 = 4'b0100;

parameter S3 = 4'b1000;

reg [3:0] curr_state;

reg [3:0] next_state;

always @(posedge clk) begin

	if(!rst_n)

		curr_state <= S0;

	else

		curr_state <= next_state;

end

always @(*)begin

	case(curr_state)

		S0:next_state = din ? S1:S0;

		S1:next_state = din ? S1:S2;

		S2:next_state = din ? S3:S0;

		S3:next_state = din ? S1:S2;

		default: next_state = S0;

	endcase

end

always @(*)begin

	led = (curr_state ==S3 && din==1'b1);

end

endmodule

源程序清单：sy12.v

module sy12(

    input         clk_50m,

    input         rst_n,

    input         en,

    input         din,

    output        ledr0

);

reg [22:0] cnt;

reg clk_4hz;

always @(posedge clk_50m or negedge rst_n) begin

    if(!rst_n) begin

        cnt <= 0;

        clk_4hz <= 0;

    end

    else if(cnt == 6249999) begin

        cnt <= 0;

        clk_4hz <= ~clk_4hz;

    end

    else

        cnt <= cnt + 1'd1;

end

parameter S0 = 4'b0001;

parameter S1 = 4'b0010;

parameter S2 = 4'b0100;

parameter S3 = 4'b1000;

reg [3:0] curr_st;

reg [3:0] next_st;

reg led_out;

// 时序逻辑

always @(posedge clk_4hz or negedge rst_n) begin

    if(!rst_n)

        curr_st <= S0;

    else if(en)

        curr_st <= next_st;

end

always @(*) begin

    case(curr_st)

        S0: next_st = din ? S1 : S0;

        S1: next_st = din ? S1 : S2;

        S2: next_st = din ? S3 : S0;

        S3: next_st = din ? S1 : S2;

        default: next_st = S0;

    endcase

end

always @(*) begin

    led_out = (curr_st == S3) && (din == 1'b1);

end

assign ledr0 = led_out;

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形应在输入最后一位补齐 1011 的那个周期输出 led=1。例如输入 1,0,1,1 时，第四位输入为 1 时输出有效。若输出提前一拍，说明输出逻辑与状态更新时序没有区分好；若检测不到重叠序列，应检查 S3 在输入 1 时是否回到 S1 而不是回到 S0。

DE2-115 开发板分析：开发板上打开使能开关后，通过输入开关按 0.25s 节拍输入 1、0、1、1，LEDR0 应在最后一个 1 后点亮。若仿真正确但上板不正确，常见原因是开关输入未同步、采样时钟分频不合适或使能开关没有打开；可用 SignalTap 抓取 curr_st 和 din。

4. 实验体会与讨论

有限状态机设计最重要的是状态含义清楚。先画状态图再写程序，可以避免在代码里迷失，尤其是处理可重叠序列时更明显。

任务二：11010 序列产生器

1. 实验目的

1. 掌握序列产生器状态机设计。

2. 理解 Moore 型输出由当前状态决定。

3. 练习异步复位下的状态循环。

2. 实验任务及要求

1. 周期性输出 11010 序列。

2. 包含高电平有效异步复位 reset。

3. 本题不用上板，仿真即可。

3. 实验过程

3.1 实验设计思路与实现步骤

序列 11010 有 5 位，因此设置 5 个状态 S0 到 S4。状态按固定顺序循环，输出分别为 1、1、0、1、0。复位有效时回到 S0，复位释放后每个时钟输出下一位。

stateDiagram-v2

    [*] --> S0

    S0 --> S1: dout=1

    S1 --> S2: dout=1

    S2 --> S3: dout=0

    S3 --> S4: dout=1

    S4 --> S0: dout=0

实现步骤为：定义 5 个状态参数；编写时序逻辑，在 posedge clk or posedge reset 下更新当前状态；编写下一状态组合逻辑形成循环；编写输出组合逻辑，使每个状态对应一位输出。

源程序清单：sy2.v

module sy2(

    input         clk,

    input         reset,

    output reg    dout

);

// 状态定义（5个状态）

parameter S0 = 3'd0;

parameter S1 = 3'd1;

parameter S2 = 3'd2;

parameter S3 = 3'd3;

parameter S4 = 3'd4;

reg [2:0] curr_state;  // 当前状态

reg [2:0] next_state;  // 下一状态

always @(posedge clk or posedge reset) begin

    if(reset)

        curr_state <= S0;   // 复位 → 回到初始状态 S0

    else

        curr_state <= next_state;

end

always @(*) begin

    case(curr_state)

        S0: next_state = S1;

        S1: next_state = S2;

        S2: next_state = S3;

        S3: next_state = S4;

        S4: next_state = S0;  // 最后一位回到 S0，循环

        default: next_state = S0;

    endcase

end

always @(*) begin

    case(curr_state)

        S0: dout = 1'b1;

        S1: dout = 1'b1;

        S2: dout = 1'b0;

        S3: dout = 1'b1;

        S4: dout = 1'b0;

        default: dout = 1'b0;

    endcase

end

endmodule

3.2 实验结果与分析

仿真波形分析：复位后第一个状态输出为 1，随后每个时钟依次输出 1、0、1、0，再回到 1，形成 11010 周期。若序列变成 10110 或整体错位，说明复位初始状态或输出状态对应关系错了；若复位后不回到第一位，应检查异步复位敏感列表和 if(reset) 分支。

DE2-115 开发板分析：老师要求本题仿真即可，不需要开发板。若要上板观察，应先分频到低速，再把 dout 接 LED，否则 50MHz 下输出序列过快，人眼无法分辨。

4. 实验体会与讨论

序列产生器比序列检测器更简单，因为状态转移不依赖外部输入。但它也提醒我：输出与状态的对应关系必须固定，否则仿真会整体错位。

任务三：8 路彩灯控制器

1. 实验目的

1. 掌握用有限状态机控制 LED 花型。

2. 理解分频后进行人眼可观察显示的必要性。

3. 学会在报告中说明自定义彩灯花型。

2. 实验任务及要求

1. 设计 8 路彩灯控制器。

2. 彩灯花型自定义，并在报告中说明清楚。

3. 只需开发板调试，必要时可仿真。

3. 实验过程

3.1 实验设计思路与实现步骤

本设计定义 8 个状态，LED 花型从全亮逐步向中间收缩，再逐步展开。50MHz 时钟经计数分频得到约 4Hz 慢时钟，状态机在慢时钟下切换花型。

实现步骤为：编写分频计数器；定义 8 个状态参数；状态在慢时钟下依次循环；输出逻辑根据当前状态给出 8 位 LED 花型；编译下载到 DE2-115 并观察 LEDR0-LEDR7。

源程序清单：sy3.v

module sy3(

	input clk_50m,

	input reset,

	output reg[7:0] led

);

reg [22:0] cnt;

reg clk_4hz;

always @(posedge clk_50m or posedge reset) begin

	if(reset) begin

		cnt <= 0;

		clk_4hz <=0;

	end

	else if(cnt == 6249999) begin

		cnt<=0;

		clk_4hz<=~clk_4hz;

	end

	else

		cnt <= cnt + 1'd1;

end

parameter S0 = 3'd0;

parameter S1 = 3'd1;

parameter S2 = 3'd2;

parameter S3 = 3'd3;

parameter S4 = 3'd4;

parameter S5 = 3'd5;

parameter S6 = 3'd6;

parameter S7 = 3'd7;

reg [2:0] curr_state;

reg [2:0] next_state;

always @(posedge clk_4hz or posedge reset) begin

	 if(reset)

        curr_state <= S0;

    else

        curr_state <= next_state;

end

always @(*) begin

    case(curr_state)

        S0: next_state = S1;

        S1: next_state = S2;

        S2: next_state = S3;

        S3: next_state = S4;

        S4: next_state = S5;

        S5: next_state = S6;

        S6: next_state = S7;

        S7: next_state = S0;

        default: next_state = S0;

    endcase

end

always @(*) begin

    case(curr_state)

        S0: led = 8'b11111111;

        S1: led = 8'b11100111;

        S2: led = 8'b11000011;

        S3: led = 8'b10000001;

        S4: led = 8'b00011000;

        S5: led = 8'b00111100;

        S6: led = 8'b01111110;

        S7: led = 8'b11111111;

        default: led = 8'b00000000;

    endcase

end

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形中 curr_state 应按 S0 到 S7 循环，led 应依次输出表中的 8 个花型。若 LED 花型顺序错乱，应检查下一状态逻辑；若花型完全不变，应检查分频时钟是否翻转或复位是否一直有效。

DE2-115 开发板分析：开发板上应看到 8 个 LED 以较慢速度按定义花型变化。若变化太快，说明分频系数过小；若某些 LED 与预期相反，可能是 LED 位序接反，应核对 led[7:0] 与实际 LEDR 管脚顺序。

4. 实验体会与讨论

彩灯控制器让我体会到状态机不仅能处理序列输入，也能用于周期性输出控制。报告中明确写出花型表，有助于判断仿真和上板现象是否正确。

任务四：8 个数码管循环显示 1 到 8

1. 实验目的

1. 掌握用有限状态机控制多个显示器件。

2. 理解单状态点亮单个数码管的扫描显示思想。

3. 练习七段段码与状态输出结合。

2. 实验任务及要求

1. 在 8 个数码管上循环显示 1 到 8。

2. 每个数字显示约 1s。

3. 必须用有限状态机实现。

3. 实验过程

3.1 实验设计思路与实现步骤

本任务使用 8 个状态 S0 到 S7，每个状态只点亮一个数码管并显示对应数字，其他数码管输出全灭段码。状态机由分频后的慢时钟驱动，使每个数字有足够显示时间。

实现步骤为：先分频得到慢时钟；定义 8 个状态；状态按顺序循环；定义数字 1 到 8 的段码和全灭段码；在输出逻辑中先将所有 HEX 置为全灭，再根据当前状态点亮对应 HEX。

源程序清单：sy4.v

module sy4(

    input clk_50m,

    input reset,

    output [6:0] HEX0,

    output [6:0] HEX1,

    output [6:0] HEX2,

    output [6:0] HEX3,

    output [6:0] HEX4,

    output [6:0] HEX5,

    output [6:0] HEX6,

    output [6:0] HEX7

);

reg [22:0] cnt;

reg clk_4hz;

always @(posedge clk_50m or posedge reset) begin

    if(reset) begin

        cnt <= 0;

        clk_4hz <= 0;

    end

    else if(cnt == 6249999) begin

        cnt <= 0;

        clk_4hz <= ~clk_4hz;

    end

    else

        cnt <= cnt + 1'd1;

end

parameter S0=3'd0,S1=3'd1,S2=3'd2,S3=3'd3,S4=3'd4,S5=3'd5,S6=3'd6,S7=3'd7;

reg [2:0] curr_st;

reg [2:0] next_st;

always @(posedge clk_4hz or posedge reset) begin

    if(reset)

        curr_st <= S0;

    else

        curr_st <= next_st;

end

always @(*) begin

    case(curr_st)

        S0:next_st=S1;

        S1:next_st=S2;

        S2:next_st=S3;

        S3:next_st=S4;

        S4:next_st=S5;

        S5:next_st=S6;

        S6:next_st=S7;

        S7:next_st=S0;

        default:next_st=S0;

    endcase

end

parameter NUM1=7'h79,NUM2=7'h24,NUM3=7'h30,NUM4=7'h19,NUM5=7'h12,NUM6=7'h02,NUM7=7'h78,NUM8=7'h00,OFF=7'h7F;

reg [6:0] h0,h1,h2,h3,h4,h5,h6,h7;

always @(*) begin

    h0=OFF;h1=OFF;h2=OFF;h3=OFF;h4=OFF;h5=OFF;h6=OFF;h7=OFF;

    case(curr_st)

        S0:h0=NUM1;

        S1:h1=NUM2;

        S2:h2=NUM3;

        S3:h3=NUM4;

        S4:h4=NUM5;

        S5:h5=NUM6;

        S6:h6=NUM7;

        S7:h7=NUM8;

        default:;

    endcase

end

assign HEX0=h0;

assign HEX1=h1;

assign HEX2=h2;

assign HEX3=h3;

assign HEX4=h4;

assign HEX5=h5;

assign HEX6=h6;

assign HEX7=h7;

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形中 curr_st 每个慢时钟切换一次，且任意时刻只有一个 HEX 输出不是 OFF。例如 S0 时 HEX0 显示 1，S1 时 HEX1 显示 2，直到 S7 时 HEX7 显示 8。若多个数码管同时亮，说明输出逻辑没有先清空所有 HEX；若数字与位置错位，应检查状态和 HEX 的对应关系。

DE2-115 开发板分析：开发板上应看到数字 1 到 8 在 8 个数码管上依次循环出现。若所有数码管都暗，可能是段码全灭值或复位信号错误；若显示太快，应调大分频系数。

4. 实验体会与讨论

这个任务训练了“默认关闭，再按状态打开一个输出”的写法。多输出状态机如果不先给默认值，容易产生锁存或多个输出残留。

任务五：交通灯 30 秒倒计时器（选做）

1. 实验目的

1. 练习倒计时计数器设计。

2. 掌握 BCD 借位和七段显示。

3. 理解交通灯倒计时系统的核心计时模块。

2. 实验任务及要求

1. 实现 30 秒倒计时。

2. 采用两个七段数码管显示倒计时结果。

3. 复位后从 30 开始递减到 00。

3. 实验过程

3.1 实验设计思路与实现步骤

本设计用 1Hz 慢时钟驱动两个 BCD 位。复位后高位为 3、低位为 0；每秒低位减 1；当低位为 0 时借位，高位减 1，低位置 9；到 00 后保持 00。

实现步骤为：对 50MHz 时钟分频得到 1Hz；定义 sec_high 和 sec_low；编写倒计时借位逻辑；编写两个七段译码 case；分配两个 HEX 管脚；上板观察 30 到 00 的变化。

源程序清单：sy5.v

module sy5(

    input clk_50m,

    input reset,

    output [6:0] HEX1,

    output [6:0] HEX0

);

reg [24:0] cnt;

reg clk_1hz;

always @(posedge clk_50m or posedge reset) begin

    if(reset) begin

        cnt <= 0;

        clk_1hz <= 0;

    end

    else if(cnt == 24999999) begin

        cnt <= 0;

        clk_1hz <= ~clk_1hz;

    end

    else

        cnt <= cnt + 1'd1;

end

reg [3:0] sec_high;

reg [3:0] sec_low;

always @(posedge clk_1hz or posedge reset) begin

    if(reset) begin

        sec_high <= 4'd3;

        sec_low <= 4'd0;

    end

    else if({sec_high,sec_low} == 8'd0) begin

        sec_high <= 4'd0;

        sec_low <= 4'd0;

    end

    else if(sec_low == 4'd0) begin

        sec_low <= 4'd9;

        sec_high <= sec_high - 1'd1;

    end

    else begin

        sec_low <= sec_low - 1'd1;

    end

end

reg [6:0] seg1,seg0;

always @(*) begin

    case(sec_high)

        4'd0:seg1=7'h40;

        4'd1:seg1=7'h79;

        4'd2:seg1=7'h24;

        4'd3:seg1=7'h30;

        default:seg1=7'h7F;

    endcase

end

always @(*) begin

    case(sec_low)

        4'd0:seg0=7'h40;

        4'd1:seg0=7'h79;

        4'd2:seg0=7'h24;

        4'd3:seg0=7'h30;

        4'd4:seg0=7'h19;

        4'd5:seg0=7'h12;

        4'd6:seg0=7'h02;

        4'd7:seg0=7'h78;

        4'd8:seg0=7'h00;

        4'd9:seg0=7'h18;

        default:seg0=7'h7F;

    endcase

end

assign HEX1 = seg1;

assign HEX0 = seg0;

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形应从 30 开始，每个 1Hz 周期变为 29、28 ... 01、00，并在 00 保持。若从 30 直接变为 39，说明借位条件写反；若 00 后又变为 99，说明到 0 保持的条件缺失；若计时速度不准确，应检查分频计数阈值是否与 50MHz 对应。

DE2-115 开发板分析：开发板上两个数码管应显示稳定倒计时。若显示乱码，应检查 seg1/seg0 的段码；若倒计时肉眼看起来过快或过慢，应检查 cnt==24999999 的翻转方式是否得到实际 1Hz 更新节拍。

4. 实验体会与讨论

倒计时器的关键是边界处理。和普通加法计数器相比，减法借位更容易出错，所以必须重点仿真 30、29、20、10、00 等关键点。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
