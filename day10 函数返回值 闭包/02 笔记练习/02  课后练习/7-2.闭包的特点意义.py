
def outer(var):   #这里的val=10.也是局部变量（外函数的局部变量）
	def inner(num):
		return var + num
		##val=10  num=15  val这个局部变量的生命周期延长了
	return inner

func = outer(10)	
res = func(15)
print(res)  #25

# ### 闭包的意义
# """全局变量的作用域大,容易被篡改"""
num = 0
def click_num():
	global num  #函数内修改全局变量
	num += 1 
	print(num)
click_num()
click_num()
click_num()
num = 100   #直接修改了全局变量
click_num()
click_num()
# 1
# 2
# 3
# 101
# 102
print('---------------------------1')

#计数器
def outer():
	x = 0  #延长生命周期,被保护起来
	def click_num():
		nonlocal x  #修改最近一层的局部变量
		x += 1  #外函数的局部变量x，在内函数中被使用了
		print(x)
	return click_num
	
click_num = outer()
click_num()
click_num()
click_num()
x = 100  #无法修改局部变量x
click_num()
click_num()

# 1
# 2
# 3
# 4
# 5





















