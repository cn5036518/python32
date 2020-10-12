# ### 双向循环的专题练习

# 1.用两个循环完成十行十列的小星星
# for
for i in range(10):  #行
	for j in range(10):  #列
		print('*',end='') #星星
	print() #换行
print('--------------1-1')

# while
i = 0
while i < 10:  #行
	j = 0
	while j < 10: #列
		print('*',end='')
		j += 1	
	print()  #换行
	i += 1
print('--------------1-2')

# 2.用两个循环完成十行十列隔列换色的小星星
for i in range(10):  #行
	for j in range(10): #列
		if j % 2 == 0:  #星星
			print('*',end='')
		else:
			print('&',end='')
	print() #换行
print('--------------2')

# 3.用两个循环完成十行十列隔行换色的小星星
for i in range(10):
	for j in range(10):
		# if j % 2 == 0: #隔列换色
		if i % 2 == 0:   #隔行换色
			print('*',end='')
		else:
			print('&',end='')
	print() #换行
print('--------------3')

# 4.99乘法表  一二三四
# 第一象限
for i in range(1,10):  #行
	for j in range(1,i+1): #列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #表达式
	print() #换行
print('--------------4-1')

# 第四象限
for i in range(9,0,-1):  #乘数1
	for j in range(1,i+1): #乘数2
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #表达式
	print() #换行
print('--------------4-2')

# 第二象限
for i in range(1,10):  #行
	#空格
	for k in range(9-i,0,-1):  #空格+行号=9
		print('       ',end="") #7个空格一组

	for j in range(1,i+1): #列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #表达式
	print() #换行
print('--------------4-3')

# 第三象限
for i in range(9,0,-1):  #乘数1
	#空格
	for k in range(9-i,0,-1):  #空格+行号=9
		print('       ',end="") #7个空格一组

	for j in range(1,i+1): #乘数2
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')  #表达式
	print() #换行
print('--------------4-4')


# 求吉利数字 100 ~ 999 之间 找 111 222 333 123 456 654 321
for i in range(100,1000):
	units = int(str(i)[-1])
	tens = int(str(i)[-2])
	hundreds = int(str(i)[-3])
	if tens == units + 1 and tens == hundreds - 1:  #优先级 算数(+-)>比较(==)>逻辑(and)
		print(i)
	elif tens == units - 1 and tens == hundreds + 1:
		print(i)
	elif tens == units and tens == hundreds:
		print(i)
print('--------------5')

# 百钱买百鸡
# 公鸡一个五块钱，母鸡一个三块钱，小鸡三个一块钱，现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？
# """
for i in range(20):
	for j in range(33):
		for k in range(100):
			if i+k+j==100 and 5*i+3*j+1/3*k==100:
				print('公鸡{},母鸡{},小鸡{}'.format(i,j,k))
print('--------------6')

































