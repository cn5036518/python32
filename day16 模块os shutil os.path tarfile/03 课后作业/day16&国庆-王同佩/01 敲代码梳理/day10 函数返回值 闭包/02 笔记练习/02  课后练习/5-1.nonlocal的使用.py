# ### nonlocal的使用 (用来修饰局部变量)
# nonlocal遵循LEGB原则
# 1 它会找当前空间上一层的变量进行修改
# 2 如果上一层空间没有,继续向上寻找
# 3 如果最后找不到,直接报错

# 1 它会找当前空间上一层的变量进行修改
def outer():
	a = 10
	def inner():
		nonlocal a
		a = 20
		print(a)  #20
	inner()
	print(a)  #20
outer()
print('------------------1')

# 2 如果上一层空间没有,继续向上寻找
def outer():
	a = 20
	def inner():
		a = 15
		def smaller():
			nonlocal a
			a = 30
			print(a)  #30
		smaller()
		print(a) #30  #只修改最近的一层
	inner()
	print(a)  #20  #最近的一层之外的 不修改
outer()
print('------------------2')

# 3 如果最后找不到,直接报错
# nonlocal 只能修改局部变量
# a  = 20
# def outer():
# 	def inner():
# 		def smaller():
# 			nonlocal a  #SyntaxError: no binding for nonlocal 'a' found
# 			a = 30
# 			print(a)  #
# 		smaller()
# 		print(a) #  #
# 	inner()
# 	print(a)  #  #
# outer()  #error
# 如果在局部变量,找不到目标,nonlocal是不能修改全局变量的(会报错)

# 4 不通过nonlocal 是否可以修改局部变量呢? 可以的
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] = 3000
		#列表 字典是引用类型,一改都改
		#number str是值类型,一改就是新建(完全独立)
	inner()
	print(lst)  #[1, 2, 3000]
outer()














































