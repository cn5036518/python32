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

filename = r'user7.txt'
def get_data(filename):
	lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			lst.append(user)
	print(lst)
	# ['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4']
	return lst

def pwd_verify(lst,filename):
	sign = True
	while sign:
		username = input('请输入用户名:')
		if ' ' in username or username == '':
			print('你的用户名含有非法字符')
		else:
			if username in lst:
				print('该用户名已经注册了')
			else:
				pwd1 = input('请输入密码:')
				while True:
					pwd2 = input('请再次输入密码:')
					if pwd1 == pwd2:
						print('注册成功')
						
						#写入文件--nok
						with open(filename,mode='a+',encoding='utf-8') as fp:
							fp.write('{}:{}{}'.format(username,pwd1,'\n'))
						
						sign = False
						break
					else:
						print('两次密码不一致,请重新输入')
		
# 方法3  老师思路默写7	
def main():
	lst = get_data(filename)
	
	pwd_verify(lst)

# main()


# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常用户名和密码
# 2 获取黑名单用户名
# 3 密码校验   黑名单文件

# 步骤
# 先写主函数
# 再写分函数

#分函数
# 1 获取白名单用户名和密码
def get_info(filename):
	user_lst = []
	pwd_lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			user_lst.append(user)
			pwd_lst.append(pwd)
	print(user_lst)
	# ['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4']
	print(pwd_lst)
	return user_lst,pwd_lst
	
# 2 获取黑名单用户名
def get_black(filename):
	black_lst = []
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			black_lst.append(i.strip())
	print(black_lst)
	return black_lst
		
	
# 3 密码校验   
def pwd_verify2(user_lst,pwd_lst,black_lst,filename2):
	times = 3
	while True:
		user = input('请输入登录用户名:')
		pwd = input('请输入登录密码:')
		if user in black_lst:
			print('该用户禁止登录')
		else:
			if user in user_lst and pwd == pwd_lst[user_lst.index(user)]:  #规律
				print('登录成功')
				break
			elif user not in user_lst:
				print('该用户名未注册')
			elif user in user_lst and pwd != pwd_lst[user_lst.index(user)]:
				times -= 1
				print('用户名或密码错误,请重新输入,你还有{}次登录机会'.format(times))
				if times == 0:
					print('对不起,错误次数已达上限,请联系客服')
					with open(filename2,mode='a+',encoding='utf-8') as fp: #写入黑名单
						fp.write(user+'\n')
					break
			

#主函数
filename = r'user8.txt'
filename2 = r'balcklist.txt'
def main():
	# 1 获取正常用户名和密码
	user_lst,pwd_lst = get_info(filename)
	
	# 2 获取黑名单用户名
	black_lst = get_black(filename2)
	
	# 3 密码校验   黑名单文件
	pwd_verify2(user_lst,pwd_lst,black_lst,filename2)
	
main()






































