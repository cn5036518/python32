#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:   2020/10/7 下午4:22


# ### 2.购物车小程序

# 1. 用户先给自己的账户充钱：比如先充3000元。
# 2. 页面显示 序号 + 名称 + 价格 , 如：
# [===========有如下商品供您选择：===========]
# 序号     名称       价格
# 1 		 电脑		1999
# 2 		 鼠标		10
# 3 		 游艇		20
# 4 		 美女		998
# n或N	购物车结算
# q或Q	退出程序(如不结算购物车可直接退出)]
# [==========================================]
# 购物车结算
# 3. 用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车，用户还可继续添加商品。
# 4. 如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 5. (1)用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价
#    (2)若充值的钱数不足则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买退出
#    (3)退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少
# 6. 用户输入Q或者q 直接退出程序。

# 思路
# 1 先写思路伪代码,再写代码
# 2 先变量,后文件

# 内容
# 1 充值   变量money  后文件
# 2 读取文件 商品展示  json==>dict
# 3 购物车结算 商品的价值和money做减法  if流程判断 

# 步骤
# 1 先简单实现demo,再迭代完善

# 待办
# 1 购物车商品展示 --nok   2个电脑,数量如何显示2?
# 2 支付完购物车后,最新余额写入文件 --nok

# 版本
# 版本1:基线版本
# 版本2:添加删除购物车部分商品1
# 版本3:添加支付完购物车后,最新余额写入文件 --nok


import json,os

# 1 充值   变量money  后文件--ok
def recharge():
	balance = input('请充值:')
	if balance.isdecimal():
		balance = int(balance)
		print('你的余额是{}元'.format(balance))
	#写入文件
		with open('balance.txt','w',encoding='utf-8') as fp:
			json.dump(balance,fp)
		# return balance
	else:
		print('请输入数字')
		
# recharge()


# 2 读取文件 商品展示  json==>dict
def product_display():
    #从文件读取到list
	lst = []
	with open('shopping_data.json','r',encoding='utf-8') as fp:
		for i in fp:
			dic = json.loads(i)
			lst.append(dic)
	print(lst)
	#[{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}]
	
	# 商品展示
	print('[===========有如下商品供您选择：===========]')
	print('序号        名称          价格')
	for i in range(len(lst)):
		print('{:<10d} {:<10s}  {:<10d}'.format(i+1,lst[i]['name'],lst[i]['price']))
	
	return lst
# lst = product_display()
# print(lst)

# 3 购物车结算 商品的价值和money做减法  if流程判断 
def shopping():
	pass
	lst = product_display()
	while True:
		choice = input('选商品按c,结算按s,退出按t,删除购物车部分商品按d:')
		if choice.upper() == 'C':
			lst_new = []
			product_id = input('请输入你要购买的商品序号1~5:')
			if product_id.isdecimal():
				product_id = int(product_id+1)
				print(product_id)
				if product_id > len(lst):
					print('输入有误，并重新输入序号1~5')
				else:
					print('你选择的商品序号是{},商品名称是[{}],商品价格是[{}]'.format(product_id,lst[product_id]['name'],lst[product_id]['price']))			

			else:
				print('输入有误，并重新输入序号1~5')
				
				# 1 如果购物车文件不存在,就创建一个				
			if not os.path.exists('shopping_car.json'):
				with open('shopping_car.json', mode='w', encoding='utf-8') as fp:
					lst_new.append(lst[product_id])
					json.dump(lst_new, fp, ensure_ascii=False)
			# 2 如果购物车文件存在,就先读取购物车文件 
			else:
				with open('shopping_car.json', mode='r+', encoding='utf-8') as fp:
					lst_new = json.load(fp)	
					# 然后把放入购物车的商品写入文件	
					lst_new.append(lst[product_id])
					print(lst_new)
					fp.seek(0)
					json.dump(lst_new, fp, ensure_ascii=False)
			print('已放入购物车的商品list是{}'.format(lst_new))
				
		elif choice.upper() == 'S':
			pass
			#1 读取余额文件
			with open('balance.txt','r',encoding='utf-8') as fp:
				balance_str = json.load(fp)
				balance = int(balance_str)
				print('你目前的余额是[{:d}]元'.format(balance))
			
			#2 读取购物车文件,打印出来
			with open('shopping_car.json', mode='r+', encoding='utf-8') as fp:
				lst_new = json.load(fp)	
				print('你的购物车的商品列表是{}'.format(lst_new))
			
			
			#3 计算购物车文件的总价格
			total_price = 0
			for i in lst_new:
				total_price += i['price'] * 1  #购物车的每个商品只买了一个 如果是多个呢?和买一个一样,list的元素可以重复
			print('你的购物车的商品的总价格是[{}]元'.format(total_price))				
			
			#4 余额-购物车总价格
			if balance >= total_price:
				balance = balance - total_price
				print('支付完购物车后,你目前的余额是[{}]元'.format(balance))
				#最新余额写入文件  --nok
			
			else:
				print('余额不足,请删除购物车里部分商品')
				
		elif choice.upper() == 'D':	
			print('你的购物车的商品列表是{}'.format(lst_new))
			product_id = input('请输入你要从购物车删除的商品序号0~{}:'.format(len(lst_new)-1))
			if product_id.isdecimal():
				product_id = int(product_id)
				if product_id > len(lst):
					print('输入有误，并重新输入序号0~{}:'.format(len(lst_new)-1))
				else:
					print('你要删除的商品序号是{},商品名称是[{}],商品价格是[{}]'.format(product_id,lst_new[product_id]['name'],lst_new[product_id]['price']))
					# print('你要删除的商品序号是{},商品名称是[{}],商品价格是[{}]'.format(product_id,lst[product_id]['name'],lst[product_id]['price']))
			else:
				print('输入有误，并重新输入序号0~{}'.format(len(lst_new)-1))
				
			#先读取购物车文件 
			with open('shopping_car.json', mode='r+', encoding='utf-8') as fp:
				lst_new = json.load(fp)	
				# 然后把放入购物车的商品写入文件	
				lst_new.pop(product_id)
				print(lst_new)
				fp.seek(0)
				fp.truncate(0)  #清空文件
				json.dump(lst_new, fp, ensure_ascii=False)
			print('删除后,已放入购物车的商品list是{}'.format(lst_new))
			
			
		elif choice.upper() == 'T':
			break
				
				
shopping()


























