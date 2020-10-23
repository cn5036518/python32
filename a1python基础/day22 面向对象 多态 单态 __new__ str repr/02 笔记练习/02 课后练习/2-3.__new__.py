# 功能  创建对象  
# 触发时机  新建对象的时候,在__init__之前执行                        
# 参数  至少是个cls
# 返回  对象或者None

# 注意点:
# 1 __new__  创建对象
  # __init__ 初始化对象
# 2 __new__在__init__之前执行
# 3 只有__new__返回本类对象的时候.init才会执行
  # 如果返回的是其他类的对象,或者返回None,init不会执行
# 4 __new__和构造方法的参数要一致
  # 推荐用__new__(cls,*args,**kwargs)
  
# 应用:单态

# 返回本类对象
# 返回其他类对象
# 返回None


# 1返回本类对象
class MyClass():
	def __new__(cls,*args,**kwargs):
	#          类.成员方法(cls)
		print(1)
		return object.__new__(cls)
		
	def __init__(self,name):
		print(2)
		self.name = name

obj = MyClass('jack')
print(obj) #<__main__.MyClass object at 0x7f4a6f1a4470>
# 1
# 2
print('----------------------1 返回本类对象')


# 2返回其他类对象
# 如果返回的是其他类的对象,或者返回None,init不会执行
class MyClass2():
	a = 10
obj2 = MyClass2()

class MyClass():
	def __new__(cls,*args,**kwargs):
		return obj2
		
	def __init(self):
		print(1)
		pass
		
obj1 = MyClass()
print(obj1)  #这里的obj1实际是obj2,即MyClass2的对象
#<__main__.MyClass2 object at 0x7f1dddcd56a0>

print('----------------------2 返回其他对象')



# 3返回None
# 如果返回的是其他类的对象,或者返回None,init不会执行
class MyClass():
	def __new__(cls,*args,**kwargs):
	#          类.成员方法(cls)
		print(1)
		
	def __init__(self,name):
		print(2)
		self.name = name
obj = MyClass('jack')
print(obj)
# 1
# None
print('----------------------3 返回None')
























