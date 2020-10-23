# ### 装饰器 : 在不改变原有代码的前提下,为原函数扩展新功能
# """
# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器(闭包的外函数)
	# (2) 把返回的新函数去替换原函数
# """

# 装饰器的重点:抓定义的2句话
# @outer 把这行转换成下面行 不跳步骤
	# func1 = outer(func1)

# (1) 装饰器的原型
def kuozhan(_func):  #定义装饰器(闭包的外函数)
	def newfunc():
		print('前 ... 干净整齐')
		_func()
		print("后 ... 酒气熏天")
	return newfunc
	
def func():
	print('我是hello..')

func = kuozhan(func)  #func = newfunc   func() <==> newfunc()
func()  #调用装饰器
# 前 ... 干净整齐
# 我是hello..
# 后 ... 酒气熏天

# (2) @符号的使用
print("<=======================> 1")
def kuozhan(_func):
	def newfunc():
		print('前 ... 干净整齐')
		_func()
		print("后 ... 酒气熏天")
	return newfunc

@kuozhan    #等价于 func = kuozhan(func)
def func():
	print('我是高富帅...')

func()
print("<=======================> 2")

# (3) 装饰器的嵌套
def kuozhan1(_func):
	def newfunc():
		print("前 ... 人模狗样1")
		_func()		
		print("后 ... 牛头马面2")
	return newfunc

def kuozhan2(_func):
	def newfunc2():
		print("前 ... 面黄肌瘦3")
		_func()	  #1 5 2	
		print("后 ... 红光满面4")
	return newfunc2

@kuozhan2
@kuozhan1   #定义装饰器
def func():  #从下往上调用
	print('我是白富美...5')

func()

# 代码解析
# func() ==> kuozhan1中的  newfunc()  # 152 
# kuozhan1中的  newfunc()   ==> kuozhan2中的  newfunc2() #31524

# ### 装饰器 : 在不改变原有代码的前提下,为原函数扩展新功能
# """
# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器(闭包的外函数)
	# (2) 把返回的新函数去替换原函数
# """

# 31524
# 前 ... 面黄肌瘦3
# 前 ... 人模狗样1
# 我是白富美...5
# 后 ... 牛头马面2
# 后 ... 红光满面4

# (4) 带有参数的装饰器
# """原函数和新函数的参数和返回值要保持一一对应"""
# 原函数有参数,新函数就有参数
# 原函数有返回值,新函数就有返回值
print("<===================> 4")
def kuozhan(_func):
	def newfunc(who,where,eat):
		print("前 ... 文质彬彬")
		_func(who,where,eat)
		print("后 ... 兽性大发")
	return newfunc
	
@kuozhan  #定义装饰器
def func(who,where,eat):	
	print('{who}在{where}吃{eat}'.format(who=who,where=where,eat=eat))

func("假率先","浴缸","榴莲") #   <==> newfunc()
# 前 ... 文质彬彬
# 假率先在浴缸吃榴莲
# 后 ... 兽性大发

# (5) 带有参数返回值的装饰器
print("<=====>  5-1")

def kuozhan(_func):
	def newfunc(*args,**kwargs):  #函数定义
		print("手工耿同学向下面的同学们致敬 ~")
		res = _func(*args,**kwargs)  #函数调用
		print("请使用我的自动称重器 ... ")
		return res
	return newfunc
	
@kuozhan        #定义装饰器
def func(*args,**kwargs):  #替换字典的键 (班长和班花的题)
	dic = {"liuwenbo":"刘文波","zhanglei":"张磊","songjian":"宋健"}
	lst = []
	
	try:
		i = 0
		for k,v in kwargs.items():
			# 键在dic中,再去拼凑字符串
			if k in dic:
				# 人名 + 地点 + 重量
				strvar = dic[k]+args[i]+v
				lst.append(strvar)
				i += 1
	except:
		# print(i) #2
		# print(list(dic.values())) #['刘文波', '张磊', '宋健']
		# print(list(dic.values())[i]) #宋健
		print('{}找不到地方'.format(list(dic.values())[i]))
		
	return lst
	# ['刘文波电线杆子下面15吨', '张磊电影院15斤', '宋健电梯里15克']

# 调用装饰器		
# res = func("电线杆子下面","电影院","电梯里",liuwenbo="15吨",zhanglei="15斤",songjian="15克")
res = func("电线杆子下面","电影院",liuwenbo="15吨",zhanglei="15斤",songjian="15克")
# IndexError: tuple index out of range
print(res)
# 手工耿同学向下面的同学们致敬 ~
# 请使用我的自动称重器 ... 
# ['刘文波电线杆子下面15吨', '张磊电影院15斤', '宋健电梯里15克']

# 手工耿同学向下面的同学们致敬 ~
# 宋健找不到地方
# 请使用我的自动称重器 ... 
# ['刘文波电线杆子下面15吨', '张磊电影院15斤']

# (6) 使用类装饰器
print("<=====>  6-1")
class Kuozhan():
	def __call__(self,_func):
		return self.kuozhan2(_func)
	
	def kuozhan1(func):
		def newfunc():
			print("前 ... 饥肠辘辘")
			func()
			print("后 ...  酒足饭饱")
		return newfunc
		
	def kuozhan2(self,func):
		def newfunc():
			print("前 ... 蓬头垢面")
			func()
			print("后 ... 衣衫褴褛")
		return newfunc

# 方式一
@Kuozhan.kuozhan1   #类名.方法   (不需要传self)  #定义装饰器函数 不执行
def func():
	print('进行时 ....')

func()  #调装饰器函数

# 前 ... 饥肠辘辘
# 进行时 ....
# 后 ...  酒足饭饱

print("<=====>  6-2")
# 方式二
@Kuozhan()   #@obj  @对象  
# func = Kuozan()(func)   
# func = obj(func)
# func = newfunc      
# func() = newfunc()   
def func():
	print('进行时 ....')

func()
# 前 ... 蓬头垢面
# 进行时 ....
# 后 ... 衣衫褴褛

# (7) 带有参数的函数装饰器
def outer(num):  #闭包
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
			
		if num == 1:
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return 'hello'		
	return kuozhan
	
class MyClass():
	@outer(1)   
	# func1 = outer(1)(func1)
	
	# func1 = kuozhan(func1)
	# func1 = newfunc1	

	def func1(self):
		print('进步')
		
	@outer(2)
	# @kuozhan
	# func2 = kuozhan(func2)
	# func2 = newfunnc2
	def func2(self):
		print('打包')
		
	@outer(3)
	def func3(self):
		print('瞄准')

print("<==============>7")

obj = MyClass()
obj.func1()
# obj.newfunc1()
# newfunc1(self)

# <__main__.MyClass object at 0x7f42b16d7278>
# 前 ... 老实巴交
# 进步
# 后 ... 浑身哆嗦

	# (1) 自动把下面修饰的原函数当成参数传递给装饰器
	# (2) 把返回的新函数去替换原函数

# 装饰器的重点:抓定义的2句话
# @outer 把这行转换成下面行 不跳步骤
	# func1 = outer(func1)

print("<==============>7-2")
obj.func2()
# obj.newfunc2()
# newfunc2(self)

# 前 ... 狂送人头
# 打包
# 后 ... 让二追三

print("<==============>7-3")
print(obj.func3)

# (8) 带有参数的类装饰器
# """
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
# """

class Kuozhan():
	ad = '百岁山'
	
	def money(self):
		print('包月1100,一小时200元')
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):  #obj()的时候触发调用
		print(cls) #MyClass
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)
		
	# 参数1的情况 : 给修饰的类 添加成员属性和方法
	def kuozhan1(self,cls):  #cls 是MyClass
		def newfunc():
			#MyClass.ad = '百岁山'
			cls.ad = Kuozhan.ad  #'百岁山'
			cls.money = Kuozhan.money
			print(cls) #<class '__main__.MyClass'>
			print(cls.__dict__) 
			#'ad': '百岁山', 'money': <function Kuozhan.money at 0x7f938da41620>}
			return cls()  #对象		
		return newfunc
	
	# 参数2的情况 : 把类中的run方法变成属性;
	def kuozhan2(self,cls):
		def newfunc():
			if 'run' in cls.__dict__:
				cls.run = cls.run() #'亢龙有悔'
				return cls()	#对象		
		return newfunc
		
print("<==================>8-1")
# 方式一
@Kuozhan(1)
# MyClass = obj(MyClass)
# MyClass = newfunc   #类变成了一个函数(闭包函数) 299行
# MyClass() = newfunc()
# MyClass() = cls()
class MyClass():
	def run():
		return '亢龙有悔'

obj = MyClass()
print(obj.ad)   #百岁山
obj.money() #包月1100,一小时200元
# print(obj.__dict__) #{}
# print(MyClass.__dict__)#{}
# MyClass这个类在全局空间已经不存在了.变成了一个函数  330 331行
# 但是MyClass在局部空间还是存在的  303 304行
# MyClass在全局和局部各有一份 完全独立

#不给类加装饰器 会报错
#AttributeError: 'MyClass' object has no attribute 'ad'

print("<==================>8-2")
# 方式二
@Kuozhan(2)
# @obj 
# MyClass = obj(MyClass)  # obj(MyClass)会触发call
# MyClass = self.kuozhan2(cls)  
# MyClass = newfunc  #类变成了函数(闭包函数)   315行
# MyClass() = newfunc()
# MyClass() = cls()   #cls.run = cls.run() #'亢龙有悔'  cls是MyClass在313行
class MyClass():
	def run():
		return '亢龙有悔'
obj = MyClass()
print(obj.run) #亢龙有悔
print(obj.__dict__) #{}
print(MyClass.__dict__)#{}

print("<==================>9")
# 虽然MyClass2这个名字替换掉了,但是内存中的该类仍然存在;
class MyClass2():
	a = 200	
print(id(MyClass2),'11111111111')
#20993640 11111111111

def func(cls):
	cls.ad = 90
	print(id(cls),'22222222222')
	#20993640 11111111111
	return cls() #对象
obj = func(MyClass2)

MyClass2 = 100 #全局空间,MyClass2这个类没有了,变成了100
print(MyClass2) #100
print(obj.a) # 200
print(obj.ad) #90



























