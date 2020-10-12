#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/20 10:22


# 1 女友找对象
	# 1-1.5  '小强,你在哪里?'
	# 1.5-1.7 '没有安全感'
	# 1.7-1.8 '帅哥,留个电话'
	# 1.8-2   '帅哥,你建议多一个女朋友么'

# 1 打印 一行十个小星星
# 2 通过打印一个变量的形式,展现一行十个小星星
# 3  一行十个换色的星星
# 4 用一个循环,打印十行十列小星星
# 5 一个循环实现十行十列,隔列换色的小星星
# 6 一个循环实现十行十列,隔行换色的小星星

# 1.字符串的拼接符号
# 2.字符串的重复符号
# 3.字符串的跨行拼接符号
# 4.字符串的切片完整格式


# 1 女友找对象
	# 1-1.5  '小强,你在哪里?'
	# 1.5-1.7 '没有安全感'
	# 1.7-1.8 '帅哥,留个电话'
	# 1.8-2   '帅哥,你建议多一个女朋友么'
height = 1.5
if height >= 1 and height < 1.5:
	print('小强,你在哪里?')
elif height >= 1.5 and height <1.7:
	print('没有安全感')
elif height >= 1.7 and height <1.8:
	print('帅哥,留个电话')
elif height >= 1.8 and height <2:
	print('帅哥,你建议多一个女朋友么')
else:
	print('请输入正常范围身高')
print('----------------------------1')


# 1 打印 一行十个小星星
for i in range(1,11):
	print('*',end='')  #**********
print('----------------------------1')

# 2 通过打印一个变量的形式,展现一行十个小星星
strvar = ''
for i in range(1,11):
	strvar += '*'
print(strvar)
print('----------------------------2')

# 3  一行十个换色的星星
for i in range(1,11):
	if i % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')  #&*&*&*&*&*
print('----------------------------3')		

# 4 用一个循环,打印十行十列小星星
# 组成  :  星星  换行
# 规律:   行号 和 列号  相等  #双循环用到

# 方法一 单循环
for i in range(0,100):  #控制星星个数  100个
	# 打印星星
	print('*',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('----------------------------4-1')	

# 方法二  双循环
for i in range(1,11):  #控制行
	# 打印星星
	for j in range(1,11):  #控制列
		print('*',end='')
	#换行
	print()
print('----------------------------4-2')		


# 5 一个循环实现十行十列,隔列换色的小星星
# 组成  :  黑星星 白星星  换行

# 方法1 单循环
for i in range(0,100): #控制星星个数  100个
	# 打印星星
	if i % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('----------------------------5-1')
		
# 方法2 双循环
for i in range(1,11):  #行
	# 打印星星
	for j in range(1,11):  #列
		if j % 2 == 0:
			print('*',end='')
		else:
			print('&',end='')
	# 换行
	print()
print('----------------------------5-2')	

# 6 一个循环实现十行十列,隔行换色的小星星
# 组成  :  黑星星 白星星  换行

# 方法1 单循环
for i in range(0,100):
	# 打印星星
	if i // 10 % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')

	#换行
	if i % 10 == 9:
		print()
print('----------------------------6-1')

# 方法2 双循环
for i in range(1,11):  # 控制行
	#打印星星
	for j in range(1,11): #控制列
		# if j % 2 == 0:  #隔列换色
		if i % 2 == 0:    #隔行换色
			print('*',end='')
		else:
			print('&',end='')	
	
	#换行
	print()
print('----------------------------6-2')



# 1.字符串的拼接符号   + +=
strvar = ''
strvar += '*'
print(strvar)  #*

# 2.字符串的重复符号  *
strvar = '*'
print(strvar * 3)  #***

# 3.字符串的跨行拼接符号  \
strvar = '我的\
祖国'           #直接enter回车换行
print(strvar)  #我的祖国
print('------------------------------3')

# strvar = '我的'\   #会报错
# '祖国2'   #SyntaxError: unexpected character after line continuation character
# print(strvar)  

# 4.字符串的切片完整格式
strvar = '我的祖国花园'
# strvar[开始索引:结束索引:步长]

print(strvar[:2])  #我的
print(strvar[2:])  #祖国花园
print(strvar[1:5]) #的祖国花
print(strvar[1:5:2]) #的国
print(strvar[-1:-5:-2]) #园国
print(strvar[5:0:-1]) #园花国祖的  
print(strvar[5:-1:-1])  #   #这里的参数2的-1是指的右边第一个,这里切不到元素  打印空行
print(strvar[5:-2:-1])  #园   #这里的参数2的-2是指的右边第2个   -2的前一个是-1 

print(strvar[::-1])  #反转 #园花国祖的我 
print('------------------------------4')

# print(range(5,-1,-1))  
for i in range(5,-1,-1):  # 5 4 3 2 1  #乘法表是range()有应用
	print(i)
print('------------------------------4-1')

# 字符串切片和range的区别
strvar = '我的祖国花园'
print(strvar[5:-1:-1])   #这里的参数2的-1是指的右边第一个,这里切不到元素  打印空行

for i in range(5,-1,-1):  # 5 4 3 2 1  #乘法表是range()有应用
	print(i)














































