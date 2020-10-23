for i in range(64):
	if i // 10 % 2 == 0:   #隔行换色
		if i % 2 == 0:
			print('&',end='')
		else:
			print('*',end='')
	else:
		if i % 2 == 0:
			print('*', end='')
		else:
			print('&', end='')
	# 换行
	if i % 8 == 7:
		print()
print('-=------------------------- 1 单循环  for')


for i in range(8):  #控制行
	if i % 2 == 0:  # 偶数行 0 2 4 6
		print('&*&*&*&*',end='')
	else:  # 奇数行 1 3 5 7
		print('*&*&*&*&',end='')

	#换行
	print()
print('-=------------------------- 2 单循环  for')


for i in range(8):
	if i % 2 == 0:
		# print('&*&*&*&*',end='')  #如何一行打印这个 不换行
		for j in range(8):
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')		
	else:
		# print('*&*&*&*&',end='')	
		for j in range(8):
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')
	# 换行
	print()
print('-=------------------------- 3 双循环  for')





























