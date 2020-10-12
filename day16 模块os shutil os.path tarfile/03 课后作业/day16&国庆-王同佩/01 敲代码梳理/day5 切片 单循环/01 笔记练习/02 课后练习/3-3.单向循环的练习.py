# ### 单向循环的练习

# (1)打印 一行十个小星星* help(print)
for i in range(10):
    print('*',end='')  #**********  #每次循环打印一个星星,打印的时候不换行
print('-----------1')

# (2)通过打印一个变量的形式,展现一行十个小星星
strvar = ''
for i in range(10):
	strvar += '*'
print(strvar)  #**********
print('-----------2')

# (3)一行十个换色的星星 ★☆★☆★☆★☆★☆
for i in range(10):
	if i % 2 == 0:
		print('★',end='')
	else:
		print('☆',end='')  #★☆★☆★☆★☆★☆
print('-----------3')

# (4)用一个循环,打印十行十列小星星
for i in range(100):
	print('*',end='')  #星星
	# 换行
	if i % 10 == 9:
		print()
print('-----------4')

# (5) 一个循环实现十行十列,格列换色的小星星
for i in range(100):
	#星星
	if i % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('-----------5')

# (6)一个循环实现十行十列,隔行换色的小星星
for i in range(100):
	# 星星
	if i // 10 % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('-----------6')





























