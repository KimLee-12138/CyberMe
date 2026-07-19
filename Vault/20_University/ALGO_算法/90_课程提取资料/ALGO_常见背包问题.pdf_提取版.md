---
id: extract-algo-f07f9ea0
type: extract
status: extracted
course: ALGO
source:
  - "[[91_Raw-Archive/PDF/ALGO_常见背包问题.pdf_课件_未知日期_f07f9ea0.pdf]]"
source_pages: all
source_hash: "f07f9ea0b18e606e0ec9e56571f4c44cc0902ca1ad42a2629f94a6a85642ee75"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 常见背包问题.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

常见背包问题  
1. 0/1 背包问题  (0/1 Knapsack)  
核心特点 ：每种物品仅有一件，可以选择 放 或 不放 。
原理讲解  
状态定义 ：  表示前   件物品放入容量为   的背包能获得的最大价值。
转移方程 ：
空间优化 ：使用一维数组时， 容量必须从大到小遍历 ，以保证更新   时使用的是 “ 上一层 ” 的状
态（即物品   还没被放入时的状态）。
代码模版  ( 一维优化 )  
0/1 背包例题：采药  
题目描述 ： 辰辰是个天资聪颖的孩子，他的梦想是成为世界上最伟大的医师。为此，他想拜附近
最有威望的医师为师。医师给了他一个考验：在规定的时间内（ ），去山洞里采摘一些草药。每
株草药采摘需要消耗时间  ，价值为  。每种草药只能采一次，求在   时间内能采到的最大总价
值。
2. 完全背包问题  (Complete Knapsack)  
核心特点 ：每种物品有 无限件 ，可以重复选取。
原理讲解  
转移方程 ：
与 0/1 背包的区别 ：在一维优化下， 容量从小到大遍历 。因为   需要用到 当前行 已经更新过的  
（代表已经选过该物品后的状态）。
代码模版  
完全背包例题：找零钱（最少硬币数）  for (int i = 0; i < n; i++) { // 遍历物品
    for (int j = m; j >= w[i]; j--) { // 逆序遍历容量
        dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    }
}
for (int i = 0; i < n; i++) {
    for (int j = w[i]; j <= m; j++) { // 正序遍历容量
        dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
    }
}

## 第2页

题目描述 ： 给定不同面额的硬币  coins 和一个总金额  amount 。每个硬币的数量是无限的。请你
计算并返回可以凑成总金额的硬币组合数。
3. 多重背包问题  (Multiple Knapsack)  
核心特点 ：每种物品有 有限件  。
原理讲解  
朴素做法 ：将其拆解为   个相同的  0/1 背包物品。复杂度高： 。
核心思路 ：把 “ 第   种物品有   个” 看作是做决策时有多个选项。
状态转移方程：
           
  其中   且 。
二进制优化 ：将   件物品拆分成系数为   的多组物品。任何数
量的   都可以由这些组组合而成。复杂度优化至： 。
代码模版  ( 一维空间优化版 )  
代码模版  ( 二进制优化 )  
多重背包例题：庆功宴  // n: 物品种类 , m: 背包总容量
// w[i]: 重量 , v[i]: 价值 , s[i]: 数量
for (int i = 1; i <= n; i++) { // 1. 遍历物品
    for (int j = m; j >= 0; j--) { // 2. 逆序遍历容量  ( 同 0/1 背包 )
        // 3. 增加一层循环：枚举当前物品选几个
        for (int k = 1; k <= s[i] && k * w[i] <= j; k++) {
            dp[j] = max(dp[j], dp[j - k * w[i]] + k * v[i]);
        }
    }
}
struct Item { int w, v; };
vector<Item> items;
// 拆分逻辑
for (int i = 0; i < n; i++) {
    int weight, value, num;
    cin >> weight >> value >> num;
    for (int k = 1; k <= num; k <<= 1) {
        items.push_back({weight * k, value * k});
        num -= k;
    }
    if (num > 0) items.push_back({weight * num, value * num});
}
// 转化为  0/1 背包
for (auto item : items) {
    for (int j = m; j >= item.w; j--)
        dp[j] = max(dp[j], dp[j - item.w] + item.v);
}

## 第3页

背包类型 物品限制 核心遍历顺序 关键点
0/1 背包 每种  1 件 j 逆序 防止同一物品被选多次
完全背包 每种无限件 j 正序 利用已更新的状态实现重复选取
多重背包 每种   件 拆分为  0/1 背包 二进制拆分是常用的优化手段
分组背包 每组选  1 件 j 在组内循环外 确保一组内只能选一个题目描述 ： 为了庆祝校赛，需要采购   种奖品。每种奖品价格为  ，价值为  ，且库存数量为  
。在预算   内，如何选择奖品使得总价值最大？
4. 分组背包问题  (Grouped Knapsack)  
核心特点 ：物品被分为若干组， 每组内最多只能选一件 。
原理讲解  
决策逻辑 ：对于每一组，我们面临的决策是：不选，或者选该组中的某一件物品。
遍历顺序 ：外层循环组，中层循环容量（逆序），内层循环组内成员。
代码模版  
分组背包例题：通天之分组背包  
题目描述 ： 物品被分成   组。每组内的物品之间是冲突的，也就是说，每组最多只能选一件物
品。求在容量   下的最大价值。
总结与备考建议  
考试技巧提醒 ：
1. 初始化 ：如果要求 “ 恰好装满 ” ，则  ，其余设为  ；如果不要求装满，则全设为  。
2. 大容量问题 ：如果背包容量   极大但物品数量小，考虑使用 价值作为  DP 维度 或 贪心 + 搜索 。
3. 二维费用 ：如果题目同时限制了 “ 重量 ” 和 “ 体积 ” ，只需在  DP 数组上多加一维。
针对你的  12 月  28 日考试，你是否需要我为你提供几道典型的 混合背包 或 有依赖的背包 （如树形  DP 结
合背包）的进阶练习题？
例题题解  
0/1 背包例题：采药  for (int i = 0; i < group_count; i++) { // 遍历每一组
    for (int j = m; j >= 0; j--) { // 逆序遍历容量
        for (int k = 0; k < group[i].size(); k++) { // 遍历组内所有物品
            if (j >= group[i][k].w) {
                dp[j] = max(dp[j], dp[j - group[i][k].w] + group[i][k].v);
            }
        }
    }
}

## 第4页

题目描述 ： 辰辰是个天资聪颖的孩子，他的梦想是成为世界上最伟大的医师。为此，他想拜附近
最有威望的医师为师。医师给了他一个考验：在规定的时间内（ ），去山洞里采摘一些草药。每
株草药采摘需要消耗时间  ，价值为  。每种草药只能采一次，求在   时间内能采到的最大总价
值。
题解思路 ：
1. 状态定义 ：dp[j] 表示在剩余时间为  j 的情况下能获得的最大价值。
2. 核心逻辑 ：对于每一株草药，我们考虑 “ 采 ” 或 “ 不采 ” 。
3. 遍历顺序 ：为了保证每种草药只被采一次，剩余时间  j 必须 从大到小（逆序） 遍历。如果正
序遍历， dp[j] 可能会引用到同一物品被放入后的  dp[j-w[i]] ，导致重复计算。
完全背包例题：零钱兑换  II ( 求方案数 )  
题目描述 ： 给定不同面额的硬币  coins 和一个总金额  amount 。每个硬币的数量是无限的。请你
计算并返回可以凑成总金额的硬币组合数。
题解思路 ：
1. 状态定义 ：dp[j] 表示凑成金额  j 的组合数。
2. 核心逻辑 ：凑成金额  j 的方法，等于 “ 不选当前硬币的方法数 ” 加上 “ 选了当前硬币后，凑成剩
余金额  j-coin 的方法数 ” 。
3. 遍历顺序 ：因为硬币无限，我们需要 正序遍历 。这样  dp[j] 在计算时，已经包含了 “ 之前可
能已经选过该硬币 ” 的状态。#include <iostream>
#include <algorithm>
using namespace std;
int dp[1005]; // 背包容量（时间）
int w[105], v[105];
int main() {
    int T, M; // T是总时间， M 是草药数量
    cin >> T >> M;
    for (int i = 1; i <= M; i++) cin >> w[i] >> v[i];
    for (int i = 1; i <= M; i++) { // 遍历物品
        for (int j = T; j >= w[i]; j--) { // 逆序遍历时间
            dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
        }
    }
    cout << dp[T] << endl;
    return 0;
}
#include <vector>
#include <iostream>
using namespace std;
int change(int amount, vector<int>& coins) {
    vector<long long> dp(amount + 1, 0);
    dp[0] = 1; // 凑成金额 0只有一种方法：什么都不选
    for (int coin : coins) { // 遍历硬币
        for (int j = coin; j <= amount; j++) { // 正序遍历金额
            dp[j] += dp[j - coin];

## 第5页

多重背包例题：庆功宴  
题目描述 ： 为了庆祝校赛，需要采购   种奖品。每种奖品价格为  ，价值为  ，且库存数量为  
。在预算   内，如何选择奖品使得总价值最大？
题解思路 ：
1. 瓶颈 ：如果直接拆分成   个 0/1 背包，当   很大时会超时。
2. 优化原理 ：任何一个正整数   都可以拆成   以及余数   的和。例如  ，拆
为 。通过这种拆分，我们可以组合出   之间的任何整数。
3. 做法 ：将每种物品按二进制拆分，转为多个  0/1 背包物品。
分组背包例题：通天之分组背包  
题目描述 ： 物品被分成   组。每组内的物品之间是冲突的，也就是说，每组最多只能选一件物
品。求在容量   下的最大价值。
题解思路 ：        }
    }
    return dp[amount];
}
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct Item { int w, v; };
int dp[6005];
int main() {
    int n, m;
    cin >> n >> m;
    vector<Item> real_items;
    for (int i = 0; i < n; i++) {
        int v_i, w_i, s_i;
        cin >> v_i >> w_i >> s_i;
        // 二进制拆分
        for (int k = 1; k <= s_i; k <<= 1) {
            real_items.push_back({v_i * k, w_i * k});
            s_i -= k;
        }
        if (s_i > 0) real_items.push_back({v_i * s_i, w_i * s_i});
    }
    // 执行 0/1 背包
    for (auto& item : real_items) {
        for (int j = m; j >= item.w; j--) {
            dp[j] = max(dp[j], dp[j - item.w] + item.v);
        }
    }
    cout << dp[m] << endl;
    return 0;
}

## 第6页

1. 核心逻辑 ：对每一组进行决策。决策有：①不选该组物品；②选该组里的第  1 件；③选该组
里的第  2 件 …… 以此类推。
2. 关键点 ： 必须先遍历容量，再遍历组内物品 。
原因：如果内层是容量，外层是组内物品，就会变成 “ 每件物品选或不选 ” ，导致一组内
可能选了多件。先固定容量  j ，然后在组内尝试替换不同的物品，能保证  dp[j] 只会
被更新一次（即该组只贡献一次）。
 #include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int dp[1005];
struct Node { int w, v; };
vector<Node> groups[105]; // 存储每一组的物品
int main() {
    int m, n;
    cin >> m >> n;
    int max_g = 0;
    for (int i = 0; i < n; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        groups[c].push_back({a, b});
        max_g = max(max_g, c);
    }
    for (int i = 1; i <= max_g; i++) { // 遍历每一组
        for (int j = m; j >= 0; j--) { // 逆序遍历容量
            for (auto& item : groups[i]) { // 遍历组内所有成员
                if (j >= item.w) {
                    dp[j] = max(dp[j], dp[j - item.w] + item.v);
                }
            }
        }
    }
    cout << dp[m] << endl;
    return 0;
}

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_算法_课程MOC|算法 MOC]]
