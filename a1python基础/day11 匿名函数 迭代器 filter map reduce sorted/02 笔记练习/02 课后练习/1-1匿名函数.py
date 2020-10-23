#  ###  匿名函数:  lambda 表达式

# 概念:用一句话来表达只有返回值的函数
# 语法:lambda 参数: 返回值
# 特点:简洁,高效

# 1 无参数的lambda表达式
def func():
	return '帅哥'
	
# 改造
func = lambda : '帅哥'
res = func()
print(res)  #帅哥

# 2 有参数的lambda表达式
def func(n):
	return id(n)

# 改造
func = lambda n : id(n)
res = func(100)
print(res)  #140724403400432

# 3 带有判断条件的lambda表达式
def func(n):
	if n % 2 == 0:
		return '偶数'
	else:
		return '奇数'

# 改造
func = lambda n : '偶数' if n % 2 == 0 else '奇数'
res = func(44)
print(res)  #偶数

# 三元运算符
# 语法:  真的值 if 条件表达式 else 假的值
# 如果条件表达式成立,返回if前面的真值
# 如果条件表达式不成立,返回else后面的假的值

n = 13
res = '偶数' if n % 2 == 0 else '奇数'
print(res)  #奇数

# 小练习:比较两者之间的最大值进行返回
def func(x,y):
	if x > y:
		return x
	else:
		return y

# 改造
func = lambda x,y : x if x > y else y
res = func(40,30)
print(res)  #40









































