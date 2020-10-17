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


# 方法2  读写文件 不用json
# 1把用户名放到list中
def get_data():
	lst_new = []
	if not os.path.exists('user.txt'):
		with open('user.txt',mode='w',encoding='utf-8') as fp:
			pass
	else:
		with open('user.txt',mode='r+',encoding='utf-8') as fp:
			for i in fp:
				a,b = i.strip().split(':')
				lst_new.append(a)
	print(lst_new) #['alex', 'jack']
	return lst_new
	
# 把注册成功的用户名和密码写入到user.txt文件
def write_data(strvar):
	with open('user.txt',mode='a+',encoding='utf-8') as fp:
		fp.write(strvar)
	
# 2 校验用户名和密码
#  判断用户名不能重复
#  检测2次密码是否一致
def pwd_verify(lst):
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if username in lst:
			print('该用户名已经注册了')
		else:
			pwd1 = input('注册,请输入密码:')
			while True:
				pwd2 = input('注册,请再次输入密码:')
				if pwd1 == pwd2:
					print('注册成功')
					sign = False
					break
				else:
					print('两次密码不一致,请重新输入')
			strvar = '{}:{}{}'.format(username,pwd1,'\n')
			print(strvar)	
			write_data(strvar)

def register():
	pass
	#1 获取数据
# 如果已注册用户文件不存在,就新建一个txt
# 如果已存在,就读取txt
	lst = get_data()

# 2 判断用户名不能重复
# 3 检测2次密码是否一致
	pwd_verify(lst)

register()

# 方法3  老师思路






















































