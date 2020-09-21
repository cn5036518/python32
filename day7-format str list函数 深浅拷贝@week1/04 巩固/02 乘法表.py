#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/19 16:19

# 一象限
for i in range(1,10):  #控制行
	# 控制列
	for j in range(1,i+1):   #这里是i+1 而不是i
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('------------------------------ 一象限')

# 二象限
for i in range(1,10):
	# 打印空格   空格和行号的关系  空格个数= 9-当前的行号  9-i
	for k in range(9-i,0,-1):  #这里的步长必须是-1  原因是:只要9-i是正数,不管i或者9-i是递增还是递减趋势,步长必须是-1,否则,取不到值
		print('       ',end='')  #空格不换行  每组是7个空格
		
	# 打印表达式
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('------------------------------ 二象限')

# 三象限
for i in range(9,0,-1):  #这里的i是第一个乘数  而不是行号
	# 空格    空格和行号的关系   空格个数= 9-当前的行号  9-i
	for k in range(9-i,0,-1):  ##这里的步长必须是-1  原因是:只要9-i是正数,不管i或者9-i是递增还是递减趋势,步长必须是-1,否则,取不到值  重点
		print('       ',end='')

	# 表达式
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	
	#换行
	print()
print('------------------------------ 三象限')

# 四象限
for i in range(9,0,-1):  #控制行 倒序
	for j in range(1,i+1):  #控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #表达式
	#换行
	print()
print('------------------------------ 四象限')




















