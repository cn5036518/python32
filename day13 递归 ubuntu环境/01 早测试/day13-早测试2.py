#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/9/27 8:35

# ''''''
# '''

# 1# 什么是推导式,推导式完成1~100的列表
# 推导式:一行代码完成一组数据的输出,返回是列表
lst = [i for i in range(1,101)]
# print(lst)

# 2#[1,2,3,4]=[2,8,24,64]
lst = [i<<i for i in range(1,5)]
print(lst)  #[2, 8, 24, 64]

# 3#[1,2,3,4,5 ,6,67,7,81]只要偶数
lst1 = [1,2,3,4,5 ,6,67,7,81]
lst2 =[i for i in lst1 if i % 2 == 0]
print(lst2)  #[2, 4, 6]

# 4#lst1 =["a","b","c"]和lst2 = ["1","2","3"]按照索引把两个列表中的元素拼接在一起存新列表
lst1 =["a","b","c"]
lst2 = ["1","2","3"]
it = zip(lst1,lst2)
# print(list(it))  #[('a', '1'), ('b', '2'), ('c', '3')]

it = map(list,it)
print(list(it))  #[['a', '1'], ['b', '2'], ['c', '3']]
print('------------------------------4')

# 5#(1).{ 'x': 'A','Y': 'B','z': 'C'}把字典写成x-A，y=B，z=c的列表推导式
dic = { 'x': 'A','Y': 'B','z': 'C'}
lst = [k+'='+v for k,v in dic.items()]
print(lst) #['x=A', 'Y=B', 'z=C']

# 6#(2).把列表中所有字符变成小写[ "ADDD", "dddDD","DDaa", "sss"]
lst = [ "ADDD", "dddDD","DDaa", "sss"]
lst = [i.lower() for i in lst]
print(lst)  #['addd', 'ddddd', 'ddaa', 'sss']

# 7#(3）.x是0-5之间的偶数，y是o-5之间的奇数把x,y组成一起变成元组,放到列表当中
lst = [(i,j) for i in range(0,6,2) for j in range(1,6,2)]
print(lst)  #[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]

# 8#(4）.使用列表推导式制作所有99乘法表中的运算
lst = ['{:d}*{:d}={:2d} '.format(i,j,i*j) for i in range(1,10) for j in range(1,i+1)]
print(lst)
print('------------------------------8')

# 9#(5)#求M，H中矩阵和元素的乘积
M= [[1,2,3], [4,5,6],[7,8,9]]
N= [[2,2,2], [3,3,3],[4,4,4]]
#=→实现效果1 [2，4,6，12，15，18，28，32，36]
lst = []
for i in range(3):
	for j in range(3):  #内循环动得快,外循环动的慢
		lst.append(M[i][j] * N[i][j])
print(lst)  #[2, 4, 6, 12, 15, 18, 28, 32, 36]

lst = [M[i][j] * N[i][j] for i in range(3) for j in range(3)]
# lst = [M[i][j] * N[i][j] for j in range(3) for i in range(3)]
print(lst)  #[2, 4, 6, 12, 15, 18, 28, 32, 36]
print('------------------------------9-1')

#=→实现效果2[[2，4，6]，[12，15，18]，[28，32，36]]   #[[],[],[]]
lst = []
for i in range(3):
	lst2 = []
	for j in range(3):  #内循环动得快,外循环动的慢
		lst2.append(M[i][j] * N[i][j])
	lst.append(lst2)
print(lst)  #[[2, 4, 6], [12, 15, 18], [28, 32, 36]]

lst = [[M[i][j] * N[i][j] for j in range(3)] for i in range(3)]
# lst = [[M[i][j] * N[i][j] for i in range(3)] for j in range(3)]  #[[2, 12, 28], [4, 15, 32], [6, 18, 36]]
print(lst)  #[[2, 4, 6], [12, 15, 18], [28, 32, 36]]
print('------------------------------9-2')

# 11#""I"   集合推导式
# 案例:
# 满足年龄在18到21，存款大于等于5000小于等于5500的人，
# 开卡格式为:尊贵VIP卡老x(姓氏)，否则开卡格式为:大汉卡老x(姓氏)
# 把并卡的种类统计出来
lst = [
    {"name":"赵沈阳","age":18,"money":3000},
    {"name":"赵万里","age":19,"money":5200},
    {"name":"赵蜂拥","age":20,"money":100000},
    {"name":"赵世超","age":21,"money":1000},
    {"name":"王志国","age":18,"money":5500},
    {"name":"王永飞","age":99,"money":5500}
]

setvar = set()
for i in lst:
	if i['age'] >= 18 and i['age'] <=21 and i['money'] >= 5000 and i['money'] <= 5500:
		setvar.add('尊贵VIP卡老{}'.format(i['name'][0]))
	else:
		setvar.add('大汉卡老{}'.format(i['name'][0]))
print(setvar)  #{'尊贵VIP卡老赵', '尊贵VIP卡老王', '大汉卡老王', '大汉卡老赵'}

setvar = {'尊贵VIP卡老{}'.format(i['name'][0]) if i['age'] >= 18 and i['age'] <=21 and i['money'] >= 5000 and i['money'] <= 5500 else '大汉卡老{}'.format(i['name'][0])  for i in lst}
print(setvar)  #{'大汉卡老王', '大汉卡老赵', '尊贵VIP卡老赵', '尊贵VIP卡老王'}   #三元运算符
print('------------------------------11')

# 12#enumerate和zip如何使用
# zip
lst1 = [1,3]
lst2 = [2,4]
it = zip(lst1,lst2)
print(list(it))  #[(1, 2), (3, 4)]

it = zip(lst1,lst2)
it = map(list,it)
print(list(it))  #[[1, 2], [3, 4]]

it = zip(lst1,lst2)
print(*list(it))  # #(1, 2) (3, 4)
  #一个星* 在实参处,表示解包 获取列表中的元素
print('------------------------------12-1')

# enumerate
lst1 = [1,4,7]
it = enumerate(lst1,10)
print(list(it))
#[(10, 1), (11, 4), (12, 7)]

it = enumerate(lst1,10)  #推荐
print(dict(it))  #{10: 1, 11: 4, 12: 7}

dic = {k:v for k,v in enumerate(lst1)}
print(dic)  #{0: 1, 1: 4, 2: 7}
print('------------------------------12-2')

# 13#定义生成器的两种方式
# 方式1
# 函数中有yield 
def func():
	for i in range(3):
		yield i
gen = func()
print(list(gen))  #[0, 1, 2]
print('------------------------------13-1')

# 方式2 生成器表达式  元组推导式
gen = (i for i in range(2))
print(gen)  #<generator object <genexpr> at 0x7fcbb14c4410>
print(list(gen))  #[0, 1]
print('------------------------------13-2')

# 14#next和send有什么不同
# next只能向下取值
# send不仅可以取值,还可以发送值给上一个yield
# send第一次必须发送的是None

# 15#生成器写斐波那契数列
def fab(n):
	a,b = 0,1
	for i in range(n):
		yield b
		a,b = b,a+b
gen = fab(4)
print(list(gen))
#[1, 1, 2, 3]
print('------------------------------15')


# '''



















