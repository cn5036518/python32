# 2.优化模型
# """特点 : 手动在队列的最后,加入标识None, 终止消费者模型"""

# get() 获取
# """在获取不到任何数据时,会出现阻塞"""

from multiprocessing import Process,Queue
import time,random

def consumer(q,name):
	while True:
		food = q.get()
		if food is None:
			break
		time.sleep(random.randrange(2))
		print('{}吃了{}'.format(name,food))
		
	
def producer(q,name,food):
	for i in range(1,6):
		time.sleep(random.randrange(2))
		print('{}生产了{}'.format(name,food+str(i)))
		q.put(food+str(i))
	
if __name__ == '__main__':
	q = Queue()
	
	p1 = Process(target=consumer,args=(q,'jack'))
	p1.start()
	
	p2 = Process(target=producer,args=(q,'tom','apple'))
	p2.start()
	
	p2.join()
	q.put(None)

# tom生成了apple1
# tom生成了apple2
# tom生成了apple3
# tom生成了apple4
# tom生成了apple5
# jack吃了apple1
# jack吃了apple2
# jack吃了apple3
# jack吃了apple4
# jack吃了apple5

# tom生产了apple1
# jack吃了apple1
# tom生产了apple2
# jack吃了apple2
# tom生产了apple3
# jack吃了apple3
# tom生产了apple4
# jack吃了apple4
# tom生产了apple5
# jack吃了apple5


# tom生产了apple1
# tom生产了apple2
# jack吃了apple1
# tom生产了apple3
# jack吃了apple2
# jack吃了apple3
# tom生产了apple4
# jack吃了apple4
# tom生产了apple5
# jack吃了apple5
























