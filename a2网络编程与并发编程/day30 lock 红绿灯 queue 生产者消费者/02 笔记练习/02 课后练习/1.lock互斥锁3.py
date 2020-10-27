# ### 12306 抢票软件

from multiprocessing import Process,Lock
import json,time,random

# 1.读写数据库当中的票数
def wr_info(sign,dic=None):  #参数1是 r w
	if sign == 'r':
		with open('ticket',mode='r',encoding='utf-8') as fp:
			dic = json.load(fp)
			# print(dic,type(dic)) 
			#{'count': 1} <class 'dict'>
			return dic
		
	elif sign == 'w':
		with open('ticket',mode='w',encoding='utf-8') as fp:
		# 清空重写
			json.dump(dic,fp)		

# 2.执行抢票的方法
def get_ticket(person): #参数是抢票人
	# 01先获取数据库中实际票数
	dic = wr_info('r')
	
	# 02模拟一下网络延迟
	time.sleep(random.uniform(0.1,0.7))
	
	# 03判断票数
	if dic['count'] > 0:		
		# 01抢到票后,让当前票数减1
		dic['count'] -= 1
		
		print('{}抢到票了,余票是{}张'.format(person,dic['count']))
		
		# 02更新数据库中的票数
		wr_info('w',dic)
		
	else:
		print('{}没有抢到票哦'.format(person))

# get_ticket('jack') 
# jack没有抢到票哦

# 3.对抢票和读写票数做一个统一的调用
def main(person,lock):
	# 01查看剩余票数
	dic = wr_info('r')
	print('{}查看票数剩余: {}张'.format(person,dic['count']))
	
	# 02上锁
	lock.acquire()
	
	# 03开始抢票
	get_ticket(person)
	
	# 04解锁 
	lock.release()
	

# lock = Lock()
# main('tom',lock)  
# tom查看票数剩余: 4张
# tom抢到票了,余票是3张

if __name__ == "__main__":
	# wr_info('r')
	lock = Lock()
	lst = ["梁新宇","康裕康","张保张","于朝志","薛宇健"]
	for i in lst:
		p = Process(target=main,args=(i,lock))
		p.start()

# 梁新宇查看票数剩余: 3张
# 康裕康查看票数剩余: 3张
# 张保张查看票数剩余: 3张
# 于朝志查看票数剩余: 3张
# 薛宇健查看票数剩余: 3张
# 梁新宇抢到票了,余票是2张
# 康裕康抢到票了,余票是1张
# 张保张抢到票了,余票是0张
# 于朝志没有抢到票哦
# 薛宇健没有抢到票哦










































