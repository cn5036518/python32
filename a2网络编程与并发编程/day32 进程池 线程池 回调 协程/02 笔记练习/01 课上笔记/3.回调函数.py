# ### 回调函数
# """
# 回调函数: 回头调用一下函数获取最后结果
# 回调函数: (服务端)回头调用一下(客户端)函数获取最后结果

# 微信支付宝付款成功后, 获取付款金额
# 微信支付宝退款成功后, 获取退款金额
# 一般用在获取最后的状态值时,使用回调
# 通过add_done_callback最后调用一下自定义的回调函数;
#  https://blog.csdn.net/TChenjx/article/details/51661173   参考链接
# """

# 打个比方，有一家旅馆提供叫醒服务，但是要求旅客自己决定叫醒的方法。
# 可以是打客房电话，也可以是派服务员去敲门，睡得死怕耽误事的，还可以要求往自己头上浇盆水。

# 这里，“叫醒”这个行为是旅馆提供的，相当于库函数(服务端)，
# 但是叫醒的方式是由旅客决定并告诉旅馆的，也就是回调函数(客户端)。

# 而旅客告诉旅馆怎么叫醒自己的动作，也就是把回调函数传入库函数的动作，
# 称为 登记回调函数（to register a callback function）

# 但是有些库函数(服务端)（library function）却要求应用(客户端)先传给它一个函数，
# 好在合适的时候调用，以完成目标任务。
# 这个被传入的、后又被调用的函数就称为 回调函数（callback function）。

# 这种灵活性是怎么实现的呢？乍看起来，回调似乎只是函数间的调用，
# 但仔细一琢磨，可以发现两者之间的一个关键的不同：

# 在回调中，我们利用某种方式，把回调函数像参数一样传入中间函数。
# 可以这么理解，在传入一个回调函数之前，中间函数是不完整的。
# 换句话说，程序可以在运行时，通过登记不同的回调函数，
# 来决定、改变中间函数的行为。这就比简单的函数调用要灵活太多了

from concurrent.futures import ProcessPoolExecutor , ThreadPoolExecutor
from threading import currentThread as ct
import os,time,random

# """进程任务"""
def func1(i):
	time.sleep(random.uniform(0.1,0.9))
	print(" 进程任务执行中 ...  start ... 进程号{}".format(os.getpid()) , i )
	print(" 进程任务执行中 ...  end ... 进程号{}".format(os.getpid()) )
	return i
	
def call_back1(obj):  #参数是对象
	print(   "<==回调函数的进程号{}==>".format(os.getpid())   )
	print(obj.result())  #异步获取返回值
	
# """线程任务"""	
def func2(i):
	time.sleep(random.uniform(0.1,0.9))
	print(" 线程任务执行中 ...  start ... 线程号{}".format(ct().ident) , i )
	print(" 线程任务执行中 ...  end ... 线程号{}".format( ct().ident) )
	return i
	
def call_back2(obj):   #参数是对象
	print(   "<==回调函数的线程号{}==>".format(  ct().ident) )
	print(obj.result())  #异步获取返回值
	


if __name__ == "__main__":


	# """		
	# (1)进程池  结果:(进程池的回调函数由主进程执行)
	# p = ProcessPoolExecutor() # os.cpu_count()  => 4
	# for i in range(1,11):
		# obj = p.submit(func1 , i )
		# 使用add_done_callback在获取最后返回值的时候,可以异步并行
		# obj.add_done_callback(call_back1)
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢;
		# obj.result()
	
	# p.shutdown()		
	# print(   "主进程执行结束...进程号:"    ,    os.getpid()  )
	# """
		
	print("<==============================================>")

	# (2)线程池  结果:(线程池的回调函数由子线程执行)
	t = ThreadPoolExecutor()
	for i in range(1,11):
		obj = t.submit(func2 , i )
		# 使用add_done_callback在获取最后返回值的时候,可以异步并发
		obj.add_done_callback(call_back2)
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢;
		# obj.result()
	t.shutdown()
	print("主线程执行结束 .... 线程号{}".format(ct().ident))
	
	
	
# """
# 原型:
class Ceshi():
	def add_done_callback(self,func): #2中间函数(库函数) 回调函数的调用者
		print("系统执行操作1 ... ")
		print("系统执行操作2 ... ")
		# 回头调用一下  调用回调函数  扩展和修改中间函数的功能
		func(self)
		
	def result(self):
		return 112233
	
def call_back(obj):   #1回调函数(应用) 形参是对象
	print(obj.result()) #修改这里,就能扩展和修改中间函数的功能


obj = Ceshi()
obj.add_done_callback(call_back)  #3起始函数(主函数):中间函数的调用者
# 对象调成员方法的时候,把回调函数的函数名call_back作为实参


# """


# 在回调中，我们利用某种方式，把回调函数像参数一样传入中间函数。
# 可以这么理解，在传入一个回调函数之前，中间函数是不完整的。
# 换句话说，程序可以在运行时，通过登记不同的回调函数，
# 来决定、改变中间函数的行为。这就比简单的函数调用要灵活太多了


# 回调函数:  把函数名字当做参数传递,然后,函数名(),就在调用函数
# 起始函数(主函数):中间函数的调用者,把回调函数的函数名call_back作为实参
# 回调函数的作用:扩展和修改中间函数(回调函数的调用者)的功能

# 闭包和装饰器:把函数名字当做返回值,然后,函数名(),就在调用函数
# 装饰器的作用:扩展原函数的功能





















