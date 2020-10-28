# ### Manager ( list 列表  ,  dict 字典 ) 进程之间共享数据
# 主进程和子进程通过队列或者Manager共享数据
from multiprocessing import Process , Manager ,Lock

#1 共享列表
def mywork(data,lock):
	data['count'] -= 10

	
if __name__ == "__main__":
	lst = []
	lock = Lock()
	m = Manager()
	
	data = m.dict({'count':5000})
	
	for i in range(10): #进程数小于1000.否则死机
		p = Process(target=mywork,args=(data,lock))
		p.start()
		lst.append(p)
		
	for i in lst:
		i.join()  #必须等所有子进程完成,才执行主进程,否则报错
		
	print(data)  #{'count': 4900}
print('-----------------------1 共享列表')


#2 共享字典
from multiprocessing import Lock,Process,Manager

def mywork(data,lock):
	data[0] -= 1

if __name__ == '__main__':
	lst = []
	lock = Lock()
	m = Manager()
	
	data = m.list([100,200,300])
	
	for i in range(10):
		p = Process(target=mywork,args=(data,lock))
		p.start()
		lst.append(p)
		
	for i in lst:
		i.join()
		
	print(data)  #[90, 200, 300]
print('-----------------------2 共享字典')
















































