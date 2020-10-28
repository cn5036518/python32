# ### JoinableQueue 队列
# """
# put 存放  
# get 获取  
# task_done 计算器属性值-1  
# join 配合task_done来使用 , 阻塞

# put 存储一次数据, 队列的内置计数器属性值+1
# get 获取一次数据, 通过task_done让队列的内置计数器属性值-1
	# get本身不-1
# join: 会根据队列计数器的属性值来判断是否阻塞或者放行
	# 队列计数器属性是 等于 0 ,  代码不阻塞放行
	# 队列计数器属性是 不等 0 ,  意味着代码阻塞
# """
from multiprocessing  import Queue,JoinableQueue,Process
import time,random

def consumer(q,name):
	while True:
		food = q.get()
		print('{}吃了{}'.format(name,food))
		q.task_done()  #计算器属性值-1 
	
def producer(q,name,food):
	for i in range(1,5):
		print('{}生产了{}'.format(name,food+str(i)))
		q.put(food+str(i))

if __name__ == '__main__':
	jq = JoinableQueue()
	
	p1 = Process(target=consumer,args=(jq,'tom'))
	p2 = Process(target=producer,args=(jq,'jack','peer'))
	p1.daemon = True  #守护进程
	
	p1.start()
	p2.start()
	
	p2.join()  #p2这个子进程全部执行完毕,才放行下面的代码
	# 必须等待队列中的所有数据全部消费完毕,再放行
	jq.join()  # 队列计数器属性是 等于 0 ,  代码不阻塞放行
	
	print("程序结束 ... ")






























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	