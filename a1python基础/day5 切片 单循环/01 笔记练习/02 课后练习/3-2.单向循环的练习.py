# ###单向循环的练习

# (1)打印 一行十个小星星* help(print)
# help 查看某个方法的文档
help(print)

'''
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
# print('*',end='')
'''
i = 0
while i<10:
	# end='' 打印时,尾部默认不加换行
	print('*',end='')  #**********
	i += 1
# 默认换行
# print()
print('--------------1')

# (2) 通过打印一个变量的形式,展现一行十个小星星
i = 0
strvar = ''
while i < 10:
	# 写上循环的逻辑
	strvar += '*' # strvar = strvar + '*'
	i += 1
print(strvar)  #**********
"""
strvar += '*' ==> strvar = '*'
strvar += '*' ==> strvar = '*' +'*' = '**'
strvar += '*' ==> strvar = '**'+'*'='***'
...

strvar += '*' ==> strvar = '*********'+'*'='*********'
"""

# (3) 一行十个换色的星星 ★☆★☆★☆★☆★☆
# 方法一
i = 0
while i < 5:
	print('★☆',end='')  #★☆★☆★☆★☆★☆
	i += 1
print('--------------3-1')
	
# 方法二
i = 0
while i < 10:
	if i % 2 == 0:
		print('★',end='')
	else:
		print('☆',end='')		
	i += 1
print('--------------3-2')

# 方法三
i = 0
strvar = ''
while i < 10:
	if i % 2 == 0:
		strvar += '★'
	else:
		strvar += '☆'	
	i += 1
print(strvar)  #★☆★☆★☆★☆★☆
print('--------------3-3')
# 公式:任意数 和n 进行取余,余数的范围:0~(n-1)

# (4) 用一个循环,打印十行十列小星星
"""
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
★★★★★★★★★★
"""
# 方法一 推荐 简洁
i = 0
while i < 100:
	# 逻辑写在这里
	print("*",end='')
	# 打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		print()	
	i +=1
print('--------------4-1')

# 方法二
i = 1
while i <= 100:
	#逻辑写在这里
	print('*',end='')
	# 打印换行 (在9 19 29 .. 99)
	if i % 10 == 0:
		print()	
	i += 1
print('--------------4-2')

# (5) 一个循环实现十行十列,换色的小星星
"""
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
★☆★☆★☆★☆★☆
"""

i = 0
while i < 100:
	#(1)打印星星
	if i % 2 == 0:
		print('★',end='')
	else:
		print('☆',end='')
	
	#(2)打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		print()
	i += 1
print('--------------5-1')

# (6) 一个循环实现十行十列,隔行换色的小星星
"""
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
★★★★★★★★★★
☆☆☆☆☆☆☆☆☆☆
"""

# 公式:任意数和n进行地板除,会出现n个相同的数
# 方法一
i = 0
while i < 100:
	# (1) 打印星星
	if i//10%2 == 0:
		print('★',end='')
	else:
		print('☆',end='')
	
	# (2) 打印换行(在9 19 29 .. 99)
	if i % 10 ==9:
		print()	
	i += 1
print('--------------6-1')	

# 方法二
i = 10
while i < 110:
	# 打印星星
	num = int(str(i)[-2])
	if num % 2 == 0:
		print('★',end='')
	else:
		print('☆',end='')
	
	# 打印换行
	if i % 10 == 9:
		print()
	i +=1
print('--------------6-2')	
































