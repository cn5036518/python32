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


from multiprocessing import Process,Queue,JoinableQueue
import time,random

def consumer(q,name):
	while True:
		food = q.get()
		print('{}吃了{}'.format(name,food))
		q.task_done()
	
def producer(q,name,food):
	for i in range(5):
		print('{}生产了{}'.format(name,food+str(i)))
		q.put(food+str(i))
	
if __name__ == '__main__':
	q = JoinableQueue()
	
	p1 = Process(target=consumer,args=(q,'tom'))
	p2 = Process(target=producer,args=(q,'jack','apple'))
	
	
	p1.daemon = True  #守护进程
	p1.start()	
	p2.start()
	
	p2.join()  #p2进程执行完毕,才放行下面的代码
	q.join()  #队列计数器属性是 等于 0 ,  代码不阻塞放行
	
	print('主程序结束')






























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

	