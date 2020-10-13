# ### 面向对象的封装 - 对象的操作

# 封装:
	# 公有:类的内外都可以访问
	# 私有:类的内部可以访问,类的外部无法访问

# 类中成员:
	# 成员属性-类外变量
	# 成员方法-类外函数

# 绑定方法:
	# 绑定对象到方法  self 对象调
		# 当对象去调类中的成员方法时,系统会自动把对象作为实参传递给成员方法,成员方法用形参self接收对象obj
	# 绑定类到方法

# 使用方式:
# 对象.成员属性
# 对象.成员方法

class Car():
	# 公有属性
	name = '特斯拉'
	
	# 私有属性
	__price = '200万'
	
	# 公有绑定方法 self 对象调
	# def run():
	def run(self):
		print('汽车会跑')
		
	# 私有绑定方法
	def __info_owner(self):
		print('车主的信息保密')
		
	# # 公有绑定方法2
	def get_private(self):  #获取私有成员(私有属性和私有方法)
		print(self.__price)
		self.__info_owner()
		
obj = Car()


# (1)实例化的对象访问成员属性和方法
# 01公有
# 001 成员属性
print(obj.name)  #特斯拉

# 002 成员方法
obj.run()  #汽车会跑

# 02私有
# 001 成员属性
# print(obj.__price) #报错
#AttributeError: 'Car' object has no attribute '__price'

obj.get_private()    #获取到了私有成员(通过公有成员)
#200万
#车主的信息保密

# 002 成员方法
# obj.__info_owner() #报错
#AttributeError: 'Car' object has no attribute '__info_owner'
print(obj.__dict__)  #{} 说明对象obj中没有成员
print('----------------------1 对象访问成员属性和方法')

#(2)实例化的对象动态添加公有成员属性
# 私有的成员属性只能在类中添加.不能在类外添加
obj.color = '黄色' #该成员属性属于obj,不属于类Car
print(obj.color) #黄色

obj.name = '法拉利'
print(obj.name) #法拉利

# 小结:对象优先使用自己的成员属性,如果没有,就使用类的成员属性,如果还没有,就报错
# __dict__ 获取类对象的内部成员
#1 获取对象的内部成员
print(obj.__dict__)  #{'color': '黄色', 'name': '法拉利'}

#2 获取类的内部成员
print(Car.__dict__)
#{'__module__': '__main__',
 # 'name': '特斯拉',
 # '_Car__price': '200万',
 # 'run': <function Car.run at 0x7efc63985158>, 
 # '_Car__info_owner': <function Car.__info_owner at 0x7efc639851e0>, 
 # 'get_private': <function Car.get_private at 0x7efc63985268>, 
 # '__dict__': <attribute '__dict__' of 'Car' objects>, 
 # '__weakref__': <attribute '__weakref__' of 'Car' objects>,
 # '__doc__': None}
print('----------------------2 对象添加公有成员属性')

#(3)实例化的对象动态添加公有成员方法
# 私有的成员方法只能在类中添加.不能在类外添加
# 1.无参方法  
# 思路: 先定义函数,然后添加
def func():
	print('我是汽车人无参函数')
	
#对象.方法 = 函数   #方法名约定俗成 和函数名保持一致
obj.func = func
obj.func()
print(obj.__dict__)
#{'color': '黄色', 'name': '法拉利', 'func': <function func at 0x7f99fcf34e18>}
print('----------------------3-1 对象添加公有成员方法')

# 2.有参方法
# 思路: 先定义函数,然后添加
# 基本版
def func2(name): #形参
	print('我是汽车人有参函数{}'.format(name))
#对象.方法 = 函数   #方法名约定俗成 和函数名保持一致
obj.func2 = func2
obj.func2('擎天柱') #实参
#我是汽车人有参函数擎天柱
print(obj.__dict__)
#{'color': '黄色', 'name': '法拉利', 'func': <function func at 0x7fb2e10a2e18>, 'func2': <function func2 at 0x7fb2e0fc22f0>}
print('----------------------3-2-1 对象添加公有成员方法')

# 升级版
def func3(obj,name): #形参
	print('我是汽车人有参函数{},我的颜色是{}'.format(name,obj.color))  #obj.color是新增的成员属性

#对象.方法 = 函数   #方法名约定俗成 和函数名保持一致
obj.func3 = func3
obj.func3(obj,'擎天柱2') #实参
#我是汽车人有参函数擎天柱2,我的颜色是黄色
print('----------------------3-2-2 对象添加公有成员方法')

# 终极版
import types
def func4(obj,name): 
	print("我是汽车人有参函数{},我的颜色是{}".format(name,obj.color))

# obj.func4 = func4
obj.func4 = types.MethodType(func4,obj) #参数1是函数 参数2是对象
# 转换后 等号右边的func4是函数 等号左边的func4是方法 方法会自动把对象obj传入,而不需要手动传obj了
obj.func4('擎天柱4') #参数1obj自动传了. 只需要传name参数即可
# 我是汽车人有参函数擎天柱4,我的颜色是黄色
   #TypeError: func4() missing 1 required positional argument: 'name'
# obj.func4(obj,'擎天柱4')
print(obj.__dict__)
# {'color': '黄色', 
# 'name': '法拉利',
 # 'func': <function func at 0x7ff1da427e18>,
 # 'func2': <function func2 at 0x7ff1da3472f0>, 
 # 'func3': <function func3 at 0x7ff1da347378>, 
 # 'func4': <bound method func4 of <__main__.Car object at 0x7ff1da3586d8>>}
print('----------------------3-2-3 对象添加公有成员方法')

# 3.lambda表达式
func5 = lambda :print('我是威震天')
obj.func5 = func5
obj.func5()
#我是威震天

#小结
# 1对象访问成员属性和成员方法
# 2对象动态添加公有成员属性
# 3对象动态添加公有成员方法


# 1对象访问成员属性和成员方法
class Car():
	#公有属性
	name = '特斯拉'
	
	#私有属性
	__price = '200万'
	
	# 公有绑定方法 self 对象调
	def run(self):
		print('汽车会跑')
		
	# 私有绑定方法
	def __info_owner(self):
		print('车主的信息保密')
		
	# 获取私有成员
	def get_private(self):
		print(self.__price)
		self.__info_owner()
		
obj = Car()

# 公有
# 01 公有属性
print(obj.name) #特斯拉

# 02 公有方法
obj.run() #汽车会跑

# 私有
# 01 私有属性  通过公有方法实现
obj.get_private()
# 200万
# 车主的信息保密

# 02 私有方法
print('-------------------1对象访问成员属性和成员方法')

# 2对象动态添加公有成员属性
# 私有成员属性只能在类中添加.无法通过对象在类外添加
obj.color = '黄色'
print(obj.color) #黄色
print(obj.__dict__) #打印对象或者类的成员 返回是字典
#{'color': '黄色'}
print('汽车的名字是{},颜色是{}'.format(obj.name,obj.color))
#汽车的名字是特斯拉,颜色是黄色   #这里的name就有取的类的成员属性

# 小结:对象优先使用自己的成员属性,如果没有,就使用类的成员属性,如果还没有,就报错
print('-------------------2对象动态添加公有成员属性')

# 3对象动态添加成员方法
# 无参
def func():
	print('我是汽车人函数')
	
obj.func = func
obj.func()  #我是汽车人函数
print('-------------------3-1 对象动态添加成员方法')

# 有参
# 基本版  参数不含对象
def func2(name):
	print('我是汽车人函数{}'.format(name))
obj.func2 = func2
obj.func2('擎天柱') #我是汽车人函数擎天柱
print('-------------------3-2-1 对象动态添加成员方法')

# 升级版 参数含有对象 手动传对象
def func3(obj,name):  #这里的obj不一定必须放在第一个位置
	print('我是汽车人函数{},我的颜色是{}'.format(name,obj.color))
obj.func3 = func3
obj.func3(obj,'擎天柱') #我是汽车人函数擎天柱,我的颜色是黄色
print('-------------------3-2-2 对象动态添加成员方法')

# 终极版  参数含有对象 自动传对象
import types
def func3(obj,name):  #
	print('我是汽车人函数{},我的颜色是{}'.format(name,obj.color))
obj.func3 = types.MethodType(func3,obj)
# 系统自动把obj对象作为参数传递,实参处就不用手动传递了
obj.func3('擎天柱2') #我是汽车人函数擎天柱2,我的颜色是黄色
print(obj.__dict__)
#{'color': '黄色',
 # 'func': <function func at 0x7f7fb69ab598>, 
# 'func2': <function func2 at 0x7f7fb69ab7b8>, 
# 'func3': <bound method func3 of <__main__.Car object at 0x7f7fb858cb00>>}
print(Car.__dict__)
print('-------------------3-2-3 对象动态添加成员方法')














































