''''''
'''

# ### 定义函数
# 1.定义函数:接收任意个参数,打印其中的最小值
# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
# 3.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等)
# 将容器中的每个元素依次添加到新的列表中返回
	#例:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
# 4.写函数，用户传入要修改的文件名，与要修改的内容，执行函数，修改操作
# 5.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，返回处理后的结果.
	#例:参数为:dic = {"k1": "v1v1", "k2": [11,22,33,44]}

# 7传入多个容器类型数据,计算所有元素的个数

# ### 闭包
#下面代码成立么?如果不成立为什么报错?怎么解决?
#1
# a = 2
# def wrapper():
#	print(a)
# wrapper()

#2
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()

#3
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()

#4
# def wrapper():
#      a = 1
#      def inner():
#          print(a)
#      inner()
# wrapper()

#5
# def wrapper():
#      a = 1
#      def inner():
#          a += 1
#          print(a)
#      inner()
# wrapper()

#6
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()
'''

# ### 定义函数
# 1.定义函数:接收任意个参数,打印其中的最小值
def func(*args):
	print(args)  #(1, 3, 54, 66)
	listvar = list(args)
	listvar.sort()
	print(listvar[0])
	return listvar[0]
tuplevar= (1,3,54,66)
func(*tuplevar)
print('-----------------------1')

# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
def func(num):

	# for i in range(1,n+1):
	# 	n *= i
	# print(n)
	factorial = 1
	for i in range(1, num + 1):
		factorial *=  i
	print("%d 的阶乘为 %d" % (num, factorial))

func(3)
print('-----------------------2')



# 3.写函数,传入函数中多个实参(均为可迭代对象如字符串,列表,元祖,集合等)
# 将容器中的每个元素依次添加到新的列表中返回
	#例:传入函数两个参数[1,2,3] (22,33)最终args为(1,2,3,22,33)
def func(*args):
	li = []
	for i in args:
		for j in i:
			li.append(j)
	print(li)
	return li

strvar = 'a'
tuplevar = (1,3)
listvar = [1,3]
dictvar = {'a':1,'b':2}
setvar = {1,3,66,6}

func(strvar,tuplevar,listvar,dictvar,setvar)
print('-----------------------3')

# 4.写函数，用户传入要修改的文件名，与要修改的内容，执行函数，修改操作
def func(filename,content):
	with open(filename,mode='r+',encoding='utf-8') as fp:
		listvar = fp.readlines()
		listvar.insert(-1,content)
		fp.seek(0)
		fp.writelines(listvar)

filename1 = 'a.txt'
content1= '年薪百万\n'  #给倒数第二行插入一行 '年薪百万\n'
func(filename1,content1)
print('-----------------------4')

# 5.写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def func(args):
	n1 = 0
	n2 = 0
	n3 = 0
	n4 = 0
	for i in args:
		if i.isdecimal():
			n1 += 1
		elif i.isalpha():
			n2 += 1
		elif i.isspace():
			n3 += 1
		else:
			n4 += 1
	print('数字的个数是{:d}'.format(n1))
	print('字母的个数是{:d}'.format(n2))
	print('空格的个数是{:d}'.format(n3))
	print('其他的个数是{:d}'.format(n4))

strvar = '1234xajv  &*7'
func(strvar)
print('-----------------------5')

# 6.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，返回处理后的结果.
	#例:参数为:dic = {"k1": "v1v1", "k2": [11,22,33,44]}
def func(args):
	for k,v in args.items():
		print(k,v)
		if len(v) > 2:
			args[k] = v[:2]
	print(args)
	return  args

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
res = func(dic)
print(res)
print('-----------------------6')

# 7传入多个容器类型数据,计算所有元素的个数
def func(*args):
	total = 0
	for i in args:
		total += len(i)
	print(total)  #5

strvar = 'a'
tuplevar = (1,3)
listvar = [1,3]
dictvar = {'a':1,'b':2}
setvar = {1,3,66,6}

func(strvar,tuplevar,listvar,dictvar,setvar)
print('-----------------------7')















