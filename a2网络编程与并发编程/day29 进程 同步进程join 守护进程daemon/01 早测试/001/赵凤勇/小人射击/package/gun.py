# 定义一个枪类;

class Gun():

	# 使用构建函数为枪类添加一个实例属性
	def __init__(self, DanJia):
		self.DanJia = DanJia

	# 定义一个shoot方法!
	def shoot(self, fire_count):
		# 开始判断并且返回射击以后的子弹详情

		if self.DanJia.zidan >= fire_count:
			self.DanJia.zidan -= fire_count
			print("哒" * fire_count,"开了{}枪枪里还有{}颗子弹".format(fire_count,self.DanJia.zidan))


		# elif fire_count - self.DanJia.zidan <= self.DanJia.zidan <= fire_count:
		#
		# 	print("哒" * self.DanJia.zidan,"开了{}枪,枪里还有{}颗子弹".format(self.DanJia.zidan, 0) )

		else:
			print("哒" * (self.DanJia.zidan),"还剩下{}子弹射不出来".format(fire_count - self.DanJia.zidan))
			print("没有子弹了,请上子弹")

