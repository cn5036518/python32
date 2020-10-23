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

import json,os

#1读取用户名文件
def get_data():
	dic = {}
	#1 获取数据
# 如果已注册用户文件不存在,就新建一个txt
	if not os.path.exists(r'whitelist.txt'):
		with open('whitelist.txt',mode='w',encoding='utf-8') as fp:
			json.dump(dic,fp,ensure_ascii = False)
	else:
		with open('whitelist.txt',mode='r+',encoding='utf-8') as fp:
# 如果已存在,就读取txt
			dic = json.load(fp)
			# print(dic)
			return dic

# 2 将注册成功的dic写入到用户名文件			
def write_data(dic):
	with open('whitelist.txt',mode='r+',encoding='utf-8') as fp:
		json.dump(dic,fp,ensure_ascii = False)

# 3 用户名和密码的校验			
def pwd_verify(dic):
	# 2 判断用户名不能重复
	sign = True
	while sign:
		username = input('注册,请输入用户名:')
		if username in dic:
			print('该用户名已经注册了哈')
			continue
		else:
		# 3 检测2次密码是否一致	
			pwd1 = input('注册,请输入密码:')
			while True:
				pwd2 = input('注册,请再次输入密码:')
				if pwd1 == pwd2:
					print('注册成功')
					sign = False
					dic[username] = pwd1
					print(dic)
					write_data(dic)
					break
				else:
					print('两次密码不一致,请重新输入')
			

# 方法1  json
def register():
	#1 获取数据
	dic = get_data()
	print(dic) #{}
	
# 2 判断用户名不能重复
# 3 检测2次密码是否一致
	pwd_verify(dic)

register()

# 方法2  读写文件 不用json




# 方法3  老师思路






















































