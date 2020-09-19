# ### 双向循环的专题练习
''''''


# 1.用两个循环完成十行十列的小星星
for i in range(1,11):
	for j in range(1,11):
		print('*',end='')
	print()
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
		if i % 2 == 0:   #隔行换色 取余而不是*
		# if j % 2 == 0:  #隔列换色
			print('★',end='')
		else:
			print('☆',end='')
	print()
print('--------------------------3')

# 4.  99 乘法表
# 一象限
for i in range(1,10):
	for j in  range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')  #1 表达式
	print() #换行
print('--------------------------4-1')

# 四象限
for i in range(9,0,-1):
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('--------------------------4-2')

# 二象限
for i in range(1,10):
	#1 打印空格
	for k in range(9-i,0,-1):
		print('       ',end='')
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i, j, i * j), end='')  # 2 表达式
	print() #3换行
print('--------------------------4-3')

# 三象限
for i in range(9,0,-1):  #倒序
	for k in range(9-i,0,-1):  #注意点:i从9 8 7 依次递减,步长就是-1 (这里的-1针对的是i,而不是9-i)
		print('       ',end='')
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i, j, i * j), end='')
	print()
print('--------------------------4-4')

# 5.求吉利数字 100~999 之间 找 111 222 333 123 456 654 321 ...

print('--------------------------5')

# 6.百钱买百鸡
# 公鸡一个五块钱,母鸡一个三块钱,小鸡三个一块钱
# 现在要用一百块买一百只鸡
# 问公鸡 母鸡,小鸡各多少只?
print('--------------------------6')
























































