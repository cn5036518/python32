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

# 1 先主函数
# 2 后分函数
# 3 全局变量

#  一 全局变量
# 1 存放正常的用户名和密码的文件
filename = r'user9.txt'

# 2  存放正常的用户名和密码的列表
normal_list = []

# 二 分函数
# 1 获取正常用户名和密码的数据
def get_normal():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			normal_list.append(user)  #list在局部修改全局,不需要加global
	print(normal_list)
	#['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'jack5', 'tom2']

# 2 密码校验
	# 1 用户名不能是已经注册的
	# 2 密码一致,注册成功 --追加到文件
	# 3 密码不一致,注册不成功
def pwd_verify():
	sign = True
	while sign:
		user = input('请输入你要注册的用户名:')
		if ' ' in user or user == '':
			print('含有非法字符')
		elif user in normal_list:
			print('该用户名已经注册')
		else:
			pwd1 = input('请输入你的密码:')
			while True:
				pwd2 = input('请再次输入你的密码:')
				if pwd1 == pwd2:
					print('注册成功')
					with open(filename,mode='a+',encoding='utf-8') as fp:  #追加到文件
						fp.write('{}:{}{}'.format(user,pwd1,'\n'))
						sign = False
						break
				else:
					print('密码不一致,请重新输入')
	
	


# 三 主函数
def register():
	get_normal()
	pwd_verify()
		
	
register()










































