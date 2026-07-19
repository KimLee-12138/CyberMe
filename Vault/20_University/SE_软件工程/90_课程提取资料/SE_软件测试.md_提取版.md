---
id: extract-se-67effe3d
type: extract
status: extracted
course: SE
source:
  - "[[91_Raw-Archive/DOC/SE_软件测试.md_笔记_未知日期_67effe3d.md]]"
source_pages: all
source_hash: "67effe3df9273c9fdea1c13c8fbb2940b0a42a6933ff27c4073f14a7df02a51f"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 软件测试.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 软件测试

- 目的：软件测试的目标是为了发现软件的缺陷

**测试方法:**

**1. 静态测试**

**2. 动态测试**

- a. 黑盒测试（主要是为了发现功能、接口、传递数据结构的错误）
- b. 白盒测试

## 静态测试

![image](assets/软件测试/p01_img001.png)

## 动态测试

![image](assets/软件测试/p02_img002.png)

- 测试用例：由输入数据和预期的输出数据两部分组成

![image](assets/软件测试/p02_img003.png)

**黑盒测试**

**等价类划分（可能考）**

![image](assets/软件测试/p02_img004.png)

![image](assets/软件测试/p03_img005.png)

![image](assets/软件测试/p03_img006.png)

![image](assets/软件测试/p03_img007.png)

![image](assets/软件测试/p04_img008.png)

**案例1：**

![image](assets/软件测试/p04_img009.png)

- 关键：找到每一个划分标准，为每一个划分标准来划分有效等价类和无效等价类

![image](assets/软件测试/p04_img010.png)

![image](assets/软件测试/p05_img011.png)

![image](assets/软件测试/p05_img012.png)

![image](assets/软件测试/p06_img013.png)

**案例2：**

![image](assets/软件测试/p06_img014.png)

![image](assets/软件测试/p06_img015.png)

**边界值分析（可能考**

![image](assets/软件测试/p07_img016.png)

![image](assets/软件测试/p07_img017.png)

![image](assets/软件测试/p07_img018.png)

**案例1：**

![image](assets/软件测试/p08_img019.png)

![image](assets/软件测试/p08_img020.png)

**案例2：**

![image](assets/软件测试/p08_img021.png)

![image](assets/软件测试/p08_img022.png)

![image](assets/软件测试/p09_img023.png)

**错误推断**

**因果图法**

![image](assets/软件测试/p09_img024.png)

![image](assets/软件测试/p10_img025.png)

![image](assets/软件测试/p10_img026.png)

**案例1：**

![image](assets/软件测试/p11_img027.png)

![image](assets/软件测试/p11_img028.png)

![image](assets/软件测试/p12_img029.png)

![image](assets/软件测试/p12_img030.png)

![image](assets/软件测试/p12_img031.png)

**白盒测试**

**逻辑覆盖法**

![image](assets/软件测试/p13_img032.png)

![image](assets/软件测试/p13_img033.png)

![image](assets/软件测试/p14_img034.png)

![image](assets/软件测试/p14_img035.png)

![image](assets/软件测试/p15_img036.png)

![image](assets/软件测试/p15_img037.png)

![image](assets/软件测试/p16_img038.png)

![image](assets/软件测试/p16_img039.png)

**关键结论**

- 1. 条件组合覆盖是最强覆盖，其用例一定满足判定覆盖、条件覆盖、判定-条件覆盖。
- 2. 判定覆盖强于语句覆盖，但弱于条件组合覆盖和判定-条件覆盖。

**3. 条件覆盖与判定覆盖无直接包含关系：**

**◦满足条件覆盖的用例可能未覆盖所有判定分支（不满足判定覆盖）。**

**◦满足判定覆盖的用例可能未覆盖所有条件取值（不满足条件覆盖）。**

**4. 路径覆盖与其他覆盖无必然包含关系：**

**◦可能覆盖所有路径但未覆盖某些条件组合（不满足条件组合覆盖）。**

**◦条件组合覆盖的用例也可能未覆盖所有路径。**

**基本路径测试（可能考，先要求画出流程图、N-S图，然后映射到程序流图，然后**

**设计测试用例）**

![image](assets/软件测试/p17_img040.png)

![image](assets/软件测试/p17_img041.png)

- 需要注意的几个点：多个顺序语句可以并为一个节点；每一个处理框和判别框都作为一个节点；分支的汇聚处需要有一个汇聚节点；复合条件要分解为一系列的单个条件的嵌套判断

![image](assets/软件测试/p18_img042.png)

![image](assets/软件测试/p18_img043.png)

![image](assets/软件测试/p18_img044.png)

![image](assets/软件测试/p19_img045.png)

![image](assets/软件测试/p19_img046.png)

![image](assets/软件测试/p19_img047.png)

![image](assets/软件测试/p20_img048.png)

- 注意这里的独立路径不包含：1-2-3-9-11-12，因为路径2覆盖了11-12，路径3覆盖了1-2-3，所以它不算独立路径

## 软件测试步骤

![image](assets/软件测试/p20_img049.png)

- 单元测试：模块接口、局部数据结构、边界条件、执行路径、内部错误的测试集成测试：自顶向下、自底向上

![image](assets/软件测试/p21_img050.png)

![image](assets/软件测试/p21_img051.png)

![image](assets/软件测试/p22_img052.png)

![image](assets/软件测试/p22_img053.png)


## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_软件工程_课程MOC|软件工程 MOC]]
