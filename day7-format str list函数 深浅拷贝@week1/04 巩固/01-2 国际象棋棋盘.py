for i in range(64):
	if i // 8 % 2  == 0:  #打印隔行换色 对8
		if i % 2 == 0:
			print('*',end='')
		else:
			print('&',end='')
	else:
		if i % 2 == 0:
			print('&',end='')
		else:
			print('*',end='')
	# 换行
	if i % 8 == 7:  #对8取余
		print()
print('========================= 1单循环 for')

# 单循环  for
for i in range(8):  #8行
	if i % 2 == 0:
		print('*&*&*&*&',end='')
	else:
		print('&*&*&*&*',end='')
	# 换行
	print()
print('========================= 2单循环 for')

# 双循环 for
for i in range(8):
	if i % 2 == 0:
		# print('*&*&*&*&',end=)  #如何打印这一行
		for j in range(8):
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')
	else:
		for j in range(8):
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')		
	# 换行
	print()
print('========================= 3 双循环 for')


























