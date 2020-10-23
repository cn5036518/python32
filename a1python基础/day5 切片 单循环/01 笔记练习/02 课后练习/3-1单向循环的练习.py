# (1) 打印 一行 十个小星星* help(print)
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
# print('*',end='')

'''
i = 0
while i < 10:
	# end = '' 打印时,尾部默认不加换行
	print('*',end='')
	i += 1
# 默认换行
# print()
print('====================1')

# (2)通过打印一个变量的形式,展示一行十个小星星
i = 0
strvar = ''
while i < 10:
	# 写上循环的逻辑
	strvar += '*' # strvar = strvar + '*'	
	i += 1
print(strvar)
'''
strvar += '*'  ==> strvar = '*'
strvar += '*'  ==> strvar = '*' + '*' = '**'
strvar += '*'  ==> strvar = '**' + '*' = '***'
...
strvar += '*'  ==> strvar = '*********' + '*' = '**********'
'''

# (3) 一行10个换色的星星  ★☆
# 方法1  #不推荐
i = 0
while i < 5:
	# 写上循环的逻辑
	print('★☆',end='')  #★☆★☆★☆★☆★☆
	i += 1
print('====================3-1')

# 方法2  print字符拼接
i = 0
while i < 10:
	# 写上循环的逻辑
	if i % 2 == 0:
		print('★',end='')  #取消换行
	else:
		print('☆',end='')	#★☆★☆★☆★☆★☆
	i += 1
print('====================3-2')

# 方法3  字符串拼接 +=
i = 0
strvar = ''
while i < 10:
	# 写上循环的逻辑
	if i % 2 == 0:
		strvar += '★'
	else:
		strvar += '☆'  	
	i += 1
print(strvar)  #★☆★☆★☆★☆★☆
print('====================3-3')
# 公式:任意数 和 n进行取余,余数的范围: 0 ~ (n-1)

# (4) 用一个循环,打印十行十列的小星星
'''
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
'''

# 方法1  print+end拼接字符
i = 0
while i < 100:
	# 写上循环的逻辑
	print('*',end='')  #打印100个星星,不换行
	# 打印换行 (在 9 19 29 ... 99)
	if i % 10 == 9:  #关键:余数是9 就换行
		print()  #换行
	i += 1
print('====================4-1')

# 方法2  print+end拼接字符2
i = 1
while i < 101:
	# 写上循环的逻辑
	print('*',end='')  #打印100个星星,不换行
	# 打印换行 (在 9 19 29 ... 99)
	if i % 10 == 0:  #关键:余数是0 就换行
		print()  #换行
	i += 1
print('====================4-2')

# 方法3  +=拼接字符串
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	strvar += '*'
	# 打印换行 (在 9 19 29 ... 99)
	if i % 10 == 9:  #关键:余数是9 就换行
		strvar += '\n'  #换行
	i += 1
print(strvar,end='')  #这里的end去掉最后多余的空行
print('====================4-3')

# 方法4  +=拼接字符串2
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	strvar += '*'
	# 打印换行 (在 9 19 29 ... 99)
	if i % 10 == 9:  #关键:余数是9 就打印一行,重置
		print(strvar)
		strvar = ''  #每行打印后,就重置
	i += 1
print('====================4-4')

# (5) 一个循环实现十行十列,换色的小星星
'''
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
★☆★☆★☆★☆★☆
'''
# 方法1  print + end 拼接字符  推荐 最简洁
i = 0
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i % 2 == 0:
		print('★',end='')
	else:
		print('☆',end='')
	
	# 2 打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		print()
	i += 1
print('====================5-1  推荐')

# 方法2  +=字符串拼接1
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i % 2 == 0:
		strvar += '★'
	else:
		strvar += '☆'
	
	# 2 打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		# print()
		strvar += '\n'  #拼接换行
	i += 1
print(strvar,end='')  #去掉最后一行的空行
print('====================5-2')

# 方法3  +=字符串拼接2
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i % 2 == 0:
		strvar += '★'
	else:
		strvar += '☆'
	
	# 2 打印当前行后,重置当前行
	if i % 10 == 9:
		print(strvar)
		strvar = ''  #
	i += 1
print('====================5-3')

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

# 方法1  print + end 拼接字符  推荐 最简洁
i = 0
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i // 10  % 2 == 0:   #关键:地板除后取余
		print('★',end='')
	else:
		print('☆',end='')
	
	# 2 打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		print()
	i += 1
print('====================6-1  推荐')

# 方法2  += 拼接字符串
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i // 10  % 2 == 0:   #关键:地板除后取余
		strvar += '★'
	else:
		strvar += '☆'
	
	# 2 打印换行 (在9 19 29 .. 99)
	if i % 10 == 9:
		# print()
		strvar += '\n'
	i += 1
print(strvar,end='')
print('====================6-2')

# 方法3  += 拼接字符串2
i = 0
strvar = ''
while i < 100:
	# 写上循环的逻辑
	# 1 打印星星
	if i // 10  % 2 == 0:   #关键:地板除后取余
		strvar += '★'
	else:
		strvar += '☆'
	
	# 2 打印当前行后 重置
	if i % 10 == 9:
		print(strvar)
		strvar = ''	
	i += 1
print('====================6-3')

# 方法4 
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
	i += 1
print('====================6-4')


'''
10~ 100 101 102 103 110..

10 ~19 ==> 1
20 ~29 ==> 2
30 ~39 ==> 3
90 ~99 ==> 9
100 ~ 109 ==> 0
'''



























	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	