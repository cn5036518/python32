# ### 进程池 和 线程池
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import os,time,random

# 获取的逻辑处理器
print(os.cpu_count()) #linux 1  win 8


# """多条进程提前开辟,可触发多cpu的并行效果"""

# (1) 进程池 ProcessPoolExecutor
def func(i):
	print(' 任务执行中 ...  start ... 进程号{}'.format(os.getpid()))
	time.sleep(3)
	# time.sleep(random.randrange(1,4))
	print(' 任务执行中 ...  end ... 进程号{}'.format(os.getpid()))
	return i 
	
if __name__ == '__main__':
	lst = []
	# (1) 创建进程池对象
	# """默认参数是 系统最大的逻辑核心数 8"""
	p = ProcessPoolExecutor()
	
	# (2) 异步提交任务
	# """submit(任务,参数1,参数2 ... )"""
	# """默认如果一个进程短时间内可以完成更多的任务,
	# 进程池就不会使用更多的进程来辅助完成 , 可以节省系统资源的损耗;"""
	for i in range(10):
		obj = p.submit(func,i)   #子进程是 Process(target=func,args=(i,))
		# print(obj)  #<Future at 0x7f34e639e7b8 state=running>
		# print(obj.result()) #不要写在这,导致程序同步,内部有阻塞
		lst.append(obj)

	# (3) 获取当前任务的返回值
	for i in lst:
		print(i.result(),">===获取返回值===?")

	# (4) shutdown 等待所有进程池里的进程执行完毕之后,再放行 #类似 子进程的join
	p.shutdown()
	
	print('进程池结束')


 # 任务执行中 ...  start ... 进程号7831
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 0 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 1 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 2 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 3 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 4 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 5 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 6 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 7 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
 # 任务执行中 ...  start ... 进程号7831
# 8 >===获取返回值===?
 # 任务执行中 ...  end ... 进程号7831
# 9 >===获取返回值===?
# 进程池结束





























