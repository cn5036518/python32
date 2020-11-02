from multiprocessing import Process,Event
import time,random

def traffic_light(e):
	print('红灯亮')
	while True:
		if e.is_set() is False:
			time.sleep(1)
			print('绿灯亮')
			e.set()
		elif e.is_set():
			time.sleep(1)
			print('红灯亮')
			e.clear()
	
def car(i,e):
# def car(e,i):  参数位置不对
	if e.is_set() is False:
		print('car{} 在等待'.format(i))
		e.wait()
	print('car{} 通行了'.format(i))
	
if __name__ == '__main__':
	e = Event()
	
	p = Process(target=traffic_light,args=(e,))
	p.start()
	
	for i in range(1,5):
		p = Process(target=car,args=(i,e))
		p.start()
		
	


























