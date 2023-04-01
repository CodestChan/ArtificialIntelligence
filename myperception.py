
#训练集和测试集文件名
FILENAME_TRAIN=r'train.csv'
FILENAME_TEST=r'test.csv'

def load_data(filename:str):
    """
    filename:文件名
    该函数加载数据集；
    分别返回第一个名的列表和第二个名的列表；
    两个列表长度不一致时进行补齐操作；
    """
    f=open(filename,'r',encoding='utf-8')
    name_list_one=[]
    name_set_one=set()
    name_list_two=[]
    name_set_two=set()

    for name in f:
        if name[1] not in name_set_one:
            name_set_one.add(name[1])
            name_list_one.append(name[1])
        if name[2] not in name_set_two:
            name_set_two.add(name[2])
            name_list_two.append(name[2])

    name_list_one.sort()
    name_list_two.sort()

    if len(name_list_one) < len(name_list_two):
        for i in range(len(name_list_two)-len(name_list_one)):
            name_list_one+=['_']
    else:
        for i in range(len(name_list_one)-len(name_list_two)):
            name_list_two+=['_']
    f.close()

    return name_list_one,name_list_two

def oindex(lst:list,ele):
    """
    lst:需要索引的列表
    ele:需要索引的元素
    由于内置函数index()在列表内无索引元素时会报错；
    所以重新编写一个索引函数，在找不到元素时返回-1；
    """
    try:
        indx=lst.index(ele)
        return indx
    except ValueError:
        return -1

def build_datalist(fname:list,sname:list,filename:str):
    """
    fname:第一个名字列表
    sname:第二个名字列表
    filename:文件名
    该函数创建训练数据集，返回一个列表；
    列表元素为一个三元元组(p1,p2,y)：p1为第一个名的向量，p2为第二个名的向量，y为该样本的标签
    """
    f=open(filename,'r',encoding='utf-8')

    length=max(len(fname),len(sname))
    data_list=[]

    #由于运行时间过长，这里直截取前10000个数据
    i=0
    for name in f:
        i+=1
        first=[0 for i in range(length)]
        second=[0 for i in range(length)]

        if oindex(fname,name[1]) != -1:
            first[fname.index(name[1])]=1
        if oindex(sname,name[2]) != -1:
            second[sname.index(name[2])]=1

        data_list.append((first,second,1 if name[-2]=='男' else -1))
        if i==10000:break
    f.close()

    return data_list,length

def sign(n):
    return 1 if n>0 else -1

def train(datalist:list,length:int):
    """
    datalist:需要训练的数据
    length:特征向量的长度
    该函数构建感知机并进行训练；
    由于样本的两个特征都是向量，所以定义两个权重w和v分别进行内积
    返回w，v，b三个参数
    """
    w=[0 for i in range(length)]
    v=[0 for i in range(length)]
    b=0

    for data in datalist:
        sum_1=0
        sum_2=0

        for i in range(length):
            sum_1+=w[i]*data[0][i]
            sum_2+=v[i]*data[1][i]

        if sign(sum_1+sum_2+b) != data[-1]:
            for j in range(length):
                w[j]+=data[-1]*data[0][j]
                v[j]+=data[-1]*data[1][j]
            b+=data[-1]

    return w,v,b

def test(database,long,w,v,b):
    """
    database:需要测试的数据
    long:特征向量长度
    w:第一个特征权重
    v:第二个特征权重
    b:偏差
    该函数进行测试；
    返回一个由预测值和真实值为一组的列表
    """
    result=[]

    for data in database:
        sum_1=0
        sum_2=0
        for i in range(long):
            sum_1+=w[i]*data[0][i]
            sum_2+=v[i]*data[1][i]
        result.append(sign(sum_1+sum_2+b))

    gold=[data[-1] for data in database]
    zipresult=list(zip(result,gold))

    return zipresult

def evaluate(result:list):
    tp,fp,tn,fn=0,0,0,0

    for f,s in result:
        if f==1 and s==1:
            tp+=1
        elif f==1 and s==-1:
            fp+=1
        elif f==-1 and s==-1:
            tn+=1
        elif f==-1 and s==1:
            fn+=1

    P=tp/(tp+fp)
    R=tp/(tp+fn)
    F1=2*P*R/(P+R)

    print('P:{:.2f} R:{:.2f} F1:{:.2f}'.format(P,R,F1))

def main():
    """
    运行主函数；
    我只迭代了一次，事实上可以设置循环进行多次迭代；
    """
    name1,name2=load_data(FILENAME_TRAIN)
    datatrain,leng=build_datalist(fname=name1,sname=name2,filename=FILENAME_TRAIN)
    w,v,b=train(datatrain,leng)
    datatest,long=build_datalist(fname=name1,sname=name2,filename=FILENAME_TEST)
    result=test(datatest,long,w,v,b)
    evaluate(result)
    print(*result,sep='\n')

if __name__ == '__main__':
    main()


