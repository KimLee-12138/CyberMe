---
id: extract-eda-b4fe8639
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_1.绪论.md_笔记_未知日期_b4fe8639.md]]"
source_pages: all
source_hash: "b4fe8639a2639362d93c63fb91152795984994e03d21f1857332775784fc9ba6"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 1.绪论.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

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

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
