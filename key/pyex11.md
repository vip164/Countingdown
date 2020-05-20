---
title: 《Python编程实践》第11章练习题及解答
date: 2019-08-03 11:32:31
tags: 
  - Python
  - 习题
comments: true
categories:
  - [Python]
meta:
  top: false
  date: true
  categories: true 
  counter: true 
  updated: true
  share: true
  tags: true 
recommended_posts: false
mathjax: true
---



《Python编程实践》第11章练习题及解答



<!-- more -->



> 版权声明
>
> 本文**可以**在互联网上自由转载，但必须：注明出处(作者：陈波，刘慧君)并包含指向本页面的链接。
>
> 本文**不可以**以纸质出版为目的进行改编、摘抄。





#### 11-1

假定一个文本文件中包含未指定个数的分数数据，请编写一个程序，从文件中读入分数，以列表的方式打印
输出所有的分数，同时计算分数之和、平均数以及最大分数。文件中的分数用空格分隔，程序运行时应该提示用户
输入一个文件名。

答案：

```python
filname=input("请输入要读取的文件名：")
with open(filname,"r") as f:
    data_list=[]
    for x in f.readlines():
        data_list+=x.split(",")
Sum=0
Count=0
Max=0
for x in data_list:
    Sum+=float(x)
    Count+=1
    Max=max(Max,float(x))
print("分数：",data_list)
print("分数之和",Sum)
print("平均数",Sum/Count)
print("最大分数",Max)


```

思路：

```
打开文件，读取所有行，然后对每一行使用split将分数分开存储到列表中，以列表的方式打印输出所有的分数，计算分数之和、平均数以及最大分数都是基于列表的操作。
```



#### 11-2

编写程序统计一个文本文件中的字符数、单词数以及行数。单词由空格分隔。程序应提示用户输入一个文件
名。

答案：

```python
filename=input("请输入读取的文件名：")

with open(filename,"r") as f:
    lines_num=0
    words_num=0
    letters_num=0
    for line in f.readlines():
        lines_num+=1
        letters_num += len(line.rstrip())
        for word in line.split(" "):
            words_num+=1

print("字符数：",letters_num)
print("单词数：",words_num)
print("行数：",lines_num)

```

思路：

```
打开文件，读取所有行；
由于换行时会有多余的字符，使用rstrip方法去除右空格，然后使用len方法，统计字符数；
使用split方法，将单词分开并计数。
```

#### 11-3

编写一个程序将随机产生的1000个1000以内整数写入一个文件，文件中的整数由逗号分隔。从文件中读取数
据，打印输出排序后的结果。

答案：

```python
import random
filename=input("请输入写入的文件名称：")

with open(filename,"w") as f:
    for x in range(1000):
        if x!=999:
            f.write(str(random.randint(0,1000))+",")
        else:
            f.write(str(random.randint(0, 1000)))

with open(filename,"r") as f:
    data=[]
    for x in f.readlines():
        for y in x.split(","):
            data.append(int(y))
print(sorted(data))
```

思路：

```
pass
```

#### 11-4

磁盘文件file1和file2,各存放有一行字母，请编写程序，将两个文件的内容读出，合并两个文件的内容并按照
字母顺序排序，再输出到一个新文件file3中。

答案：

```python
with open("file1","r") as f:
    data1=f.readlines()

with open("file2","r") as f:
    data2=f.readlines()

data3=sorted(str(data1[0])+str(data2[0]))
with open("file3","w") as f:
    ans=""
    for ch in data3:
        ans+=ch
    f.write(ans)
```

思路：

```
pass
```

#### 11-5

编写一个程序统计某个字符串在文本文件中出现的次数。

答案：

```python
with open("11-5","r") as f:
    data=""
    for x in f.readlines():
        data+=x.strip()
print(data.count("abc"))
```

思路：

```
注意使用count方法。
```

#### 11-6

编写一个程序将某个指定的字符串从文本文件中删除。

答案：

```python
with open("11-6","r") as f:
    data=""
    for x in f.readlines():
        data+=x.strip()
print(data.replace("abc",""))
```

思路：

```
注意使用replace方法。
```

#### 11-7

编写程序将工人张成的姓名、地址、电话号码以及工资信息（包含职称工资、补贴以及奖励3部分）写到文件
class.dat中，请分别使用configparser及json两种途径实现。

答案：

```python
import configparser
import json
#configparser
people=["张成","重庆市","10086",3000,800,500]
data=configparser.ConfigParser()
section="Basic"
data[section]={}
data[section]["name"]=people[0]
data[section]["address"]=people[1]
data[section]["number"]=people[2]

section="Salary_Info"
data[section]={}
data[section]["salary"]=str(people[3])
data[section]["subsidy"]=str(people[4])
data[section]["reward"]=str(people[5])
with open("class.dat","w") as f:
    data.write(f)

#json
people={"name":"张成","address":"重庆市","number":"10086","salary":3000,"subsidy":800,"reward":500}
with open("class.dat","w") as f:
    json.dump(people,f)
```

思路：

```
pass
```

#### 11-8

请借助于struct模块将下述circles列表及其内部数据打包并存入一个二进制文件，然后再从二进制文件读出，
结果为一个新的列表circles2。遍历打印circles2列表内的数据。注意: 程序应能兼容circles列表内部元素个数不同
的情况。

答案：

```python
import struct
class Circle:
    def __init__(self,center,radius):
        self.xCenter,self.yCenter = center
        self.radius = radius
circles = []
circles.append(Circle((3.2,0.1),15.7))
circles.append(Circle((0,0),0.75))
circles.append(Circle((0.1,2.2),100.24))

with open("11-8","wb") as f:
    for circle in circles:
        data=struct.pack("<fff",circle.xCenter,circle.yCenter,circle.radius)
        #print(data)
        f.write(data)

with open("11-8","rb") as f:
    rawdata=f.read()
Count=len(rawdata)//4
circles = []
for x in range(0,Count,3):
    *center,radius=struct.unpack("<fff",rawdata[x*4:x*4+12])
    circles.append(Circle(center,radius))
for circle in circles:
    print("%.2f,%.2f,%.2f"%(circle.xCenter,circle.yCenter,circle.radius))
```

思路：

```
浮点数为4个字节，每次读取3个浮点数。
```

