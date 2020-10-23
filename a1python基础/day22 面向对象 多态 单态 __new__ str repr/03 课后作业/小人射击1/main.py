# ### 小人射击
# """面向对象的核心思想: 把对象当做程序的最小单元,让对象去操作一切   """

# 需求分析: 
	# 弹匣类:  bulletbox
		# 属性: bulletcount  #子弹数量  init参数
		# 方法: 无

	# 枪类:    gun
		# 属性: 弹匣对象  #init参数
		# 方法: 射击-shoot

	# 人类:    person
		# 属性: 枪对象
		# 方法: 1.射击,  2.换子弹

# 导入弹匣类 , 枪类  , 人类
# from 文件夹.py文件 import 类
# 当前的main.py和文件夹package是同级
from package.bulletbox import BulletBox
from package.gun import Gun
from package.person import Person

# 创建一个弹匣对象
danxia = BulletBox(10)  #初始10发子弹
# print(danxia)
#<package.bulletbox.BulletBox object at 0x7f7b4303cb00>

# 创建一个枪对象
xdq1887 = Gun(danxia)

# 创建一个人对象
kangyukang = Person(xdq1887)

if __name__ == '__main__':  #这行下面的代码,只能本文件作为运行入口,才能执行
# 本文件如果被别的模块导入,这行下面的代码是不会执行的
	# 开枪发射
	kangyukang.fire(5)  #一次发射5发子弹
	#发射子弹5发 剩余的子弹数量是5

	# 上子弹
	kangyukang.fill(3)  #新加3发子弹
	#新加了3发子弹,目前的子弹总数是8
	
	# 开枪发射
	kangyukang.fire(7)
	# 发射子弹7发 剩余的子弹数量是1





































