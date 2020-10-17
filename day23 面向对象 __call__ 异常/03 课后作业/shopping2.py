# ### 购物车小程序
	# 1.充值
	# 2.加载中... 可以最后考虑--nok
	# 3.获取数据
	# 4.展现商品
	# 5.购买商品
	#    1 添加商品到购物车
	#    2 展示购物车



# 账户的余额
money = 0

# 购物车字段
car = {}



# 充值
def recharge():
	num = input('请输入你要充值的金额:')
	if num.isdecimal():
		global money
		money = int(num)
		print('充值成功,你的余额是{}元'.format(money))
	else:
		print('请输入数字')

			
# 读取数据
def get_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			i = eval(i.strip())  #把字符串转换成字符  和json类似  注意点1
			# print(i,type(i))
			lst.append(i)
	print(lst)
	# ['{"name":"电脑","price":1999}',
	# '{"name":"鼠标","price":10}',
	# '{"name":"游艇","price":20}', 
	# '{"name":"美女","price":998}', 
	# '{"name":"风油精","price":30}']
	return lst

# 商品展示	
def show_goods(data):
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))


# 1 添加商品到购物车
	#car的数据结构  {'1,{"name":"电脑","price":1999,'account':1}',
	# '2,{"name":"鼠标","price":10,'account':2}
def add_car(num,data):
	if num not in car:
		car[num]= {'acount': 1,
				   'name':data[num-1]['name'],
				   'price':data[num-1]['price']}
				   
	else:
		car[num]['acount'] += 1
	print(car)
	# {2: {'acount': 1, 'name': '鼠标', 'price': 10}, 
	# 3: {'acount': 2, 'name': '游艇', 'price': 20}}


# 2 展示购物车的商品详情

	
# 2-2 购物车结算前,显示已经购买的商品清单

# 3 得到购物车的总价
def car_list():
	total = 0
	for k,v in car.items():
		total += car[k]['price'] * car[k]['acount']
		print('商品编码:{} 商品名称{} 商品价格{} 商品数量{} 商品总价{}'
		.format(k,car[k]['name'],car[k]['price'],car[k]['acount'],total))
	print(total)
	return total


# 4 结算
def settle(total):
	print('你选择的商品已经购买成功,一共花费是{}元,你的余额是{}元'.format(total,money-total))

	
# 5 删除商品
def del_goods(total):
	print('你的余额不足,还差{}元,请删除部分商品'.format(total-money))
	num = input('请输入你要删除的商品编号:')
	if num.isdecimal():
		num = int(num)
		if num in car:
			car[num]['acount'] -= 1
			if car[num]['acount'] == 0:
				car.pop(num)
		else:
			print('你输入的编号不存在')
	else:
		print('你输入的选项不存在')


filename = r'shopping_data.json'

def main():
	# 1.充值
	recharge()
	
	# 3.获取数据
	data = get_data(filename)

	# 4.展现商品
	show_goods(data)
	
	# 5.购买商品
	sign = True
	while sign:
		# 1.添加商品到购物车
		num = input('请输入你要购买的商品编号,N结算,Q退出:')
		if num.isdecimal():
		#    1 添加商品到购物车
			num = int(num)
			if num >= 1 and num <= len(data):
				num = int(num)
				add_car(num,data)
			#    2 展示购物车的商品详情	
			else:
				print('你输入的编号不存在')

		elif num.upper() == 'N':	
		# 	2.结算商品
			while True:
				# 结算出总价格
				total = car_list()
				# 删除商品
				if total > money:
					del_goods(total)
				else:
				# 正常结算
					settle(total)
					sign = False
					break
		
		# 3.退出购物
		elif num.upper() == 'Q':
			print('欢迎下次光临')
			break
		
		# 4.选项不存在
		else:
			print('你输入的选项不存在')

	
main()





































