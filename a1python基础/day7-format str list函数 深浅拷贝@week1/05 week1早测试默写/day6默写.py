#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/19 21:04

#1.用两个循环完成十行十列小星星
#2.用两个循环完成十行十列-隔列换色的小星星
#3.用两个循环完成十行十列-隔行换色的小星星
# 4.99乘法表
# 5.求吉利数字 100~999之间 找 111 222 333 123 234  654 321...
# 6.百钱买百鸡
# 7.国际象棋棋盘
# 8.break continue pass的作用
# 9.遍历container = [1,2,3,4,('噶','234',{'马春培','李虎凌','刘子涛'})]
# 10.遍历container = [('马云','小马哥'),['王健林','王思聪'],{'王宝强','宋小宝'}]


#1.用两个循环完成十行十列小星星
for i in range(1,11):
	# 打印星星
	for j in range(1,11):
		print('*',end='')
	# 换行
	print()  
print('---------------------------------1')


#2.用两个循环完成十行十列-隔列换色的小星星
for i in range(1,11):  #控制行
	# 打印星星
	for j in range(1,11): #控制列
		if j % 2 == 0:
			print('*',end='')
		else:
			print('&',end='')
	#换行
	print()
print('---------------------------------2')


#3.用两个循环完成十行十列-隔行换色的小星星
for i in range(1,11):  #行
	# 打印星星
	for j in range(1,11):  #列
		# if j % 2 == 0:  #隔列换色
		if i % 2 == 0:    #隔行换色
			print('*',end='')
		else:
			print('&',end='')
	# 换行
	print()
print('---------------------------------3')


# 4.99乘法表
# 第一象限
# 组成:  换行  9*9=81(表达式)
# 规律:  当前行乘数2 <= 当前行乘数1
#        当前行列数 <= 当前行行号
for i in range(1,10):  #控制行  (乘数1)
	# 打印表达式
	#当前行列数 <= 当前行行号
	for j in range(1,i+1): # 控制列 (乘数2)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('---------------------------------4-1')


# 第四象限
# 组成:  换行  9*9=81(表达式)
# 规律:  当前行乘数2 <= 当前行乘数1

# for i in range(1,10):  #控制乘数1    第一象限
for i in range(9,0,-1):  #控制乘数1  9 8 7... 1  第四象限
	# 打印表达式
	#当前行乘数2 <= 当前行乘数1
	for j in range(1,i+1): #控制乘数2
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('---------------------------------4-2')

# 第二象限
# 组成:  换行  9*9=81(表达式) 空格
# 规律:  当前行乘数2 <= 当前行乘数1
#        当前行列数 <= 当前行行号i   一组表达式(9*9=81)是一列
#        当前行空格数 = 9(总行数) - 当前行行号(i)
for i in range(1,10):
	# 打印空格
	# 当前行空格数 = 9(总行数) - 当前行行号(i)
	for k in range(9-i,0,-1):  #如果第二个参数是0,只要9-i是正数,步长只能是-1 否则,取不到值
		print('       ',end='')  #7个空格一组

	# 打印表达式
	# 当前行列数 <= 当前行行号i   一组表达式(9*9=81)是一列
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('---------------------------------4-3')

# 第三象限
# 组成:  换行  9*9=81(表达式) 空格
# 规律:  当前行乘数2 <= 当前行乘数1
#        当前行空格数 = 9(总行数) - 当前行行号(i)
# for i in range(1,10):  #第二象限
for i in range(9,-1,-1):  #第三象限
	# 打印空格
	for k in range(9-i,0,-1):  
		print('       ',end='')  #7个空格一组  扩展:修改这里的空格数(比如:3个空格一组),可以打印出等腰三角形

	# 打印表达式
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('---------------------------------4-4')

# 5.求吉利数字 100~999之间 找 111 222 333 123 234  654 321...
# 思路:先取出个位 十位 百位数字  ,然后判断相等和连续

for i in range(100,1000):
	units = int(str(i)[-1])
	tens =	int(str(i)[-2])
	hundreds =  int(str(i)[-3])
	if tens == units and tens == hundreds:
		print(i)
	elif tens == units + 1 and tens == hundreds - 1:
		print(i)
	elif tens == units - 1 and tens == hundreds + 1:
		print(i)
print('---------------------------------5')

# 6.百钱买百鸡
#公鸡5元一只 母鸡3元一只  小鸡3只一元  要求:100元买100只鸡,问 公鸡 母鸡 小鸡各买多少只?
for i in range(0,20): # 从0开始  公鸡
	for j in range(0,33): # 母鸡
		for k in range(0,100): #小鸡
			if (i + j + k == 100) and (5 * i + 3 * j + 1/3 * k == 100):  #算数运算符 > 逻辑运算符
				print('公鸡:{:2d},母鸡:{:2d},小鸡:{:2d}'.format(i,j,k))
print('---------------------------------6')


# 7.国际象棋棋盘
# 组成 :* & 换行

# 方法1  单循环
for i in range(64):  #控制格子64个
	#  打印格子
	if i // 8 % 2 == 0:
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
	if i % 8 == 7:
		print()
print('---------------------------------7-1')	

# 方法2  单循环
for i in range(8):  #控制行
	# 打印格子
	if i % 2 == 0:
		print('&*&*&*&*',end='')
	else:
		print('*&*&*&*&',end='')
	
	# 换行
	print()
print('---------------------------------7-2')

# 方法3  双循环
for i in range(8): #控制行
	# 打印格子
	if i % 2 == 0:
		# print('&*&*&*&*',end='')
		for j in range(8):    #控制列
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')		
	else:
		# print('*&*&*&*&',end='')
		for j in range(8):    #控制列
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')	
	# 换行
	print()
print('---------------------------------7-3')


# 8.break continue pass的作用
# break   跳出当前循环,不能一次跳出2个循环
# continue  跳出当次循环,进入到下一次循环 (while的continue 前面行必须是 i += 1,否则死循环)
#            continue不推荐在while中使用
# pass 		代码块占位符

# 9.遍历container = [1,2,3,4,('噶','234',{'马春培','李虎凌','刘子涛'})]
container = [1,2,3,4,('噶','234',{'马春培','李虎凌','刘子涛'})]  #不等长的二级容器
for i in container:
	if isinstance(i,(tuple)):
		for j in i:
			if isinstance(j,(set)):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)
print('---------------------------------9')

# 10.遍历container = [('马云','小马哥'),['王健林','王思聪'],{'王宝强','宋小宝'}]
container = [('马云','小马哥'),['王健林','王思聪'],{'王宝强','宋小宝'}]  #等长的二级容器
for a,b in container:
	print(a)
	print(b)
print('---------------------------------10')
	
# 变量的解包  (容器类型  str tuple  list  dict  set)
a,b,c = 'poi'  #字符串
print(a,b,c)  #p o i

a,b = (1,2)  # 元组
print(a,b)  # 1 2

a,b =  1,2  # 元组
print(a,b)  # 1 2

a,b = [3,4] # 列表
print(a,b)  #3 4

a,b = {'lmh':'林明辉','jsx':'贾帅先'}
print(a,b)  #lmh jsx

a,b = {'林明辉','贾率先'}
print(a,b)  #林明辉 贾率先  顺序不固定-不推荐
print('---------------------------------11')

# range(三个值) 逆向的从右到左
for i in range(3,-2,-1):  # 3 2 1 0 -1
	print(i)












































