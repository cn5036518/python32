class Gun():
	def __init__(self,bulletbox): #弹夹对象
		self.bulletbox = bulletbox
		
	def shoot(self,shoot_num):
		if self.bulletbox.bullet_count < shoot_num:
			print('子弹不够了,需要加子弹')
		else:
			self.bulletbox.bullet_count -= shoot_num
			print('你本次发射了{}发子弹,剩余的子弹总数是{}发'.format(shoot_num,self.bulletbox.bullet_count))












