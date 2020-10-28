# ### 信号量 Semaphore (线程)

# """同一时间对多个线程上多把锁"""
#GIL 全局解释器锁  历史原因  python1989  java1995
# python中  进程可以并发,也可以并行
#            线程只能并发,不能并行(即同一个时间点)
#             1个进程中的多个线程,只能是单个cpu运行,不能是多个cpu并行运行

# 并发:一个cpu同一时间不停执行多个程序
# 并行:多个cpu同一时间不停执行多个程序

from threading import Thread,Semaphore
import time,random
def func(i,sem):
	time.sleep(random.uniform(1,2.2))
	# with语法自动实现上锁 + 解锁
	with sem:
		print('我在电影院看电影 .... 我是{}号'.format(i))

if __name__ == '__main__':
	sem = Semaphore(5)  #同一个时间点,只能允许5个线程在运行
	for i in range(30):
		Thread(target=func,args=(i,sem)).start()
	print(1)

	# 创建线程是异步的,
	# 上锁的过程会导致程序变成同步;

































































