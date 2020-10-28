# ### 守护线程 : 等待所有线程全部执行完毕之后,
# 自己再终止程序,守护所有线程
# 和守护进程不同,守护进程守护的是主进程

from threading import Thread
import time,os,random

def func1():
	while True:
		time.sleep(1)
		print("我是函数func1")
	
def func2():
	time.sleep(5)
	print("我是函数func2")
	
if __name__ == '__main__':
	t1 = Thread(target=func1)
	t2 = Thread(target=func2)
	
	# 设置守护线程 (启动前设置)
	t1.setDaemon(True)
	
	# p1.daemon = True   #设置守护进程的写法
	
	t1.start()
	t2.start()

	print("主线程执行结束.... ")

# 主线程执行结束.... 
# 我是函数func1
# 我是函数func1
# 我是函数func1
# 我是函数func1
# 我是函数func1
# 我是函数func2








































