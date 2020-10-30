# ### 进程池

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random


def func(i):
	time.sleep(random.uniform(0.1,0.8))
	# 打印进程号
	print('当前子进程号{},{}'.format(os.getpid(),i))
	return i

	
if __name__ == '__main__':
	lst = []

	# (1) 创建进程池对象
	p = ProcessPoolExecutor()  #2 linux


	# (2) 异步提交任务
	for i in range(4):   #2个cpu  2个进程  4个任务
		obj = p.submit(func,i)
		lst.append(obj)


	# (3) 获取当前任务的返回值
	for i in lst:
		print(i.result())  #对象.result() 可以获取任务的返回值


	# (4) shutdown 等待所有进程池里的进程执行完毕之后,再放行
	p.shutdown()
	
	print('进程池结束')






























