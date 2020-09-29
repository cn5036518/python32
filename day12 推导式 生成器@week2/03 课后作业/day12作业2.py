#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/25 21:20

# # 2.用推导式写如下程序
lst1 = {
		'name':'alex',
		'Values':[
			{'timestamp': 1517991992.94,'values':100,},
			{'timestamp': 1517992000.94,'values': 200,},
			{'timestamp': 1517992014.94,'values': 300,},
			{'timestamp': 1517992744.94,'values': 350},
			{'timestamp': 1517992800.94,'values': 280}
		]
	}
# 将lst1 转化成如下lst2:
lst2 = [
	[1517991992.94, 100],
	[1517992000.94, 200],
	[1517992014.94, 300],
	[1517992744.94, 350],
	[1517992800.94, 280]
]
# 普通方法

lst = lst1['Values']
# print(lst)

lst_new = []
for i in lst:
	# print(i)
	lst_new.append([i['timestamp'],i['values']])
print(lst_new)

# 推导式
lst2 = [[i['timestamp'],i['values']] for i in lst1['Values']]
print(lst2)
print('---------------------------2')


# # 3.读取一个文件所有内容,通过生成器调用一次获取一行数据.
# with open('a.txt',mode='r',encoding='utf-8') as fp:
# 	res = fp.read()
# 	print(res)
	
def mygen():
	with open('a.txt',mode='r',encoding='utf-8') as fp:
		for i in fp:
			yield i.strip()

gen = mygen()

for i in range(2):
	print(next(gen))
print('---------------------------3')

# # 4.将普通求和函数改写成yield写法
def add(a,b):
   return a + b

def mygen(a,b):
	yield a + b
	
gen = mygen(3,4)
print(next(gen))
print('---------------------------4-1')






























