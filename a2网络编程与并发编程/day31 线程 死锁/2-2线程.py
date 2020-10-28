# ### 线程 
# 进程是资源分配的最小单元
# 线程是cpu执行调度的最小单元

# (1) 一个进程里包含了多个线程,线程之间是异步并发
from threading import Thread
from multiprocessing import Process
import os ,time,random

# def func(i):
	# time.sleep(random.uniform(0.1,0.9))
	# print('当前进程号:{}'.format(os.getpid(),i))

# if __name__ == '__main__':
	# for i in range(10):
		# t = Thread(target=func,args=(i,))
		# t.start()
		
# print(os.getpid())

# 5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651
# 当前进程号:5651


# (2) 并发的多进程和多线程之间,多线程的速度更快
# 多线程速度
# def func(i):
	# print('当前进程号:{} , 参数是{}'.format(os.getpid(),i))

# if __name__ == "__main__":
	# lst = []
	# starttime = time.time()
	# for i in range(1000):
		# t = Thread(target=func,args=(i,))
		# t.start()
		# lst.append(t)
	# for i in lst:
		# i.join()
	# endtime = time.time()
	# print('运行的时间是{}'.format(endtime-starttime))
	# 运行的时间是0.9315314292907715

# 多进程速度
# def func(i):
	# print('当前进程号:{} , 参数是{}'.format(os.getpid(),i))

# if __name__ == '__main__':
	# lst = []
	# startime = time.time()
	# for i in range(1000):
		# p = Process(target=func,args=(i,))
		# p.start()
		# lst.append(p)
	# for i in lst:
		# i.join()
	# endtime = time.time()
	# print('运行的时间是{}'.format(endtime-startime))
	# 运行的时间是4.300446271896362

# (3) 多线程之间,数据共享
num = 100
lst = []
def func():
	global num
	num -= 1
	
for i in range(100):
	t = Thread(target=func)
	t.start()
	lst.append(t)
	
for i in lst:
	i.join()  #进程同步
	
print(num)  #0
































