class Person():
	def __init__(self,gun):
		self.gun = gun # 枪对象(可以拿到枪的属性和方法)  
		# shoot方法可以拿到每次发射的子弹数
		# 枪对象的属性有弹夹对象 (弹夹对象可以拿到子弹总数)
		
	def fill(self,num):  #加子弹
	# 参数是每次加的子弹数
		self.gun.bulletbox.bulletcount += num
		print('你本次新加了{}发子弹,剩余的子弹总数是{}发'.format(num,self.gun.bulletbox.bulletcount))
		# self.gun.bulletbox.bulletbox是子弹总数  #修改了子弹总数1  +
		# 通过弹夹对象的子弹总数属性
		# 枪对象-弹夹对象-子弹总数属性
		
	def fire(self,fcount):  #开火  发射子弹
	# 参数是每次发射的子弹数
		self.gun.shoot(fcount)































