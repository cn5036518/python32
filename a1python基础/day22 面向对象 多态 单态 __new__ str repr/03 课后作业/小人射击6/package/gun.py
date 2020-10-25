class Gun():
	def __init__(self,bulletbox):  #弹夹对象
		self.bulletbox = bulletbox
		
	def shoot(self,count):#参数是每次发射子弹数
		if self.bulletbox.bulletcount >= count:
			self.bulletbox.bulletcount -= count
			print('本次发射了{}发子弹,剩余子弹总数是{}发'.format(count,self.bulletbox.bulletcount))
		else:
			print('子弹不够了,需要加子弹')













