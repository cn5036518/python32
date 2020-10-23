#1 普通形参(位置形参)
# 定义函数
def small_star(row,column):
	i = 0
	while i < row:  # 行
		# 打印星星
		j = 0
		while j < column: #列
			print('*',end='')		
			j += 1	
		print()  #换行
		i += 1

# 调用函数
small_star(10,10)
print('--------------------------1')

#2. 默认形参
# 定义函数
def small_star(row=10,column=10):
	i = 0
	while i < row:  # 行
		# 打印星星
		j = 0
		while j < column: #列
			print('*',end='')		
			j += 1	
		print()  #换行
		i += 1

# 调用函数
# small_star(4,8)  #都覆盖默认参数
# small_star(8)  #参数1覆盖默认参数 参数2去默认参数
small_star()  #都取默认参数
print('--------------------------2')

# 3.普通形参 + 默认形参
# 普通形参必须放到默认形参的前面,不能调换位置
# 定义函数
def small_star(row,column=10): #参数1是普通形参  参数2是默认形参
	i = 0
	while i < row:  # 行
		# 打印星星
		j = 0
		while j < column: #列
			print('*',end='')		
			j += 1	
		print()  #换行
		i += 1

# 调用函数
# small_star(4,8)
small_star(5)
# small_star()  # error
# TypeError: small_star() missing 1 required positional argument: 'row'
print('--------------------------3')

# 4.关键字实参
# 如果都是关键字实参,可以任意调通实参的位置
# 普通实参必须写在关键字实参的前面
def small_star(row,a,b,c,column=10): #参数1 2 3 4是普通形参  参数5是默认形参
	i = 0
	while i < row:  # 行
		# 打印星星
		j = 0
		while j < column: #列
			print('*',end='')		
			j += 1	
		print()  #换行
		i += 1

# 调用函数
small_star(3,4,b=5,c=6,column=7)
# small_star(b=5,c=6,column=7,3,4) #error
# SyntaxError: positional argument follows keyword argument
print('--------------------------4')





























