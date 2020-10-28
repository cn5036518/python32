# ### 事件 Event
from threading import Thread,Event
import time,random

# wait   : 动态加阻塞 (True => 放行  False => 阻塞)
# is_set : 获取内部成员属性值是True 还是 False(默认是False)
# set    : 把False -> True
# clear  : 把True  -> False

# (1) 基本语法
# e = Event()
# print(e.is_set())  #False
#
# e.set()
# print(e.is_set())  #True
# e.wait()  #不阻塞
# print("代码执行中 ... 1")
#
# # e.clear()
# # print(e.is_set())
# # e.wait()  #阻塞
# # print("代码执行中 ...2 ")
#
# # e.clear()
# # print(e.is_set())
# # e.wait(2) #最多阻塞2秒后放行
# # print("代码执行中 ...3 ")
#
# e.set()
# print(e.is_set())
# e.wait(3)  #最多阻塞3秒后放行  这里是0秒后放行,没有任何阻塞
# print("代码执行中 ...4")
# print('------------------------------1')


# (2) 模拟连接远程数据库
# """最多连接三次,如果三次都连接不上,直接报错."""
def check(e):
	print('检测数据库的登录用户名和密码')
	time.sleep(random.randrange(1,6))
	e.set()  #从默认的False 改成 True
	print(e.is_set())  #True

def connect(e):
	for i in range(1,4):
	# 最多阻塞1秒
		e.wait(1)
		if e.is_set():
			print('数据库登录成功')
			break
		else:
			print('数据库登录第{}次失败'.format(i))
	else:
		raise TimeoutError

if __name__ == '__main__':
	e = Event()
	
	t1 = Thread(target=check,args=(e,))
	t1.start()
	
	t2 = Thread(target=connect,args=(e,))
	t2.start()



























































