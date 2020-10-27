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

# e = Event()
#
# # 默认属性值是False--阻塞.
# print(e.is_set()) #False
#
# # 判断内部成员属性是否是False
# e.wait()#阻塞
#
# # 如果是False , 代码程序阻塞
# print('代码执行中 ...')
print('-----------1')

e = Event()  #默认属性值是False--阻塞.

# 将这个属性的值改成True--不加阻塞
e.set()

# 判断内部成员属性是否是True
e.wait()

# 如果是True , 代码程序不阻塞
print('代码执行中')  #代码执行中
print('-----------2')

# 将这个属性的值改成False--阻塞
# e.clear()
# e.wait()
# print('代码执行中 .... 2')
# print('-----------3')

# e = Event()
#
# # wait(3) 代表最多等待3秒;  最多阻塞3秒后,放行下面的代码
# e.wait(3)
# print('代码执行中 .... 3')
# print('-----------4')

# ### 模拟经典红绿灯效果

# 红绿灯切换
def traffic_light(e):
	print('红灯亮')
	while True:
		if e.is_set(): #True  不加阻塞(绿灯行)
			# 绿灯状态 -> 切红灯
			time.sleep(1)
			print('红灯亮')
			# True => False
			e.clear()
			# 将这个属性的值改成False--加阻塞(红灯停)			
		else:  #False  加阻塞(红灯停)
			# 红灯状态 -> 切绿灯
			time.sleep(1)
			print('绿灯亮')
			# False => True
			e.set()
			# 将这个属性的值改成True---不加阻塞
			
# e = Event() #新建一个事件对象
# traffic_light(e)	
# 红灯亮
# 绿灯亮
# 红灯亮
# 绿灯亮

# 车的状态
def car(e,i):
	# 判断是否是红灯,如果是红灯,加上wait阻塞
	if not e.is_set():  #默认返回值是False-加阻塞
		print('car{} 在等待 ... '.format(i))
		e.wait()

	# 否则不是,代表绿灯通行;
	print('car{} 通行了 ...'.format(i))

# 1.全国红绿灯
# if __name__ == '__main__':
# 	e = Event()
#
# 	# 创建交通灯子进程
# 	p1 = Process(target=traffic_light,args=(e,))
# 	p1.start()
#
# 	# 创建小车子进程
# 	for i in range(1,5):
# 		time.sleep(random.randrange(2))
# 		p2 = Process(target=car,args=(e,i))
# 		p2.start()
		
# 2.包头红绿灯,没有车的时候,把红绿灯关了;
if __name__ == "__main__":

	lst = []
	e = Event()
	
	# 创建交通灯子进程
	p1 = Process(target=traffic_light , args=(e,))
	
	# 设置红绿灯子进程为守护进程
	p1.daemon = True
	p1.start()

	# 创建小车子进程
	for i in range(1,5):
		time.sleep(random.randrange(2))
		p2 = Process(target=car , args=(e,i))
		lst.append(p2)
		p2.start()
		
	# 让所有的小车全部跑完,把红绿灯炸飞
	print(lst)
	for i in lst:
		i.join()

	print("关闭成功 .... ")

# 红灯亮
# car3 在等待 ... 
# 绿灯亮
# car3 通行了 ...
# car2 通行了 ...
# car1 通行了 ...
# 红灯亮
# [<Process(Process-2, stopped)>, <Process(Process-3, stopped)>, <Process(Process-4, stopped)>, <Process(Process-5, started)>]
# car4 在等待 ... 
# 绿灯亮
# car4 通行了 ...
# 关闭成功 .... 



















































