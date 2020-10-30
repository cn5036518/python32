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

# 在回调中，我们利用某种方式，把回调函数像参数一样传入中间函数。
# 可以这么理解，在传入一个回调函数之前，中间函数是不完整的。
# 换句话说，程序可以在运行时，通过登记不同的回调函数，
# 来决定、改变中间函数的行为。这就比简单的函数调用要灵活太多了

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread as ct
import os,time,random

# """线程任务"""
def func2(i):
	time.sleep(random.uniform(0.1,0.8))
	print('线程任务执行中 ...  start ... 线程号{}'.format(ct().ident),i)
	print('线程任务执行中 ...  end ... 线程号{}'.format(ct().ident))
	return i
	
def call_back2(obj):
	print('<==回调函数的线程号{}==>'.format(ct().ident))
	print(obj.result())
	
if __name__ == '__main__':
	# (2)线程池  结果:(线程池的回调函数由子线程执行)
	t = ThreadPoolExecutor()  # 2个cpu  2*5=10个子线程  10个任务  linux
	for i in range(1,11):
		obj = t.submit(func2,i)  # 子线程 t = Thread(target=func2,args=(i,))
		# 使用add_done_callback在获取最后返回值的时候,可以异步并发
		obj.add_done_callback(call_back2)
		# 回调函数当参数传入
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢;
		obj.result()  #类似for内join的用法
		
	t.shutdown()  #所有的子线程执行完毕后,才放行下面的代码
	# 类似join的用法
	print('主线程执行结束 .... 线程号{}'.format(ct().ident))
	
# 线程任务执行中 ...  start ... 线程号140316951013120 9
# 线程任务执行中 ...  end ... 线程号140316951013120
# <==回调函数的线程号140316951013120==>
# 9
# 线程任务执行中 ...  start ... 线程号140316967798528 10
# 线程任务执行中 ...  end ... 线程号140316967798528
# <==回调函数的线程号140316967798528==>
# 10
# 主线程执行结束 .... 线程号140317035034368		































