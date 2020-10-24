class Gun():
	def __init__(self,bulletbox):
		self.bulletbox = bulletbox  #子弹对象
		
	def shoot(self,firecount):	
		#剩余子弹数 = 子弹总数 - 已发射子弹数
		#剩余子弹数 = self.bulletbox.bulletcount - firecount
	
		if firecount <= self.bulletbox.bulletcount:  #
			self.bulletbox.bulletcount -= firecount  #修改了子弹总数
			#(通过弹夹对象的子弹总数属性) -
			print('你本次发射了{}发子弹,剩余的子弹数是{}发'.format(firecount,self.bulletbox.bulletcount))
		else:
			print('子弹不够了,需要加子弹')
		
	
	
	
	
	








































