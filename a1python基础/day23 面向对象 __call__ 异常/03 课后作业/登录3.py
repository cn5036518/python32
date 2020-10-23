# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录

# 思路
# 1 获取正常用户名和密码
# 2 获取黑名单用户名
# 3 密码校验   黑名单文件
#   1 是否黑名单
#   2 是否未注册
#   3 用户名和密码正确,登录成功
#   4 用户名和密码不正确,3次错误写入黑名单

# 步骤
# 先写主函数
# 再写分函数

# 定义全局变量
#正常用户名列表
user_lst = []

#正常密码列表
pwd_lst = []

#黑名单用户名列表
black_lst = []

# 正常用户名和密码文件
filename = r'user8.txt'

# 黑名单用户名文件
filename2 = r'balcklist.txt'


#分函数
# 1 获取正常用户名和密码
def get_info():
	with open(filename,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			user,pwd = i.strip().split(':')
			user_lst.append(user)
			pwd_lst.append(pwd)  #list可以在函数内,修改全局变量,而不用global 和str int不一样 
			# 因为是直接修改全局变量,所以不用return
		print(user_lst) #['tom', 'jack', 'bob', 'alex', 'james', 'jack1', 'jack2', 'jack3', 'jack4', 'jack5']
		print(pwd_lst) #['111', '111', '1', '1', '1', '2', '1', '1', '1', '1']			
	
# 2 获取黑名单用户名
def get_black():
	with open(filename2,mode='r+',encoding='utf-8') as fp:
		for i in fp:
			black_lst.append(i.strip())
		print(black_lst)  #['tom', 'jack']  #list可以在函数内,修改全局变量,而不用global 和str int不一样 
	
# 3 密码校验  
def pwd_verify() :
#   1 是否黑名单
#   2 是否未注册
#   3 用户名和密码正确,登录成功
#   4 用户名和密码不正确,3次错误写入黑名单
	times = 3
	while True:
		username = input('请输入登录用户名:')
		pwd = input('请输入登录密码:')		
		if username in black_lst:
			print('该用户禁止登录,请联系客服')
		elif username not in user_lst:
			print('该用户未注册')
		elif username in user_lst and pwd == pwd_lst[user_lst.index(username)]:
			print('登录成功')
			break
		elif username in user_lst and pwd != pwd_lst[user_lst.index(username)]:
			times -= 1
			print('用户名或密码不正确,你还有{}次登录机会'.format(times))
			if times == 0:
				print('错误次数已达上限,登录账号锁定')
				with open(filename2,mode='a+',encoding='utf-8') as fp:  #这里用追加
					fp.write(username+'\n')	
					break
		else:
			pass

#主函数
def main():
	# 1 获取正常用户名和密码
	get_info()
	
	# 2 获取黑名单用户名
	get_black()
	
	# 3 密码校验   黑名单文件
	pwd_verify()
	
main()






































