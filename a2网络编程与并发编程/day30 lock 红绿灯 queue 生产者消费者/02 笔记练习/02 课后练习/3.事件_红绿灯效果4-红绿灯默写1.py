# ### 事件 (Event)

# 阻塞事件 ：
	# e = Event()生成事件对象e   
	# e.wait()动态给程序加阻塞 , 
	# 程序当中是否加阻塞完全取决于该对象中的is_set() [默认返回值是False-加阻塞]
    # 如果是True  不加阻塞
    # 如果是False 加阻塞

# 控制这个属性的值
    # set()方法     将这个属性的值改成True---不加阻塞
    # clear()方法   将这个属性的值改成False--加阻塞
    # is_set()方法  判断当前的属性是否为True  (默认上来是False-加阻塞)

from multiprocessing import Process,Event
import time,random



# ### 模拟经典红绿灯效果

# 红绿灯切换
def traffic_light(e):   #参数是 事件对象e 
	print('红灯亮')	
	while True:
		if e.is_set(): #True--不加阻塞--绿灯
			time.sleep(1)
			print('红灯亮')	
			e.clear()   #将这个属性的值改成False--加阻塞--红灯
							
		else:  #False--加阻塞--红灯
			time.sleep(1)
			print('绿灯亮')
			e.set()   # 将这个属性的值改成True---不加阻塞--绿灯
			
						

# 车的状态
def car(e,i):  #i是子进程车的编号  事件对象e 
	if not e.is_set():  #is_set()默认是False--阻塞
		print('car{}在等待'.format(i))
		e.wait()  #必须加上
	print('car{}通行了'.format(i))
	

# 1.全国红绿灯
if __name__ == '__main__':
	e = Event()

	#新建一个红绿灯子进程
	p1 = Process(target=traffic_light,args=(e,))
	p1.start()
	
	# 新建4个小车子进程
	for i in range(1,5):
		# time.sleep(random.randrange(2))
		p2 = Process(target=car,args=(e,i))
		p2.start()


		
# 2.包头红绿灯,没有车的时候,把红绿灯关了;
# if __name__ == "__main__":
	# pass




















































