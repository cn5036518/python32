# lambda 参数:返回值

# (1) 无参的lambda表达式 
def func():
	return "文哥是个帅哥"

func1 = lambda :'文哥是个帅哥'	
res = func1()
print(res)  #文哥是个帅哥


# (2) 有参的lambda表达式
def func(n):
	return id(n)
	
func = lambda n:id(n)
res = func(10)
print(res)  #11094592


# (3) 带有判断条件的lambda表达式 
def func(n):
	if n % 2 == 0:
		return "偶数"
	else:
		return "奇数"
		
func = lambda n:'偶数' if n % 2 == 0 else '奇数'
print(func(3))  #奇数

# 三元运算符
# '偶数' if n % 2 == 0 else '奇数'

# 小练习 : 比较两者之间的最大值进行返回
def func(x,y):
	if x > y:
		return x
	else:
		return y

func = lambda x,y:x if x > y else y
print(func(4,5))  #5







































