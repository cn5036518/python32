class Plane():
	# 公有成员
	captain = "赵沈阳"
	
	# 私有成员
	__air_sister = "3名空姐"
	
	# 公有绑定方法
	def fly(self):
		print("飞机要非要平流层,才能减少震动",self.__air_sister)
		
	# 私有绑定方法
	def __age(self):
		print("空姐年龄保密")
		
	# 公有无参方法
	def fly2():
		print("航天飞机飞到天空层,翱翔太空")
	
	# 私有无参方法
	def __earn():
		print("机长的收入保密")
		
	def pub_get1(self):
		print(self.__air_sister)
		self.__age()
		
	def pub_get2():
		print(Plane.__air_sister)
		Plane.__earn()
		
obj = Plane()

# 一 obj的操作		
# 1 obj获取成员属性和成员方法(obj优先获取自己的成员,如果没有,就获取类的成员,如果还没有,就报错)
# 01 公有
# 02 私有

# 2 obj添加自己的公有成员属性(私有成员只能在类里添加,无法在类外添加)
# 3 obj添加自己的公有成员方法
# 01 无参
# 02 有参
#    基础版
#    升级版
#    终极版
# 03 lambda

# 4 obj删除自己的成员属性和成员方法(obj无权修改或删除类的成员,只能获取类的成员)

# 二 类的操作
# 1 类获取自己的成员属性和成员方法(类不能获取obj的成员)
# 01 公有
# 02 私有

# 2 类添加自己的成员属性(类不能修改(添加)obj的成员)
# 3 类添加自己的成员方法
# 3 类删除自己的成员属性和成员方法

# 三 类和对象的关系
# 1.obj无权修改或删除类的成员,只能获取类的成员
# 2.类无权获取 修改或删除obj的成员(因为类和对象的内存是独立的)
print('---------------------------------------1')


# 一 obj的操作		
# 1 obj获取成员属性和成员方法(obj优先获取自己的成员,如果没有,就获取类的成员,如果还没有,就报错)
# 01 公有
# obj.captain = '赵世超'
# print(obj.captain)  #赵世超

print(obj.captain)  #赵沈阳

# 02 私有 
# 1 方法1  _类__私有成员  不推荐 
print(obj._Plane__air_sister)    #3名空姐
print(Plane._Plane__air_sister)  #3名空姐

# 2 方法2 推荐 通过公有方法获取私有成员
obj.pub_get1()
# 3名空姐
# 空姐年龄保密
print('-------------------2-2')

# 2 obj添加自己的公有成员属性(私有成员只能在类里添加,无法在类外添加)
obj.color = 'yellow'
print(obj.color)
print(obj.__dict__)  #{'color': 'yellow'}
print('-------------------2 obj添加自己的公有成员属性')

# 3 obj添加自己的公有成员方法
# 思路:先定义函数,然后添加
# 01 无参
def func1():
	print('我是飞机函数1')
obj.func1 = func1
obj.func1() #我是飞机函数1

# 02 有参
#    基础版
def func2(name):
	print('我是飞机函数2 {}'.format(name))
obj.func2 = func2
obj.func2('擎天柱2') #我是飞机函数2擎天柱2

#    升级版  手动传递obj
def func3(obj,name):
	print('我是飞机函数3 {},我的颜色是{}'.format(name,obj.color)) #对象的好处是可以获取对象中的其他属性obj.color
obj.func3 = func3
obj.func3(obj,'擎天柱3') #我是飞机函数2 擎天柱3,我的颜色是yellow

#    终极版  自动传递obj
import types
def func4(obj,name):
	print('我是飞机函数4 {},我的颜色是{}'.format(name,obj.color))
obj.func4 = types.MethodType(func4,obj)
obj.func4('擎天柱4') #我是飞机函数4 擎天柱4,我的颜色是yellow
# 只需要一个参数

# 03 lambda
func5 = lambda :print('威震天')
obj.func5 = func5
obj.func5()  #威震天
print(obj.__dict__)
#{'color': 'yellow', 'func1': <function func1 at 0x7f1f4a345e18>,
 # 'func2': <function func2 at 0x7f1f4a265488>, 
 # 'func3': <function func3 at 0x7f1f4a265510>, 
 # 'func4': <bound method func4 of <__main__.Plane object at 0x7f1f4a276940>>,
 # 'func5': <function <lambda> at 0x7f1f4868d730>}
print('-------------------3 obj添加自己的公有成员方法')


# 4 obj删除自己的成员属性和成员方法(obj无权修改或删除类的成员,只能获取类的成员)
del obj.color
del obj.func1
print(obj.__dict__)
# {'func2': <function func2 at 0x7fbdb780c488>,
 # 'func3': <function func3 at 0x7fbdb780c510>,
 # 'func4': <bound method func4 of <__main__.Plane object at 0x7fbdb781d940>>,
 # 'func5': <function <lambda> at 0x7fbdb5c34730>}
print('-------------------4 obj删除自己的成员属性和成员方法')

class Plane():
	# 公有成员
	captain = "赵沈阳"
	
	# 私有成员
	__air_sister = "3名空姐"
	
	# 公有绑定方法
	def fly(self):
		print("飞机要非要平流层,才能减少震动",self.__air_sister)
		
	# 私有绑定方法
	def __age(self):
		print("空姐年龄保密")
		
	# 公有无参方法
	def fly2():
		print("航天飞机飞到天空层,翱翔太空")
	
	# 私有无参方法
	def __earn():
		print("机长的收入保密")
		
	def pub_get1(self):  #获取私有绑定方法
		print(self.__air_sister)
		self.__age()
		
	def pub_get2(): #获取私有无参方法
		print(Plane.__air_sister)
		Plane.__earn()
		
obj = Plane()


# 二 类的操作
# 1 类获取自己的成员属性和成员方法(类不能获取obj的成员)
# 01 公有
# 成员属性
print(Plane.captain)  #赵沈阳
obj.captain2 = 'hah'
print(obj.captain2) #hah
# print(Plane.captain2)
#AttributeError: type object 'Plane' has no attribute 'captain2'
print('------------------1')

# 成员方法
Plane.fly2() #航天飞机飞到天空层,翱翔太空

# 02 私有
# 成员属性  不推荐
print(Plane._Plane__air_sister)  #3名空姐

# 成员方法
Plane.pub_get2()
#3名空姐
# 机长的收入保密

# 2 类添加自己的成员属性(类不能修改(添加)obj的成员)
Plane.color = 'red'
print(Plane.color) #red

# 3 类添加自己的成员方法
# 01 无参
def func11():
	print('我是飞机函数11')
Plane.func11 = func11
Plane.func11() #我是飞机函数11

# 02 有参
def func12(name):
	print('我是飞机函数12 {}'.format(name))
Plane.func12 = func12
Plane.func12('擎天柱12') #我是飞机函数12 擎天柱12

# 03 lambda
func13 = lambda :print('威震天2')
Plane.func13 = func13
Plane.func13() #威震天2
print(Plane.__dict__)

# 3 类删除自己的成员属性和成员方法
del Plane.color
del Plane.func13
print(Plane.__dict__)

# 三 类和对象的关系
# 1.obj无权修改或删除类的成员,只能获取类的成员
# 2.类无权获取 修改或删除obj的成员(因为类和对象的内存是独立的)













































