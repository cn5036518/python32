# 1.使用return返回+-*/运算的结果
def calc(num1,num2,sign):
	if sign == '+':
		return num1 + num2
	elif sign == '-':
		return num1 - num2
	elif sign == '*':
		return num1 * num2
	elif sign == '/':
		rerurn = num1 / num2
res = calc(3,5,'+')
print(res)  #8

# 2.什么是全局变量和局部变量
# 全局变量:函数外的变量
# 局部变量:函数内的变量

# 3.python的函数名怎么用?
# 1当参数  2当做返回值  3动态创建  4销毁  函数名也是变量

# 4.互相嵌套的多个函数获取变量时的规则
# legb  从内到外
#  local   局部作用域(内函数内)
#  enclose  嵌套作用域(内函数外,外函数内)
#  global   全局作用域
#  builtin  内置作用域

# 5.如何修改函数嵌套中的变量
# nonlocal
def outer():
	n = 1
	def inner():
		nonlocal n  #只能修改最近的一层局部变量,倒数第二层或者全局变量都不能修改
		n = 10
		print(n) #10
	inner()
	print(n) #10
outer()

# 6.如何在函数内修改全局变量
# global

n = 1
def func():
	global n
	n = 5
	print(n)  #5
func()
print(n) #5
print('--------------6')

# 7.什么是闭包函数,写一个闭包函数,
def outer():
	a = 1
	def inner():
		print(a) #1  #局部变量的生命周期延长了.局部变量内函数可以修改,外函数之外无法修改(被保护起来了)
	return inner
inner = outer()
inner()
print('--------------7')

# 8.闭包函数的特点和意义? 写一个计数器
# 局部变量的生命周期延长了.局部变量内函数可以修改,外函数之外无法修改(被保护起来了)
n = 1
def click():
	global n  #全局变量n存在,global就是从函数内修改全局变量
	#           全局变量n如果不存在,global就有定义全局变量
	n += 1
	print(n)
click() #2
click() #3
n = 100  #这里的n是全局变量,大家都可以修改(如果让一个变量,只能内函数修改,用闭包)
click() #101


print('--------------8-1')

#计数器
def outer():
	n = 0   #局部变量n的生命周期延长了.有累计的作用(比如计数器的次数是累加的,而不是每次调用后,就清零)
	def click():
		nonlocal n  #修改最近的一层局部变量
		n += 1
		print(n)  #每次调用函数,这个n的值都在累加,而不是清零
	return click  #闭包
click = outer()
click() #1
click() #2
n = 100  #局部变量n内函数可以修改,外函数之外无法修改(被保护起来了)
click()  #3
print('--------------8-2')

# 9.变量的生命周期排序规则
# 从短到长
# 局部变量<全局变量<内置变量





















