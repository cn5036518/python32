
#出题 height
#女生找对象
#男生在1米~1.5米之间小强你在哪里
#男生在1.5~1.7米之间没有安全感~
#男生1.7~1.8米之间帅哥留个电话
# 男生1.8~2米之间帅哥你建议多一个女朋友吗

# height= float(input(请输入你的身高哈:))
# if height >=1 and height < 1.5:
# 	print('小强你在哪里')
# elif height >= 1.5 and height < 1.7:
# 	print('没有安全感')
# elif height >= 1.7 and height < 1.8:
# 	print('帅哥留个电话')
# elif height >=1.8 and height < 2:
# 	print('帅哥你建议多一个女朋友吗')
# else:
# 	print('输入范围不对哈')

#(1）打印一行十个小星星*
for i in range(10):
	print('*',end='')
print('-------------1')

#(2）通过打印一个变量的形式，展现一行十个小星星
strvar = ''
for i in range(10):
	strvar += "*"
print(strvar)
print('-------------2')

# (3)一行十个换色的星星
for i in range(10):
	if i % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
print('-------------3')

#(4）用一个循坏，打印十行十列小星星
for i in range(100):  #总数
	print('*',end='') #星星
	# 换行
	if i % 10 == 9:
		print()
print('-------------4')

# (5)一个循坏实现十行十列，隔列换色的小星星
for i in range(100):  #总数
	# 星星
	if i % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
	# 换行
	if i % 10 == 9:
		print()
print('-------------5')

#(6)一个循环实现十行十列，隔行换色的小星星
for i in range(100):
	#星星
	if i // 10 % 2 == 0:
		print('*',end='')
	else:
		print('&',end='')
	
	# 换行
	if i % 10 == 9:
		print()
print('-------------6')

# 1.字符串的拼接符号  += +
#2.字符串的重复符号  *
#3.字符串跨行拼接符号  \
#4.字符串切片完整格式
strvar = 'jfjafajhdha'
# strvar[:3]
# strvar[2:]
# strvar[1:-1:2]  #步长是正数,从左到右
print(strvar[10:0:-1])  #步长是负数,从右到左
print(strvar[-1:-9:-1])  #步长是负数,从右到左
# strvar[:]  #复制
# strvar[::-1]  #翻转






















