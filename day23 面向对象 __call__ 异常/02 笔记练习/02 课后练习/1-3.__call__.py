# ### __call__ 魔术方法
# '''
	# 触发时机：把对象当做函数进行调用的时候触发    对象()
	# 功能: 模拟函数化操作
	# 参数: 至少一个self
	# 返回值: 看需求
# '''

# (1) 基本语法
class Car():
	def __call__(self):
		print('hello')
		
obj = Car()
obj()  #hello


# (2) 利用__call__魔术方法做统一调用
class Car():
	def __call__(self):
		pass
		
	def step1(self):
		pass
	
	def step2(self):
		pass
		
	def step3(self):
		pass
	
#用户调	
obj = Car()
obj.step1()	
obj.step2()	
obj.step3()	 #n个方法,用户就需要写n行

#改进  如何让用户方便调?
class Car():
	def __call__(self):
		self.step1()
		self.step2()
		self.step3()
		
	def step1(self):
		print(1)
	
	def step2(self):
		print(2)
		
	def step3(self):
		print(3)
	
#用户调	
obj = Car()
obj()
#1
# 2
# 3
print('----------------------2-2 ')

#改进  如何让用户方便调?
class Car():
	def __call__(self,name):
		self.step1(name)  #参数,这里没有init
		self.step2()
		self.step3()
		
	def step1(self,name):
		print('我的名字是{}'.format(name))
	
	def step2(self):
		print(2)
		
	def step3(self):
		print(3)
	
#用户调	   好处是:用户只需要写2步就可以了
obj = Car()
obj('jack')
# 我的名字是jack
# 2
# 3
print('----------------------2-3 传参 ')


# (3) 模拟整型强转操作
# int可以强制的类型 bool int foat 和 纯数字字符串

# bool 
# int 
# foat 
# 纯数字字符串

import math
class MyInt():
	def  __call__(self,num):
		if isinstance(num,bool):  #1 强转bool
			if num is True:
				return 1
			else:
				return 0
		elif isinstance(num,int):  #2 强转int
			return num
		elif isinstance(num,float):  #3 强转float
		#方法1
			# if num >= 0:
				# return math.floor(num)
			# else:
				# return math.ceil(num)
		#方法2
			a,b = str(num).split('.')
			return eval(a)  #a是字符串,eval(a)就是int
				
		elif isinstance(num,str):  #num是纯数字字符串  #强转纯数字字符串
			if num[1:].isdecimal() and num[0] =='+':   #  '+10'
				return eval(num[1:])
			elif num[1:].isdecimal() and num[0] =='-':  #  '-10'
				return -eval(num[1:])
			elif num.isdecimal() and num[0] not in ['+','-']:	  #'10'
				num = num.lstrip('0')  #'00012'
				if num == '': # '000000'
					return 0
				else:
					return eval(num)  #纯数字字符串转成init  
				# return num  #
			else:
				print('这个不能转换成int')

obj = MyInt()
res = obj(False)  #把对象当函数来调,触发的是类中的__call__方法
print(res)  #0

res = obj(2)  #
print(res) #2

res = obj(3.5)  #3
print(res,type(res))

res = obj(-3.5)  #-3
print(res)

res = obj('+10')  #
print(res)  #10
res = obj('-10')  #
print(res)
res = obj('10')
print(res)
res = obj('0010')
print(res,type(res)) #10 <class 'int'>
res = obj('0000')
print(res,type(res)) #0 <class 'int'>

# print(int(3.5))  #3 向下取整
# print(int(-3.5)) #-3 向上取整
# print(int('+10'))  #10
# print('+10'.isdecimal()) #False












































