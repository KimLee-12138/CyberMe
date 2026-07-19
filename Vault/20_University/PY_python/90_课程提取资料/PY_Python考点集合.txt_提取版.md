---
id: extract-py-e3ef490d
type: extract
status: extracted
course: PY
source:
  - "[[91_Raw-Archive/DOC/PY_Python考点集合.txt_笔记_未知日期_e3ef490d.txt]]"
source_pages: all
source_hash: "e3ef490d8c3f65314656665c2cccd86693cc7596b36c912ad41375029d98823b"
extract_method: "batch-auto"
created: 2026-07-17
updated: 2026-07-17
verified_by: ""
confidence: medium
needs_review: true
review_reason: "批量自动提取，需人工核对"
---

# Python考点集合.txt：提取版

> 本文件是检索中间材料，不是已核对的正式知识结论。

数据分析:
import numpy as np   矩阵库
np.array(list)  实例化一个数组对象
np.zeros()零矩阵
np.ones()全1矩阵
np.eye()单位矩阵

import scipy 解线性方程库
from scipy import linalg
a=scipy.mat('系数')
b=scipy.mat('等式右边的常数')
result=linalg.solve(a,b)结果

import matplotlib.pyplot as plt  数据可视化库
x=[]
y=[]
plt.plot(x,y,label="函数标题") 创建画图
plt.title('图像标题')
plt.xlabel('自变量')
plt.xlabel('因变量')
plt.legend()显示图例
plt.show()显示作图窗口

from pandas import Series 一维数组库
Series([列表],index=[下标列表])

from pandas import DataFrame 多维数组库
obj=DataFrame([series1第一行],[series第二行]) 
df_obj.head()查看前几行数据 默认5
df_obj.T 转置
df_obj.tail()  查看后几行的数据 默认后5行
df_obj.index   查看索引
df_obj.columns 查看列名
df_obj.values  查看数据值
df_obj.describe描述性统计
df_obj.sort(colunmns='')按照列名进行排序
df_obj.sort_values多列排序
df_obj['列索引']显示列名下的数据
df_obj[1:3]获取1~3行的数据（切片操作）
df_obj.reindex()根据index参数重新排序

文件编辑:
txt||doc文件:
with open(r'test.txt','w+',encoding='utf-8') as f:
	f.write('写入内容')
	f.writelines('写入多行')
f=open(r'test.txt','r+',encoding='utf-8')
data=f.read()读取数据
dataline=f.readline()读取某行
datalines=f.readlines()读取多行
f.close()

csv文件处理
import csv 库文件
with open(r'test.csv','w+',encoding='utf-8') as f:
	writer=csv.writer(f)
	writer.writerows('写入数据')
f=open(r'test.csv','r+',encoding='utf-8') 输出数据
reader=csv.reader(f)
for row in reader:
     print(row)
f.close()

Excel文件处理：
import xlwt  写入库文件
import xlrd	读取库文件
book=xlwt.Workbook(encoding='utf-8')  创建工作薄
sheet=book.add_sheet('表1') 创建工作表
col=('第一列','第二列','第三列') 列数据
for i in range(3):
	sheet.write(0,i,col[i]) 第一行写入列数据
sheet.write(行,列,值) 往单元格写入数据
data=xlrd.open_workbook('test.xls') 读取操作
table=data.sheets()[0] 打开第一个表
nrows=table.nrows 获取行数
ncols=table.ncols 获取列数
for row in range(nrows):
	print(table.row_values(row))按照行输出

数据库:
import sqlite3 导入库
conn=sqlite3.connect(r"test.db")#链接数据库
cur=conn.cursor()#获取游标
sql='''
	create table 表名(
	sid char(4) primary key,
	sname varchar(8),
	sage smallint);
'''创建表
sql1="insert into 表名 values('1','name','18');"增
sql2="delete from 表名 where sid='1';"删
sql3="update 表名 set sname='重新设置',sage='19' where sid='1';"改
sql4="select * from 表名 where sid='1';"查
datalist=cur.fetchall() 搭配查找使用将查找的数据返回到datalist
cur.execute(sql)提交sql命令
conn.commit()上传到数据库文件
cur.close()
conn.close()关闭数据库连接

GUI编程:
from tkinter import * 导入库文件
from tkinter import messagebox 窗口消息库文件
win=Tk() 获取窗口对象
win.title('窗口名')
win.geometry("520x520")设置窗口大小
Label(win,text="标签").grid(row=0,column=0,sticky='e')创建标签
def Submit():
	messagebox.showinfoh(title="窗口名字",message="显示的消息")
	# showinfo(title='提示',message='欢迎使用本系统') #提示消息框
	# showwarning(title='提示',message='请填写验证码')#警告提示框
	# showerror(title='提示',message='账号或密码错误')#错误提示框
Button(win,text='提交按钮',command=Submit).grid(row=0,column) 搭配函数 点击按钮执行函数
e=Stringvar()     #Intvar
e.set('设置值')
Entry(win,textvariable=e).pack()文本输入框
data=e.get()获取文本框的值 最好搭配函数使用
Radiobutton(win,text='男',variable=v,value=1).pack()
Radiobutton(win,text='女',variable=v,value=0).pack()单选框
Text(win).insert(1.1,'输入的数据').pack()文本框

win.mainloop()显示交互窗口

Web编程
from flask import Flask,request,url_for,render_template 导入库文件
app=Flask(__name__)初始化 记住是两个下划线
@app.route('/')
def fun1():
	return '显示的值'
@app.route(/user/<name>)
def fun2(name):
	return '参数传递:%s'%name
@app.route(/user/html) #模板使用
def fun3():
	datalist=[列表元素]
	return render_template('index.html',datalist=datalist) 打开index.html文件 传参 {% html文件中代码写在这里面 %}
@app.route('/query_url') #反向路由
def query_url():
    return 'query url:'+url_for('query_user')

if __name__=='__main__':
    app.run() 运行

## 提取异常

- 批量自动提取，未经人工核对。

---
> 课程导航：[[../00_python_课程MOC|python MOC]]
