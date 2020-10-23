# 五.上机题:(下面题目可以使用pycharm运行)
# 1. 打印下列图形
# * 
# ** 
# *** 
# **** 
# ***** 
for i in range(1,6):
	for j in range(1,i+1):
		print('*',end='')
	print()
print('-----------------------1')

# 2.有如下文件内容:
# alex是老男孩python发起人，创建人。
# alex其实是人妖。
# 谁说alex是sb？
# 你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
# 定义函数,将文件中所有的sb都替换成"大好人"然后写入到新文件

with open('a.txt',mode='r+',encoding='utf-8') as fp:
	res = fp.read()
	res = res.strip()
	# print(res)
	res2 = res.replace('sb','大好人')
	print(res2)
	fp.seek(0)
	fp.truncate()
	fp.write(res2)
print('-----------------------2')

# 3.用生成器,递归,尾递归方法完成斐波那契数列
#规律: 1 1 2 3 5 8 13...
# 方法1 生成器
def func(n):
	a,b = 0,1
	for i in range(n):
		# print(b)
		yield b
		a,b = b,a+b
gen = func(4)		
print(list(gen))  #[1, 1, 2, 3]

# 方法2 递归
def func(n):
	if n in (1,2):
		return 1
	else:
		return func(n-1) + func(n-2)
print(func(4)) #3

# 方法3 尾递归
def func(n,a=0,b=1):
	if n == 1:
		return b
	else:
		return func(n-1,b,a+b)
print(func(5))  #5
print('-----------------------3')

# 4.编写一个程序，求100~999之间所有的水仙花数
# 如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数,比如153.
for i in range(100,1000):
	units = int(str(i)[0])
	tens = int(str(i)[1])
	hundreds = int(str(i)[2])
	if i == units**3 + tens**3 + hundreds**3:
		print(i)
print('-----------------------4')









































