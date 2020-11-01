# ### property 
# """
# 可以把方法变成属性 : 可以动态的控制属性的获取,设置,删除相关操作
# @property  获取属性
# @方法名.setter  设置属性
# @方法名.deleter 删除属性
# """

# 方法一
# """是同一个方法名"""
class MyClass():
	def __init__(self,name):
		self.name = name
		
	def username(self):
		return self.name


obj = MyClass('小红')
res = obj.username
print(res)
#<bound method MyClass.username of <__main__.MyClass object at 0x7fc8816a2b00>>
print('--------------1-1')

# """是同一个方法名"""
class MyClass():
	def __init__(self,name):
		self.name = name
		
	@property  
	# username = property(username)
	# username = new_username   #定义装饰器
	# username() = new_username()  #调用装饰器
	def username(self):
		return self.name  #小红
		
	def username(self,val):
		# print(val)
		self.name = val


obj = MyClass('小红')
# 获取值的时候自动触发@property 装饰器下的方法
res = obj.username
print(res)  #小红
print('--------------1-2')









































