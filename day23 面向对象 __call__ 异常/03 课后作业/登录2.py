
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






































