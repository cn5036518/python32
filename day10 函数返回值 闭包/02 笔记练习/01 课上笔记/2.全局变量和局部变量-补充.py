# 一 str int
# 1
s1 = 'a'
def func():
	s1 = 'b'
	print(s1)  #'b'  #定义
func()
print(s1)  #'a'
print('------------------1 局部变量和全局变量 完全分开')

# 2
s1 = 'a'
def func():
	print(s1)  #'a'  #局部没有定义,获取全局变量的值
func()
print(s1)  #'a'
print('------------------2 局部没有定义,获取全局变量的值')

# 3
# num  = 1
# def func():
	# num = num + 1 
	# print(num)  #UnboundLocalError: local variable 'num' referenced before assignment
# func()
# print(s1)  #'a'
print('------------------3 int类型的局部变量修改全局变量,如果不使用global,就会报错')

num  = 1
def func():
	global num
	num = num + 1 
	print(num)  #2
func()
print(num)  #1
print('------------------4 int str类型的局部变量修改全局变量,必须使用global')


# 二 list dict
# 1
lst = [1,2]
def func():
	lst = [1,2,3]
	print(lst)  #[1,2,3]
func()
print(lst)  #[1,2]
print('------------------1 list dict局部变量和全局变量 完全分开   和str int一样')

# 2
lst = [1,2]
def func():
	print(lst)  #[1,2]
func()
print(lst)  #[1,2]
print('------------------2 局部没有定义,获取全局变量的值   和str int一样')

# 3
lst = [1,2]
def func():
	lst.append(33)
	print(lst)  #[1,2,33]
func()
print(lst)  #[1,2,33]
print('------------------3 list dict不用global,也可以在函数内修改全局变量  lst.append()   和str int不一样')  #特别注意

# 3-2
dic = {}
def func():
	dic['name'] = 'jack'
	print(dic)  #{'name':'jack'}
func()
print(dic)  #{'name':'jack'}
print('------------------3-2 list dict不用global,也可以在函数内修改全局变量 dic添加键值对   和str int不一样')  #特别注意


# 4
# 3
lst = [1,2]
def func():
	global lst
	lst = [1,2,333]
	print(lst)  #[1,2,333]
func()
print(lst)  #[1,2,333]
print('------------------3 list dict在函数内,重新赋值后,用global,也可以修改全局变量   和str int一样')  #




























