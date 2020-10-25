# ### main 入口文件
from package.view import View
from package.operation import Operation

class Main():
	@staticmethod  #静态方法  类和对象都可以调 不会额外传递参数
	def run():
		if View.login():
			obj = Operation()
			while True:
				choice = input('请选择需要办理的业务:')
				if choice == '1':
					obj.register()  #1 注册开户
				elif choice == '2':
					obj.query()  #2 查询  卡余额和锁定状态
				elif choice == '3':
					obj.deposit()  #3 存钱
				elif choice == '4':
					obj.withdraw()  # 4取款
				elif choice == '5':
					obj.transfer() #5 转账
				elif choice == '6':
					obj.change_pwd() #6 修改密码
				elif choice == '7':
					pass
				elif choice == '8':
					pass
				elif choice == '9':
					obj.supplment_card()  #9 补卡
				elif choice == '0':
					obj.save()   #0 保存退出
					break
	
	
if __name__ == '__main__':
	Main.run()  # 类.方法






































