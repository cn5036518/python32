# ### 登录小程序
# 账户密码会预先记录在文件中
# 输入账号密码:如果都正确,登录成功
# 如果用户登录时进行三次校验,都不对,记录黑名单文件中
# 如果是黑名单的用户,禁止下次再次登录
namelist = []
passwordlist = []
blacknamelist = []

with open("user.txt",mode="r",encoding="utf-8") as fp:
	lst = fp.readlines()
	for i in lst:
		a,b = i.strip().split(":")
		namelist.append(a)
		passwordlist.append(b)

sign = True
while sign:
	name = input("请输入用户名 :")
	if name in namelist:
		with open("black.txt",mode="r",encoding="utf-8") as fp:
			lst = fp.readlines()
			for i in lst:
				blacknamelist.append(i.strip())
				# print(blacknamelist)
		if name in blacknamelist:
			print("该用户已被拉黑,请联系客服~")
			break
		else:
			name_index = namelist.index(name)
			password = passwordlist[name_index]

			times = 1
			while times <= 3:
				pwd = input("请输入密码 :")
				if pwd == password:
					print("恭喜你登录成功")
					sign = False
					break
				else:
					print("你输入的密码有误,你还有{}次机会".format(3-times))
					if times == 3:
						print("该账户已被拉入黑名单~")
						with open("black.txt",mode="a+",encoding="utf-8") as fp:
							strvar = name + "\n"
							fp.write(strvar)
							sign = False
							break
					times += 1

	else:
		print("输入的用户不存在")