# ### 1.注册登录小程序
# 注册:
# (1)检测两次密码如果相同,确认注册成功
# (2)检测两次密码如果不同,提示两次密码不一致
# (3)用户名不能重复

#思路
# 1 获取正常用户名和密码的数据
# 2 密码校验
	# 1 用户名不能是已经注册的
	# 2 密码一致,注册成功 --追加到文件
	# 3 密码不一致,注册不成功

# 步骤
# 1 先主函数
# 2 再分函数
# 3 全局变量

# 一 全局变量
# 正常用户名和密码的文件
filename = r'user9.txt'

# 正常用户名的列表
normal_userlist = []


# 二 分函数
# 1 获取正常用户名和密码的数据
def get_data():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			normal_userlist.append(user)
		print(normal_userlist)
		#['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'jack5']

# 2 密码校验
	# 1 用户名不能是已经注册的
	# 2 密码一致,注册成功
	# 3 密码不一致,注册不成功
def pwd_verify():
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if username == '' or ' ' in username:
			print('含有非法字符')
		else:
			if username in normal_userlist:
				print('该用户名已经注册了')
			else:
				pwd1 = input('注册,请输入密码:')
				while True:
					pwd2 = input('注册,请再次输入密码:')
					if pwd1 == pwd2:
						print('注册成功')
						
						with open(filename,mode='a+',encoding='utf-8') as fp:
							fp.write('{}:{}{}'.format(username,pwd1,'\n'))  #写入文件
						
						sign = False
						break
						
					else:
						print('两次密码不一致,请重新输入')

	

# 三 主函数
def register():
# 1 获取正常用户名和密码的数据
	get_data()
# 2 密码校验
	# 1 用户名不能是已经注册的
	# 2 密码一致,注册成功
	# 3 密码不一致,注册不成功
	pwd_verify()


register()






























