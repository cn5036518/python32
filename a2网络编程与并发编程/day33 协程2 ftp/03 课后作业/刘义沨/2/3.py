import  time
def alive():
	while True:
		print("讲师机向总监控服务器发送报活信息")
		time.sleep(1)
def func():
	while True:
		try:
			print("讲师机负责抗住50用户量的并发访问")
			time.sleep(5)
			raise RuntimeError
		except:
			print("讲师机扛不住了")
			break
if __name__ == "__main__":
	p1 = Process(target=alive)
	p2 = Process(target=func)
	p1.daemon = True
	p1.start()
	p2.start()
	p2.join()
	print("主进程执行结束...")