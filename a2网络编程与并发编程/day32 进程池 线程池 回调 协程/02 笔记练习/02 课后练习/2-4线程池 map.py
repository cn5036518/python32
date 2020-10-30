# (3) 线程池 map
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from threading import currentThread as ct
from collections import Iterator,Iterable
import time,random

def func(i):
	time.sleep(random.uniform(0.1,0.8))
	print('thread ... 线程号{}'.format(ct().ident),i)
	# 注意:ct().ident )如果写错了,pycharm没有报错提示
	return '*' * i
	
if __name__ == '__main__':
	t = ThreadPoolExecutor()  #对象   默认2*5=10个子线程 linux 2  win8(逻辑处理器)
	#<concurrent.futures.thread.ThreadPoolExecutor object at 0x7f8b976b24e0>
	# print(t)
	it = t.map(func,range(10))  #2个cpu(逻辑处理器) 10个子线程执行10个任务
	# map的参数1是函数名,参数2是可迭代数据
	
	# 返回的数据是迭代器
	# print(isinstance(it,Iterator))  #True
	
	# 协调子父线程,等待线程池中所有子线程执行完毕之后,再放行下面的代码;
	t.shutdown()  # 和join类似
	
	# 获取迭代器里面的返回值 * 星星
	for i  in it:   #调用迭代器
		print(i)


# thread ... 线程号140558689621760 1
# thread ... 线程号140558664443648 4
# thread ... 线程号140558672836352 3
# thread ... 线程号140558307686144 6
# thread ... 线程号140558282508032 9
# thread ... 线程号140558299293440 7
# thread ... 线程号140558656050944 5
# thread ... 线程号140558698014464 0
# thread ... 线程号140558681229056 2
# thread ... 线程号140558290900736 8

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

# 总结: 无论是进程池还是线程池,都是由固定的进程数或者线程数来执行所有任务
# 系统不会额外创建多余的进程或者线程来执行任务;






































