# ### 循环结构
# 特点:减少冗余代码,提升执行效率
'''
语法:
while 条件表达式:
	code1
	
(1) 初始化一个变量
(2) 写上循环的条件
(3) 自增自减的值
'''

# ### 打印 1 ~ 100
# (1) 初始化一个变量
i= 1
# (2) 写上循环的条件
while i <= 100:

	# (4) 写上循环的逻辑
	print(i)

	# (3) 自增自减的值
	i += 1 # i = i + 1
	
'''
代码解析:
第一次循环
i = 1 i <= 100 判断为真,执行循环体 print(1)
i += 1 i ==> 2

第二次循环
代码回到17行,重新进行条件判定
i = 2 i <= 100 判断为真,执行循环体 print(2)
i += 1 i ==> 3

第三次循环
代码回到17行,重新进行条件判定
i = 3 i <= 100 判断为真,执行循环体 print(3)
i += 1 i ==> 4


...
以此类推

直到i = 101 i <= 100 判断为假,不执行循环体,到此循环结束
1 ~ 100
'''


# ### 1 ~ 100的累积和

# (1) 初始化一个变量
i = 1
total = 0

# (2)  写上循环的条件
while i <= 100:
	# (4) 写上自定义的逻辑
	total += i	
	# (3) 自增自减的值
	i += 1
print(total) #5050

'''
代码解析:
第一次循环:
i = 1 i <= 100 判定为真True 执行循环体 total += i ==> total = total + i ==> 0 + 1
i += 1 ==> i = 2

第二次循环:
i = 2 i <= 100 判定为真True 执行循环体 total += i ==> total = total + i ==> 0 + 1 +2
i += 1 ==> i = 3

第三次循环:
i = 3 i <= 100 判定为真True 执行循环体 total += i ==> total = total + i ==> 0 + 1 +2 +3
i += 1 ==> i = 4

...
依次类推

当i = 101 101 <= 100 判定为假False  不执行循环体,到此,循环结束

total += i ==> total = total + i ==> 0 + 1 +2 +3 + .... + 100 ==> 5050
'''

# 死循环
'''
while True:
	print(1)
'''

# ### 用死循环的方法实现 1 ~ 100 累加和
i = 1
total = 0
sign = True
while sign:
	total += i
	i += 1
	
	# 判断i是否加到了101,步参与循环
	if i == 101:
		# 终止循环
		sign = Fasle
print(total) # 1~100 =5050
		
#打印 一行十个小星星* help(print)




























