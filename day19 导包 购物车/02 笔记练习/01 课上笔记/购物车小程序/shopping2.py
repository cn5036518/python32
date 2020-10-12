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
		time.sleep(0.02)
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
	

def main():
	# 1.充值
	recharge()	
	# 2.加载中
	loading()
	
main()
























































