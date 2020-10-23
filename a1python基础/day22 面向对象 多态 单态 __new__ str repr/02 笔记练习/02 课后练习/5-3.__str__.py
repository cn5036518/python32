# ### __str__ 魔术方法
# '''
	# 触发时机: print str强转的时候
	# 功能:     查看对象的描述信息
	# 参数:     self
	# 返回值:   必须是字符串
# '''


# 触发时机1 :  print(对象)
class Car():
	gift = 'catch mouse'
	def __init__(self,name):
		self.name = name		
		
	# def __str__(self):
		# return '我叫{},我会{}'.format(self.name,self.gift) 
	
obj = Car('jack')
print(obj) #<__main__.Car object at 0x7fcf13e9aa58>
print('------------------------1')

class Car():
	gift = 'catch mouse'
	def __init__(self,name):
		self.name = name		
		
	def __str__(self):
		return '我叫{},我会{}'.format(self.name,self.gift) 
	
obj = Car('jack')
print(obj) #我叫jack,我会catch mouse
print('------------------------2  str print')	

# 触发时机2 :  str(对象)
print(str(obj))
#我叫jack,我会catch mouse
print('------------------------3  __str__ str强转')	

class Car():
	gift = 'catch mouse'
	def __init__(self,name):
		self.name = name		
		
	def __str__(self):
		return '我叫{},我会{}'.format(self.name,self.gift) 
		
	__repr__ = __str__
	
obj = Car('jack')
print(obj) #
print(str(obj))
print(repr(obj))
# 我叫jack,我会catch mouse
# 我叫jack,我会catch mouse
# 我叫jack,我会catch mouse
print('------------------------4  str ')


# ### __repr__ 魔术方法
# '''
	# 触发时机: repr
	# 功能:     查看对象的描述信息
	# 参数:    self   
	# 返回值:  必须是字符串 
# '''
class Car():
	gift = 'catch mouse'
	def __init__(self,name):
		self.name = name
		
	def __repr__(self):
		return '我叫{}.我会{}'.format(self.name,self.gift)

obj = Car('tom')
print(repr(obj))
#我叫tom.我会catch mouse
print('------------------------1  __repr__  repr')	

class Car():
	gift = 'catch mouse'
	def __init__(self,name):
		self.name = name
		
	def __repr__(self):
		return '我叫{}.我会{}'.format(self.name,self.gift)
		
	# __repr__ = __str__  #NameError: name '__str__' is not defined
	
	__str__ = __repr__ 

obj = Car('tom')
print(repr(obj))
#我叫tom.我会catch mouse

print(obj)
print(str(obj))
print('------------------------2  __repr__  repr')


































































