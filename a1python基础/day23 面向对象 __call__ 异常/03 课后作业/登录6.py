# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常的用户名和密码
# 2 获取黑名单的用户名
# 3 用户名和密码的校验
	
# 步骤
# 1 先主函数
# 2 后分函数
# 3 全局变量


#  一 全局变量
# 1 正常的用户名和密码的文件
filename1 = r'user9.txt'

# 2 黑名单的用户名的文件
filename2 = r'black.txt'

# 3 正常的用户名的列表
normal_user = []

# 4 正常的密码的列表
normal_pwd = []

# 5 黑名单的用户名的列表
black_user = []


# 二 分函数
def get_normal():
	with open(filename1,mode='r+',encoding='utf-8') as fp:	
		for i in fp:
			user,pwd = i.strip().split(':')
			normal_user.append(user)
			normal_pwd.append(pwd)
		print(normal_user) #['tom', 'jack', 'bob', 'alex', 'james', 'tom1', 'tom2']
		print(normal_pwd)	#['111', '111', '1', '1', '1', '2', '1']	 
	
def get_black():
	with open(filename2,mode='r+',encoding='utf-8') as fp:	
		for i in fp:
			black_user.append(i.strip())
		print(black_user)  #['bob', 'tom', 'jack']	
	
def pwd_verify():
	# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录
# (4)如果是未注册的用户,禁止登录
	sign = True
	while sign:
		username = input('请输入登录的用户名:')
		if username in black_user:
			print('禁止登录,请联系客服')
		elif username not in normal_user:
			print('该用户未注册')
		else:
			times = 1
			while True:
				pwd = input('请输入登录的密码:')
				if pwd == normal_pwd[normal_user.index(username)]:  #规律
					print('登录成功')
					sign = False
					break
				else:
					print('密码不对,请重新输入,你还有{}次登录机会'.format(3-times))
					times += 1
					if times == 3: #记录黑名单文件中
						print('该账户已经锁定,请联系客服')
						black_user.append(username)  #添加到黑名单列表
						with open(filename2,mode='a+',encoding='utf-8') as fp:
							fp.write(username+'\n')
						break


# 三 主函数
def login():
	get_normal()
	get_black()
	pwd_verify()
	
login()





















































