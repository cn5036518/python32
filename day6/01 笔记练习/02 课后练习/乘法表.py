#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/17 21:06

# 一象限
# 方法2 for
for i in range(1,10):  #注意 range不能少
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('----------------------4-2 for')

# 四象限
# 方法2 for
for i in range(9,0,-1):  #注意 range不能少
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()
print('----------------------5-2 for')


# 二象限
# 方法2 for
for i in range(1,10):  #
	# 打印空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #7组空格

	#打印表达式
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()  #换行
print('----------------------5-3 for')

# 三象限
# 方法2 for
for i in range(9,0,-1):  #
	# 打印空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #7组空格  关键

	#打印表达式
	for j in range(1,i+1):
		print('%d*%d=%2d ' % (i,j,i*j),end='')
	print()  #换行
print('----------------------5-4 for')
















