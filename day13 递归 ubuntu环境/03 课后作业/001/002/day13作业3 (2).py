# (选做)
# 1.可滑动的序列 自定义一个函数 根据参数n的值 , 变成对应个元素的容器 （zip）
# """
# listvar = [1,2,3,4,5,6,7,8,9]
# n = 2
# listvar = [[1,2],[3,4],[5,6],[7,8]]
# n = 3
# listvar = [[1,2,3],[4,5,6],[7,8,9]]
# n = 4
# listvar = [[1,2,3,4],[5,6,7,8]]
# """

# 找规律
# n=2
# lst1 = [1,3,5,7,9]  listvar[0::2]
# lst2 = [2,4,6,8]    listvar[1::2]

# n=3
# lst1 = [1,4,7]    listvar[0::3]
# lst2 = [2,5,8]    listvar[1::3]
# lst3 = [3,6,9]	  listvar[2::3]

# n=4
# lst1 = [1,5,9]		listvar[0::4]
# lst2 = [2,6]		listvar[1::4]
# lst3 = [3,7]		listvar[2::4]
# lst4 = [4,8]		listvar[3::4]

listvar = [1,2,3,4,5,6,7,8,9]
n = 4
lst = [listvar[i::n] for i in range(n)]  #规律 关键点1
print(lst)  #[[1, 3, 5, 7, 9], [2, 4, 6, 8]]
# #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# [[1, 5, 9], [2, 6], [3, 7], [4, 8]]

it = zip(*lst)  # 一个星* 在实参处,是解包  知识点
# print(list(it))  #[(1, 2, 3, 4), (5, 6, 7, 8)]

#将列表的元素-元组变成list  map
# it = map(list,list(it))
it = map(list,it)  #参数2可以直接用迭代器
print(list(it))  #[[1, 2, 3, 4], [5, 6, 7, 8]]

# 整合成函数
def func(n):
	return list(map(list,zip(*[listvar[i::n] for i in range(n)])))
print(func(3))  #[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 转成匿名函数
func = lambda n : list(map(list,zip(*[listvar[i::n] for i in range(n)])))
print(func(2))  #[[1, 2], [3, 4], [5, 6], [7, 8]]
print('----------------------------1')


# 2.青蛙跳台阶  (递归实现)
# '''
# 一只青蛙要跳上n层高的台阶
# 一次能跳一级,也可以跳两级
# 请问这只青蛙有多少种跳上这个n层高台阶的方法?
def fog(n):
	if n in (1,2):  #递归的结束条件
		return n
	else:
		return fog(n-1) + fog(n-2)
print(fog(4)) #5
print('----------------------------2')

# 递归的小结:
# 1 找到规律
# 2 递归的固定格式

# 非尾递归的格式
def fog(n):
	if n in (1,2):  #1 递归的结束条件
		return n    #2 返回参数(唯一)
	else:
		return fog(n-1) + fog(n-2)  # 3 return 函数调自己(参数递减的规律)  
print(fog(4)) #5


# 3.递归反转字符串 "将14235 反转成53241" (递归实现)
# 思路1
# 尾递归
# 14235
# 1.每次把最后一位,拿出来,追加到列表
# 2.递归终止条件
  # len(strvar)=1  返回列表
# 3.递减的是字符串的长度,切片  len(strvar-)-1
# 4.参数1是len(strvar),参数2是列表

# 1.每次把最后一位(切片  len(strvar)-1),拿出来,追加到列表
strvar = '14235'

def reverse_str(len,lst):  #4参数1是字符串的长度len(strvar),参数2是列表(初始是空列表)
	if len == 0:  #1递归终止条件  字符串长度是0  返回列表(最后结果)
		return lst
	else:
		lst.append(strvar[len-1]) #2每次把最后一位(切片  len(strvar)-1),拿出来,追加到列表
		# lst.append(strvar[4])  #'5'
		# lst.append(strvar[3])  #'3'
		# lst.append(strvar[2])  #'2'
		# lst.append(strvar[1])  #'4'
		# lst.append(strvar[1])  #'1'
		return reverse_str(len-1,lst)   #字符串的长度每次减1
		# reverse_str(len-1,lst)   #报错
		#3递归调用的时候,递减的是字符串的长度
	
len1 = len(strvar)  
lst1= []

lst = reverse_str(len1,lst1)  #参数1是字符串的长度len(strvar),参数2是列表(初始是空列表)
print(lst)  #['5', '3', '2', '4', '1']
res = ''.join(lst)
print(res)  #53241
print('----------------------------4-1')

# 2.递归终止条件
  # 字符串长度是0  返回列表
# 3.递归调用的时候,递减的是字符串的长度
# 4.参数1是字符串的长度len(strvar),参数2是列表(初始是空列表)


# 思路1-2
# 1 规律:每次把字符串的最后一位(切片  strvar[len(stravar)-1]),拿出来,添加到空列表
# 2 递归终止条件:
	# 字符串的长度是0的时候,返回列表(最后结果)--return
# 3 递归调用:
	# 字符串的长度每次减1
# 4 外函数形参
	  # 参数1是字符串的长度
	  # 参数2是列表
  # 内函数形参(递归调用处)  return内函数
	  # 参数1是字符串的长度-1
	  # 参数2是列表
# 5 外函数实参
	# 参数1是原字符串的长度
	# 参数2是空列表
strvar = '14235'
def reverse_str(len,lst):
	if len == 0:
		return lst
	else:
		lst.append(strvar[len-1])
				# lst.append(strvar[4])  #'5'
		# lst.append(strvar[3])  #'3'
		# lst.append(strvar[2])  #'2'
		# lst.append(strvar[1])  #'4'
		# lst.append(strvar[1])  #'1'
		return reverse_str(len-1,lst)
len1 = len(strvar)
lst1 = []
lst = reverse_str(len1,lst1)
print(lst)  #['5', '3', '2', '4', '1']
strvar_reverse = ''.join(lst)
print(strvar_reverse)  #53241
print('----------------------------4-2')	

#思路2  非尾递归
# 1 规律:每次把字符串的第一位取出来,放在字符串的最后面,拼成新的字符串   strvar = strvar[1:] + strvar[0]
# 2 递归终止条件:
	# 字符串的长度是1的时候,返回 新的字符串(最后结果)--return
# 3 递归调用:
	# 字符串的长度每次减1
# 4 外函数形参
	  # 参数1是字符串的长度
	  # 参数2是列表
  # 内函数形参(递归调用处)  return内函数
	  # 参数1是字符串的长度-1
	  # 参数2是列表
# 5 外函数实参
	# 参数1是原字符串的长度
	# 参数2是空列表
	
strvar = '14235'
def func(strvar):
	if len(strvar) == 1:
		return strvar
	else:
		return func(strvar[1:]) + strvar[0]
res = func(strvar)
print(res)
		
#去-递
# func('14235')  return func('4235') + '1'		 '53241'回5
# func('4235')  return func('235') + '4'		 '5324'回4
# func('235')  return func('35') + '2'			 '532'回3
# func('35')  return func('5') + '3'             '53'回2
# func('5')  条件 len(strvar) == 1: return '5' #回1

#回-归
print('----------------------------4-3')

#非尾递归2
strvar = '14235'
def func(strvar):
	if len(strvar) == 1:
		return strvar
	else:
		return func(strvar[1:]) + strvar[0]  #strvar[1:]本身有递减的意思
res = func(strvar)
print(res)  #53241
print('----------------------------4-4')

#尾递归2
#规律:每次把字符串的最后一位strvar[len-1]拿出来,放到列表中
def func(len,lst):
	if len == 0:
		return lst  #最后要的
	else:
		lst.append(strvar[len-1])
		return func(len-1,lst)
strvar = '14235'
len1 = len(strvar)	
lst1 = []
lst = func(len1,lst1)
print(lst)  #['5', '3', '2', '4', '1']

res = ''.join(lst)
print(res)  #53241
print('----------------------------4-5')

#非尾递归3
#规律:每次把字符串的第一位取出来,放在字符串的最后面
strvar = '14235'
def func(strvar):
	if len(strvar) == 1:
		return strvar
	else:
		return func(strvar[1:]) + strvar[0]
res = func(strvar)
print(res) #53241
print('----------------------------4-6')

#尾递归3
#规律:每次把字符串的最后一位取出来,放到列表中
strvar = '14235'
def func(len,lst):
	if len == 0:
		return lst
	else:
		lst.append(strvar[len-1])
		return func(len-1,lst)
len1 = len(strvar)
lst1 = []
lst = func(len1,lst1)
print(lst) #['5', '3', '2', '4', '1']
res = ''.join(lst)
print(res)  #53241
print('----------------------------4-7')

#非尾递归3-2
#规律:每次把最后一位拿出来,放到字符串的最前面
strvar = '14235'
def func(strvar):
	if len(strvar) == 1:
		return strvar
	else:
		# return func(strvar[:-1]) + strvar[-1]  #14235
		return strvar[-1] + func(strvar[:-1])
res = func(strvar)
print(res)  #53241

# 去
# func('14235')   return '5' + func('1423') '53241' 归回
# func('1423')   return '3' + func('142')	'3241'
# func('142')   return '2' + func('14')		'241'
# func('14')   return '4' + func('1')   	'41'
# func('1')   满足 len(strvar) == 1   return '1'
print('----------------------------4-8')

# 递归的小结:
# 1 找到规律
# 2 递归的固定格式
# 尾递归的格式
# strvar = '14235'
# def func(len,lst):
	# if len == 0:  #1 递归终止条件
		# return lst  # 2 返回参数2
	# else:
		# lst.append(strvar[len-1])  # 3  递减的规律  长度递减1
		# return func(len-1,lst)     # 4 return 函数调自己(参数递减的规律)  长度递减1
		
# 非尾递归的格式
# strvar = '14235'
# def func(strvar):
	# if len(strvar) == 1:   #1 递归终止条件
		# return strvar      # 2 返回参数
	# else:
		# return func(strvar[1:]) + strvar[0]  # 3 return 函数调自己(参数递减的规律)  长度递减1(表示形式 strvar[1:])
# res = func(strvar)
# print(res)


# 4.斐波那契数列用尾递归实现
# 普通实现 while
def fab(n):
	a,b = 0,1
	i = 0
	while i<n:
		print(b)
		a,b = b,a+b
		i += 1
fab(4)
print('----------------------------5-1')

# 生成器 while
def fab(n):
	a,b = 0,1
	i = 0
	while i<n:
		# print(b)
		yield b
		a,b = b,a+b
		i += 1
gen = fab(4)
print(list(gen))  #[1, 1, 2, 3]
print('----------------------------5-2')

# 生成器 for
def fab(n):  #n表示数列的长度
	a,b = 0,1
	for i in range(n):
		# print(b)
		yield b
		a,b = b,a+b
	
gen = fab(4)
print(list(gen))  #[1, 1, 2, 3]
print('----------------------------5-3')

# 尾递归
def func(n,a=0,b=1):  #n表示要取数列的第几个数
	if n == 1:
		return b
	else:
		return func(n-1,b,a+b)
res = func(5)
print(res)  #5
print('----------------------------5-4')

# 递归的小结:
# 1 找到规律
# 2 递归的固定格式
# 尾递归的格式
def func(n,a=0,b=1):  #n表示要取数列的第几个数
	if n == 1:  #1 递归终止的条件
		return b  #2 返回参数3
	else:
		return func(n-1,b,a+b) #3  return 函数调自己(参数递减的规律) 
res = func(5)
print(res)  #5





































