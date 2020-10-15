# ### 枪类
	# 枪类:    gun
		# 属性: 弹匣对象
		# 方法: 射击 shoot
class Gun():
	def __init__(self,bulletbox):
		self.bulletbox = bulletbox
		
	# 射击方法
	def shoot(self,firecount):
		# 剩余数量 = 总数量 - 射出的数量
		# self.bulletbox.bulletcount = self.bulletbox.bulletcount - firecount
		
		if self.bulletbox.bulletcount < firecount:
			print('你需要上子弹')
		else:
			self.bolletbox.bulletcount -= firecount
			

















































