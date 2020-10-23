# part1
# 1.集合的值和字典的键有什么数据类型上的要求
# 必须是不可变类型  Numbers(int float bool complex) tuple str
# 可变类型 list dict set

# 2.对于python3.6来说,变量的缓存机制
# Numbers
	# int    -5~正无穷    值相同  id相同
	# float  非负浮点数	值相同  id相同 
	# bool				值相同  id相同
	# complex 			值相同  id不同(正虚数除外  5j)
# 容器
	# str					值相同  id相同
	# tuple				值相同  id不同(空元组除外)
	# list				值相同  id不同
	# dict				值相同  id不同
	# set					值相同  id不同

# 3.bool类型为假的十种情况
# Numbers
	# int    		0
	# float  		0.0
	# bool		False	
	# complex     0j	
# 容器
	# str			""		
	# tuple		()		
	# list	    []	
	# dict		{}	
	# set			set()
# None

# 4.Number类型的自动转换原则
# 低精度自动向高精度转换
# bool==>int==>float==>complex

# 5.容器类型强转特征
# 容器
	# str	
		# 可以强转任意类型,两边加上引号
	# tuple	
		# str		把字符串的每个字符单独拿出来,作为新tuple的元素
		# dict 	tuple的元素是dict的键
		# set/list 把set list两端换成()
	# list
		# str		把字符串的每个字符单独拿出来,作为新list的元素
		# dict 	list的元素是dict的键
		# set/tuple 把set tuple两端换成[]
	# dict	
		# 1 必须是等长二级容器 且
		# 2 二级容器的长度是2
		
		# 外层是列表或者元组.里层是列表或者元组
		# 外层是集合.里层是元组
	# set	
		# str		把字符串的每个字符单独拿出来,作为新set的元素
		# dict 	set的元素是dict的键
		# tuple/list 把tuple list两端换成{}

# 6.什么样的类型可以强转成字典   nok
		# dict	
		# 1 必须是等长二级容器 且
		# 2 二级容器的长度是2
		
		# 外层是列表或者元组.里层是列表或者元组
		# 外层是集合.里层是元组

# 7.什么情况下会出现短路
     # False and      True or

# 8.is和==有什么区别
# is 身份运算符  看2个变量是否是同一个内存地址  id()
# == 比较运算符  比较值

# 算数-位-比较-身份-成员-逻辑-赋值
# +    <<  ==   is   in   and  =

# 9.逻辑运算符优先级排序
# () > not > and >or

# 10.<< >> 运算规律
# << 左移 乘以2的n次方 n是左移位数
# >> 右移 除以2的n次方 n是右移位数


# part2
# 1.打印一行十个小星星
for i in range(10):
	print('*',end='')
print('---------------1')

# 2.通过打印变量,直接输出一行十个小星星
strvar = ''
for i in range(10):
	strvar += '*'
print(strvar)
print('---------------2')

# 3.打印一行十个小星星,奇数个打印★,偶数个打印☆
for i in range(10):
	if i % 2 == 0:
		print('☆',end='')
	else:
		print('★',end='')
print('---------------3')

# 4.一个循环打印十行十列小星星
for i in range(100): #总数
	#星星
	print('*',end='')
	
	#换行
	if i % 10 == 9:
		print()
print('---------------4')

# 5.一个循环打印十行十列隔列变色小星星
for i in range(100):
	#星星
	if i % 2 == 0:
		print('☆',end='')
	else:
		print('★',end='')
	
	#换行
	if i % 10 == 9:
		print()
print('---------------5')

# 6.一个循环打印十行十列隔行变色小星星
for i in range(100):
	#星星
	# if i % 2 == 0:  #隔列换色
	if i // 10 % 2 == 0:  #隔行换色
		print('☆',end='')
	else:
		print('★',end='')
	
	#换行
	if i % 10 == 9:
		print()
print('---------------6')

# 7.两个循环十行十列小星星
for i in range(10): #行
	for j in range(10): #列
	#星星
		print('*',end='')
	#换行
	print()
print('---------------7')

# 8.两个循环十行十列隔列/隔行换色小星星
for i in range(10):
	for j in range(10):
		#星星
		if j % 2 == 0:  #隔列换色
			print('☆',end='')
		else:
			print('★',end='')
	#换行
	print()
print('---------------8-1')

for i in range(10):
	for j in range(10):
	#星星
		# if j % 2 == 0:  #隔列换色
		if i % 2 == 0:   #隔行换色  内层动的慢,外层动得快
			print('☆',end='')
		else:
			print('★',end='')
	#换行
	print()
print('---------------8-2')

# 9.99乘法表   一二三四象限
# 第一象限
for i in range(1,10): #行
	for j in range(1,i+1): #列
	#表达式
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('---------------9-1 ')

# 第四象限
for i in range(9,0,-1): #乘数1
	for j in range(1,i+1): #乘数2
		#表达式
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('---------------9-4 ')

# 第二象限
for i in range(1,10):#行数
	#空格
	for k in range(9-i,0,-1):  #空格数+星星数=9
		print('{}'.format('       '),end='')  #7个空格一组
	
	#表达式
	for j in range(1,i+1):#列
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('---------------9-2 ')

# 第三象限
for i in range(9,0,-1):# 乘数1
	#空格
	for k in range(9-i,0,-1):
		print('{}'.format('       '),end='')
	
	#表达式
	for j in range(1,i+1):  #乘数2
		print('{:d}*{:d}={:2d} '.format(i,j,i*j),end='')
	#换行
	print()
print('---------------9-3 ')		

# 10.吉利数字100~999,找123 321 111
for i in range(100,1000):
	units = int(str(i)[-1])
	tens = int(str(i)[-2])
	hundreds = int(str(i)[-3])
	if tens == units and tens == hundreds:
		print(i)
	elif tens == units + 1 and tens == hundreds - 1:  #优先级  算数>比较>逻辑
		print(i)
	elif tens == units - 1 and tens ==hundreds + 1:
		print(i)
print('---------------10 ')

# 11.公鸡1块钱1只,母鸡3块钱一只,小鸡5毛钱一只,问: 用100块钱买100只鸡,有多少种买法?
for i in range(100):
	for j in range(33):
		for k in range(100):
			if i+j+k == 100 and i+3*j+1/2*k == 100:  #优先级  算数>比较>逻辑
				print('公鸡{},母鸡{},小鸡{}'.format(i,j,k))
print('---------------11 ')

# 12.国际象棋
#单循环1
for i in range(64): #总数
	#格子
	if i // 8 % 2 == 0:
		if i % 2 == 0:
			print('*',end='')
		else:
			print('^',end='')
	else:
		if i % 2 == 0:
			print('^',end='')
		else:
			print('*',end='')
	
	#换行
	if i % 8 == 7:
		print()
print('---------------12-1 ')

#单循环2
for i in range(8): #行
	#格子
	if i % 2 == 0: #偶数行
		print('^*^*^*^*',end='')
	else:#奇数行
		print('*^*^*^*^',end='')
	#换行
	print()
print('---------------12-2 ')		


#双循环1
for i in range(8): #行
	#格子
	if i % 2 == 0: #偶数行
		for j in range(8): #列
			if j % 2 == 0:
				print('*',end='')
			else:
				print('^',end='')
	else:#奇数行
		# print('*^*^*^*^',end='')
		for j in range(8): #列
			if j % 2 == 0:
				print('^',end='')
			else:
				print('*',end='')
	#换行
	print()
print('---------------12-3 ')	

# 13.打印1~100不含有3的数字.  
for i in range(1,101):	
	if '3' not in str(i):
		print(i)
print('---------------13 ')	

# part3
# 1.break 和 continue有什么区别
# break 跳出整个循环,只能跳出一层循环
# continue  跳出当次循环,进入下一次循环   不推荐和while搭配使用

# 2.[1,2,3,(4,5,6,{'a','b'})] 如何遍历
lst = [1,2,3,(4,5,6,{'a','b'})]
for i in lst:
	if isinstance(i,tuple):
		for j in i:
			if isinstance(j,set):
				for k in j:
					print(k)
			else:
				print(j)		
	else:
		print(i)
print('---------------part3 2 ')
# 1
# 2
# 3
# 4
# 5
# 6
# b
# a	

# 3.([1,2],{3,4})如何遍历
tuplevar = ([1,2],{3,4})
for a,b in tuplevar:
	print(a,b)
# 1 2
# 3 4
print('---------------part3 3-1 ')

for i in tuplevar:
	for j in i:
		print(j)
# 1
# 2
# 3
# 4
print('---------------part3 3-2 ')

# 4密码111,输错三次循环终止,每次打印剩余输入机会.
def login():
	times = 1
	for i in range(3):  #3控制输入机会
		password = input('请输入密码:')
		if password.isdecimal():
			password = int(password)

			if password == 111:
				print('成功')
				break
			else:
				print('你还有{:d}次输入机会'.format(2-i))
# login()
print('---------------part3 4')

# 5求结果
	# 87 % 7    12 3  余数的符号和除数一致
	# -87 % 7  -12 4
	# 87 % 7    12 3
	# 81 // 7   11 4
	# 81.0 // 7 11.0 4.0
	# ~18  按位非  -(n+1)  -19
# 原码: 0 0000 0001 0010	 #正数 符号位 0  三码一致
# 反码: 0 0000 0001 0010
# 补码: 0 0000 0001 0010
#
# 按位非  1和0对调  符号位也对调
# 补码1: 0 0000 0001 0010
# 补码2: 1 1111 1110 1101   #符号位是1  负数 三码不一致
#
# 反码:  1 0000 0001 0010   #取反,符号位不变
# 原码:  1 0000 0001 0011   #-19
	
	# ~-18  按位非  -(n+1)  -17  对补码按位非
# 原码: 1 0000 0001 0010	 #负数 符号位 1  三码不一致
# 反码: 1 1111 1110 1101
# 补码: 1 1111 1110 1110
#
# 按位非  1和0对调  符号位也对调
# 补码1: 1 1111 1110 1110
# 补码2: 0 0000 0001 0001   #符号位是0  正数 三码一致
#
# 反码:0 0000 0001 0001
# 原码:0 0000 0001 0001   #17
	
	# 40 >> 2 ** 2  #优先级 ** > 位运算
# 40 >> 4  #右移4位,除以2的4次幂
# 40/2**4=5

# 10 1000	  #40
# 00 0101  #5
	
	# 1 > 2 and 3<=4 or not 0
# 1 > 2 and 3<=4 or not 0
# False and True or True
# False or True
# True	

# part4
# 字符串函数
# 把字符串的旧字符换成新字符
strvar = 'abc'
res = strvar.replace('a','d')
print(res)

# 判断字符串是否由空白符组成  nok
str1 = '  \t\n '
res = str1.isspace()
print(res)  #True

# 将所有字母变成小写 
strvar = 'abDADc'
res = strvar.lower()
print(res)  #abdadc

# 字符串首字母大写 
strvar = 'abDADc'
print(strvar.capitalize())  #Abdadc
print('-------------------------4')

# 按某字符将列表拼接成字符串(容器类型都可)
# lst = [1,3,4]   #TypeError: sequence item 0: expected str instance, int found  #不能拼接int
lst = ['1','3']
strvar = '_'.join(lst)
print(strvar)  #1_3

# 默认去掉首尾两边的空白符
str1 = '  addd \n'
print(str1.strip())  #addd

# 判断是否以某个字符或字符串结尾 
strvar = 'abDADc'
print(strvar.endswith('c')) #True

# 统计字符串中某个元素的数量 
strvar = 'abDADc'
print(strvar.count('D')) #2
print('-------------------------8')

# 计算字符串的长度 
strvar = 'abDADc'
print(len(strvar))  #6

# 判断是否以某个字符或字符串为开头 
strvar = 'abDADc'
print(strvar.startswith('ab'))  #True

# 查找某个字符串第一次出现的索引位置 
strvar = 'abDADc'
print(strvar.find('D')) #2
print(strvar.index('D')) #2

# 检测字符串是否以数字组成  必须是纯数字
strvar = '1234'
print(strvar.isdecimal()) #True  #应用 input
print('-------------------------12')

# 填充字符串,原字符居中 (默认填充空格)
strvar = 'abDADc'
# print(strvar.center('*',12))
# TypeError: 'str' object cannot be interpreted as an integer

print(strvar.center(12,'*'))  
#***abDADc***

# 将所有字母变成大写
strvar = 'abDADc'
print(strvar.upper())
#ABDADC

# 大小写互换 
strvar = 'abDADc'
print(strvar.swapcase())
#ABdadC

# 按某字符将字符串分割成列表(默认字符是空格)
strvar = 'abDADc'
lst = strvar.split('D')
print(lst) #['ab', 'A', 'c']

# 每个单词的首字母大写 
strvar = 'abDADc ja kss'
print(strvar.title()) #Abdadc Ja Kss
print('-------------------------17')

# part5
# 列表函数
# 列表添加方法,说明用法  append insert extend
lst = ['1','3']
lst.append(4)
print(lst)  #['1', '3', 4]

lst = ['1','3']
lst.insert(1,45)
print(lst)  #['1', 45, '3']

lst = ['1','3']
lst.extend('ac')
print(lst)  #['1', '3', 'a', 'c']
print('-----------------------1 append insert extend ')

# 列表删除方法,说明用法  pop remove clear
lst = ['1','3']
res = lst.pop()
print(res) #3
print(lst)  #['1']

lst = ['1','3']
res = lst.pop(0)
print(res)  #'1'
print(lst)  #['3']

lst = ['1','3']
lst.remove('3')
print(lst)  #['1']

lst = ['1','3']
lst.clear()
print(lst)  #[]
print('-----------------------2 pop remove clear ')

# 如何获取一个值的索引
lst = ['1','3']
print(lst.index('3'))  #1
# print(lst.find('3'))
# AttributeError: 'list' object has no attribute 'find'

# 如何排序,如何倒序
lst = ['a','c','b']
lst.sort()
print(lst)  #['a', 'b', 'c']

lst = ['a','c','b']
lst.sort(reverse = True)
print(lst)  #['c', 'b', 'a']

lst = ['a','c','b']
lst_new = sorted(lst)
print(lst_new) #['a', 'b', 'c']

lst = ['a','c','b']
lst_new = sorted(lst,reverse=True)
print(lst_new)  #['c', 'b', 'a']
print('-----------------------3 sort sorted ')

# 统计元素在列表中的个数
lst = ['a','c','b','b']
print(lst.count('b'))  #2

lst = ['a','c','b','b']
dic = {}
for i in lst:
	if i not in dic:
		dic[i] = 1
	else:
		dic[i] += 1
print(dic)  #{'a': 1, 'c': 1, 'b': 2}

lst = ['a','c','b','b']
from collections import Counter
print(Counter(lst))  #Counter({'b': 2, 'a': 1, 'c': 1})
print('-----------------------4 count ')

# 翻转列表
lst = ['a','c','b','b']
lst.reverse()
print(lst)  #['b', 'b', 'c', 'a']

lst = ['a','c','b','b']
print(lst[::-1]) #['b', 'b', 'c', 'a']

#方法3 递归 nok

# 什么是深浅拷贝
# 赋值 =
a = 1
b = a
a = 2
print(b) #1 因为int是值类型,新开辟了空间  完全独立

lst1 = ['a','c','b','b']
lst2 = lst1
lst1.append('3')
print(lst2) #['a', 'c', 'b', 'b', '3']
# 因为list是引用类型,没有新开辟空间,一变都变
print('-----------------------5 赋值= 值类型和引用类型 ')

# 浅拷贝
import copy
lst1 = ['a','c','b','b']
lst2 = copy.copy(lst1)
lst1.append(1)
print(lst1)  #['a', 'c', 'b', 'b', 1]
print(lst2)  #['a','c','b','b']
# 浅拷贝,只拷贝容器的第一层,第一层独立

lst1 = ['a','c','b','b',[1,3]]
lst2 = copy.copy(lst1)
lst1[-1].append(2)
print(lst1)  #['a', 'c', 'b', 'b', [1, 3, 2]]
print(lst2)  #['a', 'c', 'b', 'b', [1, 3, 2]]
# 浅拷贝,只拷贝容器的第一层  第二层及其以上,一改都改

# 深拷贝
lst1 = ['a','c','b','b',[1,3]]
lst2 = copy.deepcopy(lst1)
lst1[-1].append(2)
print(lst1)  #['a', 'c', 'b', 'b', [1, 3, 2]]
print(lst2)# ['a','c','b','b',[1,3]]
# 深拷贝,会拷贝容器的每一层,即每一层都完全独立

















