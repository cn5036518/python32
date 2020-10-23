# 思路  默写5
# 1 充值
# 2 读取数据
# 3 商品展示
# 4 购买
	# 1 添加商品到购物车
	# 2 算购物车总价
	# 3 结算
	# 4 删除商品

#定义全局变量	
#账户余额
money = 0
# 购物车
car = {}
# 商品文件
filename = r'shopping_data.json'
# 商品数据(从文件读取后的)
data = []
# 购物车总价格
total = 0
	
# 步骤
# 先主函数
# 后分函数

# 分函数
# 1 充值
def recharge():
	while True:
		global money
		num = input('请输入你的充值金额:')
		if num.isdecimal():
			money = int(num)
			print('你的余额是{}元'.format(money))
			break
		else:
			print('请输入数字')
	
# 2 读取数据
def read_file():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			dic = eval(i.strip())  #eval把字符串转换成字典  json.loads()
			data.append(dic)
	print(data)
	# [{'name': '电脑', 'price': 1999}, 
	# {'name': '鼠标', 'price': 10}, 
	# {'name': '游艇', 'price': 20}, 
	# {'name': '美女', 'price': 998},
	# {'name': '风油精', 'price': 30}]
	# return lst

# 3 商品展示
def show_goods():
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))

# 4 购买
	# 1 添加商品到购物车
	#car的数据结构 	# {1:{'name': '电脑', 'price': 1999,'acount':1}, 
	# 2:{'name': '鼠标', 'price': 10,'acount':2}}
def add_car(num):
	if num not in car:
		car[num] = {'name': data[num-1]['name'], 'price': data[num-1]['price']}  #1 注意点1
		car[num]['acount'] = 1
	else:
		car[num]['acount'] += 1  # 2 和统计字符串中每个字符的个数的方法类似
	print(car) #3 car是字典,可以在函数内修改全局变量,而不需要用global,和str int不一样
	#{2: {'name': '鼠标', 'price': 10, 'acount': 2}}
	
	# 2 算购物车总价
def total_price():
	global total  #修改全局变量 和31行money一样 
	total = 0  #每次都要重置,全局变量total会改变  注意点
	for k,v in car.items():
		total += v['price'] * v['acount']
	print(total)
	# return total
	
	# 3 结算
def settle(total):
	print('你选购的商品全部购买成功,一共花了{}元,你的余额是{}元'.format(total,money-total))
	
	# 4 删除商品
def del_goods(total):
	num = input('你的余额不足,请输入你要删除的商品编号:')
	if num.isdecimal():
		num = int(num)  #注意点
		if num not in car:
			print('你输入的商品编号不在购物车里')
		else:
			car[num]['acount'] -= 1 #递减数量  注意点
			if car[num]['acount'] == 0:
				car.pop(num)
	else:
		print('请输入数字')
	


# 主函数
def main():
# 1 充值
	recharge()
	
# 2 读取数据
	read_file()

# 3 商品展示
	show_goods()

# 4 购买
	sign = True
	while sign:
		num = input('请输入你要购买的商品编号,退出按Q,结算按N:')
		if num.isdecimal():
			num = int(num)
			# 1 添加商品到购物车
			add_car(num)
			
		elif num.upper() == 'N':
			while True:
				# 2 算购物车总价
				# total = total_price()
				total_price()

				if total <= money:				
					# 3 结算
					settle(total)
					sign = False
					break
				else:
					# 4 删除商品
					del_goods(total)
		elif num.upper() == 'Q':
			print('欢迎下次光临')
			break
		else:
			print('请输入数字')
	
main()














































