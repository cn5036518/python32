#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/26 10:29

''''''
'''
# 1.使用return返回+-*/运算的结果
# 2.什么是全局变量和局部变量
全局变量:
	1.函数外的变量
	2.函数内用global定义的变量(注意点) 
	
局部变量:函数内的变量  

# 3.python的函数名怎么用?
函数名也是一个变量
1.当做实参来传递  map reduce filter sorted
2.当做返回值  return后面的
3.动态创建   a = func
4.动态销毁  del a
5.作为容器的元素  li = [func1,func2]   for i in li:

# 4.互相嵌套的多个函数获取变量时的规则
LEGB就近寻找原则,从里到外
L local             局部作用域
E enclosing         嵌套作用域(内函数之外,外函数之内)
G global            全局作用域
B builtin           内置作用域

# 5.如何修改函数嵌套中的变量  nonlocal 
1 nonlocal只能修改最近一层的局部变量
2 nonlocal不能修改全局变量
3 nonlocal一次只能修改一层局部变量
   如果修改了最近一层的局部变量,就不会同时修改最近一层之外(第二层,第三层等)的局部变量

# 6.如何在函数内修改全局变量   glocal
函数内,用global关键字来修改一个全局变量

# 7.什么是闭包函数,写一个闭包函数,
闭包函数:
1 内函数使用了外函数的局部变量
2 外函数的返回值是内函数的函数名

内函数是闭包函数
整个过程叫做闭包

# 8.闭包函数的特点和意义? 写一个计数器
1.内函数使用的那个外函数的局部变量的生命周期会变长
2.内函数使用的那个外函数的局部变量,外部(他人)无法修改,安全性

# 9.变量的生命周期排 序 规则.
内置命名空间 >  全局命名空间 > 局部命名空间

'''

# 1.使用return返回+-*/运算的结果
def func(num1,num2,sign):
	if sign == '+':
		return num1 + num2
	elif sign == '-':
		return num1 - num2
	elif sign == '*':
		return num1 * num2
	elif sign == '/':
		if num2 == 0:
			print('除数不能是零')
		else:
			return num1 / num2
	else:
		print('格式不对,请传入比如5+9')
res = func(1,2,'+')
res = func(1,0,'/')
print(res)  #3
print('------------------------1')

# 3.python的函数名怎么用?
# 函数名是个变量,当做变量来使用   函数名字也是一个全局变量
# 1.当做实参来传递  map reduce filter sorted
# it = map(func,iterable)

# 2.当做返回值  return后面的
# 3.动态创建
def func():
	print(1)

a = func  #
print(a)  #<function func at 0x000001C0B533B950>
a()  #1

# 4.动态销毁
del a
# print(a)  #NameError: name 'a' is not defined
print('------------------------3-4')

# 5.作为容器的元素
def func1():
	print(1)

def func2():
	print(2)

lst = [func1,func2]
for i in lst:
	i()
print('------------------------3-5')

# 5.如何修改函数嵌套中的变量  nonlocal
# 1 nonlocal只能修改最近一层的局部变量
# 2 nonlocal不能修改全局变量  
# 3 nonlocal一次只能修改一层局部变量
#    如果修改了最近一层的局部变量,就不会同时修改最近一层之外(第二层,第三层等)的局部变量

def outer():
	a = 3
	def inner():
		a = 2
		def smaller():
			nonlocal a
			a = 4
			print(a)  #4
		smaller()
		print(a)  #4
	inner()
	print(a) #3
outer()  # 4 4 3
print('------------------------5')

# 6.如何在函数内修改全局变量  global
a = 1
def func():
	global a
	a = 2
print(a)  #1  没有修改的原因是:func()函数没有调用

a = 1
def func():
	global a  #如果该变量,在全局范围内已经定义了,那么这里就是修改
	#         如果该变量,在全局范围内没有定义,那么这里就是新建一个全局变量
	a = 2
func()
print(a)  #2
print('------------------------6')

# 6-1 如何不通过nonlocal修改局部变量  引用类型(list dict) 值类型(str number)
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] = 400
		print(lst)  #[1,2,400]
		# list dict的元素是引用类型 一改都改
	    # str number是值类型  完全独立
	inner()
	print(lst)  #[1,2,400]
outer()
print('------------------------6-1')

# 7.什么是闭包函数,写一个闭包函数,
# 闭包函数:
# 1 内函数使用了外函数的局部变量
# 2 外函数的返回值是内函数的函数名
def outer():
	a = 10
	def inner():
		print(a)
	return inner

func2 = outer()
func2()  #10

# 7-1 除了用闭包的定义的2个条件来判断外,如何用函数 方法 属性来判断闭包
tup = func2.__closure__  #这里是属性,没有小括号
print(tup)  # 这个元组有内容,就说明是闭包
#(<cell at 0x0000029D0A750888: int object at 0x00007FFB0EF763B0>,)

# 7-2 除了print外,如何获取被延长生命周期的局部变量的值  cell_contents属性
print(tup[0].cell_contents)  #10
# cell_contents 的作用是获取对象的内容(值)
print('--------------7-2')

# print(func2.cell_contents)  #AttributeError: 'function' object has no attribute 'cell_contents'

# 8.闭包函数的特点和意义? 写一个计数器
# 1.内函数使用的那个外函数的局部变量的生命周期会变长
# 2.内函数使用的那个外函数的局部变量,外部(他人)无法修改,安全性

# 第一个 计数器，外部可以修改

n = 0
def click():
	global n  #修改全局变量
	n += 1
	print(n)

click()
click()
n = 100  #外部的修改
click()
click()

# 1
# 2
# 101
# 102
print('--------------8-1')

# 第二个 计数器，外部不可以修改
def click_mouse():
	n = 0  #这个局部变量，函数外是无法修改的
	def inner():
		nonlocal n  #修改最近一层的局部变量
		n += 1
		print(n)
	return inner
inner = click_mouse()
inner()
inner()
n = 100
inner()
inner()

# 1
# 2
# 3
# 4
print('--------------8-2')

# 扩展 全局变量是否可以直接修改局部变量？
def click():
	n = 0
	n += 1
	print(n)  #1 这里的n=1是局部变量

click()
n = 2
print(n)  #2 这里的n=2是全局变量






