#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 20:16

# #3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
# 	apple 10 3
# 	tesla 100000 1
# 	mac 3000 2
# 	lenovo 30000 3
# 	chicken 10 3
# 变成如下数据格式,并计算出总价格
# [
# 	{'name':'apple','price':10,'amount':3},
# 	{'name':'tesla','price':1000000,'amount':1}
# ]

dic = {}   #字典清空    字典如果放在外面,会出现列表中有5条一样的字典类型的数据 why? 咨询老师
# 原因:此时dic的id是同一个,一变都变(里面是引用)
import copy
li = []
with open('a.txt',mode='r',encoding='utf-8') as fp:
	# dic = {}
	for i in fp:
		listvar = i.strip().split(' ')
		# print(listvar) #['apple', '10', '3']
		# dic = {}   #字典清空  每次建了一个新的字典
		dic['name'] = listvar[0]
		dic['price'] = listvar[1]
		dic['amount'] = listvar[2]

		# dic = {'name':listvar[0],'price':listvar[1],'amount':listvar[2]}
		print(dic)
		# print(id(dic))
		dic = copy.deepcopy(dic)  #完全copy了一份  独立一份
		li.append(dic)
	print(li)
	# print(id(li))

# total = 0
# for i in li:
# 	total += int(i['price']) * int(i['amount'])
# print(total)  #196060

a = [1,2]
b = []
b.append(a)
print(b)  #[[1, 2]]
a.append(1)
print(b)  #[[1, 2, 1]]

a = {1:2}
b = []
b.append(a)
print(b)  #[{1: 2}]
a['100'] = 0   #字典改变了,外面的列表就
print(b)  #[{1: 2, '100': 0}]
print('----------------------------------')

lis = []
lis_new = []
with open('a.txt', mode='r', encoding='utf-8') as fp:
	lis = fp.readlines()
	for i in lis:
		# i = i.rstrip()
		i = i.strip()
		res = i.split(' ')
		lis_new.append(res)



def fx(n, p, a):
	dic = {'name': n, 'price': int(p), 'amount': int(a)}
	lis.append(dic)


for n, a, p in lis_new:
	fx(n, a, p)
print(lis)
print(lis_new)#[['apple', '10', '3'], ['tesla', '100000', '1'], ['mac', '3000', '2'], ['lenovo', '30000', '3'], ['chicken', '10', '3']]






















