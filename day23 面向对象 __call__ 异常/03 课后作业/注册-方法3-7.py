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


#定义全局变量             好处:这个如果是函数形参,就不用在形参写了
# 已注册用户的文件
filename = 'user6.txt'

#已注册用户列表
lst = []

# 1 获取数据
# 获取已经注册的用户名到list
def get_data():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			lst.append(user)  #list可以直接修改全局变量,而不需要用global 和str int不同
	print(lst) #['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'tom']
	# return lst  #全局定义了,这里就不用返回了

# 2 校验密码
# 判断用户名不能重复
#    检测2次密码是否一致
def pwd_verify():
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
					pwd2 = input('注册,请再次输入密码')
					if pwd1 == pwd2:
						print('注册成功')
						
						#把新的用户写入文件user6.txt
						new_user = '{}:{}{}'.format(username,pwd1,'\n')
						with open(filename,mode='a+',encoding='utf-8') as fp:
							fp.write(new_user)
						
						sign = False
						break						
					else:
						print('两次密码不一致,请重新输入')	
	
			

# 方法3  参照老师思路默写7

def register():
	#1 获取数据
	get_data()
	
	#2 校验密码	
	pwd_verify()

register()

#扩展
# 1 user.txt如果不存在的判断  
# 2 用户在注册的时候,允许随时退出

















































