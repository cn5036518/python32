# ### 装饰器 : 在不改变原有代码的前提下,为原函数扩展新功能
# """
# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器函数
	# (2) 把返回的新函数去替换原函数
# """

# (1) 装饰器的原型

#01装饰器函数
def kuozhan(_func):  #原函数当参数
	def newfunc():
		print("前 ... 干净整齐")
		_func()
		print("后 ... 气熏天")
	return newfunc  #返回新函数

#02原函数
def func():
	print("我是屌丝...")

#03定义装饰器
func = kuozhan(func) # func = newfunc   func() <=> newfunc()

#04调用装饰器
func()

# 前 ... 干净整齐
# 我是屌丝...
# 后 ... 气熏天


# (2) @符号的使用
print("<=======================>1")
def kuozhan(_func):
	def newfunc():
		print("前 ... 干净整齐")
		_func()		
		print("后 ... 气熏天")
	return newfunc
	
@kuozhan
# func = kuozhan(func)  #把原函数当成参数传递给装饰器函数
# func = newfunc        #把返回的新函数去替换原函数  定义装饰器
# func() = newfunc()    #调用装饰器
def func():
	print("我是高富帅...")

func()
# 前 ... 干净整齐
# 我是高富帅...
# 后 ... 气熏天
print("<=======================>2")

# (3) 装饰器的嵌套
def kuozhan1(_func):
	def newfunc():
		print("前 ... 人模狗样1")
		_func()	  #5	
		print("后 ... 牛头马面2")
	return newfunc

def kuozhan2(_func):
	def newfunc2():
		print("前 ... 面黄肌瘦3")
		_func()		# 1 5 2 
		print("后 ... 红光满面4")
	return newfunc2

@kuozhan2
@kuozhan1   #从内到外

# @kuozhan2
# func = kuozhan1(func1)
# func = newfunc
# func() = newfunc()

# newfunc() = kuozhan2(newfunc())
# newfunc() = newfunc2
# newfunc()() = newfunc2()
def func():
	print("我是白富美...5")

func()  # 3 1 5 2 4

# 前 ... 面黄肌瘦3
# 前 ... 人模狗样1
# 我是白富美...5
# 后 ... 牛头马面2
# 后 ... 红光满面4

print("<=======================>3")

# (4) 带有参数的装饰器
# """原函数和新函数的参数和返回值要保持一一对应"""
print("<===================>")

# 01 定义装饰器函数
def kuozhan(_func):
	def newfunc(who,where,eat):  #新函数3个形参 和原函数参数一致
		print("前 ... 文质彬彬")
		_func(who,where,eat)  #原函数3个实参
		print("后 ... 大发")
	return newfunc

# 02 给原函数加装饰器
@kuozhan
# func = kuozhan(func)  #把原函数当成参数传递给装饰器函数
# func = newfunc        #把返回的新函数去替换原函数  定义装饰器
# func() = newfunc()    #调用装饰器

# 03 定义原函数
def func(who,where,eat):  #原函数3个形参
	print("{who}在{where}吃{eat}".format(who=who,where=where,eat=eat)  )

# 04 调用加了装饰器的原函数	
func("假率先","浴缸","榴莲") # <=> newfunc()

# 前 ... 文质彬彬
# 假率先在浴缸吃榴莲
# 后 ... 大发

print("<=======================>4")



# (5) 带有参数返回值的装饰器

# 01 定义装饰器函数
def kuozhan(_func):
	def newfunc(*args,**kwargs):
		print("手工耿同学向下面的同学们致敬 ~")
		res = _func(*args,**kwargs)  # 原函数
		print("请使用我的自动称重器 ... ")
		return res  #原函数返回值
		
	return newfunc

# 02 给原函数加装饰器	
@kuozhan
# func = kuozhan(func)  #把原函数当成参数传递给装饰器函数
# func = newfunc        #把返回的新函数去替换原函数  定义装饰器
# func() = newfunc()    #调用装饰器

# 03 定义原函数
def func(*args,**kwargs):	
	dic = {"liuwenbo":"刘文波","zhanglei":"张磊","songjian":"宋健"}
	lst = []
	try:
		i = 0
		for k,v in kwargs.items():
			# 键在dic中,再去拼凑字符串
			if k in dic:
				# 人名 + 地点 + 拉的重量
				strvar  = dic[k] + "在" + args[i] + "搬了" + v
				lst.append(strvar)
				i += 1	
	except:
		# print(i) # 2
		# print(list(dic.values())) # ['刘文波', '张磊', '宋健']
		# print(list(dic.values())[i])  #宋健
		print("{}找不到地点而错,请传入他的地点".format(list(dic.values())[i]))		
		
	return lst	#原函数返回值
	# return ["刘文博在电线杆子下面搬了15吨" , "张磊搬了15斤","宋健搬了15克"]

# 04 调用加了装饰器的原函数
res = func("电线杆子下面","电影院",liuwenbo="15吨",zhanglei="15斤",songjian="15克")  #关键字参数
print(res)

# 手工耿同学向下面的同学们致敬 ~
# 宋健找不到地点而错,请传入他的地点
# 请使用我的自动称重器 ... 
# ['刘文波在电线杆子下面搬了15吨', '张磊在电影院搬了15斤']  #原函数返回值
print("<=======================>5")

# (6) 使用类装饰器

# 01 定义类装饰器
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
		def newfunc2():
			print("前 ... 蓬头垢面")
			func()
			print("后 ... 衣衫褴褛")
		return newfunc2

# 方式一
# 02 给原函数加类装饰器        函数装饰器写法  @函数名
#                                类装饰器写法  @类.方法
@Kuozhan.kuozhan1
# func = Kuozhan.kuozhan1(func)  #把原函数当成参数传递给装饰器类非绑定方法
# func = newfunc				#把返回的新函数去替换原函数  定义装饰器
# func() = newfunc()			#调用加了装饰器的原函数

# 03 定义原函数
def func():
	print("进行时 .... ")

# 04 调用加了装饰器的原函数
func()

# 前 ... 饥肠辘辘
# 进行时 .... 
# 后 ...  酒足饭饱

print("<===============6-1>")

# 方式二
@Kuozhan()   #先计算右边的     函数装饰器写法  @函数名
#                                类装饰器写法  @类()   即@obj  @对象  调__call__

# func = Kuozhan()(func)   #把原函数当成参数传递给装饰器类对象
# func = obj(func)  #对象()  调__call__
# func = self.kuozhan2(func)
# func = newfunc2			#把返回的新函数去替换原函数  定义装饰器
# func() = newfunc2()		#调用加了装饰器的原函数
def func():
	print("进行时 .... ")

func()

# 前 ... 蓬头垢面
# 进行时 .... 
# 后 ... 衣衫褴褛
print("<=======================>6-2")


# (7) 带有参数的函数装饰器
# 01 定义带有参数的函数装饰器  3层函数嵌套   (普通的函数装饰器是2层函数嵌套)
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
					
		if num == 1: 
			return newfunc1
		elif num == 2:
			return newfunc2
		elif num == 3:
			return "洗洗手"
		
	return kuozhan


class MyClass():
	
	# 02 给原方法加函数装饰器
	@outer(1)  # (1)@outer(1) => @kuozhan  (2)@kuozhan =>  func1 = newfunc1 => (3) obj.func1() <=> obj.newfunc1(self)
	# func1 = outer(1)(func1)   #把原函数当成参数传递给函数装饰器
	# func1 = kuozhan(func1)
	# func1 = newfunc1			#把返回的新函数去替换原函数  定义装饰器
	# func1() = newfunc1()		#调用加了装饰器的原函数
	
	# 03 原方法
	def func1(self):
		print("向前一小步")
		
	@outer(2)
	def func2(self):
		print("打包带走")

	@outer(3)
	def func3(self):
		print("请瞄准后发射")

print("<==============>7")
obj = MyClass()

# 04 调用加了装饰器的原方法
obj.func1() # <=> obj.newfunc1()

# <__main__.MyClass object at 0x7f026fb6abe0>
# 前 ... 老实巴交
# 向前一小步
# 后 ... 浑身哆嗦

print("<==============>7-2")
obj.func2()

# 前 ... 狂送人头
# 打包带走
# 后 ... 让二追三
print("<==============>7-3")
print(obj.func3)

# 洗洗手


# (8) 带有参数的类装饰器
# """
# 参数1: 给修饰的类添加成员属性和方法
# 参数2: 把类中的run方法变成属性
# """

# 01 定义带有参数的类装饰器
class Kuozhan():

	ad = "贵族茅台,茅台中的百岁山."
	
	def money(self):
		print("贵族茅台,包月1100,一小时200元")
		
	def __init__(self,num):
		self.num = num
		
	def __call__(self,cls):
		print(cls) # MyClass
		if self.num == 1:
			return self.kuozhan1(cls)
		elif self.num == 2:
			return self.kuozhan2(cls)
			
	# 参数1的情况 : 添加成员属性和方法
	def kuozhan1(self,cls):
		def newfunc():
			# MyClass.ad = "贵族茅厕,茅厕中的百岁山."
			cls.ad = Kuozhan.ad
			cls.money = Kuozhan.money  #添加成员属性和方法
			return cls()			
		return newfunc
		
	# 参数2的情况 : 把方法变成属性;
	def kuozhan2(self,cls):
		def newfunc2():
			if "run" in cls.__dict__:
				cls.run = cls.run()  #把方法变成属性
				return cls()
		return newfunc2
		

	
print("<==================>")
# 方式一
# """

# 02 给原类加类装饰器
@Kuozhan(1) # => @obj => MyClass = obj(MyClass)
# MyClass = Kuozhan(1)(Myclass)   #把原类当成参数传递给类装饰器
# MyClass = obj(Myclass)   #调__call__
# MyClass = self.kuozhan1(Myclass)  #
# MyClass = newfunc  #            #把返回的新函数去替换原类
# MyClass() = newfunc()

# 03 定义原类
class MyClass():
	def run():
		return "亢龙有悔"

# 04 调用加了装饰器的类的方法和属性
obj = MyClass()
print(obj.ad)  #贵族茅台,茅台中的百岁山.
obj.money()    #贵族茅台,包月1100,一小时200元
# 参数1: 给修饰的类添加成员属性和方法

# """
# 方式二
@Kuozhan(2)

# MyClass = Kuozhan(2)(Myclass)   #把原类当成参数传递给类装饰器
# MyClass = obj(Myclass)   #调__call__
# MyClass = self.kuozhan2(Myclass)
# MyClass = newfunc2  #            #把返回的新函数去替换原类
# MyClass() = newfunc2()
class MyClass():
	def run():
		return "亢龙有悔"
obj = MyClass()
print(obj.run)  #亢龙有悔
# 参数2: 把类中的run方法变成属性



# """
# (扩展)
# 虽然MyClass2这个名字替换掉了,但是内j存中的该类仍然存在;
# class MyClass2():
	# a = 200

# print(id(MyClass2) , "1111111")

# def func(cls):
	# cls.ad = 90
	# print(id(cls),"22222")
	# return cls()
# obj = func(MyClass2)

# MyClass2 = 100
# print(MyClass2)
# print(obj.a)  # 200 
# print(obj.ad) # 90
# """




















	