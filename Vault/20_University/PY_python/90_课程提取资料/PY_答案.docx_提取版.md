---
id: extract-py-5cacdd24
type: extract
status: extracted
course: PY
source:
  - "[[91_Raw-Archive/DOC/PY_答案.docx_资料_未知日期_5cacdd24.docx]]"
source_pages: all
source_hash: "5cacdd2431efcc1b73aceeb07f015a4f1f783b92dca528bc72d34225b1e7a6b4"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# 答案.docx：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

华中农业大学《Python 程序设计》试卷 A 答案

一、单项选择题（每小题 2 分，共 20 分）

C
解析：Python 变量名不能以数字开头，1_x违反命名规则。

B
解析：random.random()*31+10生成范围为 [10,41) 的浮点数，取整后得到 [10,40] 的整数。

C
解析：字符串s1="kalofcoihzau"中，'coi'对应索引 5 到 7（左闭右开切片[5:8]）。

D
解析：x=2**3%2=8%2=0，if 0为 False，执行else输出0+2=2。

A
解析：range(2,10,3)生成2,5,8，求和为2+5+8=15。

D
解析：test(5,x=6)中位置参数已赋值x=5，再用关键字参数x=6会冲突。

C
解析：Python 中双下划线开头的属性__x3为私有属性。

C
解析：n%i==0表示n能被i整除，不是素数。

A
解析：写入"Python"后seek(0)回到开头，读取 3 个字符为"Pyt"。

C
解析：NumPy 数组输出格式为[1 2 3 4 5]。

二、填空题（每小题 1 分，共 10 分）

6
解析：列表包含 6 个元素：[2,'a',[1,2],(1,2),{'a':1},{1,2}]。

12.346
解析：%1.3f保留三位小数，四舍五入12.3456为12.346。

sqlite3

6
解析：int(5.2)=5，(2>1)=True=1，求和为6。

3
解析：7//2=3（整除）。

scrapy

Kivy

turtle

Pillow

cv2

三、程序阅读题（每小题 5 分，共 30 分）

30
解析：6 月为小月，固定 30 天，与闰年无关。

[73, 59]
解析：isprime()函数判断素数，列表中仅 73 和 59 是素数。

4 8
解析：字典键'A'和'C'在str1中，值翻倍后输出4和8。

'c'
解析：se[2]取键'C'对应列表['c',3,{3:'c'}]，se[2][2][3]获取'c'。

3
解析：df["A"][2]取第三行列表['C',3]，[1]获取3。

study hard
解析：索引 4 超出列表[1,2,3]范围，触发IndexError，返回"study hard"。

四、程序填空题（每空 2 分，共 10 分）

(1) connect
(2) cursor
(3) UPDATE
(4) execute
(5) fetchall

五、编程题（共 30 分）

28.（8 分）

python

运行

# 写入CSV文件  with open('test.csv', 'w') as f:  

    f.write('1,2,3\n4,5,6\n7,8,9')  

# 读取CSV文件  with open('test.csv', 'r') as f:  

    data = f.read()  

    print(data)  

29.（10 分）

python

运行

import threading  import time  

def worker_1():  

    time.sleep(2)  

    print("worker_1 完成")  

def worker_2():  

    time.sleep(3)  

    print("worker_2 完成")  

def worker_3():  

    time.sleep(4)  

    print("worker_3 完成")  

# 创建线程  

t1 = threading.Thread(target=worker_1)  

t2 = threading.Thread(target=worker_2)  

t3 = threading.Thread(target=worker_3)  

# 启动线程  

t1.start()  

t2.start()  

t3.start()  

# 等待所有线程完成  

t1.join()  

t2.join()  

t3.join()  

30.（12 分）

python

运行

class person:  

    def __init__(self, name, age, sex):  

        self.name = name  

        self.age = age  

        self.sex = sex  

    def speak(self):  

        print(f"{self.name},年龄:{self.age},性别:{self.sex}")  

class student(person):  

    def __init__(self, sid, name, age, sex, sclass):  

        super().__init__(name, age, sex)  

        self.sid = sid  

        self.sclass = sclass  

    def study(self):  

        self.speak()  

        print(f"学号:{self.sid},班级:{self.sclass}")  

# 测试实例  

s = student("2018317210101", "张珊", 18, "女", "计算机1801")  

s.study()  

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_python_课程MOC|python MOC]]
