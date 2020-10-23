''''''
'''

# 文件相关的函数有哪些?
# 如何按照行读取文件所有内容
# strvar = """
# 床前明月光
# 疑是地上霜
# 举头望明月
# 低头想家乡
# """
# 实现效果:写入文件,并且插入一句话:王文真帅呀 , 插在低头想家乡的前面
# 什么是函数
# 什么是驼峰命名法
# 参数的种类及顺序
# 任意个数值得累加和
# 拼接任意个数值变成字符串
# #写答案
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
# # 以上两个函数 打印结果
# #(一)
# f1(1, 2) # a =1 b=2 c=0 args=() kw={}
# f1(1, 2, c=3) # a=1,b=2,c=3,args=() kw={}
# f1(1, 2, 3, 'a', 'b') #a=1 b=2 c=3 args=(a,b) kw={}
# f1(1, 2, 3, 'a', 'b', x=99) # a=1 b=2 c=3 args=(a,b) kw={x:99}
# f2(1, 2, d=99, ext=None)#a=1 b=2 c=0 d=99 kw={ext:None}
# 
# #(二)
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# # f1(1,2,3,4,d=99,x=#)
# f1(*args, **kw) # a=1 b=2 c=3 args=(4,) kw={d:99,x:#}
# 
# 
# #(三)
# myargs = (1, 2, 3)
# mykw = {'d': 88, 'x': '#'}
# # f2(1,2,3,d=88,x=#)
# f2(*myargs, **mykw) # a=1,b=2,c=3 d=88 kw={x:#}
# 
# #(四)
# def f1(a, b, c=0, *args,d,**kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#     print(d)
# 
# f1(1,2,3, 'a', 'b',d=67, x=99,y=77) # a=1 b=2 c=3 args=(a,b)  kw={x:99,y:77}
# 									# d=67

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”

'''

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”
while True:
    content = input('请输入内容:')
    if ('粉嫩' or '铁锤') in content:  #优先级  in(成员>逻辑运算符)
        print('有敏感字')
    else:
        print('没有敏感字')
        break

# 任意个数值得累加和
def func(*args):
    total = 0
    for i in args:
        total += i
    print(total)

func(1,2,4)

# 拼接任意个数值变成字符串










