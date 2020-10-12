# ### python内置函数
# 1 abs 绝对值函数
print(abs(-1))  #1

# 2 round  四舍五入
# 奇进偶不进 n.5的情况下特定发生
print(round(3.5))  #4
print(round(4.5))  #4

# 3 sum 计算一个序列的和
lst = [1,3,4]
print(sum(lst))  #8

total = 0
for i in lst:
	total += i
print(total)  #8

# 4 max    获取一个序列里边的最大值
#   min    获取一个序列里边的最小值
lst = (-100,1,2,3,4,34)
print(max(lst))  #34
print(min(lst))  #-100

# max / min 的高阶函数的使用方式  和sorted类似
tup = (   ("赵万里",100)  , ("赵沈阳",101) )
def func(n):
	# print(n)
	# ('赵万里', 100)
# ('赵沈阳', 101)
	return n[-1]   #比较的标准

res = max(tup,key=func)
print(res)  #('赵沈阳', 101)  #输入的是元组,输出的是元组
res = min(tup,key=func)
print(res) 
print('----------------------------4-1')


dic = {"赵万里":100,"赵沈阳":200,"孟凡伟":-5000}
def func(n):
	# print(n)  ## 如果是字典,默认传递的是键
	return abs(dic[n])
res = min(dic,key=func)
print(res)  #赵万里    #输入的是键,输出的是键

# 5 pow 
print(pow(2,3))  #8
print(pow(2,3,7))  #1

# 6 bin  oct  hex
print(bin(8))  #0b1000
print(oct(8))  #0o10
print(hex(16)) #0x10
print('----------------------------6')

# 7 chr  ord
print(chr(65))  #'A'
print(ord('a'))  # 97
print('----------------------------7')

# 8 eval exec
strvar = 'int(15)'
print(strvar) #int15
res = eval(strvar)
print(res,type(res))  #15 <class 'int'>

# strvar = 'a=3'
# eval(strval)
# NameError: name 'strval' is not defined

strvar = 'a=3'
exec(strvar)
print(a)  #3

strvar = '''
for i in range(3):
	print(i)
'''
exec(strvar)
print('----------------------------8')

# 9 repr 
strvar = "D:\nython32_gx\tay14"
print(repr(strvar))  #'D:\nython32_gx\tay14'

strvar = r"D:\nython32_gx\tay14"
print(strvar)   #D:\nython32_gx\tay14


# 10 hash 文件内容对比
with open('__init__.py',mode='r',encoding='utf-8') as fp1,open('__init__ 1.py',mode='r',encoding='utf-8') as fp2:
	res1 = hash(fp1.read())
	res2 = hash(fp2.read())
	if res1 == res2:
		print('2个文件内容一致')
	else:
		print('2个文件内容不一致')
















































