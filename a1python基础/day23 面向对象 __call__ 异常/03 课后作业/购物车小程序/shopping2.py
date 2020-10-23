# ### 购物车小程序
# """
	# 1.充值
	# 2.加载中...
	# 3.获取数据
	# 4.展现商品
	# 5.购买商品
# """
import time,json
# 充值的金额
money = 0
# 购物车字典
car = {}

# 购物车的数据形式:
# {
	# 2:{'name': '鼠标', 'price': 10},
	# 3:{'name': '游艇', 'price': 20},
# }

# 一 充值
def recharge():
	global money  #修改全局变量
	while True:
		num = input('请充值吧,大哥:')
		if num.isdecimal():
			money = int(num)
			print('充值成功{}元人民币'.format(money))
			break
		else:
			print('充值失败,请输入数字')
			
# 二 进度条
# 1 进度条
def myprocess(percent):
	if percent > 1:
		percent = 1
	
	strvar = int(percent * 50) * "#"
	print('\r[{:s}] {:.2f}'.format(strvar,percent * 100),end='')

# 2 执行进度条
def exe_process():
	recv_size = 0
	total_size = 1000
	while recv_size < total_size:
		time.sleep(0.01)
		recv_size += 10
		percent = recv_size / total_size
		myprocess(percent)

# 3 加载中
def loading():
	print('加载商品中...')
	exe_process()
	print()
	
# 三 获取数据
# 从文件读取商品数据
def read_data(filename):
	lst = []
	with open(filename,mode='r',encoding='utf-8') as fp:
		for i in fp:
			dic = json.loads(i)
			lst.append(dic)
	return lst
	
#[{'name': '电脑', 'price': 1999},
 # {'name': '鼠标', 'price': 10},
 # {'name': '游艇', 'price': 20},
 # {'name': '美女', 'price': 998}, 
 # {'name': '风油精', 'price': 30}]
	
# 四 展示商品
def show_goods(data):
	strvar = '商品名称'.center(18)  #两边各7个空格
	print('序号{}价格'.format(strvar)) #打印商品展示第一行
	for k,v in enumerate(data,1):
		# print(k,v)
		#1 {'name': '电脑', 'price': 1999}
		v['num'] = k  #给字典新加一个键值对num
		# print(v)
		#{'name': '电脑', 'price': 1999, 'num': 1}
		print('{:<10d}{:<12s}{}'.format(v['num'],v['name'],v['price']))

def main():
	# 1.充值
	recharge()	
	# 2.加载中
	loading()
	# 3.获取数据
	data = read_data('shopping_data.json')
	print(data)
	#[{'name': '电脑', 'price': 1999}, {'name': '鼠标', 'price': 10}, {'name': '游艇', 'price': 20}, {'name': '美女', 'price': 998}, {'name': '风油精', 'price': 30}]
	# 4.展示商品
	show_goods(data)
	
	
main()
























































