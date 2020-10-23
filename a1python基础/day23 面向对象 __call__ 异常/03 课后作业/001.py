# lst = []
# def func():
	# global  lst
	# lst = [1,2333]
	# lst.append(1)
	# print(lst)

# func()	
# print(lst)
# print('------------1')

# d = 50
# def func():
	# global d
	# d = 1
	# print(d) #1
# func()
# print(d)  #1
# print('------------2')


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
# outer()
# print(a) #20


def outer():
	x = 0  #1
	def click_num():
		nonlocal x
		x += 1  # x = x+1
		print(x) #1
	print(click_num,'--------1')  #<function outer.<locals>.click_num at 0x7f1b0ce07e18>
	return click_num  #
click_num2 = outer()  #获取内函数的内存地址
click_num2()  #第40行  

click_num()
x = 10000000000
click_num()
click_num()
print(outer)  #<function outer at 0x7f4aaeb32158>

















