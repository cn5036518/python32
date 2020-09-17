# ### 双向循环的专题练习

# 1.用两个循环完成十行十列的小星星
j = 0
while j < 10:
	# 打印一行星星
	i = 0
	while i < 10:
		print('*',end='')
		i +=1
		
	# 换行
	print()
	j += 1

# 2.用两个循环完成十行十列的隔列换色的小星星
"""
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
☆★☆★☆★☆★☆★
"""

i = 0
while i < 10:
	# 打印一行黑白相间的星星
	j = 0
	while j < 10:
		if j % 2 == 0:
			print('★',end='')
		else:
			print('☆',end='')		
		j += 1
	
	# 打印换行
	print()	
	i += 1
print('---------------------------2')

# 3. 用两个循环完成十行十列隔行换色的小星星
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
'''
外层的循环i动的慢
内层的循环j动的快
外层的i动一次,内层的循环动10次
'''
i = 0
while i < 10:
	j = 0
	while j < 10:
		if i % 2 == 0:   # 隔行换色
		# if i % 2 == 0:  #隔列换色
			print('☆',end='')
		else:
			print('★',end='')		
		j += 1	
	print()
	i += 1
print('---------------------------3')

# 4.  99 乘法表
# 方向一   正向(一象限)
i = 1
while i <= 9:
	# 打印表达式
	j = 1
	while j <= i:
		print('%d*%d=%2d ' % (i,j,i*j),end='')	
		j += 1
		
	# 换行
	print()
	
	i += 1
print('---------------------------4-1 正向(一象限)')

# 1*1= 1 
# 2*1= 2 2*2= 4 
# 3*1= 3 3*2= 6 3*3= 9 
# 4*1= 4 4*2= 8 4*3=12 4*4=16 
# 5*1= 5 5*2=10 5*3=15 5*4=20 5*5=25 
# 6*1= 6 6*2=12 6*3=18 6*4=24 6*5=30 6*6=36 
# 7*1= 7 7*2=14 7*3=21 7*4=28 7*5=35 7*6=42 7*7=49 
# 8*1= 8 8*2=16 8*3=24 8*4=32 8*5=40 8*6=48 8*7=56 8*8=64 
# 9*1= 9 9*2=18 9*3=27 9*4=36 9*5=45 9*6=54 9*7=63 9*8=72 9*9=81 


# 方向二   逆向(4象限)
i = 9
while i >= 1:
	# 打印表达式
	j = 1
	while j <= i:
		print('%d*%d=%2d ' % (i,j,i*j),end="")
		j += 1
	
	# 换行
	print()
	i -= 1
print('---------------------------4-2  逆向(4象限)')

# 方向三   逆向(2象限) 空格
i = 1
while i <= 9:
	#打印空格
	kongge = 9 - i
	while kongge >=1:
		print('       ',end='')  #这里7个空格是一组
		# print(' '*7,end='')  
		kongge -= 1                                                
	
	#打印表达式
	j = 1
	while j <= i:
		print('%d*%d=%2d ' % (i,j,i*j),end='')	
		j += 1
	
	# 换行
	print()
	i +=1 
print('---------------------------4-3  逆向(2象限)')

# 方向四   逆向(3象限) 空格
i = 9
while i >= 1:
	#打印空格
	kongge = 9 -i
	while kongge >=1:
		print('       ',end='')
		kongge -=1  #注意:这里是-= 而不是+= 
	
	#打印表达式
	j = 1
	while j <= i:
		print('%d*%d=%2d ' % (i,j,i*j),end='')
		j += 1
	
	#换行
	print()

	i -= 1
print('---------------------------4-4  逆向(3象限)')

# 5.求吉利数字 100~999 之间 找 111 222 333 123 456 654 321 ...
'''
// 可以获取一个数高位
%  可以获取一个数低位
baiwei = 345//100  			3
shiwei = 345//10 % 10		4 
gewei = 345%10  			5
'''

# 方法一
i = 100
while i <= 999:
	#先获取到 个位 十位 百位的数字
	baiwei = i //100
	shiwei = i // 10 % 10
	gewei = i%10
	
	#判断比较个位 十位 百位数字
	if shiwei == gewei and shiwei == baiwei:
		print(i)
	elif shiwei == gewei + 1 and shiwei == baiwei - 1:
		# pass
		print(i)
	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)

	i += 1
print('---------------------------5-1')


# 方法二
i = 100
while i <= 999:
	#先获取到 个位 十位 百位的数字
	strvar = str(i)
	gewei = int(strvar[-1])  #字符串不能比较,需要转换成数字才行
	shiwei = int(strvar[-2])
	baiwei = int(strvar[-3])
	
	#判断比较个位 十位 百位数字
	if shiwei == gewei and shiwei == baiwei:
		print(i)
	elif shiwei == gewei + 1 and shiwei == baiwei - 1:
		# pass
		print(i)
	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)
	i += 1
print('---------------------------5-2')

# 方法三
# 思路:  123  个位+百位= 十位*2  
#   但是,需要排除 135 531 
i = 100
while i <= 999:
		#先获取到 个位 十位 百位的数字
	strvar = str(i)
	gewei = int(strvar[-1])  #字符串不能比较,需要转换成数字才行
	shiwei = int(strvar[-2])
	baiwei = int(strvar[-3])
	
	if (2*shiwei == gewei + baiwei) and (shiwei == gewei + 1 or shiwei == gewei -1):   #少冒号
		print(i)
	elif shiwei == gewei and shiwei == baiwei:
		print(i)
	i += 1
print('---------------------------5-3')

# 6.百钱买百鸡
# 公鸡一个五块钱,母鸡一个三块钱,小鸡三个一块钱
# 现在要用一百块买一百只鸡
# 问公鸡 母鸡,小鸡各多少只?

i = 0
while i <=20:
	j = 0 
	while j <= 33:
		k = 0
		while k <=100:
			if (i+j+k== 100) and (5*i + 3* j + 1/3 * k == 100):
			# 注意:是== 而不是=
				print('公鸡%s,母鸡%s,小鸡%s' % (i,j,k))		
			k +=1	
		j += 1
	i +=1

# 公鸡0,母鸡25,小鸡75
# 公鸡4,母鸡18,小鸡78
# 公鸡8,母鸡11,小鸡81
# 公鸡12,母鸡4,小鸡84























































