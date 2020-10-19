# ### 人类

	# 弹匣类:  bulletbox
		# 属性: bulletcount  #子弹数量  init参数
		# 方法: 无

	# 枪类:    gun
		# 属性: 弹匣对象  #init参数
		# 方法: 射击-shoot

	# 人类:    person
		# 属性: 枪对象  #init参数
		# 方法: 1.射击,  2.换子弹

class Person():
	def __init__(self,gun):  #gun对象作为参数 就可以得到枪对象的属性和方法
		self.gun = gun
		
	def fill(self,num):  #num是新加的子弹数
		# 找弹匣对象中的bulletcount属性填充子弹
		self.gun.bulletbox.bulletcount += num
		print('新加了{}发子弹,目前的子弹总数是{}'.
		format(num,self.gun.bulletbox.bulletcount))
		# 连贯操作
		# self.gun 枪对象
		# self.gun.bulletbox  枪对象的弹夹对象
		# self.gun.bulletbox.bulletcount  枪对象的弹夹对象的bulletcount属性
		
	def fire(self,fcount):
		self.gun.shoot(fcount)
		# 连贯操作
		# 用枪对象的shoot方法射击,参数是-每次开枪发出的子弹数

	
































