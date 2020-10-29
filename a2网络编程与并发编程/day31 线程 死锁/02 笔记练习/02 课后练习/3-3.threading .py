# (1)必须继承父类Thread,来自定义线程类
# 重新父类的run方法

from threading import Thread,Lock
import os,time,random

class MyThread(Thread):
	def __init__(self,name):
		super().__init__()    #AssertionError: Thread.__init__() not called
		#手动调用父类的构造方法
		self.name = name

	def run(self):
		print('名字是{}'.format(self.name))
		#名字是jack
		
# if __name__ == '__main__':
	# t = MyThread('jack')
	# t.start()
# print('-------------------1')

# ### 线程中的相关属性
# """
# 线程.is_alive()    检测线程是否仍然存在
# 线程.setName()     设置线程名字
# 线程.getName()     获取线程名字
# 1.currentThread().ident 查看线程id号 
# 2.enumerate()        返回目前正在运行的线程列表
# 3.activeCount()      返回目前正在运行的线程数量
# """
# """
from threading import Thread,Lock,currentThread,enumerate,activeCount

def func():
	# pass
	time.sleep(1)	
	
if __name__ == "__main__":
	t = Thread(target=func)
	t.start()
	print(t.is_alive()) #True
	
	print(t.getName())  #Thread-1
	
	t.setName('api获取')
	print(t.getName())  #api获取
	
	print(currentThread().ident)  #140588132239104  每次会变 线程号

	print(enumerate())  #返回目前正在运行的线程列表  第一个是主线程
	#[<_MainThread(MainThread, started 140523256985344)>, <Thread(api获取, started 140523218917120)>]

	print(len(enumerate()))  #2
	print(activeCount())  #2


































