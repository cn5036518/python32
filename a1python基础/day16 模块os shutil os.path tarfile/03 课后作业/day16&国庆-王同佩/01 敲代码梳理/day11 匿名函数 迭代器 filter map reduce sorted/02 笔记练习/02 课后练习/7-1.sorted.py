# ### sorted
# sorted(iterable,key=函数,reverse=False)
# 功能:
	# 排序数据
# 参数:
	# iterable: 可迭代对象(容器类型数据  range对象 迭代器)
	# key:	指定函数的名字(自定义 内置)  函数名字后面没有()
	# reverse:是否倒序
# 返回值:
	# 列表

tup = (-90,89,78,3)
# 1 从小到大
res = sorted(tup)
print(res,type(res))  #[-90, 3, 78, 89] <class 'list'>

# 2 从大到小
res = sorted(tup,reverse=True)
print(res,type(res))  #[89, 78, 3, -90] <class 'list'>

# 3 按照绝对值进行排序
tup = (-90,-100,1,2)
res = sorted(tup,key= abs)
print(res)  #[1, 2, -90, -100]

# 4 按照自定义函数(%10的余数)进行排序
tup = (19,23,42,87)

def func(n):
	return n % 10
	
lst = sorted(tup,key=func)
print(lst)  #[42, 23, 87, 19]

# 5 任意的容器类型数据都可以通过sorted排序
container = "abc"
container = [1,2,3]
container = (1,2,3)
container = {"你好","王文","你真帅"}
container = {"caixukun","xiaozhan","zhaoshenyang","wangyibo"}
container = {"ww":"英俊帅气","zxy":"猥琐抠脚","zwl":"斯文败类"} #字典用键排序
print(sorted(container))  #['ww', 'zwl', 'zxy']

# 总结:
# sorted(排序推荐使用sorted)
	# 1 可以排序所有的容器类型数据
	# 2 返回一个新的列表(原来的列表没有变化)
	
# sort
	# 1 只能排序列表
	# 2 基于原来的列表进行排序(原来的列表有变化)

































