from multiprocessing import Process
import time


def alive():
	while True:
		print('我很好')
		time.sleep(1)
	
def func():
	while True:
		try:
			print('3号服务器负责抗住3万用户量的并发访问')
			time.sleep(3)			
			raise RunTimeError			
		except:
			print('3号服务器扛不住了.. 快来修理我')
			break
	
if __name__ == '__main__':
	p1 = Process(target=alive)
	p2 = Process(target=func)
	
	p1.daemon = True
	p1.start()
	p2.start()
	
	p2.join()
	print('主进程执行结束')

# 我很好
# 3号服务器负责抗住3万用户量的并发访问
# 我很好
# 我很好
# 我很好
# 3号服务器扛不住了.. 快来修理我
# 主进程执行结束






























