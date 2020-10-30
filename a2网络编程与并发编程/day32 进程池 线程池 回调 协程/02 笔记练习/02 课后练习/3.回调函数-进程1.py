# ### 回调函数

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

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread as ct
import os,time,random

# """进程任务"""
def func1(i):   #
	time.sleep(random.uniform(0.1,0.8))
	print('进程任务执行中 ...  start ... 进程号{}'.format(os.getpid()),i)
	print('进程任务执行中 ...  end ... 进程号{}'.format(os.getpid()),i)
	return i
	
def call_back1(obj):   #回调函数  参数是对象
	print('<==回调函数的进程号{}==>'.format(os.getpid()))
	print(obj.result())  #打印返回值

if __name__ == '__main__':
	# (1)进程池  结果:(进程池的回调函数由主进程执行)
	p = ProcessPoolExecutor()   # os.cpu_count()  => 2 linux 
	# print(p)
	# <concurrent.futures.process.ProcessPoolExecutor object at 0x7f14cfa2b9b0>
	for i in range(1,11):  #2个cpu(逻辑处理器) 10个子线程 10个任务
		obj = p.submit(func1,i)  #子进程 p = Process(taget=func,args=(i,))
		# 使用add_done_callback在获取最后返回值的时候,可以异步并行
		# print(obj)
		# <Future at 0x7f14cd408828 state=running>
		
		obj.add_done_callback(call_back1)
		#1把回调函数的函数名call_back1 
		
		# 直接使用result获取返回值的时候,会变成同步程序,速度慢;
		# obj.result()
		
	p.shutdown()  #子进程的join  等子线程全部运行完毕后,再放行下面的代码
	print('主进程执行结束...进程号:{}'.format(os.getpid()))
	

# 进程任务执行中 ...  start ... 进程号5306 2
# 进程任务执行中 ...  end ... 进程号5306 2
# <==回调函数的进程号5297==>
# 2
# 进程任务执行中 ...  start ... 进程号5305 1
# 进程任务执行中 ...  end ... 进程号5305 1
# <==回调函数的进程号5297==>
# 1
# 进程任务执行中 ...  start ... 进程号5306 10
# 进程任务执行中 ...  end ... 进程号5306 10
# <==回调函数的进程号5297==>
# 10
# 主进程执行结束...进程号:5297






















