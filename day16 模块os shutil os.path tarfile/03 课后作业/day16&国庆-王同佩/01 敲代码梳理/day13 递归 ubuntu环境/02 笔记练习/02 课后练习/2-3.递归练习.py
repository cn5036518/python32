# ### 阶乘

# 普通实现
# 5! = 5 * 4 * 3 * 2 *1
n = 5
total = 1
for i in range(n,0,-1):
	total *= i
print(total)  #120

total = 1
for i in range(1,n+1):
	total *= i
print(total)

# 递归实现
# 规律  3! = 3 * 2!
#       2! = 3 * 1!
#       1! = 1

def factorial(n):
	if n == 1:  #递归终止条件
		return 1
	return factorial(n-1) * n

res = factorial(5)
print(res)  #120


# 2 递归完成斐波那契数列
# 1 1 2 3 5 8 ...
def fibonacci(n):
	if n == 1 or n == 2:  #递归终止条件
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

res = fibonacci(5)
print(res)  #5

# 3 尾递归完成阶乘
def factorial(n,endval):
	if n == 1:  #终止条件
		return endval
	return factorial(n-1,n * endval)  #依次递减
res = factorial(3,1)
print(res)  #6

# 优化代码1
def factorial(n,endval=1): #默认参数
	if n == 1:
		return endval
	return factorial(n-1,n*endval)
res = factorial(3) #3*2*1  #
# res = factorial(3,100)
print(res) #6

# 优化代码2  
# 通过嵌套函数,让只能传一个参数
def outer(n):
	def factorial(n,endval=1):
		if n == 1:
			return endval
		return factorial(n-1,n * endval)
	return factorial(n)  #双层嵌套函数,如果这里返回的是函数名,就是闭包
res = outer(3)
print(res)
# print(outer(5,1))  #120  #用户只能传一个参数,传2个,就会报错
#TypeError: outer() takes 1 positional argument but 2 were give

# 优化代码3
# 闭包实现
def outer(n):
	endval = 1
	def factorial(n):
		nonlocal endval  #修改最近一层的局部变量(外函数内,内函数外)
		# 延长了局部变量的生命周期
		if n == 1:  #递归终止条件
			return endval
		endval *= n
		return factorial(n-1)		
	return factorial  #返回内函数
func = out(3)
res = func(3)  # factorial(3)
print(res)  #6

代码解析
n = 3  endval = 3*1  return factorial(2)
n = 2  endval = 3*1*2  return factorial(1)
n = 1  endval = 3*1*2  return endval





























