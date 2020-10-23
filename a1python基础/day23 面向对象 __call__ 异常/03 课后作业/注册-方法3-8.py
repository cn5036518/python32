# ### 1.注册登录小程序
# 注册:
# (1)检测两次密码如果相同,确认注册成功
# (2)检测两次密码如果不同,提示两次密码不一致
# (3)用户名不能重复

#思路
#1 获取数据

# 2 校验用户名和密码
#   1判断用户名不能重复
#   2检测2次密码是否一致  一致就追加到文件


#步骤
#   全局变量
# 1 先主函数
# 2 再分函数


# 一 全局变量
#1 正常用户名和密码的文件
filename = r'user.txt'

#2 正常用户名列表
user_lst = []


#二 分函数
#1 获取数据
def get_data():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(":")
			user_lst.append(user)
		print(user_lst) #['alex', 'jack', 'bob']  #修改全局变量

# 2 校验用户名和密码
#   1判断用户名不能重复
#   2检测2次密码是否一致
def pwd_verify():
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if username in user_lst:
			print('该用户名已经注册过了')
		elif username == '' or ' ' in username:
			print('含有非法字符')
		else:
			pwd1 = input('请输入密码:')
			while True:
				pwd2 = input('请再次输入密码:')
				if pwd1 == pwd2:
					print('注册成功')
					
					with open(filename,mode='a+',encoding='utf-8') as fp:
						fp.write('{}:{}{}'.format(username,pwd1,'\n'))
					
					sign = False
					break
					
				else:
					print('两次密码不一致,请重新输入')

#三 主函数
def register():
#1 获取数据
	get_data()

# 2 校验用户名和密码
#   1判断用户名不能重复
#   2检测2次密码是否一致
	pwd_verify()

register()








































