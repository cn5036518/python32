# 账户密码会预先记录在文件中
# 输入账号密码:如果都正确,登录成功
# 如果用户登录时进行三次校验,都不对,记录黑名单文件中
# 如果是黑名单的用户,禁止下次再次登录

# 第一步,先将用户名和密码取出来,进行判断
user_list = []
pwd_list = []
black_list = []
with open("user.txt", mode="r+", encoding="utf-8")as fp:
	# 在这儿出现了一个问题,就是有个空格,后边的文件就不读取了,还有就是空格怎么来的.
	list1 = fp.readlines()
	# 遍历用户名和密码的列表通过字符串切片将他们分成两个列表
	for i in list1:
		name, pwd = i.strip().split(":")
		user_list.append(name)
		pwd_list.append(pwd)
	# 打开黑名单文件,读取黑名单用户的信息.
with open("black.txt",mode="r+",encoding="utf-8") as fp1:
	try:
		list2 = fp1.readlines()
		for i in list2:
			black_list.append(i)
	except:
		pass
	print(list2)

print("开始登陆!!")
sign = True
while sign:
	name = input("请输入你的用户名:")
	# 开始判断用户是否在黑名单中:
	if name in black_list:
		print(1)
		print("抱歉,您的账户异常,已被加入黑名单,请联系管理员")
	# 如果不在黑名单中,开始让用户输入密码
	else:
		pwd = input("请输入密码; ")
		times = 1
		while times <= 3:

			# 开始验证密码是否正确!
			index_num = user_list.index(name)
			if pwd == pwd_list[index_num]:
				print("登陆成功,欢迎回家!")
				sign = False
				break
			# 如果密码不正确
			else:
				pwd2 = input("密码错误,请重新输入.注意;您还有{}次机会".format(3-times))

				if times ==2:

					with open("black.txt",mode="a",encoding="utf-8") as fp3:
						strvar = name + "\n"
						fp3.write(strvar)
						print("三次密码错误,用户名加入黑名单,请联系管理员")
						sign = False
						break
			times += 1
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
		
