# ### 小人射击
# """面向对象的核心思想: 把对象当做程序的最小单元,让对象去操作一切   """

# 需求分析: 
	# 弹匣类:  bulletbox
		# 属性: bulletcount   子弹数 init参数
		# 方法: 无

	# 枪类:    gun
		# 属性: 弹匣对象   init参数
		# 方法: 射击-shoot(减去子弹总数)  通过枪对象 调方法shoot   通过弹夹对象修改子弹总数属性

	# 人类:    person
		# 属性: 枪对象   init参数
		# 方法: 
		# 1.射击(减去子弹),    通过枪对象 调方法shoot
		# 2.上子弹(增加子弹)   通过枪对象--弹夹对象修改子弹总数属性

#导包
from package.bulletbox import Bulletbox
from package.gun import Gun
from package.person import Person

# 新建对象
# 新建弹夹对象
bulletbox = Bulletbox(10)

# 新建枪对象
gun = Gun(bulletbox)  #参数是子弹对象
# gun.shoot(3)

# 新建人对象
person = Person(gun)


if __name__ == '__main__':
	# gun.shoot(3)
	person.fire(3)
	person.fill(4)
	

# 加子弹,在人类,通过枪对象-弹夹对象,修改子弹总数属性 +
# 开枪-减子弹
	# 在人类,通过枪对象-枪方法-弹夹对象,修改子弹总数属性























