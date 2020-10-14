# ### 面向对象的封装 - 类的操作

# 使用方式:
	# 类.成员属性
	# 类.成员方法

class MyCar():
	# 公有成员属性  
	platenum = '京A7758BB'
	
	# 私有成员属性
	__earning = '月收入6000'
	
	# 公有成员方法
	def car_info():
		print('牌照信息可以公开')
	
	# 私有成员方法
	def __money_info():
		print('收入信息保密')

	def get_private(): #获取私有成员
		MyCar.__money_info()  
		print(MyCar.__earning)


# (1)定义的类访问公有成员属性和方法  类访问公有成员属性和方法
print(MyCar.platenum)  #京A7758BB
MyCar.car_info() #牌照信息可以公开

# 02类访问公有成员属性和方法  类通过公有方法访问私有成员
MyCar.get_private()
# 收入信息保密
# 月收入6000

# (2)定义的类动态添加公有成员属性   类添加公有成员属性
MyCar.logo = '特斯拉'
print(MyCar.logo)  #特斯拉
print(MyCar.__dict__)

# (3)定义的类动态添加公有成员方法    类添加公有成员方法
# 先定义函数,再类添加公有成员方法
# 1.无参方法  车灯
def func1():
	print('我是造车灯的方法')
MyCar.func1 = func1
MyCar.func1() #我是造车灯的方法	

# 2.有参方法  发动机牌子
def func2(name):
	print('我是{}发动机'.format(name))
MyCar.func2 = func2
MyCar.func2('三缸') #我是三缸发动机

# 3.lambda表达式  轮胎
func3 = lambda :print('这是造轮胎的方法')
MyCar.func3 = func3
MyCar.func3() #这是造轮胎的方法

# 对比 对象和类之间的不同
# 1.类中的无参方法默认只能类来调用,对象无法调取
# 2.对象可以调用类中的成员,反过来,类不能调用对象中的成员
# 3.每创建一个对象都会在内存中占用一份空间,对象之间是彼此独立的;
obj = MyCar()
# obj.car_info()
#TypeError: car_info() takes 0 positional arguments but 1 was given
MyCar.car_info()
#牌照信息可以公开
# 1.类中的无参方法默认只能类来调用,对象无法调取

obj.price = '10万'
# print(MyCar.price)
#AttributeError: type object 'MyCar' has no attribute 'price'
# 2.对象可以调用类中的成员,反过来,类不能调用对象中的成员























