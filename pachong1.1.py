import requests
from bs4 import BeautifulSoup
import xlwt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family']='SimHei'

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "utf-8"
        return r.text
    except:
        return ""

def dataAnalyse(demo,ilt):
    soup=BeautifulSoup(demo,"html.parser")
    a=soup.find_all("div",attrs={"class":"bookinfo"})
    for i in range(len(a)):
        ila,ilb=[],[]
        for child in a[i].descendants:
            if child is None:
                continue
            else:
                ila.append(child.string)
        while None in ila:
            ila.remove(None)
        for j in ila:
            if ("连载中" or "已完结") in j:
                ilb.append(j.strip(2*("\r\n"+" "*27+"\t")))
            if "总字数" in j :
                ilb.append(j.strip("\r\n"+" "*28))
            if ("\n" or "\r" or "\t") not in j:
                ilb.append(j)
        ilt.append(ilb)

def dataCorborate(ilt,yeshu):
    nilt=[]
    for book in ilt[yeshu:]:
        bookinfo=[]
        for info in range(0,len(book),2):
            if '字数' in book[info]:
                book[info]=book[info][4:]
            bookinfo.append(book[info])
        nilt.append(bookinfo)
    return nilt

def dataSpilt(ilt,gengxing,zishu,ticai=[]):
    leixing=["奇幻玄幻","武侠仙侠","历史军事","都市娱乐","科幻游戏","悬疑灵异","竞技同人","评论文集","二次元"]
    for book in ilt:
        try:
            if len(ticai) != 0:
                ticai[leixing.index(book[2])]+=1
        except:
            ticai[3]+=1
        if "连载中" in book:
            gengxing[0]+=1
        if "连载中" not in book:
            zishu.append(book[3])
        else:zishu.append(book[4])
    gengxing[1]=len(ilt)-gengxing[0]

def characterAnalysis(ticai):
    plt.figure(figsize=(12,12),dpi=80)
    labels='奇幻玄幻','武侠仙侠','历史军事','都市娱乐','科幻游戏','悬疑灵异','竞技同人','评论文集','二次元'
    sizes=[]
    for i in ticai:
        sizes.append(i/sum(ticai))
    sizes2=[]
    for i in range(len(sizes)):
        sizes2.append(sizes[i]*100)
    plt.subplot(121)
    explode=(0,0,0,0,0,0.1,0.2,0.3,0.4)
    plt.pie(sizes2,explode=explode,labels=labels,autopct='%1.2f%%',shadow=False,startangle=90)
    plt.legend(list(labels))
    plt.subplot(122)
    n=9
    index=np.arange(n)
    width=0.5
    p2=plt.bar(index,tuple(ticai),width,label='本数',color='#87CEFA')
    plt.xlabel('小说类型')
    plt.ylabel('各类型小说总数占比')
    plt.title('各类型小说数量对比')
    plt.xticks(index,labels=labels,rotation=-15)
    plt.yticks(np.arange(0,70,10))
    plt.legend(loc='upper right')
    plt.show()

def wordNumber(zishu):
    tongji=[0,0,0,0,0,0]
    for i in range(len(zishu)):
        if eval(zishu[i]) < 5*10**6:tongji[0]+=1
        elif 5*10**6 <= eval(zishu[i]) < 7*10**6:tongji[1]+=1
        elif 7*10**6 <= eval(zishu[i]) < 9*10**6:tongji[2]+=1
        elif 9*10**6 <= eval(zishu[i]) < 11*10**6:tongji[3]+=1
        elif 11*10**6 <= eval(zishu[i]) < 13*10**6:tongji[4]+=1
        else:tongji[5]+=1
    return tongji

def wordNumberfigure(tongji):
    plt.figure(figsize=(10,10),dpi=80)
    labels='<5','5~7','7~9','9~11','11~13','>=13'
    n=6
    index=np.arange(n)
    width=0.5
    p2=plt.bar(index,tuple(tongji),width,label='本数',color='#87CEFA')
    plt.xlabel('各区间字数*1000000')
    plt.ylabel('落在各区间小说数量')
    plt.title('字数统计')
    plt.xticks(index,labels=labels,rotation=-15)
    plt.yticks(np.arange(0,100,10))
    plt.legend(loc='upper right')
    plt.show()

def statusFigure(gengxing):
    #plt.figure(figsize=(9,9),dpi=80)
    labels="连载中","已完结"
    sizes=[]
    for i in gengxing:
        sizes.append(i/sum(gengxing))
    explode=(0,0)
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.2f%%',shadow=False,startangle=90)
    plt.title("当前爬取小说更新状态")
    plt.show()

def dataDeepspilt(ilt):
    l1,l2,l3,l4,l5,l6=[],[],[],[],[],[]
    leixing=["奇幻玄幻","武侠仙侠","历史军事","都市娱乐","科幻游戏","悬疑灵异"]
    for book in ilt:
        if leixing[0] in book:l1.append(book)
        elif leixing[1] in book:l2.append(book)
        elif leixing[2] in book:l3.append(book)
        elif leixing[3] in book:l4.append(book)
        elif leixing[4] in book:l5.append(book)
        else : l6.append(book)
    return l1,l2,l3,l4,l5,l6

#def charDataspilt(li):

def characterStatusfigure(l1,l2,l3,l4,l5,l6):
    plt.figure(figsize=(12,12),dpi=80)
    li=[l1,l2,l3,l4,l5,l6]
    leixing=["奇幻玄幻","武侠仙侠","历史军事","都市娱乐","科幻游戏","悬疑灵异"]
    labels='连载中',"已完结"
    for i in range(1,7):
        plt.subplot(2,3,i)
        Igengxing,Izishu=[0,0],[]
        dataSpilt(li[i-1],Igengxing,Izishu)
        sizes=[]
        for j in Igengxing:
            sizes.append(j/sum(Igengxing))
        explode=(0,0)
        plt.pie(sizes,explode=explode,labels=labels,autopct='%1.2f%%',shadow=False,startangle=90)
        plt.title(leixing[i-1])
    plt.show()

def statusAndnumber(ilt):
    lianzai,yiwanjie=[],[]
    for book in ilt:
        if "连载中" in book:lianzai.append(book[4])
        else: yiwanjie.append(book[3])
    Wlianzai,Wyiwanjie=[],[]
    Wlianzai=wordNumber(lianzai)
    Wyiwanjie=wordNumber(yiwanjie)
    tongji=[Wlianzai,Wyiwanjie]
    labels='<5','5~7','7~9','9~11','11~13','>=13'
    lab=["连载中","已完结"]
    n=6
    index=np.arange(n)
    width=0.5    
    for i in range(1,3):
        plt.subplot(1,2,i)
        p2=plt.bar(index,tuple(tongji[i-1]),width,label='本数',color='#87CEFA')
        plt.xlabel('各区间字数*1000000')
        plt.ylabel('落在各区间小说数量')
        plt.title(lab[i-1]+"小说字数")
        plt.xticks(index,labels=labels)
        plt.yticks(np.arange(0,80,10))
        plt.legend(loc='upper right')  
    plt.show()     
#http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html
#http://www.biquw.com/xs/quanbu-default-0-0-0-0-2-0-1.html
ilt=[]
ticai=[0,0,0,0,0,0,0,0,0]
gengxing=[0,0]
zishu=[]
for i in range(1,2):
    try:
        status_url="http://book.zongheng.com/store/c0/c0/b0/u5/p"+str(i)+"/v9/s9/t0/u0/i1/ALL.html" 
        demo1=getHTMLText(status_url)
        dataAnalyse(demo1,ilt)
        ilt[(i-1)*50:]=dataCorborate(ilt,(i-1)*50)
    except:
        continue
dataSpilt(ilt,gengxing,zishu,ticai=ticai)
l1,l2,l3,l4,l5,l6=dataDeepspilt(ilt)
characterStatusfigure(l1,l2,l3,l4,l5,l6)
statusAndnumber(ilt)
statusFigure(gengxing)
wordNumberfigure(wordNumber(zishu))
characterAnalysis(ticai)
#print(len(ilt))
#print(ilt[53])
#print(ticai)
#print(gengxing)
#print(zishu)
#print(ilt[0])
#print(ilt[50])
'''
ilt=[]
url="http://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s9/t0/u0/i1/ALL.html"
demo=getHTMLText(url)
dataAnalyse(demo,ilt)
print(ilt[:10])
'''
'''

wookexcel=xlwt.Workbook(encoding="ascii")
wooksheet=wookexcel.add_sheet("Novel Database")
if len(ilt) != 500:
    print(len(ilt))
else:
    Ilabel=["序号","书名","作者","类型","字数"]
    for i in range(len(Ilabel)):
        wooksheet.write(0,i,Ilabel[i])
    for i in range(1,501):
        wooksheet.write(i,0,i)
    for i in range(1,501):
        for j in range(1,5):
            if j==4 :
                wooksheet.write(i,j,zishu[i-1])
            else:
                wooksheet.write(i,j,ilt[i-1][j-1])
    wookexcel.save("Term Design.xls")
'''

#http://book.zongheng.com/store/c0/c0/b0/u5/p1/v9/s9/t0/u0/i1/ALL.html

'''
    url="http://book.zongheng.com/store/c0/c0/b0/u5/p1/v9/s9/t0/u0/i1/ALL.html"
    demo=getHTMLText(url)
    ilt=[]
    dataAnalyse(demo,ilt)
    ilt=dataCorborate(ilt)
    ticai,gengxing,cishu=[],[],[]
    ticai,gengxing,cishu=dataSpilt(ilt)
    print(ilt[3])
    print(ticai)
    print(gengxing)
    print(cishu)
    '''
'''
r=requests.get("http://book.zongheng.com/store/c0/c0/b0/u5/p1/v9/s9/t0/u0/i1/ALL.html")
r.encoding="utf-8"
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
a=soup.find_all("div",attrs={"class":"bookinfo"})
ilt=[]
for child in a[3].descendants:
    if child is None:
        continue
    else:
        ilt.append(child.string)
        #print(child.name)
        #print(child.string)
#print(a[0].contents)
ilr=[]
count=0
while None in ilt:
    ilt.remove(None)
for i in ilt:
    if ("连载中" or "已完结") in i :
        ilr.append(i.strip(2*("\r\n"+" "*27+"\t")))
    if "总字数" in i :
        ilr.append(i.strip("\r\n"+" "*28))
        #print(count)
    if ("\n" or "\r" or "\t") not in i:
        ilr.append(i)
print(ilr)
'''