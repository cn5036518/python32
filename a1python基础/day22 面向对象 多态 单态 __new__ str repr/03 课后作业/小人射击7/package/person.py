class Person():
	def __init__(self,gun):
		self.gun = gun
		
	def fill(self,bullet_num):
		self.gun.bulletbox.bullet_count += bullet_num
		print('你本次新加了{}发子弹,剩余的子弹总数是{}发'.format(bullet_num,self.gun.bulletbox.bullet_count))
		
	def fire(self,fire_count):
		self.gun.shoot(fire_count)










