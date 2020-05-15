# 实验3 德才论
def getdata():
    """从文件中读取数据，读取考生数量，录取录取最低分数线，
      为优先录取线和考生原始数据（含学号，德分数，才分数）"""
    listtemp=[]
    fo = open(r"E:\Demo\实验\data.txt","r")
    n = fo.readline().split()
    num,low,high = int(n[0]),int(n[1]),int(n[2])
    for i in range(num):
        listtemp.append(list(map(int,fo.readline().split()))) #将数据转化为int型
    return num,low,high,listtemp

def fenlei(low,high,listA):
    'a“圣人”，b“君子”，c“愚人”，d“小人”'
    a=[];  b=[];  c=[];  d=[]
    for stu in listA:
        if stu[1]>=high and stu[2]>=high:
            a.append(stu) # 才德全尽
        elif stu[1] >= high and stu[2]<high:
            b.append(stu) # 德胜才
        elif stu[1]>stu[2] and stu[2]>=low:
            c.append(stu) # “才德兼亡”但尚有“德胜才”
        elif stu[1]>=low and stu[2]>=low:
            d.append(stu) # 才德兼亡 但达到录取线
    return a,b,c,d

def sortkey(listB):
    """"生成排序规则的元组，先总分降序，总分相同德分降序前两项相同在按学号升序"""
    return -(int(listB[1])+int(listB[2])),-int(listB[1]),int(listB[0])

def luQuSort(a,b,c,d): # 按规则进行排序
    A = sorted(a,key=sortkey)
    B = sorted(b,key=sortkey)
    C = sorted(c,key=sortkey)
    D = sorted(d,key=sortkey)
    return A,B,C,D

def printLQ(luQuList):
    print('最低分数线的考生人数:',len(luQuList))
    for x in luQuList:
        for i in x:
            print(i,end=' ')
        print()

def main(): # 主函数
    num,low,high,datalist = getdata()
    a,b,c,d = fenlei(low,high,datalist)
    a,b,c,d = luQuSort(a,b,c,d)
    luqulist = a+b+c+d
    printLQ(luqulist)

main()
