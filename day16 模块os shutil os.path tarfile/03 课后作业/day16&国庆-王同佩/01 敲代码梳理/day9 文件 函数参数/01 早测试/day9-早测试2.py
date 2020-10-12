#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 9:02

# 6	通过键获取值（若没有该键可设置默认值，预防报错）
dic = {'a': 22, 'b': 22, 'c': 22}
print(dic.get('a','没有该键'))  #22
print(dic.get('d','没有该键'))  #没有该键
print('-------------------------------1')

# 7	将字典的键组成新的可选代对象
dic = {'a': 22, 'b': 22, 'c': 22}
for i in dic.keys():
	print(i)
print('-------------------------------2')

# 8	将字典中的值组成新的可迭代对象
dic = {'a': 22, 'b': 22, 'c': 22}
for i in dic.values():
	print(i)
print('-------------------------------3')

# 9	将字典的键值对凑成一个个元组，组成新的可迭代对象
dic = {'a': 22, 'b': 22, 'c': 22}
for i in dic.items():
	print(i)
print('-------------------------------4')











































