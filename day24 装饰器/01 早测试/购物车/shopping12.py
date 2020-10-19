# 思路  默写7
# 1.充值
# 2.读取数据
# 3.商品展示
# 4.购买
	# 1添加商品到购物车
	# 2计算购物车总价
	# 3结算
	# 4删除商品
	
# 步骤
# 1先主函数
# 2后分函数
# 3定义全局变量


# 全局变量

#1 账户余额
money = 0

#2 购物车商品
car = {}

#3 总价
total = 0

#4 商品文件目录
filename = r'shopping_data.json'

#5 商品文件字典(读取商品文件)
data = []


# 二 分函数
# 1.充值
def recharge():
	while True:
		global money
		num = input('请输入你的充值金额:')
		if num.isdecimal():
			money = int(num)
			print('充值成功,你的余额是{}元'.format(money))
			break
		else:
			print('请输入数字')		

# 2.读取数据
def read_file():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			dic = eval(i.strip())
			data.append(dic)
		print(data)
		#[{'name': '电脑', 'price': 1999},
		# {'name': '鼠标', 'price': 10},
		# {'name': '游艇', 'price': 20},
		# {'name': '美女', 'price': 998},
		# {'name': '风油精', 'price': 30}]

# 3.商品展示
def show_goods():
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))

# 4.购买
	# 1添加商品到购物车
#car的数据结构  		#{1:{'name': '电脑', 'price': 1999,'acount': 1},
		# 2:{'name': '鼠标', 'price': 10,'acount': 1}}
def add_cars(num):
	if num not in car:
		car[num] = {'name': data[num-1]['name'], 'price': data[num-1]['price']}
		car[num]['acount'] = 1
	else:
		car[num]['acount'] += 1
	print(car)
	
	# 2计算购物车总价
def total_price():
	global total
	total = 0
	for k,v in car.items():
		total += v['price'] * v['acount']
	print(total)
	
	# 3结算
def settle():
	print('你选购的商品购买成功,一共花费了{}元,你的余额是{}元'.format(total,money-total))
	
	# 4删除商品
def del_goods():
	num = input('你的余额不足,请删除部分商品,请输入你要删除的商品编号:')
	if num.isdecimal():
		num = int(num)
		if num not in car:
			print('你输入的商品编号不在购物车里')
		else:
			car[num]['acount'] -= 1
			if car[num]['acount'] == 0:
				car.pop(num)
	else:
		print('请输入数字')
	

# 三 主函数
def main():
# 1.充值
	recharge()
	
# 2.读取数据
	read_file()

# 3.商品展示
	show_goods()

# 4.购买
	sign = True
	while sign:
		num = input('请输入你要选购的商品编号,退出按Q,结算按N:')
		if num.isdecimal():
			num = int(num)
			if num >=1 and num <= len(data):
				# 1添加商品到购物车
				add_cars(num)

		elif num.upper() == 'N':
			while True:
				# 2计算购物车总价
				total_price()

				if total <= money:
					# 3结算
					settle()
					sign = False
					break
					
				else:
					# 4删除商品
					del_goods()
					
		elif num.upper() == 'Q':
			print('欢迎下次光临')
			break

		else:
			print('请输入数字')
	
main()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	



























