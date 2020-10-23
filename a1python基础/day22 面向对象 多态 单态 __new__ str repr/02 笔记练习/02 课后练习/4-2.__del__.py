# ### __del__ 魔术方法(析构方法)

	# 触发时机:当对象被内存回收的时候自动触发
	  # [1.页面执行完毕回收所有变量 
	  #  2.所有对象被del的时候]
    # 功能：对象使用完毕后资源回收
	# 参数：一个self接受对象
	# 返回值：无

# (1) 基本语法
class Lion():
	def __init__(self,name): #拼写 少写一个i
		self.name = name
		
	def __del__(self):
		print('析构方法被触发')

# 触发方式一: 页面执行完毕回收所有变量
obj1 = Lion('辛巴')

# 触发方式二: 所有对象被del的时候
obj2 = obj1  
obj3 = obj1
print(obj1,obj2,obj3)  #这3个变量名(不同的别名)的值是同一个内存地址id
#<__main__.Lion object at 0x7f5029dfbb38>
 # <__main__.Lion object at 0x7f5029dfbb38>
 # <__main__.Lion object at 0x7f5029dfbb38>
print("<====start===>")
del obj1  #删除第一个变量名  对应的值(内存空间)依然存在
del obj2  #删除第2个变量名   对应的值(内存空间)依然存在
del obj3  ##删除第3个变量名 和对应的值(内存空间)
print("<====end===>")

# (2) 模拟文件操作--用面向对象的方式
import os
class ReadFile():
	# 根据文件是否存在,创建对象
	def __new__(cls,filename):
		if os.path.exists(filename):
			return object.__new__(cls)
		else:
			print('没有这个文件')

	# 打开文件
	def __init__(self,filename):
		self.fp = open(filename,mode='r',encoding='utf-8')
		# 这里的fp前面需要self 否则类内的其他地方无法使用	

	# 读取文件
	def readcontent(self):
		return self.fp.read()
	
	# 关闭文件
	def __del__(self):
		self.fp.close() #回收文件对象

obj = ReadFile('1.多态.py')
# print(obj.readcontent())


































