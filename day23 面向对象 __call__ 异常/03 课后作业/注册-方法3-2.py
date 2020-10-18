# ### 1.注册登录小程序
# 注册:
# (1)检测两次密码如果相同,确认注册成功
# (2)检测两次密码如果不同,提示两次密码不一致
# (3)用户名不能重复

#思路
#1 获取数据
# 如果已注册用户文件不存在,就新建一个txt
# 如果已存在,就读取txt

# 2 判断用户名不能重复
# 3 检测2次密码是否一致

import os

# 1 获取已经注册的用户名到list
def get_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			lst.append(user)
	print(lst) #['tom', 'jack', 'bob', 'alex']
	return lst

# 2 判断用户名不能重复
#    检测2次密码是否一致
def pwd_verify(lst,filename):
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if username == '' or ' ' in username:
			print('含有非法字符')
		else:
			if username in lst:
				print('该用户名已经注册了')
			else:
				pwd1 = input('注册,请输入密码:')
				while True:
					pwd2 = input('注册,请再次输入密码:')
					if pwd1 == pwd2:
						print('注册成功')
						
						# 将新注册的用户名和密码写入到文件
						new_user = '{}:{}{}'.format(username,pwd1,'\n')
						with open(filename,mode='a+',encoding='utf-8') as fp:
							fp.write(new_user)
						
						sign = False
						break
					else:
						print('两次密码不一致,请重新输入密码')
		
	
			

# 方法3  老师思路默写
filename = 'user2.txt'

def register():
	#1 获取数据
	lst = get_data(filename)
	
	#2 校验密码	
	pwd_verify(lst,filename)

register()



















































