# ### 闭包特点
# 特点:在闭包函数中,内函数使用了外函数的局部变量
	 # 该变量会与内函数发生绑定,延长该变量的生命周期
	 # 持续到脚本执行结束

def outer(val):
	def inner(num):
		return val + num
	return inner
	
func = outer(10)   #val = 10  #延长val的生命周期
# val是外函数的形参,也是局部变量(内函数用到了)
res = func(15)   # inner(15)  #num=15    #return 10 + 15
print(res)

# ### 闭包的意义
# 全局变量的作用域大,容易被篡改

num = 0
def click_num():
	global num
	num += 1 # 在函数内,只能获取全局变量,而不能在函数内,直接修改全局变量
	#  如果需要在函数内,修改全局变量,需要用global
	# global的两个作用
	# 1 在函数内定义全局变量(该全局变量之前未定义)
	# 2 在函数内修改已有的全局变量
	print(num)
click_num()
click_num()
click_num()
num = 100  #被篡改了
click_num()
click_num()
# 1
# 2
# 3
# 101
# 102
print('---------------------------1')

# 改造,用闭包来实现
# 闭包的意义:
	# 闭包可以优先使用外函数中的局部变量.
	# 并对闭包中的值起到了封装保护的作用,外部无法访问
	
def outer():
	x = 0
	def click_num():
		nonlocal x  # nonlocal 修改最近的一层局部变量
		# global 在在函数内修改已有的全局变量
		x += 1
		print(x)
	return click_num
click_num = outer()
click_num()
click_num()
click_num()
x = 100  #篡改不了
click_num()
click_num()

# 1
# 2
# 3
# 4
# 5
# 小结:这里的x是内函数使用了外函数的局部变量
# 通过闭包,可以实现内函数对外函数局部变量的修改,而让别人无法修改,增加了安全性

# 分为3层
# 第1层:最内层  内函数内
# 第2层:中间层  外函数的局部变量
# 第3层:最外层  函数外的全局变量














































