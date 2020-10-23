# ### __str__ 魔术方法

# 触发时机: 使用print(对象)或者str(对象)的时候触发
# 功能:     查看对象
# 参数:     一个self接受当前对象
# 返回值:   必须返回字符串类型   ***

class Cat():
	gift = '抓老鼠'
	def __init__(self,name):
		self.name = name
		
	def cat_gift(self):
		return '小猫叫{},小猫会{}'.format(self.name,self.gift)

	# def __str__(self):
		# return self.cat_gift()

tom = Cat('汤姆')
# 触发时机1 :  print(对象)
print(tom,type(tom))  #<__main__.Cat object at 0x7fca84b17b00>
#<class '__main__.Cat'>

res = str(tom)
print(res,type(tom))
#<__main__.Cat object at 0x7fb27407b588> <class '__main__.Cat'>
print('----------------1')

class Cat():
	gift = '抓老鼠'
	def __init__(self,name):
		self.name = name
		
	def cat_gift(self):
		return '小猫叫{},小猫会{}'.format(self.name,self.gift)

	def __str__(self):
		return self.cat_gift()
		
	# 系统底层默认把__str__ 方法赋值给__repr__方法,
	# 所以通过print或者str强转可以触发;
	__repr__ = __str__

tom = Cat('汤姆')
# 触发时机1 :  print(对象)
print(tom) 
#小猫叫汤姆,小猫会抓老鼠
print('----------------2-1  str print')

# 触发时机2 :  str(对象)
res = str(tom)
print(res)
# 小猫叫汤姆,小猫会抓老鼠
print('----------------2-2  str强转')

res = repr(tom)
print(res,type(res))
#小猫叫汤姆,小猫会抓老鼠 <class 'str'>
print('----------------2-3 repr ')


# ### __repr__ 魔术方法
# 触发时机: 使用repr(对象)的时候触发
# 功能:     查看对象,与魔术方法__str__相似
# 参数:     一个self接受当前对象
# 返回值:   必须返回字符串类型

class Mouse():
	gift = '偷油吃'
	def __init__(self,name):
		self.name = name
		
	def mouse_gift(self):
		return '老鼠叫{},老鼠会{}'.format(self.name,self.gift)

	def __repr__(self):
		return self.mouse_gift()
		
	# 系统底层默认把__repr__方法赋值给__str__方法,
	# 所以通过print或者str强转可以触发;
	__str__ = __repr__
		
jerry = Mouse('杰瑞')
res = repr(jerry)
print(res)
#老鼠叫杰瑞,老鼠会偷油吃
print('----------------3-1 repr')

# __str__ 可以触发
print(jerry)
#老鼠叫杰瑞,老鼠会偷油吃
print('----------------3-2 str print')

res = str(jerry)
print(res)
# 老鼠叫杰瑞,老鼠会偷油吃
print('----------------3-3 str强转')

#小结
# __str__和__repr__的区别
# 触发方式不同
# __str__ 是print(对象)或str(对象)来触发
# __repr__是repr(对象)来触发





















