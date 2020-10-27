# ### 12306 抢票软件

from multiprocessing import Process,Lock
import json,time,random

# 一 分函数
# 1.读写数据库当中的票数
def wr_info(sign,dic=None): 
	if sign == 'r':
		with open('ticket',mode='r',encoding='utf-8') as fp:
			dic = json.load(fp)
			# print(dic,type(dic))
			#{'count': 100} <class 'dict'>
			return dic 
			
	elif sign == 'w':
		with open('ticket',mode='w',encoding='utf-8') as fp:#清空写入
			json.dump(dic,fp)
	

# 2.执行抢票的方法
def get_ticket(person): 
	# 1 查询余票
	dic = wr_info('r')
	
	# 2 网络延时
	time.sleep(random.uniform(0.1,0.7))
	
	# 3 判断票数
	if dic['count'] > 0:
		dic['count'] -= 1
		print('{}抢到票了,余票是{}张'.format(person,dic['count']))
		
		wr_info('w',dic)
	else:
		print('{}没票了'.format(person))

# 二 主函数
# 3.对抢票和读写票数做一个统一的调用
def main(person,lock):
	# 1 上锁
	lock.acquire()
	
	# 2 抢票
	get_ticket(person)
	
	# 3 解锁
	lock.release()


# 4 多进程
if __name__ == "__main__":
	lock = Lock()
	lst = ['tom','jack','bob']
	for i in lst:
		p = Process(target=main,args=(i,lock))
		p.start()
	










































