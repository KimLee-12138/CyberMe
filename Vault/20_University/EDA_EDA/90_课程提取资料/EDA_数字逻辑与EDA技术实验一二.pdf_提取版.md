---
id: extract-eda-eec7b07f
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/PDF/EDA_数字逻辑与EDA技术实验一二.pdf_课件_未知日期_eec7b07f.pdf]]"
source_pages: all
source_hash: "eec7b07fc40a31527df79cfa8efe704ad85824e2ce4267c61844e3be5dd0542f"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 数字逻辑与EDA技术实验一二.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

1数字逻辑与EDA技术实验指导书
重要注意事项：
1.请大家务必要爱惜实验箱和开发板，在实验时，可把实验箱的盖子取下，不要
不要不要将开发板从实验箱中取出来，电源适配器也不要从箱子中取出，可从箱
子外侧插入适配器的线。每次实验课结束时，要把实验箱中的各部件（下载电缆，
电源线等）收拾好归位。
2.每次实验课完成后，要好好体会课堂所学内容，以达到熟练掌握和深刻理解的
程度！因为实验课是循序渐进、难度和内容递增的，前一次实验真正理解和掌
握了，后面的实验才容易开展，否则后面的实验课将会难以开展。
3.以后的实验课（第2-8次实验课）请大家务必在实验课前提前预习准备，否则
课堂上难以完成任务。以后的实验课不再集中讲解，大家到实验室就开始自行
按照实验任务做实验。课堂上若有没完成的实验任务，请课后自行找时间到实
验室补做完成。
4.每次实验课前务必完成上一次课的实验报告，注意保存好实验报告电子档，最
后一次实验结束后一个星期内提交所有实验报告，要求将所有8次实验的实验
报告电子版按顺序（实验一、实验二、实验三……实验八）集中到一个文件中，
并上传到itc系统。
5.建议对FPGA实验箱或开发板使用不熟练的同学，每次使用前看看本实验指导
书0前言部分的内容。
0前言
0实验硬件及使用说明
实验箱名称：
FGPA/SoC实验箱套件（箱子是白色的）
说明：每次使用开发板之前，必须要做几件事：（1）安装驱动—装下载电
缆usbblaster的驱动；（2）器件选择—在quartusII14.0中先选择芯片
EP4CE115F29C7；（3）器件管脚分配
0.1usbblaster驱动安装方法（说明，实验室电脑驱动已装好，用机房电脑做实
验，此步可忽略）
注意：在用de2-115开发板之前必须要装usbblaster的驱动，安装usbblaster
驱动之前先要用usbblaster线缆把实验箱与电脑连起来，并接通电源）
usbblaster的驱动安装方法：计算机——属性——设备管理器（或我的电脑
——属性——硬件——设备管理器）在有叹号的usbblaster上单击右键。
usbblaster驱动的位置在quartus的安装目录下：
C:\altera\14.0\quartus\drivers\usb-blaster（说明：也可在quartus14.0的安
装路径下找到drivers文件夹，然后再找到usb-blaster。）
0.2器件选择
可编程芯片：DE2-115开发板上有一款可编程芯片EP4CE115F29C7,该芯片
是CycloneIVE系列的，speedgrade为7。使用开发板时，打开quartusII14.0软
件的菜单Assignments->Device进行器件选择，如图7。（注意：选择芯片时请
认准EP4CE115F29C7，一个字符都不能错，否则无法下载。）

## 第2页

2
图7
芯片选好后，可在quartusII14.0的项目管理窗口看到所有芯片系列和名称（请检
查一下芯片名称，如果选错了要重新选、然后再编译），如图8所示
图8
0.3管脚分配方法（管脚分配时需要参考DE2-115中文说明书的第4章内容）
管脚分配有以下4种方法，一般采用第一种方法。管脚分配完成后，可打开
Assignment->PinPlanner，看看管脚是否确实已经分配好。
方法一.使用程序设计语言写，格式如下所示：
(*chip_pin="Y2"*)inputclk50m;
(*chip_pin="AB28"*)inputreset;
(*chip_pin="H22,J22,L25,L26,E17,F22,G18"*)outputreg[6:0]out1;
（注意1位信号的管脚分配只能一个一个的定义分配；多位信号的管脚分配可以
一起分配）
方法二、QuartusII14.0中，用Assignment->PinPlanner中一个一个分配；
方法三、新建一个pin.tcl文件，用记事本打开，按照固定格式写好管脚分配后，
在QII软件中，使用“Tools——TclScripts”标签打开TclScripts，选择pin.tcl，选
择“Run”标签，执行Tcl文件。
语句格式：set_location_assignmentPIN_Y2-toclock_50
注释用#开始，写在#后面。
方法四，直接在编译生成的qsf文件中添加。
说明：管脚分配完成后，可打开Assignment->PinPlanner，检查管脚是否已经
按照自己的期望分配好。

## 第3页

3实验一、二QuartusII软件和DE2-115开
发板使用入门（8学时）-----实验一、实验二
注意：每次实验每个实验任务在E盘新建一个文件夹，然后新建一个工程放在
这个新文件夹内！即每个工程必须在自己的一个单独的文件夹中，千万不要把不
同的工程放在一个文件夹！
一个实验任务完成后，关闭当前工程，然后再新建文件夹，新建工程，重复第一
个任务的步骤。
实验目标：熟悉QuartusII开发环境，掌握原理图输入方式、文本输入方式和波
形仿真；熟练掌握在QuartusII环境中进行FPGA设计的流程；熟悉DE2-115
开发板及其使用；
实验任务：
任务一、熟悉QuartusII开发环境，掌握原理图输入方式，在QuartusII中用
原理图方式实现半加器，并用QuartusII14.0中的波形仿真。仿真成功后，生
成半加器图形符号以供后续程序调用；----本题不需要用FPGA实验箱。
操作步骤：
（1）在开始菜单中打开quartusII14.0软件。
（2）在E盘新建一个名为sy11的文件夹。
（3）新建一个工程：在quartusII14.0软件中，单击File菜单，选择“NewProject
Wizard菜单项，单击next，出现如下对话框，选择工程所在文件夹并输
入工程名后单击finish。
（4）新建文件：在quartusII14.0软件中，单击File菜单，选择New菜单项，
弹出如下的窗口，选择BlockDiagram/SchematicFile(原理图输入方式)后单击
ok按钮。

## 第4页

4
（5）在画布上画出电路图：在画布上双击鼠标左键，弹出Symbol对话框，
单击左侧libraries下最左侧那个三角形，并单击primitives左侧的三角形和logic
左侧的三角形，如下图所示。双击and2，并在画布中单击左键确定（OK按钮），
则and2出现在画布上，同理将xnor和not符号放在画布上，然后将单击logic
左侧的减号，并单击pin左侧的加号，双击input，将输入端口放到画布上，然后
双击output，将输出端口放到画布上。然后在画布的input上单击右键，选择copy，
在画布的空白处点击paste。同理放output管脚。双击各管脚，将其pinname分
别改成a，b，sum，cout。然后单击左侧的橡皮筋
按钮，将鼠标移动到右侧
画布上的某个器件的管脚处时鼠标变成橡皮筋按钮的形状，此时可进行连线。

## 第5页

5
注意：在联线过程中，不得出现多余的链接点（该图只有两个链接点，凡是因
线没连好而出现的多余的链接点要删掉，可按下鼠标左键并移动选中多余的线
和点，然后单击键盘上的delete键即可删除），图中也不得出现带有叉的断头
线，否则编译会出错。连线结果如下：（半加器也可用教材P43页图3.6）
（6）保存文件，文件名保存为sy11.bdf（注意扩展名为bdf）
（7）将当前文件设置为top-levelentity：首先在projectnavigator窗口单击Files
按钮，然后单击DeviceDesignFiles前的加号+，如下图所示。（如果不
小心关闭了projectnavigator窗口，可点击view菜单->UtilityWindows->
projectnavigator打开）
在projectnavigator窗口的sy11.bdf文件上单击右键，选择setastop-level

## 第6页

6entity，如下图所示。
（8）编译，单击工具栏的编译按钮
（有的版本三角形是蓝色的），
提示：编译前把message窗口打开，可以看到编译过程及结果，包括错误信息。
打开方式：view菜单utilitywindowsmessages
（9）编译成功后，仿真：一,首先，建立仿真波形文件，在quartusII14.0软件
File菜单中单击new，弹出下图所示的对话框，选择verification/Debugging
Files选项卡下的UniversityprogramVWF选项，单击ok按钮。
二，调整波形文件尺度：在刚弹出的对话框simulationwaveformeditor的
edit菜单项中选择Setendtime，在弹出的endtime对话框中将时间改成

## 第7页

7100us（微秒），然后在edit菜单项中再选择GridSize改成1us。当simulation
waveformeditor窗口看不到波形图中的竖虚线时，可一直同时按
ctrl+shift+space组合键缩小波形窗口，直至窗口中的竖虚线出现。
三,调整波形图视图大小的方法：放大----鼠标单击窗口左上角的
后，将鼠标
移动到波形图区域，鼠标的形状变成
后直接在波形图区域单击鼠标左键即可
放大；缩小----连续同时按下ctrl+shift+space组合键，可将波形窗口缩小。
四，在波形窗口左侧空白处双击鼠标左键，弹出如图所示的对话框，

## 第8页

8
在该对话框中单击NodeFinder按钮，弹出NodeFinder对话框，在Node
Finder对话框中的Filter框中选Pins：all，单击list按钮，然后单击窗口
中间的
按钮，最后单击右上方的OK按钮。

## 第9页

9
五，按格子给各输入的值，尽量给出所有可能的情况，具体方法为：首先选中需
要给值的格子（选中格子的方法:按住鼠标左键在格子中拖动可选定某个格），
需要给1时，在选中格子后选择左侧工具栏的
按钮，需要给0时，在选中格
子后选择左侧工具栏的
按钮。（注意：仿真前需要给输入的值，不用给输出
的值，输出的值是执行仿真命令后，仿真器根据你的输入和你的程序出来的结果）
六，保存仿真波形文件，文件名为sy11.vwf。
七，执行仿真命令。Simulation->RunFunctionalSimulation。

## 第10页

10八，执行完仿真命令后，观察各种输入情况下得到的输出的值，进行逻辑分析，
若所有逻辑都对，则表明程序或设计无误。否则，需要修改设计。执行完仿真
命令后，按住ctrl+shift+space组合键缩小波形窗口观察。所谓仿真，就是检查
你的程序的逻辑是否正确，给出各种输入的情况，仿真器根据你的程序中的逻
辑得到输出的值，你需要分析当前的输入情况下得到的输出是否正确？若错误，
则说明你的程序逻辑是错误的。
九、仿真成功后，将半加器设置成可调用的元件（File->Create/Update->create
symbolfilesforcurrentfile），供其它程序调用。注意，此步操作一定要先将
sy11.bdf文件置于最上层（即先使得当前界面为你的图形输入窗口，如下图所示，
不能是仿真界面），否则按钮是灰色的没法操作。生成的元件命名为sy11.bsf。
十、实验一完成，此时可关闭工程：File->Closeproject。
任务二：在QuartusII中用原理图方式实现全加器，并用QuartusII14.0中的波
形仿真。要求调用任务一中的半加器来实现。----本题不需要用FPGA实验箱。
操作步骤：
（1）在E盘新建一个文件夹，命名为sy12。
（2）新建一个工程，工程路径为D:/sy12，工程名为sy12。将任务一的文件夹
sy11中的sy11.bdf和sy11.bsf两个文件拷贝一份到当前工程所在文件夹sy12中。
（3）新建一个原理图文件，按照任务一的方法和步骤在画布中画出全加器的
原理图。注意，需要调用的半加器模块在project中，如下图所示。

## 第11页

11
（4）画好原理图（1位全加器的原理图请见教材P46的图3.15）后，编译，仿
真。仿真具体过程参见任务一的步骤。该实验完成后直接关掉quartusII14.0软
件。
任务三：基于IP核的设计：锁相环IP核设计与仿真----说明：本题不需要用FPGA
实验箱。
具体操作步骤和方法请参见教材第3章第3.4节
注意：按教材上的步骤边做边思考，掌握基于IP核的设计方法和流程。不同版
本的quartus菜单栏有些小差异，比如quartusII9.0中Tools菜单下没有IPCatalog，
但可以直接从Tools菜单进入theMegaWizardPlug-InManager.
提示：注意波形仿真时输入时钟的周期只能给．．．．．．．．．．．．．．．．．20ns．．．．（．50MHZ．．．．．时钟的周期为．．．．．．20ns．．．．）．
任务四：采用文本输入方式编写一个简单的程序，要求用DE2-115开发板上的
SW0拨动开关控制LED0二极管的亮灭，当SW0拨到1的位置，LED0亮，
否则LED0灭。---本题需要用FPGA实验箱。
通过该任务的实现，要求熟练掌握DE2-115开发板的使用方法，JTAG下载
电缆驱动的安装方法。
说明：该任务需要用到DE2-115开发板，所以必须要用quartusII14.0或以上版本
的软件，且必须要选择device，必须进行管脚分配。做该任务时不需要看前言
的内容，任务三和任务四完成后再去看前言的0.3节的内容，前言0.3的内容需
要熟练掌握，后面几次实验课都要用。
具体操作步骤如下：
（1）在开始菜单中打开quartusII14.0软件。
（2）在E盘新建一个文件夹，命名为sy13。
（3）在quartusII14.0软件中新建一个工程，工程路径为D:/sy13，工程名为sy13；
器件选择如下图所示。选好器件后直接点finish。若在选器件之前不小心
点了finish也没关系，可单击Assignments菜单栏中的Device选项打开器
件选择窗口进行器件选择。也可在工程管理窗口的器件上点击右键，选择
Device选项设置。如下图红色框所示。

## 第12页

12
单击上图绿色的框，设置unusedpins，如下图所示

## 第13页

13（4）新建一个文本文件，file->new->VerilogHDLFile如下图所示:注意，以后的
实验都是用文本输入方式，都是选择“VerilogHDLFile”选项。选好后单击
ok按钮。
（5）输入程序。并进行管脚分配，分配管脚需要参考文件“DE2-115中文说明
书”第四章的内容，用到哪个连接到FPGA上的元件，就要看该元件的说
明，比如用到拨动开关sw0和LEDR0,则需要参考de2-115第四章的4.2
节（使用拨动开关）和第4.3节（使用LED），具体管脚分配方法请参考
本实验指导最前面开篇部分介绍的管脚分配方法，选择其中一种方法来分
配管脚即可。分配完管脚并编译后，打开菜单Assignment->PinPlanner确
认一下是否分配好了，本题分配好后在pinplanner窗口看到的效果如下图
所示。
管脚分配示意图：
该题的程序如下：（其中，红色粗线部分是管脚分配。）
modulesy13(in,out);说明：此处sy13为模块名
(*chip_pin="AB28"*)inputin;
(*chip_pin="G19"*)outputout;

## 第14页

14assignout=in;
endmodule
（6）保存文件，注意：文件名一定要和模块名一模一样（可把模块名复制一下，
然后在保存的时候粘贴）。
（7）编译。
（8）编译成功后，下载程序。单击Tools菜单，选择Programmer选项，打开
Programmer对话框，在Programmer对话框中点击hardwaresetup，点击
hardwaresetup对话框中的currentlyselectedhardware选项后的nohardware
下拉菜单，选择usb-blaster[USB-0],若没看到usb-blaster[USB-0]选项，重
新点击hardwaresetup进行选择（usb-blaster驱动装好后有延时，需要耐
心选择）硬件选择好后hardwaresetup后面的那个框显示的是
usb-blaster[USB-0]，而不是nohardware。然后点addfileouputfiles,找到
拓展名为.sof的文件并点open，最后单击Programmer对话框中的start按
钮进行程序下载。
（9）在线测试。程序下载到开发板后观察程序运行结果是否与预期的一样，若
不一样则需要修改程序。
任务五：采用文本输入方式编写一个简单的程序，要求用DE2-115开发板上的
SW17拨动开关控制LEDR17二极管的亮灭，当SW17拨到1的位置，LED17
亮，否则LED17灭。---本题需要用FPGA实验箱。
任务六：学会使用嵌入式逻辑分析仪signaltap（以正弦信号产生器为例，代码
请参见本文档“附件1”）具体操作步骤和方法请参见教材第3.5节SignalTapII
的使用方法。也可参考文件“SignalTapII使用实例----实验二任务六”
说明：本题需要用FPGA实验箱。
任务七：使用数字锁相环实现分频，假定输入时钟频率为50MHz，想要得到5MHz
的时钟信号，试用altpll宏功能模块实现该电路；完成电路仿真（电路仿真不
要写代码，用波形仿真方法），并用signaltap对信号进行分析。
提示：注意波形仿真时输入时钟的周期只能给．．．．．．．．．．．．．．．．．20ns．．．．（．50MHZ．．．．．时钟的周期为．．．．．．20ns．．．．）．
注意：此题不需要写.v代码，如果不会做此题，强烈建议先把任务三重新做一
遍再做此题！
signaltap使用参考任务六（areset引脚分配到AB28（0电平触发），输入时
钟引脚分配到Y2）。
学有余力的同学可选做以下题目：
1.自主完成3.3节其它内容，进一步巩固基于IP核的设计方法和流程。或者参考
第8版教材做一个模24方向可控计数器（使用LPM_COUNTER宏模块完成设计）
（具体操作步骤具体见“附件2”）
2.尝试采用2个拨动开关控制4个LED等的亮灭，要求：当输入00时，LEDR0
亮；当输入为01时，LEDR1亮；当输入为10时，LEDR2亮；当输入为11时，
LEDR3亮；
不愿意做选做题的同学，可以把反复多次把实验一和实验二做熟练，达到只看到
任务就能熟练运用软件实现任务的目的。
附件1：//实验六所需代码
modulesy16(clock,clr,dout,clk_6m);

## 第15页

15(*chip_pin="AB28"*)inputclr;
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

## 第16页

16附件2：

## 第17页

17

## 第18页

18

## 第19页

19

## 第20页

20

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
