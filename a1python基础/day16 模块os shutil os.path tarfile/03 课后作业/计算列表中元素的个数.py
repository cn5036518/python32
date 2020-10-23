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
print('--------------------4')

import json

dic2 = {'name':'jack'}
strvar = str(dic2)
print(repr(strvar),type(strvar))  #"{'name': 'jack'}" <class 'str'>

# 方法1   eval
print(eval(strvar),type(eval(strvar)))  #{'name': 'jack'} <class 'dict'>
print('--------------------4')


#方法2  json
# dic2 = {'name':'jack'}
dic2 = {"name":"jack"}

res = json.dumps(dic2)
print(res,type(res))  #{"name": "jack"} <class 'str'>
print(repr(res),type(res))  #'{"name": "jack"}' <class 'str'>

dic3 = json.loads(res)
print(dic3,type(dic3))  #{'name': 'jack'} <class 'dict'>
print('--------------------5')

dic2 = {"name":"jack"}  #
print(repr(str(dic2)))  #"{'name': 'jack'}"   结论:dict转str 用dumps,而不用用str,因为str转换后,字典变成了单引号,无法用json恢复

dic = json.loads(str(dic2))
print(dic)
print('--------------------6')
# https://blog.csdn.net/whatday/article/details/102958323

# 在 python3 里，一个json是一个字典，形如 {"a":15}
#
# 那么，如果你要将它转换成字符串，也许你用的是str({"a":15})，这样转出来的，可能是是s= "{'a':'15'}"，也就是说，里面的kv是单引号的。
# 这个字符串，传到其他地方，再用json.loads(s)的时候会出错，json不支持单引号。
#
# 所以，假如你想把一个json结构，转成字符串，传递给远处，然后再重新解析成json结构，应该这样：
#
# s = json.dumps({"a":15})
#
# 然后，把数据传到远端，然后再解析回来：
#
# d = json.loads(s)
#
# 这样就不会出错了。

str1 = '{"name":"jack"}'
dic = json.loads(str1)
print(dic,type(dic)) #{'name': 'jack'} <class 'dict'>


#结论:dict转str 用dumps,而不用用str,因为str转换后,字典变成了单引号,无法用json恢复





























