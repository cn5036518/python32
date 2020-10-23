# 1 动态创建
def func():
	print('我是func函数')

a = 1
print(a)
a = func
a()  #我是func函数

# 2 动态销毁
# del a
# a()  #NameError: name 'a' is not defined

# (3)当参数传递
def func2():
	return "我是func2函数"

def func1(f):
	return f() # "我是func2函数"  函数名() 就是调用

res = func1(func2)
print(res)  #我是func2函数

#4 作为值返回
def func3():
	print('我是func3函数')

def func4(f):
	return f

res = func4(func3)
print(res)  #<function func3 at 0x7f946398e2f0>
res()  #我是func3函数

# (5)函数名可以作为容器类型数据的元素
lst = [func,func3]
for i in lst:
	i()
# 我是func函数
# 我是func3函数

def func5():
	'''
	功能:
	参数:
	返回值	
	'''
	print('我是func5函数')

res = func5.__doc__
print(res)
	# 功能:
	# 参数:
	# 返回值

help(func5)
# Help on function func5 in module __main__:

# func5()
    # 功能:
    # 参数:
    # 返回值






























