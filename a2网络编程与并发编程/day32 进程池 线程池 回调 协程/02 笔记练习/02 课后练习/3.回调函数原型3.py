# 原型:

class Ceshi():
	def add_done_callback(self,func):  #2中间函数(库函数) 回调函数的调用者
		print('系统执行操作1 ...')
		print('系统执行操作2 ...')
		# 回头调用一下   调用回调函数  扩展和修改中间函数的功能
		func(self)  #实参是类的对象
		
	def result(self):
		return 112233
		
def call_back(obj):#1回调函数(应用) 形参是对象
	print(obj.result())  #修改这里,就能扩展和修改中间函数的功能
	
# def result(self):
	# return 112233
	

obj = Ceshi()
obj.add_done_callback(call_back) #3起始函数(主函数):中间函数的调用者
# 对象调成员方法的时候,把回调函数的函数名call_back作为实参

# 系统执行操作1 ...
# 系统执行操作2 ...
# 112233   #调用原函数的结果


# 在回调中，我们利用某种方式，把回调函数像参数一样传入中间函数。
# 可以这么理解，在传入一个回调函数之前，中间函数是不完整的。
# 换句话说，程序可以在运行时，通过登记不同的回调函数，
# 来决定、改变中间函数的行为。这就比简单的函数调用要灵活太多了


# 回调函数:  把函数名字当做参数传递,然后,函数名(),就在调用函数
#3起始函数(主函数):中间函数的调用者,把回调函数的函数名call_back作为实参
# 回调函数的作用:扩展和修改中间函数(回调函数的调用者)的功能

# 闭包和装饰器:把函数名字当做返回值,然后,函数名(),就在调用函数
# 装饰器的作用:扩展原函数的功能




































