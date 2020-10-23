# ### __call__ 魔术方法
# 触发时机：把实例化对象当作函数调用的时候自动触发
# 功能: 模拟函数化操作
# 参数: 参数不固定,至少一个self参数
# 返回值: 看需求

# (1) 基本语法
class MyClass():
	def __call__(self):
		print('__call__魔术方法被触发 ... ')

obj = MyClass()
obj() #__call__魔术方法被触发 ... 
print('---------------------------1')

# (2) 利用__call__魔术方法做统一调用
class Wash():
	def __call__(self,something):
		print('我要洗{}'.format(something))
		self.step1(something)
		self.step2()
		self.step3()
		return '洗完了'

	def step1(self,something):
		print('放水,把{}扔进去'.format(something))
		
	def step2(self):
		print('倒洗衣粉,洗衣液,蓝月亮,金纺,立白 ...')
		
	def step3(self):
		print('洗一洗,晾干,穿上')

#调用方-用户	
obj = Wash()
res = obj('衣服')
print(res)
# 我要洗衣服
# 放水,把衣服扔进去
# 倒洗衣粉,洗衣液,蓝月亮,金纺,立白 ...
# 洗一洗,晾干,穿上
# 洗完了


# (3) 模拟整型强转操作  bool int float 纯数字字符串
import math
class MyInt():
	def __call__(self,num):
		if isinstance(num,bool):
			if num == False:
				return 0
			else:
				return 1
		elif isinstance(num,int):
			return num
		elif isinstance(num,float):
			#方法1
			# a,b = str(num).split('.')
			# 将字符串a转成int
			# return eval(a)  #5 <class 'int'>
			
			#方法2
			# if num >= 0:
				# return math.floor(num)
			# else:
				# return math.ceil(num)
			#简写
			return math.floor(num) if num >=0 else math.ceil(num)
			
		elif isinstance(num,str):  #纯数字字符串
			if (num[0] == '+' or num[0] == '-') and num[1:].isdecimal():
				# 获取当前字符串的正负值
				if num[0] == '+':
					sign = 1
				elif num[0] == '-':
					sign = -1
					
				# 截取符号后面的字符串传递
				return self.calc(num[1:],sign)
				
	# 计算最后的数值
	def calc(self,num,sign=1):
		# 去掉纯数字字符串前面的"0"字符串
		num = num.lstrip('0')
		print(num,type(num),'-----------------1')
		# 55555 <class 'str'>
		if num == '':  #纯数字字符串全是0的情况
			return 0
		
		return eval(num)* sign
		# num的类型是字符串,eval把字符串转成数字			
				

myint = MyInt()
res = myint(5.1)
print(res,type(res))

res = myint("-000000000000055555")
print(res , type(res))
#-55555 <class 'int'>

print(myint("+0000000000000"))
#0



























