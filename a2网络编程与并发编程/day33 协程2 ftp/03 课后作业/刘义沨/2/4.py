from multiprocessing import Process,Event
import  time,random
def traffic_light(e):
	print("红灯亮")
	while True:
		if e.is_set():
			time.sleep(1):
			print("红灯亮")
			e.cleat()
		else:
			time.sleep(1)
			print("绿灯亮")
			e.set()

def car(e,i)
	if not e.is_set():
		print("car{}再等待".format(i))
		e.waite()
	print("car{}通行了".format(i))

if __name__=="__main__":
	e=Event()
	p1=Process(target=traffic_light,args=(e,))
	p1.start()
	for i in range(1,11):
		time.sleep(random.randrange(3))
		p2=Process(target=car,args=(e,i))
		p2.start