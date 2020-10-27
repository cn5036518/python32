# ### 进程 process

import os,time

# ps -aux 查看进程号
# ps -aux | grep 2784 过滤查找2784这个进程

# 强制杀死进程
# kill -9 进程号

# 获取当前进程号
res = os.getpid()
print(res)  #9473 pid每次运行,都会变

# 获取当前进程的父进程
res = os.getppid()
print(res)  #2297  这个是pycharm的进程号  重启pycharm后,这个pid才会变

from multiprocessing import Process
# (1) 进程的使用
# def func():
# 	print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
#
# if __name__ == "__main__":
# 	# 创建子进程 ,返回进程对象
# 	p = Process(target=func)
# 	# 调用子进程
# 	p.start()
#
# 	print('3.主进程id:{},4.父进程id:{}'.format(os.getpid(),os.getppid()))
#
# # 3.主进程id:10478,4.父进程id:2297(pycharm的pid)
# # 1.子进程id:10479,2.父进程id:10478主进程id
#
# #父进程,当前文件运行后的进程
# # 子进程,就相当于在当前文件之外的其他文件(模块)上,写了一个代码,运行后的进程
print('------------1')

# (2) 创建带有参数的进程
# def func1(n):
# 	for i in range(1,n+1):
# 		print(i)
# 		print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
# 
# if __name__ == '__main__':
# 	n = 1
# 	# target = 指定任务  args = 参数元组
# 	p = Process(target=func1,args=(n,))
# 	p.start()
#
# 	for i in range(1,n+1):
# 		print('*'*i)

# *
# 1.子进程id:13467,2.父进程id:13466
# 1
# 1.子进程id:13468,2.父进程id:13466
print('------------2')

# (3) 进程之间的数据彼此隔离

# total = 100
# def func():
# 	global total
# 	total +=1
# 	print(total,'子进程')  #101
#
# # func() #101
#
# if __name__ == '__main__':
# 	p = Process(target=func)
# 	p.start()
#
# 	print(total,'主进程')  #100

# 100 主进程
# 101 子进程  相当于62-66行代码是在另外一个py文件


# (4) 进程之间的异步性

# 1.多个进程之间是异步的并发程序,因为cpu调度策略问题,不一定先执行哪一个任务
# 默认来看,主进程执行速度稍快于子进程,因为子进程创建时,要分配空间资源可能会阻塞
# 阻塞态,cpu会立刻切换任务,以让程序整体的速度效率最大化

# 2.默认主进程要等待所有的子进程执行结束之后,再统一关闭程序,释放资源
# 若不等待,子进程可能不停的在系统的后台占用cpu和内存资源形成僵尸进程.
# 为了方便进程的管理,主进程默认等待子进程.再统一关闭程序;

def func(n):
	print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()),n)

if __name__ == '__main__':
	for i in range(1,11):
		p = Process(target=func,args=(i,))
		p.start()
		
	print('主进程执行结束了',os.getpid())

# 1.子进程id:14911,2.父进程id:14910 1
# 1.子进程id:14912,2.父进程id:14910 2
# 1.子进程id:14914,2.父进程id:14910 4
# 1.子进程id:14915,2.父进程id:14910 5
# 1.子进程id:14916,2.父进程id:14910 6
# 1.子进程id:14918,2.父进程id:14910 8
# 1.子进程id:14917,2.父进程id:14910 7
# 1.子进程id:14913,2.父进程id:14910 3
# 主进程执行结束了 14910
# 1.子进程id:14920,2.父进程id:14910 10
# 1.子进程id:14919,2.父进程id:14910 9































