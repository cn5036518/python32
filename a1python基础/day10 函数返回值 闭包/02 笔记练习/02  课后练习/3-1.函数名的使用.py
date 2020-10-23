# ### 函数名的使用
# python中的函数可以像变量一样,动态创建,销毁,当参数传递,作为值返回
# 叫第一类对象,其他语言的函数功能有限

def func():
	print('我是func函数')

# 1 动态创建
a = 1
print(a)  #1
a = func
a()  #我是func函数

# (2) 动态销毁
del a
# a()  #NameError: name 'a' is not defined
func()  #我是func函数

# 3 当参数传递
def func2():
	return '我是func2函数'

def func1(f):
	return f()  # 我是func2函数
	
res = func1(func2)
print(res)

# 4 作为值返回
def func3():
	print('我是func3函数')
	
def func4(f):
	return f
	
res = func4(func3)
print(res)  #<function func3 at 0x000001F05AF25950>  函数对象
res() #我是func3函数  #func3()

# 5 函数名可以作为容器类型数据的元素
lst = [func,func3]
for i in lst:
	i()

# ### __doc__ 或者help 查看文档
def big_chang_cishen(something):
	'''
	功能:教你怎么吃大肠
	参数:吃的内容
	返回值:是否满意	
	'''
	print('把{}洗一洗'.format(something))  #把肠子洗一洗
	return '吃完了,好吃'
	
big_chang_cishen('肠子')

# 方法一
res = big_chang_cishen.__doc__
print(res)


	# 功能:教你怎么吃大肠
	# 参数:吃的内容
	# 返回值:是否满意	

# 方法二
help(big_chang_cishen)

	
# Help on function big_chang_cishen in module __main__:

# big_chang_cishen(something)
    # 功能:教你怎么吃大肠
    # 参数:吃的内容
    # 返回值:是否满意




























