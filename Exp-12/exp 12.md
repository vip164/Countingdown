实验报告3 组合数据类型 **拾月剑客**** vip164**

**《程序设计技术（基于**** Python ****）》实验报告**

| **年级、专业、班级** | **2019**** 级 **|** 姓名** |
 | **学号** |
 |
| --- | --- | --- | --- | --- | --- |
| **实验题目** | 分支和循环程序设计 |
| **实验时间** | **2019-05-07** | **实验地点** |
 |
| **学年学期** | **2019-2020**** （ ****2**** ） **|** 实验性质 **| □** 验证性 **** ■ ****设计性**  **□**** 综合性** |
| 一、实验目的1． 理解python中得组合数据类型的应用场景。 2.- 理解列表、字典的应用 3.- 学习理解组合数据类型的常用方法。 4. 进一步学习并掌握自顶向下的设计方法和自底向上的实现方法
 |
| 二、实验项目内容德才论宋代史学家司马光在《资治通鉴》中有一段著名的&quot;德才论&quot;：&quot;是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。&quot;现给出一批考生的德才分数，请根据司马光的理论给出录取排名。输入格式：（数据来自data.txt） 输入第一行给出 3 个正整数，分别为：N（≤10000），即考生总数；L（≥60），为录取最低分数线，即德分和才分均不低于L的考生才有资格被考虑录取；H（\&lt;100），为优先录取线——德分和才分均不低于此线的被定义为&quot;才德全尽&quot;，此类考生按德才总分从高到低排序；才分不到但德分到线的一类考生属于&quot;德胜才&quot;，也按总分排序，但排在第一类考生之后；德才分均低于 H，但是德分不低于才分的考生属于&quot;才德兼亡&quot;但尚有&quot;德胜才&quot;者，按总分排序，但排在第二类考生之后；其他达到最低线 L 的考生也按总分排序，但排在第三类考生之后。随后 N 行，每行给出一位考生的信息，包括：准考证号 德分 才分，其中准考证号为 8 位整数，德才分为区间 [0, 100] 内的整数。数字间以空格分隔。输出格式：输出第一行首先给出达到最低分数线的考生人数 M，随后 M 行，每行按照输入格式输出一位考生的信息，考生按输入中说明的规则从高到低排序。当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。
要求：      1.输入输出要有提示；      2.程序代码的重要部分要有注释；      3.编程风格要符合函数式要求。       4.实验分析要全面(需要调试截图)。
 |
| 三、实验的算法（伪代码或者流程图）和源程序# 实验3 德才论def getdata():    &quot;&quot;&quot;从文件中读取数据，读取考生数量，录取录取最低分数线，      为优先录取线和考生原始数据（含学号，德分数，才分数）&quot;&quot;&quot;    listtemp=[]    fo = open(&quot;data.txt&quot;,&quot;r&quot;)    n = fo.readline().split()    num,low,high = int(n[0]),int(n[1]),int(n[2])    for i in range(num):        listtemp.append(list(map(int,fo.readline().split()))) #将数据转化为int型    return num,low,high,listtemp
def fenlei(low,high,listA):    &#39;a&quot;圣人&quot;，b&quot;君子&quot;，c&quot;愚人&quot;，d&quot;小人&quot;&#39;    a=[];  b=[];  c=[];  d=[]    for stu in listA:        if stu[1]\&gt;=high and stu[2]\&gt;=high:            a.append(stu) # 才德全尽        elif stu[1] \&gt;= high and stu[2]\&lt;high:            b.append(stu) # 德胜才        elif stu[1]\&gt;stu[2] and stu[2]\&gt;=low:            c.append(stu) # &quot;才德兼亡&quot;但尚有&quot;德胜才&quot;        elif stu[1]\&gt;=low and stu[2]\&gt;=low:            d.append(stu) # 才德兼亡 但达到录取线    return a,b,c,d
def sortkey(listB):    &quot;&quot;&quot;&quot;生成排序规则的元组，先总分降序，总分相同德分降序前两项相同在按学号升序&quot;&quot;&quot;    return -(int(listB[1])+int(listB[2])),-int(listB[1]),int(listB[0])
def luQuSort(a,b,c,d): # 按规则进行排序    A = sorted(a,key=sortkey)    B = sorted(b,key=sortkey)    C = sorted(c,key=sortkey)    D = sorted(d,key=sortkey)    return A,B,C,D
def printLQ(luQuList):    print(&#39;最低分数线的考生人数:&#39;,len(luQuList))    for x in luQuList:        for i in x:            print(i,end=&#39; &#39;)        print()
def main():# 主函数    num,low,high,datalist = getdata()    a,b,c,d = fenlei(low,high,datalist)    a,b,c,d = luQuSort(a,b,c,d)    luqulist = a+b+c+d    printLQ(luqulist)
main()
 |
| 四、实验结果及分析和（或）源程序调试过程、实验总结与体会1、实验运行结果截图 ![](RackMultipart20200515-4-yg97se_html_ece48d13be178afe.png)2、程序编写过程中遇到的问题及解决思路、方法等调试运行时发现以下问题，list里的数据均为字符串无法比较大小， ![](RackMultipart20200515-4-yg97se_html_5127e886b6d7158.png)解决方法，在读取数据时将数据转化为整数型，如下 ![](RackMultipart20200515-4-yg97se_html_8a9b24d5417c4ec8.png)
总结和体会
1. 进行数据处理时需要注意数据的类型
2. 程序应该使用自上而下设计方法
 |

实验报告填写说明：

1、第一、二部分由老师提供；

2、第三部分填写源程序和算法，源程序要符合程序编写风格（缩进、注释等）；

3、第四部分主要填写程序结果（截图）、解决问题的方法、总结和体会等；

4、报告规范：包含报告页眉、报告的排版、内容是否填写，命名是否规范等。

5、源程序和实验报告命名：学号姓名序号.py 学号姓名序号.docx，例如学号20181234的张三同学, **实验命名为：**** 20181234 ****张三**** 3.py ****和**** 20181234 ****张三**** 3.docx**