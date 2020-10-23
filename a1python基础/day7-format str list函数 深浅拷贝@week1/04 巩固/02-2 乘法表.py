#第一象限
for i in range(1,10):  #i 控制行号(乘数1)
	# 表达式
	for j in range(1,i+1):   #i+1 而不是i  #j控制列(乘数2)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	# 换行
	print()
print('-----------------------1')

#第四象限
# for i in range(1,10):   第一象限
for i in range(9,0,-1):  #i是乘数1  不是行号  第四象限
    # 表达式
	for j in range(1,i+1): #j是乘数2  (列号)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print()  #换行

print('-----------------------2')
#第二象限
for i in range(1,10):  #i是第一个乘数 行号
    # 空格   空格= 9-行号
	for k in range(9-i,0,-1):  
	# 9-i是正数(不管是递增还是递减趋势),步长必须是-1,否则取不到值
		print('       ',end='')  #7个空格一组
	
	# 表达式
	for j in range(1,i+1): #j是乘数2  (列号)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print()  #换行
	
print('-----------------------3')

#第三象限
# for i in range(1,10):  #第二象限
for i in range(9,0,-1):  #i是乘数1,而不能理解成行号  #第三象限
	#空格   空格 = 9-乘数1    9-i
	for k in range(9-i,0,-1):
	# 9-i是正数(不管是递增还是递减趋势),步长必须是-1,否则取不到值
		print('{:s}'.format('       '),end='')  #7个空格一组

	# 表达式
	for j in range(1,i+1):  #拼写错误 少了range
	# i是乘数2(列号)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print() #换行
	
#  第1行  0个空格   9列
#  第2行  1个空格   8列
#  第3行  2个空格   7列
print('----------------------- 4')

























