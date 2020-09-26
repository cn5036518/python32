# ### 闭包特点
"""
特点:在闭包函数中,内函数使用了外函数的局部变量,
该变量会与内函数发生绑定,延长该变量的生命周期,
持续到脚本执行结束.
"""
def outer(val):  #这里的val=10.也是局部变量（外函数的局部变量）
	def inner(num):
		return val + num #val=10  num=15  val这个局部变量的生命周期延长了
	return inner
	
func = outer(10)
res = func(15)
print(res)  #25


# ### 闭包的意义
"""全局变量的作用域大,容易被篡改"""
num = 0
def click_num():
	global num   #函数内修改全局变量
	num += 1 # num = num + 1
	print(num)
click_num()
click_num()
click_num()
num = 100
click_num()
click_num()

# 1
# 2
# 3
# 101
# 102

# 改造,用闭包来实现
"""
闭包的意义:
	闭包中的内函数可以优先使用外函数中的局部变量,
	并对闭包中的值（指的是内函数使用的哪个外函数的局部变量）起到了封装保护的作用.外部无法访问.
"""
def outer():
	x = 0
	def click_num():
		nonlocal x  #修改最近一层的局部变量
		x += 1
		print(x)   #外函数的局部变量x，在内函数中被使用了
	return click_num

click_num = outer()
click_num()
click_num()
click_num()
x = 100
click_num()
click_num()

# 1
# 2
# 3
# 4
# 5



















