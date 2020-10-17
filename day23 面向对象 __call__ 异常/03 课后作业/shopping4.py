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
#余额		
money = 0

#购物车
car = {}

# 1.充值
def recharge():
	global money  #修改全局变量
	num = input('请输入充值金额:')
	if num.isdecimal():
		money = int(num)
		print('充值成功,你的余额是{}元'.format(money))
	else:
		print('请输入数字')	

# 3.获取数据
def read_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			dic = eval(i.strip())  #字符串转成字典  eval 和json类似
			lst.append(dic)
	print(lst) 
	#[{'name': '电脑', 'price': 1999},
	# {'name': '鼠标', 'price': 10}, 
	# {'name': '游艇', 'price': 20}, 
	# {'name': '美女', 'price': 998}, 
	# {'name': '风油精', 'price': 30}]
	return lst

# 4.展现商品
def show_goods(data):
	print('[===========有如下商品供您选择：===========]')
	print('序号     名称       价格')
	for i in range(len(data)):
		print('{:<9d}{:<9s}{}'.format(i+1,data[i]['name'],data[i]['price']))

# 5.购买商品	
	# 1 添加商品到购物车
	
# car的数据结构
	#{1,{'name': '电脑', 'price': 1999,'acount':1},
	#2,{'name': '鼠标', 'price': 10,'acount':2}}
def add_car(num,data):
	# global car   #不需要global也可以修改全局变量 因为car是字典,是引用类型
	if num not in car:
		car[num] = {'name': data[num-1]['name'], 'price': data[num-1]['price']}
		car[num]['acount'] = 1
	else:
		car[num]['acount'] += 1
	# print(car)  #这里car是字典.不需要global,就可以通过增加键值对来修改全局变量
	# 这里如果在函数内对car进行了重新赋值 ,比如  car={},就是局部变量了,无法直接修改全局变量,必须加global才行
	
	# 3 得到购物车的总价
def total_price():	
	total = 0
	print(car,'--------------2')
	return 2


	# 4 结算
def settle(total):
	pass
	
	# 5 删除商品
def del_goods(total):
	pass

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
		num = input('请输入你要购买的商品编号,退出Q,结算N:')
		if num.isdecimal():
			num = int(num)
			if num >= 1 and num <= len(data):
	#     1 添加商品到购物车
				add_car(num,data)
			else:
				print('你输入的商品编码不存在')
	
		# 3 得到购物车的总价
		elif num.upper() == 'N':
			total = total_price()
			
		# 4 结算
			if total <= money:
				settle(total)
			else:				
		# 5 删除商品
				del_goods(total)
				
		elif num.upper() == 'Q':
			print('欢迎下次光临')
			break
		else:
			print('你输入的选项不存在')
	
main()

































