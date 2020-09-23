#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 20:54


# #8.输入列表li= [11,22,33,44,55,66,77,88,99,90]
# 	# 将大于 66 的值保存至字典的k1键中，
# 	# 将小于 66 的值保存至字典的k2键中。
# 	# 打印字典 {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}

li= [11,22,33,44,55,66,77,88,99,90]

dic = {'k1':[],'k2':[]}
for i in li:
	if i > 66:
		dic['k1'].append(i)
	elif i < 66:
		dic['k2'].append(i)
print(dic)  #{'k1': [77, 88, 99, 90], 'k2': [11, 22, 33, 44, 55]}
print('------------------------------------8')

# #7.输入字符串 "k:1|k1:2|k2:3|k3:4" 处理成字典 {'k':1,'k1':2....} 打印出来
strvar = "k:1|k1:2|k2:3|k3:4"
listvar = strvar.split('|')
print(listvar)  #['k:1', 'k1:2', 'k2:3', 'k3:4']

dic = {}
for i in listvar:
	a,b = i.split(':')
	dic[a] = b
print(dic)  #{'k': '1', 'k1': '2', 'k2': '3', 'k3': '4'}

print('------------------------------------7')

# #6.定义函数:,接收一个参数(可迭代性数据),用_让元素相连成字符串,打印出来
def func(args):
	strvar = '_'.join(args)
	print(strvar)   #a_b
listvar = ['a','b']
listvar = [1,2]

func(listvar)


def func(args):
	li = []
	for i in args:
		li.append(str(i))

	strvar = '_'.join(li)
	print(strvar)   #a_b
# listvar = ['a','b']
listvar = [1,2]

func(listvar)
print('------------------------------------6')

# #5.定义函数:参数为容器类型数据,打印所有奇数位索引对应的元素
def func(args):
	for i in range(len(args)):
		if i % 2 ==1:
			print(args[i])

listvar = ['a','b','c','d']

func(listvar)
print('------------------------------------5')

# #4.定义函数:打印用户传入的容器类型数据长度
def func(args):
	print(len(args))

listvar = ['a','b','c','d']

func(listvar)

print('------------------------------------4')



















