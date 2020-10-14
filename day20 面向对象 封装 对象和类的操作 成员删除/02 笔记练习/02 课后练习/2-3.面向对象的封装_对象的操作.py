# ### 面向对象的封装 - 对象的操作

# 封装:
	# 1.私有 : 在类内可以互相访问,在类外不能访问
	# 2.公有 : 在类内或者类外都可以访问

# 类中成员:
	# 1.成员属性
	# 2.成员方法
	
# 绑定方法:
	# 1.绑定到对象 : 当对象去调用类中成员方法时,系统会默认把该对象当成参数传递给该方法
	# 2.绑定到类   : 当对象或者类去调用类中成员方法时,
	# 系统会默认把该类当成参数传递给该方法

# 使用方式:
	# 对象.成员属性
	# 对象.成员方法
	
class MyCar():
	# 公有属性
	logo = '布加迪威龙'
	
	# 私有属性
	__price = '2000万'
	
	# 公有方法
	def run(self):
		print('百公里油耗300L,logo={},price={}'.format(self.logo,self.__price))

	# 私有方法
	def __info(self):
		print('车主信息保密,据说是某个房地产大佬的儿子')
		
	# 获取私有成员
	def get_private(self):
		self.__info()
		
obj = MyCar()

# (1)实例化的对象访问成员属性和方法
# 公有
# 01 成员属性
print(obj.logo)  #布加迪威龙

# 02 成员方法
obj.run()  #百公里油耗300L,logo=布加迪威龙,price=2000万

# 私有(私有成员无法在类外直接访问,类内可以)
# 01 成员属性
# 通过公有成员方法. 间接访问私有成员属性  (2000万就是私有成员属性)
obj.run()  #百公里油耗300L,logo=布加迪威龙,price=2000万

# 02 成员方法
obj.get_private()
#车主信息保密,据说是某个房地产大佬的儿子

#(2)实例化的对象动态添加公有成员属性   对象添加公有成员属性
# 私有成员属性只能在类中添加,类外无法添加
obj.color = 'yellow'
print(obj.color)  #yellow
print(obj.__dict__)  #{'color': 'yellow'}
print('--------------------------2 对象添加公有成员属性')

#(3)实例化的对象动态添加公有成员方法   对象添加公有成员方法
# 私有成员方法只能在类中添加,类外无法添加
# 1.无参方法
def func():
	print('我是汽车人函数')
obj.func = func
obj.func()  #我是汽车人函数

# 2.有参方法
# 01 基本版
def func2(name):
	print('我是汽车人函数2 {}'.format(name))
obj.func2 = func2
obj.func2('擎天柱')#我是汽车人函数2 擎天柱

# 02 升级版  手动传递对象
def func3(obj,name):
	print('我是汽车人函数3 {},我的颜色是{}'.format(name,obj.color))  #obj的好处是可以用的color属性
obj.func3 = func3
obj.func3(obj,'擎天柱3') #我是汽车人函数3 擎天柱3,我的颜色是yellow

# 03 终极版  自动传递对象
import types
def func4(obj,name):
	print('我是汽车人函数4 {},我的颜色是{}'.format(name,obj.color))
obj.func4 = types.MethodType(func4,obj)
obj.func4('擎天柱4') #我是汽车人函数4 擎天柱4,我的颜色是yellow

# 3.lambda表达式
func5 = lambda :print('我是威震天')
obj.func5 = func5
obj.func5()  #我是威震天

func6 = lambda n:print('我是威震天 {}'.format(n))
obj.func6 = func6
obj.func6('擎天柱5') #我是威震天 擎天柱5
print(obj.__dict__)





































