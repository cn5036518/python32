# 第一象限
for i in range(1,10):  #i 控制行
    # 表达式
	for j in range(1,i+1):  #j 控制列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print()  #换行
print('------------------------1')

# 第四象限
# for i in range(1,10):  # 第一象限
for i in range(9,0,-1):  #i是乘数1,而不是行号  #第四象限
    #表达式
	for j in range(1,1+i): #j是乘数2(列号)
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('------------------------2')

# 第二象限
for i in range(1,10):   #第二象限
	#空格  空格个数= 9-行号(乘数1)
	for k in range(9-i,0,-1):  #9-i只要是正数,步长就必须是-1
		print('{:s}'.format('       '),end='')	  #7个空格一组

	#表达式
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	print()  #换行
	
print('------------------------3')

# 第三象限
# for i in range(9,0,-1): #第二象限   
for i in range(9,0,-1): #i是乘数1,而不是行号  #第三象限
	#空格     空格个数= 9- 乘数1
	for k in range(9-i,0,-1): ##9-i只要是正数,步长就必须是-1
		print('{:s}'.format('       '),end='')
	
	#表达式
	for j in range(1,i+1):
		print('{:d}*{:d}={:2d} '.format(i,j,i*i),end='')
	
	#换行
	print()
print('------------------------4')
























