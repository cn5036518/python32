# ### 枪类

	# 弹匣类:  bulletbox
		# 属性: bulletcount  #子弹数量  init参数
		# 方法: 无

	# 枪类:    gun
		# 属性: 弹匣对象  #init参数
		# 方法: 射击-shoot
		
class Gun():
	def __init__(self,bulletbox):
		self.bulletbox = bulletbox
		
	# 射击方法
	def shoot(self,firecount):  #firecount  每次开枪发出的子弹数
		# 剩余数量 = 总数量 - 射出的数量
		# 比如:子弹总数是100发,每次开10发  第一次后 剩余90发 第二次后,剩余80发  递减
		# self.bulletbox.bulletcount = self.bulletbox.bulletcount - firecount
		#self.bulletbox.bulletcount 是连贯操作
		# 通过弹夹对象调子弹数量的属性
		
		if self.bulletbox.bulletcount < firecount:
			print('你需要上子弹')
		else:
			self.bulletbox.bulletcount -= firecount  #bulletbox 的u写成了o
			print('发射子弹{}发'.format(firecount),
			'剩余的子弹数量是{}'.format(self.bulletbox.bulletcount))

			# self.bulletbox.bulletcount = self.bulletbox.bulletcount - firecount

# ak47 = Gun()
# ak47         突突突突突突  
# 加特林      哒哒哒
# 1887霰弹枪  "蹦ong!!"
















































