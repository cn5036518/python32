# ### 进程 process

import os,time

# ps -aux 查看进程号
# ps -aux | grep 2784 过滤查找2784这个进程

# 强制杀死进程
# kill -9 进程号

# 获取当前进程号
res = os.getpid()
print(res)

# 获取当前进程的父进程  pycharm
res = os.getppid()
print(res)

from multiprocessing import Process
# (1) 进程的使用
# def func():
# 	print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
# 	# 创建子进程 ,返回进程对象
# 	p = Process(target=func)
# 	# 调用子进程
# 	p.start()
#
# 	print('3.主进程id:{},4.父进程id:{}'.format(os.getpid(),os.getppid()))

# 3.主进程id:32993,4.父进程id:2297
# 1.子进程id:32994,2.父进程id:32993

# (2) 创建带有参数的进程

# def func(n):
# 	time.sleep(1)
# 	for i in range(1,n+1):
# 		# print(i)
# 		print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
# 	n = 6
# 	# target=指定任务  args = 参数元组
# 	p = Process(target=func,args=(n,))
# 	p.start()
#
# 	for i in range(1,n+1):
# 		print('*'*i)

# *
# **
# ***
# ****
# *****
# ******
# 1.子进程id:33687,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686
# 1.子进程id:33688,2.父进程id:33686

# (3) 进程之间的数据彼此隔离

# total = 100
# def func():
# 	global total
# 	total += 1
# 	print(total) #101  #子进程
#
# if __name__ == '__main__':
# 	p = Process(target=func)
# 	p.start()
#
# 	time.sleep(1)
# 	print(total)  #100  #主进程

# (4) 进程之间的异步性
# 1.多个进程之间是异步的并发程序,因为cpu调度策略问题,不一定先执行哪一个任务
# 默认来看,主进程执行速度稍快于子进程,因为子进程创建时,要分配空间资源可能会阻塞
# 阻塞态,cpu会立刻切换任务,以让程序整体的速度效率最大化

# 2.默认主进程要等待所有的子进程执行结束之后,
# 再统一关闭程序(关闭程序和执行代码不是一回事,代码执行完了,程序可以不关闭),
# 释放资源
# 若不等待,子进程可能不停的在系统的后台占用cpu和内存资源形成僵尸进程.
# 为了方便进程的管理,主进程默认等待子进程.再统一关闭程序;

def func(n):
	print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()),n)

if __name__ == '__main__':
	for i in range(1,11):
		p = Process(target=func,args=(i,))
		p.start()
		
	print('主进程执行结束了',os.getpid())

# 1.子进程id:36154,2.父进程id:36152 2
# 1.子进程id:36155,2.父进程id:36152 3
# 1.子进程id:36153,2.父进程id:36152 1
# 1.子进程id:36156,2.父进程id:36152 4
# 1.子进程id:36157,2.父进程id:36152 5
# 1.子进程id:36159,2.父进程id:36152 7
# 1.子进程id:36160,2.父进程id:36152 8
# 主进程执行结束了 36152
# 1.子进程id:36161,2.父进程id:36152 9
# 1.子进程id:36158,2.父进程id:36152 6
# 1.子进程id:36162,2.父进程id:36152 10




















































