class Gun():
	def __init__(self,bulletbox):
		self.bulletbox = bulletbox   # 参数是弹夹对象
		
	def shoot(self,firecount):
		# 剩余子弹总数  = 初始子弹总数 - 已发射子弹总数
		if self.bulletbox.bulletcount < firecount:
			print('子弹不够了,需要加子弹')
		else:
			self.bulletbox.bulletcount -= firecount   #修改了弹夹对象的子弹总数属性
			print('你本次发射了{}发子弹,剩余{}发子弹'.format(firecount,self.bulletbox.bulletcount))
		
	
	
	
	
	








































