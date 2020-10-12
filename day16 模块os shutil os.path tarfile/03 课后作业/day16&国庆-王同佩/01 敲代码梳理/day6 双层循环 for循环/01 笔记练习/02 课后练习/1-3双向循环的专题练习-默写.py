# ### 双向循环的专题练习
''''''


# 1.用两个循环完成十行十列的小星星
for i in range(1,11):
	for j in range(1,11):
		print('*',end='')
	print()  #换行
print('--------------------------1')

# 2.用两个循环完成十行十列的隔列换色的小星星
for i in range(1,11):
	for j in range(1,11):
		if j % 2 == 0:
			print('★',end='')
		else:
			print('☆',end='')
	print()
print('--------------------------2')

# 3. 用两个循环完成十行十列隔行换色的小星星
for i in range(1,11):
	for j in range(1,11):
		if i % 2 == 0:  #隔行换色
		# if i % 2 == 0: #隔列换色
			print('★',end='')
		else:
			print('☆', end='')
	print()
print('--------------------------3')

# 4.  99 乘法表
# 一象限
for i in range(1,10):
	for j in range(1,i+1):  #这里必须是i+1 而不能是i   关键点
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('--------------------------4-1')

# 四象限
for i in range(9,0,-1):  #倒序
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('--------------------------4-2')

# 二象限
for i in range(1,10):
	#打印空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #7个空格

	# 打印表达式
	for j in range(1,i+1):  #这里必须是i+1 而不能是i   关键点
		print('%d*%d=%2d ' % (i,j,i*j),end='')  #%2d后面一个空格
	print() #换行
print('--------------------------4-3')

# 三象限
for i in range(9,0,-1):  #倒序
	#打印空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #7个空格

	# 打印表达式
	for j in range(1,i+1):  #这里必须是i+1 而不能是i   关键点
		print('%d*%d=%2d ' % (i,j,i*j),end='')  #%2d后面一个空格
	print() #换行
print('--------------------------4-4')



# 5.求吉利数字 100~999 之间 找 111 222 333 123 456 654 321 ...
# for i in range(100,1000):
# 	gewei = int(str(i)[-1])
# 	shiwei = int(str(i)[-2])
# 	baiwei = int(str(i)[-3])
# 	if shiwei == gewei and shiwei == baiwei:
# 		print(i)
# 	elif shiwei == gewei +1 and shiwei == baiwei -1:
# 		print(i)
# 	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
# 		print(i)
print('--------------------------4')

# 6.百钱买百鸡
# 公鸡一个五块钱,母鸡一个三块钱,小鸡三个一块钱
# 现在要用一百块买一百只鸡
# 问公鸡 母鸡,小鸡各多少只?
for i in range(21):
	for j in range(34):
		for k in range(100):
			if (i+j+k==100) and (5*i+3*j+1/3*k==100):
				print(i,j,k)
























































