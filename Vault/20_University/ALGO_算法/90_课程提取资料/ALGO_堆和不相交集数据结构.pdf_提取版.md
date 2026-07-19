---
id: extract-algo-7aed5553
type: extract
status: extracted
course: ALGO
source:
  - "[[91_Raw-Archive/PDF/ALGO_堆和不相交集数据结构.pdf_课件_未知日期_7aed5553.pdf]]"
source_pages: all
source_hash: "7aed5553bddff14c11b87e393b6de520310956a27cfa0db5f61c03f74248449b"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 堆和不相交集数据结构.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

堆和不相交集数据结构  
cover ：小孩不哭站起来
一、堆  
1. 基本概念  
定义 ：堆通常是一个 完全二叉树  。
性质 ：
最大堆  ：任意节点的值都   其子节点的值。根节点是最大值  1 。
最小堆  ：任意节点的值都   其子节点的值。根节点是最小值  2 。
存储结构 ：通常使用 数组 来实现。
对于下标为   的节点：
左孩子下标：
右孩子下标：
父节点下标：
2. 核心操作  
Sift-up ( 上滤 / 上浮 ) ：
场景 ：通常用于 插入  (Insert) 。
过程 ：将新元素放到数组末尾，如果它违反了堆序性（例如比父节点大），就与父节点交
换，直到满足性质。
时间复杂度 ： 。
伪代码：
Sift-down ( 下滤 / 下沉 ) ：
场景 ：通常用于 删除最大值  (Delete-max)  或 构建堆  (MakeHeap) 。
过程 ：将根节点移走，把数组最后一个元素放到根节点位置，然后让它与较大的子节点交
换，直到沉到合适的位置。
时间复杂度 ： 。
伪代码：// A: 数组 , i: 当前节点下标
Function SiftUp(A, i):
    // 当没有到达根节点 (i>1) ，且当前节点比父节点大时
    While i > 1 AND A[i] > A[Floor(i / 2)]:
        // 违反堆序，交换当前节点与父节点
        Swap(A[i], A[Floor(i / 2)])
        
        // 当前节点位置变为父节点位置，继续向上检查
        i = Floor(i / 2)
    End While
End Function
// A: 数组 , i: 当前下沉节点下标 , n: 堆的大小

## 第2页

Insert ( 插入 ) ：
逻辑：将元素添加到末尾   执行  Sift-up 。
Delete-max ( 删除最大值 ) ：
逻辑：移除根节点   将末尾元素移至根部   执行  Sift-down 。
伪代码：
3. 建堆  
目标 ：将一个无序数组转换为堆。
方法 ：
1. 自顶向下  (Top-down) ：通过不断  Insert 实现，复杂度  。
伪代码：Function SiftDown(A, i, n):
    largest = i          // 假设当前节点是最大的
    left = 2 * i         // 左孩子下标
    right = 2 * i + 1    // 右孩子下标
    // 如果左孩子存在，且左孩子比当前最大值大
    If left <= n AND A[left] > A[largest]:
        largest = left
    // 如果右孩子存在，且右孩子比当前最大值大
    If right <= n AND A[right] > A[largest]:
        largest = right
    // 如果最大值不是当前节点本身（说明子节点中有更大的）
    If largest != i:
        Swap(A[i], A[largest])  // 交换
        SiftDown(A, largest, n) // 递归：继续对下沉后的位置进行检查
    End If
End Function
// A: 数组 , n: 当前堆大小 , key: 要插入的值
Function Insert(A, n, key):
    n = n + 1          // 堆大小加  1
    A[n] = key         // 将新元素放到数组末尾
    SiftUp(A, n)       // 执行上滤，恢复堆序
End Function
// A: 数组 , n: 当前堆大小
Function DeleteMax(A, n):
    If n < 1:
        Error "Heap Underflow"
    
    maxElement = A[1]    // 保存根节点（最大值）
    A[1] = A[n]          // 将数组最后一个元素移到根节点
    n = n - 1            // 堆大小减  1
    
    SiftDown(A, 1, n)    // 对新的根节点执行下滤，恢复堆序
    Return maxElement
End Function

## 第3页

2. 自底向上  (Bottom-up) ：从最后一个非叶子节点开始，依次对每个节点执行  Sift-down 。
优势 ：这种方法的总时间复杂度是  （线性时间），比插入法更快。
伪代码：
4. 堆排序  
PPT 中给出了一个具体的排序例子： A[1..10]={4,3,8,10,11,13,7,30,17,26} 555 。
算法流程 ：
1. 建堆 ：将数组建成一个最大堆  (Max Heap) 。
2. 排序 ：
将根节点（最大值）与堆的最后一个元素交换。
堆的大小减  1 。
对新的根节点执行  Sift-down 恢复堆序。
重复上述过程直到堆为空。
复杂度 ： 。
特点 ：原地排序  (In-place) ，空间复杂度  。
伪代码：Function BuildHeap_TopDown(A, n):
    // 假设 A[1..n] 是无序的，我们模拟从空堆开始插入
    current_heap_size = 0
    For i from 1 to n:
        Insert(A, current_heap_size, A[i])
        // 注意：这里  Insert 内部会调用  SiftUp
End Function
Function BuildHeap_BottomUp(A, n):
    // 最后一个非叶子节点的索引是  Floor(n / 2)
    // 从后往前，对每个父节点执行  SiftDown
    For i from Floor(n / 2) down to 1:
        SiftDown(A, i, n)
End Function
// A: 待排序数组 , n: 数组长度
Function HeapSort(A, n):
    // 1. 建堆  (使用效率更高的自底向上法 )
    BuildHeap_BottomUp(A, n)
    // 2. 排序逻辑
    // 此时 A[1] 是最大值
    For i from n down to 2:
        // 将堆顶 (最大值 ) 与堆的最后一个元素交换
        Swap(A[1], A[i])
        
        // 此时 A[i] 已经是排好序的位置，不再属于堆
        // 堆的大小变为  i-1
        
        // 对新的堆顶  A[1] 执行下滤，恢复堆序
        SiftDown(A, 1, i - 1)
    End For
End Function

## 第4页

二、不相交集  
1. 核心概念  
定义 ：不相交集是一种数据结构，它维护了一系列 互不相交 的子集合。每个集合选出一个 “ 代表 ”
（Representative ），通常是树的根节点，用来标识这个集合。
存储结构 ：通常使用 数组  parent[] 来实现。
parent[i] 表示元素  i 的父节点。
如果  parent[i] == i ，说明  i 是根节点（集合的代表）。
2. 三个基本操作  
(1) Make-Set(x) —— 建立集合  
创建一个只包含元素   的新集合。
逻辑 ：让   的父节点指向它自己。
伪代码 ：
(2) Find(x) —— 查找  
确定元素   属于哪个子集。这通常通过不断向上查找父节点，直到找到根节点为止。
逻辑 ：如果   不是根，就找  ，一直找到根。
伪代码（基础版） ：
如果树退化成一条链（像链表一样），查找的时间复杂度会变成  ，效率很低。
(3) Union(x, y) —— 合并  
将元素   所在的集合和元素   所在的集合合并为一个集合。
逻辑 ：
1. 找到   的根  rootX = Find(x) 。
2. 找到   的根  rootY = Find(y) 。
3. 如果  rootX != rootY ，将其中一个根指向另一个根（例如  parent[rootX] = rootY ）。
伪代码（基础版） ：Function MakeSet(x):
    parent[x] = x
    rank[x] = 0   #用于后续的优化，记录树的高度/秩
Function Find(x):
    if parent[x] == x:
        return x
    else:
        return Find(parent[x])
Function Union(x, y):
    rootX = Find(x)
    rootY = Find(y)
    if rootX != rootY:
        parent[rootX] = rootY

## 第5页

3. 关键优化策略  
优化一：按秩合并  (Union by Rank)  
解决树过高的问题 。在合并两棵树时，不要随意合并，而是总是 把矮树（秩小的树）挂在原本就高的树
（秩大的树）下面 。
这样可以避免树的高度增加过快，保证树的高度维持在  。
伪代码 ：
优化二：路径压缩  (Path Compression)  
解决重复查询效率低的问题 。在执行  Find(x) 的过程中，既然我们已经费力找到了根节点，不如 顺手
把路径上经过的所有节点直接指向根节点 。
这样，下一次查询这些节点时，一步就能跳到根节点，不需要再递归了。
伪代码（带路径压缩的  Find ） ：
4. 最终的时间复杂度  
如果同时使用了 按秩合并 和 路径压缩 ：
单次操作的平均时间复杂度接近  。
更严谨的说法是  ，其中   是阿克曼函数（ Ackermann function ）的反函数。
这个函数增长极慢，对于宇宙中任何实际规模的  （例如  ）， 。因此，可以认
为它是常数时间。Function Union(x, y):
    rootX = Find(x)
    rootY = Find(y)
    
    if rootX == rootY: return  # 已经在同一个集合，无需合并
    # 谁高谁做父亲
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY
        rank[rootY] = rank[rootY] + 1  # 只有两棵同高树合并，高度才会+1
Function Find(x):
    if parent[x] != x:
        # 递归查找，并将结果直接赋值给  parent[x] （压缩路径）
        parent[x] = Find(parent[x])
    return parent[x]

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_算法_课程MOC|算法 MOC]]
