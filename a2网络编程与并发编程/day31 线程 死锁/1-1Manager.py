# ### Manager ( list 列表  ,  dict 字典 ) 进程之间共享数据
from multiprocessing import Process,Manager,Lock

# 1 共享列表
def mywork(data,lock):
	# 共享字典

	# 共享列表
	lock.acquire()  #
	data[0] += 1
	lock.release()
	
if __name__ == '__main__':
	lst = []
	m = Manager()
	lock = Lock()
	
	# 多进程中的共享列表
	data = m.list([100,200,300])
	print(data,type(data))
	
	# 进程数超过1000,处理该共享数据,死机(谨慎操作)
	for i in range(10):
		p = Process(target=mywork,args=(data,lock))
		p.start()
		lst.append(p)

	# 必须等待子进程所有计算完毕之后,再去打印该字典或列表,否则报错;
	#AttributeError: 'ForkAwareLocal' object has no attribute 'connection'
	for i in lst:
		i.join()
		
	print(data)
print('----------------1')

#2 共享字典
def mywork(data,lock):
	# 共享字典
	lock.acquire()
	data['count'] -= 10
	lock.release()
	
if __name__ == '__main__':	
	lst = []
	m = Manager()
	lock = Lock()
	
	# 多进程中的共享字典
	data = m.dict({'count':5000})
	print(data , type(data) )
	
	# 进程数超过1000,处理该共享数据,死机(谨慎操作)
	for i in range(10):
		p = Process(target=mywork,args=(data,lock))
		p.start()
		lst.append(p)
		
	# 必须等待子进程所有计算完毕之后,再去打印该字典,否则报错;
	#AttributeError: 'ForkAwareLocal' object has no attribute 'connection'
	for i in lst:
		i.join()
		
	print(data)
	




































