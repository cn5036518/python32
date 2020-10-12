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

with open('a.txt',mode='r',encoding='utf-8') as fp:
	fruit_list = []
	for i in fp:
		data = i.strip().split(' ')
		# print(data)
		fruit_dict = {}
		fruit_dict['name'] = data[0]
		fruit_dict['price'] = data[1]
		fruit_dict['amount'] = data[2]
		# print(fruit_dict)
		fruit_list.append(fruit_dict)
	print(fruit_list)









