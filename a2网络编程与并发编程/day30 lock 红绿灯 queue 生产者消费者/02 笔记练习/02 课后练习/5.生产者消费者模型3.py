# 1.基础版生产者消费者模型
# """问题 : 当前模型,程序不能正常终止--有阻塞  消费者子进程一直在运行  """
# """
from multiprocessing import Process,Queue
import time,random
# 消费者模型
def consumer(q,name):
	while True:
		time.sleep(random.uniform(0.1,1))
		food = q.get()
		print('{}在吃{}'.format(name,food))	


# 生产者模型
def producer(q,name,food):
	for i in range(1,5):
		time.sleep(random.uniform(0.1,1))
		print('{}在生产{}'.format(name,food+str(i)))
		q.put(food+str(i))

	
# if __name__ == "__main__":
	# q = Queue()
	
	# p1 = Process(target=consumer,args=(q,'jack'))
	# p2 = Process(target=producer,args=(q,'tom','apple'))

	# p1.start()
	# p2.start()
	
	# p2.join()

# 2.优化模型
# """特点 : 手动在队列的最后,加入标识None, 终止消费者模型"""
# 消费者模型
def consumer(q,name):
	while True:
		time.sleep(random.uniform(0.1,1))
		food = q.get()
		if food is None:
			break
		print('{}在吃{}'.format(name,food))	


# 生产者模型
def producer(q,name,food):
	for i in range(1,5):
		time.sleep(random.uniform(0.1,1))
		print('{}在生产{}'.format(name,food+str(i)))
		q.put(food+str(i))

	
# if __name__ == "__main__":
	# q = Queue()
	
	# p1 = Process(target=consumer,args=(q,'jack'))
	# p2 = Process(target=producer,args=(q,'tom','apple'))

	# p1.start()
	# p2.start()
	
	# p2.join()
	p2.put(None)  #AttributeError: 'Process' object has no attribute 'put'
	# q.put(None)


# 3.多个生产者和消费者

# """ 问题 : 虽然可以解决问题 , 但是需要加入多个None  , 代码冗余"""
# 消费者模型
def consumer(q,name):
	while True:
		time.sleep(random.uniform(0.1,1))
		food = q.get()
		if food is None:
			break
		print('{}在吃{}'.format(name,food))	


# 生产者模型
def producer(q,name,food):
	for i in range(1,5):
		time.sleep(random.uniform(0.1,1))
		print('{}在生产{}'.format(name,food+str(i)))
		q.put(food+str(i))

	
if __name__ == "__main__":
	q = Queue()
	
	p1 = Process(target=consumer,args=(q,'jack'))
	p1_2 = Process(target=consumer,args=(q,'jack2'))
	
	p2 = Process(target=producer,args=(q,'tom','apple'))
	p2_2 = Process(target=producer,args=(q,'tom2','orange'))

	p1.start()
	p1_2.start()
	
	p2.start()
	p2_2.start()
	
	p2.join()
	p2_2.join()
	# p2.put(None)  #AttributeError: 'Process' object has no attribute 'put'
	q.put(None)
	q.put(None)
































































