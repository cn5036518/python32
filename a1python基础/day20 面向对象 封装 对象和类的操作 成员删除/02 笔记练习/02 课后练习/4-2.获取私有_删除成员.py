# ### 1.如何在类外访问私有成员

class Plane():
	# # 公有成员
	captain = '赵沈阳'
	
	# 私有成员
	__air_sister = '3名空姐'
	
	# 公有绑定方法
	def fly(self):
		print('飞机要在平流层,才能减少震动',self.__air_sister)

	# 私有绑定方法
	def __age(self):
		print('空姐年龄保密')

	# 公有无参方法--非绑定 只能类调用
	def fly2():
		print('航天飞机飞到天空层,翱翔太空')

	# 私有无参方法
	def __earn():
		print('机长的收入保密')
		
	def pub_get1(self):# 对象通过公有绑定方法获取私有绑定方法
		print(self.__air_sister)
		self.__age()
		
	def pub_get2(): #类通过公有非绑定方法获取私有非绑定方法
		print(Plane.__air_sister)
		Plane.__earn()

# 实例化对象 新建对象
obj = Plane()


# 方法一.访问私有成员 (不推荐)  #目前对于私有成员,采用的是_类__私有成员的改名策略
print(obj._Plane__air_sister)  #3名空姐
print(Plane.__dict__)

# 方法二.访问私有成员 (使用类中的公有方法,间接访问私有成员) (推荐)
obj.pub_get1()
# 3名空姐
# 空姐年龄保密

# ### 2.使用类对象删除相应的成员
# """
# 1.对象可以访问类中的公有成员,但是无权修改或者删除该类中的成员  (有使用权,无所有权)
# 2.对象在访问成员时,优先访问该对象自己的成员,如果没有再访问类的,类如果也没有直接报错;
# """

# 01 删除对象成员属性
obj.captain = '赵世超'
print(obj.__dict__) #{'captain': '赵世超'}
del obj.captain
print(obj.__dict__)  #{}
print(obj.captain) #赵沈阳
# 小结:对象在访问成员时,优先访问该对象自己的成员,如果没有再访问类的,类如果也没有直接报错;

# 02 删除对象成员方法
obj.basketball = lambda :print('打篮球')
print(obj.__dict__) #{'basketball': <function <lambda> at 0x7fc3a7b75e18>}
del obj.basketball
print(obj.__dict__) #{}

# 03 删除类中成员属性
print(Plane.__dict__)
del Plane.captain
print(Plane.__dict__)
obj.captain = '赵世超'
print(obj.captain)
print('---------------1')
#通过类删除类的成员(属性,方法)后,不影响对象的成员,即类和对象的成员是相互独立的

# del obj.captain  #AttributeError: captain
# 对象可以访问类中的公有成员,但是无权修改或者删除该类中的成员  (有使用权,无所有权)

# 04 删除类中成员方法
print(Plane.__dict__)
# del Plane.fly
print(Plane.__dict__)

# del obj.fly  #AttributeError: fly

# 注意: 对象无法调无参方法!! 
# 反过来,类可以调用对象的绑定方法么? 可以!!
Plane.fly(obj)
#飞机要在平流层,才能减少震动 3名空姐


#小结
# 一 获取私有成员
# 1 不推荐使用obj._类__私有成员获取私有成员
# 2 推荐obj通过公有方法,获取私有成员

# 二 删除成员
# 1 对象obj只能访问类的成员,但是无权修改和删除类的成员
# 2 通过obj删除对象的成员(属性,方法)后,对象会访问类的成员,如果类中也没有,就报错
# 3 通过类删除类的成员(属性,方法)后,不影响对象的成员,即类和对象的成员是相互独立的
















