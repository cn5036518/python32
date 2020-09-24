# ### nonlocal的使用 (用来修改局部变量)
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
		print(a)
	inner()
	print(a)
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
		print(a)  #30
	inner()
	print(a)  #20
outer()  # 30 30 20

# (3)如果最后找不到,直接报错
"""nonlocal 只能修改局部变量,而不能修改全局变量"""
"""
a = 20
def outer():	
	def inner():
		def smaller():
			nonlocal a
			a = 30
			print(a)
		smaller()
		print(a)
	inner()
	print(a)
outer()
error
"""


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



