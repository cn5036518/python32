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

def get_data():
	lst = [] # 存放用户名
	with open('user1.txt',mode='r+',encoding='utf-8') as fp:
		for i in fp:
			a,b = i.strip().split(':')
			lst.append(a)
	print(lst)  #['alex', 'jack', 'bob']
	return lst
	
def pwd_verify(lst):
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if ' ' in username or username == '':
			print('用户名含有非法字符')
		else:
			if username in lst:
				print('该用户名已经注册了')
			else:
				pwd1 = input('注册,请输入密码:')
				while True:
					pwd2 = input('注册,请再次输入密码:')
					if pwd1 == pwd2:
						print('注册成功')
						
						strvar = '{}:{}{}'.format(username,pwd1,'\n')
						with open('user1.txt',mode='a+',encoding='utf-8') as fp:
							fp.write(strvar)
						
						sign = False
						break
					else:
						print('两次密码不一致,请重新输入')
			

# 方法3  老师思路
def register():
	#1 获取数据
	lst = get_data()
	
	#2 校验密码
	pwd_verify(lst)

register()



















































