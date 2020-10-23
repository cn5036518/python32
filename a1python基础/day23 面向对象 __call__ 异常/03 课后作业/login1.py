# ### 登录小程序
# 账户密码会预先记录在文件中
# 输入账号密码:如果都正确,登录成功
# 如果用户登录时进行三次校验,都不对,记录黑名单文件中
# 如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常用户名和密码
# 2 获取黑名单用户名
# 3 登录3次校验,记录黑名单

# 步骤
# 先主函数-提纲
# 后分函数

# 账户列表
# accountlist = []

# 密码列表
# pwdlist = []

# 黑名单列表
# blacklist = []

# 分函数
# 1 获取正常用户名和密码
def get_info(filename1):
	accountlist = []
	pwdlist = []
	with open(filename1,mode='a+',encoding='utf-8') as fp:
		fp.seek(0)
		for i in fp:
			user,pwd = i.strip().split(':')
			accountlist.append(user)
			pwdlist.append(pwd)
		print(accountlist)  #['alex', 'jack', 'bob']
		print(pwdlist)   #['111', '111', '1']
	return accountlist,pwdlist
	
# 2 获取黑名单用户名
def get_black(filename2):
	blacklist = []
	with open(filename2,mode='a+',encoding='utf-8') as fp:
		fp.seek(0)
		for i in fp:
			blacklist.append(i.strip())
		print(blacklist)
	return blacklist
			
# 3 登录3次校验,记录黑名单
def pwd_verify(filename2,accountlist,pwdlist,blacklist):	
	sign = True
	while sign:
		name = input('请输入您的用户名:')
		if name in accountlist:			
			# 检测是否是拉黑的用户
			if name in blacklist:
				print('该账户已经被冻结,请联系客户人员')
			else:
				# 该账户已经被冻结,请联系客户人员
				index_num = accountlist.index(name)  #重点1
				# 通过索引号获取密码
				pwd_true = pwdlist[index_num]
				# print(pwd_true)				
				
				# 控制密码输错次数不超过3次
				for times in range(1,4):
					ask_pwd = input('请输入您的登录密码:')
					if ask_pwd == pwd_true:
						print('登录成功')
						sign = False
						break
					else:
						# 剩下次数 = 总次数-使用过的次数
						print("抱歉您的密码输入错误,还剩下{}机会".format(3-times))
						if times == 3:
							print('抱歉~,输错三次,您的账号被冻结~')
							## 把当前用户拉黑,记录到黑名单中
							with open(filename2,mode='a+',encoding='utf-8') as fp:
								strvar = name + '\n'
								fp.write(strvar)
								sign = False
								break	
		else:
			print('该用户名不存在')
			
			

filename1 = r'user.txt'
filename2 = r'black.txt'

#主函数
def login():
	# 1 获取正常用户名和密码
	accountlist,pwdlist = get_info(filename1)
	
# 2 获取黑名单用户名
	blacklist = get_black(filename2)

# 3 登录3次校验,记录黑名单
	pwd_verify(filename2,accountlist,pwdlist,blacklist)
	
login()








































