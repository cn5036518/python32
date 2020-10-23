# 2.res是多少?
# def func():
	# return [lambda x : i*x    for i in range(4)]
# res = [m(2) for m in func()]


for i in [lambda x : i*x    for i in range(4)]:
	print(i,type(i))
	# < function < listcomp >.< lambda > at 0x7fdab23ef158 > < class 'function' >
	#                                  < function < listcomp >.< lambda > at 0x7fdab23ef1e0 > < class 'function' >
	#                                  < function < listcomp >.< lambda > at 0x7fdab23ef268 > < class 'function' >
	#                                  < function < listcomp >.< lambda > at 0x7fdab23ef2f0 > < class 'function' >


print(lambda x : i*x    for i in range(4))
# <generator object <genexpr> at 0x7fdab082c048>


# [lambda x : i*x    for i in range(4)]
# 这是一个列表,列表有4个元素,每个元素是一个匿名函数,改写如下

def func():
	li = []
	for i in range(4):
		def inner(x):
			return i*x
		li.append(inner)
	return li

res = func()
print(res)  #这是一个列表,列表有4个元素,每个元素是一个匿名函数
for i in res:
	print(i(2))


