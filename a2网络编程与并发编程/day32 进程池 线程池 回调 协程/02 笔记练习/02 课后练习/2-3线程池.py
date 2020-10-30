# ### 进程池 和 线程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

# (2) ThreadPoolExecutor
from threading import currentThread as ct
# from threading import current_thread as ct

def func(i):
	time.sleep(random.uniform(0.1,0.8))
	print(' 任务执行中 ...  start ... 线程号{}'.format(ct().ident),i)
	# 注意:ct().ident )如果写错了,pycharm没有报错提示
	# time.sleep(1)
	print('任务执行中 ...  end ... 线程号{}'.format(ct().ident),i)
	return ct().ident  #线程号

if __name__ == '__main__':
	lst = []
	setvar = set()
	# """默认参数是 系统最大的逻辑核心数 8 * 5 = 40"""  win是8 linix是2
	# """默认参数是 系统最大的逻辑核心数 2 * 5 = 10"""  win是8 linix是2
	
	# (1) 创建线程池对象
	t = ThreadPoolExecutor()  #40
	# print(t)
	#<concurrent.futures.thread.ThreadPoolExecutor object at 0x7ff11792d518>

	# (2) 异步提交任务
	# """默认如果一个线程短时间内可以完成更多的任务,
	# 线程池就不会使用更多的线程来辅助完成 , 可以节省系统资源的损耗;"""
	for i in range(20):  #线程池有10个线程-linux,执行20个任务
		obj = t.submit(func,i) #子线程 t = Thread(targer=func,args=(i,))
		# print(obj.result()) 不要写在这,导致程序同步,内部有阻塞  (和join用法类似)
		lst.append(obj)
		
	# (3) 获取当前任务的返回值
	for i in lst:
		setvar.add(i.result())  #集合单个添加add  多个添加update  无序去重
		
	# (4) shutdown 等待所有线程池里的线程执行完毕之后,再放行
	t.shutdown()   #(和join用法类似)
		
	print('主线程执行结束')
	print(len(setvar),setvar)
# 10 {139725135169280, 139725126776576, 139725109991168, 139725101598464, 
# 139725118383872, 139725093205760, 139724748486400, 139724740093696, 
# 139724731700992, 139724723308288}


 # 任务执行中 ...  start ... 线程号139685731645184 4
# 任务执行中 ...  end ... 线程号139685731645184 4
 # 任务执行中 ...  start ... 线程号139685706467072 7
# 任务执行中 ...  end ... 线程号139685706467072 7
 # 任务执行中 ...  start ... 线程号139685756823296 1
# 任务执行中 ...  end ... 线程号139685756823296 1
 # 任务执行中 ...  start ... 线程号139685756823296 12























