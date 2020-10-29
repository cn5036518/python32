from threading import Thread,Lock
import random,time

n= 0

def func1(lock):
	global n
	# with(lock):  #自动上锁和解锁
	with lock:  #和with open类似
		for i in range(100000):  #10万
			n += 1
	
def func2(lock):
	global n
	# with lock:
	lock.acquire()
	for i in range(100000):
		n -= 1
	lock.release()
	
if __name__ == '__main__':
	lst = []
	lock = Lock()
	start = time.time()
	for i in range(10):
		t1 = Thread(target=func1,args=(lock,))
		t2 = Thread(target=func2,args=(lock,))
		
		t1.start()
		t2.start()
		
		lst.append(t1)
		lst.append(t2)

	for i in lst:
		i.join()
	end = time.time()
		
	print(n)  #47511
	print('总共耗时{}'.format(end-start))





























