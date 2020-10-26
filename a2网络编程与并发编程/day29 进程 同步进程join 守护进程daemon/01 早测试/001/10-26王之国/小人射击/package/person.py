# 定义士兵类

class Person():

	def __init__(self,gun):
		self.gun = gun

	def fill(self,bulletnum):
		self.gun.bulletbox.bulletboxcount += bulletnum
		print("装弹成功,剩余{}发".format(self.gun.bulletbox.bulletboxcount))

	def fire(self,fcount):
		self.gun.shoot(fcount)