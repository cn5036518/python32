# ### 生产者和消费者模型 

# 爬虫案例
# 1号进程负责抓取其他多个网站中相关的关键字信息,正则匹配到队列中存储(mysql)
# 2号进程负责把队列中的内容拿取出来,将经过修饰后的内容布局到自个的网站中

# 1号进程可以理解成生产者
# 2号进程可以理解成消费者

# 从程序上来看 
	# 生产者负责存储数据 (put)
	# 消费者负责获取数据 (get)
	
# 生产者和消费者比较理想的模型:
	# 生产多少,消费多少 . 生产数据的速度 和 消费数据的速度 相对一致	

# 1.基础版生产者消费者模型
# """问题 : 当前模型,程序不能正常终止--有阻塞  消费者子进程一直在运行 """
from multiprocessing import Process,Queue
import time,random
# 消费者模型
def consumer(q,name):
	while True:
		# 获取队列中的数据
		food = q.get()
		time.sleep(random.uniform(0.1,1))
		print('{}吃了{}'.format(name,food))

# 生产者模型
def producer(q,name,food):
	for i in range(3):
		time.sleep(random.uniform(0.1,1))
		
		# 展示生产的数据
		print('{}生产了{}'.format(name,food+str(i)))
		
		# 存储生产的数据在队列中
		q.put(food+str(i))

# if __name__ == '__main__':
	# q = Queue()
	# p1 = Process(target=consumer,args=(q,'赵万里'))
	# p2 = Process(target=producer,args=(q,"赵沈阳" , "香蕉"))
	
	# p1.start()
	# p2.start()
	
	# p2.join()  #等到生产者子进程全部结束,再走join下面的代码(主进程)

# 赵沈阳生产了香蕉0
# 赵万里吃了香蕉0
# 赵沈阳生产了香蕉1
# 赵沈阳生产了香蕉2
# 赵万里吃了香蕉1
# 赵万里吃了香蕉2

# 2.优化模型
# """特点 : 手动在队列的最后,加入标识None, 终止消费者模型"""
from multiprocessing import Process,Queue
import time,random
# 消费者模型
def consumer(q,name):
	while True:
	# 获取队列中的数据
		food = q.get()
			# 如果最后一次获取的数据是None , 
		# 代表队列已经没有更多数据可以获取了,终止循环;
		if food is None:
			break
		time.sleep(random.uniform(0.1,1))
		print('{}吃了{}'.format(name,food))

# 生产者模型
def producer(q,name,food):
	for i in range(3):
		time.sleep(random.uniform(0.1,1))

		# 展示生产出来的数据
		print('{}生产了{}'.format(name,food+str(i)))
		# 存储生产出来的数据在队列中
		q.put(food+str(i))

# if __name__ == '__main__':
	# q = Queue()
	# p1 = Process(target=consumer,args=(q,'赵万里'))
	# p2 = Process(target=producer,args=(q,"赵沈阳" , "香蕉" ))

	# p1.start()
	# p2.start()
	
	# p2.join()   #等到生产者子进程全部结束,再走join下面的代码(主进程)
	# q.put(None)  # 香蕉0 香蕉1 香蕉2  None


# 赵沈阳生产了香蕉0
# 赵万里吃了香蕉0
# 赵沈阳生产了香蕉1
# 赵万里吃了香蕉1
# 赵沈阳生产了香蕉2
# 赵万里吃了香蕉2

# 3.多个生产者和消费者
# """ 问题 : 虽然可以解决问题 , 但是需要加入多个None  , 代码冗余"""
from multiprocessing import Process,Queue
import time,random
# 消费者模型
def consumer(q,name):
	while True:
		# 获取队列中的数据
		food = q.get()
			# 如果最后一次获取的数据是None , 
		# 代表队列已经没有更多数据可以获取了,终止循环;
		if food is None:
			break
		time.sleep(random.uniform(0.1,1))
		print('{}吃了{}'.format(name,food))

# 生产者模型
def producer(q,name,food):
	for i in range(3):
		time.sleep(random.uniform(0.1,1))

		# 展示生产出来的数据
		print('{}生产了{}'.format(name,food+str(i)))
		
		# 存储生产出来的数据在队列中
		q.put(food+str(i))

if __name__ == '__main__':
	q = Queue()
	p1 = Process(target=consumer,args=(q,'赵万里'))
	p1_1 = Process(target=consumer,args=(q,'赵世超'))
	
	p2 = Process(target=producer,args=(q,"赵沈阳" , "香蕉"))
	p2_2 = Process(target=producer,args=(q,"赵凤勇" , "大蒜"))

	p1.start()
	p1_1.start()
	
	p2.start()
	p2_2.start()

	# 等待所有数据填充完毕
	p2.join()   #等到生产者子进程2全部结束,再走join下面的代码(主进程)
	p2_2.join() #等到生产者子进程2_2全部结束,再走join下面的代码(主进程)

	# 把None 关键字放在整个队列的最后,作为跳出消费者循环的标识符;
	q.put(None)  # 给第一个消费者加一个None , 用来终止
	q.put(None)  # 给第二个消费者加一个None , 用来终止


# 赵凤勇生产了大蒜0
# 赵沈阳生产了香蕉0
# 赵凤勇生产了大蒜1
# 赵沈阳生产了香蕉1
# 赵万里吃了大蒜0
# 赵世超吃了香蕉0
# 赵沈阳生产了香蕉2
# 赵凤勇生产了大蒜2
# 赵万里吃了大蒜1
# 赵世超吃了香蕉1
# 赵万里吃了香蕉2
# 赵世超吃了大蒜2































