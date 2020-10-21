import time


class View():
	def login():
		name = input("请输入管理员的账户:")
		pwd = input("请输入管理员密码:")
		if name == "admin" and pwd == "111":
			View.welcome()
			time.sleep(0.5)
			return True
		else:
			print("管理员用户密码错误")

	@staticmethod
	def welcome():
		print("*******************************************")
		print("*                                         *")
		print("*                                         *")
		print("*         Welcome To OldBoy Bank          *")
		print("*                                         *")
		print("*                                         *")
		print("*******************************************")
				
	@staticmethod
	def operation(card):
		if card:
			print(f"************** 登入卡号:{card.cardid} **************")
		else:
			print("*******************************************")
		print("*     卡号登录入口(C)     身份证登录入口(Z)    *")
		print("*     开户(1)           查询(2)            *")
		print("*     存钱(3)           取钱(4)            *")
		print("*     转账(5)           改密(6)            *")
		print("*     锁卡(7)           解卡(8)            *")
		print("*     补卡(9)           新卡(N)            *")
		print("*     登出(X)           退出(0)            *")
		print("*******************************************")

	@staticmethod
	def mode_choice(v):
		print('**************************')
		print(f'[1] 通过密码{v}')
		print(f'[2] 通过身份证{v}')
		print('**************************')

	@staticmethod
	def lst_show(lst):
		print('**************************')
		num = 1
		for i in lst:
			print(f'[{num}] {i}')
			num += 1
		print('**************************')

	@staticmethod
	def query_choice():
		print('**************************')
		print(f'[1] 查询余额')
		print(f'[2] 查询过往操作记录')
		print('**************************')

	@staticmethod
	def query_logs(dic):
		print('************操作记录查询************')
		for k, v in dic.items():
			print(k, v)
		print('************操作记录查询************')


if __name__ == "__main__":
	View.login()
