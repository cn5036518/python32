# ### 进程池

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

# 获取的逻辑处理器
print(os.cpu_count()) # 2 linux   win-8

# """多条进程提前开辟,可触发多cpu的并行效果"""
# (1) 进程池 ProcessPoolExecutor
def func(i):
	# print(i)
	time.sleep(random.uniform(0.1,0.8))
	print('任务执行中 ...  start ... 进程号{}'.format(os.getpid()),i)
	print('任务执行中 ...  end ... 进程号{}'.format(os.getpid()),i)
	return i	
	
if __name__ == '__main__':
	lst = []
	# (1) 创建进程池对象
	# """默认参数是 系统最大的逻辑核心数 2-linux  win-8 我的"""
	p = ProcessPoolExecutor()
	# print(p)
	#<concurrent.futures.process.ProcessPoolExecutor object at 0x7fdf457d9b00>

	# (2) 异步提交任务
	# """submit(任务,参数1,参数2 ... )"""
	# """默认如果一个进程短时间内可以完成更多的任务,
	# 进程池就不会使用更多的进程来辅助完成 , 可以节省系统资源的损耗;"""
	for i in range(4):
		obj = p.submit(func,i)  #子进程 p = Process(target=func,args=(i,))
	# print(obj)
	#<Future at 0x7f906f891208 state=pending>
		# print(obj.result()) 不要写在这,导致程序同步,内部有阻塞  类似for内的join
		lst.append(obj)

	# (3) 获取当前任务的返回值
	for i in lst:
		print(i.result())

	# (4) shutdown 等待所有进程池里的进程执行完毕之后,再放行
	p.shutdown()  #类似join
	
	print('进程池结束')


# 任务执行中 ...  start ... 进程号7315 1
# 任务执行中 ...  end ... 进程号7315 1
# 任务执行中 ...  start ... 进程号7316 0
# 任务执行中 ...  end ... 进程号7316 0
# 0
# 1



























