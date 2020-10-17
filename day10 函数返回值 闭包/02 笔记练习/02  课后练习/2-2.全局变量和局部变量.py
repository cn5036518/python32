# 1 局部变量
def func():
	a = 1  #定义
	print(a) #获取
	a = 2  #修改
	print(a)
func()
print('-----------------1')

# 2 全局变量
b = 10  #定义
print(b) #获取
b = 20  #修改
print(b)
print('-----------------2')

def func():
	print(b)  #全局变量可以在函数内获取
func()  #20

#补充
# https://www.yht7.com/news/20627

# 变量作用域
# 一般在函数体外定义的变量成为全局变量，在函数内部定义的变量称为局部变量。

# 全局变量所有作用域都可用，局部变量只能在本函数可用，变量的使用顺序是，局部变量 > 全局变量, 也就是说：优先使用局部变量



# 那么问题来了， 如果想在函数内使用全局变量，或改变全局变量的值， 应该怎么做呢？



# global关键字
# 为了解决函数内使用全局变量的问题，python增加了global关键字， 利用它的特性， 可以指定变量的作用域。

# global关键字的作用：声明变量var是全局的



# 代码实例
# 实例1：
# 函数优先使用局部变量

str = 'global'
def func1():
    str = 'local'
    print(str)
func1()
print(str)
# 结果：

# local
# global
print('--------------------1 str 函数优先使用局部变量')


# 实例2：
# 在没有局部变量的情况下， 使用全局变量

str = 'global'
def func1():
    print(str)
func1()
print(str)
# 结果：

# global
# global
print('--------------------2 str 在没有局部变量的情况下， 使用全局变量')


# 实例3：
# 改变全局变量的值， 通过实例1可以看到， 函数内赋值并不能改变全局变量的值，所以需要global关键字

str = 'global'
def func1():
    global str
    str = 'local'
    print(str)
func1()
print(str)


# 结果：

# local
# local
print('--------------------3 str  局部变量改变全局变量的值 必须用global')


# 其他用法
# 你可以使用同一个global语句指定多个全局变量。

# 例如

# global var1, var2, var3


# 特殊类型
# 字符串、数字类型是不能被在局部被修改的(因为str int是值类型,不可变)，除非使用global关键字，
# 但是 列表，字典是可修改(因为list dict是引用类型,可变)，但不能重新赋值，如果需要重新赋值，需要在函数内部使用global定义全局变量



# 代码实例1：
list = ['global', 'pythontab.com']
def func1():
    list.append('bbs.pythontab.com')
    print(list)
func1()
print(list)
# 结果：

# ['global', 'pythontab.com', 'bbs.pythontab.com']
# ['global', 'pythontab.com', 'bbs.pythontab.com']


# 发现上面的list并没有使用global但是值却改变了， 说明列表是可以在局部被修改的
print('--------------------1 list  局部变量改变(append 而不是赋值)全局变量的值 list dict不用global,这里和str int有不同')



# 代码实例2：
list = ['global', 'pythontab.com']
def func1():
    list = ['docs.pythontab.com']
    print(list)
func1()
print(list)
# 结果：

# ['docs.pythontab.com']
# ['global', 'pythontab.com']
# 局部变量赋值不能改变全局变量的值
print('--------------------2 list  局部变量赋值不能改变全局变量的值  这里和str int是相同的')



# 代码实例3：
list = ['global', 'pythontab.com']
def func1():
    global list
    list = 'docs.pythontab.com'
    print(list)
func1()
print(list)
# 结果：

# docs.pythontab.com
# docs.pythontab.com
# 使用了global关键字后， 变量被重新赋值

print('--------------------3 list  使用了global关键字后， 变量被重新赋值  这里和str int是相同的')
























