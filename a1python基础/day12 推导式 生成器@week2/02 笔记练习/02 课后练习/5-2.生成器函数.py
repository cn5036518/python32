# ### 生成器函数
# 1 基本语法
def mygen():
	print('111')
	yield 1
	
	print('222')
	yield 2
	
	print('333')
	yield 3
	
gen = mygen()

res = next(gen)
print(res)  #1
print('---------------1')
# 111
# 1

res = next(gen)
print(res)  #2
print('---------------2')
# 222
# 2

res = next(gen)
print(res)  #3
print('---------------3')
# 333
# 3

# 2 优化生成器代码
def mygen():
	for i in range(1,11):
		return i  #返回1后,函数就结束了
res = mygen()
print(res) #1
print('--------------------2-1')

def mygen():
	for i in range(1,11):
		yield i  #
gen = mygen()

for i in range(3):
	num = next(gen)
	print('我的球衣号码是{}'.format(num))
print('-------------------2-2')
for i in range(3):
	num = next(gen)
	print('我的球衣号码是{}'.format(num))

# 4 yield from的使用
# 将一个可迭代对象变成一个迭代器返回
def mygen():
	lst = ["张磊","李亚峰","刘一峰","王同培"]
	yield from lst

gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# 张磊
# 李亚峰
# 刘一峰
# 王同培
print('----------------------4')

# 5 斐波那契数列 生成器实现
# 1 1 2 3 5 8...
def mygen(maxval):
	a,b = 0,1
	i = 0
	while i < maxval:
		yield b  #生成器函数
		a,b = b,a+b
		i += 1
		
gen = mygen(10)
# print(list(gen))
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

for i in range(3):
	print(next(gen))
print('----------------------5-1')

for i in range(3):
	print(next(gen))
print('----------------------5-2')


# 方法2  生成器  for
def mygen(maxval):
	a,b = 0,1
	for i in range(0,maxval):	
		yield b
		a,b = b,a+b

gen = mygen(10)
print(list(gen))
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 3 send
def mygen():
	print('start')
	
	res = yield '内部1'  #第一次调用,到此结束
	print(res,'------------内部11')
	
	res = yield '内部2'
	print(res,'------------内部12')
	
	res = yield '内部3'
	print(res,'------------内部13')
	
	print('end')

gen = mygen()

res1 = gen.send(None)
# res = gen.send()  #TypeError: send() takes exactly one argument (0 given)
print(res1)
print('-----------------1')
# start
# 内部1

res2 = gen.send('100')
print(res2)
print('-----------------2')
# 100 ------------内部11
# 内部2

res3 = gen.send('200')
print(res3)
print('-----------------3')
# 200 ------------内部12
# 内部3

res4 = gen.send('300')
print(res4)
print('-----------------4')
# 300 ------------内部13
#end


























