---
id: extract-eda-ff45c200
type: extract
status: extracted
course: EDA
source:
  - "[[91_Raw-Archive/DOC/EDA_13.时序逻辑电路.md_笔记_未知日期_ff45c200.md]]"
source_pages: all
source_hash: "ff45c200ca2d6106746b55e2d487dfbf1a88b69f687c644f57b43ca74841c14c"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 13.时序逻辑电路.md：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

# 13.时序逻辑电路

时序逻辑电路的特点：

1.功能上:任意时刻的输出不仅仅取决于该时刻的输入还取决于电路原来的状态有关

2.电路结构上：包含存储电路和组合电路；存储器状态和输入变量共同决定输出

可以用三个方程来描述，输出方程，驱动方程，状态方程

时序逻辑电路的分类：

1.同步电路（所有的触发器共用同一个时序信号，状态变换发生在同一时刻）

2.异步电路（不是统一的时序信号clk，触发器状态变化有先有后）（分析不做要求）

题型一：**适用于同步电路****根据时序逻辑电路图分析时序电路的功能**

步骤：先有电路图得到每一个触发器的驱动方程，在代入特征方程得到状态方程，再写出输出方程，根据这几个方程可以写出时序电路的状态转移表->状态转移图（->状态机流程图->时序图）。由此可以判断时序逻辑电路的功能

**例题1：**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=M2MzOTY3OTE0OWZjYTNjZWMwZmZhNzE2NTNkOGY4OWJfYW9ybk8ybG1tRmVhU3J5QlI1QnprQ0NBNHIxREYyWTVfVG9rZW46RnpyUWJWdlpjb09NSDJ4UlRwN2NlYmlublBoXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MDUwNmI0ZWIwYzZjMzQyMjgxMTZjOGRiMWVjMjZhYjFfS1oycXBMVHpCcUdrN0xGT0kzYVpkem5VZkEwWE1qTGtfVG9rZW46VzQ5MWJpTGk3b1psVlF4MU9kZmNYbU9KbjgwXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

由此可见111是无效状态，并且这个时序逻辑电路的功能是一个模7的计数器

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MTIzZTkxMjI1YWU3MzQ0MTA1NTc4MDMyMTEzMWQxZjdfME9ZdTBZQTBnZG5BZjJlV0I2N0JlMVJRMmhwZU1ScWhfVG9rZW46REh1bmJ0dTRhb1FZTnF4NWxsc2NWcDJ6bmliXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MGRkZTA3OTMxNWM5MGNiZGJkNjgzZmY0NTg4MDBiNjVfSW5Ua2dZcldmOW1qNWQ1cDg1OHdaUk1GT1AwbE5DblJfVG9rZW46Q0cyeWJmYkxib1hQSWZ4YnVJSmNXOHlQbkFoXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

**例题2：**

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MzIxNjY0Njc5YzU4ZTA3NGQ5YzQ5ODI5NGY0NzczZjZfTGFqdE5hYmdOdHltNUloYlYwZ3k1MmZDMUpvOFF6aDhfVG9rZW46SnVFdGJwR0U4b29PR0d4Z3B4dGM3YnU4bmVnXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=ODQ1NzIxODVkNjljMTM4ZTdmOGU0NjZmNjUwNTQ0YjdfOWVoZUJkcGxRbDVINHVDUUN2TTdBRW15aWNpQTREcURfVG9rZW46SDNCSGIzdGpzb09pcHB4eDBmMWMzMGJzbnNmXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

题型2：**适用于同步时序电路****根据电路功能设计时序逻辑电路**必考！！！！！🌟🌟🌟🌟🌟

解题步骤：

1. 分析有几种状态
2. 画出状态转移图（必要的时候状态化简）
3. 根据化简结果更新状态转移图
4. 根据化简后最终的状态数量，设计触发器个数
5. 由状态转移图得到状态转移表（没有的状态就用X表示）
6. 由表得到输出方程（即Y=？）
7. 将表简单分别转换为显示单个触发器状态变换的表再根据该表用卡诺图得各个触发器的状态方程（即Q*=？）
8. 判断自启动
9. 选择触发器（一般为D，JK最好掌握）得驱动方程
10. 画出电路图（组合电路和时序电路先分开画，再合并）

> 1.如何**状态化简？**
>
> 若两个状态在相同的输入下有相同的输出，并且转换到同一个次态，则成为等价状态。等价状态可以合并，进而做到状态化简
>
> 2.如何判断是否能够**自启动？**
>
> ### **自启动判定条件**
>
> - **可自启动**：所有无效状态均能通过有限次转移进入有效状态。
> - **不可自启动**：存在至少一个无效状态陷入循环或无法转移至有效状态。
>
> ### **示例分析**
>
> 以3位模5计数器为例：
>
> - **有效状态**：000, 001, 010, 011, 100。
> - **无效状态**：101, 110, 111。
> - **转移逻辑**：
>   - 若101→110→111→000，则无效状态可进入有效循环，电路自启动。
>   - 若101→110→111→101（循环），则无法自启动，需修正逻辑。

题目：

有一个时序电路，能够检测到“1101”时输出1，否则输出0.请画出他的电路图

具体解题过程：

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MDQxY2E2MWMwMzNhOGIxMGZmMjU2M2QyY2ZiYzg2YzVfT1o4eEJkb1pndlJrckg3c2xSMlpIRVBHOFE2cG40cU5fVG9rZW46STZ4Z2JicEZKbzhvb2Z4bGMyN2M5SGtwbmJjXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=MzE4MzAzNjEyNGFiODNmZDJmYjFiNWI2NTRmOTMwYzhfeGJQS21pVHo4aFJsTVZDVk9wc1duVVRnSERJZUx1RGhfVG9rZW46UjdxN2I4ZGJyb0FzeXZ4bjNWdWNqSDRsbmJnXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

![img](https://zq2r5nk4aa8.feishu.cn/space/api/box/stream/download/asynccode/?code=M2I3OTQ5NzAyMzgwYmNmMDA4ZWMyMjhlZGI0ZmY3YmVfbmlmSDNWd05Yd3VINzc2SWFwTnkyRDlFTzFzY3JaRUpfVG9rZW46QkFxeGJQc0Vjb2lCdDZ4cnJlWWNjOTJSbnBlXzE3Nzc5MDIxOTA6MTc3NzkwNTc5MF9WNA)

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
