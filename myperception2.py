import myperception as mp
import copy

def load_name_data(filename):
    """
    filename:文件名
    该函数加载数据集；
    分别返回第一个名的集合和第二个名的集合；
    两个集合长度不一致时进行补齐操作；
    """
    f=open(filename,'r',encoding='utf-8')
    name_one_set=set()
    name_two_set=set()

    for name in f:
        if name[1] not in name_one_set:
            name_one_set.add(name[1])
        if name[2] not in name_two_set:
            name_two_set.add(name[2])

    onelen=len(name_one_set)
    twolen=len(name_two_set)
    if onelen < twolen:
        temp_set=name_two_set-name_one_set
        for i in temp_set:
            name_one_set.add(i)
            if len(name_one_set)==len(name_two_set):break
    elif onelen > twolen:
        temp_set=name_one_set-name_two_set
        for i in temp_set:
            name_two_set.add(i)
            if len(name_one_set)==len(name_two_set):break
    f.close()

    return name_one_set,name_two_set

def train_data(fname:set,sname:set,filename:str):
    """
    fname:第一个名字集合
    sname:第二个名字集合
    filename:文件名
    该函数构建感知机并进行训练；
    由于样本的两个特征都是向量，所以定义两个权重w和v分别进行内积
    返回w，v，b三个参数
    """
    f=open(filename,'r',encoding='utf-8')
    w={word:0 for word in fname}
    v={word:0 for word in sname}
    b=0

    for name in f:
        label=1 if name[-2]=='男' else -1
        sum_1=w[name[1]] if name[1] in fname else 0
        sum_2=v[name[2]] if name[2] in sname else 0

        if mp.sign(sum_1+sum_2+b) != label:
            if name[1] in fname:
                w[name[1]]+=label
            if name[2] in sname:
                v[name[2]]+=label
            b+=label
    f.close()

    return w,v,b

def iter_train(w:dict,v:dict,b:int,fname,sname,filename):
    '''
    w:第一个特征权重
    v:第二个特征权重
    b:偏差
    fname:第一个名字集合
    sname:第二个名字集合
    filename:文件名
    该函数用于迭代训练感知机，通过传入初建感知机的三个参数进行训练，不断更新参数；
    '''
    f=open(filename,'r',encoding='utf-8')

    for name in f:
        label=1 if name[-2]=='男' else -1
        sum_1=w[name[1]] if name[1] in fname else 0
        sum_2=v[name[2]] if name[2] in sname else 0

        if mp.sign(sum_1+sum_2+b) != label:
            if name[1] in fname:
                w[name[1]]+=label
            if name[2] in sname:
                v[name[2]]+=label
            b+=label
    f.close()

    return w,v,b

def test_data(w:dict,v:dict,b:int,filename):
    """
    w:第一个特征权重
    v:第二个特征权重
    b:偏差
    filename:文件名
    该函数进行测试；
    返回一个由预测值和真实值为一组的列表
    """
    f=open(filename,'r',encoding='utf-8')
    result=[]

    for name in f:
        label=1 if name[-2]=='男' else -1

        sum_1=w[name[1]] if w.get(name[1],0) else 0
        sum_2=v[name[2]] if v.get(name[2],0) else 0

        result.append((mp.sign(sum_1+sum_2+b),label))
    f.close()

    return result

def main():
    '''
    该程序改进了第一代编写的以列表为主体的感知机，极大地缩短了运行时间；
    一百次的迭代可以在三十秒之内完成；
    '''
    first_name,second_name=load_name_data(mp.FILENAME_TRAIN)
    w,v,b=train_data(first_name,second_name,mp.FILENAME_TRAIN)
    w_o=copy.deepcopy(w)
    v_o=copy.deepcopy(v)
    b_o=b
    for i in range(100):
        w,v,b=iter_train(w,v,b,first_name,second_name,mp.FILENAME_TRAIN)
        if w==w_o and v==v_o and b==b_o:break
        w_o = copy.deepcopy(w)
        v_o = copy.deepcopy(v)
        b_o = b
    result=test_data(w,v,b,mp.FILENAME_TEST)
    mp.evaluate(result)
    print(*result[:101],sep='\n')

if __name__=='__main__':
    main()