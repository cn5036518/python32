# ### nonlocal的使用 (用来修改局部变量,且只能修改局部变量)
"""
nonlocal遵循LEGB原则
(1) 它会找当前空间上一层的变量进行修改
(2) 如果上一层空间没有,继续向上寻找
(3) 如果最后找不到,直接报错
4   只能修改最近一层的局部变量,而无法修改最近一层之外的局部变量
"""

# (1)它会找当前空间上一层的变量进行修改
def outer():
	a = 10
	def inner():
		nonlocal a
		a = 20
		print(a)  #20
	inner()
	print(a)  #20
outer()  #20 20

# (2)如果上一层空间没有,继续向上寻找
def outer():
	a = 20
	def inner():
		a = 15  #30
		def smaller():
			nonlocal a
			a = 30
			print(a)  # 30
		smaller()
		print(a)  #30  一次只修改最近一层的局部变量
	inner()
	print(a)  #20  不变
outer()  # 30 30 20

# (3)如果最后找不到,直接报错
"""nonlocal 只能修改局部变量,而不能修改全局变量"""

# a = 20
# def outer():
# 	def inner():
# 		def smaller():
# 			nonlocal a  #SyntaxError: no binding for nonlocal 'a' found
# 			a = 30
# 			print(a)  #30
# 		smaller()
# 		print(a)
# 	inner()
# 	print(a)
# outer()
# # error



# (4) 不通过nonlocal 是否可以修改局部变量呢?ok
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] = 3000
		# 列表 字典等是引用类型,一改都改
	    # str  number是值类型,完全独立
	inner()
	print(lst)
outer()

#自己补充  20201018  yangyt
a = 20
def outer():
	a =2
	def inner():
		def smaller():
			nonlocal a
			a = 30
			print(a) #30
		smaller()
		print(a) #30  #第二步:执行32行 inner()调用的时候,31行的a没有值,就按照legb原则.从里向外找,就找到了24行的a,此时24行的a已经从2改成了30,所以这里打印30
	inner()
	print(a) #30  #第一步:执行30行 smaller()调用的时候,24行的a就从2改成了30了.所以这里打印30
outer()
print(a) #20
# 小结:对于多层嵌套函数,先看函数调用处,再看函数定义处.不要先看函数定义处(容易混淆),因为函数定义的时候,是不执行的,只有调用才会执行






















