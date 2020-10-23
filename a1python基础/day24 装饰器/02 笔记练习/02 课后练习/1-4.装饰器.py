# (7) 带有参数的函数装饰器
def outer(num):
	def kuozhan(_func):
		def newfunc1(self):
			print(self)
			print('前 ... 老实巴交')
			_func(self)
			print('后 ... 浑身哆嗦')
			
		def newfunc2(self):
			print(self)
			print('前 ... 狂送人头')
			_func(self)
			print('后 ... 让二追三')
			
		if num == 1:
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return '洗洗手'
			
	return kuozhan
	
class MyClass():
	
	@outer(1)   #func1 = outer(1)(func1)
	# func1 = kuozhan(func1)
	# func1 = newfunc1
	# func1() = newfunc1()
	def func1(self):
		print('向前一小步')
		
	@outer(2)
	def func2(self):
		print('打包')
		
	@outer(3)
	def func3(self):
		print('瞄准')
	
obj = MyClass()
obj.func1()
# 前 ... 老实巴交
# 向前一小步
# 后 ... 浑身哆嗦

print(obj.func3)
#洗洗手
print('----------------------1')


# (7) 带有参数的函数装饰器2
def outer(num):
	def kuozhan(_func):
		def newfunc1(self):
			print('前 ... 老实巴交')
			_func(self)
			print('后 ... 浑身哆嗦')
			
		def newfunc2(self):
			print('前 ... 狂送人头')
			_func(self)
			print('后 ... 让二追三')
			
		if num == 1:
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return '洗洗手'		
		
	return kuozhan

class MyClass():
	
	@outer(1)
	def func1(self):
		print('文明')

	@outer(2)
	def func2(self):
		print('打包')
		
	@outer(3)
	def func3(self):
		print('瞄准')

obj = MyClass()
obj.func1()
print(obj.func3)
print('----------------------2')

# (7) 带有参数的函数装饰器3
def outer(num):
	def kuozhan(_func):
		def newfunc1(self):
			print('前 ... 老实巴交')
			_func(self)
			print('后 ... 浑身哆嗦')
			
		def newfunc2(self):
			print('前 ... 狂送人头')
			_func(self)
			print('后 ... 让二追三')
		
	return kuozhan


# (8) 带有参数的类装饰器1
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性

class Kuozhan():
	
	ad = '百岁山'
	
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		# print(cls)
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)
			
	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc1():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls() #对象
		return newfunc1
			
	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc2():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc2

@Kuozhan(2)
# MyClass = Kuozhan(2)(MyClass)
# MyClass = newfunc2
# MyClass() = newfunc2()
class MyClass():
	def run():
		return "亢龙有悔"

#方法2
obj = MyClass()
print(obj.run)  #亢龙有悔
print('-------------------------------8-1')

#方式1
@Kuozhan(1)
# MyClass = Kuozhan(1)(MyClass)
# MyClass = newfunc1
# MyClass() = newfunc1()

class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.ad)
obj.money()
# 百岁山
# 包月1100
print('-------------------------------8-2')


# (8) 带有参数的类装饰器2
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def nuewfunc1():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls()
		return newfunc1

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc2():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()			
		return newfunc2

@Kuozhan(1)
class MyClass():
	def run():
		return '亢龙有悔'
		
obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return '亢龙有悔'
obj.MyClass()
print(obj.run)
print('-------------------------------2')

# (8) 带有参数的类装饰器3
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def nuewfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1)
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------3')


# (8) 带有参数的类装饰器4
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cl)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():	
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			retuen cls()
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls(0
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------4')

# (8) 带有参数的类装饰器5
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan(0:
	ad = '百岁山'
	
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elf self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def nuwfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls(0
		reurn newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return  newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------5')

# (8) 带有参数的类装饰器6
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls()
		return newfun

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------6')

# (8) 带有参数的类装饰器7
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性

class Kuozhan():
	ad = '百岁山'
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls()
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------7')

# (8) 带有参数的类装饰器8
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性

class Kuozhan():
	ad = '百岁山'
	def money(self):	
		print('包月1100')
	
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)

	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls()
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:	
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------8')


# (8) 带有参数的类装饰器9
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)
			
	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money
			return cls()
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
print('-------------------------------9')


# (8) 带有参数的类装饰器10
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
class Kuozhan():
	ad = '百岁山'
	def money(self):
		print('包月1100')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)
			
	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			cls.ad = Kuozhan.ad
			cls.monwy = Kuozhan.money
			return cls()
		return newfunc

	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run()
				return cls()
		return newfunc

@Kuozhan(1) 
class MyClass():
	def run():
		return "亢龙有悔"

obj = MyClass()
print(obj.ad)
obj.money()

@Kuozhan(2)
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)
























