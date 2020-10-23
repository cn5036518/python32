# ### 购物车小程序
	# 1.充值
	# 2.加载中... 可以最后考虑--nok
	# 3.获取数据
	# 4.展现商品
	# 5.购买商品
	#    1 添加商品到购物车
	#    2 展示购物车

import json

# 账户的余额
money = 0
# 购物车字段
car = {}


# 充值
def recharge():
	global money
	while True:
		num = input('请充值哈:')
		if num.isdecimal():
			money = int(num)
			print('充值成功{}元人民币'.format(money))
			break
		else:
			print('充值失败，请输入数字')
			
# 读取数据
def read_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			dic = json.loads(i)
			# print(dic,type(dic))
			lst.append(dic)
	print(lst)
	# [{'name': '电脑', 'price': 1999}, 
	# {'name': '鼠标', 'price': 10}, 
	# {'name': '游艇', 'price': 20},
	# {'name': '美女', 'price': 998},
	# {'name': '风油精', 'price': 30}]
	return lst
	
def show_goods(data):
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		# print(i)
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))

# 1 添加商品到购物车
def add_car(num,data):#num是商品编号
# 购物车的数据形式:
# {
	# 2:{'name': '鼠标', 'price': 10, 'account': 1},
	# 3:{'name': '游艇', 'price': 20, 'account': 1},
	# 1: {'name': '电脑', 'price': 1999, 'account': 1}
# }

	# 如果第一次购买商品,键一定不在字典中
	if num not in car:
		car[num] = {'name':data[num-1]['name'],
		'price':data[num-1]['price'],
		'account':1}
	else:
		car[num]['account'] += 1
	print(car)
	#{1: {'name': '电脑', 'price': 1999, 'account': 1}}

# 2 展示购物车的商品详情
def show_car(num):	
	print('*' * 50)
	print('您选择的商品具体信息:')
	print('*-商品名称:{}'.format(car[num]['name']))
	print('*-商品单价:{}'.format(car[num]['price']))
	print('*-商品数量:{}'.format(car[num]['account']))
	print('已成功添加到购物车~ 请继续shopping ~')
	print('*' * 50)
	
# 3 购物车结算前,显示已经购买的商品清单
# car = {1: {'name': '电脑', 'price': 1999, 'account': 1},
# 2:{'name': '鼠标', 'price': 10, 'account': 2}
# }	
# 1 {'name': '电脑', 'price': 1999, 'account': 1}
# 2 {'name': '鼠标', 'price': 10, 'account': 2}

# 3 得到购物车的总价
def car_list():
	total_price = 0
	print('你购买的商品清单如下:')
	for k,v in car.items():
		print(k,v)
		total_price += v['price'] * v['account']
		# print('商品编号:{} 商品名称:{} 商品单价:{}元 商品数量:{}个 商品总价:{}元'
		# .format(k,v['name'],v['price'],v['account'],total_price))
	print(total_price)
	return total_price
	
# car_list()

# 4 结算
def settle(total,money):
	print('一共{}元,你已经成功购买商品,你的余额是{}元'
	.format(total,money-total))
	
# 5 删除商品
def del_goods(total,money):
	print('余额不足,还差{}元,请删除商品'.format(total-money))
	num = input('请输入要删除的商品编号:')
	if num.isdecimal():
		num = int(num)
		if num in car:
			# 删除商品数量
			car[num]['account'] -= 1
			# 检测商品数量是不是0,如果是把该条商品信息从购物车中删掉,不显示
			if car[num]['account'] == 0:
				car.pop(num)
		else:
			print('你输入的商品不存在')
	else:
		print('你输入的选项不存在')


def main():
	# 1.充值
	recharge()
	
	# 3.获取数据
	data = read_data('shopping_data.json')
	# 4.展现商品
	show_goods(data)
	
	# 5.购买商品
	sign = True
	while sign:
		num = input('请输入您要购买的商品,N结算,Q退出：')
		# 1.添加商品到购物车
		if num.isdecimal():
			num = int(num)
			if num >= 1 and num <= len(data):
				#    1 添加商品到购物车
				add_car(num,data)
				#    2 展示购物车的商品详情
				show_car(num)
			else:
				print('你输入的商品不存在,请输入1~{}'.format(len(data)))
			
		# 2.结算商品
		elif num.upper() == 'N':
			while True:
			# 结算出总价格
				total = car_list()
				print(total)
				if total > money:
				# 删除商品
					del_goods(total,money)
				else:
					# 正常结算
					settle(total,money)
					sign = False
					break
				
		
		# 3.退出购物
		elif num.upper() == 'Q':
			print('欢迎下次光临')
			sign = False
		else:
			print('你输入的选项不存在')
	
	
main()





































