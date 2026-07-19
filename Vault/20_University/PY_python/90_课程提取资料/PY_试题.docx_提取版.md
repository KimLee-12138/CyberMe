---
id: extract-py-d8a1f457
type: extract
status: extracted
course: PY
source:
  - "[[91_Raw-Archive/DOC/PY_试题.docx_资料_未知日期_d8a1f457.docx]]"
source_pages: all
source_hash: "d8a1f4571578b2ecad610bc2b4bb0023da593f6665a0ad3c28df12db53541c7b"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 试题.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

Python程序设计-2019-2020-2-大数据19级期末考试

简答题 （总分：15.00）

1.	关于Python的思考（理论考试题目）（分值：15.00）

请简要回答如下问题：

(1) 请写出你认为最重要的3~5个Python第三方库，并指出各自典型特点；

(2) Python仍然在不断更新，如果需要你对Python进行功能扩展，你最想设计出哪种功能的库，请简要说明；

(3) 请结合Python生态，展望未来编程语言发展趋势，并简要说明。

编程题（总分：100.00）

1.	质因数分解（实验考试题目） （分值：30.00）

【问题描述】输入一个正整数（不超过1000），验证其是否可以分解为若干个质数乘积的形式

【输入形式】

【输出形式】

【样例输入】30

【样例输出】30=2*3*5

【样例说明】分解后的质数应该是从小到大的顺序进行乘积

【评分标准】

2.	成绩分析（实验考试题目） （分值：30.00）

【问题描述】

当前目录下有一个文件名为class_score.txt

的文本文件，存放着某班学生的学号、姓名、微积分课成绩（第3列）和英语课成绩（第4列）。请编程完成下列要求：

（1）分别求这个班微积分和英语的平均分（保留1位小数）并输出。

（2）找出两门课都不及格（<60）的学生，输出他们的学号、姓名和各科成绩。

（3）找出两门课的平均分在90分以上的学生，输出他们的学号、姓名和各科成绩。

   请用三个函数分别实现以上要求。

【样例输出】

math aver:88.5,Eng aver:72.7

Two courses failed:

2016308200131zhouxiaodi5552

2016308200315liuanqi5554

aver of two(>90):

2016308200101caichangrong94100

2016308200102aichunhui9296

2016308200119wanghaozhi9498

2016308200210yexiang9493

2016308200226liuchang9095

2016308200305mengyoulian9486

2016308200307wangxudong9294

2016308200310niuhong9488

2016308200314weihaobin9496

2016308200321wangzilv9485

3.	最长连续递增序列（实验考试题目） （分值：40.00）

【问题描述】

输入一组各不相同的无序正整数，用空格间隔，编程求出其中最长的连续递增子序列（该序列中后一个整数比前一个整数多1，序列的长度是指序列中整数的个数，长度应大于等于2）。例如输入13个整数：3520 4 3 89 56 88 3521 9 90 1 99 2 87，其中连续升序子序列有3个：3520 3521，1 2 3 4和87 88 89 90，长度分别为2、4、4，所以后两个子序列都是最长的连续递增子序列。当整个序列不存在长度大于等于2的连续递增序列时，直接输出0。最终结果写到同目录下的文件out.txt中。

【输入形式】

输入这些不相同的无序正整数，各整数之间以一个空格分隔

【输出形式】

在文件out.txt第一行中输出最长连续递增子序列的长度，然后在下一行开始输出最长连续递增子序列，各整数之间以一个空格分隔，每行最后一个整数后也要有一个空格。如果有多个长度相同的子序列，按照各个子序列从小到大分多行输出

若没有连续递增子序列，直接输出0。

【样例输入1】

3520 4 3 89 56 88 3521 9 90 1 99 2 87

【样例输出1】

4

1 2 3 4 

87 88 89 90 

【样例输入2】

5 8 21 2 14

【样例输出2】

0

【样例说明】

输出结果要写入文件out.txt中，如果直接print输出会扣分。

文件上传编程题 （总分：85.00）

1.	英文段落分析（理论考试题）（分值：25.00）

已知有如下一段英文段落，请编程回答相关问题。

text = 'Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.'

(1) 请找出text中出现次数top 5的单词(忽略大小写)；

(2) 请使用正则表达式统计text中python出现的次数(忽略大小写)；

(3) 请使用正则表达式编写一个函数检查字符串中是否只包含数字和大小写字母，如果是返回True，如果否返回False。

2.	英文单词管理（理论考试题目）（分值：30.00）

小明希望用电脑记录他每天掌握的英文单词。

请设计程序和相应的数据结构，使小明能记录新学的英文单词和其中文翻译，并能很方便地根据英文来查找中文。

该程序功能如下，完成后将代码和不少于5个用例的测试文档报告（word或txt均可）压缩后上传。

(1) 背单词(添加单词)；

(2) 查单词(根据单词进行翻译)；

(3) 修改单词含义。

3.	网络数据分析与展示（理论考试题目）（分值：30.00）

数据文件：

LJdata.xlsx   

请从已经爬取的链家网数据中，做相关数据分析，数据从上面链接下载，问题如下：

（1）请对整个数据集进行统计分析，如常见的描述性统计；

（2）找到最近更新信息的20套房子；

（3）求房龄最小的20套房子的平均看房人数、平均面积；

（4）求房子价格的分布(均值，方差，中位数)；

（5）对区域列的内容进行词云展示。

请将上面各个问题结果写成word报告，格式不限，连同Python代码，压缩后一起上传。

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_python_课程MOC|python MOC]]
