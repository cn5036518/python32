# (1) 多线程之间,数据共享

from threading import Thread,Lock
from multiprocessing import Process,Lock,Manager
import os,random,time

num = 100
def func():
	global num
	num -= 1
	
if __name__ == '__main__':
	lst = []
	for i in range(10):
		t = Thread(target=func)
		t.start()
		lst.append(t)
		
	for i in lst:
		i.join()
		
	print(num)  #90
print('-----------------------1 多线程之间,数据共享')
	
# (1) 多进程之间,数据隔离
num = 100
def func():
	global num
	num -= 1
	
if __name__ == '__main__':
	lst = []
	for i in range(10):
		t = Process(target=func)
		t.start()
		lst.append(t)
		
	for i in lst:
		i.join()
		
	print(num) #100
print('-----------------------2 多进程之间,数据隔离')











































