# ### 购物车小程序
	# 1.充值
	# 2.加载中... 可以最后考虑--nok
	# 3.获取数据
	# 4.展现商品
	# 5.购买商品
	#     1 添加商品到购物车
		# 3 得到购物车的总价
		# 4 结算	
		# 5 删除商品



# 账户的余额
money = 0


# 购物车字段
car = {}



# 充值
def recharge():
	global money  #修改全局变量
	num = input('请输入充值金额:')
	if num.isdecimal():
		money = int(num)
		print('充值成功,你的余额是{}元'.format(money))
	else:
		print('请输入数字')
			
# 读取数据
def read_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			lst.append(eval(i.strip()))
	print(lst)
	# [{'name': '电脑', 'price': 1999},
	# {'name': '鼠标', 'price': 10}, 
	# {'name': '游艇', 'price': 20}, 
	# {'name': '美女', 'price': 998},
	# {'name': '风油精', 'price': 30}]
	return lst

# 商品展示	
def show_goods(data):
	pass
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))


# 1 添加商品到购物车
# car的结构
	# {1:{'name': '电脑', 'price': 1999,'acount':1},
	# 2: {'name': '鼠标', 'price': 10,'acount':1}}

def add_goods(num,data):
	if num not in car:
		for i in data:
			car[num] = {'name': data[num-1]['name'], 'price': data[num-1]['price']}
			car[num]['acount'] = 1
	else:
		car[num]['acount'] += 1
	print(car) 
	#{1: {'name': '电脑', 'price': 1999, 'acount': 2}, 2: {'name': '鼠标', 'price': 10, 'acount': 1}}


# 3 得到购物车的总价
def toatl_price(num):
	total = 0
	for k,v in car.items():
		total += v['price'] * v['acount']
	print(total)
	return total


# 4 结算
def settle(total):
	print('你选购的商品全部购买成功,一共花了{}元,你的余额是{}元'.format(total,money-total))
	
# 5 删除商品
def del_goods(total):
	print('你的余额不够,还差{}元,请删除部分商品'.format(total-money))
	num = input('请输入你要删除的商品编号:')
	if num.isdecimal():
		num = int(num)
		if num  in car:
			car[num]['acount']  -= 1
			if car[num]['acount'] == 0:
				car.pop(num)
		else:
			print('你输入的选项不存在')
		
	else:
		print('请输入数字')



filename = r'shopping_data.json'

def main():
	# 1.充值
	recharge()
	
	# 3.获取数据
	data = read_data(filename)

	# 4.展现商品
	show_goods(data)

	
	# 5.购买商品
	sign = True
	while sign:
		# 1.添加商品到购物车
		num = input('请输入你要购买的商品编号,Q退出,N结算')
		if num.isdecimal():
			num = int(num)
			if num >=1 and num <= len(data):
			#    1 添加商品到购物车
				add_goods(num,data)

				#2 展示购物车的商品详情	
			else:
				print('你输入的选项不存在')

		elif num.upper() == 'N':
			while True:
			# 	2.结算商品
					# 结算出总价格
				total = toatl_price(num)
				if total > money:
					# 删除商品
					del_goods(total)
				else:
					# 正常结算
					settle(total)
					sign = False
					break

		elif num.upper() == 'Q':
		# 3.退出购物
			print('欢迎下次光临')
			break

		else:
		# 4.选项不存在
			print('你输入的选项不存在')

	
main()





































