#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/19 14:59

# 单循环 for
for i in range(64):
	if i // 10 % 2 == 0:  #打印隔行换色
		if i % 2 == 0:  #加上隔列换色
			print('*',end='')
		else:
			print('&',end='')
	else:
		if i % 2 == 0:
			print('&',end='')
		else:
			print('*',end='')
	# 打印换行
	if i % 8 == 7:
		print()
print('--------------------------1 单循环for')

# 双循环 for
for i in range(8): #8行
	if i % 2 == 0:  #偶数行
		print('*&*&*&*&',end='')
	else:  #奇数行
		print('&*&*&*&*', end='')
	# 换行
	print()
print('--------------------------2 双循环for')

# 双循环2 for
for i in range(8): #8行
	if i % 2 == 0:  #偶数行  0 2 4 6
		# 打印一行   *&*&*&*&
		for j in range(8):
			if j % 2 == 0:
				print('&', end='')
			else:
				print('*',end='')
	else:  #奇数行  1 3 5 7
		# 打印一行  &*&*&*&*
		for j in range(8):
			if j % 2 == 0:
				print('*', end='')
			else:
				print('&',end='')
	# 换行
	print()
print('--------------------------3 双循环for')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


















