#1.用两个循环完成十行十列小星星
for i in range(10): #行
	for j in range(10): #列
	#星星
		print('*',end='')
	#换行
	print()
print('-----------------1')

#2.用两个循环完成十行十列隔列换色的小星星
for i in range(10):
	for j in range(10):
		#星星
		if j % 2 == 0:  #内循环 变动快 隔列换色  
			print('*',end='')
		else:
			print('&',end='')
	#换行
	print()
print('-----------------2')

#3.用两个循环完成十行十列隔行换色的小星星
for i in range(10):
	for j in range(10):
		#星星
		# if j % 2 == 0:  #隔列换色
		if i % 2 == 0:    #隔行换色
			print("*",end='')
		else:
			print('&',end='')
	
	#换行
	print()
print('-----------------3')

# 4.99乘法表  
# 第一象限  234象限--nok
for i in range(1,10): #行
	for j in range(1,i+1): #列
		#表达式
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('-----------------4-1')



#5.求吉利数字100～ 999之间找111 222 333 123 456 654 321 ...
for i in range(100,1000):
	units = int(str(i)[-1])
	tens = int(str(i)[-2])
	hundreds = int(str(i)[-3])
	if tens == units and tens == hundreds:
		print(i)
	elif tens == units + 1 and tens == hundreds - 1:   #优先级:算数(+-)>比较(==)>逻辑and
		print(i)
	elif tens == units - 1 and tens == hundreds + 1:
		print(i)
print('-----------------5')

#6.百钱买百鸡  公鸡5元  母鸡3元  小鸡3只一元
for i in range(20):
	for j in range(33):
		for k in range(100):
			if i+j+k==100 and 5*i+3*j+1/3*k== 100:   #优先级:算数(+-)>比较(==)>逻辑and
				print('公鸡{},母鸡{},小鸡{}'.format(i,j,k))
print('-----------------6')

# 7.国际象棋  --nok
# 单循环
# 方法1
for i in range(64): #总数
	# 格子
	if i //8 % 2 == 0:
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
print('-----------------7-1 当循环1')

# 单循环
# 方法2   --nok
for i in range(8): #行
	#格子
	if i % 2 == 0:
		print('*&*&*&*&',end='')
	else:
		print('&*&*&*&*',end='')

	#换行
	print()
print('-----------------7-2 单循环2')

# 双循环  --nok2
for i in range(8): #行
	#格子
	if i % 2 == 0:  #偶数行
		for j in range(8): #列		
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')   #print('*&*&*&*&')
	else:  #奇数行
		for j in range(8): #列		
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')  #print('&*&*&*&*')
	#换行
	print()
print('-----------------7-3 双循环')

#单循环  关键点
for i in range(8):
	# 星星
	if i % 2 == 0:
		print('*&*&*&*&',end='')
	else:
		print('&*&*&*&*',end='')
	# 换行
	print()
print('-----------------7-2-1 单循环')	

#双循环
for i in range(8):	 #行
	#星星
	if i % 2 == 0:
		for j in range(8): #列
			if j % 2 == 0:
				print('*',end='')
			else:
				print('&',end='')  #'*&*&*&*&'
	else:
		for j in range(8):	 #列
			if j % 2 == 0:
				print('&',end='')
			else:
				print('*',end='')	  #'&*&*&*&*'
	#换行
	print()
print('-----------------7-3-1 双循环')

#8.break continue pass的作用
# break 跳出整个循环，只能跳出一层
# continue  跳出当次循环,进入到下一次循环   和while不推荐搭配
# pass  	代码占位

#9.遍历container=[1,2,3,4，("嗄","234",{"马春配", "李虎凌","刘子涛"})
container=[1,2,3,4,("嗄","234",{"马春配", "李虎凌","刘子涛"})]
for i in container:
	if isinstance(i,tuple):
		for j in i:
			if isinstance(j,set):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)
print('-----------------9')

# 1
# 2
# 3
# 4
# 嗄
# 234
# 刘子涛
# 马春配
# 李虎凌

#10.遍历container =[ ("马云";,"小马哥"; "马春配")，["王健林"."王思聪" ,"王志国"1,{("王宝强" ,r马蓉 "未小宝")]

container =[ ("马云","小马哥","马春配"),["王健林","王思聪" ,"王志国"],("王宝强" ,'马蓉', "未小宝")]

for a,b,c in container:
	print(a,b,c)
# 马云 小马哥 马春配
# 王健林 王思聪 王志国
# 王宝强 马蓉 未小宝
print('-----------------10-1')

for i in container:
	for j in i:
		print(j)
# 马云
# 小马哥
# 马春配
# 王健林
# 王思聪
# 王志国
# 王宝强
# 马蓉
# 未小宝
print('-----------------10-2')





























