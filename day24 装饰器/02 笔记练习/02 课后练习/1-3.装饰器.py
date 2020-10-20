# ### 装饰器 : 在不改变原有代码的前提下,为原函数扩展新功能
# """
# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器
	# (2) 把返回的新函数去替换原函数
# """

# (1) 装饰器的原型
def kuozhan(_func):  #装饰器函数
	def newfunc():  #闭包函数
		print("前 ... 干净整齐")
		_func()
		print("后 ... 熏天")
	return newfunc

def func(): #被修饰的函数
	print('hello')

# 定义装饰器
func = kuozhan(func)
# func = newfunc
# 调用装饰器
func()
# func() <=> newfunc()

# 前 ... 干净整齐
# hello
# 后 ... 熏天
print('-----------------------1')

# (2) @符号的使用
def kuozhan(_func):  #装饰器函数
	def newfunc():  #闭包函数
		print("前 ... 干净整齐")
		_func()
		print("后 ... 熏天")
	return newfunc

@kuozhan  #定义装饰器
# func = kuozhan(func)
# func = newfunc
def func(): #被修饰的函数
	print('我是高富帅')

func()  #调用装饰器
# newfunc()  #调用装饰器


# 前 ... 干净整齐
# 我是高富帅
# 后 ... 熏天
print('-----------------------2')

# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器  @后面的就是装饰器
	# (2) 把返回的新函数去替换原函数

# (3) 装饰器的嵌套
def kuozhan1(_func):
	def newfunc11():
		print("前 ... 人模狗样1")
		_func()	 #5	
		print("后 ... 牛头马面2")
	return newfunc11

def kuozhan2(_func):
	def newfunc22():
		print("前 ... 面黄肌瘦3")
		_func()		 # 1 5 2
		# newfunc11()
		print("后 ... 红光满面4")
	return newfunc22

@kuozhan2  #定义装饰器   2个装饰器从下往上调
@kuozhan1

#第一层装饰器
# @kuozhan1
# func = kuozhan1(func)
# func = newfunc
# func() = newfunc11()  

# 前 ... 人模狗样1
# 我是白富美...5
# 后 ... 牛头马面2

#第2层装饰器
# @kuozhan2
# newfunc11 = kuozhan2(newfunc11)
# newfunc11 = newfunc22
# newfunc11() = newfunc22()

# 前 ... 面黄肌瘦3
# 前 ... 人模狗样1
# 我是白富美...5
# 后 ... 牛头马面2
# 后 ... 红光满面4

# newfunc11()

def func():
	print('我是白富美...5')
	
func() #调用装饰器

# 前 ... 面黄肌瘦3
# 前 ... 人模狗样1
# 我是白富美...5
# 后 ... 牛头马面2
# 后 ... 红光满面4
print('-----------------------3')

# (4) 带有参数的装饰器
# """原函数和新函数的参数和返回值要保持一一对应"""
def kuozhan(_func):
	def newfunc(who,where,eat):
		print("前 ... 文质彬彬")
		_func(who,where,eat)
		print("后 ... 大发")
	return newfunc

@kuozhan
# func = kuozhan(func)
# func = newfunc   #定义装饰器
def func(who,where,eat):
	print('{who}在{where}吃{eat}'.format(who=who,where=where,eat=eat))

func("假率先","浴缸","榴莲")
# newfunc("假率先","浴缸","榴莲")  #调用装饰器

# 前 ... 文质彬彬
# 假率先在浴缸吃榴莲
# 后 ... 大发
print('-----------------------4')


# (5) 带有参数返回值的装饰器
def kuozhan(_func):
	def newfunc(*args,**kwargs):
		print("手工耿同学向下面的同学们致敬 ~")
		res = _func(*args,**kwargs)
		print("请使用我的自动称重器 ... ")
		return res
	return newfunc

@kuozhan
# func = kuozhan(func)  定义装饰器
# func = newfunc
# func() = newfunc()  #调用装饰器
def func(*args,**kwargs):
	dic = {"liuwenbo":"刘文波","zhanglei":"张磊","songjian":"宋健"}
	lst = []
	try:
		i = 0
		for k,v in kwargs.items():  #替换键
			# 键在dic中,再去拼凑字符串
			if k in dic:
				# 人名 + 地点 + 重量
				strvar = dic[k] + args[i]+v
				lst.append(strvar)
				i += 1		
	except:
		# print(i)
		# print(list(dic.values()))
		# print(list(dic.values())[i])
		print('{}找不到地方'.format(list(dic.values())[i]))  #捕获报错
	return lst

res = func("电线杆子下面","电影院",liuwenbo="15吨",zhanglei="15斤",songjian="15克")
print(res)
# 手工耿同学向下面的同学们致敬 ~
# 宋健找不到地方
# 请使用我的自动称重器 ... 
# ['刘文波电线杆子下面15吨', '张磊电影院15斤']  
print('-----------------------5')


# (6) 使用类装饰器  
# 前面5个都是用闭包函数当做装饰器
class Kuozhan():
	def __call__(self,__func):
		return self.kuozhan2(__func)
		
	def kuozhan1(func):  #类调用
		def newfunc():#闭包函数
			print("前 ... 饥肠辘辘")
			func()
			print("后 ...  酒足饭饱")
		return newfunc
		
	def kuozhan2(self,func): #绑定方法
		def newfunc():
			print("前 ... 蓬头垢面")
			func()
			print("后 ... 衣衫褴褛")
		return newfunc

# 方式一
@Kuozhan.kuozhan1   #定义装饰器  @类.方法
# func = Kuozhan.kuozhan1(func)  #类名调非绑定方法
# func = newfunc
# func() = newfunc()
def func():
	print('进行时')

func()  #调用装饰器

# 前 ... 饥肠辘辘
# 进行时
# 后 ...  酒足饭饱
print('-----------------------6-1')

# 方式二
@Kuozhan()  #@obj   @类() @对象   用到call
# func = obj(func)   #obj() 会调用call
# func = self.kuozhan2(func)
# func = newfunc
# func() = newfunc()
def func():
	print('进行时2')
	
func()
print('-----------------------6-2')

# 前 ... 蓬头垢面
# 进行时2
# 后 ... 衣衫褴褛

# (7) 带有参数的函数装饰器
def outer(num):
	def kuozhan(_func):
		def newfunc1(self):
			print(self)
			print("前 ... 老实巴交")
			_func(self)
			print("后 ... 浑身哆嗦")
			
		def newfunc2(self):
			print(self)
			print("前 ... 狂送人头")
			_func(self)
			print("后 ... 让二追三")
			
		if num == 1:  #生命周期延长
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return '洗洗手'			
	return kuozhan

class MyClass():
	@outer(1)
	# @kuozhan
	# func1 = kuozhan(func1)
	# func1 = newfunc1  #定义装饰器
	# func1() = newfunc1()  #调用装饰器
	def func1(self):
		print('文明')
		
	# <__main__.MyClass object at 0x7f5c600a0400>
# 前 ... 老实巴交
# 文明
# 后 ... 浑身哆嗦
	
	@outer(2)
	# @kuozhan
	# func2 = kuozhan(func2)
	# func2 = newfunc2
	# func2() = newfunc2()
	def func2(self):
		print('打包')
# <__main__.MyClass object at 0x7f8ca11f2400>
# 前 ... 狂送人头
# 打包
# 后 ... 让二追三
		
	@outer(3)
	# @kuozhan
	# func3 = kuozhan(func3)
	# func3 = newfunc3
	def func3(self):
		print('瞄准')
		#洗洗手

obj = MyClass()
obj.func1()
print('------------------------7-1')

obj.func2()
print('------------------------7-2')

print(obj.func3)
# obj.func3()
print('------------------------7-3')






















































