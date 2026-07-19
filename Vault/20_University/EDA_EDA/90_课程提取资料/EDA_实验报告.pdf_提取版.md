---
id: extract-eda-d88f9833
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/PDF/EDA_实验报告.pdf_课件_未知日期_d88f9833.pdf]]"
source_pages: all
source_hash: "d88f9833619c4988eeab7370a328a2797e335837acb7e229e05cce817d25deaa"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 实验报告.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

《ＥＤＡ技术》试验
实验一
QuartusII软件和DE2-115
开发板使用入门
（一）
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第2页

任务一：半加器原理图设计、编译与仿真
一、实验目的
1.熟悉QuartusII工程建立、原理图输入、编译和波形仿真流程。
2.理解半加器的组合逻辑功能，掌握和位、进位的逻辑表达。
3.学会将原理图模块生成符号文件，供后续层次化设计调用。
二、实验任务及要求
1.在QuartusII中用原理图方式实现半加器。
2.完成编译和波形仿真，验证S=AxorB、C=AandB。
3.仿真成功后生成半加器图形符号。
三、实验过程
1.实验设计思路与实现步骤
半加器输入为A和B，输出为和位S与进位C。设计时先根据真值表列出
逻辑关系：当两个输入不同，和位为1；当两个输入同时为1，进位为1。因
此用XOR门产生S，用AND门产生C。
实现步骤为：新建half_adder工程，选择DE2-115对应器件；新建BDF原
理图文件，放置两个输入端、两个输出端、XOR门和AND门；连接后保存并
设为顶层；编译通过后建立波形文件，依次给出00、01、10、11四组输入；
运行功能仿真，最后生成.bsf符号文件，供全加器任务调用。

## 第3页

图：半加器波形仿真结果
2.实验结果与分析
仿真波形分析：截图中输入按四种组合变化时，和位应呈现0、1、1、0，进
位应呈现0、0、0、1。这个结果与半加器真值表完全一致，所以仿真结果正确。
若波形不正确，首先检查XOR和AND是否接反，其次检查输出端口命名是
否与波形文件中的节点一致；如果某个输出一直为0或X，应返回原理图检查
连线是否悬空，并重新编译后再生成仿真网表。
DE2-115开发板分析：本任务按老师要求不需要上板，主要通过Quartus功
能仿真验证组合逻辑。若扩展到开发板，可把两个输入接拨动开关、两个输出
接LED，开关组合变化时LED应与真值表一致。
四、实验体会与讨论
本任务让我熟悉了从逻辑表达式到原理图再到波形验证的完整流程。半加器
功能很简单，但它是后续全加器层次化设计的基础，因此符号生成和工程文件
保存尤其重要。

## 第4页

任务二：调用半加器实现全加器
一、实验目的
1.掌握层次化原理图设计方法。
2.理解全加器由两个半加器和一个或门构成的结构。
3.通过仿真验证三输入加法的和位和进位。
二、实验任务及要求
1.在新的Quartus工程中调用任务一生成的半加器符号。
2.实现一位全加器并完成波形仿真。
3.验证A、B、Cin八种组合下输出正确。
三、实验过程
1.实验设计思路与实现步骤
全加器输入为A、B、Cin，输出为S和Cout。设计思路是先用第一个半加
器计算A+B，得到中间和S1和进位C1；再用第二个半加器计算S1+Cin，得
到最终和S和进位C2；最后用OR门将C1和C2合成为Cout。
实现步骤为：在sy12工程中复制任务一生成的half_adder.bdf和
half_adder.bsf；新建全加器原理图，调用两个半加器符号；放置OR门并完成
连线；编译后建立波形文件，让A/B/Cin覆盖0到7的所有输入组合；观察S
和Cout是否等于三输入二进制相加结果。

## 第5页

图：全加器原理图或编译结果
图：全加器波形仿真结果
2.实验结果与分析
仿真波形分析：全加器正确输出应满足{Cout,S}=A+B+Cin。例如输入001、
010、100时，输出应为01；输入011、101、110时，输出应为10；输入111

## 第6页

时输出应为11。截图中的波形若按照这个规律变化，即说明层次化调用和进位
合成正确。若波形只在部分组合错误，通常是半加器的中间和或中间进位接线
错误；若所有组合都错误，应检查复制的符号文件是否来自正确的半加器工程。
DE2-115开发板分析：本任务不要求上板，原因是主要训练原理图层次化和
功能仿真。若上板验证，可把三个输入分配到拨动开关，S/Cout分配到LED，
通过八组开关组合观察两个LED是否对应二进制加法结果。
四、实验体会与讨论
本任务体现了模块复用的价值。把半加器封装成符号后，全加器原理图更清
晰，也更接近实际数字系统中由小模块构建大模块的设计方式。
任务三：PLLIP核设计与仿真
一、实验目的
1.掌握Quartus中宏功能模块/IP核的生成流程。
2.理解PLL的输入时钟、复位、输出时钟和锁定信号。
3.学会用顶层模块调用自动生成的IP核。
二、实验任务及要求
1.按教材步骤生成PLLIP核。
2.编写或使用顶层模块调用PLL。
3.通过仿真观察输出时钟和locked信号。
三、实验过程
1.实验设计思路与实现步骤
PLL设计不适合手写普通逻辑完成，而应使用Quartus提供的altpll宏功能
模块。实验思路是先在IP配置界面设置输入时钟和期望输出时钟，再生成
mypll相关文件，最后用顶层pll_top连接复位、输入时钟、输出时钟和锁定信
号。

## 第7页

实现步骤为：打开IP/MegaWizard配置向导；选择PLL类型并设置输入时
钟；根据实验要求配置输出时钟；生成Verilog文件、黑盒文件和例化模板；
在pll_top.v中例化mypll；建立仿真波形，给输入时钟和复位信号，观察输出
时钟是否稳定，以及locked是否在PLL锁定后有效。
源程序清单：pll_top.v
modulepll_top(
inputaclr,clk50m,
outputclk9m,clk100m,locked);
mypllil(
.areset(aclr),
.inclk0(clk50m),
.c0(clk9m),
.c1(clk100m),
.locked(locked));
endmodule
图：PLL仿真或工程结果
2.实验结果与分析

## 第8页

仿真波形分析：PLL的正确波形应表现为输入时钟连续稳定，复位释放后输
出时钟按配置频率翻转，locked在短暂锁定时间后变为有效。如果输出时钟始
终不翻转，优先检查areset是否一直有效、输入时钟周期是否设置错误、顶层
端口是否接到IP的inclk0。如果输出频率与要求不符，应回到IP参数配置界
面检查倍频/分频参数，然后重新生成IP文件并重新编译。
DE2-115开发板分析：本题不需要直接下载到开发板，但PLL输入时钟若
上板通常来自CLOCK_50管脚。实际硬件中应保证复位端释放，否则locked
不会稳定有效，后续由PLL驱动的逻辑也会异常。
四、实验体会与讨论
IP核实验让我意识到EDA设计不只是写Verilog，还包括正确使用厂商提
供的成熟硬件模块。对于时钟类电路，使用IP核比手写逻辑更可靠。
任务四：文本输入实现SW0控制LEDR0
一、实验目的
1.掌握Verilog文本输入方式。
2.熟悉DE2-115拨动开关和LED管脚分配。
3.完成从代码、编译、管脚约束到上板验证的流程。
二、实验任务及要求
1.使用SW0控制LEDR0。
2.当SW0为1时LEDR0亮，当SW0为0时LEDR0灭。
3.用文本方式编写并下载到DE2-115验证。
三、实验过程
1.实验设计思路与实现步骤
该任务是最基本的组合连线逻辑，设计思路是将输入端in直接连续赋值给
输出端out。代码中使用chip_pin属性把in分配到SW0对应管脚AB28，

## 第9页

把out分配到LEDR0对应管脚G19。
实现步骤为：新建工程并选择器件；新建Verilog文件sy14.v；写出输入、
输出和连续赋值；编译确认无错误；通过Programmer下载.sof文件到
DE2-115；拨动SW0，观察LEDR0状态。
源程序清单：sy14.v
modulesy14(in,out);
(*chip_pin="AB28"*)inputin;
(*chip_pin="G19"*)outputout;
assignout=in;
endmodule
2.实验结果与分析
仿真波形分析：若进行功能仿真，out应完全跟随in，没有时钟延迟，因为
这是纯组合连续赋值。若仿真中out不跟随in，一般是端口名加入波形文件时
选错节点，或代码中赋值方向写反。修改方法是确认assignout=in;，重新编译
后再仿真。
DE2-115开发板分析：开发板上SW0拨到高电平位置时LEDR0应点亮，
拨回低电平时应熄灭。若仿真正确但上板不正确，首先检查管脚分配是否对应
SW0/LEDR0，其次检查下载的是否为当前工程最新.sof，还要确认开发板电源、
USB-Blaster和JTAG链接正常。
四、实验体会与讨论
文本输入方式比原理图更简洁。通过这个任务，我掌握了Verilog最基本的
模块结构和管脚约束写法，也理解了“仿真正确”和“上板正确”之间还隔着管脚、
下载和硬件观察这些步骤。

## 第10页

《ＥＤＡ技术》试验
实验二
QuartusII软件和DE2-115
开发板使用入门（二）
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第11页

任务一：SW17控制LEDR17
一、实验目的
1.继续熟悉文本输入设计流程。
2.练习高位拨动开关和高位LED的管脚分配。
3.巩固编译、下载和硬件观察方法。
二、实验任务及要求
1.用SW17控制LEDR17。
2.SW17为1时LEDR17点亮，否则熄灭。
3.需要在DE2-115开发板上验证。
三、实验过程
1.实验设计思路与实现步骤
本任务与实验一SW0控制LEDR0的逻辑相同，但更换了输入输出资源。
设计仍采用连续赋值，重点在于正确选择SW17和LEDR17的管脚。仓库中
的sy25.v已把输入分配到Y23，输出分配到H15。
实现步骤为：新建sy25工程；编写Verilog文件；完成编译；下载到DE2-115；
拨动SW17并观察LEDR17。由于逻辑只有一条直连线，若出现错误，主要从
管脚和下载流程排查。
源程序清单：sy25.v
modulesy25(
(*chip_pin="Y23"*)inputin,
(*chip_pin="H15"*)outputout
);
assignout=in;
endmodule

## 第12页

2.实验结果与分析
仿真波形分析：功能仿真时out应与in同步变化。若in=0时out=1或
in=1时out=0，说明赋值方向或端口极性理解有误，应检查代码是否被写成取
反。如果波形中out为高阻或未知值，应检查输出是否声明正确、文件是否设
为顶层。
DE2-115开发板分析：SW17拨到1时LEDR17点亮，拨到0时熄灭，
说明代码、管脚和下载均正确。若仿真正确但LED不亮，应重点检查LEDR17
的管脚是否和开发板手册一致，或者工程顶层是否仍然指向旧模块。
四、实验体会与讨论
这个任务看似重复，但训练的是避免管脚分配错误。后续复杂实验中输入输
出更多，只有先养成检查QSF和开发板手册的习惯，才能减少硬件调试时间。
任务二：SignalTap正弦信号发生器观察
一、实验目的
1.学习嵌入式逻辑分析仪SignalTap的使用。
2.理解查找表方式产生离散正弦数据。
3.掌握在开发板上抓取内部信号的方法。
二、实验任务及要求
1.以正弦信号发生器为例建立工程。
2.用SignalTap观察cnt、dout、clk_6m等信号。
3.分析抓取数据是否呈周期性正弦变化。
三、实验过程
1.实验设计思路与实现步骤
该任务的核心不是把信号显示到LED，而是在FPGA内部产生周期性数据，
再用SignalTap抓取。sy261.v先用count8对50MHz时钟进行节拍划分，产

## 第13页

生较慢的clk_6m采样信号；在clk_6m上升沿，计数器cnt递增；case(cnt)输
出0到255范围内的查找表数据dout，这些数据近似一个正弦周期。
实现步骤为：建立工程并编译；打开SignalTap，添加cnt、dout、clk_6m、
clr等节点；设置采样时钟和触发条件；下载到开发板后运行采样；观察数据是
否从中值逐渐上升到最大、再下降到最小、最后回到中值。
源程序清单：sy261.v
modulesy261(clock,clr,dout,clk_6m);
(*chip_pin="AB28"*)inputclr;
(*chip_pin="Y2"*)inputclock;
outputregclk_6m;
outputreg[7:0]dout;
reg[6:0]cnt;
reg[2:0]count8;
always@(posedgeclock)
beginif(count8==7)
begincount8<=0;clk_6m<=1;end
elsebegincount8<=count8+1;clk_6m<=0;endend
always@(posedgeclk_6mornegedgeclr)
begin
if(!clr)cnt<=0;elsecnt<=cnt+1;
case(cnt)
0:dout<=127;1:dout<=134;2:dout<=140;3:dout<=146;4:dout<=152;
5:dout<=159;6:dout<=165;7:dout<=171;8:dout<=176;9:dout<=182;
10:dout<=188;11:dout<=193;12:dout<=199;13:dout<=204;14:dout<=209;

## 第14页

15:dout<=213;16:dout<=218;17:dout<=222;18:dout<=226;19:dout<=230;
20:dout<=234;21:dout<=237;22:dout<=240;23:dout<=243;24:dout<=246;
25:dout<=248;26:dout<=250;27:dout<=252;28:dout<=253;29:dout<=254;
30:dout<=255;31:dout<=255;32:dout<=255;33:dout<=255;34:dout<=255;
35:dout<=254;36:dout<=253;37:dout<=252;38:dout<=250;39:dout<=248;
40:dout<=246;41:dout<=243;42:dout<=240;43:dout<=237;44:dout<=234;
45:dout<=230;46:dout<=226;47:dout<=222;48:dout<=218;49:dout<=213;
50:dout<=209;51:dout<=204;52:dout<=199;53:dout<=193;54:dout<=188;
55:dout<=182;56:dout<=176;57:dout<=171;58:dout<=165;59:dout<=159;
60:dout<=152;61:dout<=146;62:dout<=140;63:dout<=134;64:dout<=128;
65:dout<=121;66:dout<=115;67:dout<=109;68:dout<=103;69:dout<=96;
70:dout<=90;71:dout<=84;72:dout<=79;73:dout<=73;74:dout<=67;
75:dout<=62;76:dout<=56;77:dout<=51;78:dout<=46;79:dout<=42;
80:dout<=37;81:dout<=33;82:dout<=29;83:dout<=25;84:dout<=21;
85:dout<=18;86:dout<=15;87:dout<=12;88:dout<=9;89:dout<=7;
90:dout<=5;91:dout<=3;92:dout<=2;93:dout<=1;94:dout<=0;
95:dout<=0;96:dout<=0;97:dout<=0;98:dout<=0;99:dout<=1;
100:dout<=2;101:dout<=3;102:dout<=5;103:dout<=7;104:dout<=9;
105:dout<=12;106:dout<=15;107:dout<=18;108:dout<=21;109:dout<=25;
110:dout<=29;111:dout<=33;112:dout<=37;113:dout<=42;114:dout<=46;
115:dout<=51;116:dout<=56;117:dout<=62;118:dout<=67;119:dout<=73;
120:dout<=79;121:dout<=84;122:dout<=90;123:dout<=96;124:dout<=103;
125:dout<=109;126:dout<=115;127:dout<=121;
endcaseendendmodule

## 第15页

图：SignalTap正弦信号观察结果
2.实验结果与分析
仿真波形分析：若用仿真观察，clk_6m应按count8的计数周期产生脉冲，
cnt只在clk_6m有效边沿递增，dout应按查找表顺序变化。截图中如果dout
呈现先增后减的周期性规律，就说明查找表和计数逻辑正确。如果dout卡在某
个数值，常见原因是复位clr一直有效或clk_6m没有翻转；如果波形跳变顺
序错乱，应检查case(cnt)是否覆盖完整地址，或者cnt位宽是否足够。
DE2-115开发板分析：SignalTap抓取到的内部数据若与仿真规律一致，说
明硬件中时钟、复位和查找表逻辑都正常。若仿真正确而SignalTap数据不动，
应检查采样时钟选择是否正确、节点是否被优化、工程是否启用了SignalTap文
件。
四、实验体会与讨论

## 第16页

SignalTap让我看到LED无法直接反映的内部状态。以后遇到开发板现象不
明显的问题，可以优先抓取关键寄存器和状态信号，而不是盲目改代码。
任务三：PLL实现50MHz到5MHz分频
一、实验目的
1.巩固PLLIP核的生成和调用。
2.理解输入时钟周期与输出分频关系。
3.练习用仿真或SignalTap验证时钟频率。
二、实验任务及要求
1.使用altpll宏功能模块实现50MHz到5MHz分频。
2.输入时钟周期按20ns设置。
3.完成波形仿真，并可用SignalTap分析。
三、实验过程
1.实验设计思路与实现步骤
本任务使用PllIP核完成十分频。输入时钟inclk0来自DE2-115的
50MHz时钟，周期为20ns；输出c0目标频率为5MHz，周期为200ns。工程
中areset分配到AB28，输入时钟分配到Y2。
实现步骤为：打开PLL配置向导；设置输入时钟为50MHz；配置输出c0为
5MHz；生成Pll.v等文件；建立仿真波形，给inclk020ns周期时钟，并让areset
释放；观察c0周期是否约为输入的10倍，locked是否稳定有效。
modulePll(
areset,
inclk0,
c0,
locked

## 第17页

);
图：PLL50MHz到5MHz仿真结果

## 第18页

图：PLL分频SignalTap或工程结果
2.实验结果与分析
仿真波形分析：正确波形应满足inclk0每20ns翻转一个完整输入周期，c0
的完整周期约为200ns，即输出频率为5MHz。locked在复位释放后经过锁定
时间变为有效。如果c0没有输出，应检查areset是否保持有效；如果输出周
期不是200ns，应回到PLL参数界面检查分频/倍频设置；如果locked抖动，
可能是输入时钟不连续或复位信号设置不合理。
DE2-115开发板分析：上板时可用SignalTap抓取c0与locked。若仿真正
确而板上不正确，应检查输入时钟管脚Y2是否分配到inclk0，复位按键是否
释放，以及下载的SOF是否为包含PLL的工程。
四、实验体会与讨论

## 第19页

通过本任务，我进一步理解了时钟IP的使用边界。时钟分频虽然也能用计
数器实现，但PLL能提供更准确、更适合FPGA时钟网络的输出。

## 第20页

《ＥＤＡ技术》试验
实验三
组合逻辑电路设计、仿真与实
现
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第21页

任务一：4-7BCD码译码器
一、实验目的
1.掌握七段数码管译码逻辑。
2.理解共阳极数码管段码低电平点亮的特点。
3.练习用case语句描述组合逻辑。
二、实验任务及要求
1.用4个拨动开关输入BCD码。
2.用一个七段数码管显示0到9。
3.非法输入10到15时应避免显示错误数字。
三、实验过程
1.实验设计思路与实现步骤
BCD输入只有0000到1001是有效十进制数字。设计时根据DE2-115共
阳极数码管段码表，为每个数字写出7位段码。由于共阳极数码管通常低电平
点亮，所以数字0的段码为1000000，表示除g段外其余段点亮。
实现步骤为：建立bcd_7seg工程；编写always@(*)组合逻辑；用
case(bcd_in)覆盖0到9；默认分支输出全灭；编译后分配4个开关和7个
数码管段管脚；上板拨动开关观察显示。
源程序清单：bcd_7seg.v
modulebcd_7seg(
inputwire[3:0]bcd_in,//4位BCD输入：SW17~SW14，对应bcd_in[3:0]
outputreg[6:0]seg_out//7位段码：HEX0[6:0]，对应gfedcba
);
always@(*)begin

## 第22页

case(bcd_in)
4'b0000:seg_out=7'b1000000;//0
4'b0001:seg_out=7'b1111001;//1
4'b0010:seg_out=7'b0100100;//2
4'b0011:seg_out=7'b0110000;//3
4'b0100:seg_out=7'b0011001;//4
4'b0101:seg_out=7'b0010010;//5
4'b0110:seg_out=7'b0000010;//6
4'b0111:seg_out=7'b1111000;//7
4'b1000:seg_out=7'b0000000;//8
4'b1001:seg_out=7'b0010000;//9
default:seg_out=7'b1111111;//10-15全灭
endcase
end
endmodule
输入 预期显示 输入 预期显示
0000 0 0101 5
0001 1 0110 6
0010 2 0111 7
0011 3 1000 8
0100 4 1001 9
2.实验结果与分析

## 第23页

图：4-7BCD码译码器结果
仿真波形分析：正确波形应表现为bcd_in每改变为一个有效BCD值，
seg_out立即变化为对应段码，无时钟延迟。若0到9的段码和表格一致，则
仿真正确。若某个数字显示错，应检查该分支段码位序是否按gfedcba或工程
实际连接顺序编写；若所有数字都反相，说明共阳/共阴极理解错误，需要把段
码取反。
DE2-115开发板分析：开发板上拨动4个开关输入0到9时，数码管应
显示相应数字。若仿真正确但板上段位错乱，通常是管脚分配顺序与seg_out[6:0]
位序不一致，应按开发板手册重新核对HEX0的a-g管脚。
四、实验体会与讨论
这个任务让我认识到显示电路不仅要逻辑正确，还要考虑硬件极性和管脚顺
序。写七段译码时最好先确定位序，再建立统一的段码表。
任务二：4位全加器及七段显示
一、实验目的
1.掌握多位加法和显示模块的组合设计。

## 第24页

2.练习把运算模块与显示模块分开。
3.理解二进制输入到十进制显示的转换。
二、实验任务及要求
1.用拨动开关输入两个4位数据。
2.将两个输入数据和加法结果显示到七段数码管。
3.采用运算模块和显示模块分离的结构。
三、实验过程
1.实验设计思路与实现步骤
顶层top_adder4接收SW_A[3:0]和SW_B[3:0]。因为每个操作数范围是0
到15，显示时需要拆成十位和个位；加法结果范围是0到30，也拆成十位和
个位。显示模块seg7负责把0到9转为段码。
实现步骤为：编写七段译码模块；在顶层中计算sum=SW_A+SW_B；用除
以10和取模10得到十位、个位；例化多个seg7模块显示A、B、sum；完
成管脚分配后上板验证不同输入组合。
源程序清单：top_adder4.v
moduletop_adder4(
inputwire[3:0]SW_A,//SW17~SW14→A(0~15)
inputwire[3:0]SW_B,//SW13~SW10→B(0~15)
outputwire[6:0]HEX7,
outputwire[6:0]HEX6,
outputwire[6:0]HEX5,
outputwire[6:0]HEX4,

## 第25页

outputwire[6:0]HEX3,
outputwire[6:0]HEX2,
outputwire[6:0]HEX1,
outputwire[6:0]HEX0
);
//==============================
//A：0~15拆分为十位、个位
//==============================
wire[3:0]A_ten=SW_A/10;
wire[3:0]A_unit=SW_A%10;
//==============================
//B：0~15拆分为十位、个位
//==============================
wire[3:0]B_ten=SW_B/10;
wire[3:0]B_unit=SW_B%10;
//==============================
//求和sum：0~30
//==============================
wire[4:0]sum=SW_A+SW_B;
//==============================

## 第26页

//sum拆分为十位、个位
//==============================
wire[3:0]sum_ten=sum/10;
wire[3:0]sum_unit=sum%10;
//==============================
//显示A：HEX7(十位)+HEX6(个位)
//==============================
seg7u7(.num(A_ten),.seg(HEX7));
seg7u6(.num(A_unit),.seg(HEX6));
//==============================
//显示B：HEX5(十位)+HEX4(个位)
//==============================
seg7u5(.num(B_ten),.seg(HEX5));
seg7u4(.num(B_unit),.seg(HEX4));
//==============================
//显示sum：HEX1(十位)+HEX0(个位)
//==============================
seg7u3(.num(4'd0),.seg(HEX3));
seg7u2(.num(4'd0),.seg(HEX2));
seg7u1(.num(sum_ten),.seg(HEX1));
seg7u0(.num(sum_unit),.seg(HEX0));

## 第27页

endmodule
源程序清单：seg7.v
moduleseg7(
inputwire[3:0]num,
outputreg[6:0]seg
);
always@(*)begin
case(num)
4'd0:seg=7'b1000000;
4'd1:seg=7'b1111001;
4'd2:seg=7'b0100100;
4'd3:seg=7'b0110000;
4'd4:seg=7'b0011001;
4'd5:seg=7'b0010010;
4'd6:seg=7'b0000010;
4'd7:seg=7'b1111000;
4'd8:seg=7'b0000000;
4'd9:seg=7'b0010000;
default:seg=7'b1111111;
endcase
end

## 第28页

endmodule
2.实验结果与分析
仿真波形分析：正确判断方法是检查sum是否等于SW_A+SW_B，再检查
十位和个位是否满足sum_ten=sum/10、sum_unit=sum%10。例如A=9、B=8时
结果应为17，数码管结果十位显示1、个位显示7。若加法值正确但显示错误，
应检查seg7段码；若显示十位错误，应检查除法/取模结果位宽是否足够。
DE2-115开发板分析：上板时通过拨动开关输入两个数字，A、B和结果数
码管应同步变化。若某一组数码管一直不亮，通常是对应HEX管脚没有分配
或段码极性错误；若输入超过9时显示十进制10-15，应确认拆位逻辑是否按
二进制数值而非BCD直接解释。
四、实验体会与讨论
这个任务比单个译码器更接近实际系统，因为它同时包含输入、运算和显示。
把显示模块独立出来后，后续ALU、计数器等任务都可以复用类似思想。
任务三：4位比较器
一、实验目的
1.掌握比较器组合逻辑设计。
2.理解三个比较结果互斥输出的关系。
3.练习用LED显示逻辑判断结果。
二、实验任务及要求
1.用两组4位拨动开关输入A和B。
2.用LED分别指示A>B、A=B、A<B。
3.在开发板上验证比较结果。
三、实验过程

## 第29页

1.实验设计思路与实现步骤
4位比较器可直接用Verilog关系运算符描述。因为任意两个数只可能满足
大于、等于、小于三种关系之一，所以三个LED输出应互斥。该方式简洁，
也便于综合工具映射为组合比较电路。
实现步骤为：建立comparator4模块；声明两组4位输入和三个输出；用连
续赋值分别描述sw_a>sw_b、sw_a==sw_b、sw_a<sw_b；编译并分配8个
开关和3个LED；上板输入典型组合验证。
源程序清单：cmp.v
modulecomparator4(
//输入：两组4位操作数，对应拨码开关SW17~SW10
inputwire[3:0]sw_a,//操作数A：SW17~SW14(sw_a[3]~sw_a[0])
inputwire[3:0]sw_b,//操作数B：SW13~SW10(sw_b[3]~sw_b[0])
//输出：3个LED，高电平点亮
outputwireled_a_gt_b,//A>B时点亮
outputwireled_a_eq_b,//A==B时点亮
outputwireled_a_lt_b//A<B时点亮
);
//比较逻辑
assignled_a_gt_b=(sw_a>sw_b);
assignled_a_eq_b=(sw_a==sw_b);
assignled_a_lt_b=(sw_a<sw_b);
endmodule

## 第30页

2.实验结果与分析
仿真波形分析：正确波形应满足任意时刻三个输出中只有一个为1。例如
A=5、B=3时led_a_gt_b=1；A=7、B=7时led_a_eq_b=1；A=2、B=9时
led_a_lt_b=1。若两个LED同时为1，说明比较表达式或输出连接错误；若所
有LED都为0，应检查输入是否为未知值或输出节点是否加入错误。
DE2-115开发板分析：开发板上拨动两组开关后，应只有一个LED点亮。
若仿真正确但板上多个LED亮，可能是LED管脚分配到同一个或相邻端口，
也可能是输入开关位序与预期相反，需要对照QSF检查sw_a[3:0]和
sw_b[3:0]的高低位。
四、实验体会与讨论
比较器任务让我体会到Verilog高级关系运算符可以直接表达硬件功能，但
上板时仍然要认真核对位序，否则数值大小会被解释错。

## 第31页

《ＥＤＡ技术》试验
实验四
时序逻辑电路设计
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第32页

任务一：模200计数器两种实现
一、实验目的
1.掌握时序计数器的行为描述方法。
2.理解IP核计数器的例化和复位信号适配。
3.比较手写逻辑和IP核实现同一功能的差异。
二、实验任务及要求
1.设计模200二进制加法计数器。
2.用Verilog行为描述和IP核两种方式实现。
3.仿真时要观察计数最大值199以及回零过程。
三、实验过程
1.实验设计思路与实现步骤
行为描述版本使用一个8位寄存器out，在时钟上升沿递增，低电平复位时
清零，计数到199后回到0。IP版本使用counter_mod200a，顶层
ip_counter_mod200将低有效复位rst_n取反后接到IP的高有效清零端aclr。
实现步骤为：先编写并仿真counter_mod200.v；再用QuartusIP生成计数器
核；写顶层调用IP；分别建立波形文件，输入时钟和复位；拖动仿真波形滚动
条到199附近，确认计数器是否从199回到0。
源程序清单：counter_mod200.v
modulecounter_mod200(
inputclk,
inputrst_n,
outputreg[7:0]out
);

## 第33页

always@(posedgeclkornegedgerst_n)
begin
if(!rst_n)
out<=8'd0;
elseif(out==8'd199)
out<=8'd0;
else
out<=out+1'd1;
end
endmodule
源程序清单：ip_counter_mod200.v
moduleip_counter_mod200(
inputclk,
inputrst_n,//低电平异步复位
output[7:0]q,//计数输出0~199
outputcout//进位输出，数到199时为1
);
counter_mod200au_counter(
.clock(clk),
.aclr(~rst_n),//IP核的aclr是高电平有效，所以取反
.q(q),
.cout(cout)
);

## 第34页

endmodule
图：模200计数器仿真结果一

## 第35页

图：模200计数器仿真结果二

## 第36页

图：IP计数器仿真结果
图：计数到199后回零结果
2.实验结果与分析
仿真波形分析：正确结果是复位释放后out/q从0开始逐拍加1，达到十进
制199后下一拍回到0。截图若显示199后立即回零，则模值正确。若计数
到200才回零，说明判断条件写成了out==200或复位/加一顺序不对；若计数
一直不动，应检查复位是否一直有效或时钟是否没有加入波形。
DE2-115开发板分析：本任务主要要求仿真。若上板，可把计数值低位接
LED或接数码管显示，但50MHz时钟下人眼无法观察，需要先分频。若板上
显示跳变过快，不代表计数错误，而是缺少可观察的慢时钟。
四、实验体会与讨论
计数器设计最容易出错的是边界值。通过专门观察199附近波形，我学会了
不能只看前几个周期，还要检查回零边界是否满足模值要求。
任务二：10分频器设计与仿真
一、实验目的

## 第37页

1.掌握偶数分频器设计方法。
2.理解计数翻转输出实现50MHz到5MHz的关系。
3.练习分析时钟周期和占空比。
二、实验任务及要求
1.对50MHz输入时钟进行10分频。
2.输出5MHz时钟。
3.仿真时在NodeFinder中选择全部管脚和寄存器，观察计数器与输出时钟。
三、实验过程
1.实验设计思路与实现步骤
10分频的设计思路是用0到9的循环计数器控制输出翻转。计数到4时
输出翻转一次，计数到9时输出再翻转一次并清零，这样输出的高低电平各持
续5个输入周期，完整输出周期为10个输入周期。
实现步骤为：编写fenping10.v；复位时清零计数器并让输出为0；时钟上升
沿根据cnt的值决定加一、翻转或回零；建立波形文件输入50MHz时钟；观
察clk_out的周期是否为输入的10倍。
源程序清单：fenping10.v
modulefenping10(
inputclk,//50MHz输入
inputrst_n,//低电平复位
outputregclk_out//5MHz输出
);
reg[3:0]cnt;//计数器0~9

## 第38页

always@(posedgeclkornegedgerst_n)begin
if(!rst_n)begin
cnt<=4'd0;
clk_out<=1'b0;
end
elseif(cnt==4'd4)begin//计数到4翻转
cnt<=cnt+1'b1;
clk_out<=~clk_out;
end
elseif(cnt==4'd9)begin//计数到9归0
cnt<=4'd0;
clk_out<=~clk_out;
end
elsebegin
cnt<=cnt+1'b1;
end
end
endmodule

## 第39页

图：10分频仿真结果
2.实验结果与分析
仿真波形分析：正确波形中，cnt应从0计到9，再回到0；clk_out在cnt=4
和cnt=9附近翻转，因此输出周期等于10个输入周期，占空比约为50%。若
输出频率不是5MHz，应检查翻转点是否写错；若占空比明显不对，应检查高
电平和低电平持续的输入周期数是否相等。
DE2-115开发板分析：若把5MHz时钟直接接LED，人眼仍无法观察明显
闪烁，因此上板分析应借助示波器或SignalTap。若后续电路使用该分频时钟，
需注意它是由逻辑寄存器产生的普通信号，不应随意作为全局高质量时钟使用。
四、实验体会与讨论
分频器让我更清楚地理解了“翻转一次不是一个完整周期”。完整周期包含一
次上升和一次下降，所以10分频需要两个翻转点配合。
任务三：0-F闪烁七段显示控制
一、实验目的

## 第40页

1.掌握慢时钟分频和周期显示控制。
2.练习七段数码管显示0到F。
3.理解闪烁效果与显示使能的关系。
二、实验任务及要求
1.在一个共阳极七段数码管上循环显示0到F。
2.显示应带闪烁功能。
3.使用分频后的慢时钟，避免人眼无法观察。
三、实验过程
1.实验设计思路与实现步骤
设计分为三部分：第一部分将50MHz时钟分频为约1Hz；第二部分用4位
计数器num在0到15循环；第三部分根据num输出七段段码，并利用慢
时钟低电平阶段输出全灭段码，实现闪烁。
实现步骤为：编写分频计数器cnt_div；在clk_1hz上升沿更新num；编写
0-F的段码case；当clk_1hz==0时输出1111111全灭；编译、仿真并下载观
察。
源程序清单：seg_scan_flash.v
moduleseg_scan_flash(
inputclk_50m,
inputrst_n,
output[6:0]seg
);
reg[25:0]cnt_div;
regclk_1hz;

## 第41页

always@(posedgeclk_50mornegedgerst_n)
begin
if(!rst_n)begin
cnt_div<=26'd0;
clk_1hz<=1'b0;
end
elseif(cnt_div==26'd24999999)begin
cnt_div<=26'd0;
clk_1hz<=~clk_1hz;
end
elsebegin
cnt_div<=cnt_div+1'd1;
end
end
reg[3:0]num;
always@(posedgeclk_1hzornegedgerst_n)
begin
if(!rst_n)
num<=4'd0;
elseif(num==4'd15)
num<=4'd0;

## 第42页

else
num<=num+1'd1;
end
reg[6:0]seg_r;
always@(*)begin
if(clk_1hz==1'b0)begin
seg_r=7'b1111111;
end
elsebegin
case(num)
4'd0:seg_r=7'b1000000;
4'd1:seg_r=7'b1111001;
4'd2:seg_r=7'b0100100;
4'd3:seg_r=7'b0110000;
4'd4:seg_r=7'b0011001;
4'd5:seg_r=7'b0010010;
4'd6:seg_r=7'b0000010;
4'd7:seg_r=7'b1111000;
4'd8:seg_r=7'b0000000;
4'd9:seg_r=7'b0010000;
4'd10:seg_r=7'b0001000;
4'd11:seg_r=7'b0000011;

## 第43页

4'd12:seg_r=7'b1000110;
4'd13:seg_r=7'b0100001;
4'd14:seg_r=7'b0000110;
4'd15:seg_r=7'b0001110;
default:seg_r=7'b1111111;
endcase
end
end
assignseg=seg_r;
endmodule
2.实验结果与分析
仿真波形分析：正确波形中，num应按0、1、2...F循环变化；seg在慢时
钟高电平时显示当前数字段码，在慢时钟低电平时全灭。因此如果只看某一个
周期，可能会看到显示和全灭交替，这是闪烁功能而不是错误。若数码管不闪
烁，应检查全灭分支是否存在；若数字顺序错误，应检查num的递增和回零条
件。
DE2-115开发板分析：开发板上应看到一个数码管以较慢速度显示0-F，并
有亮灭闪烁。如果显示太快或几乎不闪，说明分频系数不适合人眼观察；如果
显示字符不完整，通常是段码位序或共阳极极性错误。
四、实验体会与讨论
这个任务把时序计数和组合译码结合起来。实现闪烁时不能只写段码，还要
考虑显示使能信号，这也是动态显示控制的基础。

## 第44页

任务四：数字计时器设计与实现（选做）
一、实验目的
1.练习分钟、秒计数器的级联设计。
2.掌握十进制位拆分和数码管显示。
3.理解计时范围和进位/回零条件。
二、实验任务及要求
1.实现0分00秒到9分59秒计时。
2.计时应准确，并能在数码管上显示分钟、秒十位、秒个位。
3.具有复位清零功能。
三、实验过程
1.实验设计思路与实现步骤
计时器先由50MHz分频得到1Hz时钟；秒计数器sec从0到59循环；
当sec==59时分钟min加1；分钟从0到9循环。显示部分把秒拆成十位
和个位，再用函数seg_dec转换为七段段码。
实现步骤为：编写1Hz分频器；编写秒计数器和分钟计数器；用除法和取
模得到秒十位、秒个位；写七段译码函数；分配三个数码管管脚；上板观察0:00
到9:59的计时循环。
源程序清单：clockk.v
moduleclockk(
inputclk_50m,
inputrst_n,//复位按键KEY0
output[6:0]hex2,//显示分
output[6:0]hex1,//显示秒十位
output[6:0]hex0//显示秒个位

## 第45页

);
reg[25:0]cnt_div;
regclk_1hz;
always@(posedgeclk_50mornegedgerst_n)begin
if(!rst_n)begin
cnt_div<=26'd0;
clk_1hz<=1'b0;
end
elseif(cnt_div==26'd24999999)begin
cnt_div<=26'd0;
clk_1hz<=~clk_1hz;
end
elsebegin
cnt_div<=cnt_div+1'd1;
end
end
reg[5:0]sec;
always@(posedgeclk_1hzornegedgerst_n)begin
if(!rst_n)

## 第46页

sec<=6'd0;
elseif(sec==6'd59)
sec<=6'd0;
else
sec<=sec+1'd1;
end
reg[3:0]min;
always@(posedgeclk_1hzornegedgerst_n)begin
if(!rst_n)
min<=4'd0;
elseif(sec==6'd59)begin
if(min==4'd9)
min<=4'd0;
else
min<=min+1'd1;
end
end
wire[3:0]sec_ten=sec/10;//秒十位
wire[3:0]sec_one=sec%10;//秒个位

## 第47页

function[6:0]seg_dec;
input[3:0]num;
begin
case(num)
4'd0:seg_dec=7'b1000000;
4'd1:seg_dec=7'b1111001;
4'd2:seg_dec=7'b0100100;
4'd3:seg_dec=7'b0110000;
4'd4:seg_dec=7'b0011001;
4'd5:seg_dec=7'b0010010;
4'd6:seg_dec=7'b0000010;
4'd7:seg_dec=7'b1111000;
4'd8:seg_dec=7'b0000000;
4'd9:seg_dec=7'b0010000;
default:seg_dec=7'b1111111;
endcase
end
endfunction
assignhex2=seg_dec(min);
assignhex1=seg_dec(sec_ten);

## 第48页

assignhex0=seg_dec(sec_one);
endmodule
2.实验结果与分析
仿真波形分析：正确波形中，复位后min=0、sec=0；每个1Hz有效边沿sec
加1；当sec从59回到0时，min加1；当min=9且sec=59后再次回到
0:00。若秒从60才回零，应修改边界判断为sec==59；若分钟提前加1，应检
查分钟计数是否只在秒满时更新。
DE2-115开发板分析：开发板上应看到三个数码管稳定显示分钟和秒。若跳
秒不准确，可能是分频系数不对应50MHz；若数码管显示残缺，则仍需检查段
码和管脚。由于没有动态扫描而是每位固定输出，显示稳定性主要取决于段码
正确。
四、实验体会与讨论
计时器让我体会到多级计数的边界条件比单个计数器更复杂。必须分别验证
秒个位、秒十位、分钟位的进位关系，不能只看计数器是否在变化。

## 第49页

《ＥＤＡ技术》试验
实验五
层次化电路设计与实现
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第50页

任务一：4位累加器设计、仿真与实现
一、实验目的
1.理解累加器由加法器、寄存器、分频器和显示译码器组成。
2.掌握层次化设计中顶层模块协调多个子模块的方法。
3.练习用按键输入数据并用七段数码管显示累加结果。
二、实验任务及要求
1.设计4位累加器。
2.要求采用层次化电路设计方法。
3.用按键输入数据，用七段数码管显示结果；结果不正确时可用仿真或
SignalTap排查。
三、实验过程
1.实验设计思路与实现步骤
当前仓库中EDA第五次实验/sy1保存了工程文件、编译报告和输出文件，
且output_files中存在.done，说明工程曾经完成编译。但QSF中记录的源码
路径为外部路径D:/quartus/abc/add4.v、reg4.v、acc4.v、clk_div.v、seg7.v、sy1.v，
这些源码未保存在本仓库中。因此本任务报告只根据老师要求、工程配置和编
译结果说明设计过程，不补造源程序。
合理的层次化设计应包括：4位加法器用于计算当前累加值与新输入的和；4
位寄存器用于保存累加结果；按键或使能信号控制寄存器更新；分频模块把
50MHz时钟变为人眼可观察的慢节拍；七段译码模块显示累加结果。实现步骤
应先分别验证加法器和寄存器，再把它们接入顶层，最后调试显示部分。
2.实验结果与分析
仿真波形分析：正确的累加器波形应满足每次有效按键或使能到来时，寄存
器输出更新为“旧累加值+输入值”；复位后累加值回到0；若输入保持不变且

## 第51页

使能无效，输出保持不变。若波形中结果每个50MHz时钟都累加，说明按键
使能没有正确同步或去抖；若结果只显示输入值而不累加，说明寄存器反馈没
有接回加法器。
DE2-115开发板分析：上板时按键输入后，七段数码管应显示累加后的结果。
若显示跳变很快，可能是按键抖动或时钟未分频；若显示不正确，可用SignalTap
抓取寄存器当前值、输入值、加法器输出和更新使能，判断错误发生在运算、
寄存还是显示环节。
四、实验体会与讨论
虽然仓库缺少该任务源码，但从工程记录可以看出该任务的重点是层次化连
接。累加器调试不能只看最终数码管，应优先验证内部寄存器反馈路径是否正
确。
任务二：4位算术逻辑运算单元ALU
一、实验目的
1.掌握ALU多运算选择设计。
2.理解零标志位Z的产生方法。
3.练习运算模块、显示模块和顶层模块的分层组织。
二、实验任务及要求
1.实现加、减、与、或、异或、非、逻辑左移、逻辑右移、算术右移。
2.输入数据和运算结果用七段数码管显示。
3.结果为0时Z标志输出为1。
三、实验过程
1.实验设计思路与实现步骤
ALU核心模块alu4根据aluc选择不同运算。顶层sy2把拨动开关分为操
作数A、操作数B和运算选择码，ALU输出结果后送入七段译码器显示，同

## 第52页

时把零标志接到LED。
实现步骤为：先写加减模块add_sub4；再写ALU的case(aluc)选择逻辑；
写七段译码模块；顶层例化ALU和三个显示模块；分配输入开关、显示管脚
和零标志LED；对每个运算选择码分别仿真和上板验证。
源程序清单：add_sub4.v
moduleadd_sub4(
output[3:0]s,
outputcout,
input[3:0]a,b,
inputmode
);
assign{cout,s}=mode?(a-b):(a+b);
endmodule
源程序清单：alu4.v
modulealu4(
outputreg[3:0]c,//运算结果
outputZ,//全零标志位，c=0时Z=1
input[3:0]a,b,//两个4位输入
input[3:0]aluc//运算选择控制信号
);
//加减用的线
wire[3:0]add_s;
wireadd_cout;

## 第53页

add_sub4u_addsub(add_s,add_cout,a,b,aluc==1);
always@(*)begin
case(aluc)
4'd0:c=a+b;//0:加法
4'd1:c=a-b;//1:减法
4'd2:c=a&b;//2:与
4'd3:c=a|b;//3:或
4'd4:c=a^b;//4:异或
4'd5:c=~a;//5:非（只对a）
4'd6:c=a<<1;//6:逻辑左移
4'd7:c=a>>1;//7:逻辑右移
4'd8:c=$signed(a)>>>1;//8:算术右移
default:c=4'b0000;
endcase
end
//全零标志：结果c是0000则Z=1
assignZ=(c==4'b0000);
endmodule
源程序清单：sy2.v
modulesy2(
inputCLOCK_50,

## 第54页

input[3:0]SWa,//SW0~3：操作数a
input[3:0]SWb,//SW4~7：操作数b
input[3:0]SWaluc,//SW8~11：运算选择
output[6:0]HEX0,//显示结果c
output[6:0]HEX4,//显示a
output[6:0]HEX5,//显示b
outputLEDZ//显示全零标志Z
);
wire[3:0]result;
wirezflag;
//实例化ALU
alu4u_alu(
.c(result),
.Z(zflag),
.a(SWa),
.b(SWb),
.aluc(SWaluc)
);
seg7d0(HEX0,result);//结果
seg7d4(HEX4,SWa);//显示a
seg7d5(HEX5,SWb);//显示b

## 第55页

assignLEDZ=zflag;//结果为0时亮灯
endmodule
源程序清单：seg7.v
moduleseg7(
outputreg[6:0]seg,
input[3:0]din
);
always@(*)begin
case(din)
4'h0:seg=7'b1000000;
4'h1:seg=7'b1111001;
4'h2:seg=7'b0100100;
4'h3:seg=7'b0110000;
4'h4:seg=7'b0011001;
4'h5:seg=7'b0010010;
4'h6:seg=7'b0000010;
4'h7:seg=7'b1111000;
4'h8:seg=7'b0000000;
4'h9:seg=7'b0010000;
4'ha:seg=7'b0001000;
4'hb:seg=7'b0000011;
4'hc:seg=7'b1000110;

## 第56页

4'hd:seg=7'b0100001;
4'he:seg=7'b0000110;
4'hf:seg=7'b0001110;
endcase
end
endmodule
2.实验结果与分析
仿真波形分析：应选取典型输入逐项验证，例如A=5、B=3时，加法结果为
8，减法结果为2，与为1，或为7，异或为6；当结果为0时Z=1。如果某
一种运算错误而其他运算正确，应检查case(aluc)对应分支；如果所有显示错
误但内部c正确，应检查seg7；如果Z总是0，应检查assignZ=(c==
4'b0000)是否连接到顶层LED。
DE2-115开发板分析：拨动SWa、SWb和SWaluc时，HEX应显示操作
数和结果，LEDZ在结果为0时点亮。若仿真正确但上板选择码混乱，通常是
SWaluc[3:0]的管脚高低位顺序与预期不一致。
四、实验体会与讨论
ALU是典型的层次化综合任务。通过这个任务我体会到，每增加一种运算都
应增加相应测试组合，否则很容易只验证加减法而漏掉移位和取反。
任务三：三层楼道灯组合控制电路
一、实验目的
1.理解实际控制问题到逻辑表达式的转换。
2.掌握三输入异或逻辑。
3.练习用LED表示组合逻辑输出。
二、实验任务及要求

## 第57页

1.三层楼每层一个开关，共同控制一盏灯。
2.任意一个开关动作都能改变灯的亮灭状态。
3.采用组合逻辑实现。
三、实验过程
1.实验设计思路与实现步骤
楼道灯问题可抽象为奇偶控制：三个开关中有奇数个为1时灯亮，有偶数个
为1时灯灭，因此输出F=S1xorS2xorS3。该表达式正好表示三个开关状态
的奇偶性。
实现步骤为：建立sy3模块；声明三个输入S1/S2/S3和输出F；用连续赋
值写出三输入异或；编译后将三个输入接拨动开关，输出接LED；上板测试8
种开关组合。
源程序清单：sy3.v
modulesy3(
outputF,
inputS1,
inputS2,
inputS3
);
assignF=S1^S2^S3;
endmodule
2.实验结果与分析
仿真波形分析：8种输入组合中，001、010、100、111应输出1，000、011、
101、110应输出0。若仿真与该真值表一致，说明组合逻辑正确。若只在111
时错误，应检查是否错误使用了“至少一个开关亮”的或逻辑；若所有输出反相，

## 第58页

则可能把LED亮灭极性理解反了。
DE2-115开发板分析：开发板上拨动任意一个开关，LED状态都应翻转。
若某个开关拨动没有效果，说明该开关输入管脚或位名没有正确分配；若多个
开关组合时不符合真值表，应回到代码确认是否确实使用异或而不是或门。
四、实验体会与讨论
这个任务说明实际生活中的控制问题往往可以转化为真值表和逻辑表达式。
先分析事件行为，再写代码，会比直接试写程序更可靠。
任务四：带延时自动关闭的楼道灯
一、实验目的
1.掌握组合触发和时序延时相结合的设计。
2.理解分频后慢时钟在人眼可观察控制中的作用。
3.练习用计数器实现延时关闭。
二、实验任务及要求
1.在楼道灯基础上增加延时自动关闭。
2.采用Verilog代码输入逻辑功能描述。
3.使用按钮输入，采用时序电路实现延时。
三、实验过程
1.实验设计思路与实现步骤
本任务在组合楼道灯基础上增加“亮灯后延时关闭”。顶层sy4先用clk_div
把50MHz时钟降低，light_delay检测三个按钮异或得到触发信号。触发后灯
点亮并清零延时计数器；若没有新触发，计数器递增，达到设定值后灯自动熄
灭。
实现步骤为：编写分频器；编写延时控制模块，包含触发信号、灯亮状态和
延时计数器；顶层连接KEY输入并考虑按键低有效，所以对子按键取反；编

## 第59页

译后下载到开发板，按下任意楼层按钮观察LED是否亮起并延时熄灭。
源程序清单：clk_div.v
moduleclk_div(
outputclk_out,
inputclk_in,
inputrst_n
);
reg[23:0]cnt;
always@(posedgeclk_inornegedgerst_n)
begin
if(!rst_n)
cnt<=0;
else
cnt<=cnt+1;
end
assignclk_out=cnt[23];
endmodule
源程序清单：light_delay.v
modulelight_delay(
inputclk,//4Hz慢时钟
inputrst_n,//复位
inputS1,S2,S3,//三个按钮
outputreglight//灯输出
);

## 第60页

//三控组合逻辑：任意按钮触发
wiretrigger=S1^S2^S3;
//延时计数器（4Hz下数约4秒）
reg[3:0]delay_cnt;
//状态：灯是否亮
reglight_en;
always@(posedgeclkornegedgerst_n)begin
if(!rst_n)begin
light_en<=0;
delay_cnt<=0;
light<=0;
end
elsebegin
//按任意键→重新亮灯、重新计时
if(trigger)begin
light_en<=1;
delay_cnt<=0;
light<=1;
end
//灯亮中：延时计数

## 第61页

elseif(light_en)begin
delay_cnt<=delay_cnt+1;
light<=1;
//数到15→时间到，关灯
if(delay_cnt==15)begin
light_en<=0;
light<=0;
end
end
//灯灭
elsebegin
light<=0;
end
end
end
endmodule
源程序清单：sy4.v
modulesy4(
inputCLOCK_50,
inputKEY0,//复位
inputKEY1,//S1
inputKEY2,//S2

## 第62页

inputKEY3,//S3
outputLEDR0//灯
);
wireclk_4hz;
//分频
clk_divu_clk(
.clk_in(CLOCK_50),
.rst_n(KEY0),
.clk_out(clk_4hz)
);
//延时灯控制
light_delayu_light(
.clk(clk_4hz),
.rst_n(KEY0),
.S1(~KEY1),//按键低有效，取反
.S2(~KEY2),
.S3(~KEY3),
.light(LEDR0)
);
endmodule

## 第63页

2.实验结果与分析
仿真波形分析：正确波形中，触发信号出现后light立即为1，delay_cnt从
0开始递增；在计数达到阈值前light保持为1，到阈值后变为0。若灯一闪就
灭，说明延时计数阈值过小或light_en没有保持；若灯一直不灭，说明
delay_cnt==15条件没有被满足或计数器没有递增。
DE2-115开发板分析：按下任意KEY后LEDR0应亮起，等待一段时间后
自动熄灭。若按键无效，应检查KEY是低有效还是高有效；若灯亮灭不稳定，
可能是机械按键抖动导致多次触发，可增加消抖逻辑或在SignalTap中观察
trigger。
四、实验体会与讨论
该任务把组合逻辑扩展为时序控制。仅靠异或表达式无法实现“延时”这种时
间行为，必须引入时钟、状态保持和计数器。
任务五：工厂供电控制电路
一、实验目的
1.掌握多输入组合控制逻辑。
2.理解根据请求数量选择不同输出资源的方法。
3.练习用开关和LED显示控制结果。
二、实验任务及要求
1.三个车间各需1KW电力。
2.一个车间工作时由1KW发电机供电，两个车间工作时由2KW发电机供电，
三个车间工作时两台同时供电。
3.用三个开关表示车间请求，用两个LED表示发电机输出。
三、实验过程
1.实验设计思路与实现步骤

## 第64页

设A/B/C表示三个车间请求，Y1表示1KW发电机，Y2表示2KW发电
机。一个或三个请求时Y1为1，因此Y1=AxorBxorC；两个或三个请求时Y2
为1，因此Y2=AB+AC+BC。
实现步骤为：编写核心模块power_ctrl；顶层sy5把SW0-SW2接入A/B/C，
把LEDR0/LEDR1接到Y1/Y2；编译、管脚分配并上板测试所有8种输入组
合。
源程序清单：power_ctrl.v
modulepower_ctrl(
inputA,//车间1
inputB,//车间2
inputC,//车间3
outputY1,//1KW发电机
outputY2//2KW发电机
);
//1KW：奇数个车间工作
assignY1=A^B^C;
//2KW：两个或三个车间工作
assignY2=(A&B)|(A&C)|(B&C);
endmodule
源程序清单：sy5.v
modulesy5(

## 第65页

inputSW0,//车间A
inputSW1,//车间B
inputSW2,//车间C
outputLEDR0,//1KW发电机
outputLEDR1//2KW发电机
);
power_ctrlu1(
.A(SW0),
.B(SW1),
.C(SW2),
.Y1(LEDR0),
.Y2(LEDR1)
);
endmodule
2.实验结果与分析
仿真波形分析：输入001、010、100时应Y1=1,Y2=0；输入011、101、110
时应Y1=0,Y2=1；输入111时应Y1=1,Y2=1；输入000时两者都为0。若两
个请求时两灯都亮，说明Y1逻辑可能写成了或门；若三个请求时只有2KW亮，
说明Y1没有使用异或或没有覆盖奇数请求。
DE2-115开发板分析：拨动三个车间请求开关时，两个LED的亮灭应与供
电策略一致。若仿真正确但板上结果不一致，应检查SW0-SW2与
LEDR0/LEDR1管脚是否对应，以及LED高电平点亮假设是否成立。

## 第66页

四、实验体会与讨论
供电控制任务让我学会把自然语言需求转化为请求数量和逻辑表达式。先列
真值表再化简，可以避免漏掉三个车间同时工作的情况。

## 第67页

《ＥＤＡ技术》试验
实验六
有限状态机设计与实现
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第68页

任务一：1011序列检测器
一、实验目的
1.理解序列检测器的状态定义方法。
2.掌握用parameter编码状态并实现状态转移。
3.练习可重叠序列检测和开发板慢速采样。
二、实验任务及要求
1.检测输入序列中是否出现1011。
2.先仿真，再在开发板上加入使能开关和0.25s采样时钟。
3.检测到完整序列时点亮LEDR0。
三、实验过程
1.实验设计思路与实现步骤
状态定义为：S0未匹配，S1已匹配1，S2已匹配10，S3已匹配101。
当处于S3且当前输入为1时，说明检测到1011。开发板版本增加分频器和
使能输入，避免开关输入变化太快或状态机在未使能时运行。
stateDiagram-v2
[*]-->S0
S0-->S1:din=1
S0-->S0:din=0
S1-->S1:din=1
S1-->S2:din=0
S2-->S3:din=1
S2-->S0:din=0
S3-->S1:din=1/led=1
S3-->S2:din=0

## 第69页

实现步骤为：先画状态图；编写状态寄存器、下一状态组合逻辑和输出逻辑；
仿真输入序列如1011011，检查是否在每次出现1011时输出；再编写sy12.v，
加入4Hz分频、使能开关和开发板LED输出。
源程序清单：sy1.v
modulesy1(
inputclk,
inputrst_n,//同步复位
inputdin,//序列输入
outputregled//检测到1011输出1
);
//状态编码
parameterS0=4'b0001;
parameterS1=4'b0010;
parameterS2=4'b0100;
parameterS3=4'b1000;
reg[3:0]curr_state;
reg[3:0]next_state;
always@(posedgeclk)begin
if(!rst_n)
curr_state<=S0;
else

## 第70页

curr_state<=next_state;
end
always@(*)begin
case(curr_state)
S0:next_state=din?S1:S0;
S1:next_state=din?S1:S2;
S2:next_state=din?S3:S0;
S3:next_state=din?S1:S2;
default:next_state=S0;
endcase
end
always@(*)begin
led=(curr_state==S3&&din==1'b1);
end
endmodule
源程序清单：sy12.v
modulesy12(
inputclk_50m,
inputrst_n,
inputen,
inputdin,

## 第71页

outputledr0
);
reg[22:0]cnt;
regclk_4hz;
always@(posedgeclk_50mornegedgerst_n)begin
if(!rst_n)begin
cnt<=0;
clk_4hz<=0;
end
elseif(cnt==6249999)begin
cnt<=0;
clk_4hz<=~clk_4hz;
end
else
cnt<=cnt+1'd1;
end
parameterS0=4'b0001;
parameterS1=4'b0010;
parameterS2=4'b0100;
parameterS3=4'b1000;

## 第72页

reg[3:0]curr_st;
reg[3:0]next_st;
regled_out;
//时序逻辑
always@(posedgeclk_4hzornegedgerst_n)begin
if(!rst_n)
curr_st<=S0;
elseif(en)
curr_st<=next_st;
end
always@(*)begin
case(curr_st)
S0:next_st=din?S1:S0;
S1:next_st=din?S1:S2;
S2:next_st=din?S3:S0;
S3:next_st=din?S1:S2;
default:next_st=S0;
endcase
end

## 第73页

always@(*)begin
led_out=(curr_st==S3)&&(din==1'b1);
end
assignledr0=led_out;
endmodule
2.实验结果与分析
仿真波形分析：正确波形应在输入最后一位补齐1011的那个周期输出
led=1。例如输入1,0,1,1时，第四位输入为1时输出有效。若输出提前一拍，
说明输出逻辑与状态更新时序没有区分好；若检测不到重叠序列，应检查S3在
输入1时是否回到S1而不是回到S0。
DE2-115开发板分析：开发板上打开使能开关后，通过输入开关按0.25s节
拍输入1、0、1、1，LEDR0应在最后一个1后点亮。若仿真正确但上板不正
确，常见原因是开关输入未同步、采样时钟分频不合适或使能开关没有打开；
可用SignalTap抓取curr_st和din。
四、实验体会与讨论
有限状态机设计最重要的是状态含义清楚。先画状态图再写程序，可以避免
在代码里迷失，尤其是处理可重叠序列时更明显。
任务二：11010序列产生器
一、实验目的
1.掌握序列产生器状态机设计。
2.理解Moore型输出由当前状态决定。
3.练习异步复位下的状态循环。

## 第74页

二、实验任务及要求
1.周期性输出11010序列。
2.包含高电平有效异步复位reset。
3.本题不用上板，仿真即可。
三、实验过程
1.实验设计思路与实现步骤
序列11010有5位，因此设置5个状态S0到S4。状态按固定顺序循环，
输出分别为1、1、0、1、0。复位有效时回到S0，复位释放后每个时钟输出下
一位。
stateDiagram-v2
[*]-->S0
S0-->S1:dout=1
S1-->S2:dout=1
S2-->S3:dout=0
S3-->S4:dout=1
S4-->S0:dout=0
实现步骤为：定义5个状态参数；编写时序逻辑，在posedgeclkorposedge
reset下更新当前状态；编写下一状态组合逻辑形成循环；编写输出组合逻辑，
使每个状态对应一位输出。
源程序清单：sy2.v
modulesy2(
inputclk,
inputreset,
outputregdout

## 第75页

);
//状态定义（5个状态）
parameterS0=3'd0;
parameterS1=3'd1;
parameterS2=3'd2;
parameterS3=3'd3;
parameterS4=3'd4;
reg[2:0]curr_state;//当前状态
reg[2:0]next_state;//下一状态
always@(posedgeclkorposedgereset)begin
if(reset)
curr_state<=S0;//复位→回到初始状态S0
else
curr_state<=next_state;
end
always@(*)begin
case(curr_state)
S0:next_state=S1;
S1:next_state=S2;
S2:next_state=S3;

## 第76页

S3:next_state=S4;
S4:next_state=S0;//最后一位回到S0，循环
default:next_state=S0;
endcase
end
always@(*)begin
case(curr_state)
S0:dout=1'b1;
S1:dout=1'b1;
S2:dout=1'b0;
S3:dout=1'b1;
S4:dout=1'b0;
default:dout=1'b0;
endcase
end
endmodule
2.实验结果与分析
仿真波形分析：复位后第一个状态输出为1，随后每个时钟依次输出1、0、
1、0，再回到1，形成11010周期。若序列变成10110或整体错位，说明复
位初始状态或输出状态对应关系错了；若复位后不回到第一位，应检查异步复
位敏感列表和if(reset)分支。
DE2-115开发板分析：老师要求本题仿真即可，不需要开发板。若要上板观

## 第77页

察，应先分频到低速，再把dout接LED，否则50MHz下输出序列过快，人
眼无法分辨。
四、实验体会与讨论
序列产生器比序列检测器更简单，因为状态转移不依赖外部输入。但它也提
醒我：输出与状态的对应关系必须固定，否则仿真会整体错位。
任务三：8路彩灯控制器
一、实验目的
1.掌握用有限状态机控制LED花型。
2.理解分频后进行人眼可观察显示的必要性。
3.学会在报告中说明自定义彩灯花型。
二、实验任务及要求
1.设计8路彩灯控制器。
2.彩灯花型自定义，并在报告中说明清楚。
3.只需开发板调试，必要时可仿真。
三、实验过程
1.实验设计思路与实现步骤
本设计定义8个状态，LED花型从全亮逐步向中间收缩，再逐步展开。
50MHz时钟经计数分频得到约4Hz慢时钟，状态机在慢时钟下切换花型。
状态 LED花型 说明
S0 11111111 全亮
S1 11100111 中间部分熄灭
S2 11000011 向中间收缩
S3 10000001 两端亮
S4 00011000 中间亮
S5 00111100 向外扩展
S6 01111110 接近全亮
S7 11111111 回到全亮

## 第78页

实现步骤为：编写分频计数器；定义8个状态参数；状态在慢时钟下依次循
环；输出逻辑根据当前状态给出8位LED花型；编译下载到DE2-115并观
察LEDR0-LEDR7。
源程序清单：sy3.v
modulesy3(
inputclk_50m,
inputreset,
outputreg[7:0]led
);
reg[22:0]cnt;
regclk_4hz;
always@(posedgeclk_50morposedgereset)begin
if(reset)begin
cnt<=0;
clk_4hz<=0;
end
elseif(cnt==6249999)begin
cnt<=0;
clk_4hz<=~clk_4hz;
end
else
cnt<=cnt+1'd1;

## 第79页

end
parameterS0=3'd0;
parameterS1=3'd1;
parameterS2=3'd2;
parameterS3=3'd3;
parameterS4=3'd4;
parameterS5=3'd5;
parameterS6=3'd6;
parameterS7=3'd7;
reg[2:0]curr_state;
reg[2:0]next_state;
always@(posedgeclk_4hzorposedgereset)begin
if(reset)
curr_state<=S0;
else
curr_state<=next_state;
end
always@(*)begin
case(curr_state)
S0:next_state=S1;
S1:next_state=S2;

## 第80页

S2:next_state=S3;
S3:next_state=S4;
S4:next_state=S5;
S5:next_state=S6;
S6:next_state=S7;
S7:next_state=S0;
default:next_state=S0;
endcase
end
always@(*)begin
case(curr_state)
S0:led=8'b11111111;
S1:led=8'b11100111;
S2:led=8'b11000011;
S3:led=8'b10000001;
S4:led=8'b00011000;
S5:led=8'b00111100;
S6:led=8'b01111110;
S7:led=8'b11111111;
default:led=8'b00000000;
endcase
end

## 第81页

endmodule
2.实验结果与分析
仿真波形分析：正确波形中curr_state应按S0到S7循环，led应依次输
出表中的8个花型。若LED花型顺序错乱，应检查下一状态逻辑；若花型完
全不变，应检查分频时钟是否翻转或复位是否一直有效。
DE2-115开发板分析：开发板上应看到8个LED以较慢速度按定义花型
变化。若变化太快，说明分频系数过小；若某些LED与预期相反，可能是LED
位序接反，应核对led[7:0]与实际LEDR管脚顺序。
四、实验体会与讨论
彩灯控制器让我体会到状态机不仅能处理序列输入，也能用于周期性输出控
制。报告中明确写出花型表，有助于判断仿真和上板现象是否正确。
任务四：8个数码管循环显示1到8
一、实验目的
1.掌握用有限状态机控制多个显示器件。
2.理解单状态点亮单个数码管的扫描显示思想。
3.练习七段段码与状态输出结合。
二、实验任务及要求
1.在8个数码管上循环显示1到8。
2.每个数字显示约1s。
3.必须用有限状态机实现。
三、实验过程
1.实验设计思路与实现步骤
本任务使用8个状态S0到S7，每个状态只点亮一个数码管并显示对应数
字，其他数码管输出全灭段码。状态机由分频后的慢时钟驱动，使每个数字有

## 第82页

足够显示时间。
实现步骤为：先分频得到慢时钟；定义8个状态；状态按顺序循环；定义数
字1到8的段码和全灭段码；在输出逻辑中先将所有HEX置为全灭，再根
据当前状态点亮对应HEX。
源程序清单：sy4.v
modulesy4(
inputclk_50m,
inputreset,
output[6:0]HEX0,
output[6:0]HEX1,
output[6:0]HEX2,
output[6:0]HEX3,
output[6:0]HEX4,
output[6:0]HEX5,
output[6:0]HEX6,
output[6:0]HEX7
);
reg[22:0]cnt;
regclk_4hz;
always@(posedgeclk_50morposedgereset)begin
if(reset)begin
cnt<=0;

## 第83页

clk_4hz<=0;
end
elseif(cnt==6249999)begin
cnt<=0;
clk_4hz<=~clk_4hz;
end
else
cnt<=cnt+1'd1;
end
parameterS0=3'd0,S1=3'd1,S2=3'd2,S3=3'd3,S4=3'd4,S5=3'd5,S6=3'd6,S7=3'd7;
reg[2:0]curr_st;
reg[2:0]next_st;
always@(posedgeclk_4hzorposedgereset)begin
if(reset)
curr_st<=S0;
else
curr_st<=next_st;
end
always@(*)begin
case(curr_st)
S0:next_st=S1;

## 第84页

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
parameter
NUM1=7'h79,NUM2=7'h24,NUM3=7'h30,NUM4=7'h19,NUM5=7'h12,NUM6=
7'h02,NUM7=7'h78,NUM8=7'h00,OFF=7'h7F;
reg[6:0]h0,h1,h2,h3,h4,h5,h6,h7;
always@(*)begin
h0=OFF;h1=OFF;h2=OFF;h3=OFF;h4=OFF;h5=OFF;h6=OFF;h7=OFF;
case(curr_st)
S0:h0=NUM1;
S1:h1=NUM2;
S2:h2=NUM3;
S3:h3=NUM4;
S4:h4=NUM5;

## 第85页

S5:h5=NUM6;
S6:h6=NUM7;
S7:h7=NUM8;
default:;
endcase
end
assignHEX0=h0;
assignHEX1=h1;
assignHEX2=h2;
assignHEX3=h3;
assignHEX4=h4;
assignHEX5=h5;
assignHEX6=h6;
assignHEX7=h7;
endmodule
2.实验结果与分析
仿真波形分析：正确波形中curr_st每个慢时钟切换一次，且任意时刻只有
一个HEX输出不是OFF。例如S0时HEX0显示1，S1时HEX1显示2，
直到S7时HEX7显示8。若多个数码管同时亮，说明输出逻辑没有先清空所
有HEX；若数字与位置错位，应检查状态和HEX的对应关系。
DE2-115开发板分析：开发板上应看到数字1到8在8个数码管上依次
循环出现。若所有数码管都暗，可能是段码全灭值或复位信号错误；若显示太

## 第86页

快，应调大分频系数。
四、实验体会与讨论
这个任务训练了“默认关闭，再按状态打开一个输出”的写法。多输出状态机
如果不先给默认值，容易产生锁存或多个输出残留。
任务五：交通灯30秒倒计时器（选做）
一、实验目的
1.练习倒计时计数器设计。
2.掌握BCD借位和七段显示。
3.理解交通灯倒计时系统的核心计时模块。
二、实验任务及要求
1.实现30秒倒计时。
2.采用两个七段数码管显示倒计时结果。
3.复位后从30开始递减到00。
三、实验过程
1.实验设计思路与实现步骤
本设计用1Hz慢时钟驱动两个BCD位。复位后高位为3、低位为0；每
秒低位减1；当低位为0时借位，高位减1，低位置9；到00后保持00。
实现步骤为：对50MHz时钟分频得到1Hz；定义sec_high和sec_low；编
写倒计时借位逻辑；编写两个七段译码case；分配两个HEX管脚；上板观察30
到00的变化。
源程序清单：sy5.v
modulesy5(
inputclk_50m,
inputreset,

## 第87页

output[6:0]HEX1,
output[6:0]HEX0
);
reg[24:0]cnt;
regclk_1hz;
always@(posedgeclk_50morposedgereset)begin
if(reset)begin
cnt<=0;
clk_1hz<=0;
end
elseif(cnt==24999999)begin
cnt<=0;
clk_1hz<=~clk_1hz;
end
else
cnt<=cnt+1'd1;
end
reg[3:0]sec_high;
reg[3:0]sec_low;
always@(posedgeclk_1hzorposedgereset)begin

## 第88页

if(reset)begin
sec_high<=4'd3;
sec_low<=4'd0;
end
elseif({sec_high,sec_low}==8'd0)begin
sec_high<=4'd0;
sec_low<=4'd0;
end
elseif(sec_low==4'd0)begin
sec_low<=4'd9;
sec_high<=sec_high-1'd1;
end
elsebegin
sec_low<=sec_low-1'd1;
end
end
reg[6:0]seg1,seg0;
always@(*)begin
case(sec_high)
4'd0:seg1=7'h40;
4'd1:seg1=7'h79;
4'd2:seg1=7'h24;

## 第89页

4'd3:seg1=7'h30;
default:seg1=7'h7F;
endcase
end
always@(*)begin
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
assignHEX1=seg1;
assignHEX0=seg0;

## 第90页

endmodule
2.实验结果与分析
仿真波形分析：正确波形应从30开始，每个1Hz周期变为29、28...01、
00，并在00保持。若从30直接变为39，说明借位条件写反；若00后又变
为99，说明到0保持的条件缺失；若计时速度不准确，应检查分频计数阈值
是否与50MHz对应。
DE2-115开发板分析：开发板上两个数码管应显示稳定倒计时。若显示乱码，
应检查seg1/seg0的段码；若倒计时肉眼看起来过快或过慢，应检查
cnt==24999999的翻转方式是否得到实际1Hz更新节拍。
四、实验体会与讨论
倒计时器的关键是边界处理。和普通加法计数器相比，减法借位更容易出错，
所以必须重点仿真30、29、20、10、00等关键点。

## 第91页

《ＥＤＡ技术》试验
实验七
复杂系统设计与实现1
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第92页

任务一：32位超前进位加法器
一、实验目的
1.理解超前进位加法器的产生/传播逻辑。
2.掌握从小位宽模块逐级扩展到32位的方法。
3.练习复杂组合系统的层次化设计与仿真分析。
二、实验任务及要求
1.设计32位超前进位加法器。
2.输入为a[31:0]、b[31:0]和ci，输出为s[31:0]与co。
3.要求能讲清楚分层设计思路。
三、实验过程
1.实验设计思路与实现步骤
超前进位加法器的核心是为每一位产生g=a&b和传播p=a|b，再用组进位模
块提前计算高位需要的进位。设计从1位add开始，组合成2位cla_2、4位
cla_4，再在顶层中定义8位、16位、32位结构。这样能减少串行进位带来的
延迟。
实现步骤为：先验证1位加法单元；编写g_p组进位公式；逐级例化构造2
位和4位CLA；在sy78.v中继续构造8位、16位和32位；仿真选取普通
加法、带进位加法、全1溢出等测试样例，检查s和co。
源程序清单：add.v
moduleadd(
inputa,
inputb,
inputc,
outputg,

## 第93页

outputp,
outputs
);
assigns=a^b^c;
assigng=a&b;
assignp=a|b;
endmodule
源程序清单：g_p.v
moduleg_p(
input[1:0]g,
input[1:0]p,
inputc_in,
outputg_out,
outputp_out,
outputc_out
);
assigng_out=g[1]|(p[1]&g[0]);
assignp_out=p[1]&p[0];
assignc_out=g[0]|(p[0]&c_in);
endmodule
源程序清单：cla_2.v
modulecla_2(
input[1:0]a,
input[1:0]b,

## 第94页

inputc_in,
outputg_out,
outputp_out,
output[1:0]s
);
wire[1:0]g,p;
wirec_out;
addadd0(.a(a[0]),.b(b[0]),.c(c_in),.g(g[0]),.p(p[0]),.s(s[0]));
addadd1(.a(a[1]),.b(b[1]),.c(c_out),.g(g[1]),.p(p[1]),.s(s[1]));
g_pg_p0(.g(g),.p(p),.c_in(c_in),.g_out(g_out),.p_out(p_out),.c_out(c_out));
endmodule
源程序清单：cla_4.v
modulecla_4(
input[3:0]a,
input[3:0]b,
inputc_in,
outputg_out,
outputp_out,
output[3:0]s
);
wire[1:0]g,p;
wirec_out;

## 第95页

cla_2 cla0
(.a(a[1:0]),.b(b[1:0]),.c_in(c_in),.g_out(g[0]),.p_out(p[0]),.s(s[1:0]));
cla_2 cla1
(.a(a[3:2]),.b(b[3:2]),.c_in(c_out),.g_out(g[1]),.p_out(p[1]),.s(s[3:2]));
g_pg_p0(.g(g),.p(p),.c_in(c_in),.g_out(g_out),.p_out(p_out),.c_out(c_out));
endmodule
源程序清单：sy78.v
modulesy78(
input[31:0]a,
input[31:0]b,
inputci,
output[31:0]s,
outputco
);
wireg_out,p_out;
cla_16 cla0
(.a(a[15:0]),.b(b[15:0]),.c_in(ci),.g_out(g_out0),.p_out(p_out0),.s(s[15:0]));
cla_16 cla1
(.a(a[31:16]),.b(b[31:16]),.c_in(c_out1),.g_out(g_out1),.p_out(p_out1),.s(s[31:
16]));

## 第96页

g_pg_p1(.g({g_out1,g_out0}),.p({p_out1,p_out0}),.c_in(ci),
.g_out(g_out),.p_out(p_out),.c_out(c_out1));
assignco=g_out|(p_out&ci);
endmodule
//下面是内部用到的8/16位模块，直接放在顶层文件最下面即可
modulecla_8(
input[7:0]a,
input[7:0]b,
inputc_in,
outputg_out,
outputp_out,
output[7:0]s
);
wire[1:0]g,p;
wirec_out;
cla_4 cla0
(.a(a[3:0]),.b(b[3:0]),.c_in(c_in),.g_out(g[0]),.p_out(p[0]),.s(s[3:0]));
cla_4 cla1
(.a(a[7:4]),.b(b[7:4]),.c_in(c_out),.g_out(g[1]),.p_out(p[1]),.s(s[7:4]));
g_pg_p0(.g(g),.p(p),.c_in(c_in),.g_out(g_out),.p_out(p_out),.c_out(c_out));
endmodule

## 第97页

modulecla_16(
input[15:0]a,
input[15:0]b,
inputc_in,
outputg_out,
outputp_out,
output[15:0]s
);
wire[1:0]g,p;
wirec_out;
cla_8 cla0
(.a(a[7:0]),.b(b[7:0]),.c_in(c_in),.g_out(g[0]),.p_out(p[0]),.s(s[7:0]));
cla_8 cla1
(.a(a[15:8]),.b(b[15:8]),.c_in(c_out),.g_out(g[1]),.p_out(p[1]),.s(s[15:8]));
g_pg_p0(.g(g),.p(p),.c_in(c_in),.g_out(g_out),.p_out(p_out),.c_out(c_out));
endmodule

## 第98页

图：32位超前进位加法器仿真结果一
图：32位超前进位加法器仿真结果二
2.实验结果与分析
仿真波形分析：正确结果应满足{co,s}=a+b+ci。例如a=0、b=0、ci=1时s=1；
a=32'hFFFF_FFFF、b=1、ci=0时s=0且co=1。截图中若不同测试向量的和与

## 第99页

数学加法一致，则说明分层进位链正确。若低16位正确而高16位错误，应
重点检查c_out1是否正确传入高16位；若所有高层进位错误，应检查g_p的
组产生和组传播公式。
DE2-115开发板分析：32位输入输出位数较多，不适合直接完整接到开关
和LED，主要通过仿真验证。若需要硬件调试，可选择低位子集或用SignalTap
观察内部g/p/c_out，避免仅凭少量LED判断完整32位功能。
四、实验体会与讨论
这个任务让我体会到复杂组合电路必须分层设计。只要每一级模块接口清楚，
就能把1位加法逐步扩展到32位，并且仿真时也能按层定位问题。

## 第100页

《ＥＤＡ技术》试验
实验八
复杂系统设计与实现2
专业：计算机科学与技术
姓名：李尚凯
学号：2024317220214
班级：计科2401班
报告撰写时间：2026年5月26日

## 第101页

任务一：IPRAM方式实现1024x8RAM字扩展
一、实验目的
1.理解RAM字扩展的地址划分。
2.掌握用2-4译码器产生片选信号。
3.练习调用多片256x8RAM组成更大容量存储器。
二、实验任务及要求
1.将4片256x8RAM扩展成1024x8RAM。
2.高2位地址选择RAM片，低8位地址访问片内单元。
3.给出仿真波形，检查读写是否正确。
三、实验过程
1.实验设计思路与实现步骤
1024个地址需要10位地址。字扩展时，addr[9:8]用来选择4片RAM中
的一片，addr[7:0]作为片内地址。2-4译码器输出低有效片选cs_n，写使能为
wren&~cs_n[i]，保证任意时刻只有被选中的RAM被写入。读出时根据片选
从q0-q3中选择一路送到dout。
实现步骤为：编写2-4译码器；用QuartusIP生成256x8RAM；顶层例化
4片RAM；连接共同的数据输入和片内地址；按片选控制写使能；仿真时分别
向不同高位地址写入不同数据，再读出检查。
源程序清单：decoder_2to4.v
moduledecoder_2to4(
input[1:0]a,
outputreg[3:0]y_n
);
always@(*)begin

## 第102页

case(a)
2'b00:y_n=4'b1110;
2'b01:y_n=4'b1101;
2'b10:y_n=4'b1011;
2'b11:y_n=4'b0111;
endcase
end
endmodule
源程序清单：sy8.v
modulesy8(
inputclk,
inputwren,//1写0读
input[9:0]addr,//10位地址
input[7:0]din,//写入数据
output[7:0]dout//读出数据
);
wire[3:0]cs_n;
wire[7:0]q0,q1,q2,q3;
//2-4译码器：高2位做片选
decoder_2to4u_dec(
.a(addr[9:8]),
.y_n(cs_n)

## 第103页

);
//4片256x8RAM，低位地址并联，片选独立
ram_256x8u_ram0(
.clock(clk),
.address(addr[7:0]),
.data(din),
.wren(wren&~cs_n[0]),
.q(q0)
);
ram_256x8u_ram1(
.clock(clk),
.address(addr[7:0]),
.data(din),
.wren(wren&~cs_n[1]),
.q(q1)
);
ram_256x8u_ram2(
.clock(clk),
.address(addr[7:0]),
.data(din),
.wren(wren&~cs_n[2]),
.q(q2)
);

## 第104页

ram_256x8u_ram3(
.clock(clk),
.address(addr[7:0]),
.data(din),
.wren(wren&~cs_n[3]),
.q(q3)
);
//输出根据片选选通对应RAM的q
assigndout=(~cs_n[0])?q0:
(~cs_n[1])?q1:
(~cs_n[2])?q2:q3;
endmodule

## 第105页

图：IPRAM写入仿真结果

## 第106页

图：IPRAM读出仿真结果
2.实验结果与分析
仿真波形分析：正确波形中，当addr[9:8]=00时只有第0片RAM写使能
有效；01/10/11分别选择第1/2/3片。写入后切换到读操作，dout应等于先前
写入该地址的数据。若读出总是来自同一片，说明输出多路选择条件错误；若
多个RAM同时被写，说明片选译码或写使能与片选的与逻辑错误。
DE2-115开发板分析：RAM扩展不适合完全通过开关手动验证1024个地
址，推荐用仿真和SignalTap。若上板测试，可选少量地址和数据，通过开关输
入地址/数据、LED或数码管显示读出值，重点验证跨256边界的地址，如255、
256、511、512。
四、实验体会与讨论

## 第107页

RAM字扩展的关键是地址高低位分工。高位决定选片，低位决定片内地址；
只要片选和写使能设计正确，容量扩展就比较自然。
任务二：手写RAM方式实现1024x8RAM字扩展
一、实验目的
1.通过Verilog数组理解RAM的基本行为。
2.对比手写RAM与IPRAM的接口差异。
3.进一步巩固字扩展顶层连接方法。
二、实验任务及要求
1.自行写256x8RAM模块。
2.继续用2-4译码器和4片RAM组成1024x8RAM。
3.仿真验证读写数据是否正确。
三、实验过程
1.实验设计思路与实现步骤
手写方案中，ram_256x8使用reg[7:0]mem[0:255]建立存储阵列，在时钟
上升沿且wren=1时写入数据，读出端直接返回mem[addr]。顶层sy82与IP
方案相同，仍使用高2位地址片选和低8位片内地址。
实现步骤为：编写RAM数组模块；编写或复用2-4译码器；顶层例化4个
RAM；分别连接片选写使能；用多组地址写入和读出仿真。手写RAM便于理
解读写行为，但真实FPGA综合时仍需关注综合工具是否能推断为块RAM。
源程序清单：decoder_2to4.v
moduledecoder_2to4(
input[1:0]a,//高位地址addr[9:8]
output[3:0]y_n//低有效片选0选中
);

## 第108页

reg[3:0]y_n_reg;
always@(*)begin
case(a)
2'b00:y_n_reg=4'b1110;
2'b01:y_n_reg=4'b1101;
2'b10:y_n_reg=4'b1011;
2'b11:y_n_reg=4'b0111;
endcase
end
assigny_n=y_n_reg;
endmodule
源程序清单：ram_256x8.v
moduleram_256x8(
inputclk,
inputwren,//1=写0=读
input[7:0]addr,//8位地址0~255
input[7:0]din,//8位数据输入
output[7:0]dout//8位数据输出
);
reg[7:0]mem[0:255];//256个8位存储单元

## 第109页

always@(posedgeclk)begin
if(wren)
mem[addr]<=din;//写操作
end
assigndout=mem[addr];//读操作
endmodule
源程序清单：sy82.v
modulesy82(
inputclk,
inputwren,//总写使能
input[9:0]addr,//10位地址0~1023
input[7:0]din,//写入数据
output[7:0]dout//读出数据
);
wire[3:0]cs_n;
wire[7:0]q0,q1,q2,q3;
//2-4译码器：高2位地址产生片选
decoder_2to4u_dec(
.a(addr[9:8]),
.y_n(cs_n)

## 第110页

);
//4片256×8RAM，字扩展
ram_256x8u_ram0(
.clk(clk),
.wren(wren&~cs_n[0]),//只有选中才写
.addr(addr[7:0]),
.din(din),
.dout(q0)
);
ram_256x8u_ram1(
.clk(clk),
.wren(wren&~cs_n[1]),
.addr(addr[7:0]),
.din(din),
.dout(q1)
);
ram_256x8u_ram2(
.clk(clk),
.wren(wren&~cs_n[2]),
.addr(addr[7:0]),
.din(din),

## 第111页

.dout(q2)
);
ram_256x8u_ram3(
.clk(clk),
.wren(wren&~cs_n[3]),
.addr(addr[7:0]),
.din(din),
.dout(q3)
);
//输出选择
assigndout=(~cs_n[0])?q0:
(~cs_n[1])?q1:
(~cs_n[2])?q2:q3;
endmodule
2.实验结果与分析
仿真波形分析：写操作应在posedgeclk后生效，因此读出数据可能在写入
边沿之后才稳定。正确波形应显示同一地址写入后再次读出能得到相同数据，
不同高位地址互不影响。若读出的数据全为X，可能是仿真中没有先写入该地
址；若写入一个地址影响另一片RAM，说明片选写使能没有正确限制。
DE2-115开发板分析：手写RAM上板后与IP方案现象应一致。若仿真通
过但综合后资源异常，应检查RAM写读风格是否能被Quartus推断为存储器；

## 第112页

若开发板读写不稳定，应增加明确的写入按键同步和消抖，避免一次按键造成
多次写入。
四、实验体会与讨论
手写RAM方案让我从代码层面理解存储器行为。与IP方案相比，它更直
观，但工程化使用时仍要考虑综合结果和时序稳定性。
总结
本报告按每个实验任务分别整理，尽量做到每个任务都能独立说明目的、要
求、设计过程、仿真分析、开发板分析和体会。八次实验从Quartus入门、组
合逻辑、时序逻辑、层次化设计、有限状态机，逐步过渡到超前进位加法器和
RAM字扩展。整体来看，正确的实验流程应是：先读懂任务并画出逻辑关系，
再编写或搭建模块，之后通过仿真验证关键边界，最后结合DE2-115管脚、下
载和SignalTap做硬件分析。若仿真和开发板结果不一致，应优先区分代码逻
辑错误、管脚分配错误、时钟/复位错误和硬件观察方式错误。
任务三：附加题1供电控制电路
一、实验目的
1.掌握三输入组合控制电路的逻辑分析方法。
2.理解按用电请求数量自动选择甲、乙供电站的控制策略。
3.练习用拨动开关表示请求、用LED表示输出结果。
二、实验任务及要求
1.三个工厂分别用一个开关表示用电请求。
2.一个工厂用电时由甲站供电，两个工厂用电时由乙站供电，三个工厂用电时
甲、乙两站同时供电。
3.用两个LED显示甲站和乙站供电结果，并完成仿真验证。
三、实验过程

## 第113页

1.实验设计思路与实现步骤
设F0、F1、F2表示三个工厂用电请求，JIA表示甲站供电，YI表示乙站
供电。一个或三个请求时甲站输出有效；两个或三个请求时乙站输出有效。因
此乙站逻辑为两两相与后相或，甲站逻辑采用奇偶关系并补充三请求情况。实
现时建立fj1顶层模块，将F0-F2接入组合逻辑，JIA/YI输出到LED。
源程序清单：fj1.v
//供电控制电路顶层模块
modulefj1(
inputwireF0,//工厂0用电请求
inputwireF1,//工厂1用电请求
inputwireF2,//工厂2用电请求
outputwireJIA,//甲站供电LED
outputwireYI//乙站供电LED
);
//逻辑实现
assignJIA=(F2^F1^F0)|(F2&F1&F0);
assignYI=(F2&F1)|(F2&F0)|(F1&F0);
endmodule
测试激励文件中例化名写成了power_control，而当前顶层模块名为fj1；若使
用该测试文件，应将例化模块名改为fj1后再进行ModelSim仿真。
//测试激励文件
moduletb_power_control;

## 第114页

regF0,F1,F2;
wireJIA,YI;
//例化顶层模块
power_controluut(
.F0(F0),
.F1(F1),
.F2(F2),
.JIA(JIA),
.YI(YI)
);
//生成测试序列
initialbegin
//初始化
F0=0;F1=0;F2=0;#10;
//1个工厂用电
F0=1;F1=0;F2=0;#10;
F0=0;F1=1;F2=0;#10;
F0=0;F1=0;F2=1;#10;
//2个工厂用电
F0=1;F1=1;F2=0;#10;
F0=1;F1=0;F2=1;#10;

## 第115页

F0=0;F1=1;F2=1;#10;
//3个工厂用电
F0=1;F1=1;F2=1;#10;
//结束
$stop;
end
endmodule
图：附加题1供电控制仿真结果
2.实验结果与分析
仿真波形分析：输入001、010、100时应只有JIA为1；输入011、101、
110时应只有YI为1；输入111时JIA和YI同时为1；输入000时两者
均为0。截图中若输出符合这个真值表，说明逻辑正确。若两个工厂请求时甲
站也亮，应检查JIA是否错误写成简单或门；若三个请求时甲站不亮，应检查

## 第116页

三输入同时为1的项是否被覆盖。
DE2-115开发板分析：上板时三个拨动开关表示三个工厂请求，两个LED
分别表示甲、乙站。若仿真正确但LED结果不一致，应优先检查开关位序和
LED管脚分配。
四、实验体会与讨论
该任务的关键是先列真值表，再化简逻辑表达式。自然语言中的“一个、两个、
三个请求”如果不转化为输入组合，很容易漏掉111这种边界情况。
任务四：附加题2BCD判偶电路
一、实验目的
1.理解BCD码最低位与奇偶性的关系。
2.掌握简单组合逻辑的直接表达方法。
3.练习用仿真波形验证0到9的奇偶判断。
二、实验任务及要求
1.输入4位BCD码。
2.当输入表示偶数时输出Y为1。
3.完成仿真并分析输出是否符合0、2、4、6、8为偶数的规律。
三、实验过程
1.实验设计思路与实现步骤
BCD码中最低位D决定数值奇偶性：D=0表示偶数，D=1表示奇数。因
此判偶输出可写成Y=~D。实现步骤是建立fj2模块，声明A、B、C、D四
位输入和输出Y，使用连续赋值实现最低位取反。
//BCD判偶电路附加题2
modulefj2(
inputwireA,

## 第117页

inputwireB,
inputwireC,
inputwireD,
outputwireY
);
assignY=~D;//最低位取反就是判偶输出
endmodule
图：BCD判偶仿真结果
2.实验结果与分析
仿真波形分析：当输入为0000、0010、0100、0110、1000时，D=0，Y应
为1；当输入为0001、0011、0101、0111、1001时，D=1，Y应为0。若波
形满足该关系，说明判偶逻辑正确。若结果反相，则应检查是否误写成Y=D。

## 第118页

DE2-115开发板分析：上板时拨动开关输入BCD值，LED输出Y。偶数
输入LED亮，奇数输入LED灭。若高位开关变化影响了结果，说明代码中
不应引入A/B/C参与判偶。
四、实验体会与讨论
这个任务说明不是所有组合逻辑都需要复杂化简。抓住最低位决定奇偶性的
规律后，电路可以非常简洁。
任务五：附加题3BCD判奇电路
一、实验目的
1.理解奇数判断与BCD最低位的关系。
2.掌握判奇电路的最简逻辑实现。
3.对比判奇与判偶电路的互补关系。
二、实验任务及要求
1.输入4位BCD码。
2.当输入表示奇数时输出Y为1。
3.通过仿真验证1、3、5、7、9输出有效。
三、实验过程
1.实验设计思路与实现步骤
BCD码最低位D=1时表示奇数，因此判奇输出直接等于D。建立fj3模
块后，用连续赋值assignY=D;即可实现该功能。
modulefj3(
inputwireA,
inputwireB,
inputwireC,

## 第119页

inputwireD,
outputwireY
);
assignY=D;//最低位=1就是奇数，直接输出
endmodule
图：BCD判奇仿真结果
2.实验结果与分析
仿真波形分析：输入0001、0011、0101、0111、1001时Y应为1；输入0000、
0010、0100、0110、1000时Y应为0。若波形与最低位D完全一致，说明结
果正确。若Y与D相反，应检查是否误用了判偶表达式。
DE2-115开发板分析：开发板上奇数输入时LED应点亮，偶数输入时熄灭。
若显示异常，主要检查最低位开关D是否接到预期管脚。

## 第120页

四、实验体会与讨论
判奇电路进一步说明了逻辑设计要先寻找本质变量。该题中高三位只决定数
值大小，不决定奇偶性。
任务六：附加题4组合逻辑函数实现
一、实验目的
1.练习由逻辑表达式直接建立组合电路。
2.掌握与、或、非混合表达式的Verilog连续赋值写法。
3.通过仿真确认表达式覆盖的输入条件。
二、实验任务及要求
1.输入A、B、C、D四个逻辑变量。
2.实现输出Y=(~A&~B)|(~A&~C&~D)。
3.通过仿真波形检查所有关键输入组合。
三、实验过程
1.实验设计思路与实现步骤
该任务直接由给定表达式实现。表达式可理解为A=0且B=0时输出有效，
或者A=0、C=0、D=0时输出有效。实现时注意非运算、与运算和或运算的优
先级，用括号明确逻辑关系。
modulefj4(
inputwireA,
inputwireB,
inputwireC,
inputwireD,
outputwireY

## 第121页

);
assignY=(~A&~B)|(~A&~C&~D);
endmodule
图：附加题4仿真结果
2.实验结果与分析
仿真波形分析：当A=0、B=0时，无论C/D如何变化，第一项使Y=1；当
A=0、C=0、D=0时，第二项使Y=1。其他不满足条件的输入组合Y应为0。
若仿真中A=1时仍出现Y=1，应检查表达式中的~A是否漏写；若B、C、D
条件混乱，应检查括号。
DE2-115开发板分析：上板时四个开关表示A-D，LED表示Y。因为组合
数较多，建议重点测试表达式应为1的组合和几个应为0的反例组合。
四、实验体会与讨论

## 第122页

直接表达式实现虽然简单，但括号非常重要。写组合逻辑时保持表达式和真
值表一致，可以减少优先级造成的误解。
任务七：附加题5组合逻辑函数化简实现
一、实验目的
1.掌握化简后的组合逻辑表达式实现方法。
2.理解输出条件A|(B&D)的含义。
3.练习用仿真验证化简表达式。
二、实验任务及要求
1.输入A、B、C、D四个变量。
2.实现最简逻辑Y=A|(B&D)。
3.完成仿真并分析不同输入组合下输出是否正确。
三、实验过程
1.实验设计思路与实现步骤
化简后的表达式表明，只要A=1，Y必为1；当A=0时，需要B和D同
时为1，Y才为1。变量C不影响最终输出，因此代码中不需要使用C。实
现时保留C作为输入端口，是为了与题目四变量输入保持一致。
modulefj5(
inputwireA,
inputwireB,
inputwireC,
inputwireD,
outputwireY
);

## 第123页

//最简逻辑实现
assignY=A|(B&D);
endmodule
图：附加题5仿真结果
2.实验结果与分析
仿真波形分析：所有A=1的组合Y都应为1；当A=0时，只有B=1且
D=1时Y=1，其余组合Y=0。若C的变化导致Y变化，说明代码错误地引
入了C；若A=1时Y不稳定，应检查或运算项是否写错。
DE2-115开发板分析：开发板上可先固定A=1，观察LED是否恒亮；再令
A=0，测试B/D组合。若LED与C开关相关，则说明设计没有正确使用化
简表达式。
四、实验体会与讨论

## 第124页

该任务体现了逻辑化简的价值。化简后C不再参与输出，硬件资源更少，
仿真和排错也更容易。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
