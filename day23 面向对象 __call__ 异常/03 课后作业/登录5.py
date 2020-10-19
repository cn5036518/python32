# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常的用户名和密码
# 2 获取黑名单用户名
# 3 登录校验
	# 1黑名单用户-禁止登录
	# 2用户名未注册
	# 3用户名在正常的用户名列表,密码正确 成功登录
	# 4用户名在正常的用户名列表,密码不正确 追加到黑名单
	
# 步骤
# 1 先主函数
# 2 后分函数
# 3 全局变量

# 一 全局变量
# 1 正常的用户名和密码文件
filename1 = r'user9.txt'

# 2 黑名单用户名文件
filename2 = r'black.txt'

# 3 正常的用户名列表
normal_user = []

# 4 正常的密码列表
normal_pwd = []

# 5 黑名单用户列表
black_user = []

	
# 二 分函数
# 1 获取正常的用户名和密码
def get_info():
	with open(filename1,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			normal_user.append(user)
			normal_pwd.append(pwd)
		print(normal_user) #['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'jack5', 'tom2']
		print(normal_pwd) #['111', '111', '1', '1', '1', '2', '1', '1', '1', '1', 'tom2']
	
# 2 获取黑名单用户名
def get_black():
	with open(filename2,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			black_user.append(i.strip())
		print(black_user) #['bob', 'tom']		

# 3 登录校验
	# 1黑名单用户-禁止登录
	# 2用户名未注册
	# 3用户名在正常的用户名列表,密码正确 成功登录
	# 4用户名在正常的用户名列表,密码不正确 追加到黑名单
def pwd_verify():
	sign = True
	times = 3
	while sign:
		username = input('请输入登录用户名:')
		pwd = input('请输入登录密码:')
		if username in black_user:
			print('该用户禁止登录,请联系客服')
		elif username not in normal_user:
			print('该用户未注册')
		else:
			if pwd == normal_pwd[normal_user.index(username)]:  #关键点1
				print('登录成功')
				break
			else:	
				times -= 1
				print('用户名或密码不正确,请重新输入,你还有{}次机会'.format(times))
				if times == 0:
					print('对不起,错误次数太多,账号锁定')
					with open(filename2,mode='a+',encoding='utf-8') as fp:
						fp.write(username+'\n')
						break
				
				

# 三 主函数
def login():
# 1 获取正常的用户名和密码
	get_info()

# 2 获取黑名单用户名
	get_black()

# 3 登录校验
	# 1黑名单用户-禁止登录
	# 2用户名未注册
	# 3用户名在正常的用户名列表,密码正确 成功登录
	# 4用户名在正常的用户名列表,密码不正确 追加到黑名单
	pwd_verify()
	

login()























