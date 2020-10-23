from package.view import View
from package.operation import Operation

class Main():
	
	@staticmethod
	def run():
		if View.login():  #返回True
			obj = Operation()  #新建对象
			while True:
				choice = input('请选择需要办理的业务:')
				if choice == '1':
					obj.register()  #1 调开户
				elif choice == '2':
					obj.query()   #2 调查询 查询卡的余额 
				elif choice == '3':
					obj.sava_money()  # 3调存钱
				elif choice == '4':
					obj.withdraw()  # 4调取款
				elif choice == '5':
					obj.transfer()  # 5调转账
				elif choice == '6':
					obj.change_pwd() # 6修改密码
				elif choice == '7':
					obj.lock_card() # 7锁卡
				elif choice == '8':
					obj.unlock_card()  # 8解卡
				elif choice == '9':
					obj.supplment_card() # 9补卡
				elif choice == '0': #0 调保存退出
					obj.save()
					break
		
if __name__ == '__main__':	
	Main.run()





























