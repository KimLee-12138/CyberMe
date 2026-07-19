---
id: extract-eda-2b778957
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_EDA第五次实验报告.docx_资料_未知日期_2b778957.docx]]"
source_pages: all
source_hash: "2b77895701b2ffcd97fe802bfacf313af89b539d6b2acddc69f3df202f690d11"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# EDA第五次实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

《ＥＤＡ技术》试验

实验五

层次化电路设计与实现

专业：    计算机科学与技术

姓名：    李尚凯

学号：    2024317220214

班级：    计科 2401 班

报告撰写时间：2026 年 5 月 26 日

任务一：4 位累加器设计、仿真与实现

1. 实验目的

1. 理解累加器由加法器、寄存器、分频器和显示译码器组成。

2. 掌握层次化设计中顶层模块协调多个子模块的方法。

3. 练习用按键输入数据并用七段数码管显示累加结果。

2. 实验任务及要求

1. 设计 4 位累加器。

2. 要求采用层次化电路设计方法。

3. 用按键输入数据，用七段数码管显示结果；结果不正确时可用仿真或 SignalTap 排查。

3. 实验过程

3.1 实验设计思路与实现步骤

当前仓库中 EDA第五次实验/sy1 保存了工程文件、编译报告和输出文件，且 output_files 中存在 .done，说明工程曾经完成编译。但 QSF 中记录的源码路径为外部路径 D:/quartus/abc/add4.v、reg4.v、acc4.v、clk_div.v、seg7.v、sy1.v，这些源码未保存在本仓库中。因此本任务报告只根据老师要求、工程配置和编译结果说明设计过程，不补造源程序。

合理的层次化设计应包括：4 位加法器用于计算当前累加值与新输入的和；4 位寄存器用于保存累加结果；按键或使能信号控制寄存器更新；分频模块把 50MHz 时钟变为人眼可观察的慢节拍；七段译码模块显示累加结果。实现步骤应先分别验证加法器和寄存器，再把它们接入顶层，最后调试显示部分。

3.2 实验结果与分析

仿真波形分析：正确的累加器波形应满足每次有效按键或使能到来时，寄存器输出更新为“旧累加值 + 输入值”；复位后累加值回到 0；若输入保持不变且使能无效，输出保持不变。若波形中结果每个 50MHz 时钟都累加，说明按键使能没有正确同步或去抖；若结果只显示输入值而不累加，说明寄存器反馈没有接回加法器。

DE2-115 开发板分析：上板时按键输入后，七段数码管应显示累加后的结果。若显示跳变很快，可能是按键抖动或时钟未分频；若显示不正确，可用 SignalTap 抓取寄存器当前值、输入值、加法器输出和更新使能，判断错误发生在运算、寄存还是显示环节。

4. 实验体会与讨论

虽然仓库缺少该任务源码，但从工程记录可以看出该任务的重点是层次化连接。累加器调试不能只看最终数码管，应优先验证内部寄存器反馈路径是否正确。

任务二：4 位算术逻辑运算单元 ALU

1. 实验目的

1. 掌握 ALU 多运算选择设计。

2. 理解零标志位 Z 的产生方法。

3. 练习运算模块、显示模块和顶层模块的分层组织。

2. 实验任务及要求

1. 实现加、减、与、或、异或、非、逻辑左移、逻辑右移、算术右移。

2. 输入数据和运算结果用七段数码管显示。

3. 结果为 0 时 Z 标志输出为 1。

3. 实验过程

3.1 实验设计思路与实现步骤

ALU 核心模块 alu4 根据 aluc 选择不同运算。顶层 sy2 把拨动开关分为操作数 A、操作数 B 和运算选择码，ALU 输出结果后送入七段译码器显示，同时把零标志接到 LED。

实现步骤为：先写加减模块 add_sub4；再写 ALU 的 case(aluc) 选择逻辑；写七段译码模块；顶层例化 ALU 和三个显示模块；分配输入开关、显示管脚和零标志 LED；对每个运算选择码分别仿真和上板验证。

源程序清单：add_sub4.v

module add_sub4(

	output [3:0] s,

	output cout,

	input [3:0] a,b,

	input mode

);

	assign {cout,s} = mode?(a-b) : (a+b);

endmodule

源程序清单：alu4.v

module alu4(

    output reg [3:0] c, // 运算结果

    output Z, // 全零标志位，c=0时Z=1

    input [3:0] a, b, // 两个4位输入

    input [3:0] aluc // 运算选择控制信号

);

// 加减用的线

wire [3:0] add_s;

wire add_cout;

add_sub4 u_addsub(add_s, add_cout, a, b, aluc == 1);

always @(*) begin

    case(aluc)

        4'd0: c = a + b; // 0:加法

        4'd1: c = a - b; // 1:减法

        4'd2: c = a & b; // 2:与

        4'd3: c = a | b; // 3:或

        4'd4: c = a ^ b; // 4:异或

        4'd5: c = ~a; // 5:非（只对a）

        4'd6: c = a << 1; // 6:逻辑左移

        4'd7: c = a >> 1; // 7:逻辑右移

        4'd8: c = $signed(a) >>> 1; // 8:算术右移

        default: c = 4'b0000;

    endcase

end

// 全零标志：结果c是0000则Z=1

assign Z = (c == 4'b0000);

endmodule

源程序清单：sy2.v

module sy2(

    input CLOCK_50,

    input [3:0] SWa, // SW0~3：操作数a

    input [3:0] SWb, // SW4~7：操作数b

    input [3:0] SWaluc, // SW8~11：运算选择

    output [6:0] HEX0, // 显示结果c

    output [6:0] HEX4, // 显示a

    output [6:0] HEX5, // 显示b

    output LEDZ // 显示全零标志Z

);

wire [3:0] result;

wire zflag;

// 实例化ALU

alu4 u_alu(

    .c(result),

    .Z(zflag),

    .a(SWa),

    .b(SWb),

    .aluc(SWaluc)

);

seg7 d0(HEX0, result); // 结果

seg7 d4(HEX4, SWa); // 显示a

seg7 d5(HEX5, SWb); // 显示b

assign LEDZ = zflag; // 结果为0时亮灯

endmodule

源程序清单：seg7.v

module seg7(

    output reg [6:0] seg,

    input [3:0] din

);

    always @(*) begin

        case(din)

            4'h0: seg = 7'b1000000;

            4'h1: seg = 7'b1111001;

            4'h2: seg = 7'b0100100;

            4'h3: seg = 7'b0110000;

            4'h4: seg = 7'b0011001;

            4'h5: seg = 7'b0010010;

            4'h6: seg = 7'b0000010;

            4'h7: seg = 7'b1111000;

            4'h8: seg = 7'b0000000;

            4'h9: seg = 7'b0010000;

            4'ha: seg = 7'b0001000;

            4'hb: seg = 7'b0000011;

            4'hc: seg = 7'b1000110;

            4'hd: seg = 7'b0100001;

            4'he: seg = 7'b0000110;

            4'hf: seg = 7'b0001110;

        endcase

    end

endmodule

3.2 实验结果与分析

仿真波形分析：应选取典型输入逐项验证，例如 A=5、B=3 时，加法结果为 8，减法结果为 2，与为 1，或为 7，异或为 6；当结果为 0 时 Z=1。如果某一种运算错误而其他运算正确，应检查 case(aluc) 对应分支；如果所有显示错误但内部 c 正确，应检查 seg7；如果 Z 总是 0，应检查 assign Z = (c == 4'b0000) 是否连接到顶层 LED。

DE2-115 开发板分析：拨动 SWa、SWb 和 SWaluc 时，HEX 应显示操作数和结果，LEDZ 在结果为 0 时点亮。若仿真正确但上板选择码混乱，通常是 SWaluc[3:0] 的管脚高低位顺序与预期不一致。

4. 实验体会与讨论

ALU 是典型的层次化综合任务。通过这个任务我体会到，每增加一种运算都应增加相应测试组合，否则很容易只验证加减法而漏掉移位和取反。

任务三：三层楼道灯组合控制电路

1. 实验目的

1. 理解实际控制问题到逻辑表达式的转换。

2. 掌握三输入异或逻辑。

3. 练习用 LED 表示组合逻辑输出。

2. 实验任务及要求

1. 三层楼每层一个开关，共同控制一盏灯。

2. 任意一个开关动作都能改变灯的亮灭状态。

3. 采用组合逻辑实现。

3. 实验过程

3.1 实验设计思路与实现步骤

楼道灯问题可抽象为奇偶控制：三个开关中有奇数个为 1 时灯亮，有偶数个为 1 时灯灭，因此输出 F=S1 xor S2 xor S3。该表达式正好表示三个开关状态的奇偶性。

实现步骤为：建立 sy3 模块；声明三个输入 S1/S2/S3 和输出 F；用连续赋值写出三输入异或；编译后将三个输入接拨动开关，输出接 LED；上板测试 8 种开关组合。

源程序清单：sy3.v

module sy3(

	output F,

	input S1,

	input S2,

	input S3

);

	assign F = S1^S2^S3;

endmodule

3.2 实验结果与分析

仿真波形分析：8 种输入组合中，001、010、100、111 应输出 1，000、011、101、110 应输出 0。若仿真与该真值表一致，说明组合逻辑正确。若只在 111 时错误，应检查是否错误使用了“至少一个开关亮”的或逻辑；若所有输出反相，则可能把 LED 亮灭极性理解反了。

DE2-115 开发板分析：开发板上拨动任意一个开关，LED 状态都应翻转。若某个开关拨动没有效果，说明该开关输入管脚或位名没有正确分配；若多个开关组合时不符合真值表，应回到代码确认是否确实使用异或而不是或门。

4. 实验体会与讨论

这个任务说明实际生活中的控制问题往往可以转化为真值表和逻辑表达式。先分析事件行为，再写代码，会比直接试写程序更可靠。

任务四：带延时自动关闭的楼道灯

1. 实验目的

1. 掌握组合触发和时序延时相结合的设计。

2. 理解分频后慢时钟在人眼可观察控制中的作用。

3. 练习用计数器实现延时关闭。

2. 实验任务及要求

1. 在楼道灯基础上增加延时自动关闭。

2. 采用 Verilog 代码输入逻辑功能描述。

3. 使用按钮输入，采用时序电路实现延时。

3. 实验过程

3.1 实验设计思路与实现步骤

本任务在组合楼道灯基础上增加“亮灯后延时关闭”。顶层 sy4 先用 clk_div 把 50MHz 时钟降低，light_delay 检测三个按钮异或得到触发信号。触发后灯点亮并清零延时计数器；若没有新触发，计数器递增，达到设定值后灯自动熄灭。

实现步骤为：编写分频器；编写延时控制模块，包含触发信号、灯亮状态和延时计数器；顶层连接 KEY 输入并考虑按键低有效，所以对子按键取反；编译后下载到开发板，按下任意楼层按钮观察 LED 是否亮起并延时熄灭。

源程序清单：clk_div.v

module clk_div(

	output clk_out,

	input clk_in,

	input rst_n

);

	reg [23:0] cnt;

	always @(posedge clk_in or negedge rst_n)

begin

	if(!rst_n)

		cnt <= 0;

	else

		cnt <= cnt+1;

	end

	assign clk_out =cnt[23];

endmodule

源程序清单：light_delay.v

module light_delay(

    input clk, // 4Hz 慢时钟

    input rst_n, // 复位

    input S1, S2, S3, // 三个按钮

    output reg light // 灯输出

);

// 三控组合逻辑：任意按钮触发

wire trigger = S1 ^ S2 ^ S3;

// 延时计数器（4Hz 下数约 4 秒）

reg [3:0] delay_cnt;

// 状态：灯是否亮

reg light_en;

always @(posedge clk or negedge rst_n) begin

    if(!rst_n) begin

        light_en <= 0;

        delay_cnt <= 0;

        light <= 0;

    end

    else begin

        // 按任意键 → 重新亮灯、重新计时

        if(trigger) begin

            light_en <= 1;

            delay_cnt <= 0;

            light <= 1;

        end

        // 灯亮中：延时计数

        else if(light_en) begin

            delay_cnt <= delay_cnt + 1;

            light <= 1;

            // 数到 15 → 时间到，关灯

            if(delay_cnt == 15) begin

                light_en <= 0;

                light <= 0;

            end

        end

        // 灯灭

        else begin

            light <= 0;

        end

    end

end

endmodule

源程序清单：sy4.v

module sy4(

    input CLOCK_50,

    input KEY0, // 复位

    input KEY1, // S1

    input KEY2, // S2

    input KEY3, // S3

    output LEDR0 // 灯

);

wire clk_4hz;

// 分频

clk_div u_clk(

    .clk_in(CLOCK_50),

    .rst_n(KEY0),

    .clk_out(clk_4hz)

);

// 延时灯控制

light_delay u_light(

    .clk(clk_4hz),

    .rst_n(KEY0),

    .S1(~KEY1), // 按键低有效，取反

    .S2(~KEY2),

    .S3(~KEY3),

    .light(LEDR0)

);

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形中，触发信号出现后 light 立即为 1，delay_cnt 从 0 开始递增；在计数达到阈值前 light 保持为 1，到阈值后变为 0。若灯一闪就灭，说明延时计数阈值过小或 light_en 没有保持；若灯一直不灭，说明 delay_cnt==15 条件没有被满足或计数器没有递增。

DE2-115 开发板分析：按下任意 KEY 后 LEDR0 应亮起，等待一段时间后自动熄灭。若按键无效，应检查 KEY 是低有效还是高有效；若灯亮灭不稳定，可能是机械按键抖动导致多次触发，可增加消抖逻辑或在 SignalTap 中观察 trigger。

4. 实验体会与讨论

该任务把组合逻辑扩展为时序控制。仅靠异或表达式无法实现“延时”这种时间行为，必须引入时钟、状态保持和计数器。

任务五：工厂供电控制电路

1. 实验目的

1. 掌握多输入组合控制逻辑。

2. 理解根据请求数量选择不同输出资源的方法。

3. 练习用开关和 LED 显示控制结果。

2. 实验任务及要求

1. 三个车间各需 1KW 电力。

2. 一个车间工作时由 1KW 发电机供电，两个车间工作时由 2KW 发电机供电，三个车间工作时两台同时供电。

3. 用三个开关表示车间请求，用两个 LED 表示发电机输出。

3. 实验过程

3.1 实验设计思路与实现步骤

设 A/B/C 表示三个车间请求，Y1 表示 1KW 发电机，Y2 表示 2KW 发电机。一个或三个请求时 Y1 为 1，因此 Y1=A xor B xor C；两个或三个请求时 Y2 为 1，因此 Y2=AB+AC+BC。

实现步骤为：编写核心模块 power_ctrl；顶层 sy5 把 SW0-SW2 接入 A/B/C，把 LEDR0/LEDR1 接到 Y1/Y2；编译、管脚分配并上板测试所有 8 种输入组合。

源程序清单：power_ctrl.v

module power_ctrl(

    input A, // 车间1

    input B, // 车间2

    input C, // 车间3

    output Y1, // 1KW发电机

    output Y2 // 2KW发电机

);

    // 1KW：奇数个车间工作

    assign Y1 = A ^ B ^ C;

    // 2KW：两个或三个车间工作

    assign Y2 = (A & B) | (A & C) | (B & C);

endmodule

源程序清单：sy5.v

module sy5(

    input SW0, // 车间A

    input SW1, // 车间B

    input SW2, // 车间C

    output LEDR0, // 1KW发电机

    output LEDR1 // 2KW发电机

);

    power_ctrl u1(

        .A(SW0),

        .B(SW1),

        .C(SW2),

        .Y1(LEDR0),

        .Y2(LEDR1)

    );

endmodule

3.2 实验结果与分析

仿真波形分析：输入 001、010、100 时应 Y1=1,Y2=0；输入 011、101、110 时应 Y1=0,Y2=1；输入 111 时应 Y1=1,Y2=1；输入 000 时两者都为 0。若两个请求时两灯都亮，说明 Y1 逻辑可能写成了或门；若三个请求时只有 2KW 亮，说明 Y1 没有使用异或或没有覆盖奇数请求。

DE2-115 开发板分析：拨动三个车间请求开关时，两个 LED 的亮灭应与供电策略一致。若仿真正确但板上结果不一致，应检查 SW0-SW2 与 LEDR0/LEDR1 管脚是否对应，以及 LED 高电平点亮假设是否成立。

4. 实验体会与讨论

供电控制任务让我学会把自然语言需求转化为请求数量和逻辑表达式。先列真值表再化简，可以避免漏掉三个车间同时工作的情况。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
