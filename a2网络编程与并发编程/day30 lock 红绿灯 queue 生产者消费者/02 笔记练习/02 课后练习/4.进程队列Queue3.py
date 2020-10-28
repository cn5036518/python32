# 2.进程间的通信IPC  inter-process comunication
from multiprocessing import Process,Queue

def func(q):
	print(q.get())
	
	q.put(2)
	
if __name__ == '__main__':
	q = Queue()
	
	p = Process(target=func,args=(q,))
	p.start()
	
	q.put(1)
	
	p.join()  #等子进程执行完毕后,做放行join下面的代码
	
	print(q.get())












































