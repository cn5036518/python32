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
def traffic_light(e):   #
	# print('红灯亮')
	while True:		
		if e.is_set() is False:
			time.sleep(1)
			print('绿灯亮')
			e.set()   #True --不加阻塞
		elif e.is_set():
			time.sleep(1)
			print('红灯亮')
			e.clear()  #False --加阻塞							

# 车的状态
def car(e,i):  #
	if e.is_set() is False:  #is_set()默认是False--阻塞--红灯
		print('car{} 在等待...'.format(i))
		e.wait()   #注意点
	print('car{} 通行了...'.format(i))
	

# 1.全国红绿灯
if __name__ == '__main__':
	e = Event()
	# traffic_light(e)
	
	p1 = Process(target=traffic_light,args=(e,))
	p1.start()
	
	for i in range(1,5):
		time.sleep(random.randrange(3))
		p2 = Process(target=car,args=(e,i))
		p2.start()


		
# 2.包头红绿灯,没有车的时候,把红绿灯关了;
# if __name__ == "__main__":
	# pass




















































