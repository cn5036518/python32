# 打印菱形小星星
"""
     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *
"""

# 组成  空格  星星  换行
# 当前行空格数 = 6(总行数)- 当前行号i
# 当前行星星数 = 当前行号i * 2-1

# 三角形6行
for i in range(1,7):
	# 打印空格
	# for k in range(6-i,-1,-1): #最左边会多一个空格
	for k in range(5-i,-1,-1):
		print(' ',end='')	
	
	# 打印星星
	for j in range(2*i-1):
		print('*',end='')
	# 换行
	print()
	
# for i in range(1,7):  #正三角
for i in range(6,-1,-1):  #倒三角 i不能直接理解成行号
	# 打印空格
	for k in range(5-i,-1,-1):
	# for k in range(6-i,-1,-1):  #最左边会多一个空格
		print(' ',end='')	
	
	# 打印星星
	for j in range(2*i-1):
		print('*',end='')
	# 换行
	print()	
print('------------------------------------1')
	
# 三角形行数不固定
rows = 4  #
for i in range(1,rows+1):
	# 打印空格
	# for k in range(6-i,-1,-1): #最左边会多一个空格
	for k in range(rows-1-i,-1,-1):
		print(' ',end='')	
	
	# 打印星星
	for j in range(2*i-1):
		print('*',end='')
	# 换行
	print()
	
# for i in range(1,7):  #正三角
for i in range(rows,-1,-1):  #倒三角 i不能直接理解成行号
	# 打印空格
	for k in range(rows-1-i,-1,-1):
	# for k in range(6-i,-1,-1):  #最左边会多一个空格
		print(' ',end='')	
	
	# 打印星星
	for j in range(2*i-1):
		print('*',end='')
	# 换行
	print()	
print('------------------------------------2')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
















