---
id: extract-algo-3e156f7f
type: extract
status: extracted
course: ALGO
source:
  - "[[91_Raw-Archive/PDF/ALGO_归纳法.pdf_课件_未知日期_3e156f7f.pdf]]"
source_pages: all
source_hash: "3e156f7fc3372062a2e4675cf532c3a36fa82f6cc1165a88f4cc87a9862ee7cb"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 归纳法.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

归纳法  
cover ：小孩不哭站起来
斐波那契数列  
核心思想：
第  项的值完全依赖于前两项。  归纳关系：  ，基础情况  
伪代码：
选择排序（递归版）  
核心思想：归纳法  (Induction)
我们如何把 “ 对   个元素排序 ” 的问题，转化为 “ 对   个元素排序 ” 的问题？
逻辑如下：
1. 归纳假设 ：假设我们已经知道怎么对前   个元素进行排序。
2. 当前步骤 ：对于   个元素的数组  ：
首先，在整个数组中找到 最大 的那个元素。
把它和数组的 最后一个位置  ( ) 交换。
此时，最大的元素已经归位了。
3. 递归调用 ：剩下的任务就是对前   个元素  ( ) 重复上述过程  
伪代码  ( 递归版 )Algorithm Fibonacci(n)
    // 输入：非负整数  n
    // 输出：第  n 个斐波那契数
    
    // 1. 基础情况  (Base Case)
    if n = 0 return 0
    if n = 1 return 1
    
    // 2. 归纳步骤  (Inductive Step)
    return Fibonacci(n-1) + Fibonacci(n-2)
Algorithm SelectionSort(A, n)
    // 输入：数组  A[1..n] ，当前要处理的规模  n
    // 输出：排好序的数组
    
    // 1. 基础情况  (Base Case) 
    // 如果数组里只有 1 个元素（或 0 个），那它自然是有序的，直接返回
    if n <= 1 return 
    
    // 2. 找到最大值的位置  (Find Max)
    // 这一步是该算法的主要 “ 工作量 ” 来源
    maxIndex = 1

## 第2页

时间复杂度分析：
第n 层：这需要扫描整个当前范围，进行   次比较  。
剩下的任务：这是规模为   的同一问题，代价记为   。
合并起来：总代价  = 当前这一步的代价  + 剩下的递归代价
      
                        
                               
                               
插入排序  
核心思想：归纳法  (Induction)
我们同样把 “ 对   个元素排序 ” 的问题，转化为 “ 对   个元素排序 ” 的问题。
逻辑如下：
1. 归纳假设 ：假设前   个元素   已经排好序了。
2. 当前步骤 ：要把第   个元素（也就是最后一个元素）插入到前面这个 已经有序 的序列中的正确位
置。
3. 递归结构 ：先递归地让前   个排好，再处理第   个的插入。
算法伪代码  ( 递归版 )    for i from 2 to n:
        if A[i] > A[maxIndex]:
            maxIndex = i
            
    // 3. 交换  (Swap)
    // 将找到的最大值放到当前范围的最后面  ( 第  n 个位置 )
    swap(A[maxIndex], A[n])
    
    // 4. 归纳 /递归步骤  (Recursive Step) 
    // 现在最大的已经在最后了，只需要对剩下的  n-1 个元素排序
    SelectionSort(A, n-1)
Algorithm InsertionSort(A, n)
    // 输入：数组  A[1..n] ，当前处理的规模  n
    
    // 1. 基础情况  (Base Case)
    // 如果只有 1个元素，它本身就是有序的
    if n <= 1 return 
    
    // 2. 递归步骤  (Recursive Step)
    // 先不管第  n 个元素，把前  n-1 个排好序
    // 这一步结束后， A[1] 到  A[n-1] 是有序的
    InsertionSort(A, n-1)
    
    // 3. 归纳步骤  (Inductive Step) - " 插入 "
    // 将第 n 个元素  (key) 插入到前面有序数组的正确位置
    key = A[n]
    j = n - 1

## 第3页

时间复杂度：
1. 最好情况  (Best Case)
场景 ：数组原本就是有序的（比如  [1, 2, 3, 4, 5] ）。
分析 ：当我们试图把  5 插入到  [1, 2, 3, 4] 时，只需要比一次，发现  ，就不用动了。
公式 ：
结果 ： 。这意味着对于 基本有序 的数据，插入排序非常快。
2. 最坏情况  (Worst Case)
场景 ：数组是反序的（比如  [5, 4, 3, 2, 1] ）。
分析 ：当我们试图把  1 插入到  [2, 3, 4, 5] 时，必须一路比到头，把前面所有元素都挪一
遍。
公式 ：
结果 ：这个公式和选择排序一模一样，解出来是  。
基数排序  
核心思想：多关键字排序
基数排序完全跳出了 “ 比较两个数大小 ” 的思维定势。它不直接比较  7467 和 1247 的大小，而是
把数字拆分成 个位、十位、百位 ... ，把每一位看作一个独立的关键字来进行排序。
关键点：稳定性  (Stability)
每一轮排序必须是 “ 稳定 ” 的。
什么是稳定？  如果两个数当前位相同（比如个位都是 7 ），那么它们在这一轮排序后的前后关系，
必须和上一轮结束时保持一致。
为什么？  当我们在排高位（比如十位）时，如果十位相同，我们希望个位小的排在前面。因为个
位之前已经排好了，利用 “ 稳定性 ” ，就能保留个位排序的成果
算法伪代码
时间复杂度    // 向前扫描：如果前面的元素比  key 大，就往后挪一格
    while j > 0 and A[j] > key:
        A[j+1] = A[j]
        j = j - 1
    
    // 找到位置了，填入  key
    A[j+1] = key
 for j=1 to k
        准备10 个空表 L0,L1,…,L9.
        while L 非空
             a=L中的下一元素；删除 L 中的 a
             i=a中的第j位数字；将 a 加入表 Li 中
         end while 
         L=L0
         for i=1 to 9
              L=L,Li          {将表Li 加入表 L中}
       end for
    end for
    return L

## 第4页

如果有   个数，每个数有   位。
每一轮排序（桶排序 / 计数排序）需要扫描一遍数组  。
总共要做   轮。
总复杂度：  。
结论 ：当  （位数）很小时，这比   的快速排序还要快，也就是 PPT 中提到的 “ 更有效的
方法 ” 7 。
整数幂  
核心思想：二分幂  (Binary Exponentiation)
普通方法  (Brute Force) ：直接把   乘  次： 。这需要   次乘法。
归纳优化：我们可以利用数学上的性质来减少计算量：
当  是偶数时 ： 。比如算出   只需要算出   然后自乘一次。
当  是奇数时 ： 。比如算出  ，可以转化为  。
伪代码：
时间复杂度：
普通乘法需要做   次运算。
这种方法只需要做   次递归。
霍纳法则  
核心思想：嵌套重构算法 5.4 EXPREC (优化版)
Input: 实数 x 和非负整数 n。
Output: x^n。
Function power(x, n)
    // 1. 基础情况  (Base Case)
    // 递归的终止条件：任何数的  0 次方都是  1
    if n = 0 then return 1
    // 2. 递归步骤  (Recursive Step)
    // 核心思想：先计算一半规模的结果  x^( ⌊ n/2 ⌋ )
    // 使用 floor(n/2) 确保这是整数除法
    half_pow ← power(x, ⌊n/2 ⌋)
    // 3. 归纳与合并  (Conquer)
    // 无论奇偶，都需要先将一半的结果平方
    // 对应公式： (x^(n/2))^2
    result ← half_pow * half_pow
    // 4. 奇数修正
    // 如果 n 是奇数，整数除法会少算一次  x ，这里乘回来
    // 例如 n=5， n/2=2 ， result 算的是  x^4 ，需要再乘  x 得到  x^5
    if n 是奇数 then 
        result ← result * x
    end if
    return result
End Function

## 第5页

将  改写为：
这样我们就不需要算  ，只用不断的 “ 乘   加系数 ” 即可。
伪代码  ：
时间复杂度：
乘法次数 ：循环执行   次，每次做  1 次乘法。总共   次乘法 。
加法次数 ：循环执行   次，每次做  1 次加法。总共   次加法 。
总运算量 ：  次基本运算。
 
时间复杂度 ：忽略常数系数，即为   1 。
生成全排列  
第一种方法：交换回溯法  
核心思想
我们持有一个初始化好的数组  P = [1, 2, ..., n] 。
递归逻辑 ：当前函数  perm1(m) 的任务是确定第  m 个位置上的数字。
怎么确定？  它把第  m 个位置原本的数字，和它后面的每一个数字（包括它自己）进行 交换 。
回溯 ：交换后，递归处理下一个位置  m+1 。递归回来后，必须再次 交换 （恢复原状），以便尝试
下一个可能的数字。
伪代码：算法 5.5 HORNER ( 优化版 )
Input: 
    A: 多项式系数数组，其中  A[i] 表示  x^i 的系数  ( 即  a_0, a_1, ..., a_n)
    n: 多项式的最高次幂  (degree)
    x: 需要求值的具体数值
Output: 多项式  P(x) 的值
Function horner(A, n, x)
    // 1. 初始化  (Initialization)
    // 归纳基础：从最高次项的系数  a_n 开始
    // 把这一项看作最内层的括号里的值
    result ← A[n]
    // 2. 迭代计算  (Iterative Step)
    // 从倒数第二高位  (n-1) 开始，一路向低位扫描直到  0
    for i ← n-1 downto 0 do
        
        // 核心归纳步骤：
        // 当前结果乘以  x ，再加上下一位的系数
        // 这相当于数学上的： result * x + a_i
        result ← result * x + A[i]
        
    end for
    // 循环结束时， result 包含了整个多项式的值
    return result
End Function

## 第6页

第二种方法：填空插入法  
核心思想：
初始化一个全为  0 的数组，表示所有位置都是空的。
递归逻辑 ：函数  perm2(m) 的任务是把数字  m 放到数组中一个 空闲的位置 上。
怎么放？  遍历整个数组，如果发现  P[j] == 0 （是空的），就把  m 放进去。
递归 ：放好  m 后，递归调用  perm2(m-1) 去放下一个更小的数字。
回溯 ：递归回来后，把该位置重置为  0 （变回空位），以便  m 可以尝试放在别的位置。
时间复杂度：
全排列的时间复杂度 ： 。
核心原因 ：全排列的数量级本身就是  ，且每次输出需要  。算法5.7 PERMUTATIONS1 (交换法)
Input: 正整数n.
Output: 数1,2,...,n. 的所有可能排列
for j←1 to n      // 生成数组
    P[j]←j
end for
perm1(1)
过程 perm1(m)
    if m=n then output P[1...n]
    else
        for j←m to n
            互换 P[j] and P[m]
            perm1(m+1)
            互换 P[j] and P[m]
            comment: at this point P[m..n]=m, m+1, ..., n
        end for
    end if
算法5.8 PERMUTATIONS2 (填空法)
Input: 正整数n.
Output: 数1,2,...,n的所有可能排列。
for j←1 to n
    P[j]←0
end for
perm2(n)
过程 perm2(m)
    if m=0 then output P[1..n]
    else
        for j←1 to n
            if P[j]=0 then
                P[j]←m
                perm2(m-1)
                P[j]←0
            end if
        end for
    end if

## 第7页

寻找多数元素  
核心思想：抵消法  (Cancellation)
1. 归纳假设 ：如果我们在数组中删去 两个不同 的元素，那么剩下的数组中，多数元素依然是原数组的
多数元素（或者多数元素不存在）。
2. 直观理解 ：把多数元素看作 “ 盟军 ” ，其他元素看作 “ 敌军 ” 。因为 “ 盟军 ” 超过半数，所以如果采取 “ 一
换一 ” 同归于尽的策略，最后剩下的活口一定是 “ 盟军 ” 。
伪代码：
算法 5.7 MAJORITY (多数元素投票法)
Input: 数组 A[1..n]
Output: 数组中的多数元素 (若存在)
Function find_majority(A, n)
    // 1. 初始化  (Initialization)
    // c: 当前的候选人  (Candidate)
    // count: 当前候选人的票数  ( 强度 )
    c ← unknown
    count ← 0
    // 2. 扫描与抵消  (Sweeping and Canceling)
    // 遍历数组中的每一个元素  x
    for i ← 1 to n do
        x ← A[i]
        if count = 0 then
            // 之前的都抵消光了，当前元素  x 成为新的候选人
            c ← x
            count ← 1
        else
            if x = c then
                // 如果 x 是自己人，票数  +1
                count ← count + 1
            else
                // 如果 x 是其他人，一换一抵消，票数  -1
                count ← count - 1
            end if
        end if
    end for
    // 3. 验证阶段  (Verification - 可选 )
    // 此时 c 是唯一的幸存者，但需要确认它是否真的超过半数
    // (如果题目保证一定存在多数元素，这一步可以省略 )
    total ← 0
    for i ← 1 to n do
        if A[i] = c then total ← total + 1
    end for
    if total > n/2 then 
        return c
    else
        return "不存在"
    end if
End Function

## 第8页

时间复杂度：
 
暴力法  (Brute-Force) ：
思路：对于每一个元素，都去数一遍它出现了几次。
复杂度：双重循环， 。
排序法  (Sorting) ：
思路：先给数组排序，如果存在多数元素，它一定位于中间位置  。
复杂度：取决于排序算法，通常是  。
投票抵消法  ( 本算法 ) ：
思路：一换一抵消。
复杂度： 。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_算法_课程MOC|算法 MOC]]
