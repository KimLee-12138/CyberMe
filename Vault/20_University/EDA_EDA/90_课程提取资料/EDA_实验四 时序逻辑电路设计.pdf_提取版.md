---
id: extract-eda-451d3a05
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/PDF/EDA_实验四 时序逻辑电路设计.pdf_课件_未知日期_451d3a05.pdf]]"
source_pages: all
source_hash: "451d3a054dad8fb8997320708ebe49a7044bf76c2879657fdb70cc7d3b260322"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 实验四 时序逻辑电路设计.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

实验四时序逻辑电路设计、仿真与实现（4
学时）
任务一：计数器设计与仿真
设计一个模200的二进制加法计数器并在quartusII14.0中仿真。
要求用两种方式实现：方式一、直接用verilogHDL行为描述方法实现；
方式二、采用ip核实现（参考实验一的任务三或绿皮书3.3节）
两种设计方式都需要仿真。
注意：（1）此题截仿真结果图的时候要移动滚动条将计数最大值199那部分
显示出来。给输入时钟脉冲的值可直接点左侧工具栏的时钟图标
，可一次性
给出输入脉冲的所有值。（说明：如果仿真时看不到199，可将仿真器的endtime
值设大一点。）
（2）计数结果用UnsignedDecimal显示，不要用ASCII。修改过程如下图所示：
在信号名上单击右键，选择properties选项，在Radix栏中选择UnsignedDecimal，
单击确定按钮。

## 第2页

（3）仿真之前检查一下所用的仿真文件是否为当前设置的波形文件：
Assignments->settings,在settings对话框中查看simulatorsettings中的simulation
input文件。
任务二、10分频器设计与仿真
设计并实现偶数分频器，对开发板上的50Mhz时钟分频，得到一个5MHz
的时钟。
注意：该题仿真的时候，nodefinder对话框的Filter中选择pins:all&register
postfitting项，如下图所示。
任务三、实现一个带有闪烁功能的共阳极七段数码管的显示译码控制电路（在1
个数码管上动态循环显示0～F）。
提示：1）DE2-115开发板上的时钟频率是50Mhz,频率太高，周期太短，人眼识
别不了变化，故需要设计分频器，得到4hz或1hz的时钟来使用。
2）可在频率为1hz的clk的高电平期间让数码管亮，低电平期间让数码管灭，
达到闪烁的效果。也可用某个计数器来实现闪烁效果。
学有余力的同学可选做
（1）计时器设计与实现
要求设计并实现一个数字计时器，可以完成0分00秒-9分59秒的计时功能
且计时准确。并且能够在控制电路的作用下具有开机清零、快速校分、整点报时
（用LED二极管显示）等功能。能够通过七段数码管或LCD1602液晶进行输出。
（2）与参与科研项目相关的自选题
（3）HDLbits网站的题目

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
