# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常的用户名和密码
# 2 获取黑名单的用户名
# 3 登录检验
	# 1 是否黑名单,是就禁止登录
	# 2 用户名密码正确,登录成功
	# 3 密码错误3次,记黑名单

# 步骤
# 1 先主函数
# 2 后分函数
# 3 全局变量定义

# 一 全局变量
# 1正常用户名和密码文件
filename_normal = r'user6.txt'

# 2黑名单用户名文件
filename_balck = r'black.txt'

# 3正常用户名列表
normal_user = []

# 4正常密码列表
normal_pwd = []

# 5黑名单用户名列表
black_user = []


# 二 分函数
# 1 获取正常的用户名和密码
def get_info():
	with open(filename_normal,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			normal_user.append(user)
			normal_pwd.append(pwd)  #修改全局变量
		print(normal_user) #['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'tom2']
		print(normal_pwd)  #['111', '111', '1', '1', '1', '2', '1', '1', '1', '1']
	
# 2 获取黑名单的用户名
def get_black():
	with open(filename_balck,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			black_user.append(i.strip())
		print(black_user) #['bob']
			
# 3 登录检验
	# 1 是否黑名单,是就禁止登录
	# 2 用户名密码正确,登录成功
	# 3 密码错误3次,记黑名单
	# 4 用户未注册
def login_verify():
	times = 3
	while True:
		username = input('请输入登录用户名:')
		pwd = input('请输入登录密码:')
		if username in black_user:
			print('禁止登录,请联系客服')
		else:
			if username not in normal_user:
				print('该用户未注册')
			else:
				if username in normal_user and pwd == normal_pwd[normal_user.index(username)]:  #关键点
					print('登录成功')
					break
				elif username in normal_user and pwd != normal_pwd[normal_user.index(username)]:
					times -= 1
					print('用户名或密码错误,你还有{}次登录机会'.format(times))
					
					if times == 0:
						print('错误已达上限,用户冻结')
						
						with open(filename_balck,mode='a+',encoding='utf-8') as fp:
							fp.write(username+'\n')						
						break
					
	
	

# 三 主函数
def login():
# 1 获取正常的用户名和密码
	get_info()
	
# 2 获取黑名单的用户名
	get_black()

# 3 登录检验
	# 1 是否黑名单,是就禁止登录
	# 2 用户名密码正确,登录成功
	# 3 密码错误3次,记黑名单
	login_verify()

login()





























