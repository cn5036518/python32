# 思路
# 1 红绿灯
# 2 车
# 3 多线程


from multiprocessing import Process,Event
from threading import Thread,Event
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


# 3 多线程
if __name__ == '__main__':
	e = Event()
	
	# 1 红绿灯子线程
	# p = Process(target=trafic_light,args=(e,))
	t = Thread(target=trafic_light,args=(e,))
	t.start()
	
	# 2 4个小车子线程
	for i in range(1,5):
		# p = Process(target=car,args=(i,e))
		t = Thread(target=car,args=(i,e))
		t.start()


# 红灯亮
# car1 在等待..
# car2 在等待..
# car3 在等待..
# car4 在等待..
# 绿灯亮
# car1 通行了..
# car2 通行了..
# car3 通行了..
# car4 通行了..
# 红灯亮
# 绿灯亮














































