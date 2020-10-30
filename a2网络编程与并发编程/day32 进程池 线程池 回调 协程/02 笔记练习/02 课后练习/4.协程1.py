# ### 协程 

# 进程是资源分配的最小单位
# 线程是程序调度的最小单位
# 协程是线程实现的具体方式

# 总结:
# 在进程一定的情况下,开辟多个线程,
# 在线程一定的情况下,创建多个协程,
# 以便提高更大的并行并发


# (1) 用协程改写生产者消费者模型
def producer():
	for i in range(100):
		yield i  #生成器函数
		
def consumer(gen):
	for i in range(2):
		print(next(gen))
	
gen = producer() #生成器对象

# consumer(gen)	
# print("<==========>")
# consumer(gen)
# print("<==========>")
# consumer(gen)

# 0
# 1
# <==========>
# 2    #记住上次的位置
# 3
# <==========>
# 4
# 5	

# (2) greenlet 协程的早期版本
from greenlet import greenlet
import time
# """ switch 可以切换任务,但是需要手动切换"""
def eat():
	print('eat1')
	g2.switch()
	time.sleep(3)
	print('eat2')	

def play():
	print('play1')
	time.sleep(3)
	print('play2')
	g1.switch()
	
# g1 = greenlet(eat)	
# g2 = greenlet(play)	
# g1.switch()

# eat1
# play1
# play2
# eat2

# (3) 升级到gevent版本
# """自动进行任务上的切换,但是不能识别阻塞  比如:time.sleep(1)"""
import gevent

def eat():
	print('eat1')
	gevent.sleep(3)
	#time.sleep(3)
	print('eat2')

def play():
	print('play1')
	gevent.sleep(3)
	#time.sleep(3)
	print('play2')
	
# # 利用gevent.spawn创建协程对象g1
# g1 = gevent.spawn(eat)
#
# # 利用gevent.spawn创建协程对象g2
# g2 = gevent.spawn(play)
#
# # 如果不加join, 主线程直接结束任务,不会默认等待协程任务.
#
# # 阻塞,必须等待g1任务完成之后在放行
# g1.join()
#
# # 阻塞,必须等待g2任务完成之后在放行
# g2.join()
#
# print("主线程执行结束 ....  ")

# eat1
# play1
# eat2
# play2
# 主线程执行结束 .... 

# (4) 协程的终极版本;
from gevent import monkey
monkey.patch_all()
# """引入猴子补丁,可以实现所有的阻塞全部识别   阻塞 比如 time.sleep(1)"""

import time
import gevent

def eat():
	print('eat1')
	time.sleep(3)
	print('eat2')
	
def play():
	print('play1')
	time.sleep(3)
	print('play2')

# 利用gevent.spawn创建协程对象g1
g1 = gevent.spawn(eat)
# 利用gevent.spawn创建协程对象g2
g2 = gevent.spawn(play)
# 如果不加join, 主线程直接结束任务,不会默认等待协程任务.

# 阻塞,必须等待g1任务完成之后在放行
g1.join()
# 阻塞,必须等待g2任务完成之后在放行
g2.join()

print(" 主线程执行结束 ... ")

# eat1
# play1 #3秒后,eat2和play2几乎同时打印
# eat2   
# play2
 # 主线程执行结束 ... 

# 分号,利用分号可以把多行代码放在一行进行编写;
a = 1
b = 2
a = 1;b = 2
































