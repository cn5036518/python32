# ### python的内置函数
# 小结默写1

# 第一组
# 1 abs    绝对值函数
print(abs(-45))  #45

# 2 round  四舍五入
# """奇进偶不进 n.5的情况特定发生;"""
print(round(3.5)) #4
print(round(4.5)) #4
print(round(-3.5)) #-4
print(round(-3.51)) #-4  #注意
print(round(-4.5)) #-4
print('-----------------2 round')

# 3 sum    计算一个序列得和
lst = [1,2,3]
print(sum(lst))  #6

total = 0
for i in lst:
	total += i
print(total)  #6

# 4  max    获取一个序列里边的最大值
# min    获取一个序列里边的最小值
lst = [1,2,3]
print(max(lst)) #3
print(min(lst)) #1
print('-----------------4 max min')

# max / min 的高阶函数的使用方式   类似sorted
lst = [1,-3,-2]
def func(n):
	return abs(n)
	
res = max(lst,key=func)
print(res)    #-3
print('-----------------4 max ')

lst = [1,-3,-2]
def func(n):
	return abs(n)
	
res = min(lst,key=func)
print(res)  #1
print('-----------------4 min')

lst = [1,-3,-2]
def func(n):
	return abs(n)
	
lst = sorted(lst,key=func)
print(lst)  #[1,-2,-3]
print('-----------------4 sorted')


tup = (   ("赵万里",100)  , ("赵沈阳",101) , ("孟凡伟",99) )
# # 按照年龄找到最小值元组

def func(n):
	return n[-1]
res = min(tup,key=func)
print(res)  #('孟凡伟', 99) #传入的是元组,最后的值就是元组
print('-----------------4-1 min')

dic = {"赵万里":100,"赵沈阳":200,"孟凡伟":-5000}
# # 按照工资找到最大值的那个人
def func(n):
	# print(n)  #参数是字典的键
	return dic[n]  #返回值是比较标准
res = max(dic,key=func)
print(res)  #赵沈阳  #传入的是字典的键,最后的值就是字典的键
print('-----------------4-2 max')

# 5 pow    计算某个数值的x次方
# """如果是三个参数,前两个运算的结果和第三个参数取余"""
print(pow(2,3))  #8
print(pow(2,3,7)) #1
print(pow(2,3,4))  #0
print(pow(2,3,5))  #3
print('-----------------5 pow')

# 6 range  产生指定范围数据的可迭代对象
# for i in range(1,6,2):  # 1 3 5
	# print(i)

# for i in range(6,1,-1): # 6 5 4 3 2
	# print(i)
print('-----------------6 range')
print('-----------------第一组')

# 第二组
# 1 bin    将10进制数据转化为二进制
print(bin(10))  #0b1010

# oct    将10进制数据转化为八进制
print(oct(10)) #0o12

# hex    将10进制数据转化为16进制
print(hex(17))  #0x11
print('-----------------1 bin oct hex')

# 2 chr    将ASCII编码转换为字符
print(chr(97))  #a

# ord    将字符转换为ASCII编码
print(ord('a'))  #97
print('-----------------2 chr ord')
print('-----------------第二组')

# 第三组
# 1 eval和exec在和第三方用户交互时候,谨慎使用; 
# eval   将字符串当作python代码执行
strvar = 'print(123)'
eval(strvar)  #123

# strvar = '''
# for i in range(3):
	# print(i)
# '''
# eval(strvar)   #SyntaxError: invalid syntax   
# 01 eval不能执行多行字符串

# strvar = 'a=3'
# eval(strvar)
#SyntaxError: invalid syntax
# print(a)   
## 02 eval不能创建变量

print('-----------------1 eval')

# exec   将字符串当作python代码执行(功能更强大)
# strvar = '''
# for i in range(3):
	# print(i)
# '''
# exec(strvar)
# 0
# 1
# 2
# 01 exec可以执行多行字符串

strvar = 'a=3'
exec(strvar)
print(a)
## 02 exec可以创建变量

print('-----------------1-2 exec')

# 2 repr   不转义字符输出字符串
print(repr('\tpython,\npython'))
#'\tpython,\npython'
path1 = r'\tpython,\npython'
print(path1)
#\tpython,\npython
print('-----------------2 repr')

# 3 input  接受输入字符串
# name = input('请输入你的用户名:')  #name是str类型

# 4 hash   生成哈希值    
# 文件校验
with open('__init__.py',mode='r',encoding='utf-8') as fp1,open('__init__1.py',mode='r',encoding='utf-8') as fp2:
	res1 = hash(fp1.read())
	res2 = hash(fp2.read())
	if res1 == res2:
		print('两个文件完全一样')
	else:
		print('两个文件内容不一样')


# 小结 
# 内置函数分3组
# 第一组 7个
# abs    求绝对值
# round  四舍五入  奇进偶不进  n.5
# sum     求和
# max/min  最大值 最小值  高阶 类似sorted
# pow       幂运算 (取余)
# range     

# 第二组 5个
# bin()   十进制转二进制
# oct()   十进制转八进制
# hex()   十进制转十六进制
# chr()   ascii==> 字符
# ord()   字符==>ascii

# 第三组 4个
# eval/exec  把字符串当代码执行
			# exec可以执行多行字符串--三引号
			# exec可以创建变量
# repr   原型化输出
# input  接受字符串输入
# hash   校验文件的内容是否完全一致











































