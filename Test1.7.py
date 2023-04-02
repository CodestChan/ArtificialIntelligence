from random import *
from math import *
from numpy import cumsum
from time import *

def seedi(NP,L):                   
    zhong=[]
    for i in range(NP):
        c=''
        for j in range(L):
            c+=str(randint(0,1))
        zhong.append(c)
    return zhong

func=lambda x:x+10*sin(5*x)+7*cos(4*x)

def together(Fit,minFit,maxFit):
    for i in range(50):
        Fit[i]=(Fit[i]-minFit)/(maxFit-minFit)

def dianchu(Fit,sum):
    fit=[]
    for i in range(50):
        fit.append(Fit[i]/sum)
    return fit

def randf():
    sd=[]
    for i in range(50):
        sd.append(random())
    return sd

def shu():
    fn=[]
    for i in range(50):
        fn.append('')
    return fn

def ranseti():
    t=''
    for i in range(20):
        t+=str(randint(0,1))
    return t

def repl(a,b,c):
    a=a[0:b]+c+a[b+1:]
    return a

def jingqing(l1,l2):
    a=0
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            a+=1
        else:continue
    b=a/len(l1)
    return b

NP,L,Pc,Pm,G,Xs,Xx=50,20,0.8,0.1,100,10,0  #种群数量，染色体长度，交叉率，变异率，遗传代数，上限，下限
t1,t2=0,0
while t2<100:
    t=perf_counter()
    nf=shu()
    f=seedi(NP,L)                 #随机获得初始种群，50个由01构成的长度为20的字符串
    for k in range(G):            #开始迭代
        x,Fit=[],[]
        for i in range(NP):       #将二进制字符串解码为定义域范围内的十进制
            U=f[i]
            m=0
            for j in range(L):
                m=eval(U[j])*2**j+m
            a=Xx+m*(Xs-Xx)/(2**L-1)
            x.append(a)
            Fit.append(func(a))
        maxFit=max(Fit)           #适应度函数最大值
        minFit=min(Fit)           #最小值
        rr=Fit.index(maxFit)      #最大值在种群当中的位置
        fBest=f[rr]               #记录当代最优个体
        xBest=x[rr]
        together(Fit,minFit,maxFit)  #归一化适应度值 对Fit里的每一个元素执行(Fit[i]-minFit)/(maxFit-minFit)
        
        #基于轮盘赌的复制操作
        sum_Fit=sum(Fit)
        fitvalue=dianchu(Fit,sum_Fit) #对Fit中的每一个值进行除操作：Fit[i]/sum_Fit
        fitvalue=cumsum(fitvalue)     #累加求和，例如：[1,2,3],cumsum之后，变为[1,3,6]
        ms=sorted(randf())            #随机生成50个由小到大的大小介于0到1之间的小数的列表
        fiti,newi=0,0
        while newi<NP:
            if ms[newi]<fitvalue[fiti]:
                nf[newi]=f[fiti]
                newi+=1
            else:fiti+=1
        
        #基于概率的交叉操作
        for i in range(0,NP,2):
            if random()<Pc:
                q=ranseti()
                for j in range(L):
                    if q[j]=='1':
                        temp=nf[i+1][j]
                        nf[i+1]=repl(nf[i+1],j,nf[i][j]) #repl(a,b,c)将a字符串中的j位置的字符替换为字符c
                        nf[i]=repl(nf[i],j,temp)
        
        #基于概率的变异操作
        i=0
        while i<round(NP*Pm):
            h=randint(0,NP-1)    #随机选择一个种群中的染色体
            for j in range(0,round(L*Pm)):
                g=randint(0,L-1) #随机选取需要变异的基因数
                if nf[h][g]=='1':nf[h]=repl(nf[h],g,'0')
                else:nf[h]=repl(nf[h],g,'1')
            i+=1
        f=nf.copy()  #更新种群
        f[0]=fBest   #将当代最优个体放在下一代中
    t=perf_counter()-t
    t1+=t
    t2+=1
print(t1/100)
print(xBest)
print(maxFit)


