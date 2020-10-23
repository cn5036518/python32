# ###小人射击小程序
# 机枪扫射声中我们寻找遮蔽的战壕
# 儿时沙雕的城堡毁坏了重新盖就好
# 可是你那沾染血布满弹孔的军外套
# 却就连祷告手都举不好
# 此时,战士拿起了手中的枪,面对敌人的枪火,奋勇射击，
# 突突突的子弹声响彻整个峡谷

# 用面向对象的思想完成该程序,要求:
# (1)子弹可以装载到弹匣中
# (2)弹夹可以装载到枪支中
# (3)人具有拿枪射击的功能,也可以换子弹



# 子弹-->  弹夹-->  枪支-->  人   类   继承关系
# 拿枪射击  换子弹-->  人的方法

class Person():
	def shoot(self):  #拿枪射击
		print('拿枪射击')
	def bullet_replace(self): #换子弹
		print('我可以{},也可以{}'.format(self.bullet_load(),self.clip_load()))
		# 我可以把子弹装载到弹夹,也可以把弹夹装载到枪支中	
	
class Gun(Person):
	def clip_load(self):
		return '把弹夹装载到枪支中'
	
class clip(Gun):	#弹夹
	def bullet_load(self): #子弹
		return '把子弹装载到弹夹'
		
obj = clip()
obj.shoot()
obj.bullet_replace()		
		
# 拿枪射击
# 我可以把子弹装载到弹夹,也可以把弹夹装载到枪支中	
		
		
		
		
		
		
		



















