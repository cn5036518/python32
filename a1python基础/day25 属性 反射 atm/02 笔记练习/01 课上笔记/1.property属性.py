# ### property 
# """
# 可以把方法变成属性 : 可以动态的控制属性的获取,设置,删除相关操作
# @property  获取属性
# @方法名.setter  设置属性
# @方法名.deleter 删除属性
# """

# 方法一
# """是同一个方法名 不同的装饰器"""
class MyClass():
	
	def __init__(self,name):
		self.name = name
		
	@property    #username = property(username)
	def username(self):
		return self.name
		# pass
		
	@username.setter    #username = username.setter(username)
	def username(self,val):
		# print(val)
		self.name = val
		pass

	@username.deleter   #username = username.deleter(username)
	def username(self):
		# print("222")
		del self.name
		pass

obj = MyClass("小红")
# 获取值的时候自动触发@property 装饰器下的方法
res = obj.username  #把方法变成属性
print(res)  #小红

# 设置值的时候自动触发@username.setter 装饰器下的方法
obj.username1 = "小兰"  #给属性设置值
print(obj.username)  #小兰

# 删除值的时候自动触发@username.deleter 装饰器下的方法
# del obj.username
# print(obj.username)


# 方法二   不同的方法名  不用装饰器
class MyClass():

	def __init__(self,name):
		self.name = name
		
	# 获取数据
	def get_username(self):
		return self.name
	
	# 设置数据
	def set_username(self,val):
		self.name = val
	
	# 删除数据
	def del_username(self):
		del self.name
		
	# 参数的顺序: 获取 , 设置  , 删除
	username = property(get_username , set_username  , del_username )
	# username = property(set_username,get_username , del_username )
	##把方法变成属性
		


obj = MyClass("小芳")
# 获取值的时候,执行get_username下的相关操作
print(obj.username)  #小芳   #把方法变成属性

# 设置值的时候,执行 set_username 下的相关操作
obj.username = "11223344"
print(obj.username) #11223344   #给属性设置值

# 删除值的时候,执行 del_username 下的相关操作
# del obj.username
# print(obj.username)






