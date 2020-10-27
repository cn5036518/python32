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
		if e.is_set(): #True 不加阻塞   绿灯行==>红灯停
			time.sleep(1)
			e.clear()  # True==>False
			print('红灯亮')
			
		else:# 默认False 阻塞  红灯停==>绿灯行
			time.sleep(1)
			e.set()   # False==>True
			print('绿灯亮')
	
# e = Event()
# traffic_light(e)	
# 红灯亮
# 绿灯亮
# 红灯亮
# 绿灯亮

# 车的状态
def car(e,i):  #i是子进程车的编号  事件对象e 
	if not e.is_set(): # is_set()默认False 阻塞--车等待		
		print('car{} 在等待 ... '.format(i))
		e.wait()  #阻塞
	# elif e.is_set():  # is_set()是True 不阻塞--车通行
	# else:  # 
	print('car{} 通行了 ...'.format(i))		
	

# 1.全国红绿灯
if __name__ == '__main__':
	e = Event()
	
	# 创建交通灯子进程 1个子进程
	p1 = Process(target=traffic_light,args=(e,) )
	p1.start()	

	# 创建小车子进程  4个子进程 4个车
	for i in range(1,5):  #1 2 3 4
		# time.sleep(random.randrange(2))
		p2 = Process(target=car,args=(e,i))
		p2.start()


		
# 2.包头红绿灯,没有车的时候,把红绿灯关了;
# if __name__ == "__main__":
	# pass


# car1 在等待 ... 
# car2 在等待 ... 
# 红灯亮
# car4 在等待 ... 
# car3 在等待 ... 
# 绿灯亮
# car2 通行了 ...
# car4 通行了 ...
# car1 通行了 ...
# car3 通行了 ...

#创建小车子进程 不加随机时间
# 红灯亮
# car2 在等待 ... 
# car3 在等待 ... 
# car4 在等待 ... 
# car1 在等待 ... 
# 绿灯亮
# car3 通行了 ...
# car4 通行了 ...
# car2 通行了 ...
# car1 通行了 ...
# 红灯亮
# 绿灯亮

















































