from package.view import View
from package.operation import Operation


class Main:
	'''
	开户(1)
	查询(2)          新加入操作日志查询
	存钱(3)
	取钱(4)
	转账(5)
	改密(6)
	锁卡(7)
	解卡(8)
	补卡(9)
	退出(0)
	登出(X)           新加入
	新卡(N)           新加入 开多张卡
	卡号登录(C)        新加入 登录 可直接执行功能模块触发 登录装饰器
	身份证登录(Z)      新加入 身份证登录
	'''

	@staticmethod
	def run():
		if View.login():
			obj = Operation()
			while True:
				View.operation(obj.login_card)
				choice = input("请选择需要办理的业务>>>").strip().upper()
				if choice == "1":
					obj.register()
				elif choice == "2":
					obj.query()
				elif choice == "3":
					obj.save_money()
				elif choice == "4":
					obj.get_money()
				elif choice == "5":
					obj.trans_money()
				elif choice == "6":
					obj.change_pwd()
				elif choice == "7":
					obj.lock()
				elif choice == "8":
					obj.unlock()
				elif choice == "9":
					obj.new_card()
				elif choice == "0":
					obj.save()
					break
				elif choice == "X":
					obj.signout()
				elif choice == "N":
					obj.append_card()
				elif choice == 'C':
					obj.cardid_login()
				elif choice == 'Z':
					obj.userid_login()


if __name__ == "__main__":
	Main.run()



