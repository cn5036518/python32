# ### 1.如何在类外访问私有成员

class Plane():
	# 公有成员
	captain = '赵沈阳'
	
	# 私有成员
	__air_sister = '3名空姐'
	
	# 公有绑定方法 self
	def fly(self):
		print('飞机要在平流层,才能减少震动',self.__air_sister) #私有成员
		
	# 私有绑定方法 self 
	def __age(self):
		print('空姐年龄保密')
		
	# 公有无参方法  类来调
	def fly2():
		print('航天飞机飞到天空层,翱翔太空')
	
	# 私有无参方法  
	def __earn():
		print('机长的收入保密')
		
	def pub_get1(self):
		print(self.__air_sister)  #对象获取私有成员
		self.__age()  #对象调私有绑定方法

	def pub_get2():
		print(Plane.__air_sister)  #类获取私有成员
		Plane.__earn() #类调私有无参方法

# 实例化对象 新建对象
obj = Plane()

# 方法一.访问私有成员 (不推荐)
# python私有化: 采取了改名策略 =>  _类名 + __air_sister
# _类名 + 私有成员名
# print(obj.__air_sister)
#AttributeError: 'Plane' object has no attribute '__air_sister'
print(obj._Plane__air_sister) #3名空姐  # _类名 + 私有成员名
print(Plane.__dict__) #获取类或者对象的成员
# {'__module__': '__main__', 
# 'captain': '赵沈阳', 
# '_Plane__air_sister': '3名空姐', 
# 'fly': <function Plane.fly at 0x7f86335b3158>, 
# '_Plane__age': <function Plane.__age at 0x7f86335b31e0>,
 # 'fly2': <function Plane.fly2 at 0x7f86335b3268>,
 # '_Plane__earn': <function Plane.__earn at 0x7f86335b32f0>, 
 # 'pub_get1': <function Plane.pub_get1 at 0x7f86335b3378>, 
 # 'pub_get2': <function Plane.pub_get2 at 0x7f86335b3400>,
 # '__dict__': <attribute '__dict__' of 'Plane' objects>, 
 # '__weakref__': <attribute '__weakref__' of 'Plane' objects>,
 # '__doc__': None}

# 方法二.访问私有成员 (使用类中的公有方法,间接访问私有成员) (推荐)
obj = Plane()
obj.pub_get1()  #对象调绑定方法 self
# 3名空姐
# 空姐年龄保密
Plane.pub_get2() #类调非绑定方法 没有self 包含无参
# 3名空姐
# 机长的收入保密

# ### 2.使用类对象删除相应的成员
# 1.对象可以访问类中的公有成员,但是无权修改或者删除该类中的成员
#   对象有使用权,没有所有权
# 2.对象在访问成员时,优先访问该对象自己的成员,
# 如果没有在访问类的,类如果也没有直接报错;

# 01 删除对象成员属性
obj.captain = '赵世超'
del obj.captain
print(obj.captain)#赵沈阳 对象的成员属性被输出了,就找类的成员属性

# 02 删除对象成员方法
obj.basketball = lambda : print('我的私人飞机可以在天上打篮球')
print(obj.__dict__) #{'basketball': <function <lambda> at 0x7fef56f18e18>}
obj.basketball() #我的私人飞机可以在天上打篮球
del obj.basketball
print(obj.__dict__) #{}
# obj.basketball() error
#AttributeError: 'Plane' object has no attribute 'basketball'

# 03 删除类中成员属性
# del Plane.captain
# print(Plane.__dict__)
# {'__module__': '__main__',
 # '_Plane__air_sister': '3名空姐', 
 # 'fly': <function Plane.fly at 0x7f9c6dd84158>, 
 # '_Plane__age': <function Plane.__age at 0x7f9c6dd841e0>,
 # 'fly2': <function Plane.fly2 at 0x7f9c6dd84268>, 
 # '_Plane__earn': <function Plane.__earn at 0x7f9c6dd842f0>,
 # 'pub_get1': <function Plane.pub_get1 at 0x7f9c6dd84378>, 
 # 'pub_get2': <function Plane.pub_get2 at 0x7f9c6dd84400>,
 # '__dict__': <attribute '__dict__' of 'Plane' objects>,
 # '__weakref__': <attribute '__weakref__' of 'Plane' objects>,
 # '__doc__': None}

# Plane.captain
#AttributeError: type object 'Plane' has no attribute 'captain'
# print(obj.captain)
#AttributeError: 'Plane' object has no attribute 'captain'

# 04 删除类中成员方法
del Plane.fly2
# Plane.fly2()  #error
#AttributeError: type object 'Plane' has no attribute 'fly2'

# 注意: 对象无法调无参方法!! 
# 反回来,类可以调用对象的绑定方法么? 可以!!(参数是对象即可)
# Plane.fly()  error
#TypeError: fly() missing 1 required positional argument: 'self'
Plane.fly(obj) #飞机要在平流层,才能减少震动 3名空姐
























