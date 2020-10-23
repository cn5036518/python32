# ### 全局变量和局部变量
# 1.概念
# 	局部变量:在函数内部定义的变量
# 	全局变量:在函数外定义的变量
# 			 或者在函数内部使用global关键字声明的
#
# 2.作用域
# 	局部变量的作用范围仅仅在函数的内部
# 	全局变量的作用范围横跨整个文件
#
# 3.生命周期:该变量的作用时长
# 	内置命名空间 --> 全局命名空间 --> 局部命名空间(开辟空间顺序)
# 	内置属性 > 全局属性 > 局部属性 (作用时长:长-->短)

# 1 局部变量
def func():
	# 定义一个局部变量
	a = 1
	
	# 获取当前的局部变量
	print(a)
	
	# 修改一个局部变量
	a = 2
	print(a)

func()
# print(a) #error
#NameError: name 'a' is not defined

# 2.全局变量
# 定义一个全局变量
b = 10

# 获取当前的全局变量
print(b)

# 修改一个全局变量
b = 20
print(b)  #20
print('-------------1')

def func():
	print(b)
func()  #20
print('-------------2')

# 3. 函数内部定义全局变量
def func():
	global c
	c = 30
func()
print(c)  #30
print('-------------3')

# 4.函数内部修改全局变量
d = 50
def func():
	global d
	d = 51
func()
print(d)  #51


# 小结:   
# 1 函数内部可以获取全局变量
# 2 函数内部不能直接修改全局变量
     # 要修改,必须通过global进行修改

# 变量的3个操作:定义 获取-print  修改

# 总结: global的使用
# 如果当前不存在全局变量,可以在函数内部通过global关键字来定义全局变量
# 如果当前存在全局变量,  可以在函数内部通过global关键字来修改全局变量


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





























