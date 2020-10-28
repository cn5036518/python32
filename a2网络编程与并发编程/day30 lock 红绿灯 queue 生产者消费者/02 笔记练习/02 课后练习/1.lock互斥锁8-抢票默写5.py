from multiprocessing import Process,Lock
import json,os,time,random

# 思路:
# 读写文件数据
# 抢票

def wr_info(sign,dic={}):
	if sign == 'r':
		with open('ticket',mode='r',encoding='utf-8') as fp:
			dic = json.load(fp)
			return dic
	elif sign == 'w':
		with open('ticket',mode='w',encoding='utf-8') as fp:
			json.dump(dic,fp)

def get_ticket(person):
	# 1 获取票的数据
	dic = wr_info('r')
	
	# 2 网络延时
	time.sleep(random.uniform(0.1,0.5))
	
	# 3 判断票数
	if dic['count'] > 0:
		dic['count'] -= 1
		wr_info('w',dic)
		print('{} 买到票了,余票是{}张'.format(person,dic['count']))
	else:
		print('{} 没票了'.format(person))

	
def main(person,lock):
	# 1 查余票
	dic = wr_info('r')
	print('{}在查票,余票是{}张'.format(person,dic['count']))
	
	# 2 上锁
	lock.acquire()
	
	# 3  抢票
	get_ticket(person)
	
	# 4 解锁
	lock.release()
	
if __name__ == '__main__':
	lock = Lock()
	lst = ['jack','tom','bob']  #3个人抢票. 3个子进程
	for i in lst:
		p = Process(target=main,args=(i,lock))
		p.start()

# jack在查票,余票是93张
# tom在查票,余票是93张
# bob在查票,余票是93张
# jack 买到票了,余票是92张
# tom 买到票了,余票是91张
# bob 买到票了,余票是90张






































