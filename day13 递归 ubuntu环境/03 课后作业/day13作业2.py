# (选做)
# 1.可滑动的序列 自定义一个函数 根据参数n的值 , 变成对应个元素的容器 （zip）
# """
# listvar = [1,2,3,4,5,6,7,8,9]
# n = 2
# listvar = [[1,2],[3,4],[5,6],[7,8]]
# n = 3
# listvar = [[1,2,3],[4,5,6],[7,8,9]]
# n = 4
# listvar = [[1,2,3,4],[5,6,7,8]]
# """

# 找规律
# n=2
# lst1 = [1,3,5,7,9]  listvar[0::2]
# lst2 = [2,4,6,8]    listvar[1::2]

# n=3
# lst1 = [1,4,7]    listvar[0::3]
# lst2 = [2,5,8]    listvar[1::3]
# lst3 = [3,6,9]	  listvar[2::3]

# n=4
# lst1 = [1,5,9]		listvar[0::4]
# lst2 = [2,6]		listvar[1::4]
# lst3 = [3,7]		listvar[2::4]
# lst4 = [4,8]		listvar[3::4]

listvar = [1,2,3,4,5,6,7,8,9]
n = 4
lst = [listvar[i::n] for i in range(n)]  #规律 关键点1
print(lst)  #[[1, 3, 5, 7, 9], [2, 4, 6, 8]]
# #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# [[1, 5, 9], [2, 6], [3, 7], [4, 8]]

it = zip(*lst)  # 一个星* 在实参处,是解包  知识点
# print(list(it))  #[(1, 2, 3, 4), (5, 6, 7, 8)]

#将列表的元素-元组变成list  map
# it = map(list,list(it))
it = map(list,it)  #参数2可以直接用迭代器
print(list(it))  #[[1, 2, 3, 4], [5, 6, 7, 8]]

# 整合成函数
def func(n):
	return list(map(list,zip(*[listvar[i::n] for i in range(n)])))
print(func(3))  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 转成匿名函数
func = lambda n : list(map(list,zip(*[listvar[i::n] for i in range(n)])))
print(func(2))  #[[1, 2], [3, 4], [5, 6], [7, 8]]
print('----------------------------1')


# 2.青蛙跳台阶  (递归实现)
# '''
# 一只青蛙要跳上n层高的台阶
# 一次能跳一级,也可以跳两级
# 请问这只青蛙有多少种跳上这个n层高台阶的方法?
def fog(n):
	if n in (1,2):  #递归的结束条件
		return n
	else:
		return fog(n-1) + fog(n-2)
print(fog(4)) #5
print('----------------------------2')


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)





# 4.斐波那契数列用尾递归实现
# 普通实现
def fab(n):
	a,b = 0,1
	i = 0
	while i<n:
		print(b)
		a,b = b,a+b
		i += 1
fab(4)

# 尾递归










































