#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/21 10:46

''''''
'''
# part2
# 1.打印一行十个小星星
# 2.通过打印变量,直接输出一行十个小星星
# 3.打印一行十个小星星,奇数个打印★,偶数个打印☆
# 4.一个循环打印十行十列小星星
# 5.一个循环打印十行十列隔列变色小星星
# 6.一个循环打印十行十列隔行变色小星星
# 7.两个循环十行十列小星星
# 8.两个循环十行十列隔列/隔行换色小星星
# 9.99乘法表
# 10.吉利数字100~999,找123 321 111
# 11.公鸡1块钱1只,母鸡3块钱一只,小鸡5毛钱一只,问: 用100块钱买100只鸡,有多少种买法?
# 12.国际象棋
# 13.打印1~100不含有3的数字.   nok
'''

# 1.打印一行十个小星星
for i in range(10):
	print('*',end='')  #**********  后面无空行(换行)
print('---------------------1')

# 2.通过打印变量,直接输出一行十个小星星
strvar = ''
for i in range(10):
	strvar += '*'
print(strvar)  #**********  后面有空行(换行)
print('---------------------2')


# 3.打印一行十个小星星,奇数个打印★,偶数个打印☆
for i in range(10):
	if i % 2 == 0:
		print('*',end='')
	else:
		print('#',end='')  #*#*#*#*#*#
print('---------------------3')

# 4.一个循环打印十行十列小星星
# 组成   星星  换行
for i in range(100):  #星星个数
    # 星星
	print('*',end='')
	# 换行
	if i % 10 == 9:
		print()
print('---------------------4')

# 5.一个循环打印十行十列隔列变色小星星
# 组成   星星(黑白)  换行
for i in range(100):
	# 星星
	if i % 2 == 0:
		print('*',end='')
	else:
		print('#',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('---------------------5')

# 6.一个循环打印十行十列隔行变色小星星
# 组成   星星(黑白)  换行
for i in range(100):
	# 星星
	# if i % 2 == 0:  #隔行换色
	if i // 10 % 2 == 0:  #隔列换色
		print('*',end='')
	else:
		print('#',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('---------------------6')

# 7.两个循环十行十列小星星
# 组成   星星  换行
for i in range(10):  #行
	for j in range(10):  #控制列
		print('*',end='') #星星
	print()  # 换行
print('---------------------7')

# 8.两个循环十行十列隔列/隔行换色小星星
# 组成   星星(黑白)  换行
for i in range(10):  #控制行
	for j in range(10): # 控制列
		if j % 2 == 0:
			print('*',end='')
		else:
			print('#',end='')		
	print() # 换行
print('---------------------8-1')

for i in range(10):  #控制行
	for j in range(10): # 控制列
		# if j % 2 == 0:  #隔列换色
		if i % 2 == 0:    # 隔行换色
			print('*',end='')
		else:
			print('#',end='')		
	print() # 换行
print('---------------------8-2')

# 9.99乘法表
# 组成   表达式  换行
# 规律   当前行列数 <= 当前行行号i
# 第一象限
for i in range(1,10):  #控制行
	for j in range(1,i+1): #控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')		
	print() #换行
print('---------------------9-1')

# 第四象限
# for i in range(1,10):  #控制行  第一象限
for i in range(9,0,-1):  #控制行  第四象限
	for j in range(1,i+1): #控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')		
	print() #换行
print('---------------------9-4')

# 第二象限
# 组成   表达式  换行 空格
# 规律   当前行列数 <= 当前行行号i
#		 当前行空格数 = 9(总行数)- 当前行行号i
for i in range(1,10):  #控制行
	# 空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #空格7个一组	
	
	# 星星
	for j in range(1,i+1): #控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')		
	print() #换行
print('---------------------9-2')

# 第三象限
# 组成   表达式  换行 空格
# 规律   当前行列数 <= 当前行行号i
#		 当前行空格数 = 9(总行数)- 当前行行号i
# for i in range(1,10):  #控制行  第二象限
for i in range(9,0,-1):  #控制行    第三象限
	# 空格
	for k in range(9-i,0,-1):
		print('       ',end='')  #空格7个一组	
	
	# 星星
	for j in range(1,i+1): #控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')		
	print() #换行
print('---------------------9-2')

# 10.吉利数字100~999,找123 321 111
for i in range(100,1000):
	units = int(str(i)[-1])
	tens = int(str(i)[-2])
	hundreds = int(str(i)[-3])
	if tens == units and tens == hundreds:
		print(i)
	elif tens == units + 1 and tens == hundreds - 1:  #算数运算符(+ -) > 比较运算符(==)  优先级
		print(i)
	elif tens == units - 1 and tens == hundreds + 1:
		print(i)
print('---------------------10-1')

# 11.公鸡1块钱1只,母鸡3块钱一只,小鸡5毛钱一只,问: 用100块钱买100只鸡,有多少种买法?
for i in range(20):
	for j in range(33):
		for k in range(100):
			# if i+j+k == 100 and 5*i + 3*j + 1/3*k == 100:   #算数运算符(+ -) > 比较运算符(==)  >逻辑运算符and 优先级
			if (i+j+k == 100) and (5*i + 3*j + 1/3*k == 100):   #算数运算符(+ -) > 比较运算符(==)  >逻辑运算符and 优先级
				print('公鸡:{:2d},母鸡:{:2d},小鸡:{:2d}'.format(i,j,k))
print('---------------------11-1')

# 12.国际象棋
# 组成:格子  换行
# 方法1  单循环
for i in range(64):  # 格子个数
	# 格子
	if i // 10 % 2 == 0:
		if i % 2 == 0:
			print('*',end='')
		else:
			print('#',end='')
	else:
		if i % 2 == 0:
			print('#',end='')
		else:
			print('*',end='')	
	
	# 换行
	if i % 8 == 7:
		print()
print('---------------------12-1')

# 方法2  单循环2
for i in range(8):  #控制行
	# 格子
	if i % 2 == 0:
		print('*&*&*&*&',end='')
	else:
		print('&*&*&*&*',end='')
	
	# 换行
	print()
print('---------------------12-2')

# 方法3  双循环
for i in range(8):  #控制行
	# 格子
	if i % 2 == 0:
		# print('*&*&*&*&',end='')
		for j in range(8):   #控制列
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')
	else:
		# print('&*&*&*&*',end='')
		for j in range(8):  #控制列
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')
	
	# 换行
	print()
print('---------------------12-3')

# 13.打印1~100不含有3的数字.   nok
for i in range(1,101):
	# if 3 in str(i):  #TypeError: 'in <string>' requires string as left operand, not int
	if '3' not in str(i):
		print(i)
	
print('---------------------13')		












































