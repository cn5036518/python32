# ### 视图类
# 登录 打印欢迎界面 打印操作界面

import time

class View():
	
	def login():
		name = input('请输入管理员的账户:')
		pwd = input('请输入管理员密码:')
		if name == 'admin' and pwd == '111':
			# 打印欢迎界面
			View.welcome_view()  #类.静态方法
			
			# 延迟一秒
			# time.sleep(1)
			
			# 打印操作界面
			View.operation_view()  #类.静态方法
			
			return True
			
		else:
			print('您的用户密码有错误')
		
		
	@staticmethod   #静态方法  类和对象都可以调 不会额外传递参数
	def welcome_view():
		strvar = '''
*******************************************
*                                         *
*                                         *
*         Welcome To OldBoy Bank          *
*                                         *
*                                         *
*******************************************  '''
		print(strvar,end='')
		
	@staticmethod
	def operation_view():
		strvar = '''
*******************************************
*           开户(1)    查询(2)             *
*           存钱(3)    取钱(4)             *
*           转账(5)    改密(6)             *
*           锁卡(7)    解卡(8)             *
*           补卡(9)    退出(0)             *
******************************************* '''
		print(strvar)
	
	
if __name__ == '__main__':
	View.login() #类.无参方法














































