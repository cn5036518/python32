# ### 1.使用递归实现任意数n的阶乘 
# 1普通实现  累乘
def factorial(n):
	total = 1
	# for i in range(n,0):  #没有-1 取不到值
	for i in range(n,0,-1):
		total *= i
		# total = total * i
		# return total   #error
	return total  # 和for对齐
res = factorial(3)
print(res) #6

# 2递归实现
# 规律:
# 5的阶乘=5*4的阶乘
# 4的阶乘=4*3的阶乘
# 3的阶乘=3*2的阶乘
# 2的阶乘=2*1的阶乘
# 1的阶乘=1  #递归结束  终止条件

#步骤:
# 1 先写终止条件
# 2 想最后一步,找规律--关键点  递归函数依次递减调用
def factorial(n):
	if n == 1:
		return 1  #终止条件
	else:
		return n * factorial(n-1)  #规律  依次递减调用
res = factorial(4)
print(res)  #24


# ### 2. 使用尾递归来实现任意数的阶乘
# 普通递归:return后面是一个表达式 含有+-*/等
# 尾递归:return后面是函数本身
#         尾递归在归的时候,最后一层和第一层的返回值是一样的

#步骤:
# 1 先写终止条件
# 2 想最后一步,找规律--关键点  递归函数依次递减调用
# 3 通过return第2个参数来实现
def factorial(n,endval):
	if n == 1:
		return endval
	else:
		return factorial(n-1,endval * n)
		#参数1   n-1 递减  
		# 参数2  endval * n   #这个是一个累乘的效果
res = factorial(3,1)  #这里需要用户传2个参数
print(res)
print('-----------------2 阶乘 尾递归')

# n=3 endval=1  factorial(2,1 * 3)
# n=2 endval=1*3  factorial(1,1 * 3*2)
# n=1 endval=1*3*2  return endval 1*3*2

#优化1
def factorial(n,endval=1):  #默认参数
	if n == 1:
		return endval
	else:
		return factorial(n-1,endval * n)
		#参数1   n-1 递减  
		# 参数2  endval * n   #这个是一个累乘的效果
res = factorial(3)  
# res = factorial(3,100)    #无法防止这个
print(res)
print('-----------------2-2 阶乘 尾递归 默认参数')

#优化2  双层嵌套函数
def outer(n):
	def factorial(n,endval=1):  #默认参数
		if n == 1:
			return endval
		else:
			return factorial(n-1,endval * n)
	return factorial(n)   #非闭包,如果这里是factorial,才是闭包
			#参数1   n-1 递减  
			# 参数2  endval * n   #这个是一个累乘的效果
res = outer(3)  
# res = factorial(3,100)    #有效防止用户输入2个参数
print(res)
print('-----------------2-3 阶乘 尾递归 限制用户只能输入一个参数')


# ### 3.使用递归来完成斐波那契数列
# 1 1 2 3 5 8 13...
def fab(n):
	if n == 1 or n== 2:
		return 1  #终止条件
	else:
		return fab(n-1) + fab(n-2)

res = fab(5)
res = fab(6)
# print(res)  #8

#步骤:
# 1 先写终止条件
# 2 想最后一步,找规律--关键点  递归函数依次递减调用




































