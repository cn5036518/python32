# ### 面向对象的封装 - 类的操作
# """
# 使用方式:
	# 类.成员属性
	# 类.成员方法
# """

class MyCar():
	# 公有成员属性
	platenum = '京A7758BB'
	
	# 私有成员属性
	__earning = '月收入6000'
	
	# 公有成员方法
	def car_info():
		print('牌照信息可以公开')
		# print('------------1')
		# MyCar.__money_info() #收入信息保密 月收入6000
		
	# 私有成员方法
	def __money_info():
		print('收入信息保密',MyCar.__earning)
		
obj = MyCar()


# (1)定义的类访问公有成员属性和方法
print(MyCar.platenum) #京A7758BB
MyCar.car_info() #牌照信息可以公开

# (2)定义的类动态添加公有成员属性
# 私有成员属性只能在类中添加,类外不能添加
MyCar.oil = '100L'
print(MyCar.oil) #100L
print(MyCar.__dict__)

# (3)定义的类动态添加公有成员方法
# 私有成员方法只能在类中添加,类外不能添加
# 思路:先定义函数,后添加成员方法

# 01 无参  车灯
def func():
	print('我是造车灯的函数')
	
MyCar.func = func
MyCar.func() #我是造车灯的函数

# 02 有参  发动机牌子
def func2(name):
	print('我是{}发动机函数'.format(name))
	
MyCar.func2 = func2
MyCar.func2('三缸') #我是三缸发动机函数


# 03  lambda表达式  轮胎
func3 = lambda :print('我是造轮胎的方法')
MyCar.func3 = func3
MyCar.func3() #我是造轮胎的方法
print(MyCar.__dict__)

# 对象和类的操作的不同
# 1 类中的无参方法只能是类来调用,对象无法调用
# 2 对象可以调用类的成员,反过来,类不能调对象的成员
# 3 每创建一个对象,空间都是独立的

# 1 类中的无参方法只能是类来调用,对象无法调用
# obj.car_info() 报错
#TypeError: car_info() takes 0 positional arguments but 1 was given
MyCar.car_info()
#牌照信息可以公开

# 2 对象可以调用类的成员,反过来,类不能调对象的成员
obj.oil2 = '101L'
# print(MyCar.oil2)
#AttributeError: type object 'MyCar' has no attribute 'oil2'
print(obj.oil2) #101L





























