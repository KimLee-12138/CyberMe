---
id: extract-calculus-90532ac8
type: extract
status: extracted
course: CALCULUS
source:
  - "[[91_Raw-Archive/PDF/CALCULUS_8.7 斯托克斯公式与旋度2.pdf_课件_未知日期_90532ac8.pdf]]"
source_pages: all
source_hash: "90532ac873f6f25fda08d65ec259be32391d662988ea3487cb297c555985e531"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 8.7 斯托克斯公式与旋度2.pdf：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

## 第1页

§8.7 斯托克斯公式与旋度

## 第2页

一、斯托克斯公式
右手大拇指指向  的侧  其余四
指环绕的方向即为  的正向 ,
.+
 
双侧曲面  的侧与其边界曲线
  的正向 右手法  则 满足 ：+
 
规定：



## 第3页

定理：
设  是一张光滑或分片光滑的定向曲面    的正
向边界  为光滑或分段光滑的闭曲线  若函数
  则(1),
.
( , , ), ( , , ), ( , , ) ( ) ,P x y z Q x y z R x y z C+


( ) ( ) ( ) .R Q P R Q Pdydz dzdx dxdyy z z x x y       − + − + −       
Pdx Qdy Rdz
+= + +
一、斯托克斯公式

## 第4页

一、斯托克斯公式
x
y
z
o
),(: yxfz=
xyD

C
n
设Σ与平行于
z 轴的直线相交不多于一点 , 
并Σ取上侧 ,有向曲线 C为Σ的正向边界曲
线
在
xoy的投影.且所围区域
xyD . 
证明
xPd
yxyPxzzPdd dd−=
先证

## 第5页

斯托克斯公式还可写为：
或用第一类曲面积分表示：




R Q Pz y xdxdy dzdx dydz
dS
R Q Pz y x cos cos cos




. 
+++= Rdz Qdy Pdx
. 
+++= Rdz Qdy Pdx一、斯托克斯公式

## 第6页

（2）斯托克斯公式的实质：
建立了有向曲面上的曲面积分与其边界曲线上
的曲线积分之间的联系。
（3）斯托克斯公式 格林公式特殊情形
)    ( 面上的平面区域时是xoy曲面积分 二重积分 曲线积分1 2（1）斯托克斯公式的证明思路：注：一、斯托克斯公式

## 第7页

一、斯托克斯公式
Stokes’ Theorem is named after the Irish mathematical physicist Sir 
George Stokes (1819 –1903). Stokes was a professor at Cambridge 
University (in fact he held the same position as Newton, Lucasian
Professor of Mathematics) and was especially noted for his studies of 
fluid flow and light. What we call Stokes’ Theorem was actually 
discovered by the Scottish physicist Sir William Thomson  (1824 –1907, 
known as Lord Kelvin). Stokes learned of this theorem in a letter from 
Thomson in 1850 and asked students to prove it on an examination 
at Cambridge University in 1854. We don’t know if any of those 
students was able to do so.
--Calculus Early Transcendentals 9th Edition by James Stewart

## 第8页

0
xyD
x
y
z
n
1
1
1
x
y
o
1
1
xyD例1、一、斯托克斯公式
利用斯托克斯公式计算积分
其中为平面 x+ y+ z = 1 被三坐标面所截三角
形的整个边界 , 若从向量 (1,1,1)正向看去 , 取逆
时针方向 .

## 第9页

0
xyD
x
y
z
n
1
1
1
x
y
o
1
1
xyD例1、一、斯托克斯公式
利用斯托克斯公式计算积分
其中为平面 x+ y+ z = 1 被三坐标面所截三角
形的整个边界 , 若从向量 (1,1,1)正向看去 , 取逆
时针方向 .

## 第10页

求  其中  
是平面  截立方体  
 的表面所得截痕  从  轴正向看去  取
逆时针方向 2 2 2 2 2 2( ) ( ) ( ) ,
3: 0 1,0 1,2
0 1 . ,
.y z dx z x dy x y dz
x y z x y
zx− + − + − 
+ + =    
  
例2、
z
x
y
o

n
一、斯托克斯公式

## 第11页

xyD
23=+yx
21=+yx
求  其中  
是平面  截立方体  
 的表面所得截痕  从  轴正向看去  取
逆时针方向 2 2 2 2 2 2( ) ( ) ( ) ,
3: 0 1,0 1,2
0 1 . ,
.y z dx z x dy x y dz
x y z x y
zx− + − + − 
+ + =    
  
例2、
z
x
y
o

n
一、斯托克斯公式

## 第12页

.   ,    .  1    ,  
2 22 2 2
取逆时针方向 轴正向看去从曲线界 位于第一卦限部分的边 抛物面是其中 计算曲线积分
−−= ++

zy x zdzz dyxy zdxx例3、
z
o
x
y
1
1
1一、斯托克斯公式
z
x
y
o

## 第13页

x
y
o
12 2=+y x
.   ,    .  1    ,  
2 22 2 2
取逆时针方向 轴正向看去从曲线界 位于第一卦限部分的边 抛物面是其中 计算曲线积分
−−= ++

zy x zdzz dyxy zdxx例3、一、斯托克斯公式
2
15 16+
z
x
y
o

## 第14页

二、旋度

## 第15页

二、旋度
定义：
在点 处的旋度( , , ) ( ( , , ), ( , , ), ( , , ))
( , , )F x y z P x y z Q x y z Q x y z
x y z=
rot i j k
Fx y z
P Q R  =  
( ) ( ) ( ) .R Q P R Q Pi j ky z z x x y     = − + − + −     
例4、
求电场强度  的旋度 3.qErr=

## 第16页

二、旋度
例4、
求电场强度  的旋度 3.qErr=

## 第17页

斯托克斯公式的旋度表示：
rot rot  F d S F n dS F dr
+  =  =   
二、旋度
斯托克斯公式的物理解释 ：
向量场沿有向闭曲线 的环流量等于向量场的
旋度场通过 所张的曲面的通量
 的正向与 的侧符合右手法则.
()FF 


环流量：
沿定向闭曲线 的积分 ( ) . F F dr F e ds
  = 

## 第18页

应用场景
旋度在流体力学和电磁学中有着重要的应用。例如，在流
体力学中，旋度可以用来描述流体的涡旋运动，帮助分析涡旋
的形成和演化。在电磁学中，旋度用于描述磁场的旋度，即安
培定律，描述电流产生的磁场。此外，旋度还用于流体动力学
中的涡度方程，描述流体中的涡旋结构。

## 第19页

定理：
设  是空间的一个一维单连通区域，  函数 
 则
沿  内定向 的充要
条件是
                       曲线
  积分与路径无关
      (1)( , , ), ( , , ), ( , , ) ( ) ,
( , , ) ( ( , , ), ( , , ), ( , , ))
0.G
P x y z Q x y z R x y z C
F x y z P x y z Q x y z R x y z
G
rot F
=
=
二、旋度

## 第20页

作业
习题8-7：1（偶数题）、 3             
小结
1、双侧曲面及其边界侧的规定；
2、斯托克斯公式建立了曲面上第二类曲面积分
与其边界上第二类曲线积分的联系；
3、散度、环流量的概念；
4、斯托克斯公式的物理意义 .

## 第21页

斯托克斯 (1819 -1903)
英国数学物理学家 . 他是 19世纪英国
数学物理学派的重要代表人物之一 , 其
主要兴趣在于寻求解重要数学物理问题
的有效且一般的新方法 , 在1845年他导
出了著名的粘性流体运动方程 ( 后称之
为纳维–斯托克斯方程 ), 1847年先于
柯西提出了一致收敛的概念 . 他提出的斯托克斯公式
是向量分析的基本公式 . 他一生的工作先后分五卷
出版 .

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_微积分_课程MOC|微积分 MOC]]
