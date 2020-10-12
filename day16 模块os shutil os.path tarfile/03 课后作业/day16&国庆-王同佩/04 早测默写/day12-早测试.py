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



# 6.如何定义迭代器
# 7.如何调用迭代器
# 8.如何判断迭代器
# 9.法代器和可迭代对象的区别
# 10 .dic = {97:"a",98:'b",99:"e"}
# 给你一个列表["a","b","c]=> [97,98,991
# 11. ""123 =>123 不使用int的情况下实现该操作;
# 12.filter过滤奇数
# 13 . sorted 和sort区别
# 14 .tup = (19,23,42,87）按照和10余数排序






















