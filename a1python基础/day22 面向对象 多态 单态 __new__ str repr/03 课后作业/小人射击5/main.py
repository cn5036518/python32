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

#新建对象
bulletbox = Bulletbox(10)

gun = Gun(bulletbox)  #参数是弹夹对象

person = Person(gun) #参数是枪对象


if __name__ == "__main__":
	# gun.shoot(2)
	person.fire(3)
	person.fill(4)
	person.fire(2)
	person.fill(3)


# 子弹的初始个数是10发
# 本次发射了3发子弹,剩余子弹总数是7发
# 本次新加了4发子弹,剩余子弹总数是11发
# 本次发射了2发子弹,剩余子弹总数是9发
# 本次新加了3发子弹,剩余子弹总数是12发
















