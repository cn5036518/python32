# ### 互斥锁 死锁 递归锁
from threading import Thread,Lock,RLock
import time

# (1) 语法上的死锁
# """语法上的死锁: 是连续上锁不解锁"""
lock = Lock()
lock.acquire()
# lock.acquire() error
print('代码执行中 ... 1')
lock.release()
# lock.release()  RuntimeError: release unlocked lock


# """是两把完全不同的锁"""
lock1 = Lock()
lock2 = Lock()

lock1.acquire()
lock2.acquire()
print('代码执行中 ... 2')
lock2.release()
lock1.release()

# (2) 逻辑上的死锁
noodles_lock = Lock()
chopsticks_lock = Lock()

def eat1(name):
	noodles_lock.acquire()
	print('{}抢到面条了 ... '.format(name))
	chopsticks_lock.acquire()
	print('{}抢到筷子了 ...'.format(name))
	
	print('开始享受香菇青菜面 ...')
	time.sleep(0.5)
	
	chopsticks_lock.release()
	print('{}吃完了,满意的放下了筷子'.format(name))
	noodles_lock.release()
	print('{}吃完了,满意的放下了面条'.format(name))	
	
def eat2(name):
	chopsticks_lock.acquire()
	print('{}抢到筷子了2 ...'.format(name))
	noodles_lock.acquire()
	print('{}抢到面条了2 ... '.format(name))
	
	print("开始享受香菇青菜面 ... ")
	time.sleep(0.5)
	
	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))
	chopsticks_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))
	
	
# if __name__ == '__main__':
	# lst1 = ["康裕康","张宇"]
	# lst2 = ["张保张","赵沈阳"]
	# for name in lst1:
		# Thread(target=eat1,args=(name,)).start()
		
	# for name in lst2:
		# Thread(target=eat2,args=(name,)).start()
		
# 在linux下,出现同学a抢到了面条.同学b抢到了筷子的几率相对不大
# 在win下,出现同学a抢到了面条.同学b抢到了筷子的几率相对比较大,此时就是死锁

# (3) 使用递归锁
	# 递归锁的提出专门用来解决死锁现象
	# 用于快速解决线上项目死锁问题
	# 即使连续上锁,使用递归锁后也可以解锁,因为递归锁的作用在于解锁;

# 基本语法
rlock = RLock()
rlock.acquire()
# print("代码执行中 ... 3")
rlock.release()

noodles_lock = Lock()
chopsticks_lock = Lock()

# 让noodles_lock和chopsticks_lock 都等于递归锁
noodles_lock = chopsticks_lock = RLock()
# 一行解决死锁

def eat1(name):
	noodles_lock.acquire()
	print('{}抢到面条了 ... '.format(name))
	chopsticks_lock.acquire()
	print('{}抢到筷子了 ...'.format(name))
	
	print('开始享受香菇青菜面 ...')
	time.sleep(0.5)
	
	chopsticks_lock.release()
	print('{}吃完了,满意的放下了筷子'.format(name))
	noodles_lock.release()
	print('{}吃完了,满意的放下了面条'.format(name))	
	
def eat2(name):
	chopsticks_lock.acquire()
	print('{}抢到筷子了2 ...'.format(name))
	noodles_lock.acquire()
	print('{}抢到面条了2 ... '.format(name))
	
	print("开始享受香菇青菜面 ... ")
	time.sleep(0.5)
	
	noodles_lock.release()
	print("{}吃完了,满意的放下了面条".format(name))
	chopsticks_lock.release()
	print("{}吃完了,满意的放下了筷子".format(name))
	
	
# if __name__ == '__main__':
	# lst1 = ["康裕康","张宇"]
	# lst2 = ["张保张","赵沈阳"]
	# for name in lst1:
		# Thread(target=eat1,args=(name,)).start()
		
	# for name in lst2:
		# Thread(target=eat2,args=(name,)).start()
print('----------------------------3')

# (4) 尽量使用一把锁解决问题,(少用锁嵌套-2把锁,容易逻辑死锁)
lock = Lock()

def eat1(name):
	lock.acquire()
	print("{}抢到面条了 ... ".format(name))
	print("{}抢到筷子了 ... ".format(name))
	
	print("开始享受香菇青菜面 ... ")
	time.sleep(0.5)	

	print("{}吃完了,满意的放下了筷子".format(name))	
	print("{}吃完了,满意的放下了面条".format(name))
	lock.release()
	
	
def eat2(name):
	lock.acquire()
	print("{}抢到筷子了 ... ".format(name))
	print("{}抢到面条了 ... ".format(name))
	
	print("开始享受香菇青菜面 ... ")
	time.sleep(0.5)	

	print("{}吃完了,满意的放下了筷子".format(name))
	print("{}吃完了,满意的放下了筷子".format(name))
	lock.release()
	
# if __name__ == '__main__':
	# lst1 = ["康裕康","张宇"]
	# lst2 = ["张保张","赵沈阳"]
	
	# for name in lst1:
		# Thread(target=eat1,args=(name,)).start()
		
	# for name in lst2:
		# Thread(target=eat2,args=(name,)).start()
print('----------------------------4')


lock = Lock()

def eat1(name):
	with(lock):
		print("{}抢到面条了 ... ".format(name))
		print("{}抢到筷子了 ... ".format(name))
		
		print("开始享受香菇青菜面 ... ")
		time.sleep(0.5)	

		print("{}吃完了,满意的放下了筷子".format(name))	
		print("{}吃完了,满意的放下了面条".format(name))

	
	
def eat2(name):
	with(lock):
		print("{}抢到筷子了 ... ".format(name))
		print("{}抢到面条了 ... ".format(name))
		
		print("开始享受香菇青菜面 ... ")
		time.sleep(0.5)	

		print("{}吃完了,满意的放下了筷子".format(name))
		print("{}吃完了,满意的放下了筷子".format(name))
		# lock.release()
	
if __name__ == '__main__':
	lst1 = ["康裕康","张宇"]
	lst2 = ["张保张","赵沈阳"]
	
	for name in lst1:
		Thread(target=eat1,args=(name,)).start()
		
	for name in lst2:
		Thread(target=eat2,args=(name,)).start()
print('----------------------------5')




















