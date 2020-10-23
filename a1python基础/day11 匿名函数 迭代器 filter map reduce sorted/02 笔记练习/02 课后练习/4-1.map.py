# ### 高阶函数: 能够把函数当做参数传递的就是高阶函数
#  map filter reduce sorted

#map
# map(func,Iterable)
# 功能:
	# 处理数据
# 参数:
	# func:函数(内置函数,自定义函数)
	# Iterable:可迭代的对象(容器类型数据,range对象,迭代器)
# 返回值:
	# 迭代器

# 1 把列表中的元素都变成整型
lst = ['1','2','3','4']

# 普通方法
lst_new = []
for i in lst:
	lst_new.append(int(i))
print(lst_new)  #[1, 2]
print('--------------------1-1')

# map改写
from collections import Iterator

lst = ['1','2','3','4']
it = map(int,lst)  #这里的int是内置函数
print(isinstance(it,Iterator))  #True
# print(list(it))  #[1, 2]  #这里如果已经调用了迭代器,后面就无法再
# 从迭代器中取值了,需要重新生成迭代器
print('--------------------1-2')

# 代码解析:
# 第一次调用迭代器
	# 先把列表中的第一个元素'1'拿出来放到int中做强转,变成整型1返回出来
# 第二次调用迭代器
	# 先把列表中的第二个元素'2'拿出来放到int中做强转,变成整型2返回出来
# 第三次调用迭代器
	# 先把列表中的第三个元素'3'拿出来放到int中做强转,变成整型3返回出来
# 第四次调用迭代器
	# 先把列表中的第四个元素'4'拿出来放到int中做强转,变成整型4返回出来

# 1.调用迭代器 next
print(next(it)) #1
print(next(it)) #2
# print(next(it))  #StopIteration  error
print('--------------------1-11')

# 2.调用迭代器 for
it = map(int,lst)  #第二次生成迭代器
for i in range(3):
	print(i)
print('--------------------1-12')

# 3.调用迭代器 for + next
it = map(int,lst)
for i in range(3):
	print(next(it))
print('--------------------1-13')

# 4.调用迭代器 强转成列表  ---推荐
it = map(int,lst)
print(list(it))
print('--------------------1-14')

# 2 [1,2,3,4] ==>[2,8,24,64]

# 1 * 2 ^1  2
# 2 * 2 ^2 	8
# 3 * 2 ^3	24
# 4 * 2 ^4	64

# 左移1,2,3,4位   规律
# 1 << 1
# 2 << 2
# 3 << 3
# 4 << 4

# 普通方法
lst = [1,2,3,4]
lst_new = []
for i in lst:
	lst_new.append(i<<i)
print(lst_new)  #[2, 8, 24, 64]
print('--------------------2-1')

# map改写
def func(n):
	return n << n
	
it = map(func,lst)  #参数1是函数名字
print(list(it))  #调用迭代器   [2, 8, 24, 64]
print('--------------------2-2')	

# map+lambda
it = map(lambda n: n<<n,lst)
print(list(it))  #[2, 8, 24, 64]
print('--------------------2-3')
#注意点:func的形参和返回值必须写

# 3 给你一个列表['a','b','c']  要求输出[97,98,99]
# 已知字符,要求输出字符对应的ascii

# 方法1 普通方法

# 思路:
# 1 先完成字典的键值对翻转
# 2 然后根据字符来取值ascii 
#    即已知:['a','b','c'] ,要求输出[97,98,99]

# 字典的键值翻转操作
dic = {97:'a',98:'b',99:'c'}
# 如何把上述字典的键值对调   
# 输出 dic = {'a':97,'b':98,'c':99}
dic_new = {}
for k,v in dic.items():
	# print(k,v)
	dic_new[v] = k
print(dic_new)  #{'a': 97, 'b': 98, 'c': 99}

# 已知:['a','b','c'] ,要求输出[97,98,99]
lst = ['a','b','c']
lst_new = []
for i in lst:
	v = dic_new[i]   #这里的i两边是中括号[],不是小括号()
	lst_new.append(v)
print(lst_new)  #[97, 98, 99]
print('--------------------3-1')

# 方法2 map改写
lst = ['a','b','c']
# func 实现字典的翻转,通过给予a,b,c三个键,得到对应的ascii码,
# 通过list强转得到列表
def func(n):
	dic = {97:'a',98:'b',99:'c'}  #已知条件
	dic_new = {}
	for k,v in dic.items():
		dic_new[v] = k
	# print(dic_new)  ##{'a': 97, 'b': 98, 'c': 99}
	# 完成字典的翻转
	# 给参数'a',return 97
	# 给参数'b',return 98
	# 给参数'c',return 98
	return dic_new[n]

it = map(func,lst)
print(list(it))  #[97, 98, 99]
print('--------------------3-2')






















































