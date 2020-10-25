# """
# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码）
# 要求只要登录成功一次，后续的函数都无需输入用户名和密码
# """

# 方法一

flag = False
def login(func):
	def inner(*args,**kwargs):
		global flag  #函数内修改全局变量
		
		# 如果flag = True  代表已经登录
		if flag:
			res = func(*args,**kwargs)
			return res
			
		# 否则没有登录
		else:
			username = input('请输入您的登录用户名:')
			password = input('请输入您的登录密码:')
			if username == 'wangwen' and password == '111':
				# 登录成功
				flag = True
				res = func(*args,**kwargs)
				return res
			else:
				print('账号或者密码输入错误')		
	return inner

@login  
#buy_bao = login(buy_bao)
#buy_bao = inner
#buy_bao() = inner()
def buy_bao():
	print('我要买包')
	
@login
#buy_fruit = login(buy_fruit)
#buy_fruit = inner
#buy_fruit() = inner()
def buy_fruit():
	print('我要买水果')
print('-----------1')

# buy_bao()
# buy_fruit()

# 请输入您的登录用户名:wangwen
# 请输入您的登录密码:111
# 我要买包
# 我要买水果


#思路
# 先把装饰器的格式写好,卡定义
# 再写逻辑

flag = False  #默认没登录
def login(func):
	def inner(*args,**kwargs):
		global flag
		if flag: #True是登录了,不需要登录,直接调函数
			res = func(*args,**kwargs)   #buy_bao()
			return res
		else:
			username = input('请输入你的登录用户名:')
			pwd = input('请输入你的登录密码:')
			if username == 'wangwen' and pwd == '111':
				print('登录成功')
				flag = True
				res = func(*args,**kwargs)
				return res	
			else:
				print('登录失败')
	return inner

@login
#buy_bao = login(buy_bao)	
#buy_bao = inner	
#buy_bao() = inner()
def buy_bao():
	print('我要买包')
	
@login
def buy_fruit():
	print('我要买水果')

# buy_bao()
# buy_fruit()

# 请输入你的登录用户名:wangwen
# 请输入你的登录密码:1
# 登录失败
# 请输入你的登录用户名:wangwen
# 请输入你的登录密码:111
# 登录成功
# 我要买水果
print('-----------2')


#思路
# 先把装饰器的格式写好,卡定义
# 再写逻辑

#默写3
flag = False
def login(func):  
	def inner(*args,**kwargs):
		global flag
		if flag:  #True登录成功
			res = func(*args,**kwargs)  #buy_bao()
			return res			
		else:  #登录认证
			username = input('请输入登录用户名:')
			pwd = input('请输入登录密码:')
			if username == 'wangwen' and pwd =='111':		
				print('登录成功')
				flag = True
				res = func(*args,**kwargs)
				return res
			else:
				print('登录失败')
	return inner
	
	
@login
# buy_bao = login(buy_bao)
# buy_bao = inner
# buy_bao() = inner()
def buy_bao():
	print('我要买包')

@login
def buy_fruit():
	print('我要买水果')

# buy_bao()
# buy_fruit()

# 请输入登录用户名:wangwen
# 请输入登录密码:111
# 登录成功
# 我要买包
# 我要买水果
print('-----------方法一 3')


# 方法2 类装饰器
#思路
# 先把装饰器的格式写好,卡定义
# 再写逻辑

class Shop():
	def __init__(self,flag):
		self.flag = flag
		
	def login(func):
		def inner(self,*args,**kwargs):
			if self.flag:  #True是已经登录
				# res = self.func(*args,**kwargs)  #不对
				res = func(self,*args,**kwargs)
				return res
			else: #验证登录密码
				username = input('请输入登录用户名:')
				pwd = input('请输入登录密码:')
				if username == 'wangwen' and pwd == '111':
					print('登录成功')
					self.flag = True
					# res = self.func(*args,**kwargs)  #不对
					res = func(self,*args,**kwargs)
				else:
					print('登录失败')			
		return inner		
		
	@login	
	# buy_bao = login(buy_bao)
	# buy_bao = inner
	# buy_bao() = inner()
	def buy_bao(self):
		print('我要买包')
		
	@login
	def buy_fruit(self):
		print('我要买水果')
		
# shop = Shop(False)
# shop.buy_bao()
# shop.buy_fruit()
print('-----------方法二 1')


# 类装饰器  卡定义  默写2
class Shopping():
	def __init__(self,flag):
		self.flag = flag
		
	def login(func):
		def inner(self,*args,**kwargs):
			if self.flag:  #True是已登录
				res = func(self,*args,**kwargs)
				return res
				
			else: #验证登录密码
				username = input('请输入登录用户名:')
				pwd = input('请输入登录密码:')
				if username == 'wangwen' and pwd == '111':
					print('登录成功')
					self.flag = True
					res = func(self,*args,**kwargs)
					return res
				else:
					print('登录失败')			
		return inner		
		
	@login
	#buy_bao = login(buy_bao)
	#buy_bao = inner
	#buy_bao() = inner()	
	def buy_bao(self):
		pass
		
	@login
	def buy_fruit(self):
		pass	
	
# obj = Shopping(False)
# obj.buy_bao()
# obj.buy_fruit()
print('-----------方法二 2')


# """
# 2.编写装饰器，为多个函数加上记录调用功能，
# 要求 每次调用函数把调用的函数名称写入文件
# """

# 方法1 函数装饰器   卡定义
def log1(func):
	def inner(*args,**kwargs):	
		with open('log.txt',mode='a+',encoding='utf-8') as fp:
			fp.write(func.__name__+'\n')  #函数或类的名称  __name__
			res = func(*args,**kwargs)  #调用函数前,把函数名字写入对log文件
			return res		
	return inner

@log1	
# buy_bao = log1(buy_bao)	
# buy_bao = inner	
# buy_bao() = inner()
def buy_bao():
	print('我要买包')
	
@log1
def buy_fruit():
	print('我要买水果')

# buy_bao()
# buy_fruit()
print('-----------第2题 方法一 1')


# 方法2 类装饰器   卡定义
class Log1():	
	def log1(func):
		def inner(self,*args,**kwargs):	
			with open('log2.txt',mode='a+',encoding='utf-8') as fp:
				fp.write(func.__name__+'\n')  #函数或类的名称  __name__
				res = func(self,*args,**kwargs)  #调用函数前,把函数名字写入对log文件
				return res		
		return inner

	@log1	
	# buy_bao = log1(buy_bao)	
	# buy_bao = inner	
	# buy_bao() = inner()
	def buy_bao(self):
		print('我要买包')
		
	@log1
	def buy_fruit(self):
		print('我要买水果')

log1 = Log1()
log1.buy_bao()
log1.buy_fruit()
print('-----------第2题 方法二 1')


# 小结:
# 1 装饰器的作用和常见应用场景
# 可以在不修改原函数的情况下,
   # 在原函数执行的前后,添加功能
   
# print(1)  #这个可以是登录验证,也可以是记录函数名字到文件等
# 最常见的是给原函数加登录验证(即原函数之前不需要登录验证,现在需要登录验证了,如何在不修改原函数的情况下实现呢?---装饰器)
# func()  #原函数的调用
# print(2)

# 2 装饰器的分类
# 函数装饰器
# 类装饰器

# 3 装饰器的定义  严格卡定义
#定义装饰器函数   闭包
def login(func):
	def inner(*args,**kwargs):
		buy2()    #在原函数执行前,调其他函数
		print(1)  #这个可以是登录验证,也可以是记录函数名字到文件等  最常见的是给原函数加登录验证
		func(*args,**kwargs)  #原函数的调用
		print(2)   #在原函数执行后,添加功能或者调其他函数
		buy()       #在原函数执行后,调其他函数
	return inner

@login   #给原函数添加装饰器
#func = login(func)
#func = inner
#func() = inner()
def func():
	pass
	
def buy():
	print('haha')
	
def buy2():
	print('haha2')

func()  #调函数
# haha2
# 1
# 2
# haha
print('-----------小结1')

























