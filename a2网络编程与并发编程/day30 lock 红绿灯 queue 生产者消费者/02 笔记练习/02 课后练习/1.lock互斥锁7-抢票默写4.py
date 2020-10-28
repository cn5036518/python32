# ### 12306 抢票软件

from multiprocessing import Process,Lock
import json,time,random

# 步骤
# 1 先主函数
# 2 后分函数
# 3 最后多进程

# 一 分函数
# 1.读写数据库当中的票数
def wr_info(sign,dic=None): 
	#1 读
	if sign == 'r':
		with open('ticket',mode='r',encoding='utf-8') as fp:
			dic = json.load(fp)
			print(dic)
			return dic
	
	#2 写
	elif sign == 'w':
		with open('ticket',mode='w',encoding='utf-8') as fp:
			json.dump(dic,fp)

wr_info('r')

# # 2.执行抢票的方法
# def get_ticket(person):
# 	#1 余票
# 	dic = wr_info('r')
# 	print(dic)
#
# 	#2 网络延时
# 	time.sleep(random.uniform(0.1,0.9))
#
# 	#3 余票判断
# 	if dic['count'] > 0:
# 		dic['count'] -= 1
# 		print('{}抢到票了.余票是{}张'.format(person,dic['count']))
# 		# wr_info('w')
# 		wr_info('w',dic)
#
# 	else:
# 		print('{} 票没了'.format(person))
#
#
# # 二 主函数
# # 3.对抢票和读写票数做一个统一的调用
# def main(person,lock):
# 	# 1 查票
# 	dic = wr_info('r')
# 	print('{}查票,余票是{}张'.format(person,dic['count']))
#
# 	# 2 上锁
# 	lock.acquire()
#
# 	# 3 抢票
# 	get_ticket(person)
#
# 	# 4 解锁
# 	lock.release()
#
#
# # 4 多进程
# if __name__ == "__main__":
# 	lock = Lock()
# 	lst = ['jack','tom','bob']
# 	for i in lst:
# 		p = Process(target=main,args=(i,lock))
# 		p.start()









































