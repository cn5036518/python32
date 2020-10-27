# ### 守护进程

# 守护进程守护的是主进程,当主进程所有代码执行完毕之后,
# 立刻强制杀死守护进程自己;

from multiprocessing import Process
import time

# (1) 基本语法
# def func():
# 	print('start... 当前的子进程')
# 	time.sleep(0.01)
# 	print('end... 当前的子进程')
#
# if __name__ == '__main__':
# 	p = Process(target=func)
# 	# 在进程启动之前,设置守护进程
# 	p.daemon = True
# 	p.start()
#
# 	time.sleep(0.01)
# 	print('主进程执行结束')

# start... 当前的子进程
# 主进程执行结束  #此时13行不会打印

# (2) 多个子进程的守护场景;
# """默认主进程等待所有非守护进程,也就是子进程执行结束之后,再关闭程序,释放资源
# 守护进程只要在主进程代码执行结束时,就会自动关闭;
# 执行代码和关闭程序是分开的,主进程可以先执行完代码,
# 但是不关闭程序,过一会再关闭程序

# def func1():
# 	print('start ... func1 执行当前子进程 ...')
# 	print('end ... func1 执行当前子进程 ...')
#
# def func2():
# 	count = 1
# 	while True:
# 		print('*' * count)
# 		time.sleep(1)
# 		count += 1
#
# if __name__ == '__main__':
# 	p1 = Process(target=func1)
# 	p2 = Process(target=func2)
#
# 	# 把p2这个进程变成守护进程;
# 	p2.daemon = True
# 	p1.start()
# 	p2.start()
#
# 	print('主进程执行结束')

# (3) 守护进程用途: 监控报活
def alive():
	while True:
		print('3号服务器向总监控服务器发送报活信息: i am ok~')
		time.sleep(1)

def func():
	while True:
		try:
			print('3号服务器负责抗住3万用户量的并发访问')
			time.sleep(3)
			
			# 主动抛出执行错误的异常,触发except分支
			raise RuntimeError			
		except:
			print('3号服务器扛不住了.. 快来修理')
			break

if __name__ == '__main__':
	p1 = Process(target=alive)
	p2 = Process(target=func)
	
	p1.daemon = True
	p1.start()
	p2.start()


















