#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/9/28 11:05

# part2
# 1.打印一行十个小星星
for i in range(10):
	print('*',end='')
print('-----------------------1')

# 2.通过打印变量,直接输出一行十个小星星
strvar = ''
for i in range(10):
	strvar += '*'
print(strvar)
print('-----------------------2')

# 3.打印一行十个小星星,奇数个打印★,偶数个打印☆
for i in range(10):
	if i % 2 == 1:
		print('*',end='')
	else:
		print('&',end='')
print('-----------------------3')

# 4.一个循环打印十行十列小星星
for i in range(100):
	# 星星
	print('*',end='')
	#换行
	if i % 10 == 9:
		print()
print('-----------------------4-1')

for i in range(10):  #行
    #星星
	for j in range(10): #列
		print('*',end='')
	#换行
	print()
print('-----------------------4-2')

# 5.一个循环打印十行十列隔列变色小星星
for i in range(100):
	# 星星
	if i % 2 == 1:
		print('*',end='')
	else:
		print('&',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('-----------------------5')

# 6.一个循环打印十行十列隔行变色小星星
for i in range(100):
	#星星
	if i // 10 % 2 == 1:
		print('*',end='')
	else:
		print('&',end='')
	
	#换行
	if i % 10 == 9:
		print()
print('-----------------------6')

# 7.两个循环十行十列小星星
for i in range(10):  #行
	for j in range(10):  #列
		print('*',end='')  #星星
	print()  #换行
print('-----------------------7')

# 8.两个循环十行十列隔列/隔行换色小星星
for i in range(10):  #行
	for j in range(10):  #列  内层动的快,外层动的慢
	# 星星
		if j % 2 == 1:
			print('*',end='')
		else:
			print('&',end='')	
	#换行
	print()
print('-----------------------8-1 ')
	
for i in range(10):  #行
	for j in range(10):  #列  内层动的快,外层动的慢
	# 星星
		# if j % 2 == 1: #隔列换色
		if i  % 2 == 1:  #隔行换色  内层动的快,外层动的慢
			print('*',end='')
		else:
			print('&',end='')	
	#换行
	print()
print('-----------------------8-2 ')

# 9.99乘法表
for i in range(1,10): #行
	for j in range(1,i+1):  #列
	# 表达式
		print('{:d}*{:d}={:2d}'.format(i,j,i*j),end='')
	
	#换行
	print()
print('-----------------------9 ')

# 10.吉利数字100~999,找123 321 111
for i in range(100,1000):
	units = int(str(i)[-1])
	tens = int(str(i)[-2])
	hundreds = int(str(i)[-3])
	if tens == units and tens == hundreds:
		print(i)
	elif tens == units + 1 and tens == hundreds - 1:
		print(i)
	elif tens == units - 1 and tens == hundreds + 1:
		print(i)
print('-----------------------10 ')

# 11.公鸡1块钱1只,母鸡3块钱一只,小鸡5毛钱一只,问: 用100块钱买100只鸡,有多少种买法?
for i in range(20):
	for j in range(33):
		for k in range(100):
			if (i+j+k == 100) and ( i*5 + j*3 + k*1/3 == 100):   #优先级  算数> 位> 比较> 身份is >成员in > 逻辑 >赋值
				print('公鸡{:2d},母鸡{:2d},小鸡{:2d}'.format(i,j,k))
print('-----------------------11 ')

# 12.国际象棋
for i in range(64):
	# 星星
	if i // 8 % 2 == 0:
		if i % 2 == 0:
			print('&',end='')
		else:
			print('*',end='')
	else:
		if i % 2 == 0:
			print('*',end='')
		else:
			print('&',end='')
	
	if i % 8 == 7:
		print()
	# 换行
print('-----------------------12-1 ')

for i in range(8):  #行
	# for j in range(8):  #列
	#格子
	if i % 2 == 0:
		print('&*&*&*&*&*',end='')
	else:
		print('*&*&*&*&*&',end='')
		
	#换行
	print()
print('-----------------------12-2 ')


# 13.打印1~100不含有3的数字.   nok



















