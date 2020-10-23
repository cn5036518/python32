# ### python的内置函数
# abs 绝对值函数
print(abs(-1))
print(abs(100))

# round 四舍五入
# 奇进偶不进 n.5的情况特定发生
res = round(3.5)  #4
res = round(4.5)  #4
res = round(4.51) #5
print(res)

# sum 计算一个序列的和
lst = [1,2,3]
res = sum(lst)  #6
print(res) #6

total = 0
for i in lst:
	total += i
print(total)   #6

# max 获取一个序列里边的最大值
# min 获取一个序列里面的最小值
lst = (-100,1,2,3)
res = max(lst)  #3
res = min(lst)  #-100
print(res)  

# max / min 的高阶函数的使用方式  和sorted用法类似
tup = (('赵万里',100),('赵沈阳',101))
def func(n):
	# print(n)   #参数n:依次传入的是可迭代数据的元素
	# ('赵万里', 100)
# ('赵沈阳', 101)
	# 按照年龄找到最小值元组
	return n[-1]   #返回值是可迭代数据的元素的第二项(年龄)
	# return n

res = min(tup,key = func)
print(res)  #('赵万里', 100)
res = max(tup,key=func)
print(res)  #('赵沈阳', 101)
# 参数是键(小元组),return的是值的第二个元素(比较标准),  最后res也是键(小元组)
print('-----------------------1')

dic = {'赵万里':100,'赵沈阳':-5000}
def func(n):
	#如果是字典,参数n默认依次传递的是键
	# print(n)
	# 赵万里
# 赵沈阳
	print(dic[n])
	#100
# -5000
	return abs(dic[n])
		#100
# 5000

res = min(dic,key=func)
print(res)  #赵万里   
# 参数是键,return的是值的绝对值(比较标准),  最后res就是键
# 最后输出的是存款绝对值小的100,对应的键--赵万里


# pow 计算某个数值的x次方
# 如果是三个参数,前两个运算的结果和第三个参数取余
print(pow(2,3))  #8
print(pow(2,3,7))  #1
print(pow(2,3,4))  #0
print(pow(2,3,5))  #3


# range 产生指定范围数据的可迭代对象
# 一个参数
for i in range(3):  # 0 1 2
	print(i)
	
# 二个参数
for i in range(3,5): #3 4
	print(i)

# 三个参数
# 正向
for i in range(1,9,5): # 1 6 取头舍尾
	print(i)
	
# 逆向
for i in range(9,1,-3):  # 9 6 3
	print(i)
	
# bin 将十进制数据转化为二进制
print(bin(8))   #0b1000
# oct 将十进制数据转化为八进制
print(oct(8))   #0o10
# hex 将十进制数据转化为十六进制
print(hex(16))  #0x10


# chr  将ASCII编码转换为字符
print(chr(65))  #A
# ord  将字符转换为	ASCII编码
print(ord('A'))  #65


# ### eval 和 exec 在和第三方用户交互的时候,谨慎使用,防止攻击(删除数据库等)
# eval  将字符串当做python代码执行
strvar = 'print(123)'
print(strvar)  #print(123)
eval(strvar)  #123
print('-----------------------1')
res = eval(strvar)  #123
print(res,type(res))  #None <class 'NoneType'>

strvar = 'a=3'
# eval(strvar)  #SyntaxError: invalid syntax  
# error eval的局限性 不能创建变量

# exec  将字符串当做python代码执行(功能更强大)
strvar = 'a=3'
exec(strvar)
print(a)  #3   #创建变量的第5个方法

# a = 1   方法1
# a,b = 1,2   方法2
# a = b = 2	   方法3
# globals 		方法4   增加键值对
# exec			方法5

strvar = '''
for i in range(3):
	print(i)
'''
exec(strvar)
# 0
# 1
# 2


# repr 不转义字符输出字符串
strvar = 'D\ython32_gx\tay14'
res = repr(strvar)
print(res)  #'D\\ython32_gx\tay14'

strvar = r'D"\ython32_gx\tay14'
print(res)   #'D\\ython32_gx\tay14'


# input 接受输入字符串
# res = input('输入内容')
# print(res,type(res))

# hash 生成哈希值
# 文件校验
with open('linux2.txt',mode='r',encoding='utf-8') as fp1,open('linux2-11.txt',mode='r',encoding='utf-8') as fp2:
	res1 = hash(fp1.read())
	res2 = hash(fp2.read())
	if res1 == res2:
		print('文件校验成功,2个文件的内容完全一致')
	else:
		print('文件校验失败')  #即便多一个空格,2个文件的内容就不同























