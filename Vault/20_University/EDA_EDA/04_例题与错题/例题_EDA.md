---
id: eda-probs
type: problem-set | status: cleaned | course: EDA
created: 2026-07-17 | updated: 2026-07-17
needs_review: true | problem_origin: ai-generated
tags: [EDA, 练习]
---

# 例题_EDA

## 例题1

**题目**：用卡诺图化简 F(A,B,C)=∑m(1,3,4,5,6,7)。

**答案**：卡诺图化简得 F = A + C（画两个大圈）。验证：A=1或C=1的所有最小项。

## 例题2

**题目**：用Verilog写一个带同步复位的4位计数器。

**答案**：always @(posedge clk) begin if(rst) count<=0; else count<=count+1; end

---
> 课程导航：[[../00_EDA_课程MOC|EDA MOC]]
