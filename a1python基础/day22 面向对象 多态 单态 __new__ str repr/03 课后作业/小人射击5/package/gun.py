class Gun():
	def __init__(self,bulletbox):  #弹夹对象
		self.bulletbox = bulletbox
		
	def shoot(self,firecount):  #参数是每次发射的子弹数
		if self.bulletbox.bulletcount < firecount:
			print('子弹不够了,要加子弹')
		else:
			self.bulletbox.bulletcount -= firecount
			print('本次发射了{}发子弹,剩余子弹总数是{}发'.format(firecount,self.bulletbox.bulletcount))
			
	
	
	
	








































