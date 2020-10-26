# 定义一个 人类

class Peoson():

	def __init__(self, Gun):
		self.Gun = Gun

	# 方法1 添加子弹
	def add_zi(self,n1):
		self.Gun.DanJia.zidan += n1
		print("添加了{}颗子弹,还剩{}发子弹".format(n1, self.Gun.DanJia.zidan))

	# 方法2 开火
	def fire(self, n2):
		self.Gun.shoot(n2)
