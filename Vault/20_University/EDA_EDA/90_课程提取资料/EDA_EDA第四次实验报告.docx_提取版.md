---
id: extract-eda-b5652569
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_EDA第四次实验报告.docx_资料_未知日期_b5652569.docx]]"
source_pages: all
source_hash: "b565256954c300c28081e4e32684ccaec3207198ae8cc5f82c505b3e06533ad0"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# EDA第四次实验报告.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

《ＥＤＡ技术》试验

实验四

时序逻辑电路设计

专业：    计算机科学与技术

姓名：    李尚凯

学号：    2024317220214

班级：    计科 2401 班

报告撰写时间：2026 年 5 月 26 日

任务一：模 200 计数器两种实现

1. 实验目的

1. 掌握时序计数器的行为描述方法。

2. 理解 IP 核计数器的例化和复位信号适配。

3. 比较手写逻辑和 IP 核实现同一功能的差异。

2. 实验任务及要求

1. 设计模 200 二进制加法计数器。

2. 用 Verilog 行为描述和 IP 核两种方式实现。

3. 仿真时要观察计数最大值 199 以及回零过程。

3. 实验过程

3.1 实验设计思路与实现步骤

行为描述版本使用一个 8 位寄存器 out，在时钟上升沿递增，低电平复位时清零，计数到 199 后回到 0。IP 版本使用 counter_mod200a，顶层 ip_counter_mod200 将低有效复位 rst_n 取反后接到 IP 的高有效清零端 aclr。

实现步骤为：先编写并仿真 counter_mod200.v；再用 Quartus IP 生成计数器核；写顶层调用 IP；分别建立波形文件，输入时钟和复位；拖动仿真波形滚动条到 199 附近，确认计数器是否从 199 回到 0。

源程序清单：counter_mod200.v

module counter_mod200(

	input clk,

	input rst_n,

	output reg[7:0] out

);

always @(posedge clk or negedge rst_n)

begin

	if(!rst_n)

		out <= 8'd0;

	else if(out==8'd199)

		out <= 8'd0;

	else

		out <= out +1'd1;

end

endmodule

源程序清单：ip_counter_mod200.v

module ip_counter_mod200(

    input clk,

    input rst_n, // 低电平异步复位

    output [7:0] q, // 计数输出 0~199

    output cout // 进位输出，数到199时为1

);

counter_mod200a u_counter(

    .clock(clk),

    .aclr(~rst_n), // IP核的aclr是高电平有效，所以取反

    .q(q),

    .cout(cout)

);

endmodule

图：模 200 计数器仿真结果一

图：模 200 计数器仿真结果二

图：IP 计数器仿真结果

图：计数到 199 后回零结果

3.2 实验结果与分析

仿真波形分析：正确结果是复位释放后 out/q 从 0 开始逐拍加 1，达到十进制 199 后下一拍回到 0。截图若显示 199 后立即回零，则模值正确。若计数到 200 才回零，说明判断条件写成了 out==200 或复位/加一顺序不对；若计数一直不动，应检查复位是否一直有效或时钟是否没有加入波形。

DE2-115 开发板分析：本任务主要要求仿真。若上板，可把计数值低位接 LED 或接数码管显示，但 50MHz 时钟下人眼无法观察，需要先分频。若板上显示跳变过快，不代表计数错误，而是缺少可观察的慢时钟。

4. 实验体会与讨论

计数器设计最容易出错的是边界值。通过专门观察 199 附近波形，我学会了不能只看前几个周期，还要检查回零边界是否满足模值要求。

任务二：10 分频器设计与仿真

1. 实验目的

1. 掌握偶数分频器设计方法。

2. 理解计数翻转输出实现 50MHz 到 5MHz 的关系。

3. 练习分析时钟周期和占空比。

2. 实验任务及要求

1. 对 50MHz 输入时钟进行 10 分频。

2. 输出 5MHz 时钟。

3. 仿真时在 Node Finder 中选择全部管脚和寄存器，观察计数器与输出时钟。

3. 实验过程

3.1 实验设计思路与实现步骤

10 分频的设计思路是用 0 到 9 的循环计数器控制输出翻转。计数到 4 时输出翻转一次，计数到 9 时输出再翻转一次并清零，这样输出的高低电平各持续 5 个输入周期，完整输出周期为 10 个输入周期。

实现步骤为：编写 fenping10.v；复位时清零计数器并让输出为 0；时钟上升沿根据 cnt 的值决定加一、翻转或回零；建立波形文件输入 50MHz 时钟；观察 clk_out 的周期是否为输入的 10 倍。

源程序清单：fenping10.v

module fenping10(

    input clk, // 50MHz输入

    input rst_n, // 低电平复位

    output reg clk_out // 5MHz输出

);

reg [3:0] cnt; // 计数器 0~9

always @(posedge clk or negedge rst_n) begin

    if(!rst_n) begin

        cnt <= 4'd0;

        clk_out <= 1'b0;

    end

    else if(cnt == 4'd4) begin // 计数到4翻转

        cnt <= cnt + 1'b1;

        clk_out <= ~clk_out;

    end

    else if(cnt == 4'd9) begin // 计数到9归0

        cnt <= 4'd0;

        clk_out <= ~clk_out;

    end

    else begin

        cnt <= cnt + 1'b1;

    end

end

endmodule

图：10 分频仿真结果

3.2 实验结果与分析

仿真波形分析：正确波形中，cnt 应从 0 计到 9，再回到 0；clk_out 在 cnt=4 和 cnt=9 附近翻转，因此输出周期等于 10 个输入周期，占空比约为 50%。若输出频率不是 5MHz，应检查翻转点是否写错；若占空比明显不对，应检查高电平和低电平持续的输入周期数是否相等。

DE2-115 开发板分析：若把 5MHz 时钟直接接 LED，人眼仍无法观察明显闪烁，因此上板分析应借助示波器或 SignalTap。若后续电路使用该分频时钟，需注意它是由逻辑寄存器产生的普通信号，不应随意作为全局高质量时钟使用。

4. 实验体会与讨论

分频器让我更清楚地理解了“翻转一次不是一个完整周期”。完整周期包含一次上升和一次下降，所以 10 分频需要两个翻转点配合。

任务三：0-F 闪烁七段显示控制

1. 实验目的

1. 掌握慢时钟分频和周期显示控制。

2. 练习七段数码管显示 0 到 F。

3. 理解闪烁效果与显示使能的关系。

2. 实验任务及要求

1. 在一个共阳极七段数码管上循环显示 0 到 F。

2. 显示应带闪烁功能。

3. 使用分频后的慢时钟，避免人眼无法观察。

3. 实验过程

3.1 实验设计思路与实现步骤

设计分为三部分：第一部分将 50MHz 时钟分频为约 1Hz；第二部分用 4 位计数器 num 在 0 到 15 循环；第三部分根据 num 输出七段段码，并利用慢时钟低电平阶段输出全灭段码，实现闪烁。

实现步骤为：编写分频计数器 cnt_div；在 clk_1hz 上升沿更新 num；编写 0-F 的段码 case；当 clk_1hz==0 时输出 1111111 全灭；编译、仿真并下载观察。

源程序清单：seg_scan_flash.v

module seg_scan_flash(

    input clk_50m,

    input rst_n,

    output [6:0] seg

);

reg [25:0] cnt_div;

reg clk_1hz;

always @(posedge clk_50m or negedge rst_n)

begin

    if(!rst_n) begin

        cnt_div <= 26'd0;

        clk_1hz <= 1'b0;

    end

    else if(cnt_div == 26'd24999999) begin

        cnt_div <= 26'd0;

        clk_1hz <= ~clk_1hz;

    end

    else begin

        cnt_div <= cnt_div + 1'd1;

    end

end

reg [3:0] num;

always @(posedge clk_1hz or negedge rst_n)

begin

    if(!rst_n)

        num <= 4'd0;

    else if(num == 4'd15)

        num <= 4'd0;

    else

        num <= num + 1'd1;

end

reg [6:0] seg_r;

always @(*) begin

    if(clk_1hz == 1'b0) begin

        seg_r = 7'b1111111;

    end

    else begin

        case(num)

            4'd0: seg_r = 7'b1000000;

            4'd1: seg_r = 7'b1111001;

            4'd2: seg_r = 7'b0100100;

            4'd3: seg_r = 7'b0110000;

            4'd4: seg_r = 7'b0011001;

            4'd5: seg_r = 7'b0010010;

            4'd6: seg_r = 7'b0000010;

            4'd7: seg_r = 7'b1111000;

            4'd8: seg_r = 7'b0000000;

            4'd9: seg_r = 7'b0010000;

            4'd10: seg_r = 7'b0001000;

            4'd11: seg_r = 7'b0000011;

            4'd12: seg_r = 7'b1000110;

            4'd13: seg_r = 7'b0100001;

            4'd14: seg_r = 7'b0000110;

            4'd15: seg_r = 7'b0001110;

            default: seg_r = 7'b1111111;

        endcase

    end

end

assign seg = seg_r;

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形中，num 应按 0、1、2 ... F 循环变化；seg 在慢时钟高电平时显示当前数字段码，在慢时钟低电平时全灭。因此如果只看某一个周期，可能会看到显示和全灭交替，这是闪烁功能而不是错误。若数码管不闪烁，应检查全灭分支是否存在；若数字顺序错误，应检查 num 的递增和回零条件。

DE2-115 开发板分析：开发板上应看到一个数码管以较慢速度显示 0-F，并有亮灭闪烁。如果显示太快或几乎不闪，说明分频系数不适合人眼观察；如果显示字符不完整，通常是段码位序或共阳极极性错误。

4. 实验体会与讨论

这个任务把时序计数和组合译码结合起来。实现闪烁时不能只写段码，还要考虑显示使能信号，这也是动态显示控制的基础。

任务四：数字计时器设计与实现（选做）

1. 实验目的

1. 练习分钟、秒计数器的级联设计。

2. 掌握十进制位拆分和数码管显示。

3. 理解计时范围和进位/回零条件。

2. 实验任务及要求

1. 实现 0 分 00 秒到 9 分 59 秒计时。

2. 计时应准确，并能在数码管上显示分钟、秒十位、秒个位。

3. 具有复位清零功能。

3. 实验过程

3.1 实验设计思路与实现步骤

计时器先由 50MHz 分频得到 1Hz 时钟；秒计数器 sec 从 0 到 59 循环；当 sec==59 时分钟 min 加 1；分钟从 0 到 9 循环。显示部分把秒拆成十位和个位，再用函数 seg_dec 转换为七段段码。

实现步骤为：编写 1Hz 分频器；编写秒计数器和分钟计数器；用除法和取模得到秒十位、秒个位；写七段译码函数；分配三个数码管管脚；上板观察 0:00 到 9:59 的计时循环。

源程序清单：clockk.v

module clockk(

    input clk_50m,

    input rst_n, // 复位按键 KEY0

    output [6:0] hex2, // 显示 分

    output [6:0] hex1, // 显示 秒十位

    output [6:0] hex0 // 显示 秒个位

);

reg [25:0] cnt_div;

reg clk_1hz;

always @(posedge clk_50m or negedge rst_n) begin

    if(!rst_n) begin

        cnt_div <= 26'd0;

        clk_1hz <= 1'b0;

    end

    else if(cnt_div == 26'd24999999) begin

        cnt_div <= 26'd0;

        clk_1hz <= ~clk_1hz;

    end

    else begin

        cnt_div <= cnt_div + 1'd1;

    end

end

reg [5:0] sec;

always @(posedge clk_1hz or negedge rst_n) begin

    if(!rst_n)

        sec <= 6'd0;

    else if(sec == 6'd59)

        sec <= 6'd0;

    else

        sec <= sec + 1'd1;

end

reg [3:0] min;

always @(posedge clk_1hz or negedge rst_n) begin

    if(!rst_n)

        min <= 4'd0;

    else if(sec == 6'd59) begin

        if(min == 4'd9)

            min <= 4'd0;

        else

            min <= min + 1'd1;

    end

end

wire [3:0] sec_ten = sec / 10; // 秒十位

wire [3:0] sec_one = sec % 10; // 秒个位

function [6:0] seg_dec;

    input [3:0] num;

    begin

        case(num)

            4'd0: seg_dec = 7'b1000000;

            4'd1: seg_dec = 7'b1111001;

            4'd2: seg_dec = 7'b0100100;

            4'd3: seg_dec = 7'b0110000;

            4'd4: seg_dec = 7'b0011001;

            4'd5: seg_dec = 7'b0010010;

            4'd6: seg_dec = 7'b0000010;

            4'd7: seg_dec = 7'b1111000;

            4'd8: seg_dec = 7'b0000000;

            4'd9: seg_dec = 7'b0010000;

            default: seg_dec = 7'b1111111;

        endcase

    end

endfunction

assign hex2 = seg_dec(min);

assign hex1 = seg_dec(sec_ten);

assign hex0 = seg_dec(sec_one);

endmodule

3.2 实验结果与分析

仿真波形分析：正确波形中，复位后 min=0、sec=0；每个 1Hz 有效边沿 sec 加 1；当 sec 从 59 回到 0 时，min 加 1；当 min=9 且 sec=59 后再次回到 0:00。若秒从 60 才回零，应修改边界判断为 sec==59；若分钟提前加 1，应检查分钟计数是否只在秒满时更新。

DE2-115 开发板分析：开发板上应看到三个数码管稳定显示分钟和秒。若跳秒不准确，可能是分频系数不对应 50MHz；若数码管显示残缺，则仍需检查段码和管脚。由于没有动态扫描而是每位固定输出，显示稳定性主要取决于段码正确。

4. 实验体会与讨论

计时器让我体会到多级计数的边界条件比单个计数器更复杂。必须分别验证秒个位、秒十位、分钟位的进位关系，不能只看计数器是否在变化。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
