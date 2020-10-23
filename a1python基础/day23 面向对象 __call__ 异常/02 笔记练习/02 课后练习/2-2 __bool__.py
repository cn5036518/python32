# ### __bool__ 魔术方法
	# 触发时机：使用bool(对象)的时候自动触发
	# 功能：强转对象
	# 参数：一个self接受当前对象
	# 返回值：必须是布尔类型

# 类似的还有如下等等(了解):
	# __complex__(self)      被complex强转对象时调用
	# __int__(self)          被int强转对象时调用
	# __float__(self)        被float强转对象时调用

class MyClass():
	def __bool__(self):
		return True
obj = MyClass()
print(bool(obj)) #True


#__add__ 魔术方法  (与之相关的__radd__ 反向加法)
# '''
	# 触发时机：使用对象进行运算相加的时候自动触发
	# 功能：对象运算
	# 参数：二个对象参数
	# 返回值：运算后的值

# 类似的还有如下等等(了解):
	# __sub__(self, other)           定义减法的行为：-
	# __mul__(self, other)           定义乘法的行为：
	# __truediv__(self, other)       定义真除法的行为：/

class MyClass():
	def __init__(self,num):
		self.num = num
		
	## 当对象在 + 号的左侧时,自动触发
	def __add__(self,other):
		print(self) #<__main__.MyClass object at 0x7f1e62df04e0>
		print(other) #1
		return self.num * 3 + other  #3*3+1=10
		
	## 当对象在 + 号的右侧时,自动触发
	def __radd__(self,other):
		print(self) #<__main__.MyClass object at 0x7f4ae7f18518>
		print(other) #7
		return self.num * 5 + other #5*5+7=32

# add的触发方式
a = MyClass(3)
res = a + 1
print(res)  #10

# radd的触发方式
b = MyClass(5)
res = 7 + b
print(res) #32

# 对象 + 对象
res = a + b
print(res) #34
# add
# self.num * 3 + other  a.num * 3 + b  3 * 3 + b  9+b  res = 9+b
# radd
# self.num * 5 + other  b.num*5 + 9 = 5*5 +9 =34  res =34

# ### __len__ 魔术方法
	# 触发时机：使用len(对象)的时候自动触发 
	# 功能：用于检测对象中或者类中某个内容的个数
	# 参数：一个self接受当前对象
	# 返回值：必须返回整型

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
		return len([i for i in MyClass.__dict__ if not (i.startswith('__') and i.endswith('__'))])

obj = MyClass()
print(len(obj)) #6

# 代码原型;
print(MyClass.__dict__)
#{'__module__': '__main__', 'pty1': 1, 'pty2': 2, '_MyClass__pty3': 3}
lst = []
for i in MyClass.__dict__:
	# print(i)
	if not (i.startswith('__') and i.endswith('__')):
		lst.append(i)
print(lst)	
#['pty1', 'pty2', '_MyClass__pty3', 'func1', 'func2', '_MyClass__func3']
print(len(lst)) #6
























































