# 1.请定义一个交通工具(Vehicle)的类，其中有:
# 属性：速度(公有speed)， 车的类型(私有type)
# 方法：速度(公有setSpeed)，加速(私有speedUp),减速(私有speedDown)
# 让公有setSpeed调用私有speedUp和私有speedDown

# 2.用类改写:猜数字游戏：
# 一个类有两个成员num和guess，
# num有一个初值100。
# 定义一个方法guess，
# 调用guess,如果大了则提示大了，小了则提示小了。等于则提示猜测成功。

# 3.创建一个圆Circle类。
# 为该类提供一个变量r表示半径
# 方法一返回圆的面积,方法二返回圆的周长；


# 1.请定义一个交通工具(Vehicle)的类，其中有:
# 属性：速度(公有speed)， 车的类型(私有type)
# 方法：速度(公有setSpeed)，加速(私有speedUp),减速(私有speedDown)
# 让公有setSpeed调用私有speedUp和私有speedDown
class Vehicle():
	# 公有属性
	speed = 80
	
	# 私有属性
	__type = '电动车'
	
	# 公有绑定方法
	def setSpeed(self):
		Vehicle.__speedUp()  #类.私有非绑定方法-无参
		Vehicle.__speedDown()
		
	# 私有非绑定方法-无参
	def __speedUp():
		print('加速')
		
	# 私有非绑定方法2-无参
	def __speedDown():
		print('减速')

v1 = Vehicle()
v1.setSpeed()
# 加速
# 减速
print('---------------1-1')

class Vehicle():
	# 公有属性
	speed = 80
	
	# 私有属性
	__type = '电动车'
	
	# 公有绑定方法
	def setSpeed(self):
		self.__speedUp()  #对象.私有绑定方法-无参
		self.__speedDown()
		
	# 私有绑定方法-无参
	def __speedUp(self):
		print('加速')
		
	# 私有绑定方法2-无参
	def __speedDown(self):
		print('减速')
v1 = Vehicle()
v1.setSpeed()
# 加速
# 减速
print('---------------1-2')


# 2.用类改写:猜数字游戏：
# 一个类有两个成员num和guess，
# num有一个初值100。
# 定义一个方法guess，
# 调用guess,如果大了则提示大了，小了则提示小了。等于则提示猜测成功。

class GuessNum():
	# 公有属性
	num = 100

	# 公有绑定方法  self 对象调
	def guess(self):
		while True:
			content = input('请输入一个数:')
			if content.isdecimal():
				content = int(content)
				if content > self.num:
					print('大了')
				elif content < self.num:
					print('小了')	
				elif content == self.num:
					print('猜测成功')
					break
			else:
				print('请输入数字哈')

# g1 = GuessNum()
# g1.guess()
print('---------------2')

# 3.创建一个圆Circle类。
# 为该类提供一个变量r表示半径
# 方法一返回圆的面积,方法二返回圆的周长；
import math
class Circle():
	# 公有属性
	r = 10
	
	# 公有绑定方法 self 对象调
	def area(self):
		return math.pi*(self.r**2)
		
	# 公有非绑定方法  不带self 类调
	def perimeter():  
		return 2*math.pi*Circle.r

c1 = Circle()
area1 = c1.area()
print(area1)  #314.1592653589793

perimeter1 = Circle.perimeter()
print(perimeter1) #62.83185307179586
print('---------------3-1')

import math
class Circle():
	# 公有属性
	# r = 10
	
	# 公有绑定方法 self 对象调
	def area(self,r):  #有参数
		# return math.pi*(self.r**2)
		return math.pi*(r**2)
		
	# 公有绑定方法  self 对象调
	def perimeter(self,r):  
		# return 2*math.pi*self.r
		return 2*math.pi*r
c1 = Circle()
area1 = c1.area(10)
print(area1)  #314.1592653589793

perimeter1 = c1.perimeter(10)
print(perimeter1)  #62.83185307179586
print('---------------3-2')

class Circle():
	# 公有属性
	# r = 10
	
	# 构造方法
	def __init__(self,r):
		self.r = r
	
	# 公有绑定方法 self 对象调
	def area(self):  #有参数
		return math.pi*(self.r**2)
		
	# 公有绑定方法  self 对象调
	def perimeter(self):  
		return 2*math.pi*self.r

c1 = Circle(10)
area1 = c1.area()
print(area1)  #314.1592653589793

perimeter1 = c1.perimeter()
print(perimeter1) #62.83185307179586
print('---------------3-3')


















































