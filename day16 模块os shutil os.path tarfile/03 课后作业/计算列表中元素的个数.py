#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:   2020/10/7 下午8:21


lst1= [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '风油精', 'price': 30}]
lst = [{'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '游艇', 'price': 20}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}]


li = []
for i in lst1:
	if i in lst:
		i["amount"]=lst.count(i)
		li.append(i)
print(li)
#[{'name': '电脑', 'price': 1999, 'amount': 3}, {'name': '鼠标', 'price': 10, 'amount': 1},
# {'name': '游艇', 'price': 20, 'amount': 2}, {'name': '美女', 'price': 998, 'amount': 1}]

# 求列表中每个元素的个数
#  方法1
li = [1,22,33,33]
from collections import Counter
print(dict(Counter(li)))
# {1: 1, 22: 1, 33: 2}

# 方法2
li = [1,22,33,33]
dic = {}
for i in li:
	if i not in  dic:
		dic[i] = 1
	else:
		dic[i] += 1
print(dic)


lst1= [{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '风油精', 'price': 30}]
lst2 = [{'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '游艇', 'price': 20}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}]

lst_new = []
for i in lst1:
	if i in lst2:
		i['mount'] = lst2.count(i)
		lst_new.append(i)
print(lst_new)
#[{'name': '电脑', 'price': 1999, 'mount': 3}, {'name': '鼠标', 'price': 10, 'mount': 1}, 
# {'name': '游艇', 'price': 20, 'mount': 2}, {'name': '美女', 'price': 998, 'mount': 1}]
print('-------------------------1')

setvar = set()
for i in lst2:
	setvar.add(str(i))
print(setvar)

for i in setvar:
	print(eval(i),type(i),type(eval(i)))
print('-------------------------2')


lst2 = [{'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '游艇', 'price': 20}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}, {'name': '电脑', 'price': 1999}]

dic = {}
for i in lst2:
	# if i not in dic:
	i = str(i)
	if i not in dic:    #把字典的两端加上引号 变成字符串,就是不可变的
	#TypeError: unhashable type: 'dict'  #字典的键必须是不可变的,字典是可变的,不能作为字典的键
		dic[i] = 1
	else:
		dic[i] += 1
print(dic)
print('--------------------3')

for k,v in dic.items():
	print(k,type(k),type(eval(k)),v)  #这里的eval可以把k两端的引号去掉,转成dict  ,即把"{'name': '鼠标', 'price': 10}" 变成了{'name': '鼠标', 'price': 10}
	# print(k,type(k),type(exec(k)),v) #这里exec没有eval的功能



































