# ### 面向对象的封装 - 对象的操作

# 封装:
	# 1.私有 : 在类内可以互相访问,在类外不能访问
	# 2.公有 : 在类内或者类外都可以访问

# 类中成员:
	# 1.成员属性--变量(类外)
	# 2.成员方法--函数(类外)

# 绑定方法:
	# 1.绑定到对象 : 当对象去调用类中成员方法时,
	# 系统会默认把该对象当成参数传递给该方法
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

# 实例化对象(类的实例化) 新建对象
obj = MyCar()

# (1)实例化的对象访问成员属性和方法  对象访问属性和方法
# 01公有
# 公有属性
print(obj.logo) #布加迪威龙  
# 公有方法
obj.run() #百公里油耗300L,logo=布加迪威龙,price=2000万

# 02私有 (私有成员无法在类外访问,类内可以)
# obj.__price  #error
#AttributeError: 'MyCar' object has no attribute '__price'
# obj.__info() #error
#AttributeError: 'MyCar' object has no attribute '__info'


#(2)实例化的对象动态添加公有成员属性  对象添加成员属性
# 对象属性
obj.color = '黄色'
print(obj.color)  #黄色   

obj.logo = '五菱宏光'
print(obj.logo)  #五菱宏光
# 有对象属性,就取对象属性,没有就取类的成员属性

# __dict__ 获取类对象的内部成员
# 01 对象的内部成员
print(obj.__dict__)
#{'color': '黄色', 'logo': '五菱宏光'}

# 02 类的内部成员
print(MyCar.__dict__)
#{'__module__': '__main__', 
# 'logo': '布加迪威龙',
 # '_MyCar__price': '2000万', 
 # 'run': <function MyCar.run at 0x7f8f22bc4158>,
 # '_MyCar__info': <function MyCar.__info at 0x7f8f22bc41e0>,
 # '__dict__': <attribute '__dict__' of 'MyCar' objects>, 
 # '__weakref__': <attribute '__weakref__' of 'MyCar' objects>, 
 # '__doc__': None}


#(3)实例化的对象动态添加公有成员方法  对象添加成员方法

# 1.无参方法    对象添加成员方法-无参
def dahuangfeng():  #无参函数
	print('我是大黄蜂')

# 对象.方法 = 函数名   #定义方法
obj.dahuangfeng = dahuangfeng
# 等号右边是78行的函数名  
# 等号左边的dahuangfeng是自定义的,约定俗成和右边的函数名保持一致
obj.dahuangfeng() #我是大黄蜂
# 对象.方法()     #调用方法

# 2.有参方法     对象添加成员方法--有参
# 01基本版
def qingtianzhu(name):
	print('我是{}'.format(name))

# 对象.方法 = 函数  #从右往左看  方法名是自定义的,约定俗成,和函数名保持一致
obj.qingtianzhu = qingtianzhu
obj.qingtianzhu('擎天柱')
#我是擎天柱

# 02升级版
def qingtianzhu(obj,name):  #obj在这里不是必须放在第一个参数处的
# def qingtianzhu(name,obj):  #obj在这里不是必须放在第一个参数处的
	print('我是{},我的颜色是{}'.format(name,obj.color)) #对象.成员属性

print(type(qingtianzhu))  #<class 'function'>
# 对象.方法 = 函数  #从右往左看  方法名是自定义的,约定俗成,和函数名保持一致
obj.qingtianzhu = qingtianzhu
print('--------------1')

obj.qingtianzhu(obj,'擎天柱')
# obj.qingtianzhu('擎天柱',obj)
#我是擎天柱,我的颜色是黄色

# 03终极版
# """如果要创建绑定方法(带self),参数的顺序,self对象本身要放到第一位."""
def qingtianzhu(obj,name): #定义函数
	print('我是{},我的颜色是{}'.format(name,obj.color))

import types
# 创建绑定方法(带self),系统自动把该对象当成参数传递给方法;
# types.MethodType(方法,对象) => 绑定方法  
# types.MethodType(函数名,对象) ==> 绑定方法(带self)
res = types.MethodType(qingtianzhu,obj)  #这里的qingtianzhu是115行的函数名
print(res)
#<bound method qingtianzhu of <__main__.MyCar object at 0x7f8fe147fa58>>
print(type(res)) #<class 'method'>

# 对象.方法 = 方法  #从右往左看  方法名是自定义的,约定俗成,和函数名保持一致
obj.qingtianzhu = types.MethodType(qingtianzhu,obj)
# 解析:
# types.MethodType(qingtianzhu,obj)的类型是方法
# types.MethodType(qingtianzhu,obj)中的qingtianzhu的类型是函数
# 把函数qingtianzhu变成方法types.MethodType(qingtianzhu,obj),该方法自动把obj
# 当成参数传给等号左边的方法obj.qingtianzhu
obj.qingtianzhu('擎天柱') #会自动把obj当做第一个参数传递,类似下面行
# obj.qingtianzhu(obj,'擎天柱') #类似
# 我是擎天柱,我的颜色是黄色

#小结:
# 升级版 
# 形参 def qingtianzhu(obj,name):
# 实参 obj.qingtianzhu(obj,"擎天柱") 实参是2个参数

# 终极版:
# 形参 def qingtianzhu(obj,name):
# obj.qingtianzhu = types.MethodType(qingtianzhu,obj)
# 实参 obj.qingtianzhu("擎天柱") 实参是1个参数  多了上一行操作后
# types.MethodType(qingtianzhu,obj)的写法 参数1是函数名 参数2是对象名

# 3.lambda表达式
# 对象.方法 = 匿名函数
obj.weizhentian = lambda : print('我是威震天')
obj.weizhentian()
#我是威震天

















