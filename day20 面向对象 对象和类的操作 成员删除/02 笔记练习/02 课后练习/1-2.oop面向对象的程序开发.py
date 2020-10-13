# ### oop 面向对象的程序开发

# (1) 类的定义

# 1
class Car:
	pass
	
# 2  推荐 因为和def func() 写法一致.更方便理解记忆
class Car():
	pass
	
# 3 
class Car(object):
	pass

# (2)类的实例化   新建对象
obj = Car()
print(obj)


# (3)类的基本结构
# 成员属性  类外变量
# 成员方法  类外函数
class Car():
	# 成员属性
	name = '甜甜'
	
	# 成员方法
	# def run():  #非绑定
	def run(self): #绑定
		print('小猫会跑')

# 不要裸露的把判断和循环直接写在类中,而是用方法包起来
# 类的规范写法是:除了成员属性和成员方法外,没有别的.

# (4)类的命名
# 推荐用大驼峰
class MyCar():
	pass



#小结
# 1类的定义
class Car:
	pass
	
class Car(): #推荐
	pass
	
class Car(object):
	pass

# 2类的实例化(新建对象)
obj = Car()

# 3类的成员 
	# 成员属性--类外变量
	# 成员方法--类外函数
class Cat():
	# 成员属性
	name = '喵喵'
	
	# 成员方法
	# def run():
	def run(self):
		print('小猫会跑')

# 4类的命名  
	# MyCar 大驼峰

































