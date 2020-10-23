# ### locals 与 globals 使用(了解)

# 一.locals 获取当前作用域所有的变量
# 1.全局变量
# locals 在函数外,获取的是打印之前的所有的全局变量
# locals 在函数内,获取的是调用之前的所有的局部变量

def func():
	a1 = 1
	b2 = 2
	
a = 1
b = 2
res = locals()
c = 3
print(res)  #这里的d不打印   locals 在函数外,获取的是打印之前的所有的全局变量(包含函数func)
d = 4
# {'func': <function func at 0x0000021D3618C1E0>, 'a': 1, 'b': 2, 'res': {...}, 'c': 3}
print('---------------1')

# 2.局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = locals()  #locals 在函数内,获取的是调用之前的所有的局部变量
	c3 = 3
	print(res)
	d4 = 4
c = 3
func()  #{'a1': 1, 'b2': 2}
d = 4
print('---------------2')

# 二.globals 只获取全局空间的全局变量
# globals 在函数外,获取的是打印之前所有的全局变量  py3.6
# globals 在函数外,获取的是所有的全局变量          py3.7
# globals 在函数内,获取的是调用之前所有的全局变量  py3.6
# globals 在函数内,获取的是所有的全局变量  py3.7

# 1.全局空间
def func():
	a1 = 1
	b2 = 2
	
a = 1
b = 2
res = globals()  #调用
c = 3
print(res)  #打印
d = 4
print('---------------3')
# {'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4}  py3.7
3.7

# 2.局部空间
a = 1
b = 2
def func():
	a1 = 1
	b2 = 2
	res = globals()
	c3 = 3
	print(res)
	d4 = 4
c = 3
func()  #调用
d = 4
print('---------------4')
# 'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4}  py3.7

# ### globals  返回的是内置系统的全局字典
dic = globals()
print(dic)
# # {'__name__': '__main__', '__doc__': None, '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002B7C7541CF8>,
#  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>,
#  '__file__': 'E:/python32/day11 匿名函数 迭代器
#  filter map reduce sorted/2-1local与globals.py', '__cached__': None,
#  'func': <function func at 0x000002B7C924BD08>,
#  'a': 1, 'b': 2, 'res': {...}, 'c': 3, 'd': 4, 'dic': {...}}

# 通过字符串可以创建全局变量
dic['wangwen'] = '18'  #放入字典的键值对的键 的名字就是 全局变量的名字
print(wangwen)  #18
print('---------------4')

# 批量创建全局变量
def func():
	dic = globals()
	for i in range(1,5):
		dic['a' + str(i)] = i
func()
print(a1,a2,a3,a4)  # 1 2 3 4
# 这里批量创建了4个全局变量 a1=1 a2=2 a3=3 a4=4
































