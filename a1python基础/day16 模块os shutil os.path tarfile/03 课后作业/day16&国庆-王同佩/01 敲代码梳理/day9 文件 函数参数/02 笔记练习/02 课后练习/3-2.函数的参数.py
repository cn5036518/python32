# 函数的参数
# 参数:函数运算时需要的值

# 参数的种类:
	# 形参:形式参数,在函数的定义处
	# 实参:实际参数,在函数的调用处
	
# 形参的种类
	# 1 普通形参(位置形参)
	# 2 默认形参
	# 3 普通收集形参
	# 4 命名关键字形参
	# 5 关键字收集形参
	
# 实参的种类
	# 1 普通实参
	# 2 关键字实参
	
# 原则:
	# 形参和实参要一一对应

# 1 普通形参(位置形参)
def small_star(row,column):
	i = 0
	while i < row:
		j = 0
		while j < column:
			print('*',end='')
			j += 1  #在循环体内
		print()
		i +=1  #在循环体内
small_star(2,3)
# ***
# ***
print('---------------1')

# 2 默认形参
def small_star(row = 2,column = 2):
	i = 0
	while i < row:
		j = 0
		while j < column:
			print('*',end='')			
			j += 1	
		print()
		i += 1	
small_star()
# **
# **
print('---------------2-1')
small_star(3)
# **
# **
# **
print('---------------2-2')
small_star(3,3)
# ***
# ***
# ***
print('---------------2-3')


# 3 普通形参 + 默认形参
# 普通形参必须写在默认形参的前面 不能调换位置
def small_star(row,column=3):
	i = 0
	while i < row:
		j = 0
		while j < column:
			print('*',end='')			
			j += 1
		print()  #换行		
		i += 1	
small_star(1,5)  #*****
print('---------------3-1')

small_star(2)
print('---------------3-2')
# ***
# ***

# small_star()
#TypeError: small_star() missing 1 required positional argument: 'row'

# 4 关键字实参
# 如果都是关键字实参,可以任意调整实参的顺序
# 普通实参必须写在关键字实参的前面

# 具体指定参数的值叫做关键字实参,在函数的调用处

def small_star(row,a,b,c,column=1):
	i = 0
	while i < row:
		j = 0
		while j < column:
			print('*',end='')		
			j += 1
		print()
		i += 1

# small_star(b=5,c=6,column=7,3,4)  #报错
# SyntaxError: positional argument follows keyword argument

small_star(3,4,b=5,column=7,c=6)
# *******
# *******
# *******

























