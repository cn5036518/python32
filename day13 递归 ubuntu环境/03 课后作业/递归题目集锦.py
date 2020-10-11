# 递归题目集锦   20201011
# day13 课后作业
# 2.青蛙跳台阶  (递归实现)
# '''
# 一只青蛙要跳上n层高的台阶
# 一次能跳一级,也可以跳两级
# 请问这只青蛙有多少种跳上这个n层高台阶的方法?

# 普通递归
# 规律  1 2 3 5 8 13...   类斐波那契数列
def fog(n):
	if n in (1,2):  #1 递归终止条件
		return n    #2 返回参数(唯一)
	else:
		return fog(n-1) + fog(n-2)  #3 return 函数调自己(参数递减的规律  第一个参数-1) 
n1 = 4
res = fog(n1)
print(res)  #5
print('青蛙跳上{:d}层台阶有{:d}种方法'.format(n1,res))
#青蛙跳上[4]层台阶有[5]种方法
print('--------------------2 青蛙')


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
# 1普通递归
# 规律:将字符串第一位字符拿出来,放到字符串最后
strvar= '14235'
def func(strvar):
	if len(strvar) == 1:  #1 递归终止条件
		return strvar	  #2 返回参数(唯一)
	else:
		return func(strvar[1:]) + strvar[0]  #3 return 函数调自己(参数递减的规律  第一个参数-1的变种 字符串的长度-1 strvar[1:])
res = func(strvar)
print(res) #53241
print('--------------------3-1 翻转字符串')

# 2普通递归
# 规律:将字符串最后一位字符拿出来,放到字符串的第一位
strvar= '14235'
def func(strvar):
	if len(strvar) == 1:  #1 递归终止条件
		return strvar     #2 返回参数(唯一)
	else:
		return strvar[-1] + func(strvar[:-1])  #3 return 函数调自己(参数递减的规律  第一个参数-1的变种 字符串的长度-1 strvar[:-1])
res = func(strvar)
print(res) #53241
print('--------------------3-2 翻转字符串')

# 3尾递归
# 规律:将字符串最后一位字符拿出来,放到参数2-列表中,最后返回列表
strvar= '14235'
def func(len,lst):
	if len == 0:   #1 递归终止条件
		return lst #2 返回参数2--尾递归
	else:
		lst.append(strvar[len-1])  #3规律:将字符串最后一位字符拿出来,放到参数2-列表中  字符串长度递减1
		return func(len-1,lst)   # 4 return 函数调自己(参数递减的规律  第一个参数-1)  字符串长度递减1
len1 = len(strvar)
lst1 = []
lst = func(len1,lst1)
print(lst)  #['5', '3', '2', '4', '1']
res = ''.join(lst)
print(res)  #53241
print('--------------------3-3 翻转字符串')


# 4.斐波那契数列用尾递归实现
# 规律: 1 1 2 3 5 8 13...
# 方法1:普通递归
def fab(n):
	if n in (1,2):  #1 递归的结束条件
		return n     #2 返回参数(唯一)
	else:
		return fab(n-1) + fab(n-2)  # 3 return 函数调自己(参数递减的规律)  
n1 = 4
res = fab(n1)
print(res) #5
print('斐波那契数列中第{:d}个数是{:d}'.format(n1,res))
#斐波那契数列中第4个数是5
print('--------------------4-1 斐波那契数列')

# 方法2:普通实现
def fab(n):
	a,b = 0,1
	for i in range(n):
		print(b)	
		a,b = b,a+b
fab(4)
# 1
# 1
# 2
# 3
print('--------------------4-2 斐波那契数列')

# 方法3:迭代器实现
def fab(n):
	a,b = 0,1
	for i in range(n):
		yield b
		a,b = b,a+b
gen = fab(4)
print(list(gen))  #[1, 1, 2, 3]
print('--------------------4-3 斐波那契数列')

# 方法4:尾递归递归  (通过方法2改写)
# 规律: 1 1 2 3 5 8 13...
def fab(n,a=0,b=1):
	if n == 1:  #1 递归终止条件
		return b  #2 返回参数3
	else:
		return fab(n-1,b,a+b) #3 return 函数调自己(参数递减的规律  第一个参数-1)    a,b = b,a+b 替换规律也在
n1 = 4
res = fab(n1)
print(res) #3
print('斐波那契数列中第{:d}个数是{:d}'.format(n1,res))
#斐波那契数列中第4个数是3
print('--------------------4-4 斐波那契数列')

#day13 课堂练习
# ### 1.使用递归实现任意数n的阶乘 
#方法1 普通实现
def func(n):
	total = 1
	for i in range(1,n+1):
		total *= i
	return total
n1 = 4
res = func(n1)
print(res) #24
print('{:d}的阶乘是{:d}'.format(n1,res))
#4的阶乘是24
print('--------------------1-1 阶乘')

#方法2 普通实现
def func(n):
	total = 1
	for i in range(n,1,-1):
		total *= i
	return total
n1 = 4
res = func(n1)
print(res) #24
print('{:d}的阶乘是{:d}'.format(n1,res))
#4的阶乘是24
print('--------------------1-2 阶乘')

#方法3 普通递归
# 规律:4!=4*3!  3!=3*2!
def func(n):
	if n == 1:     #1 递归的结束条件
		return n   #2 返回参数1(唯一)
	else:
		return func(n-1)*n  #3 return 函数调自己(参数递减的规律  第一个参数-1)  
n1 = 4
res = func(n1)
print(res) #24
print('{:d}的阶乘是{:d}'.format(n1,res))
#4的阶乘是24
print('--------------------1-3 阶乘')

# ### 2. 使用尾递归来实现任意数的阶乘
# 规律:4!=4*3!  3!=3*2!
# 方法1  尾递归
def func(n,endvar=1):
	if n == 1:   #1 递归终止条件
		return endvar  #2 返回参数2
	else:
		return func(n-1,endvar*n)  # 3 return 函数调自己(参数递减的规律  第一个参数-1)  endvar*n 规律:4!=4*3! 累乘
n1 = 4
res = func(n1)
print(res) #24
print('{:d}的阶乘是{:d}'.format(n1,res))
#4的阶乘是24
print('--------------------2-1 阶乘')

# 方法2  优化 嵌套函数 [把尾递归需要的参数值隐藏起来,避免篡改.]
def outer(n):
	def func(n,endvar=1):
		if n == 1:
			return endvar
		else:
			return func(n-1,endvar*n)
	return func(n,1)  #不是闭包
res = outer(4)
print(res)  #24
print('--------------------2-2 阶乘')

# ### 3.使用递归来完成斐波那契数列
# 规律: 1 1 2 3 5 8 13...
# 方法1:普通递归
def fab(n):
	if n in (1,2):  #1 递归的结束条件
		return n     #2 返回参数(唯一)
	else:
		return fab(n-1) + fab(n-2)  # 3 return 函数调自己(参数递减的规律)  
n1 = 4
res = fab(n1)
print(res) #5
print('斐波那契数列中第{:d}个数是{:d}'.format(n1,res))
#斐波那契数列中第4个数是5
print('--------------------3 斐波那契数列')

#day14 课后作业
# 5 计算文件夹的大小
# 思路:
# 1 拼接文件夹的绝对路径  os.getcwd  os.path.join 或os.path.abspath
# 2 查看文件夹的内容  os.listdir
# 3 拼接内容的绝对路径 os.path.join 或os.path.abspath
# 4 遍历内容,判断是否是文件夹 os.path.isdir
# 5 如果是文件夹,递归,参数是3
# 6 如果是文件,os.path.getsize累加  os.path.isfile

# 思路:
# 1 拼接文件夹的绝对路径  os.getcwd  os.path.join 或os.path.abspath
import os
path1 = os.path.abspath('001')
print(path1)
#/mnt/hgfs/ubuntu_gx/python32/day13 递归 ubuntu环境/03 课后作业/001

# 2 查看文件夹的内容  os.listdir
def getfilesize(path1):
	content = os.listdir(path1)
	print(content)  #['002', 'day13作业1.py', 'day13作业2.py']

	# 3 拼接内容的绝对路径 os.path.join 或os.path.abspath
	size = 0  #位置在for外面
	for i in content:	
		path2 = os.path.join(path1,i)
		# print(path2)
		# /mnt/hgfs/ubuntu_gx/python32/day13 递归 ubuntu环境/03 课后作业/001/002
	# /mnt/hgfs/ubuntu_gx/python32/day13 递归 ubuntu环境/03 课后作业/001/day13作业1.py
	# /mnt/hgfs/ubuntu_gx/python32/day13 递归 ubuntu环境/03 课后作业/001/day13作业2.py
		if os.path.isdir(path2):
			size += getfilesize(path2)  #关键点
		elif os.path.isfile(path2):
			size += os.path.getsize(path2)
	# print(size)	
	return size
res = getfilesize(path1)
print(res)  #21576

# 4 遍历内容,判断是否是文件夹
# 5 如果是文件夹,递归,参数是3
# 6 如果是文件,os.path.getsize累加

































































