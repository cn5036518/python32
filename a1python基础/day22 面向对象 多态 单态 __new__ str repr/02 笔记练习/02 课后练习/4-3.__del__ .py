# ### __del__ 魔术方法(析构方法)
# '''
	# 触发时机:当对象被内存回收的时候自动触发
	  # 页面执行完毕的时候 
	   # 所有对象被del的时候
    # 功能：对象使用完毕后的资源回收
	# 参数：self
	# 返回值：无
# '''

# (1) 基本语法
# 触发方式一: 页面执行完毕回收所有变量
class Car():
	def __init__(self):
		pass
		
	def __del__(self):
		print('我是析构方法')
		
# obj1 = Car()	


# 触发方式二: 所有对象被del的时候
# 指的是单个对象的引用次数变成0的时候
class Car():
	def __init__(self):
		pass
		
	def __del__(self):
		print('我是析构方法')
		
obj1 = Car()
obj2 = obj1
obj3 = obj1
print('--------------1')
del obj1
del obj2
del obj3
print('--------------2')

# --------------1
# 我是析构方法
# --------------2

class Car():
	def __init__(self):
		pass
		
	def __del__(self):
		print('我是析构方法')
		
obj1 = Car()
obj2 = Car()
obj3 = Car()
print('--------------3')
del obj1
del obj2
print('--------------4')

# --------------3
# 我是析构方法  ## 指的是单个对象obj1的引用次数变成0的时候
# 我是析构方法  ## 指的是单个对象obj2的引用次数变成0的时候
# --------------4
# 我是析构方法  #指的是页面执行完毕回收所有变量的时候


# (2) 模拟文件操作
# 思路:
# 判断文件对象是否存在  os.path.exists  __new__
# 打开文件对象  __init__  open()
# 读取文件  read()
# 关闭文件对象  __del__  close()

import os
class ReadFile():
	def __new__(cls,filename):
# 判断文件对象是否存在  os.path.exists
		if os.path.exists(filename):
			return object.__new__(cls)
		else:
			print('文件不存在')

# 打开文件对象  __init__
	def __init__(self,filename):  #少了__ 拼写
		self.fp = open(filename,mode='r+',encoding='utf-8')

# 读取文件
	def read_content(self):
		return self.fp.read()

# 关闭文件对象  __del__
	def __del__(self):
		self.fp.close()

# obj = ReadFile('1.多态.py')
# print(obj.read_content())

# 思路:
import os
class ReadFile():
# 判断文件对象是否存在  os.path.exists  __new__
	def __new__(cls,filename): #和构造方法参数一致
		if os.path.exists(filename):
			# print(1)
			return object.__new__(cls)
		else:
			print('文件不存在')


# 打开文件对象  __init__  open()
	def __init__(self,filename):  #构造方法传入参数
		self.fp = open(filename,mode='r',encoding='utf-8')

# 读取文件  read()
	def read_content(self):
		res =  self.fp.read()
		return res

# 关闭文件对象  __del__  close()
	def __del__(self):
		self.fp.close()

obj = ReadFile('1.多态.py')
res = obj.read_content()
print(res)
























































