# 命名关键字参数
# 定义
# def func(a,b,*,c,d) 跟在*号后面的c和d是命名关键字参数
# def func(*args,e,**kwargs) 加在*args和**kwargs之间的参数都是命名关键字参数

# 命名关键字参数:在调用函数时,必须使用指定关键字实参的形式来进行调用;否则报错

# 定义方法一
def func(a,b,*,c,d):
	print(a,b) #1 2
	print(c,d) #3 4
	
# 必须指定关键字实参,才能对命名关键字形参进行赋值
func(1,2,c=3,d=4)
# func(1,2,3,d=4)  #报错  必须写c=3
#TypeError: func() takes 2 positional arguments 
#but 3 positional arguments (and 1 keyword-only argument) were given

# 定义方法二
def func(*args,e,**kwargs):
	print(args) #(1, 2, 3, 4)  普通收集实参打包成元组
	print(e)  #3  #命名关键字形参
	print(kwargs)  #{'a': 1, 'b': 2}  关键字收集实参打包成字典

func(1,2,3,4,a=1,b=2,e=3)
# func(1,2,3,4,a=1,b=2) # 报错 e是命名关键字形参,实参必须写e=3的形式
#TypeError: func() missing 1 required keyword-only argument: 'e'

# ### 星号的使用
# 1 * 和 ** 如果在函数的定义处使用:形参处打包
	# *  把多余的普通实参打包成元组
	# ** 把多余的关键字实参打包成字典
	
# 2 * 和 ** 如果在函数的调用处使用:实参处解包
	# *   把元组或者列表进行解包  #注意:还有列表
	# **  把字典进行解包			字典解包成关键字实参

def func(a,b,*,c,d):
	print(a,b) #	1 2
	print(c,d) #3 4

tup = (1,2)
# 函数的调用处 *号用法
func(*tup,c=3,d=4)  #func(1,2,c=3,d=4)

# 函数的调用处 **号用法
dic = {"c":3,"d":4}
func(1,2,**dic)  #func(1,2,c=3,d=4)
# func(**dic,1,2)  #func(c=3,d=4,1,2)  报错
# SyntaxError: positional argument follows keyword argument unpacking

# 定义成如下形式,可以收集所有的实参
def func(*args,**kwargs):
	pass
	
# 形参的顺序
# 普通形参==>默认形参==>普通收集形参==>命名关键字形参==>关键字收集形参

def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)









































