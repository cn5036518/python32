# 单态模式:
# 概念:同一个类,无论实例化多少次,都只有一个对象
# 目的:节省内存空间(每新建一个对象都会占用内存空间)
# 应用:只需要单纯调用类的成员,而不需要给当前对象添加成员的场景

# 写法:
class Singleton():
	__obj = None
	
	def __new__(cls):
		if cls._obj is None:
			cls._obj = object.__new__(cls)
		return cls._obj

# 第一次新建对象的时候,cls._obj is None成立,
# 返回 cls._obj = object.__new__(cls)

# 第二次新建对象的时候,cls._obj is None不成立,
# return cls._obj 还是返回第一次新建的对象

# 以后每次新建都是第一次新建的对象

class Singleton():
	__obj = None
	
	def __new__(cls,*args,**kwargs):
		if cls.__obj is None:
			cls.__obj = object.__new__(cls)
		return cls.__obj
		
	def __init__(self,name):
		self.name = name

obj1 = Singleton('jack')		
obj2 = Singleton('tom')		
print(obj1)
print(obj2)
print(obj1.name) #tom  obj1和obj2 对象是同一个 打印了2次
print(obj2.name) #tom
































