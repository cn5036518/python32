# 1.什么是匿名函数，语法:
func = lambda x:id(x)
print(func(100))  #11097472

# 2.配合三运运算符写一个过滤奇数的匿名函数
func = lambda x:True if x % 2 ==1 else False
res = func(3)
print(res)  #True

# 3.locals和globals什么区别
# locals 返回当前作用域的所有变量,返回的是字典
# globals 返回全局作用域的所有变量,返回的是字典
#  往全局变量中添加键值对,如果键是字符串,将键的引号去掉,就是一个全局变量

print(globals())
#'func': <function <lambda> at 0x7f481d6bc158>, 'res': True}
dic = globals()
dic['wangwen'] = 'teacher'
print(wangwen)  #teacher  #这里wangwen是一个新的全局变量

#创建变量的5种方法
a = 1  #第1种
a = b =1 #第2种
a,b = 1,3 # 第3种

# 第4种  globals
dic = globals()
dic['wangwen'] = 'teacher'
print(wangwen) 

# 第5种  exec
strvar = 'c=3'
# eval(strvar) #SyntaxError: invalid syntax
exec(strvar)  #
print(c)
print('--------------------------------3')

# 4.如何用字符串定义全局变量
dic = globals()
dic['wangwen'] = 'teacher4'
print(wangwen) 
print('--------------------------------4')

# 5.什么是迭代器
# 能被next函数调用,并且不断返回下一个值的对象就是迭代器-Iterator
# 取值到最后,无值可取,就返回stopiteration

# 6.如何定义迭代器
# it = iter(iterable)或者
# it = iterable.__iter__()

# 7.如何调用迭代器
# next(it)  #一次取一个

# next for  #用多少取多少
# for i in range(3):
	# next(it)

# for #全部取完
# for i in it:
	# print(i)

# list  #强转
# print(list(it))


# 8.如何判断迭代器
# from collections import  Iterator
# isinstance(it,Iterator)

# if __iter__ in dir(it) and __next__ in dir(it)

# 9.迭代器和可迭代对象的区别
# 迭代器Iterator是可迭代对象Iterable
# 可迭代对象不一定是迭代器

# 10 .dic = {97:"a",98:'b",99:"e"}
# 给你一个列表["a","b","c]=> [97,98,991

# 11. ""123 =>123 不使用int的情况下实现该操作;

# 12.filter过滤奇数
lst = [1,2,3,4,5,6]
def func(n):
	if n % 2 == 1:
		return True
	else:
		return False
	
it = filter(func,lst)
print(list(it))  #[1, 3, 5]
print('----------------------12')

# 13 . sorted 和sort区别
# sort 只能用于list
     # 会改变list本身
# sorted 可以适用于容器
       # 不会改变list本身,会新建一个list

# 14 .tup = (19,23,42,87）按照和10余数排序






















