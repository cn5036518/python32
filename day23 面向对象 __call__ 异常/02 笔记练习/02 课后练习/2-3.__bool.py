# ### 1 __bool__ 魔术方法   __init__   __float__   __complex__

# 触发时机：使用bool(对象)的时候自动触发
# 功能：强转对象  (把obj对象转换成bool)
# 参数：一个self接受当前对象
# 返回值：必须是布尔类型
# 应用:把对象obj转换成bool int float 复数 

# 类似的还有如下等等(了解):
	# __complex__(self)      被complex强转对象时调用   (把obj对象转换成复数)
	# __int__(self)          被int强转对象时调用		(把obj对象转换成int)
	# __float__(self)        被float强转对象时调用      (把obj对象转换成float)

class Car():
	def __bool__(self):
		return True
	
obj = Car()
res = bool(obj)  #
print(res)  #True


#2 __add__ 魔术方法  (与之相关的__radd__ 反向加法)      __sub__    __mul__     __truediv__
# 触发时机：使用对象进行运算相加的时候自动触发
# 功能：对象运算
# 参数：二个对象参数
# 返回值：运算后的值
# 应用:对象obj进行运算+ - * /

# 类似的还有如下等等(了解):
	# __sub__(self, other)           定义减法的行为：-
	# __mul__(self, other)           定义乘法的行为：
	# __truediv__(self, other)       定义真除法的行为：/

class Car():
	def __init__(self,num):
		self.num = num
	
	# 对象obj在加号的左边
	def __add__(self,other):
		return self.num + other
		
	# 对象obj在加号的右边
	def __radd__(self,other):
		return self.num + other
		
obj = Car(3)
res = obj + 1  #self.num是3  other 是1   调的是__add__
print(res)   #4

obj = Car(5)
res = 3 + obj  #调的是__radd__    #self.num是5 other是3
print(res)   #8

# 两个对象想加
obj1 = Car(7)   #先调的是__add__   			 self.num是7  other是obj2    return   7+obj2
obj2 = Car(8)   #7+obj2  再调的是__radd__    self.num是8  other是7		 return   15
res = obj1 + obj2
print(res)  #15


# ### __len__ 魔术方法
# '''
	# 触发时机：使用len(对象)的时候自动触发 
	# 功能：用于检测对象中或者类中某个内容的个数
	# 参数：一个self接受当前对象
	# 返回值：必须返回整型
# '''

# len(对象) => 类中的所有自定义成员
class MyClass():
	pty1 = 1
	pty2 = 2 
	__pty3 = 3
	
	def func1():
		pass
	def func2():
		pass
	def __func3():
		pass
		
	def __len__(self):
		dic = MyClass.__dict__
		lst = []
		for i in dic:
			if  not (i.startswith("__") and i.endswith("__")):
				lst.append(i)
		print(lst) #['pty1', 'pty2', '_MyClass__pty3', 'func1', 'func2', '_MyClass__func3']
		return len(lst) #6

# print(MyClass.__dict__)
# print(len(MyClass.__dict__)) #11
print('-------------------------------3-1')
# {'__module__': '__main__',
 # 'pty1': 1,
 # 'pty2': 2, 
 # '_MyClass__pty3': 3,
 # 'func1': <function MyClass.func1 at 0x7f8db58d0378>, 
 # 'func2': <function MyClass.func2 at 0x7f8db58d0400>, 
 # '_MyClass__func3': <function MyClass.__func3 at 0x7f8db58d0488>, 
 # '__dict__': <attribute '__dict__' of 'MyClass' objects>,
 # '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
 # '__doc__': None}

obj = MyClass()
print(len(obj)) #6

class MyClass():
	pty1 = 1
	pty2 = 2 
	__pty3 = 3
	
	def func1():
		pass
	def func2():
		pass
	def __func3():
		pass
		
	def __len__(self):
		lst = self.len1()  #用self调成员方法
		return len(lst) #6
		
	def len1(self):
		dic = MyClass.__dict__
		lst = []
		for i in dic:
			if  not (i.startswith("__") and i.endswith("__")):
				lst.append(i)
		return lst

obj = MyClass()
print(len(obj))  #7   新增了一个成员 len1
print('-------------------------------3-2')

class MyClass():
	pty1 = 1
	pty2 = 2 
	__pty3 = 3
	
	def func1():
		pass
	def func2():
		pass
	def __func3():
		pass
		
	def __len__(self):
		lst = [i for i in MyClass.__dict__ if  not (i.startswith("__") and i.endswith("__"))]
		return len(lst) #6
		
obj = MyClass()
print(len(obj))  #6
print('-------------------------------3-3 列表推导式')





















