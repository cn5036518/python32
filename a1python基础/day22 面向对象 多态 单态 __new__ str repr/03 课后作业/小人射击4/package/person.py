class Person():
	def __init__(self,gun):
		self.gun = gun
		
	def fill(self,num):
		self.gun.bulletbox.bulletcount += num
		print('你本次新加了{}发子弹,你的子弹总数是{}发'.format(num,self.gun.bulletbox.bulletcount))
		# 枪对象--弹夹对象--子弹总数属性
		
	def fire(self,fcount):
		self.gun.shoot(fcount)






























