---
id: algo-problems-dc-dp
type: problem-set
status: active
course: ALGO
created: 2026-07-17
updated: 2026-07-18
mastery: reviewing
importance: high
---

# 例题集：分治与动态规划

> 包含经典教材题 + LeetCode 原题，每题标注难度与来源。

---

## 分治篇

### 题 1. 递归方程求解 ★★☆

求解 $T(n) = 3T(n/2) + n^2$。

**解**：套主定理。$a=3, b=2$，$\log_2 3 \approx 1.585$。$f(n)=n^2 = \Omega(n^{1.585+\epsilon})$，Case 3。正则条件：$3\cdot(n/2)^2 = 3n^2/4 \le cn^2$（取 $c=3/4$）。故 $T(n)=\Theta(n^2)$。

---

### 题 2. 归并排序递归树 ★★☆

分析 $T(n) = 2T(n/2) + cn$ 的复杂度。

**解**：递归树：层 0 = $cn$，层 1 = $cn/2+cn/2=cn$，...每层都是 $cn$，树高 $\log_2 n$。总代价 = $cn \cdot \log_2 n = O(n\log n)$。

---

### 题 3. 快排最坏情况 ★★☆

数组 $[1,2,3,4,5]$ 用快排（选第一个为 pivot），求比较次数。

**解**：每轮 pivot 是最小值，比较次数 = $4+3+2+1=10 = O(n^2)$。这说明了为什么快排对于已排序数组退化。

---

### 题 4. 求 x 的平方根 ★★☆ [LC 69]

实现 `int sqrt(int x)`，返回整数部分。

**解**：二分查找法。在 $[0,x]$ 中二分搜索 $mid$，使得 $mid^2 \le x < (mid+1)^2$。

```
int mySqrt(int x) {
    if (x <= 1) return x;
    int lo = 1, hi = x / 2, ans = 0;
    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (mid * mid <= x) { ans = mid; lo = mid + 1; }
        else hi = mid - 1;
    }
    return ans;
}
```

$O(\log x)$。

---

### 题 5. 搜索旋转排序数组 ★★★ [LC 33]

在旋转后的有序数组 $[4,5,6,7,0,1,2]$ 中查找 target，$O(\log n)$。

**解**：二分查找时判断 mid 落在左有序段还是右有序段，再确定 target 在哪边。

```
int search(vector<int>& A, int target) {
    int lo = 0, hi = A.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (A[mid] == target) return mid;
        if (A[lo] <= A[mid]) {  // 左半有序
            if (A[lo] <= target && target < A[mid]) hi = mid - 1;
            else lo = mid + 1;
        } else {  // 右半有序
            if (A[mid] < target && target <= A[hi]) lo = mid + 1;
            else hi = mid - 1;
        }
    }
    return -1;
}
```

---

### 题 6. 数组中的第 K 个最大元素 ★★★ [LC 215]

在未排序数组中找第 $k$ 大的元素。

**解**：基于快排 partition（QuickSelect）。每次 partition 后确定 pivot 位置，只递归一侧。

```
int findKthLargest(vector<int>& A, int k) {
    // 第 k 大 = 第 n-k 小（0-indexed）
    int target = A.size() - k, lo = 0, hi = A.size() - 1;
    while (lo <= hi) {
        int p = partition(A, lo, hi);
        if (p == target) return A[p];
        else if (p < target) lo = p + 1;
        else hi = p - 1;
    }
    return -1;
}
```

期望 $O(n)$，最坏 $O(n^2)$。

---

### 题 7. 最大子数组和 ★★☆ [LC 53]

求子数组的最大和。

**解（分治）**：分左右两半，最大子数组可能在左边、右边或横跨中间。横跨的情况从中间向两边扩展求和。

**解（DP/Kadane，更优）**：$dp[i] = \max(A[i], dp[i-1]+A[i])$。$O(n)$，$O(1)$ 空间。

```
int maxSubArray(vector<int>& A) {
    int cur = A[0], best = A[0];
    for (int i = 1; i < A.size(); i++) {
        cur = max(A[i], cur + A[i]);
        best = max(best, cur);
    }
    return best;
}
```

---

## 动态规划篇

### 题 8. 爬楼梯 ★☆☆ [LC 70]

每次爬 1 或 2 阶，到第 $n$ 阶有几种方法。

**解**：$dp[i] = dp[i-1] + dp[i-2]$，$dp[0]=1, dp[1]=1$。斐波那契数列。

---

### 题 9. 打家劫舍 ★★☆ [LC 198]

不能偷相邻房屋，求最大金额。

**解**：$dp[i] = \max(dp[i-1], dp[i-2] + nums[i])$。$O(n)$。

```
int rob(vector<int>& nums) {
    int prev2 = 0, prev1 = 0;
    for (int x : nums) {
        int cur = max(prev1, prev2 + x);
        prev2 = prev1; prev1 = cur;
    }
    return prev1;
}
```

---

### 题 10. 最长递增子序列 ★★★ [LC 300]

求最长严格递增子序列长度。

**解（$O(n^2)$ DP）**：$dp[i] = \max_{j<i, A[j]<A[i]} (dp[j] + 1)$。

**解（$O(n\log n)$ 贪心+二分）**：维护一个数组 `tails`，`tails[k]` = 长度为 k+1 的递增子序列的最小末尾值。遍历时二分查找插入位置。

```
int lengthOfLIS(vector<int>& A) {
    vector<int> tails;
    for (int x : A) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else *it = x;
    }
    return tails.size();
}
```

---

### 题 11. 编辑距离 ★★★ [LC 72]

将 word1 转换为 word2 的最少操作数（增/删/改）。

**解**：$dp[i][j]$ = word1 前 $i$ 个字符 → word2 前 $j$ 个字符的最小编辑距离。

$$dp[i][j] = \begin{cases} dp[i-1][j-1] & A[i]=B[j] \\ 1 + \min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) & A[i] \neq B[j] \end{cases}$$

$O(mn)$。

---

### 题 12. 零钱兑换 ★★☆ [LC 322]

用不同面额硬币凑出 amount 的最少硬币数。

**解**：$dp[i] = \min_{coin \le i}(dp[i-coin] + 1)$，$dp[0]=0$。完全背包变体。

```
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++)
        for (int c : coins)
            if (i >= c) dp[i] = min(dp[i], dp[i - c] + 1);
    return dp[amount] > amount ? -1 : dp[amount];
}
```

---

### 题 13. 分割等和子集 ★★★ [LC 416]

能否将数组分成两个和相等的子集。

**解**：转化为 0-1 背包 —— 能否从数组中选出若干个元素，和为 $sum/2$。$dp[j] = dp[j] \mid dp[j-nums[i]]$，逆序遍历。

---

### 题 14. 最长回文子串 ★★★ [LC 5]

求最长回文子串。

**解（DP）**：$dp[i][j]$ 表示 $s[i..j]$ 是否回文。$dp[i][j] = (s[i]==s[j]) \land dp[i+1][j-1]$。从长度递推，$O(n^2)$。

**解（中心扩展）**：枚举每个中心，向两边扩展。$O(n^2)$，$O(1)$ 空间。

---

### 题 15. 正则表达式匹配 ★★★★ [LC 10]

实现 `.` 和 `*` 的正则匹配。

**解**：$dp[i][j]$ = s 的前 $i$ 个字符能否匹配 p 的前 $j$ 个模式。
- 若 $p[j-1]='*'$：$dp[i][j] = dp[i][j-2]$（不使用 `*`）或 $dp[i-1][j]$（使用 `*` 且字符匹配）
- 否则：$dp[i][j] = dp[i-1][j-1]$（字符匹配）

---

### 题 16. 矩阵链相乘 ★★★

$A_1(30\times35), A_2(35\times15), A_3(15\times5), A_4(5\times10), A_5(10\times20)$，求最少乘法次数。

**解**：$m[1][5] = 11875$。最优加括号：$(A_1(A_2A_3))((A_4A_5))$。

---

### 题 17. 不同路径 ★★☆ [LC 62]

$m\times n$ 网格左上→右下，只能向右或向下，有几种走法。

**解**：$dp[i][j] = dp[i-1][j] + dp[i][j-1]$。组合数解：$C(m+n-2, m-1)$。

---

### 题 18. 三角形最小路径和 ★★☆ [LC 120]

三角形从上到下的最小路径和。

**解**：自底向上 DP。$dp[i][j] = \triangle[i][j] + \min(dp[i+1][j], dp[i+1][j+1])$。

---

### 题 19. 单词拆分 ★★★ [LC 139]

判断字符串能否由字典中的单词拼接而成。

**解**：$dp[i]$ = s 的前 $i$ 个字符能否被拆分。$dp[i] = \bigvee_{j<i} (dp[j] \land s[j..i-1] \in dict)$。

---

### 题 20. 买卖股票的最佳时机 ★★☆ [LC 121]

一次交易的最大利润。

**解**：遍历时维护最低价格，当天利润 = 当前价格 - 历史最低。

---

## 相关链接
- [[../02_知识点/分治策略|分治策略]]
- [[../02_知识点/动态规划|动态规划]]
- [[../02_知识点/Strassen矩阵乘法|Strassen矩阵乘法]]
- [[../03_公式与规则/算法_公式速查|公式速查]]
