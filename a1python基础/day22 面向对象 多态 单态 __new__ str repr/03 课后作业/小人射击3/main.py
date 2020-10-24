# ### 小人射击
# """面向对象的核心思想: 把对象当做程序的最小单元,让对象去操作一切   """

# 需求分析: 
	# 弹匣类:  bulletbox
		# 属性: bulletcount   子弹数 init参数
		# 方法: 无

	# 枪类:    gun
		# 属性: 弹匣对象   init参数
		# 方法: 射击-shoot

	# 人类:    person
		# 属性: 枪对象   init参数
		# 方法: 
		# 1.射击(减去子弹),  
		# 2.上子弹(增加子弹)

#导包
from package.bulletbox import Bulletbox
from package.gun import Gun
from package.person	 import  Person

#新建对象
#1 新建一个弹夹对象
bulletbox = Bulletbox(10)
print(bulletbox.bulletcount)  #10

#2 新建一个枪对象
gun = Gun(bulletbox)  #参数是弹夹对象
# gun.shoot(3)  #你剩余的子弹数是7发

#3 新建一个人对象
person = Person(gun)  #参数是枪对象


if __name__ == '__main__':
	person.fire(2)  #你剩余的子弹数是8发
	person.fill(3)  #你本次新加了3发子弹,剩余的子弹总数是11发
	person.fire(2)  #你剩余的子弹数是9发

























