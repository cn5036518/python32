# ### 匿名函数  lambda 表达式

# 1 无参数的lambad 表达式
def func():
	return '文哥是个帅哥'
	
# 改造
func = lambda : '文哥是个帅哥'
print(func())  #文哥是个帅哥

# 2 有参数的lambda 表达式
def func(n):
	return id(n)
	
func = lambda n:id(n)
print(func(100))  #11097472

# 3 带有判断条件的lambda表达式
def func(n):
	if n % 2 == 0:
		return '偶数'
	else:
		return '奇数'

func = lambda n : '偶数' if n % 2 == 0 else '奇数'
print(func(44))  #偶数
# func = lambda n : '偶数'
#冒号后面是三元运算符

n = 13
res = '偶数' if n % 2 == 0 else '奇数'
print(res)  #奇数


# 比较两者的最大值进行返回
def func(x,y):
	if x > y :
		return x
	else:
		return y
		
print(func(5,3))

func = lambda x,y :x if x > y else y
print(func(6,8))  #8









































