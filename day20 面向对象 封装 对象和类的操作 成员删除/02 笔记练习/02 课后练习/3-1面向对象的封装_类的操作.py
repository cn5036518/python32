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
		print("<======>")
		MyCar.__money_info()  #类.私有方法
		
	# 私有成员方法
	def __money_info():
		print('收入信息保密',MyCar.__earning)

# (1)定义的类访问公有成员属性和方法   类访问成员属性和方法
print(MyCar.platenum) #京A7758BB
MyCar.car_info() #牌照信息可以公开

# MyCar.__money_info() #报错 error
#AttributeError: type object 'MyCar' has no attribute '__money_info'

# (2)定义的类动态添加公有成员属性  类添加成员属性
MyCar.oil = '1000L'
print(MyCar.oil)  #1000L
print(MyCar.__dict__)
#{'__module__': '__main__', 
# 'platenum': '京A7758BB', 
# '_MyCar__earning': '月收入6000', 
# 'car_info': <function MyCar.car_info at 0x7f0b18682158>,
 # '_MyCar__money_info': <function MyCar.__money_info at 0x7f0b186821e0>, 
 # '__dict__': <attribute '__dict__' of 'MyCar' objects>,
 # '__weakref__': <attribute '__weakref__' of 'MyCar' objects>,
 # '__doc__': None,
 # 'oil': '1000L'}

# (3)定义的类动态添加公有成员方法  类添加成员方法
# 1.无参方法
def car_light():
	print('我是造车灯的方法')
MyCar.car_light = car_light
# 类.方法 = 函数
MyCar.car_light()  
#我是造车灯的方法

# 2.有参方法
def car_engine(name):
	print('我是造{}发动机的方法'.format(name))
MyCar.car_engine = car_engine
MyCar.car_engine('三缸')
#我是造三缸发动机的方法

# 3.lambda表达式
MyCar.luntai = lambda : print('我是造轮胎的方法')
MyCar.luntai()
#我是造轮胎的方法

# 对比 对象和类之间的不同
# 1.类中的无参方法默认只能类来调用,对象无法调取
# 2.对象可以调用类中的成员,反过来,类不能调用对象中的成员
# 3.每创建一个对象都会在内存中占用一份空间,对象之间是彼此独立的;

obj = MyCar()
# obj.car_info()
#TypeError: car_info() takes 0 positional arguments but 1 was given
MyCar.car_info()
#牌照信息可以公开

obj.price = '10万'
# print(MyCar.price) error  类不能调用对象中的成员
#AttributeError: type object 'MyCar' has no attribute 'price'



























