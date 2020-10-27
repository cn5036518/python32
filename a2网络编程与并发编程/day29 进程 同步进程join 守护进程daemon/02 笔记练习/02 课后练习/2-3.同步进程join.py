# ### 1.同步主进程和子进程 : join
# """必须等待当前的这个子进程执行结束之后,再去执行下面的代码;,
# 用来同步子父进程;"""

from multiprocessing import Process
import time

# (1) join 的基本使用
# def func():
# 	print('发送第一封邮件 :  我的亲亲领导,你在么?')
#
# if __name__ == '__main__':
# 	p = Process(target=func)
# 	p.start()
# 	p.join() #在这里,主进程不会比子进程先执行
# 	print('发送第二封邮件 :  我想说,工资一个月给我涨到6万')

# 发送第一封邮件 :  我的亲亲领导,你在么?
# 发送第二封邮件 :  我想说,工资一个月给我涨到6万

# (2) 多进程场景中的join
# def func(i):
# 	time.sleep(1)
# 	print('发送第一封邮件{} :  我的亲亲领导,你在么?'.format(i))
#
# if __name__ == '__main__':
# 	lst = []
# 	for i in range(1,11):
# 		p = Process(target=func,args=(i,))
# 		p.start()
# 		# join 写在里面会导致程序变成同步
# 		lst.append(p)
#
# 	# 把所有的进程对象都放在列表中,统一使用.join进行管理;
# 	for i in lst:
# 		i.join()
#
# 	print('发送第二封邮件 :  我想说,工资一个月给我涨到6万')

# 发送第一封邮件1 :  我的亲亲领导,你在么?
# 发送第一封邮件2 :  我的亲亲领导,你在么?
# 发送第一封邮件3 :  我的亲亲领导,你在么?
# 发送第一封邮件4 :  我的亲亲领导,你在么?
# 发送第一封邮件5 :  我的亲亲领导,你在么?
# 发送第一封邮件7 :  我的亲亲领导,你在么?
# 发送第一封邮件6 :  我的亲亲领导,你在么?
# 发送第一封邮件8 :  我的亲亲领导,你在么?
# 发送第一封邮件10 :  我的亲亲领导,你在么?
# 发送第一封邮件9 :  我的亲亲领导,你在么?
# 发送第二封邮件 :  我想说,工资一个月给我涨到6万

# ### 2使用自定义进程类,创建进程

# (1) 基本语法
import os
#
# class MyProcess(Process):  #继承
# 	def run(self):  #重写run方法
# 		print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
#
# if __name__ == "__main__":
# 	p = MyProcess()
# 	p.start()
# 1.子进程id:39053,2.父进程id:39052

# (2) 带有参数的自定义进程类
class MyProcess(Process):
	def __init__(self,name):
		# 手动调用一下父类的构造方法,完成系统成员的初始化;
		super().__init__()  # super()只调用父类的成员,不会调自己的成员
		self.name = name
		
	def run(self):
		print('1.子进程id:{},2.父进程id:{}'.format(os.getpid(),os.getppid()))
		print(self.name)

if __name__ == '__main__':
	p = MyProcess('我是参数')
	p.start()

# 1.子进程id:39731,2.父进程id:39730
# 我是参数













































