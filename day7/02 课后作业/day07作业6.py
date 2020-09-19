#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 22:31

# 6.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
listvar = []
for i in range(51):
	if i % 3 == 0:
		listvar.append(i)
print(listvar)  #[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

# 7.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来
listvar = []
for i in range(100,9,-1):
	if i % 4 == 0:
		listvar.append(i)
print(listvar)  #[100, 96, 92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12]


# 8.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
# li = ["xboy ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
li = ["xboy ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
listvar = []
for i in li:
	i = i.strip()
	if (i.startswith('a') or i.startswith('A')) and i.endswith('c'):
		listvar.append(i)
print(listvar)  #['aqc']

# 9.敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到新列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# listvar1 = []
# listvar2 = []
#
# while True:
# 	content = input('请输入姓名:')
# 	if content in li:
# 	    content = len(content) * '*'
# 	    listvar2.append(content)
# 	else:
# 		listvar1.append(content)
# 		break
# print(listvar1)
# print(listvar2)
print('----------------------------------9-1')

# 推荐方法
li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# content = '日本苍老师日本'
# content = '日本日本'

listvar = []
listvar2 = []
sign = True
while sign:
	content = input('请输入内容,输入q退出:')
	if content.lower() == 'q':
		break
	else:
		for i in li:
			if i in content:
				ele = content.replace(i,len(i)*'*')
				listvar.append(ele)
				# sign = False
				break
		else: #缩进不能和if对齐(不然,列表会出现4个相同的元素)
			listvar2.append(content)
print('含有敏感词的内容列表是{}'.format(listvar))
print('不含有敏感词的内容列表是{}'.format(listvar2))

print('----------------------------------9-2')

# 10.li = [1, 3, 4, "alex", [3, 7, “23aa”,8, "xboy"], 5,(‘a’,’b’)]
# 循环打印列表中的每个元素,并转化为小写，遇到列表则再循环打印出它里面的元素。
li = [1, 3, 4, "alex", [3, 7, '23aa',8, "xboy"], 5,('a','b')]

for i in li:
	if isinstance(i,(tuple,list)):
		for j in i:
			if isinstance(j,str):
				print(j.upper())
			else:
				print(j)
	elif isinstance(i,str):
		print(i.upper())
	else:
		print(i)

# 11.tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a.讲述元组的特性  #有序,可获取,不可修改

# b.请问tu变量中的第一个元素 "alex" 是否可被修改？  #不能

# c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
	# 列表   可以修改
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
tu[1][2]['k2'].append('Sever')
print(tu)

# d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"
# 元组,不能


















