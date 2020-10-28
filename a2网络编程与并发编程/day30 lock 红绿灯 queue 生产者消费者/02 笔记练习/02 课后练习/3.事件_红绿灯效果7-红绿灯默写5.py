# 思路
# 1 红绿灯
# 2 车
# 3 多进程


from multiprocessing import Process,Event
import time,random

# 1 红绿灯
def trafic_light(e):
	print('红灯亮') #默认阻塞-红灯
	while True:
		if e.is_set() is False:
			time.sleep(1)
			print('绿灯亮')
			e.set()
		elif e.is_set():
			time.sleep(1)
			print('红灯亮')
			e.clear()

# 2 车
def car(i,e):
	if e.is_set() is False:
		print('car{} 在等待..'.format(i))
		e.wait()
	print('car{} 通行了..'.format(i))


# 3 多进程
if __name__ == '__main__':
	e = Event()
	
	# 1 红绿灯子进程
	p = Process(target=trafic_light,args=(e,))
	p.start()
	
	# 2 4个小车子进程
	for i in range(1,5):
		p = Process(target=car,args=(i,e))
		p.start()

















































