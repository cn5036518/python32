# ### 生成器函数

# 1 基本语法
def mygen():
	print('111')
	yield 1
	
	print('222')
	yield 2
	
	print('333')
	yield 3
	
# 初始化生成器函数  返回生成器对象(即-生成器)
gen = mygen()

# 第一次调用
res = next(gen)
print(res)  #111   1

# 第二次调用
res = next(gen)
print(res)  #222 2

# 第三次调用
res = next(gen)
print(res)  #333 3

# 第四次调用
# res = next(gen)  #StopIteration
# 报错的原因:没有更多的yield 返回数据,停止迭代

# 2 优化生成器代码
# 生成器应用的场景:大数据的范围中使用,不可直接用for遍历所有,
# 可能无法短时间内获取所有数据

def mygen():
	for i in range(1,101):
		yield i
#初始化生成器函数
# gen = mygen()
# for i in range(30):
# 	num = next(gen)
# 	print('我的球衣号码是{}'.format(num))
#
# print('--------')
# for i in range(40):
# 	num = next(gen)
# 	print('我的球衣号码是{}'.format(num))

# 4 yield from的使用
# 将一个可迭代对象变成一个迭代器返回
def mygen():
	lst = ["张磊","李亚峰","刘一峰","王同培"]
	yield from lst
	
# 初始化生成器函数
gen = mygen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen)) StopIteration

# 5 斐波那契数列  11 2 3 5 8 13..
# 使用生成器分段获取所有内容,而不是一股脑的把所有数据全部打印
def mygen(maxval):  #形参是数列中数据的个数
	a,b = 0,1
	i = 0
	while i < maxval:
		print(b)
		yield b  # 生成器的
		a,b = b,a+b  #a 赋值给 b  b赋值给 a+b
		i += 1
gen = mygen(5)
# print(list(gen))

# 第一次获取
for i in range(2):
	print(next(gen))
print('---------------------1')

# 第二次获取
for i in range(3):
	print(next(gen))
print('---------------------2 斐波那契数列')

# 3 send的使用方式(给上一个yield发送数据)
# next和send区别:
# 	next 只能取值
# 	send 不但能取值,还能发送值
# send 注意点:
# 	第一个send不能给yield 传值,默认只能写None
# 	最后一个yield 接受不到send的发送值
def mygen():
	print('start')
	
	res11 = yield '内部1'     #  第一次调用,到这里结束
	print(res11,'--内部1--')  # 100 --内部1--   #把'100'给到98行(第一个yield)  res11='100'   100 --内部1--
	
	res12 = yield '内部2'   #   第二次调用,到这里结束
	print(res12,'--内部2--')  #  res12 = '200'   200 --内部2--   把'200'给到101行(第二个yield)
	
	res13 = yield '内部3'   #    第三次调用,到这里结束
	print(res13,'--内部3--')  #
	
	print('end')
	
# 初始化生成器函数
gen = mygen()

# 第一次调用生成器
# 因为没有遇到yield保存的代码位置.
# 无法发送数据,默认第一次只能发送None

res1 = gen.send(None)  # start   res1是 内部1
print(res1,'--外部1--') #内部1 --外部1--
print('------------------------------1')

# # 第二次调用生成器
res2 = gen.send('100')  #把'100'给到98行(第一个yield)  res11='100'   100 --内部1--
print(res2,'--外部2--')  #res2是内部2   内部2 --外部2--
print('------------------------------2')
# #
# 第三次调用生成器
res3 = gen.send('200')   #把'200'给到101行(第二个yield)   res12 = '200'   200 --内部2--
print(res3,'--外部3--')  #res3是内部3    内部3 --外部3--
print('------------------------------3')
#

# 第四次调用生成器
res4 = gen.send('300')  #把'300'给到104行(第三个yield) , res13='300'   300 --内部3--   end
print(res4,'--外部4--')  #StopIteration
# 因为没有更多的yield 返回数据,gen.send(300)无法接受到返回值,停止迭代
print('------------------------------4')











































