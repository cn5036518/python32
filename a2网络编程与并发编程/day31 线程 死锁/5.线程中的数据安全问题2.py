# ### 线程中的数据安全问题

from threading import Thread,Lock
import time

n=0

def func1(lock):
	global n
	
	# lock.acquire()
	for i in range(100000):
		n += 1
	# lock.release()
	
def func2(lock):
	global n
	
	# with语法可以简化上锁+解锁的操作,自动完成
	# with lock:
	for i in range(100000):
		n -= 1
			
if __name__ == '__main__':
	lst = []
	lock = Lock()
	
	start = time.time()
	for i in range(10):
		t1 = Thread(target=func1,args=(lock,))
		t1.start()
		
		t2 = Thread(target=func2,args=(lock,))
		t2.start()
		
		lst.append(t1)
		lst.append(t2)
		
	for i in lst:
		i.join()
		
	end = time.time()
	print('主线程执行结束... 当前n结果为{} ,用时{}'.format(n,end-start))
# 主线程执行结束... 当前n结果为-92390 ,用时0.22953391075134277
print('-----------------1 不加线程锁  数据不对')


n=0

def func1(lock):
	global n
	
	lock.acquire()
	for i in range(100000):
		n += 1
	lock.release()
	
def func2(lock):
	global n
	
	# with语法可以简化上锁+解锁的操作,自动完成
	with lock:  #和with open类似
		for i in range(100000):
			n -= 1
			
if __name__ == '__main__':
	lst = []
	lock = Lock()
	
	start = time.time()
	for i in range(10):
		t1 = Thread(target=func1,args=(lock,))
		t1.start()
		
		t2 = Thread(target=func2,args=(lock,))
		t2.start()
		
		lst.append(t1)
		lst.append(t2)
		
	for i in lst:
		i.join()
		
	end = time.time()
	print('主线程执行结束... 当前n结果为{} ,用时{}'.format(n,end-start))
# 主线程执行结束... 当前n结果为0 ,用时0.11082172393798828
print('-----------------2 加线程锁 数据准确')

#线程锁可以保证同一时间,只有一个线程在修改文件数据(数据库)



































