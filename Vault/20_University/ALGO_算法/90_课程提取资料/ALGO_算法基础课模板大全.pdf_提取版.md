---
id: extract-algo-f0ce9d11
type: extract
status: extracted
course: ALGO
source:
  - "[[91_Raw-Archive/PDF/ALGO_算法基础课模板大全.pdf_课件_未知日期_f0ce9d11.pdf]]"
source_pages: all
source_hash: "f0ce9d1140962cdce3e5294b7983eef368df8e4cf9cda2017e16546abe90bf2d"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 算法基础课模板大全.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

一、基础算法  
快 速 排 序 算 法 模 板  
边界问题
因为边界问题只有这两种组合，不能随意搭配
归 并 排 序 算 法 模 板  void quick_sort(int q[], int l, int r)
{
    //递归的终止情况
    if (l >= r) return;
    
     //选取分界线。这里选数组中间那个数
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    //划分成左右两个部分
    while (i < j)
    {
        do i ++ ; while (q[i] < x);
        do j -- ; while (q[j] > x);
        if (i < j) swap(q[i], q[j]);
    }
    //对左右部分排序
    quick_sort(q, l, j), quick_sort(q, j + 1, r);
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
x不能取q[l]和q[l+r>>1];
quick_sort(q,l,i-1),quick_sort(q,i,r);1
2
x不能取q[r]和q[(l+r+1)>>1];
quick_sort(q,l,j),quick_sort(q,j+1,r);1
2
void merge_sort(int q[], int l, int r)
{
    //递归的终止情况
    if (l >= r) return;
    //第一步：分成子问题
    int mid = l + r >> 1;
    //第二步：递归处理子问题
    merge_sort(q, l, mid);
    merge_sort(q, mid + 1, r);
    
    //第三步：合并子问题
    int k = 0, i = l, j = mid + 1;1
2
3
4
5
6
7
8
9
10
11
12

## 第2页

整 数 二 分 算 法 模 板  
对lower_bound 来 说 ， 它 寻 找 的 就 是 第 一 个 满 足 条 件 “ 值 大 于 等 于 x” 的 元 素 的 位 置 ； 对 upper_bound 函
数来说，它寻找的是第一个满足 “ 值大于  x” 的元素的位置。
浮 点 数 二 分 算 法 模 板      while (i <= mid && j <= r)
        if (q[i] <= q[j]) tmp[k ++ ] = q[i ++ ];
        else tmp[k ++ ] = q[j ++ ];
    while (i <= mid) tmp[k ++ ] = q[i ++ ];
    while (j <= r) tmp[k ++ ] = q[j ++ ];
    //第四步：复制回原数组
    for (i = l, j = 0; i <= r; i ++, j ++ ) q[i] = tmp[j];
}13
14
15
16
17
18
19
20
21
bool check(int x) {/* ... */} // 检查x是否满足某种性质
// 区间[l, r]被划分成 [l, mid] 和 [mid + 1, r] 时使用：
int bsearch_1(int l, int r)
{
    while (l < r)
    {
        int mid = l + r >> 1;
        if (check(mid)) r = mid;    // check()判断 mid 是否满足性质
        else l = mid + 1;//左加右减
    }
    return l;
}
// 区间[l, r]被划分成 [l, mid - 1] 和 [mid, r] 时使用：
int bsearch_2(int l, int r)
{
    while (l < r)
    {
        int mid = l + r + 1 >> 1;//如果下方 else后面是 l 则这里加 1
        if (check(mid)) l = mid;
        else r = mid - 1;//左加右减
    }
    return l;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24

## 第3页

高 精 度 加 法  
高 精 度 减 法  bool check(double x) {/* ... */} // 检查x是否满足某种性质
double bsearch_3(double l, double r)
{
    const double eps = 1e-6;   // eps 表示精度，取决于题目对精度的要求
    while (r - l > eps)
    {
        double mid = (l + r) / 2;
        if (check(mid)) r = mid;
        else l = mid;
    }
    return l;
}1
2
3
4
5
6
7
8
9
10
11
12
13
// C = A + B, A >= 0, B >= 0
vector<int> add(vector<int> &a,vector<int> &b){
    //c为答案
    vector<int> c;
    //t为进位
    int t=0;
    for(int i=0;i<a.size()||i<b.size();i++){
        //不超过a的范围添加 a[i]
        if(i<a.size())t+=a[i];
        //不超过b的范围添加 b[i]
        if(i<b.size())t+=b[i];
        //取当前位的答案
        c.push_back(t%10);
        //是否进位
        t/=10;
    }
    //如果t!=0的话向后添加 1
    if(t)c.push_back(1);
    return c;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
// C = A - B, 满足 A >= B, A >= 0, B >= 0
vector<int> sub(vector<int> &A, vector<int> &B)
{
    //答案
    vector<int> C;
    //遍历最大的数
    for (int i = 0, t = 0; i < A.size(); i ++ )
    {
        //t为进位
        t = A[i] - t;
        //不超过B的范围 t=A[i]-B[i]-t;
        if (i < B.size()) t -= B[i];
        //合二为一，取当前位的答案
        C.push_back((t + 10) % 10);1
2
3
4
5
6
7
8
9
10
11
12
13
14

## 第4页

高 精 度 比 大 小 （ cmp 函 数 ）  
高 精 度 乘 低 精 度  
高 精 度 乘 高 精 度  
高精度加减乘除 ：https://www .bilibili.com/video/BV1LA41 1v7mt/        //t<0则t=1
        if (t < 0) t = 1;
        //t>=0则 t=0
        else t = 0;
    }
    //去除前导零
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}15
16
17
18
19
20
21
22
23
//高精度比大小
bool cmp(vector<int> &A, vector<int> &B) {
    if (A.size() != B.size())
        return A.size() > B.size();
    for (int i = A.size() - 1; i >= 0; i -- )
        if (A[i] != B[i])
            return A[i] > B[i];
    return true;
}1
2
3
4
5
6
7
8
9
// C = A * b, A >= 0, b >= 0
vector<int> mul(vector<int> &A, int b)
{
    //类似于高精度加法
    vector<int> C;
    //t为进位
    int t = 0;
    for (int i = 0; i < A.size() || t; i ++ )
    {
        //不超过A的范围 t=t+A[i]*b
        if (i < A.size()) t += A[i] * b;
        //取当前位的答案
        C.push_back(t % 10);
        //进位
        t /= 10;
    }
    //去除前导零
    while (C.size() > 1 && C.back() == 0) C.pop_back();
    return C;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

## 第5页

高 精 度 除 低 精 度  
高 精 度 除 高 精 度  
高精度加减乘除 ：https://www .bilibili.com/video/BV1LA41 1v7mt/vector<int> mul(vector<int> &A, vector<int> &B) {
    vector<int> C(A.size() + B.size()); // 初始化为  0， C 的 size 可以大一点
    for (int i = 0; i < A.size(); i++)
        for (int j = 0; j < B.size(); j++)
            C[i + j] += A[i] * B[j];
    for (int i = 0,t = 0; i < C.size(); i++) { // i = C.size() - 1 时  t 一定小于  10
        t += C[i];
        C[i] = t % 10;
        t /= 10;
    }
    while (C.size() > 1 && C.back() == 0) C.pop_back(); // 必须要去前导  0 ，因为最高
位很可能是  0
    return C;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
// A / b = C ... r, A >= 0, b > 0
vector<int> div(vector<int> &A, int b, int &r)//高精度A，低精度 b ，余数 r
{
    vector<int> C;//答案
    r = 0;
    for (int i = A.size() - 1; i >= 0; i -- )
    {
        r = r * 10 + A[i];//补全r>=b
        C.push_back(r / b);//取当前位的答案
        r %= b;//r%b为下一次计算
    }
    reverse(C.begin(), C.end());//倒序为答案
    while (C.size() > 1 && C.back() == 0) C.pop_back();//去除前导零
    return C;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
vector<int> div(vector<int> &A, vector<int> &B, vector<int> &r) {
    vector<int> C;
    if (!cmp(A, B)) {
        C.push_back(0);
        r.assign(A.begin(), A.end());
        return C;
    }
    int j = B.size();
    r.assign(A.end() - j, A.end());
    while (j <= A.size()) {
        int k = 0;
        while (cmp(r, B)) {
            r = sub(r, B);
            k ++;
        }1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

## 第6页

一 维 前 缀 和  
前 缀 和 可 以 用 于 快 速 计 算 一 个 序 列 的 区 间 和 ， 也 有 很 多 问 题 里 不 是 直 接 用 前 缀 和 ， 但 是 借 用 了 前 缀
和的思想。  
应用
二 维 前 缀 和  
应用        C.push_back(k);
        if (j < A.size())
            r.insert(r.begin(), A[A.size() - j - 1]);
        if (r.size() > 1 && r.back() == 0)
            r.pop_back();
        j++;
    }
    reverse(C.begin(), C.end());
    while (C.size() > 1 && C.back() == 0)
        C.pop_back();
    return C;
}16
17
18
19
20
21
22
23
24
25
26
27
预处理:s[i]=a[i]+a[i-1]
求区间[l,r]:sum=s[r]-s[l-1]
"前缀和数组 "和"原数组"可以合二为一1
2
3
const int N=100010;
int a[N];
int main(){
    int n,m;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%d",&a[i]);
    for(int i=1;i<=n;i++)a[i]=a[i-1]+a[i];
    scanf("%d",&m);
    while(m--){
        int l,r;
        scanf("%d%d",&l,&r);
        printf("%d\n",a[r]-a[l-1]);
    }
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
计算矩阵的前缀和： s[x][y] = s[x - 1][y] + s[x][y -1] - s[x-1][y-1] + a[x][y]
以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵的和为：
计算子矩阵的和： s = s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 -1]1
2
3
int s[1010][1010];
int n,m,q;1
2
3
4

## 第7页

一 维 差 分  
差分是前缀和的逆运算，对于一个数组 a ，其差分数组 b 的每一项都是 a [ i ] 和前一项 a [ i − 1 ] 的差。
 注意：差分数组和原数组必须分开存放！！！！  
应用
二 维 差 分  
应用int main(){
    scanf("%d%d%d",&n,&m,&q);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            scanf("%d",&s[i][j]);
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            s[i][j]+=s[i-1][j]+s[i][j-1]-s[i-1][j-1];
    while(q--){
        int x1,y1,x2,y2;
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        printf("%d\n",s[x2][y2]-s[x2][y1-1]-s[x1-1][y2]+s[x1-1][y1-1]);
    }
    return 0;
}5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
给区间[l, r]中的每个数加上 c ： B[l] += c, B[r + 1] -= c 1
using namespace std;
int a[100010],s[100010];
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++)cin>>a[i];   
    for(int i=1;i<=n;i++)s[i]=a[i]-a[i-1];// 读入并计算差分数组
    while(m--){
        int l,r,c;
        cin>>l>>r>>c;
        s[l]+=c;
        s[r+1]-=c;// 在原数组中将区间 [l, r] 加上 c
    }
    for(int i=1;i<=n;i++){
        s[i]+=s[i-1];
        cout<<s[i]<<' ';
    }// 给差分数组计算前缀和，就求出了原数组
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
给以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵中的所有元素加上 c ：
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c1
2

## 第8页

关于前缀和  与  差分的相关博客链接： https://blog.csdn.net/qq_39757593/article/details/129219491
位 运 算  const int N = 1e3 + 10;
int a[N][N], b[N][N];
void insert(int x1, int y1, int x2, int y2, int c)
{
    b[x1][y1] += c;
    b[x2 + 1][y1] -= c;
    b[x1][y2 + 1] -= c;
    b[x2 + 1][y2 + 1] += c;
}
int main()
{
    int n, m, q;
    cin >> n >> m >> q;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            cin >> a[i][j];
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            insert(i, j, i, j, a[i][j]);      //构建差分数组
        }
    }
    while (q--)
    {
        int x1, y1, x2, y2, c;
        cin >> x1 >> y1 >> x2 >> y2 >> c;
        insert(x1, y1, x2, y2, c);//加c
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            b[i][j] += b[i - 1][j] + b[i][j - 1] - b[i - 1][j - 1];  //二维前缀和
        }
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            printf("%d ", b[i][j]);
        }
        printf("\n");
    }
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
求n的第k位数字: n >> k & 1
返回n的最后一位 1 ： lowbit(n) = n & -n1
2

## 第9页

双 指 针 算 法  
离 散 化  
离 散 化 的 本 质 是 建 立 了 一 段 数 列 到 自 然 数 之 间 的 映 射 关 系 （ value -> index) ， 通 过 建 立 新 索 引 ， 来 缩
小目标区间，使得可以进行一系列连续数组可以进行的操作比如二分，前缀和等 …
离散化首先需要排序去重：
1. 排序： sort(alls.begin(),alls.end())
2. 去重： alls.earse(unique(alls.begin(),alls.end()),alls.end());
应用for (int i = 0, j = 0; i < n; i ++ )
{
    while (j < i && check(i, j)) j ++ ;
    // 具体问题的逻辑
}
常见问题分类：
    (1) 对于一个序列，用两个指针维护一段区间
    (2) 对于两个序列，维护某种次序，比如归并排序中合并两个有序序列的操作1
2
3
4
5
6
7
8
vector<int> alls; // 存储所有待离散化的值
sort(alls.begin(), alls.end()); // 将所有值排序
alls.erase(unique(alls.begin(), alls.end()), alls.end());   // 去掉重复元素
// 二分求出 x对应的离散化的值
int find(int x) // 找到第一个大于等于 x 的位置
{
    int l = 0, r = alls.size() - 1;
    while (l < r)
    {
        int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1; // 映射到 1, 2, ...n
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
typedef pair<int, int> PII;
const int N = 300010;
int n, m;
int a[N], s[N];
vector<int> alls;//存入下标容器
vector<PII> add, query;//add增加容器，存入对应下标和增加的值的大小
//query存入需要计算下标区间和的容器
int find(int x)
{
    int l = 0, r = alls.size() - 1;
    while (l < r)//查找大于等于 x 的最小的值的下标
    {1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

## 第10页

区 间 合 并          int mid = l + r >> 1;
        if (alls[mid] >= x) r = mid;
        else l = mid + 1;
    }
    return r + 1;//因为使用前缀和，其下标要 +1 可以不考虑边界问题
}
int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i ++ )
    {
        int x, c;
        cin >> x >> c;
        add.push_back({x, c});//存入下标即对应的数值 c
        alls.push_back(x);//存入数组下标 x=add.first
    }
    for (int i = 0; i < m; i ++ )
    {
        int l, r;
        cin >> l >> r;
        query.push_back({l, r});//存入要求的区间
        alls.push_back(l);//存入区间左右下标
        alls.push_back(r);
    }
    // 区间去重
    sort(alls.begin(), alls.end());
    alls.erase(unique(alls.begin(), alls.end()), alls.end());
    // 处理插入
    for (auto item : add)
    {
        int x = find(item.first);//将add容器的 add.secend 值存入数组 a[] 当中，
        a[x] += item.second;//在去重之后的下标集合 alls 内寻找对应的下标并添加数值
    }
    // 预处理前缀和
    for (int i = 1; i <= alls.size(); i ++ ) s[i] = s[i - 1] + a[i];
    // 处理询问
    for (auto item : query)
    {
        int l = find(item.first), r = find(item.second);//在下标容器中查找对应的左右
两端[l~r]下标，然后通过下标得到前缀和相减再得到区间 a[l~r] 的和
        cout << s[r] - s[l - 1] << endl;
    }
    return 0;
}16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
// 将所有存在交集的区间合并 1

## 第11页

二、数据结构  
单 链 表  
应用void merge(vector<PII> &segs)
{
    vector<PII> res;
    sort(segs.begin(), segs.end());
    int st = -2e9, ed = -2e9;
    for (auto seg : segs)
        if (ed < seg.first)
        {
            if (st != -2e9) res.push_back({st, ed});
            st = seg.first, ed = seg.second;
        }
        else ed = max(ed, seg.second);
    if (st != -2e9) res.push_back({st, ed});
    segs = res;
}2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
const int N=100010;
int head,e[N],ne[N],idx;
//初始化
void init(){
    head=-1;
    idx=0;
}
//在链表头部添加节点
void add_to_head(int x){
    e[idx]=x,ne[idx]=head,head=idx++;
}
//在位置k添加节点 x
void add(int k,int x){
    e[idx]=x,ne[idx]=ne[k],ne[k]=idx++;
}
//删除位置 k的节点
void remove(int k){
    ne[k]=ne[ne[k]];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
int main(){
    int m;
    init();
    cin>>m;
    while(m--){
        int k,x;1
2
3
4
5
6

## 第12页

双 链 表  
应用        char op;
        cin>>op;
        if(op=='H'){
            cin>>x;
            add_to_head(x);
        }else if(op=='D'){
            cin>>k;
            if(!k)head=ne[head];
            remove(k-1);
        }else {
            cin>>k>>x;
            add(k-1,x);
        }
    }
    for(int i=head;i!=-1;i=ne[i])cout<<e[i]<<' ';
    cout<<endl;
    return 0;
}7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
const int N=100010;
int e[N],l[N],r[N],idx;
//初始化
void init(){
    l[1]=0;
    r[0]=1;
    idx=2;
}
//在节点a的右边插入一个数 x
void insert(int a,int x){
    e[idx]=x;
    l[idx]=a,r[idx]=r[a];
    l[r[a]]=idx,r[a]=idx++;
}
//删除节点 a
void remove(int a){
    l[r[a]]=l[a];
    r[l[a]]=r[a];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
int main(){
    int m;
    cin>>m;
    init();
    while(m--){
        string op;
        cin>>op;
        int k,x;
        if(op=="L"){//在最左端插入数 x
            cin>>x;1
2
3
4
5
6
7
8
9
10

## 第13页

栈  
应用            insert(0,x);
        }else if(op=="R"){//在最右端插入数 x
            cin>>x;
            insert(l[1],x);
        }else if(op=="D"){//删除第k个插入的数
            cin>>k;
            remove(k+1);
        }else if(op=="IL"){//在第k个位置的左侧插入一个数
            cin>>k>>x;
            insert(l[k+1],x);
        }else if(op=="LR"){//在第k个位置的右侧插入一个数
            cin>>k>>x;
            insert(k+1,x);
        }
    }
    for(int i=r[0];i!=1;i=r[i])printf("%d ",e[i]);
    cout<<endl;
    return 0;
}11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
// tt表示栈顶
int stk[N], tt = 0;
// 向栈顶插入一个数
stk[ ++ tt] = x;
// 从栈顶弹出一个数
tt -- ;
// 栈顶的值
stk[tt];
// 判断栈是否为空，如果  tt > 0 ，则表示不为空
if (tt > 0)
{
}1
2
3
4
5
6
7
8
9
10
11
12
13
const int N=100010;
int stk[N],tt;
int main(){
    int m;
    cin>>m;
    while(m--){
        string op;
        int x;
        cin>>op;
        if(op=="push"){
            cin>>x;
            stk[tt++]=x;
        }else if(op=="pop"){
            tt--;
        }else if(op=="query"){
            cout<<stk[tt-1]<<endl;
        }else{
            if(!tt)cout<<"YES"<<endl;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

## 第14页

队 列  
普通队列  
应用            else cout<<"NO"<<endl;
        }
    }
    return 0;
}20
21
22
23
24
// hh 表示队头， tt 表示队尾
int q[N], hh = 0, tt = -1;
// 向队尾插入一个数
q[ ++ tt] = x;
// 从队头弹出一个数
hh ++ ;
// 队头的值
q[hh];
// 判断队列是否为空，如果  hh <= tt ，则表示不为空
if (hh <= tt)
{
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
int const N=100010;
int que[N],hh,tt=-1;
int main(){
    int m;
    cin>>m;
    while(m--){
        string op;
        int x;
        cin>>op;
        if(op=="push"){
            cin>>x;
            que[++tt]=x;
        }else if(op=="query"){
            cout<<que[hh]<<endl;
        }else if(op=="pop"){
            hh++;
        }else{
            if(hh>tt)cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
    }
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第15页

循环队列  
单 调 栈  
应用
单 调 队 列  // hh 表示队头， tt 表示队尾的后一个位置
int q[N], hh = 0, tt = 0;
// 向队尾插入一个数
q[tt ++ ] = x;
if (tt == N) tt = 0;
// 从队头弹出一个数
hh ++ ;
if (hh == N) hh = 0;
// 队头的值
q[hh];
// 判断队列是否为空，如果 hh != tt ，则表示不为空
if (hh != tt)
{
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
常见模型：找出每个数左边离它最近的比它大/小的数
int tt = 0;
for (int i = 1; i <= n; i ++ )
{
    while (tt && check(stk[tt], i)) tt -- ;
    stk[ ++ tt] = i;
}1
2
3
4
5
6
7
找出每个数左边离它最近的比它大/小的数
stack<int> stk;
int main(){
    int n;
    cin >> n;
    stk.push(-1);
    for (int i = 0; i < n; i ++){
        int x; 
        cin >> x;
        while (stk.size() && stk.top() >= x) stk.pop();
        cout << stk.top() << " ";
        stk.push(x);
    }
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

## 第16页

KMP 字 符 串 匹 配  
下标从 1 开始的 kmp 算法常见模型：找出滑动窗口中的最大值/最小值
int hh = 0, tt = -1;
for (int i = 0; i < n; i ++ )
{
    while (hh <= tt && check_out(q[hh])) hh ++ ;  // 判断队头是否滑出窗口
    while (hh <= tt && check(q[tt], i)) tt -- ;
    q[ ++ tt] = i;
}1
2
3
4
5
6
7
8
const int N = 1000010;
int a[N];
int main()
{
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i ++ ) cin >> a[i];//读入数据
    deque<int> q;
    for(int i = 1; i <= n; i++)
    {
        while(q.size() && q.back() > a[i]) //新进入窗口的值小于队尾元素，则队尾出队列
            q.pop_back();
        q.push_back(a[i]);//将新进入的元素入队
        if(i - k >= 1 && q.front() == a[i - k])//若队头是否滑出了窗口，队头出队 
            q.pop_front();
        if(i >= k)//当窗口形成，输出队头对应的值
            cout << q.front() <<" ";
    }
    q.clear();
    cout << endl;
    //最大值亦然
    for(int i = 1; i <= n; i++)
    {
        while(q.size() && q.back() < a[i]) q.pop_back();
        q.push_back(a[i]);
        if(i - k >= 1 && a[i - k] == q.front()) q.pop_front(); 
        if(i >= k) cout << q.front() << " ";
    }
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
const int N = 100010, M = 1000010;
int n, m;
int ne[N];
char s[M], p[N];
int main()
{
    cin >> n >> p + 1 >> m >> s + 1;
    for (int i = 2, j = 0; i <= n; i ++ )
    {
        while (j && p[i] != p[j + 1]) j = ne[j];
        if (p[i] == p[j + 1]) j ++ ;1
2
3
4
5
6
7
8
9
10
11

## 第17页

下标从 0 开始的 kmp 算法        ne[i] = j;
    }//处理ne数组
    for (int i = 1, j = 0; i <= m; i ++ )
    {
        while (j && s[i] != p[j + 1]) j = ne[j];
        if (s[i] == p[j + 1]) j ++ ;
        if (j == n)
        {
            printf("%d ", i - n);
            j = ne[j];
        }
    }//匹配算法
    return 0;
}12
13
14
15
16
17
18
19
20
21
22
23
24
25
// s[]是长文本， p[] 是模式串， n 是 s 的长度， m 是 p 的长度
求模式串的 Next数组：
for (int i = 2, j = 0; i <= m; i ++ )
{
    while (j && p[i] != p[j + 1]) j = ne[j];
    if (p[i] == p[j + 1]) j ++ ;
    ne[i] = j;
}
// 匹配
for (int i = 1, j = 0; i <= n; i ++ )
{
    while (j && s[i] != p[j + 1]) j = ne[j];
    if (s[i] == p[j + 1]) j ++ ;
    if (j == m)
    {
        j = ne[j];
        // 匹配成功后的逻辑
    }
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
const int N = 1000010;
int n, m;
char s[N], p[N];
int ne[N];
int main()
{
    cin >> m >> p >> n >> s;
    ne[0] = -1;
    for (int i = 1, j = -1; i < m; i ++ )
    {
        while (j >= 0 && p[j + 1] != p[i]) j = ne[j];
        if (p[j + 1] == p[i]) j ++ ;
        ne[i] = j;
    }
    for (int i = 0, j = -1; i < n; i ++ )
    {
        while (j != -1 && s[i] != p[j + 1]) j = ne[j];
        if (s[i] == p[j + 1]) j ++ ;
        if (j == m - 1)1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

## 第18页

Trie 树  
Trie 树是一种多叉树的结构，每个节点保存一个字符，一条路径表示一个字符串。
相关链接： https://www .acwing.com/solution/content/27771/        {
            cout << i - j << ' ';
            j = ne[j];
        }
    }
    return 0;
}22
23
24
25
26
27
28
int son[N][26], cnt[N], idx;
// 0号点既是根节点，又是空节点
// son[][]存储树中每个节点的子节点
// cnt[]存储以每个节点结尾的单词数量
// 插入一个字符串
void insert(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) son[p][u] = ++ idx;
        p = son[p][u];
    }
    cnt[p] ++ ;
}
// 查询字符串出现的次数
int query(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) return 0;
        p = son[p][u];
    }
    return cnt[p];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
const int N = 100010;
int son[N][26], cnt[N], idx;
char str[N];
void insert(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) son[p][u] = ++ idx;1
2
3
4
5
6
7
8
9
10
11
12

## 第19页

并 查 集          p = son[p][u];
    }
    cnt[p] ++ ;
}//插入
int query(char *str)
{
    int p = 0;
    for (int i = 0; str[i]; i ++ )
    {
        int u = str[i] - 'a';
        if (!son[p][u]) return 0;
        p = son[p][u];
    }
    return cnt[p];
}//查询
int main()
{
    int n;
    scanf("%d", &n);
    while (n -- )
    {
        char op[2];
        scanf("%s%s", op, str);
        if (*op == 'I') insert(str);
        else printf("%d\n", query(str));
    }
    return 0;
}13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
(1)朴素并查集：
    int p[N]; //存储每个点的祖宗节点
    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
    // 初始化，假定节点编号是 1~n
    for (int i = 1; i <= n; i ++ ) p[i] = i;
    // 合并a和 b所在的两个集合：
    p[find(a)] = find(b);
(2)维护size的并查集：
    int p[N], size[N];
    //p[]存储每个点的祖宗节点 , size[] 只有祖宗节点的有意义，表示祖宗节点所在集合中的点的
数量1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

## 第20页

应用    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
    // 初始化，假定节点编号是 1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        size[i] = 1;
    }
    // 合并a和 b所在的两个集合：
    size[find(b)] += size[find(a)];
    p[find(a)] = find(b);
(3)维护到祖宗节点距离的并查集：
    int p[N], d[N];
    //p[]存储每个点的祖宗节点 , d[x] 存储 x 到 p[x] 的距离
    // 返回x的祖宗节点
    int find(int x)
    {
        if (p[x] != x)
        {
            int u = find(p[x]);
            d[x] += d[p[x]];
            p[x] = u;
        }
        return p[x];
    }
    // 初始化，假定节点编号是 1~n
    for (int i = 1; i <= n; i ++ )
    {
        p[i] = i;
        d[i] = 0;
    }
    // 合并a和 b所在的两个集合：
    p[find(a)] = find(b);
    d[find(a)] = distance; // 根据具体问题，初始化 find(a) 的偏移量23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
const int N=100010;
int p[N],n,m;
int find(int x){//找到祖宗节点 + 路径压缩
    if(p[x]!=x)p[x]=find(p[x]);
    return p[x];
}
int main(){
    scanf("%d%d",&n,&m);1
2
3
4
5
6
7
8
9
10

## 第21页

堆  
应用：堆排序    for(int i=1;i<=n;i++)p[i]=i;
    while(m--){
        char op[2];
        int a,b;
        scanf("%s%d%d",op,&a,&b);
        if(op[0]=='M')p[find(a)]=find(b);
        else {
            if(find(a)==find(b))puts("Yes");
            else puts("No");
        }
    }
    return 0;
}11
12
13
14
15
16
17
18
19
20
21
22
23
// h[N]存储堆中的值 , h[1] 是堆顶， x 的左儿子是 2x, 右儿子是 2x + 1
// ph[k]存储第 k 个插入的点在堆中的位置
// hp[k]存储堆中下标是 k 的点是第几个插入的
int h[N], ph[N], hp[N], size;
// 交换两个点，及其映射关系
void heap_swap(int a, int b)
{
    swap(ph[hp[a]],ph[hp[b]]);
    swap(hp[a], hp[b]);
    swap(h[a], h[b]);
}
void down(int u)
{
    int t = u;
    if (u * 2 <= size && h[u * 2] < h[t]) t = u * 2;
    if (u * 2 + 1 <= size && h[u * 2 + 1] < h[t]) t = u * 2 + 1;
    if (u != t)
    {
        heap_swap(u, t);
        down(t);
    }
}
void up(int u)
{
    while (u / 2 && h[u] < h[u / 2])
    {
        heap_swap(u, u / 2);
        u >>= 1;
    }
}
// O(n)建堆
for (int i = n / 2; i; i -- ) down(i);1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
const int N=100010;
int heap[N],cnt;1
2

## 第22页

一 般 hash  void down(int u){
    int t=u;
    if(u*2<=cnt&&heap[u*2]<=heap[t])t=u*2;
    if(u*2+1<=cnt&&heap[u*2+1]<=heap[t])t=u*2+1;
    if(t!=u){
        swap(heap[t],heap[u]);
        down(t);
    }
}//down操作
void up(int u){
    while(u/2&&heap[u/2]>heap[u]){
        swap(heap[u/2],heap[u]);
        u>>=1;
    }
}//up操作
int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)scanf("%d",&heap[i]);
    cnt=n;
    for(int i=n/2;i;i--)down(i);
    while(m--){
        printf("%d ",heap[1]);
        heap[1]=heap[cnt--];
        down(1);
    }
    return 0;
}3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
(1) 拉链法
    int h[N], e[N], ne[N], idx;
    // 向哈希表中插入一个数
    void insert(int x)
    {
        int k = (x % N + N) % N;
        e[idx] = x;
        ne[idx] = h[k];
        h[k] = idx ++ ;
    }
    // 在哈希表中查询某个数是否存在
    bool find(int x)
    {
        int k = (x % N + N) % N;
        for (int i = h[k]; i != -1; i = ne[i])
            if (e[i] == x)
                return true;
        return false;
    }1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23

## 第23页

字 符 串 哈 希  
STL  (2) 开放寻址法
    int h[N];
    // 如果x在哈希表中，返回 x 的下标；如果 x 不在哈希表中，返回 x 应该插入的位置
    int find(int x)
    {
        int t = (x % N + N) % N;
        while (h[t] != null && h[t] != x)
        {
            t ++ ;
            if (t == N) t = 0;
        }
        return t;
    }24
25
26
27
28
29
30
31
32
33
34
35
36
37
核心思想：将字符串看成 P 进制数， P 的经验值是 131 或 13331 ，取这两个值的冲突概率低
小技巧：取模的数用 2^64 ，这样直接用 unsigned long long存储，溢出的结果就是取模的结果
typedef unsigned long long ULL;
ULL h[N], p[N]; // h[k]存储字符串前 k 个字母的哈希值 , p[k] 存储  P^k mod 2^64
// 初始化
p[0] = 1;
for (int i = 1; i <= n; i ++ )
{
    h[i] = h[i - 1] * P + str[i];
    p[i] = p[i - 1] * P;
}
// 计算子串  str[l ~ r] 的哈希值
ULL get(int l, int r)
{
    return h[r] - h[l - 1] * p[r - l + 1];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

## 第24页

视频讲解： 100 STL 容器哔哩哔哩 bilibili
vector, 变长数组，倍增的思想
    size()  返回元素个数
    empty()  返回是否为空
    clear()  清空
    front()/back()
    push_back()/pop_back()
    begin()/end()
    []
    支持比较运算，按字典序
pair<int, int>
    first, 第一个元素
    second, 第二个元素
    支持比较运算，以 first 为第一关键字，以 second 为第二关键字（字典序）
string，字符串
    size()/length()  返回字符串长度
    empty()
    clear()
    substr(起始下标，(子串长度))  返回子串
    c_str()  返回字符串所在字符数组的起始地址
queue, 队列
    size()
    empty()
    push()  向队尾插入一个元素
    front()  返回队头元素
    back()  返回队尾元素
    pop()  弹出队头元素
priority_queue, 优先队列，默认是大根堆
    size()
    empty()
    push()  插入一个元素
    top()  返回堆顶元素
    pop()  弹出堆顶元素
    定义成小根堆的方式： priority_queue<int, vector<int>, greater<int>> q;
stack, 栈1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39

## 第25页

size()
    empty()
    push()  向栈顶插入一个元素
    top()  返回栈顶元素
    pop()  弹出栈顶元素
deque, 双端队列
    size()
    empty()
    clear()
    front()/back()
    push_back()/pop_back()
    push_front()/pop_front()
    begin()/end()
    []
set, map, multiset, multimap, 基于平衡二叉树（红黑树），动态维护有序序列
    size()
    empty()
    clear()
    begin()/end()
    ++, -- 返回前驱和后继，时间复杂度 O(logn)
    set/multiset
        insert()  插入一个数
        find()  查找一个数
        count()  返回某一个数的个数
        erase()
            (1) 输入是一个数 x，删除所有 x   O(k + logn)
            (2) 输入一个迭代器，删除这个迭代器
        lower_bound()/upper_bound()
            lower_bound(x)  返回大于等于 x的最小的数的迭代器
            upper_bound(x)  返回大于x的最小的数的迭代器
    map/multimap
        insert()  插入的数是一个 pair
        erase()  输入的参数是 pair 或者迭代器
        find()
        []  注意multimap不支持此操作。 时间复杂度是 O(logn)
        lower_bound()/upper_bound()
unordered_set, unordered_map, unordered_multiset, unordered_multimap, 哈希表
    和上面类似，增删改查的时间复杂度是 O(1)
    不支持 lower_bound()/upper_bound()， 迭代器的++，--
bitset, 圧位
    bitset<10000> s;
    ~, &, |, ^
    >>, <<
    ==, !=
    []
    count()  返回有多少个 1
    any()  判断是否至少有一个 1
    none()  判断是否全为 0
    set()  把所有位置成 1
    set(k, v)  将第k位变成 v
    reset()  把所有位变成 0
    flip()  等价于~
    flip(k) 把第k位取反40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100

## 第26页

三、搜索与图论  
树 与 图 的 存 储  
树是一种特殊的图，与图的存储方式相同。
对于无向图中的边 ab ，存储两条有向边 a->b, b->a 。
因此我们可以只考虑有向图的存储。
邻接矩阵  
邻接矩阵： g[a][b] 存储边 a->b 的距离
邻接表  
树 与 图 的 遍 历  
时间复杂度 O(n+m) ， n 表示点数， m 表示边数
深度优先遍历  // 对于每个点 k，开一个单链表，存储 k 所有可以走到的点。 h[k] 存储这个单链表的头结点
int h[N], e[N], ne[N], idx;
// 添加一条边 a->b
void add(int a, int b)
{
    //存下b的值， b下一个指向 a 的下个一节点， a 的下一个节点指向 b
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}
// 初始化
idx = 0;
memset(h, -1, sizeof h);1
2
3
4
5
6
7
8
9
10
11
int dfs(int u)
{
    st[u] = true; // st[u] 表示点 u 已经被遍历过
    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j]) dfs(j);
    }
}1
2
3
4
5
6
7
8
9
10

## 第27页

应 用 ： 数 字 全 排 列  
应 用 ： 树 的 重 心  #include <iostream>
using namespace std;
int res[10],b[10],n;
void dfs(int k){
    if(k==n){//k==n则输出 n个数字
        for(int i=0;i<n;i++)printf("%d ",res[i]);
        cout<<endl;
    }
    for(int i=1;i<=n;i++){
        if(!b[i]){//判断是否被用过
            res[k]=i;//当前k位存入位置
            b[i]=1;//表示被占用
            dfs(k+1);
            b[i]=0;//恢复现场
        }
    }
}
int main(){
    cin>>n;
    dfs(0);//从0开始枚举
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 100010, M = N * 2;//无向图n条边时，最多 2n 个 idx ，因为每条边在邻接表中会出
现两次
int n;//n个结点 ,n-1条边
int h[N], e[M], ne[M], idx;//n个链表头， e每一个结点的值， ne 每一个结点的 next 指针
int ans = N;//最小的最大值
bool st[N];//状态数组，防止子节点搜索父节点
void add(int a, int b)//a->b
{//e记录当前点的值 ( 地址 -> 值 ),ne 下一点的地址 ( 地址 -> 地址 ) ， h 记录指向的第一个点的地址 ( 值 ->
地址)
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}//头插法
int dfs(int u)//通过h数组找到子结点的向
{
    st[u] = true;//st标记当前点被搜过
    int size = 0, sum = 0;
    //size删掉元素后各个子连通块的最大值1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26

## 第28页

应 用 ： n- 皇 后 问 题  
    //sum当前子树大小，遍历叶节点时，返回 1
    for (int i = h[u]; i != -1; i = ne[i])//遍历单链表，链表末端初始化为 -1
    {
        int j=e[i];
        if(st[j])continue;//此处防逆向 dfs
        int s = dfs(j);//s各个子连通块的大小
        size = max(size, s);//size删掉元素后各个连通块的最大值
        sum += s;//各个连通块大小之和
    }
    size = max(size, n - sum - 1);//判断最大子连通块与父连通块的最大值
    ans = min(ans, size);//全局变量 ans存最小的最大值
//注意：本题若求最大的最大值，则只需去除任意叶节点即可，即 n-1
    return sum + 1;//各个子连通块，当前结点之和
}
int main()
{
    scanf("%d", &n);
    memset(h, -1, sizeof h);//n个头节点全部指向 -1
    for (int i = 0; i < n - 1; i ++ )//n个结点， n-1条边
    {
        int a, b;
        scanf("%d%d", &a, &b);
        add(a, b), add(b, a);//不知道子节点还是父节点，所以需要建两条边可以双向查找
    }
    dfs(1);//结点编号为 1~n 且可能只有一个结点，则参数只能为 1
    printf("%d\n", ans);
    return 0;
}27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
using namespace std;
const int N = 11;
char q[N][N];//存储棋盘
bool dg[N * 2], udg[N * 2], cor[N];//点对应的两个斜线以及列上是否有皇后1
2
3
4
5
6

## 第29页

宽度优先遍历  int n;
void dfs(int r)
{
    if(r == n)//放满了棋盘，输出棋盘
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
                cout << q[i][j];
            cout << endl;
        }
        cout << endl;
        return;
    }
    for(int i = 0; i < n; i++)//第 r 行，第  i 列  是否放皇后
    {
        if(!cor[i] && !dg[i + r] && !udg[n - i + r])//不冲突，放皇后
        {
            q[r][i] = 'Q';
            cor[i] = dg[i + r] = udg[n - i + r] = 1;//对应的 列，  斜线  状态改变
            dfs(r + 1);//处理下一行
            cor[i] = dg[i + r] = udg[n - i + r] = 0;//恢复现场
            q[r][i] = '.';
        }
    }
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < n; j ++ )
            q[i][j] = '.';
    dfs(0);
    return 0;
}7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
queue<int> q;
st[1] = true; // 表示1号点已经被遍历过
q.push(1);
while (q.size())
{
    int t = q.front();
    q.pop();
    
    for (int i = h[t]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])
        {
            st[j] = true; // 表示点 j已经被遍历过1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

## 第30页

应 用 ： 走 迷 宫  
应 用 ： 八 数 码              q.push(j);
        }
    }
}16
17
18
19
typedef pair<int,int> PII;//声明pair时候必须要在代码前面写上 using namespace std;
const int N=110;
int g[N][N],f[N][N],n,m;
int bfs(int x,int y){
    queue<PII> que;
    que.push({x,y});
    int dx[4]={0,1,0,-1},dy[4]={1,0,-1,0};
    while(!que.empty()){
        PII t=que.front();
        que.pop();
        g[t.first][t.second]=1;
        for(int i=0;i<4;i++){
            int a=t.first+dx[i],b=t.second+dy[i];
            if(a>=0&&b>=0&&a<n&&b<m&&!g[a][b]){
                g[a][b]=1;
                f[a][b]=f[t.first][t.second]+1;
                que.push({a,b});
            }
        }
    }
    return f[n-1][m-1];
}
int main(){
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++)
        for(int j=0;j<m;j++)
            scanf("%d",&g[i][j]);
    cout<<bfs(0,0)<<endl;
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
using namespace std;
int bfs(string state) {
    queue<string> q;
    unordered_map<string, int> d;
    int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
    string ed = "12345678x";
    q.push(state);
    d[state] = 0;
    while (q.size()) {
        auto t = q.front();
        q.pop();
        if (t == ed)//等于结果就输出步数1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

## 第31页

拓 扑 排 序  
啥是拓扑排序？
一个 有向图 ，如果图中有入度为  0 的点，就把这个点删掉，同时也删掉这个点所连的边。
一直进行上面出处理，如果所有点都能被删掉，则这个图可以进行拓扑排序。
纯净版              return d[t];
        int distance = d[t];
        int k = t.find('x');//寻找x
        int x = k / 3, y = k % 3;//计算下标
        for (int i = 0; i < 4; i ++ ) {
            int a = x + dx[i], b = y + dy[i];
            if (a >= 0 && a < 3 && b >= 0 && b < 3) {
                swap(t[a * 3 + b], t[k]);//交换
                if (!d.count(t)) {//不存在就入队
                    d[t] = distance + 1;
                    q.push(t);
                }
                swap(t[a * 3 + b], t[k]);//还原
            }
        }
    }
    return -1;
}
int main() {
    char s[2];
    string state;
    for (int i = 0; i < 9; i ++ ) {
        cin >> s;
        state += *s;
    }
    cout<<bfs(state)<<endl;
    return 0;
}16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
bool topsort()
{
    int hh = 0, tt = -1;
    // d[i] 存储点 i 的入度
    for (int i = 1; i <= n; i ++ )
        if (!d[i])
            q[ ++ tt] = i;
    while (hh <= tt)
    {
        int t = q[hh ++ ];
        for (int i = h[t]; i != -1; i = ne[i])1
2
3
4
5
6
7
8
9
10
11
12
13
14

## 第32页

解说版          {
            int j = e[i];
            if (-- d[j] == 0)
                q[ ++ tt] = j;
        }
    }
    // 如果所有点都入队了，说明存在拓扑序列；否则不存在拓扑序列。
    return tt == n - 1;
}15
16
17
18
19
20
21
22
23
24
using namespace std;
const int N = 100010;
int e[N], ne[N], idx; //邻接表存储图
int h[N];//邻接表的每个头链表
int q[N], hh = 0, tt = -1; //队列保存入度为 0 的点，也就是能够输出的点
int n, m; //保存图的点数和边数
int d[N];//保存各个点的入度
void add(int a, int b) {
    e[idx] = b, ne[idx] = h[a], h[a] = idx++;
}
void topsort() {
    for (int i = 1; i <= n; i++) {//遍历一遍顶点的入度。
        if (!d[i])//如果入度为 0，则可以入队列
            q[++tt] = i;
    }
    while (tt >= hh) { //循环处理队列中点的
        int a = q[hh++];
        for (int i = h[a]; i != -1; i = ne[i]) {
            int b = e[i]; //a 有一条边指向 b
            d[b]--;//删除边后， b的入度减 1
            if (!d[b])//如果b的入度减为  0, 则  b 可以输出，入队列
                q[++tt] = b;
        }
    }
    if (tt == n - 1) {//如果队列中的点的个数与图中点的个数相同，则可以进行拓扑排序
        for (int i = 0; i < n; i++)//队列中保存了所有入度为 0 的点，依次输出
            printf("%d ", q[i]);
    } else//如果队列中的点的个数与图中点的个数不相同，则可以进行拓扑排序
        cout << -1;
}
int main() {
    cin >> n >> m; //保存点的个数和边的个数
    memset(h, -1, sizeof h); //初始化领接矩阵
    while (m--) { //依次读入边
        int a, b;
        cin >> a >> b;
        d[b]++;//顶点b的入度 +1
        add(a, b); //添加到邻接矩阵
    }
    topsort();//进行拓扑排序
    return 0;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

## 第33页

Dijkstra 算 法  
朴素版  
时间复杂是 $O(n^2+m)$ ， n 表示点数， m 表示边数
应用}45
int g[N][N];  // 存储每条边
int dist[N];  // 存储1号点到每个点的最短距离
bool st[N];   // 存储每个点的最短路是否已经确定
// 求1号点到 n号点的最短路，如果不存在则返回 -1
int dijkstra()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    for (int i = 0; i < n - 1; i ++ )
    {
        int t = -1;     // 在还未确定最短路的点中，寻找距离最小的点
        for (int j = 1; j <= n; j ++ )
            if (!st[j] && (t == -1 || dist[t] > dist[j]))
                t = j;
        // 用t更新其他点的距离
        for (int j = 1; j <= n; j ++ )
            dist[j] = min(dist[j], dist[t] + g[t][j]);
        st[t] = true;
    }
    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
const int N = 510, M = 100010;
int h[N], e[M], ne[M], w[M], idx;//邻接表存储图
int state[N];//state 记录是否找到了源点到该节点的最短距离
int dist[N];//dist 数组保存源点到其余各个节点的距离
int n, m;//图的节点个数和边数
void add(int a, int b, int c)//插入边
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx++;
}
void Dijkstra()
{
    memset(dist, 0x3f, sizeof(dist));//dist 数组的各个元素为无穷大
    dist[1] = 0;//源点到源点的距离为置为  0
    for (int i = 0; i < n; i++)
    {1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

## 第34页

堆优化版  
时间复杂度 $O(mlogn)$ ， n 表示点数， m 表示边数        int t = -1;
        for (int j = 1; j <= n; j++)//遍历 dist 数组，找到没有确定最短路径的节点中距离
源点最近的点 t
        {
            if (!state[j] && (t == -1 || dist[j] < dist[t]))
                t = j;
        }
        state[t] = 1;//state[i] 置为  1 。
        for (int j = h[t]; j != -1; j = ne[j])//遍历 t 所有可以到达的节点  i
        {
            int i = e[j];
            dist[i] = min(dist[i], dist[t] + w[j]);//更新 dist[j]
        }
    }
}
int main()
{
    memset(h, -1, sizeof(h));//邻接表初始化
    cin >> n >> m;
    while (m--)//读入 m 条边
    {
        int a, b, w;
        cin >> a >> b >> w;
        add(a, b, w);
    }
    Dijkstra();
    if (dist[n] != 0x3f3f3f3f)//如果dist[n]被更新了，则存在路径
        cout << dist[n];
    else
        cout << "-1";
}19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
typedef pair<int, int> PII;
int n;      // 点的数量
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N];        // 存储所有点到 1 号点的距离
bool st[N];     // 存储每个点的最短距离是否已确定
// 求1号点到 n号点的最短距离，如果不存在，则返回 -1
int dijkstra(){
    memset(dist,0x3f,sizeof dist);//距离初始化为无穷大
    dist[1]=0;//1->1的节点距离为 0
    priority_queue<PII,vector<PII>,greater<PII>> heap;//小根堆
    heap.push({0,1});//插入距离和节点编号
    1
2
3
4
5
6
7
8
9
10
11
12
13
14

## 第35页

关于 Dijkstra 的相关博客链接：
AcW ing 849. Dijkstra 求最短路  I ：图解  详细代码（图解）  - AcW ing
AcW ing 850. Dijkstra 求最短路  II ：详解 + 代码注释  - AcW ing
Bellman-Ford 算 法  
时间复杂度 $O(nm)$ ， n 表示点数， m 表示边数
注意在模板题中需要对下面的模板稍作修改，加上备份数组，详情见模板题。
上图为 Bellman-ford 草稿图      while(heap.size()){
        auto t=heap.top();//取距离源点最近的点
        heap.pop();
        
        int ver=t.second,distance=t.first;//ver：节点编号， distance 源点距离 ver
        if(st[ver])continue;//如果距离已经确定，则跳过该点
        st[ver]=true;
        for(int i=h[ver];i!=-1;i=ne[i])//更新ver所指向的节点距离
        {
            int j=e[i];
            if(dist[j]>dist[ver]+w[i]){
                dist[j]=dist[ver]+w[i];
                heap.push({dist[j],j});//距离变小，则入堆
            }
        }
    }
    if(dist[n]==0x3f3f3f3f)return -1;
    return dist[n];
}15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
int n, m;       // n表示点数， m 表示边数
int dist[N],backup[N];        // dist[x]存储 1 到 x 的最短路距离
struct Edge     // 边，a表示出点， b 表示入点， w 表示边的权重
{
    int a, b, w;
}edges[M];1
2
3
4
5
6
7
8

## 第36页

应用
问题：为什么把每一条边用不等式刷 k 次就是 k 条件下的值？// 求1到 n的最短路距离，如果无法从 1 走到 n ，则返回 -1 。
int bellman_ford()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    // 如果第 n次迭代仍然会松弛三角不等式，就说明存在一条长度是 n+1 的最短路径，由抽屉原理，
路径中至少存在两个相同的点，说明图中存在负权回路。
    for (int i = 0; i < n; i ++ )
    {
        memcpy(back,dist,sizeof dist);
        for (int j = 0; j < m; j ++ )
        {
            int a = edges[j].a, b = edges[j].b, w = edges[j].w;
            if (dist[b] > backup[a] + w)
                dist[b] = backup[a] + w;
        }
    }
    if (dist[n] > 0x3f3f3f3f / 2) return -1;
    return dist[n];
}9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
int n,m,k;
const int N=512,M=10012;
struct Edge{
    int a,b,w;
}e[M];
int dist[N];
int back[N];
void bellman_ford(){
    memset(dist,0x3f,sizeof dist);
    dist[1]=0;
    for(int i=0;i<k;i++){
        memcpy(back,dist,sizeof dist);
        for(int j=0;j<m;j++){
            int a=e[j].a,b=e[j].b,c=e[j].w;
            dist[b]=min(dist[b],back[a]+c);
        }
    }
}
int main(){
    scanf("%d%d%d",&n,&m,&k);
    for(int i=0;i<m;i++){
        int a,b,w;
        scanf("%d%d%d",&a,&b,&w);
        e[i]={a,b,w};
    }
    bellman_ford();
    if(dist[n]>0x3f3f3f3f/2)cout<<"impossible"<<endl;
    else cout<<dist[n]<<endl;
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

## 第37页

你 可 以 想 象 这 个 图 是 1->2->3->4....->n 这 样 一 条 直 线 。 比 如 说 第 一 次 迭 代 ， 为 什 么 只 有 与 原 点 相 连 的
点 才 能 被 更 新 dist 呢 ？ 因 为 原 点 的 dist 是 0 ， 其 他 点 的 dist 是 +∞ ， 满 足 dist[2] > dist[1]+c ， 而 +∞ 并 不
>+∞+c ， 所 以 第 一 次 迭 代 结 束 就 是 不 超 过 一 条 边 走 到 i 节 点 最 短 路 的 距 离 ， 依 次 类 推 ， 第 二 次 迭 代 ，
只 有 3 会 被 更 新 ， 因 为 只 有 1 、 2 的 dist 不 是 +∞ ， 第 二 次 迭 代 就 是 不 超 过 2 条 边 走 到 i 节 点 的 最 短 距 离 。
这 就 是 为 什 么 k 次 迭 代 最 多 是 走 了 k 条 边 ， 同 时 也 是 为 什 么 一 共 只 用 迭 代 n-1 次 ， 因 为 n 个 点 的 有 向
图，如果能走到，原点到 n 号点的最短距离最多是 n-1 次，也就是 1->2->…->n 直线这种。
SPFA 算 法 （ 队 列 优 化 的 Bellman-Ford 算 法 ）  
时间复杂度平均情况下 $O(m)$ ，最坏情况下 $O(nm)$ ， n 表示点数， m 表示边数
模板
应用int n;      // 总点数
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N];        // 存储每个点到 1 号点的最短距离
bool st[N];     // 存储每个点是否在队列中
// 求1号点到 n号点的最短路距离，如果从 1 号点无法走到 n 号点则返回 -1
int spfa()
{
    memset(dist, 0x3f, sizeof dist);
    dist[1] = 0;
    queue<int> q;
    q.push(1);
    st[1] = true;
    while (q.size())
    {
        auto t = q.front();
        q.pop();
        st[t] = false;
        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                if (!st[j])     // 如果队列中已存在 j ，则不需要将 j 重复插入
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }
    if (dist[n] == 0x3f3f3f3f) return -1;
    return dist[n];
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
const int N = 1e6 + 10; 1

## 第38页

int n, m;//节点数量和边数
int h[N], w[N], e[N], ne[N], idx;//邻接矩阵存储图
int dist[N];//存储距离
bool st[N];//存储状态
void add(int a, int b, int c)
{
    e[idx] = b, w[idx] = c, ne[idx] = h[a], h[a] = idx ++ ;
}
int spfa()
{
    memset(dist, 0x3f, sizeof dist);//距离初始化为无穷大
    dist[1] = 0;//初始化1到 1的距离为 0
    queue<int> que;//队列
    que.push(1);//1入队
    while (que.size())//判断是否存在
    {
        int t=que.front();
        que.pop();//获取第一个并出队
        st[t]=false;//第一个取消占用
        for(int i=h[t];i!=-1;i=ne[i]){//遍历第一个可以到达的结点
            int j=e[i];
            if(dist[j]>dist[t]+w[i]){//1号点可到达的节点距离是否大于上次的距离距离加上
当前的距离
                dist[j]=dist[t]+w[i];//赋值给可到达的节点
                if(!st[j]){//如果可到达的节点未被占用
                    que.push(j);//则入队
                    st[j]=true;//占用
                }
            }
        }
    }
    return dist[n];
}
int main()
{
    scanf("%d%d", &n, &m);
    memset(h, -1, sizeof h);
    while (m -- )
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        add(a, b, c);
    }
    int t=spfa();
    if(t==0x3f3f3f3f)cout<<"impossible"<<endl;
    else printf("%d\n",t);
    return 0;
}2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

## 第39页

应用： spfa判断图中是否存在负权  
floyd 算 法  
时间复杂度 $O(n^3)$ ， n 表示点数
视频讲解： https://www .bilibili.com/video/BV14R4y1x7GB/
模板int n;      // 总点数
int h[N], w[N], e[N], ne[N], idx;       // 邻接表存储所有边
int dist[N], cnt[N];        // dist[x]存储 1 号点到 x 的最短距离， cnt[x] 存储 1 到 x 的最短路
中经过的点数
bool st[N];     // 存储每个点是否在队列中
// 如果存在负环，则返回 true ，否则返回 false 。
bool spfa()
{
    // 不需要初始化 dist 数组
    // 原理：如果某条最短路径上有 n 个点（除了自己），那么加上自己之后一共有 n+1 个点，由抽屉
原理一定有两个点相同，所以存在环。
    queue<int> q;
    for (int i = 1; i <= n; i ++ )
    {
        q.push(i);
        st[i] = true;
    }
    while (q.size())
    {
        auto t = q.front();
        q.pop();
        st[t] = false;
        for (int i = h[t]; i != -1; i = ne[i])
        {
            int j = e[i];
            if (dist[j] > dist[t] + w[i])
            {
                dist[j] = dist[t] + w[i];
                cnt[j] = cnt[t] + 1;
                if (cnt[j] >= n) return true;       // 如果从 1号点到 x 的最短路中包含
至少n个点（不包括自己），则说明存在环
                if (!st[j])
                {
                    q.push(j);
                    st[j] = true;
                }
            }
        }
    }
    return false;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

## 第40页

应用初始化：
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= n; j ++ )
            if (i == j) d[i][j] = 0;
            else d[i][j] = INF;
// 算法结束后， d[a][b] 表示 a 到 b 的最短距离
void floyd()
{
    for (int k = 1; k <= n; k ++ )//k为中转节点
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= n; j ++ )
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
using namespace std;
const int N = 210, INF = 1e9;
int n, m, Q;
int d[N][N];
void floyd()
{
    for (int k = 1; k <= n; k ++ )//k为中转节点
        for (int i = 1; i <= n; i ++ )
            for (int j = 1; j <= n; j ++ )
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
}
int main()
{
    scanf("%d%d%d", &n, &m, &Q);
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= n; j ++ )
            if (i == j) d[i][j] = 0;
            else d[i][j] = INF;
    while (m -- )
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        d[a][b] = min(d[a][b], c);
    }
    floyd();
    while (Q -- )
    {
        int a, b;
        scanf("%d%d", &a, &b);
        int t = d[a][b];
        if (t > INF / 2) puts("impossible");
        else printf("%d\n", t);
    }1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43

## 第41页

最 短 路 算 法 总 结  
最短路
单 源 最 短 路 ： 给 定 V 中 的 一 个 顶 点 ， 称 为 源 。 要 计 算 从 源 到 其 他 所 有 各 顶 点 的 最 短 路 径 长 度 。 这 里
的长度就是指路上各边权之和。这个问题通常称为单源最短路径  问题。
 所有边权都是正数：
  朴素 Dijkstra 算法  O(n^2) 适合稠密图，贪心思想
  堆优化版的 Dijkstra 算法  O(mlogn) 适合稀疏图，贪心思想
 存在负权边：
  Bellman-ford O(nm) ，动态规划思想
  SPFA 一般： O(m) ，最坏 O(nm)
多 源 汇 最 短 路 ： 任 意 两 点 最 短 路 径 被 称 为 多 源 最 短 路 径 ， 即 给 定 任 意 两 个 点 ， 一 个 出 发 点 ， 一 个 到
达点，求这两个点的之间的最短路径，就是任意两点最短路径问题
 Floyd 算法  O(n^3)
prim 算 法  
时间复杂度是 $O(n^2+m)$ ， n 表示点数， m 表示边数    return 0;
}44
45
int n;      // n表示点数
int g[N][N];        // 邻接矩阵，存储所有边
int dist[N];        // 存储其他点到当前最小生成树的距离
bool st[N];     // 存储每个点是否已经在生成树中
// 如果图不连通，则返回 INF( 值是 0x3f3f3f3f), 否则返回最小生成树的树边权重之和
int prim()
{
    memset(dist, 0x3f, sizeof dist);
    int res = 0;
    for (int i = 0; i < n; i ++ )
    {
        int t = -1;
        for (int j = 1; j <= n; j ++ )
            if (!st[j] && (t == -1 || dist[t] > dist[j]))
                t = j;
        if (i && dist[t] == INF) return INF;
        if (i) res += dist[t];
        st[t] = true;
        for (int j = 1; j <= n; j ++ ) dist[j] = min(dist[j], g[t][j]);
    }
    return res;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

## 第42页

应用
Kruskal 算 法  
时间复杂度 $O(mlogm)$ ， n 表示点数， m 表示边数const int N = 510, INF = 0x3f3f3f3f;
int n, m;
int g[N][N];
int dist[N];
bool st[N];
int prim()
{
    memset(dist, 0x3f, sizeof dist);
    int res = 0;
    for (int i = 0; i < n; i ++ )
    {
        int t = -1;
        for (int j = 1; j <= n; j ++ )
            if (!st[j] && (t == -1 || dist[t] > dist[j]))
                t = j;
        if (i && dist[t] == INF) return INF;
        if (i) res += dist[t];
        st[t] = true;
        for (int j = 1; j <= n; j ++ ) dist[j] = min(dist[j], g[t][j]);
    }
    return res;
}
int main()
{
    scanf("%d%d", &n, &m);
    memset(g, 0x3f, sizeof g);
    while (m -- )
    {
        int a, b, c;
        scanf("%d%d%d", &a, &b, &c);
        g[a][b] = g[b][a] = min(g[a][b], c);
    }
    int t = prim();
    if (t == INF) puts("impossible");
    else printf("%d\n", t);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51

## 第43页

应用int n, m;       // n是点数， m是边数
int p[N];       // 并查集的父节点数组
struct Edge     // 存储边
{
    int a, b, w;
    bool operator< (const Edge &W)const
    {
        return w < W.w;
    }
}edges[M];
int find(int x)     // 并查集核心操作
{
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}
int kruskal()
{
    sort(edges, edges + m);
    for (int i = 1; i <= n; i ++ ) p[i] = i;    // 初始化并查集
    int res = 0, cnt = 0;
    for (int i = 0; i < m; i ++ )
    {
        int a = edges[i].a, b = edges[i].b, w = edges[i].w;
        a = find(a), b = find(b);
        if (a != b)     // 如果两个连通块不连通，则将这两个连通块合并
        {
            p[a] = b;
            res += w;
            cnt ++ ;
        }
    }
    if (cnt < n - 1) return INF;
    return res;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 100010, M = 200010, INF = 0x3f3f3f3f;
int n, m;
int p[N];
struct Edge
{
    int a, b, w;
    bool operator< (const Edge &W)const
    {1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17

## 第44页

染 色 法 判 别 二 分 图  
什么叫二分图
有两顶点集且图中每条边的的两个顶点分别位于两个顶点集中，每个顶点集中没有边直接相连接！        return w < W.w;
    }
}edges[M];
int find(int x)
{
    if (p[x] != x) p[x] = find(p[x]);
    return p[x];
}
int kruskal()
{
    sort(edges, edges + m);
    for (int i = 1; i <= n; i ++ ) p[i] = i;    // 初始化并查集
    int res = 0, cnt = 0;
    for (int i = 0; i < m; i ++ )
    {
        int a = edges[i].a, b = edges[i].b, w = edges[i].w;
        a = find(a), b = find(b);
        if (a != b)
        {
            p[a] = b;
            res += w;
            cnt ++ ;
        }
    }
    if (cnt < n - 1) return INF;
    return res;
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < m; i ++ )
    {
        int a, b, w;
        scanf("%d%d%d", &a, &b, &w);
        edges[i] = {a, b, w};
    }
    int t = kruskal();
    if (t == INF) puts("impossible");
    else printf("%d\n", t);
    return 0;
}18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69

## 第45页

说 人 话 的 定 义 ： 图 中 点 通 过 移 动 能 分 成 左 右 两 部 分 ， 左 侧 的 点 只 和 右 侧 的 点 相 连 ， 右 侧 的 点 只 和 左
侧的点相连。
下图就是个二分图：
时间复杂度是 $O(n+m)$ ， n 表示点数， m 表示边数
int n;      // n表示点数
int h[N], e[M], ne[M], idx;     // 邻接表存储图
int color[N];       // 表示每个点的颜色， -1 表示未染色， 0 表示白色， 1 表示黑色
// 参数： u表示当前节点， c 表示当前点的颜色
bool dfs(int u, int c)
{
    color[u] = c;
    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (color[j] == -1)
        {
            if (!dfs(j, !c)) return false;
        }
        else if (color[j] == c) return false;
    }
    return true;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

## 第46页

应用bool check()
{
    memset(color, -1, sizeof color);
    bool flag = true;
    for (int i = 1; i <= n; i ++ )
        if (color[i] == -1)
            if (!dfs(i, 0))
            {
                flag = false;
                break;
            }
    return flag;
}21
22
23
24
25
26
27
28
29
30
31
32
33
34
using namespace std;
const int N = 100010, M = 200010;// 由于是无向图 , 顶点数最大是 N ，那么边数 M 最大是顶点数
的2倍
int n, m;
int h[N], e[M], ne[M], idx;
int color[N];
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}
bool dfs(int u, int c)
{
    color[u] = c;
    for (int i = h[u]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!color[j])
        {
            if (!dfs(j, 3 - c)) return false;
        }
        else if (color[j] == c) return false;
    }
    return true;
}
int main()
{
    scanf("%d%d", &n, &m);
    memset(h, -1, sizeof h);
    while (m -- )
    {
        int a, b;
        scanf("%d%d", &a, &b);
        add(a, b), add(b, a);// 无向图， a->b, b->a
    }1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42

## 第47页

匈 牙 利 算 法  
要了解匈牙利算法必须先理解下面的概念：
匹配：在图论中，一个「匹配」是一个边的集合，其中任意两条边都没有公共顶点。
最大匹配：一个图所有匹配中，所含匹配边数最多的匹配，称为这个图的最大匹配。
下面是一些补充概念：
完美匹配：如果一个图的某个匹配中，所有的顶点都是匹配点，那么它就是一个完美匹配。
交替路：从一个未匹配点出发，依次经过非匹配边、匹配边、非匹配边 … 形成的路径叫交替路。
增 广 路 ： 从 一 个 未 匹 配 点 出 发 ， 走 交 替 路 ， 如 果 途 径 另 一 个 未 匹 配 点 （ 出 发 的 点 不 算 ） ， 则 这 条 交
替 路称为增广路（ agumenting path ）。
时间复杂度 $O(nm)$ ， n 表示点数， m 表示边数    bool flag = true;
    for (int i = 1; i <= n; i ++ )
        if (!color[i])
        {
            if (!dfs(i, 1))
            {
                flag = false;
                break;
            }
        }
    if (flag) puts("Yes");
    else puts("No");
    return 0;
}43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
//遍历自己喜欢的女孩 int n1, n2;     // n1 表示第一个集合中的点数， n2 表示第二个集合中的点
数
int h[N], e[M], ne[M], idx;     // 邻接表存储所有边，匈牙利算法中只会用到从第一个集合
指向第二个集合的边，所以这里只用存一个方向的边
int match[N];       // 存储第二个集合中的每个点当前匹配的第一个集合中的点是哪个
bool st[N];     // 表示第二个集合中的每个点是否已经被遍历过
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}
bool find(int x)
{
    //遍历自己喜欢的女孩
    for (int i = h[x]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])//如果在这一轮模拟匹配中 , 这个女孩尚未被预定
        {1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

## 第48页

应用：二分图的最大匹配  
相关题解： AcW ing 861. 二分图的最大匹配 ---- 图解 --$\color{r ed}{ 海绵宝宝来喽 }$ （转）  - AcW ing            st[j] = true;//那x就预定这个女孩了
            //如果女孩 j没有男朋友，或者她原来的男朋友能够预定其它喜欢的女孩。配对成功
            if (match[j] == 0 || find(match[j]))
            {
                match[j] = x;
                return true;
            }
        }
    }
    //自己中意的全部都被预定了。配对失败。
    return false;
}
// 求最大匹配数，依次枚举第一个集合中的每个点能否匹配第二个集合中的点
int res = 0;
for (int i = 1; i <= n1; i ++ )
{
    memset(st, false, sizeof st);
    if (find(i)) res ++ ;
}20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
using namespace std;
const int N = 510, M = 100010;
int n1, n2, m;
int h[N], e[M], ne[M], idx;
int match[N];
bool st[N];
void add(int a, int b)
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14

## 第49页

四、数学知识  
算法的数学知识定理证明可以在这里查阅： 数学部分简介  - OI W iki (oi-wiki.or g)
试 除 法 判 定 质 数  bool find(int x)
{
     // 和各个点尝试能否匹配
    for (int i = h[x]; i != -1; i = ne[i])
    {
        int j = e[i];
        if (!st[j])//打标记
        {
            st[j] = true;
            // 当前尝试点没有被匹配或者和当前尝试点匹配的那个点可以换另一个匹配
            if (match[j] == 0 || find(match[j]))
            {
                // 和当前尝试点匹配在一起
                match[j] = x;
                return true;
            }
        }
    }
    return false;
}
int main()
{
    scanf("%d%d%d", &n1, &n2, &m);
    memset(h, -1, sizeof h);
    // 保存图，因为只从一遍找另一边，所以该无向图只需要存储一个方向
    while (m -- )
    {
        int a, b;
        scanf("%d%d", &a, &b);
        add(a, b);
    }
    int res = 0;
    //为各个点找匹配
    for (int i = 1; i <= n1; i ++ )
    {
        memset(st, false, sizeof st);
        //找到匹配
        if (find(i)) res ++ ;
    }
    printf("%d\n", res);
    return 0;
}15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61

## 第50页

试 除 法 分 解 质 因 数  
埃 氏 筛 法 求 质 数  
线 性 筛 法 求 质 数  
算法动画讲解： https://www .bilibili.com/video/BV1LR4y1Z7pmbool is_prime(int x)
{
    if (x < 2) return false;
    for (int i = 2; i <= x / i; i ++ )
        if (x % i == 0)
            return false;
    return true;
}1
2
3
4
5
6
7
8
void divide(int x)
{
    for (int i = 2; i <= x / i; i ++ )
        if (x % i == 0)//i 一定是质数
        {
            int s = 0;
            while (x % i == 0) x /= i, s ++ ;
            cout << i << ' ' << s << endl;
        }
    if (x > 1) cout << x << ' ' << 1 << endl;
    cout << endl;
}1
2
3
4
5
6
7
8
9
10
11
12
int primes[N], cnt;     // primes[]存储所有素数
bool st[N];         // st[x]存储 x是否被筛掉
void get_primes(int n)
{
    for (int i = 2; i <= n; i ++ )
    {
        if (st[i]) continue;
        primes[cnt ++ ] = i;
        for (int j = i + i; j <= n; j += i)
            st[j] = true;
    }
}1
2
3
4
5
6
7
8
9
10
11
12
13
int primes[N], cnt;     // primes[]存储所有素数
bool st[N];         // st[x]存储 x是否被筛掉
void get_primes(int n)
{
    for (int i = 2; i <= n; i ++ )1
2
3
4
5
6

## 第51页

试 除 法 求 所 有 约 数  
约 数 个 数  
约数个数定理和约数和定理公式推导 ：https://www .bilibili.com/video/BV13R4y1o777
约数个数定理推导 ：https://www .bilibili.com/video/BV1NY41 187GM
     {
        if (!st[i]) primes[cnt ++ ] = i;
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}7
8
9
10
11
12
13
14
15
vector<int> get_divisors(int x)
{
    vector<int> res;
    for (int i = 1; i <= x / i; i ++ )
        if (x % i == 0)
        {
            res.push_back(i);
            if (i != x / i) res.push_back(x / i);
        }
    sort(res.begin(), res.end());
    return res;
}1
2
3
4
5
6
7
8
9
10
11
12
using namespace std;
typedef long long LL;
const int N = 110, mod = 1e9 + 7;
int main()
{
    int n;
    cin >> n;
    unordered_map<int, int> primes;
    while (n -- )
    {
        int x;
        cin >> x;
        for (int i = 2; i <= x / i; i ++ )
            while (x % i == 0)
            {
                x /= i;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

## 第52页

约 数 之 和  
约数个数定理和约数和定理公式推导 ：https://www .bilibili.com/video/BV13R4y1o777
代码第 26 行解释 ：                primes[i] ++ ;
            }
        if (x > 1) primes[x] ++ ;
    }
    LL res = 1;
    for (auto p : primes) res = res * (p.second + 1) % mod;
    cout << res << endl;
    return 0;
}17
18
19
20
21
22
23
24
25
using namespace std;
typedef long long LL;
const int N = 110, mod = 1e9 + 7;
int main()
{
    int n;
    cin >> n;
    unordered_map<int, int> primes;
    while (n -- )
    {
        int x;
        cin >> x;
        for (int i = 2; i <= x / i; i ++ )
            while (x % i == 0)
            {
                x /= i;
                primes[i] ++ ;
            }
        if (x > 1) primes[x] ++ ;
    }
    LL res = 1;
    for (auto p : primes)
    {
        LL a = p.first, b = p.second;
        LL t = 1;
        while (b -- ) t = (t * a + 1) % mod;//遍历b次后得到 t=p^b+p^(b-1)+...+p+1
        res = res * t % mod;
    }
    cout << res << endl;
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

## 第53页

欧 几 里 得 算 法 ( 求 最 大 公 约 数 )  
求 欧 拉 函 数  
前置知识
互质：互质是公约数只有 1 的两个整数，叫做互质整数。
欧拉函数定义
$1 ∼N-1$ 中与 N 互质的数的个数被称为欧拉函数，记为 $\phi(N)$ 。
若在算数基本定理中， $N=p_1^{a_1}p_2^{a_2}...p_m^{a_m}$ ，则：
$\phi(N)=N\cdot\frac{p_1-1}{p_1}\cdot\frac{p_2-1}{p_2}\cdot...\cdot\frac{p_m-1}{p_m}$
欧拉函数推导
首先我们要知道 $1,2,3...N-1,N$ 与 $N$ 互质的个数是 $1 ∼ N$ 数列去除 N 的质因子的倍数。
例 如 $N=10, 即 1,2,3,4,5,6,7,8,9,10$ 去 除 $N$ 的 质 因 子 的 倍 数 $, 则
1,\bcancel{2},3,\bcancel{4},\bcancel{5},\bcancel{6},7,\bcancel{8},9,\bcancel{10}.$
显然， $1,3,7,9$ 与 $10$ 互质。
由上方结论使用容斥原理进行数学推导如下：
$\because N=p_1^{a_1}p_2^{a_2}...p_m^{a_m}$
①. 从 1~n 中去掉 $p_1,p_2,...,p_k$ 的所有倍数的个数，即
$n←n-\frac{n}{p_1}-\frac{n}{p_2}-...-\frac{n}{p_k}$int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}1
2
3
4

## 第54页

②. 由 容 斥 原 理 ， $p_i \cdot p_j$ 的 倍 数 被 ① 减 了 两 次 ， 所 以 加 上 所 有 $p_i\cdot p_j$ 的 倍 数 的 个 数 （ 其
中$p_i,p_j$ 是 $p_1 ∼ p_k$ 的组合），即
$n←n+\frac{n}{p_1\cdot p_2}+\frac{n}{p_1\cdot p_3}+...+\frac{n}{p_{k-1}\cdot p_k}$
③. 减去所有 $p_i\cdot p_j \cdot p_k$ 的倍数个数，即
$n←n-\frac{n}{p_1\cdot p_2\cdot p_3}-\frac{n}{p_1\cdot p_2 \cdot p_4}-...-\frac{n}{p {k-2}\cdot p{k-
1}\cdot p_k}$
④. 同理，加上所有 $p_i\cdot p_j \cdot p_k \cdot p_l$ 的倍数个数，即
$n←n+\frac{n}{p_1\cdot p_2\cdot p_3\cdot p_4} +\frac{n}{p_1\cdot p_2 \cdot p_3\cdot p_5}+...+\frac{n}
{p{k-3}\cdot p {k-2}\cdot p_{k-1}\cdot {p_k}}$
因此，
也就是 n 减去奇数个质因子的倍数个数，加上偶数个质因子的倍数个数，循环往复。
将上式等价变形，得到
$\phi(n)=n\cdot(1-\frac{1}{p_1})\cdot(1-\frac{1}{p_2})...\cdot(1-\frac{1}{p_k})$
证必。
代码模板
线 性 筛 法 求 欧 拉 函 数  int phi(int x)
{
    int res = x;
    for (int i = 2; i <= x / i; i ++ )
        if (x % i == 0)
        {
            res = res / i * (i - 1);
            while (x % i == 0) x /= i;
        }
    if (x > 1) res = res / x * (x - 1);
    return res;
}1
2
3
4
5
6
7
8
9
10
11
12
13
int primes[N], cnt;     // primes[]存储所有素数
int euler[N];           // 存储每个数的欧拉函数
bool st[N];         // st[x]存储 x是否被筛掉
void get_eulers(int n)  // 线性筛法求 1~n 的欧拉函数1
2
3
4
5

## 第55页

快 速 幂  
快速幂公式证明： 快速幂  - OI W iki (oi-wiki.or g)
扩 展 欧 几 里 得 算 法  
扩展欧几里得算法讲解： https://www .bilibili.com/video/BV1KU4y1a7E2/
优秀题解： https://www .acwing.com/solution/content/1393
优秀博客： https://blog.csdn.net/mango1 14514/article/details/121048335
x 的第一个正解就是 (x%k+k)%k
其中， k=b/gcd(a,b){
    euler[1] = 1;
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i])
        {
            primes[cnt ++ ] = i;
            euler[i] = i - 1;
        }
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            int t = primes[j] * i;
            st[t] = true;
            if (i % primes[j] == 0)
            {
                euler[t] = euler[i] * primes[j];
                break;
            }
            euler[t] = euler[i] * (primes[j] - 1);
        }
    }
}6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
// 求 m^k mod p ，时间复杂度  O(logk) 。
// m为底数， k为幂
int qmi(int m, int k, int p)
{
    int res = 1 % p, t = m;
    while (k)
    {
        if (k&1) res = res * t % p;
        t = t * t % p;
        k >>= 1;
    }
    return res;
}1
2
3
4
5
6
7
8
9
10
11
12
13

## 第56页

中 国 剩 余 定 理  
中国剩余定理讲解： https://www .bilibili.com/video/BV1AN4y1N7Su/
// 求x, y，使得 ax + by = gcd(a, b)
int exgcd(int a, int b, int &x, int &y)
{
    if (!b)
    {
        x = 1, y = 0;
        return a;
    }
    int d = exgcd(b, a % b, y, x);
    y -= (a/b) * x;
    return d;
}1
2
3
4
5
6
7
8
9
10
11
12
LL exgcd(LL a,LL b,LL &x,LL &y){
    if(b==0){
        x=1,y=0; 
        return a;
    }
    LL d=exgcd(b,a%b,y,x);
    y -= (a/b) * x;
    return d;
}
LL CRT(LL m[],LL r[]){
    LL m=1,ans=0;
    for(int i=1;i<=n;i++)M*=m[i];
    for(int i=1;i<=n;i++){
        LL c=M/m[i],x,y;
        exgcd(c,m[i],x,y);
        ans=(ans+r[i]*c*x%M)%M;
    }
    return (ans%M+M)%M;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19

## 第57页

扩 展 中 国 剩 余 定 理  
扩展中国剩余定理讲解： https://www .bilibili.com/video/BV1Ut4y1F7HG/
高 斯 消 元 法  
高斯消元  $O(n^3)$
求解例如下面方程组LL exgcd(LL a,LL b,LL &x,LL &y){
    if(b==0){
        x=1,y=0; 
        return a;
    }
    LL d=exgcd(b,a%b,y,x);
    y -= (a/b) * x;
    return d;
}
LL EXCRT(LL m[],LL r[]){
    LL m1,m2,r1,r2,p,q;
    m1=m[1],r1=r[1];
    for(int i=2;i<=n;i++){
        m2=m[i],r2=r[i];
        LL d = exgcd(m1,m2,p,q);
        if((r2-r1)%d){
            return -1;
        }
        p=p*(r2-r1)/d;//特解
        p=(p%(m2/d)+m2/d)%(m2/d);
        r1=m1*p+r1;
        m1=m1*m2/d;
    }
    return (r1%m1+m1)%m1;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第58页

高斯消元讲解： https://www .bilibili.com/video/BV1Kd4y127vZ/
模板
应用// a[N][N]是增广矩阵
int gauss()
{
    int c, r;
    for (c = 0, r = 0; c < n; c ++ )
    {
        int t = r;
        for (int i = r; i < n; i ++ )   // 找到绝对值最大的行
            if (fabs(a[i][c]) > fabs(a[t][c]))
                t = i;
        if (fabs(a[t][c]) < eps) continue;
        for (int i = c; i <= n; i ++ ) swap(a[t][i], a[r][i]);      // 将绝对值最大
的行换到最顶端
        for (int i = n; i >= c; i -- ) a[r][i] /= a[r][c];      // 将当前行的首位变
成1
        for (int i = r + 1; i < n; i ++ )       // 用当前行将下面所有的列消成 0
            if (fabs(a[i][c]) > eps)
                for (int j = n; j >= c; j -- )
                    a[i][j] -= a[r][j] * a[i][c];
        r ++ ;
    }
    if (r < n)
    {
        for (int i = r; i < n; i ++ )
            if (fabs(a[i][n]) > eps)
                return 2; // 无解
        return 1; // 有无穷多组解
    }
    for (int i = n - 1; i >= 0; i -- )
        for (int j = i + 1; j < n; j ++ )
            a[i][n] -= a[i][j] * a[j][n];
    return 0; // 有唯一解
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
using namespace std;
const int N = 110;
const double eps = 1e-6;
int n;
double a[N][N];
int gauss()
{1
2
3
4
5
6
7
8
9
10

## 第59页

int c, r;// c 代表  列  col ，  r 代表  行  row
    for (c = 0, r = 0; c < n; c ++ )
    {
        int t = r;// 先找到当前这一列，绝对值最大的一个数字所在的行号
        for (int i = r; i < n; i ++ )
            if (fabs(a[i][c]) > fabs(a[t][c]))
                t = i;
        if (fabs(a[t][c]) < eps) continue;// 如果当前这一列的最大数都是  0 ，那么所有
数都是 0，就没必要去算了，因为它的约束方程，可能在上面几行
        for (int i = c; i < n + 1; i ++ ) swap(a[t][i], a[r][i]);//// 把当前这一
行，换到最上面（不是第一行，是第  r 行）去
        for (int i = n; i >= c; i -- ) a[r][i] /= a[r][c];// 把当前这一行的第一个
数，变成 1，  方程两边同时除以  第一个数，必须要到着算，不然第一个数直接变 1 ，系数就被篡改，
后面的数字没法算
        for (int i = r + 1; i < n; i ++ )// 把当前列下面的所有数，全部消成  0
            if (fabs(a[i][c]) > eps)// 如果非 0 再操作，已经是  0 就没必要操作了
                for (int j = n; j >= c; j -- )// 从后往前，当前行的每个数字，都减去对
应列 * 行首非 0的数字，这样就能保证第一个数字是  a[i][0] -= 1*a[i][0];
                    a[i][j] -= a[r][j] * a[i][c];
        r ++ ;// 这一行的工作做完，换下一行
    }
    if (r < n)// 说明剩下方程的个数是小于  n 的，说明不是唯一解，判断是无解还是无穷多解
    {// 因为已经是阶梯型，所以  r ~ n-1 的值应该都为  0
        for (int i = r; i < n; i ++ )// 
            if (fabs(a[i][n]) > eps)// a[i][n] 代表  b_i , 即  左边 =0 ，右边 =b_i,0 != 
b_i, 所以无解。
                return 2;
        return 1;// 否则，  0 = 0 ，就是 r ~ n-1 的方程都是多余方程
    }
    // 唯一解  ↓，从下往上回代，得到方程的解
    for (int i = n - 1; i >= 0; i -- )
        for (int j = i + 1; j < n; j ++ )
            a[i][n] -= a[j][n] * a[i][j];//因为只要得到解，所以只用对  b_i 进行操作，
中间的值，可以不用操作，因为不用输出
    return 0;
}
int main()
{
    cin >> n;
    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < n + 1; j ++ )
            cin >> a[i][j];
    int t = gauss();
    if (t == 0)
    {
        for (int i = 0; i < n; i ++ ) printf("%.2lf\n", a[i][n]);
    }
    else if (t == 1) puts("Infinite group solutions");
    else puts("No solution");
    return 0;
}11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62

## 第60页

求 组 合 数  
递推法求组合数  
排列组合详细讲解： https://www .bilibili.com/video/BV1e741 1J7SC/
 
 
1. 左右两侧斜线都是 1 ， $C^0_n=C^n_n=1$
2. 其他数等于其左上角和右上角两数之和 $C^{m-1} n+C^m_n=C^m {n+1}$
// c[a][b] 表示从 a 个苹果中选 b 个的方案数
int c[N][N];
for (int i = 0; i < N; i ++ )
    for (int j = 0; j <= i; j ++ )
        if (!j) c[i][j] = 1;
        else c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
//本质上杨辉三角1
2
3
4
5
6
7

## 第61页

通过预处理逆元的方式求组合数  
模板
应用// 首先预处理出所有阶乘取模的余数 fact[N] ，以及所有阶乘取模的逆元 infact[N]
// 如果取模的数是质数，可以用费马小定理求逆元
int qmi(int a, int k, int p)    // 快速幂模板
{
    int res = 1;
    while (k)
    {
        if (k & 1) res = (LL)res * a % p;
        a = (LL)a * a % p;
        k >>= 1;
    }
    return res;
}
// 预处理阶乘的余数和阶乘逆元的余数
fact[0] = infact[0] = 1;
for (int i = 1; i < N; i ++ )
{
    fact[i] = (LL)fact[i - 1] * i % mod;
    infact[i] = (LL)infact[i - 1] * qmi(i, mod - 2, mod) % mod;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
using namespace std;
typedef long long LL;
const int N = 100010,mod=1e9+7;//1e9+7是质数所以与 [1,1e9+7) 中的数互质
int fact[N],infact[N];
int qmi(int a,int k,int p){
    int res=1;
    while(k){
        if(k&1)res=(LL)res*a%p;
        a=(LL)a*a%p;
        k>>=1;
    }
    return res;
}
int main()
{
    fact[0]=infact[0]=1;
    for (int i = 1; i <= N; i ++ ){
        fact[i]=(LL)fact[i-1]*i%mod;
        infact[i]=(LL)infact[i-1]*qmi(i,mod-2,mod)%mod;
    }
    
    int n;
    scanf("%d",&n);
    while (n -- ){
        int a,b;
        scanf("%d%d", &a, &b);1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

## 第62页

Lucas定理求组合数  
Lucas 定理证明： https://blog.csdn.net/Qiuker_jl/article/details/109528164
模板
应用        printf("%d\n",(LL)fact[a]*infact[b]%mod*infact[a-b]%mod);
    }
    return 0;
}32
33
34
35
// 若p是质数，则对于任意整数  1 <= m <= n ，有：
// C(n, m) = C(n % p, m % p) * C(n / p, m / p) (mod p)
int qmi(int a, int k, int p)  // 快速幂模板
{
    int res = 1 % p;
    while (k)
    {
        if (k & 1) res = (LL)res * a % p;
        a = (LL)a * a % p;
        k >>= 1;
    }
    return res;
}
int C(int a, int b, int p)  // 通过定理求组合数 C(a, b)
{
    if (a < b) return 0;
    LL x = 1, y = 1;  // x是分子， y是分母
    for (int i = a, j = 1; j <= b; i --, j ++ )
    {
        x = (LL)x * i % p;
        y = (LL) y * j % p;
    }
    return x * (LL)qmi(y, p - 2, p) % p;
}
int lucas(LL a, LL b, int p)
{
    if (a < p && b < p) return C(a, b, p);
    return (LL)C(a % p, b % p, p) * lucas(a / p, b / p, p) % p;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
using namespace std;
typedef long long LL;
int qmi(int a,int k,int p)
{
    int res = 1;
    while(k)1
2
3
4
5
6
7
8

## 第63页

分解质因数法求组合数  
模板    {
        if(k&1)res = (LL)res*a%p;
        a = (LL)a*a%p;
        k>>=1;
    }
    return res;
}
int C(int a,int b,int p)//自变量类型 int
{
    if(b>a)return 0;//漏了边界条件
    int res = 1;
    // a!/(b!(a-b)!) = (a-b+1)*...*a / b! 分子有 b 项
    for(int i=1,j=a;i<=b;i++,j--)//i<=b而不是 <
    {
        res = (LL)res*j%p;
        res = (LL)res*qmi(i,p-2,p)%p;
    }
    return res;
}
//对公式敲
int lucas(LL a,LL b,int p)
{
    if(a<p && b<p)return C(a,b,p);//lucas递归终点是 C_{bk}^{ak}
    return (LL)C(a%p,b%p,p)*lucas(a/p,b/p,p)%p;//a%p后肯定是 <p 的 , 所以可以用 C(), 但 a/p
后不一定<p 所以用 lucas 继续递归
}
int main()
{
    int n;
    cin >> n;
    while(n--)
    {
        LL a,b;
        int p;
        cin >> a >> b >> p;
        cout << lucas(a,b,p) << endl;
    }
    return 0;
}9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
当我们需要求出组合数的真实值，而非对某个数的余数时，分解质因数的方式比较好用：
    1. 筛法求出范围内的所有质数
    2. 通过 C(a, b) = a! / b! / (a - b)! 这个公式求出每个质因子的次数。 n! 中p的次数是 
n / p + n / p^2 + n / p^3 + ...
    3. 用高精度乘法将所有质因子相乘
int primes[N], cnt;     // 存储所有质数
int sum[N];     // 存储每个质数的次数
bool st[N];     // 存储每个数是否已被筛掉1
2
3
4
5
6
7
8
9
10

## 第64页

void get_primes(int n)      // 线性筛法求素数
{
    for (int i = 2; i <= n; i ++ )
    {
        if (!st[i]) primes[cnt ++ ] = i;
        for (int j = 0; primes[j] <= n / i; j ++ )
        {
            st[primes[j] * i] = true;
            if (i % primes[j] == 0) break;
        }
    }
}
int get(int n, int p)       // 求n！中的次数
{
    int res = 0;
    while (n)
    {
        res += n / p;
        n /= p;
    }
    return res;
}
vector<int> mul(vector<int> a, int b)       // 高精度乘低精度模板
{
    vector<int> c;
    int t = 0;
    for (int i = 0; i < a.size(); i ++ )
    {
        t += a[i] * b;
        c.push_back(t % 10);
        t /= 10;
    }
    while (t)
    {
        c.push_back(t % 10);
        t /= 10;
    }
    return c;
}
get_primes(a);  // 预处理范围内的所有质数
for (int i = 0; i < cnt; i ++ )     // 求每个质因数的次数
{
    int p = primes[i];
    sum[i] = get(a, p) - get(b, p) - get(a - b, p);
}
vector<int> res;
res.push_back(1);
for (int i = 0; i < cnt; i ++ )     // 用高精度乘法将所有质因子相乘
    for (int j = 0; j < sum[i]; j ++ )
        res = mul(res, primes[i]);11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70

## 第65页

应用
using namespace std;
const int N = 5010;
int primes[N],cnt=0;
// v[i] 记录数字  i 为素数还是合数， v[i]=true 时  i 为合数，否则  i 为素数
bool v[N];
// sum[i]=c 表示质数  i 的个数为  c
int sum[N];
// 线性筛法
void get_primes(int n)
{
    for(int i=2;i<=n;++i)
    {
        // i为质数，则存在 primes 中
        if(!v[i])primes[cnt++]=i;
        // 给当前数 i乘上一个质因子 pj
        for(int j=0;primes[j]<=n/i;++j)
        {
            v[primes[j]*i]=true;
            if(i%primes[j]==0)break;
        }
    }
}
// 计算 n 里面含有质数  p 的个数，这里的计算是不重不漏的。
// p^k的倍数会被计算 k 次：第一次算 p 的倍数时，被加一次；第二次算 p^2 的倍数时，被加一次；第三
次算p^3的倍数时，被加一次 ... 第 k 次算 p^k 的倍数时，被加一次。总共被加了 k 次，是不重不漏的。
int get(int n,int p)
{
    int res=0;
    while(n)
    {
        res+=n/p;
        n/=p;
    }
    return res;
}
// A * b：把  b 看成一个整体，然后与  A 中每一位相乘， A 中的数字采用小端存储，即低位数字存
储在数组的前面，高位数字存储在数组的后面
vector<int> mul(const vector<int>& A,const int b)
{
    if(b==0)return {0};
    vector<int> res;
    // t 表示乘法进位，这里的进位不限于 0 1 ，可以为任意数字
    for(int i=0,t=0,n=A.size();i<n||t>0;++i)
    {
        // 获得当前位的乘积和
        if(i<n)t+=A[i]*b;
        // 添加个位数字
        res.push_back(t%10);
        // 保留进位
        t/=10;
    }
     // 如 1234 * 0 = 0000 ，需要删除前导 0
    while(res.size()>1&&res.back()==0)res.pop_back();
    return res;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

## 第66页

容 斥 原 理 应 用  
经典例题： 890. 能被整除的数  - AcW ing 题库
AC 代码：}
int main()
{
    int a,b;cin>>a>>b;
    // 将 a 分解质因数
    get_primes(a);
    for(int i=0;i<cnt;++i)
    {
        // 当前的质数为  p
        int p=primes[i];
        // 用分子里面  p 的个数减去分母里面  p 的个数。这里的计算组合数的公式为 a!/(b!*(a-
b)!)，因此用  a 里面  p 的个数减去  b 里面  p 的个数和  (a-b) 里面  p 的个数。
        sum[i]=get(a,p)-get(b,p)-get(a-b,p);
    }
    // 使用高精度乘法把所有质因子乘到一块去就好了
    vector<int> res={1};
    for(int i=0;i<cnt;++i)
        // res*p^k，这里是 k 个 p 相乘，不是 k*p ，所以需要使用一个循环
        for(int j=0;j<sum[i];++j)
            res=mul(res,primes[i]);
    // 倒序打印  res 即可，由于采用小端存储，所以高位在后，从后往前打印即可
    for(int i=res.size()-1;i>=0;i--)printf("%d",res[i]);
    return 0;
}58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
using namespace std;
typedef long long LL;
const int N = 20;
int p[N], n, m;
int main() {
cin >> n >> m;
for(int i = 0; i < m; i++) cin >> p[i];
int res = 0;
//枚举从1 到  1111...(m 个 1) 的每一个集合状态 , ( 至少选中一个集合 )
for(int i = 1; i < 1 << m; i++) {
  int t = 1;             //选中集合对应质数的乘积
  int s = 0;             //选中的集合数量
  //枚举当前状态的每一位
  for(int j = 0; j < m; j++){
      //选中一个集合
      if(i >> j & 1){
          //乘积大于 n, 则 n/t = 0, 跳出这轮循环
          if((LL)t * p[j] > n){    1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

## 第67页

详细题解： AcW ing 890. 能被整除的数  - AcW ing
博 弈 论  
NIM游戏  
定理 1 ：必胜态 的后继状态至少存在一个 必败态
定理 2 ：必败态 的后继状态均为 必胜态
NIM 游戏科普： 尼姆游戏（学霸就是这样欺负人的） 哔哩哔哩 bilibili
再看 nim 游戏哔哩哔哩 bilibili
经典例题： P2197 【模板】 nim 游戏  - 洛谷  | 计算机科学教育新生态  (luogu.com.cn)
AC 代码：              t = -1;
              break;
          }
          s++;                  //有一个1，集合数量 +1
          t *= p[j];
      }
  }
  if(t == -1) continue;  
  if(s & 1) res += n / t;              //选中奇数个集合 , 则系数应该是 1, n/t 为当
前这种状态的集合数量
  else res -= n / t;                      //反之则为  -1
}
cout << res << endl;
return 0;
}23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
using namespace std;
int T;
int main() {
    cin >> T;
    while (T--) {
        int n;
        scanf("%d", &n);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int k;
            scanf("%d", &k);
            ans ^= k;
        }
        if (ans)
            puts("Yes");
        else
            puts("No");
    }
    return 0;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20

## 第68页

结论：
若初态为 必胜态 ($a_1\oplus a_2\oplus ...\oplus a_n \neq0$). 则先手必胜
若初态为 必败态 ($a_1\oplus a_2\oplus ...\oplus a_n =0$). 则先手必败
视频讲解： 581 尼姆（ Nim ）游戏【博弈论】 哔哩哔哩 bilibili
台阶型 NIM游戏  
经典例题： 892. 台阶 -Nim 游戏  - AcW ing 题库
AC 代码：
结论： 若奇数台阶上的 $a_1\oplus a_3\oplus a_5\oplus ...\neq0$ ，则先手必胜，反之先手必败。
视频讲解： 582 台阶型  Nim 游戏【博弈论】 哔哩哔哩 bilibili
集合型 NIM游戏  
经典例题： 893. 集合 -Nim 游戏  - AcW ing 题库
AC 代码：}21
using namespace std;
const int N = 100010;
int main()
{
     int n;
     scanf("%d", &n);
  int res = 0;
     for (int i = 1; i <= n; i ++ )
     {
         int x;
         scanf("%d", &x);
         if (i & 1) res ^= x;
     }
     if (res) puts("Yes");
  else puts("No");
     return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
using namespace std;
const int N=110,M=10010;
int n,m;
int f[M],s[N];//s存储的是可供选择的集合 ,f 存储的是所有可能出现过的情况的 sg 值1
2
3
4
5
6

## 第69页

思路： 转换成 有向图游戏
视频讲解： 583 有向图游戏  SG 函数【博弈论】 哔哩哔哩 bilibili
 
五、动态规划  int sg(int x)
{
     if(f[x]!=-1) return f[x];
     //因为取石子数目的集合是已经确定了的 , 所以每个数的 sg 值也都是确定的 , 如果存储过了 ,
直接返回即可
     unordered_set<int> S;
     //set代表的是有序集合 ( 注 : 因为在函数内部定义 , 所以下一次递归中的 S 不与本次相同 )
     for(int i=0;i<m;i++)
     {
         int sum=s[i];
         if(x>=sum) S.insert(sg(x-sum));
         //先延伸到终点的 sg 值后 , 再从后往前排查出所有数的 sg 值
     }
     for(int i=0;;i++)
     //循环完之后可以进行选出最小的没有出现的自然数的操作
      if(!S.count(i))
       return f[x]=i;
}
int main()
{
     cin>>m;
     for(int i=0;i<m;i++)
     cin>>s[i];
     cin>>n;
     memset(f,-1,sizeof(f));//初始化f均为 -1, 方便在 sg 函数中查看 x 是否被记录过
     int res=0;
     for(int i=0;i<n;i++)
     {
         int x;
         cin>>x;
         res^=sg(x);
         //观察异或值的变化 , 基本原理与 Nim 游戏相同
     }
     if(res) printf("Yes");
     else printf("No");
     return 0;
}7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47

## 第70页

背 包 问 题  
01 背包每件物品只能装一次
完全背包每件物品可以装无限次
多重背包每件物品只能装有限次（多次）
分组背包每组只能选择一件物品装入（ 01 背包升级）
相关链接： https://zhuanlan.zhihu.com/p/166439661
01背包问题  
01 背包每件物品只能装一次
视频讲解： 408 背包 DP 【模板】 01 背包哔哩哔哩 bilibili

## 第71页

01 背包，使用滚动数组，倒序遍历using namespace std;
const int N=1010;
int n,m;
int v[N],w[N];//v代表体积， w代表价值
int f[N][N];
int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++)cin>>v[i]>>w[i];
    for(int i=1;i<=n;i++)//i代表这 n件物品
    {
        for(int j=1;j<=m;j++){//j代表背包容量
            if(v[i]>j)//如果v[i]的容量大于当前的背包容量则不装进行下一个
                f[i][j]=f[i-1][j];
            else f[i][j]=max(f[i-1][j],f[i-1][j-v[i]]+w[i]);//如果v[i]的容量小于当
前背包容量则可以选择装与不装得到最大值 
        }
    }
    cout<<f[n][m]<<endl;//输出最后的一个一定是最大的
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

## 第72页

状态转移方程： dp[j]=max(dp[j],dp[j-v[i]]+w[i]);
完全背包问题  
完全背包每件物品可以装无限次
视频讲解： 409 背包 DP 完全背包【动态规划】 哔哩哔哩 bilibili
完全背包问题和 01 背包优化版的区别在于第二重循环的 v[i] 和 m 做交换
状态转移方程： dp[j]=max(dp[j],dp[j-v[i]]+w[i]);
多重背包问题 1  
多重背包每件物品只能装有限次（多次）using namespace std;
const int N=1010;
int n,m;
int v[N],w[N];//v代表体积， w代表价值
int dp[N];
int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++)//i代表这 n件物品
    {
        cin>>v[i]>>w[i];//在线算法
        for(int j=m;j>=v[i];j--){//j代表背包容量，滚动数组必须倒序遍历
            dp[j]=max(dp[j],dp[j-v[i]]+w[i]);//滚动数组
        }
    }
    cout<<dp[m]<<endl;//输出最后的一个一定是最大的
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
using namespace std;
int v[N],w[N];
int dp[N];
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=1;i<=n;i++){//遍历物品
        cin>>v[i]>>w[i];//在线算法
        for(int j=v[i];j<=m;j++){//正序遍历背包容量
            dp[j]=max(dp[j],dp[j-v[i]]+w[i]);//滚动数组
        }
    }
    cout<<dp[m]<<endl;//输出答案
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
using namespace std;
int n,m;1
2

## 第73页

状态转移方程： dp[i][j]=max(dp[i][j],dp[i-1][j-v[i]*k]+w[i]*k);k 为第 i 个物品的个数
多重背包问题 2(二进制优化 )  
思路： 转换成 2 进制，再用 01 背包求解
视频讲解： 410 背包 DP 多重背包  二进制优化【动态规划】 哔哩哔哩 bilibiliint v[N],w[N],s[N];
int dp[N][N];
int main(){
    cin>>n>>m;
    for(int i=1;i<=n;i++)cin>>v[i]>>w[i]>>s[i];
    for(int i=1;i<=n;i++)//物品
        for(int j=0;j<=m;j++)//背包容量
            for(int k=0;k<=s[i]&&k*v[i]<=j;k++)
                dp[i][j]=max(dp[i][j],dp[i-1][j-v[i]*k]+w[i]*k);
    cout<<dp[n][m]<<endl;
    return 0;
}3
4
5
6
7
8
9
10
11
12
13
14
15
using namespace std;
const int N = 12010, M = 2010;
int n, m;
int v[N], w[N];
int f[M];
int main()
{
    cin >> n >> m;
    int cnt = 0;
    for (int i = 1; i <= n; i ++ )
    {
        int a, b, s;
        cin >> a >> b >> s;
        int k = 1;
        while (k <= s)
        {
            cnt ++ ;
            v[cnt] = a * k;
            w[cnt] = b * k;
            s -= k;
            k *= 2;
        }
        if (s > 0)
        {
            cnt ++ ;
            v[cnt] = a * s;
            w[cnt] = b * s;
        }
    }//二进制优化操作
    n = cnt;1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35

## 第74页

分组背包问题  
分组背包每组只能选择一件物品装入
视频讲解： 416 背包 DP 分组背包【动态规划】 哔哩哔哩 bilibili
状态转移方程： f[j]=max(f[j],f[j-v[i][k]]+w[i][k]);
线 性 DP  
数字三角形  
视频讲解： 402 线性 DP 数字三角形【动态规划】 哔哩哔哩 bilibili    for (int i = 1; i <= n; i ++ )
        for (int j = m; j >= v[i]; j -- )
            f[j] = max(f[j], f[j - v[i]] + w[i]);
    cout << f[m] << endl;
    return 0;
}36
37
38
39
40
41
42
43
44
using namespace std;
const int N=110;
int f[N];
int v[N][N],w[N][N],s[N];
int n,m,k;
int main(){
    cin>>n>>m;
    for(int i=0;i<n;i++){
        cin>>s[i];
        for(int j=0;j<s[i];j++){
            cin>>v[i][j]>>w[i][j];
        }
    }
    for(int i=0;i<n;i++){
        for(int j=m;j>=0;j--){
            for(int k=0;k<s[i];k++){    //for(int k=s[i];k>=1;k--) 也可以
                if(j>=v[i][k])
                    f[j]=max(f[j],f[j-v[i][k]]+w[i][k]);  
            }
        }
    }
    cout<<f[m]<<endl;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第75页

状态转移方程： f[i][j]=max(f[i-1][j-1]+a[i][j],f[i-1][j]+a[i][j]);
最长上升子序列 1  
视频讲解： 403 线性 DP 最长上升子序列【动态规划】 哔哩哔哩 bilibiliusing namespace std;
const int N=510,INF=1e9;
int n;
int a[N][N];
int f[N][N];
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=i;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for(int i=0;i<=n;i++){
        for(int j=0;j<=i+1;j++){
            f[i][j]=-INF;
        }
    }
    f[1][1]=a[1][1];
    for(int i=2;i<=n;i++)
        for(int j=1;j<=i;j++)
            f[i][j]=max(f[i-1][j-1]+a[i][j],f[i-1][j]+a[i][j]);//状态转移方程
    int res=-INF;
    for(int i=1;i<=n;i++)res=max(res,f[n][i]);
    printf("%d",res);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27

## 第76页

状态转移方程： if(a[j]<a[i])f[i]=max(f[i],f[j]+1);
最长上升子序列 2( 二分优化 )  
视频讲解： 404 线性 DP 最长上升子序列  二分优化哔哩哔哩 bilibiliusing namespace std;
const int N = 1010;
int n;
int a[N],f[N];
int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ )scanf("%d",&a[i]);
    for (int i = 1; i <= n; i ++ ){
        f[i]=1;//只有a[i]一个数
        for (int j = 1; j <= i; j ++ )
            if(a[j]<a[i])
                f[i]=max(f[i],f[j]+1);
    }
    int res=0;
    for (int i = 1; i <= n; i ++ )res=max(res,f[i]);
    printf("%d\n",res);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
using namespace std;
const int N = 100010;
int n;
int a[N];
int q[N];
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ) scanf("%d", &a[i]);
    int len = 0;
    for (int i = 0; i < n; i ++ )
    {
        int l = 0, r = len;
        while (l < r)
        {
            int mid = l + r + 1 >> 1;
            if (q[mid] < a[i]) l = mid;
            else r = mid - 1;
        }
        len = max(len, r + 1);
        q[r + 1] = a[i];//替换或添加
    }
    printf("%d\n", len);1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29

## 第77页

最长公共子序列  
视频讲解： 405 线性 DP 最长公共子序列【动态规划】 哔哩哔哩 bilibili
状态转移方程：
最短编辑距离  
给定两个字符串  A 和  B ，现在要将  A 经过若干操作变为  B ，可进行的操作有：
1. 删除 – 将字符串  A 中的某个字符删除。
2. 插入 – 在字符串  A 的某个位置插入某个字符。
3. 替换 – 将字符串  A 中的某个字符替换为另一个字符。
现在请你求出，将  A 变为  B 至少需要进行多少次操作。
视频讲解： 407 线性 DP 编辑距离【动态规划】 哔哩哔哩 bilibili    return 0;
}30
31
using namespace std;
const int N=1010;
int n,m;
char a[N],b[N];
int f[N][N];
int main()
{
    cin>>n>>m>>a+1>>b+1;
    for (int i = 1; i <= n; i ++ ){
        for (int j = 1; j <= m; j ++ ){
            f[i][j]=max(f[i-1][j],f[i][j-1]);
            if(a[i]==b[j])f[i][j]=max(f[i][j],f[i-1][j-1]+1);
        }
    }
    cout<<f[n][m]<<endl;
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
f[i][j]=max(f[i-1][j],f[i][j-1]);
if(a[i]==b[j])f[i][j]=max(f[i][j],f[i-1][j-1]+1);1
2

## 第78页

状态转移方程 :
区 间 DP  
石子合并  
每堆石子有一定的质量，可以用一个整数来描述，现在要将这  N 堆石子合并成为一堆。
每 次 只 能 合 并 相 邻 的 两 堆 ， 合 并 的 代 价 为 这 两 堆 石 子 的 质 量 之 和 ， 合 并 后 与 这 两 堆 石 子 相 邻 的 石 子
将和新堆相邻，合并时由于选择的顺序不同，合并的总代价也不相同。using namespace std;
const int N = 1010;
int n,m;
char a[N],b[N];
int f[N][N];
int main()
{
    scanf("%d%s", &n, a+1);
    scanf("%d%s", &m, b+1);
    for (int i = 0; i <= m; i ++ )f[0][i]=i;
    for (int i = 0; i <= n; i ++ )f[i][0]=i;//初始化字符串的编辑操作
    for (int i = 1; i <= n; i ++ ){
        for (int j = 1; j <= m; j ++ ){
            f[i][j]=min(f[i-1][j]+1,f[i][j-1]+1);
            if(a[i]==b[j])f[i][j]=min(f[i][j],f[i-1][j-1]);
            else f[i][j]=min(f[i][j],f[i-1][j-1]+1);//状态转移方程
        }
    }
    printf("%d\n",f[n][m]);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
f[i][j]=min(f[i-1][j]+1,f[i][j-1]+1);
if(a[i]==b[j])f[i][j]=min(f[i][j],f[i-1][j-1]);
else f[i][j]=min(f[i][j],f[i-1][j-1]+1);//状态转移方程1
2
3

## 第79页

视频讲解： 428 区间 DP 【模板】石子合并 哔哩哔哩 bilibili
 
状态转移方程找到最小值状态转移方程为 f[l][r]=min(f[l][r],f[l][k]+f[k+1][r]+s[r]-s[l-1])
计 数 类 DP  
整数划分  
一个正整数  n 可以表示成若干个正整数之和，我们将这样的一种表示称为正整数  n 的一种划分。  
现在给定一个正整数  n ，请你求出  n 共有多少种不同的划分方法。  using namespace std;
const int N = 310;
int n;
int s[N];
int f[N][N];//状态表示：集合 f[l][r] 为 [l,r] 区间；属性：所堆成的最小值
int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ )scanf("%d",&s[i]);
    for (int i = 1; i <= n; i ++ )s[i]+=s[i-1];//前缀和用来求一段区间的和
    for (int len = 2; len <= n; len ++ )//区间长度为 len// 枚举长度
        for (int i = 1; i+len-1 <= n; i ++ ){//意思就是 i在区间 [1,n-len+1] 中去 // 枚举
区间
            int l=i,r=i+len-1;//区间在[i,i+len-1] 中间长度为 len// 设置 l 和 r 的区间
            f[l][r]=1e9;//初始化最大值
            for (int k = l; k < r; k ++ )//枚举分界点 //不取 r
                f[l][r]=min(f[l][r],f[l][k]+f[k+1][r]+s[r]-s[l-1]);//找到最小值状态
转移方程为 f[l][k]+f[k+1][r]+s[r]-s[l-1];
        }
    printf("%d\n",f[1][n]);//输出区间 [1,n] 的最小值
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

## 第80页

完全背包写法
状态转移方程： f[j]=(f[j-i]+f[j])
数 位 统 计 DP  
计数问题  
题目链接： 338. 计数问题  - AcW ing 题库
//完全背包的写法
using namespace std;
const int M=1e9+7;
int f[1010],n;
int main()
{
    cin>>n;
    f[0]=1;
    for (int i = 1; i <= n; i ++ )
        for (int j = i; j <= n; j ++ ){
            f[j]=(f[j-i]+f[j])%M;
        }
    cout<<f[n]<<endl;
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

## 第81页

using namespace std;
//因为我们举的分类中，有需要求一串数字中某个区间的数字，例如 abcdefg 有一个分类需要求出
efg+1
int get(vector<int> num,int l,int r){
    int res=0;
    for(int i=l;i>=r;i--)res=res*10+num[i];//这里从小到大枚举的是因为下面 count 的时候
读入数据是从最低为读到最高位，那么此时在 num 里，最高位存的就是数字的最低位，那么假如我们要
求efg，那就是从 2 算到 0
    return res;
}
int power10(int i)//这里有power10 是因为有一个分类需要求得十次方得值
{
    int res=1;
    while(i--)res*=10;
    return res;
}
int count(int n,int x){
    if(!n)return 0;//n=0则返回 0
    vector<int> num;//num用来存储数中的每一位数字
    while(n){
        num.push_back(n%10);
        n/=10;
    }
    n=num.size();//得出它的长度
    int res=0;
    for (int i = n-1-!x; i >=0; i -- )
    //这里需要注意，我们的长度需要减一，是因为 num 是从 0 开始存储，而长度是元素的个数，因此
需要减1才能读到正确的数值，而 !x 出现的原因是因为我们不能让前导零出现，如果此时需要我们列举
的是0得出现的次数，那么我们自然不能让他们出现第一位，而是从第二位开始枚举
    {
        if(i<n-1)//其实这里可以不同 if 判断，因为 for 循环里面实际上就已经达成了 if 得判断，
但为了方便理解还是加上 if 来理解，这里 i 要小于 n-1 的原因是因为我们不能越界只有 7 位数就最高从七
位数开始读起
        {
            res+=get(num,n-1,i+1)*power10(i);//这里就是第一个分类， 000~abc-1 ，那么此
时情况个数就会是 abc*103, 这里的 3 取决于后面的 efg 的长度，假如他是 efgh ，那么就是 4
            //这里的n-1,i+1, 自己将数组列出然后根据分类标准就可以得出为什么 l 是 n-1,r=i+11
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32

## 第82页

状 态 压 缩 DP  
蒙德里安的梦想  
题目链接： U204941 蒙德里安的梦想  - 洛谷  | 计算机科学教育新生态  (luogu.com.cn)
视频讲解： 431 状态压缩 DP 蒙德里安的梦想【动态规划】 哔哩哔哩 bilibili            if(!x)res-=power10(i);//假如此时我们要列举的是 0 出现的次数，因为不能出现前
导零，这样是不合法也不符合我们的分类情况，例如 abcdefg 我们列举 d ，那么他就得从 001~abc-1 ，
这样就不会直接到 efg ，而是会到 0efg ，因为前面不是前导零，自然就可以列举这个时候 0 出现的次
数，所以要减掉 1 个 power10
        }
        if(num[i]==x)res+=get(num,i-1,0)+1;
        else if(num[i]>x)res+=power10(i);
    }
    return res;//返回res，即出现次数
}
int main()
{
    int a,b;
    while(cin>>a>>b,a||b){
        if(a>b)swap(a,b);//a大于b则交换 a ， b 使得变成合法参数
        for(int i=0;i<10;i++)
            cout<<count(b,i)-count(a-1,i)<<' ';//使用前缀和思想解决 [a,b] 的 i 出现的次
数
        cout<<endl;
    }
    return 0;
}33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
using namespace std;
const int N = 12,M=1<<N;
int n,m;
long long f[N][M];
bool st[M];
int main()
{
    int n,m;
    while(cin>>n>>m,n||m){
        memset(f, 0, sizeof f);
        //预处理：判断合并列的状态 i 是否合法
        //如果合并列的某行是 1 表示横放，是 0 表示竖放
        //如果合并列不存在连续的奇数个 0 ，即为合法状态
        for (int i = 0; i < 1<<n; i ++ ){
            st[i]=true;
            int cnt=0;//记录合并列中连续 0 的个数
            for (int j = 0; j < n; j ++ ){
                if(i>>j&1){//如果是1
                    if(cnt&1){//如果连续 0的个数是奇数
                        st[i]=false;//记录i不合法
                        break;
                    }1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第83页

状态转移方程：
最短 Hamilton路径  
题目链接： U122241 最短 Hamilton 路径  - 洛谷  | 计算机科学教育新生态  (luogu.com.cn)
状态转移方程：                }else cnt++;//如果是0，记录 0 的个数
            }
            if(cnt&1)st[i]=false;//处理高位 0的个数
        }
        //状态计算
        f[0][0]=1;//第0列不横放是一种合法的方案
        for (int i = 1; i <= m; i ++ )//阶段：枚举列
            for (int j = 0; j < 1<<n; j ++ )//状态：枚举 i列的状态
                for (int k = 0; k < 1<<n; k ++ )//状态：枚举 i-1 列的状态
                    //两列状态兼容：不出现重叠的 1 ，不出现连续奇数个 0
                    if((j&k)==0&&st[j|k])
                        f[i][j]+=f[i-1][k];
        cout<<f[m][0]<<endl;//第m列不横放，既答案
    }
    return 0;
}26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
if((j&k)==0&&st[j|k])
 f[i][j]+=f[i-1][k];1
2
using namespace std;
const int N = 20,M = 1 << N;
int n;
int w[N][N];
int f[M][N];//第一维表示是否访问到该点的压缩状态，第二维是走到点 j
            //f[i][j]表示状态为 i 并且到 j 的最短路径
int main(){
    cin>>n;
    for (int i = 0; i < n; i ++ )
        for (int j = 0; j < n; j ++ )//读入i到 j的距离
            cin>>w[i][j];
    memset(f, 0x3f, sizeof f);
    f[1][0]=0;
    for (int i = 0; i < 1 << n; i ++ )//枚举压缩的状态
        for (int j = 0; j < n; j ++ )//枚举到0~j的点
            if(i >> j & 1)//该状态存在 j点
                for (int k = 0; k < n; k ++ )//枚举从j倒数第二个点 k
                    if(i >> k & 1)//倒数点k存在
                        f[i][j]=min(f[i][j],f[i-(1<<j)][k]+w[k][j]);//状态转移方
程，在f[i][j]和状态去掉 j 的点 f[i-(i<<j)][k]+w[k][j] 取最小值
    cout<<f[(1<<n)-1][n-1]<<endl;//输出状态全满也就是所有点都经过且到最后一个点的最短
距离
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

## 第84页

树 形 DP  
没有上司的舞会  
题目： P1352 没有上司的舞会  - 洛谷  | 计算机科学教育新生态  (luogu.com.cn)
视频讲解： 417 树形 DP 没有上司的舞会【动态规划】 哔哩哔哩 bilibilif[i][j]=min(f[i][j],f[i-(1<<j)][k]+w[k][j]); 1
using namespace std;
const int N = 6010;
int n;
int w[N];//每个节点的高兴度
int h[N], e[N], ne[N], idx;//邻接表存储树
bool st[N];//判断是否有父节点
int f[N][2];
void add(int a, int b)  // 添加一条边 a->b
{
    e[idx] = b, ne[idx] = h[a], h[a] = idx ++ ;
}
void dfs(int u){
    f[u][0]=0;
    f[u][1]=w[u];//初始化f[u][1] ，当第二维是 0 则不选该点即高兴度为 0 ，同理 f[u][1]=w[u];
    for (int i = h[u]; i!=-1 ; i =ne[i] ){//遍历u的子节点进行深度优先遍历
        int j=e[i];
        dfs(j);
        //状态转移方程
        f[u][0]+=max(f[j][0],f[j][1]);//f[u][0]表示不选择父节点 u ，所以在 f[j][0] 和
f[j][1]取最大值
        f[u][1]+=f[j][0];//f[u][1]表示选择根节点 u ，所以累加不选择子节点的 f[j][0]
    }
}
int main()
{
    cin>>n;
    for (int i = 1; i <= n; i ++ )cin>>w[i];
    memset(h, -1, sizeof h);
    for (int i = 0; i < n-1; i ++ ){
        int a,b;
        cin>>a>>b;
        add(b,a);
        st[a]=true;//存储是否存在父节点
    }
    int root=1;
    while(st[root])root++;//判断是否是根节点
    dfs(root);//dfs对f[i][j] 进行状态转移计算
    cout<<max(f[root][0],f[root][1])<<endl;//取选与不选根节点的最大值
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44

## 第85页

状态转移方程：
记 忆 化 搜 索  
滑雪  
题目链接： [P1434 SHOI2002 ] 滑雪  - 洛谷  | 计算机科学教育新生态  (luogu.com.cn)
状态转移方程： v=max(v,dp(a,b)+1);
六、贪心  f[u][0]+=max(f[j][0],f[j][1]);
f[u][1]+=f[j][0];1
2
using namespace std;
const int N = 310;
int n,m;
int h[N][N];
int f[N][N];
int dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
int dp(int x,int y){
    int &v=f[x][y];
    if(v!=-1)return v;//记忆化搜索核心
    v=1;
    for (int i = 0; i < 4; i ++ ){
        int a=x+dx[i],b=y+dy[i];
        if(a>=1&&a<=n&&b>=1&&b<=m&&h[a][b]<h[x][y])//判断是否越界且上一个经过的点的高
度是否大于当前高度
            v=max(v,dp(a,b)+1);
    }
    return v;
}
int main()
{
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= m; j ++ )
            scanf("%d", &h[i][j]);
    memset(f, -1, sizeof f);
    int res=0;
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= m; j ++ )
            res=max(res,dp(i,j));
    printf("%d\n",res);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35

## 第86页

一 个 贪 心 算 法 总 是 做 出 当 前 最 好 的 选 择 ， 也 就 是 说 ， 它 期 望 通 过 局 部 最 优 选 择 从 而 得 到 全 局 最 优 的 解 决
方案。 --- 《算法导论》
区 间 问 题  
区间选点  
给 定  N 个 闭 区 间 $[a_i,b_i]$ ， 请 你 在 数 轴 上 选 择 尽 量 少 的 点 ， 使 得 每 个 区 间 内 至 少 包 含 一 个 选 出 的
点
输出选择的点的最小数量。  
using namespace std;
const int N = 100010;
int n;
struct Range{
    int l,r;
    bool operator <(const Range& W)const{
        return r<W.r;
    }//重载小于号
}range[N];
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ){
        int l,r;
        scanf("%d%d", &l, &r);
        range[i]={l,r};//读入l,r
    }
    sort(range,range+n);//按右端点进行排序
    int res=0,ed=-2e9;//ed代表上一个点的右端点
    for (int i = 0; i < n; i ++ ){1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23

## 第87页

最大不相交区间数量  
给 定  $N$ 个 闭 区 间  $[a_i,b_i]$ ， 请 你 在 数 轴 上 选 择 若 干 区 间 ， 使 得 选 中 的 区 间 之 间 互 不 相 交 （ 包 括
端点）。
输出可选取区间的最大数量。
结论： 最大不相交区间数量 = 最少覆盖区间点数
为什么最大不相交区间数 = 最少覆盖区间点数呢？
因为如果几个区间能被同一个点覆盖
说明他们相交了，所以有几个点就是有几个不相交区间        if(range[i].l>ed){
            res++;//点的数量加一
            ed=range[i].r;
        }
    }
    printf("%d\n",res);
    return 0;
}24
25
26
27
28
29
30
31
using namespace std;
const int N = 100010;
int n;
struct Range{
    int l,r;
    bool operator <(const Range& W)const{
        return r<W.r;
    }
}range[N];
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ){
        int l,r;
        scanf("%d%d", &l, &r);
        range[i]={l,r};
    }
    sort(range,range+n);
    int res=0,ed=-2e9;
    for (int i = 0; i < n; i ++ ){
        if(range[i].l>ed){
            res++;
            ed=range[i].r;
        }
    }
    printf("%d\n",res);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31

## 第88页

区间分组  
排 序 不 等 式  
排队打水  
有 $n$ 个 人 排 队 到  $1$ 个 水 龙 头 处 打 水 ， 第  $i$ 个 人 装 满 水 桶 所 需 的 时 间 是  $t_i$ ， 请 问 如 何 安 排 他
们的打水顺序才能使所有人的等待时间之和最小？
t[i] 从小到大排序using namespace std;
const int N = 1e5+10;
int n;
struct Range{
    int l,r;
    bool operator<(const Range &W)const{
        return l<W.l;
    }//按左端点排序
}range[N];
int main()
{
    scanf("%d", &n);
    for (int i = 0; i < n; i ++ ){
        int l,r;
        scanf("%d%d", &l, &r);
        range[i]={l,r};
    }
    sort(range,range+n);//sort排序
    priority_queue<int,vector<int>,greater<int>> heap;//小根堆维护所有组的右端点最小
值
    for (int i = 0; i < n; i ++ ){//从左往右枚举
        auto r=range[i];//选择当前区间
        if(heap.empty()||heap.top()>=r.l)heap.push(r.r);
        else{
            heap.pop();
            heap.push(r.r);
        }
    }
    printf("%d\n",heap.size());
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33

## 第89页

计算公式： $t[0]×(n-1)+t[1]×(n-2)+t[2]×(n-3)...+t[n]×0$
笔记作者 QQ ：946808247
欢迎一起交流技术using namespace std;
typedef long long LL;
const int N = 1e5 + 10;
int t[N];
int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &t[i]);
    sort(t, t + n);//排序
    LL  ans = 0;
    for (int i = 0; i < n; i++) {
        ans += t[i] * (n - i - 1);//计算
    }
    printf("%lld", ans);
    return 0;
}1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_算法_课程MOC|算法 MOC]]
