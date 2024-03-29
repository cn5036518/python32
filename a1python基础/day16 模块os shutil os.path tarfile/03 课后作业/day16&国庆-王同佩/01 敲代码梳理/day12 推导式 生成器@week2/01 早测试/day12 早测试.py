#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/25 9:03

''''''
'''

# 1.什么是匿名函数,语法?
1 没有函数名字的函数就是匿名函数
2 写法
lambda 参数:返回值 条件

无参数
lambad  : '文哥是个帅哥'

参数+返回值
lambda  x : id(x)

参数+返回值+条件(三元运算符)
lambda  x : '偶数' if x % 2 == 0   #错误的写法  必须是三元运算,这里缺少else  会出现语法错误
lambda  x : '偶数' if x % 2 == 0 else '奇数'

# 2.配合三运运算符写一个过滤奇数的匿名函数
func = lambda x : True if x % 2 == 1 else False

# 3.locals和globals什么区别
locals 返回当前作用域的所有变量,返回的是字典
		函数外:打印之前  print()
		函数内:调用之前  locals()
	
globals 返回全局范围的所有变量,返回的是字典
		函数外:打印之前        print()   py3.6
		函数外:打印前后所有的  print()   py3.7及其以上
		
		函数内:调用之前        globals() py3.6
		函数内:调用前后所有的  globals() py3.7及其以上
		
往golbals()返回的字典添加键值对,就是在新建全局变量
如果键是字符串,这个字符串去掉两边的引号,就是一个全局变量的名字


# 4.如何用字符串定义全局变量
# 5.什么是迭代器
概念:能被next函数调用,并且不断返回下一个值的对象就是迭代器Iterator
     取值到最后,无值可取.就返回stopiteration

# 6.如何定义迭代器
# it = iter(Iterable)
# 或许  it = Iterabel.__iter__()

# 7.如何调用迭代器
1  next  一次取一个
next(it)
或者 it.__next__()

2 for  一次全部取完 
for i in it:
	print(i)

3 next for  用多少取多少
for i in range(5)
	next(it)

4 list转换  一次全部取完
print(list(it))


# 8.如何判断迭代器
from collections import Iterator,Iterable
from collections.abc import Iterator,Iterable
isinstance(it,Iterator)

if __iter__ in dir(it) and __next__ in dir(it):

# 9.迭代器和可迭代对象的区别
迭代器是可迭代对象
可迭代对象不一定是迭代器

迭代器  __iter__ in dir(it) and __next__ in dir(it)
可迭代对象(容器类型数据  range对象 迭代器)
__iter__ in dir(iterable)

# 10.dic = {97:"a",98:"b",99:"c"}
# 给你一个列表["a","b","c"] => [97,98,99]
# 11."123" => 123 不使用int的情况下实现该操作;
# 12.filter过滤奇数
# 13.sorted 和 sort区别
sort 只能用于列表
	 会改变原来的列表
sorted 可以适应所有容器类型
	会产生一个新的列表,不会改变原来的列表

# 14.tup = (19,23,42,87) 按照和10余数排序

'''

# 14.tup = (19,23,42,87) 按照和10余数排序

tup = (19,23,42,87)

def func(n):
	return n % 10 
	
lst = sorted(tup,key=func)
print(lst)  #[42, 23, 87, 19]
print('-----------------------14')

# 12.filter过滤奇数
tup = (19,23,42,87)
def func(n):
	if n % 2 == 1:
		return True
	else:
		return False
	
it = filter(func,tup)
print(list(it))  #[19, 23, 87]
print('-----------------------12-1')
tup = (19,23,42,87)

#                     三元运算
it = filter(lambda n:True if n % 2 == 1 else False ,tup)
print(list(it))  #[19, 23, 87]
print('-----------------------12-2')

# 10.dic = {97:"a",98:"b",99:"c"}
# 给你一个列表["a","b","c"] => [97,98,99]

# 思路
# 先把{97:"a",98:"b",99:"c"}的键值对调,变成 {"a":97,"b":98,"c":99}
# 然后用map

lst = ["a","b","c"]

def func(n):
	dic = {97:"a",98:"b",99:"c"}
	dic_new = {}
	for k,v in dic.items():
		dic_new[v] = k
	# print(dic_new)
	return dic_new[n]
# func()  #{'a': 97, 'b': 98, 'c': 99}
	
it = map(func,lst)
print(list(it))  #[97, 98, 99]
print('-----------------------10')

# 11."123" => 123 不使用int的情况下实现该操作;
# 思路
# 先把'123'变成[1,2,3] map
# 然后把[1,2,3]变成123  reduce

strvar = '123'
def func(n):
	dic= {'1':1,'2':2,'3':3}
	return dic[n]
	
it = map(func,strvar)
# print(list(it))  #[1, 2, 3]


def func2(x,y):
	return x*10 +y

from functools import reduce
res = reduce(func2,it)  #返回是计算结果
print(res)  #123
print('-----------------------11')





















