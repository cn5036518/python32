#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/17 9:23

#1
i = 0
while i < 10:
	print('*',end='')
	i += 1
print('-----------------1')

j = 0
while j < 10:
	# 打印星星
	i = 0
	while i < 10:
		print('*', end='')
		i += 1
	#  换行
	print()
	j += 1
print('-----------------2')

j = 0
while j < 10:
	# 打印星星
	i = 0
	while i < 10:
		if i % 2 == 0:
			print('★', end='')
		else:
			print('☆', end='')
		i += 1
	#  换行
	print()
	j += 1
print('-----------------3 隔列换色')

# 先打印2行 ==内
# 再循环5次 --外


i = 0
while i <20:
	if i // 10 == 0:
		print('★', end='')
	elif i // 10 == 1:
		print('☆', end='')
	if i % 10 == 9:
		print()
	i += 1
print('-----------------4 隔行变色')


i = 0
while i <20:
	if i // 10 == 0:
		print('★', end='')
	elif i // 10 == 1:
		print('☆', end='')
	if i % 10 == 9:
		print()
	i += 1
print('-----------------')

j = 0
while j < 5:
	i = 0
	while i < 20:
		if i // 10 == 0:
			print('★', end='')
		elif i // 10 == 1:
			print('☆', end='')
		if i % 10 == 9:
			print()
		i += 1
	j += 1
print('-----------------4 隔行变色')

j = 0
while j < 10:
	# 打印星星
	i = 0
	while i < 10:
		if j % 2 == 0:  #这里i改成j  关键
			print('★', end='')
		else:
			print('☆', end='')
		i += 1
	#  换行
	print()
	j += 1
print('-----------------5 隔行换色')


# i = 0
# while i < 9:
# 	print('%s * %s = %s' % (i,j,i*j))
# 	i += 1

j = 1
while j < 10:
# while j < i:
	i = 1
	# while i < 10:
	while i <= j:  #关键
		# print('%s * %s = %s' % (j, i, i * j))
		print('%s * %s = %s   ' % (j, i, i * j),end='')  #不换行 关键
		i += 1
	print()
	j += 1
print('-----------------6 乘法表')

j = 1
while j < 10:
# while j < i:
	i = 1
	# while i < 10:
	while i <= j:  #关键
		# print('%s * %s = %s' % (j, i, i * j))
		print('%d * %d = %2d' % (j, i, i * j),end='   ')  #不换行  (加空格)关键
		i += 1
	print()
	j += 1
print('-----------------7 乘法表1 正向-一象限')

i = 9
while i >= 1:
	j = 1
	while j <=i:
		print('%d * %d = %2d' % (i,j,i*j),end='   ')
		j +=1
	print()
	i -= 1
print('-----------------8 乘法表2 逆向-4象限')

i = 1
while i <= 9:
	# 打印空格
	kongge = 9 - i
	while kongge >= 1:
		print("       ",end="")
		kongge -= 1

	# 打印表达式
	j = 1
	while j <= i:
		print('%d*%d=%2d' % (i,j,i * j),end=' ')
		j += 1

	# 打印换行
	print()
	i +=1
print('-----------------9 乘法表3 正向-2象限')

# 方向三
i = 1
while i <= 9:
	kongge = 9 - i
	# 打印空格
	while kongge > 0:
		print("       ", end="")
		kongge -= 1

	# 打印表达式
	j = 1
	while j <= i:
		print("%d*%d=%2d " % (i, j, i * j), end="")
		j += 1

	# 换行
	print()
	i += 1
print('-----------------10')


# 100-999
i = 100
while i <= 999:
	bai = str(i)[-1]
	shi = str(i)[-2]
	ge = str(i)[-3]
	if bai == shi and bai == ge:
		print('%s%s%s' % (bai,shi,ge))
	elif int(shi) == int(ge) + 1 and int(bai) == int(shi) +1 and int(bai) == int(ge) + 2:
		print('%s%s%s' % (bai,shi,ge))
	elif int(shi) == int(ge) - 1 and int(bai) == int(shi) -1 and int(bai) == int(ge) - 2 and int(bai) != 0:
		print('%s%s%s' % (bai,shi,ge))
	i += 1

print('-----------------11')


i = 0
while i <= 20:
	j = 0
	while j <= 33:
		k = 0
		# while k <= 300:
		while k <= 100:  #100只
			if (1/3) * k + 3*j +5*i == 100 and (i + k +j) == 100:
				print('公鸡%s只,母鸡%s只,小鸡%s只' % (i,j,k))
			k +=1
		j+=1
	i += 1
print('-----------------12 百钱买百鸡')
# 公鸡4只,母鸡18只,小鸡78只  4*5+18*3+78/3= 20 +54 +26
# 公鸡8只,母鸡11只,小鸡81只
# 公鸡12只,母鸡4只,小鸡84只

#


















