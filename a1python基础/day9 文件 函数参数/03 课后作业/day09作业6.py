#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/23 22:38

# #6.定义函数:,接收一个参数(可迭代性数据),用_让元素相连成字符串,打印出来
# def func(args):
# 	strvar = '_'.join(args)
# 	print(strvar)   #a_b
# listvar = ['a','b']
# listvar = [1,2]
#
# func(listvar)


def func(args):
	li = []
	for i in args:
		li.append(str(i))

	strvar = '_'.join(li)
	print(strvar)   #a_b
# listvar = ['a','b']
listvar = [1,2]
func(listvar)


def func(*args):
	li = []
	for i in args:
		li.append(str(i))

	strvar = '_'.join(li)
	print(strvar)   #a_b
# listvar = ['a','b']
listvar = [1,2]
func(*listvar)

print('------------------------------------6')



















