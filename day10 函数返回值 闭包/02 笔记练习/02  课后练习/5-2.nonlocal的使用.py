# (1)它会找当前空间上一层的变量进行修改
def outer():
	a = 10
	def inner():
		nonlocal a   #nonlocal修改最近一层的局部变量,nonlocal不能修改全局变量
		a = 20
		print(a)  #20
	inner()
	print(a) #20 
outer()  #20 20
print('---------------1')

# (2)如果上一层空间没有,继续向上寻找
def outer():
	a = 20
	def inner():
		a = 15
		def smaller():
			nonlocal a
			a = 30
			print(a) #30
		smaller()
		print(a)  #30  #nonlocal 只修改最近的一层的局部变量,之外的不修改
	inner()
	print(a)  #20
outer()  # 30 30 20
print('---------------2')

# (3)如果最后找不到,直接报错
# """nonlocal 只能修改局部变量,而不能修改全局变量"""
# a = 20 # 全局变量
# def outer():
	# def inner():
		# def smaller():
			# nonlocal a  #SyntaxError: no binding for nonlocal 'a' found
			# a = 30
			# print(a) #30
		# smaller()
		# print(a)
	# inner()
	# print(a)
# outer()

# (4) 不通过nonlocal 是否可以修改局部变量呢?ok
def outer():
	lst = [1,2,3]
	def inner():
		lst[-1] = 3000
		# list dict 等是引用类型,一改都改
		# str numbers是值类型,完全独立
	inner()
	print(lst)  #[1, 2, 3000]
outer()  #[1, 2, 3000]



































