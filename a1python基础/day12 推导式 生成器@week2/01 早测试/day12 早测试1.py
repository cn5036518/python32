#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/26 9:10

# 1.什么是匿名函数,语法?


# lambda  x : '偶数' if x % 2 == 0
# lambda  x : '偶数' if x % 2 == 0 else '奇数'


# func ＝　lambda  x : '偶数' if x % 2 == 0
# print(func(12))  


func = lambda  x : '偶数' if x % 2 == 0 else '奇数'
print(func(12))
print('-----------------------1')

# 2.配合三运运算符写一个过滤奇数的匿名函数

lst = [1,2,3,4,5,6]

lst_new = []
for i in lst:
	if i % 2 == 1:
		lst_new.append(i)
print(lst_new)  #[1, 3, 5]

func = lambda x: '奇数' if x % 2 == 1 else '偶数'
print(func(33))  #奇数
print('-----------------------2')

# 4.如何用字符串定义全局变量
# 1 用字符串创建一个全局变量
dic = globals()
print(dic)  # {'func': <function <lambda> at 0x0000026EE451BD08>, 'lst': [1, 2, 3, 4, 5, 6], 'lst_new': [1, 3, 5]}

dic['name'] = 'jack'  #用字符串'name' 创建了一个全局变量name,该全局变量的值是'jack'
print(name)  # jack
print(dic)
print('-----------------------4-1')

# 2 用字符串创建多个全局变量(批量创建) a1 a2 a3
def func():
	for i in range(1,4):
		dic = globals()   #获取全局变量的字典
		k = 'a'+str(i)    #str和int无法用+拼接  只能是str和str用+拼接 所有需要把int转换成str
		dic[k] = i
		# dic[k] = 1   #写死  a1 a2 a3的值都是1
	print(dic)  # {'a1': 1, 'a2': 2, 'a3': 3}
	return dic
func()
print('-----------------------4-2')

# 3 如何批量创建一个字典
# dic = {'1':1,'2':2,...'9':9}
dic2 = {}
for i in range(1,10):
	dic2[str(i)] = i
print(dic2)  #{'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
print('-----------------------4-3')


































