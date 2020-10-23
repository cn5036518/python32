# ''''''
# '''

### 字符串相关练习
# 1.有变量name = "aleX leNb" 完成如下操作：

# 移除 name 变量对应的值两边的空格,并输出处理结果
name = "  aleX leNb"
res = name.strip()
print(res)  #aleX leNb


# 1)移除name变量左边的"al"并输出处理结果
name = "aleX leNb"
res = name.lstrip('al')
print(res)  #eX leNb

# 2)移除name变量右面的"Nb",并输出处理结果
name = "aleX leNb"
res = name.rstrip('Nb')
print(res)  #aleX le

# 3)移除name变量开头的a与最后的"b",并输出处理结果
name = "aleX leNb"
res = name.strip('ab')
print(res) #leX leN
print('-------------------3')

# 4)判断 name 变量是否以 "al" 开头,并输出结果
name = "aleX leNb"
res = name.startswith('al')
print(res)  #True

# 5)判断name变量是否以"Nb"结尾,并输出结果
name = "aleX leNb"
res = name.endswith('Nb')
print(res)  #True

# 6)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
name = "aleX leNb"
res = name.replace('l','p')
print(res)  #apeX peNb

import re
pattern = re.compile(r'l')
res = pattern.sub('p',name)
print(res) #apeX peNb
print('-------------------6')

# 7)将name变量对应的值中的第一个"l"替换成"p",并输出结果
name = "aleX leNb"
res = name.replace('l','p',1)  #新产生一个字符串,原字符串不变
print(res)  #apeX leNb

import re
pattern = re.compile(r'l')
res = pattern.sub('p',name,1)
print(res) #apeX leNb

# 8)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
name = "aleX leNb"
lst = name.split('l')
print(lst)  #['a', 'eX ', 'eNb']

import re
pattern = re.compile(r'l')
lst = pattern.split(name)
print(lst)  #['a', 'eX ', 'eNb']
print('-------------------8')

# 9)将name变量对应的值根据第一个"l"分割,并输出结果。
name = "aleX leNb"
lst = name.split('l',1)
print(lst)  #['a', 'eX leNb']

import re
pattern = re.compile(r'l')
lst = pattern.split(name,1)
print(lst)  #['a', 'eX leNb']
print('-------------------9')

# 10)将 name 变量对应的值变大写,并输出结果
name = "aleX leNb"
res = name.upper()
print(res) #ALEX LENB

# 11)将 name 变量对应的值变小写,并输出结果
name = "aleX leNb"
res = name.lower()
print(res) #alex lenb

# 12)将name变量对应的值首字母"a"大写,并输出结果
name = "aleX leNb"
res = name.capitalize()
print(res)  #Alex lenb
print('-------------------12')

# 13)判断name变量对应的值字母"l"出现几次，并输出结果
name = "aleX leNb"
res = name.count('l')
print(res)

# 计算字符串中每个字符出现的个数
dic = {}
for i in name:
	if i not in dic:
		dic[i] = 1
	else:
		dic[i] += 1
print(dic)
#{'a': 1, 'l': 2, 'e': 2, 'X': 1, ' ': 1, 'N': 1, 'b': 1}

from collections import Counter
print(Counter(name))
#Counter({'l': 2, 'e': 2, 'a': 1, 'X': 1, ' ': 1, 'N': 1, 'b': 1})

# 14)如果判断name变量对应的值前四位"l"出现几次,并输出结果
name = "aleX leNb"
res = name.count('l',0,4)  #1
print(res)
print('-------------------14')

# 15)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
name = "aleX leNb"
res = name.index('N')
print(res)  #7

# 16)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
name = "aleX leNb"
res = name.find('N')
print(res) #7

# 17)从name变量对应的值中找到"X le"对应的索引,并输出结果
name = "aleX leNb"
res = name.find('X le')
print(res)  #3
print('-------------------17')

# 18)请输出 name 变量对应的值的第 2 个字符?
name = "aleX leNb"
res = name[1]
print(res)  #l

# 19)请输出 name 变量对应的值的前 3 个字符?
name = "aleX leNb"
print(name[:3])  #ale

# 20)请输出 name 变量对应的值的后 2 个字符?
name = "aleX leNb"
print(name[-2:])  #Nb

# 21)请输出 name 变量对应的值中 "e" 所在索引位置?
name = "aleX leNb"
res = name.find('e')
print(res)  #2
print('-------------------21')

# 2.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算
# content = input("请输入内容:")
# a,b = content.split('+')
# res = int(a.strip()) + int(b.strip())
# print(res)

# 3.升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
# content = input("请输入内容:")
# lst = content.split('+')
# total = 0
# for i in lst:
	# total += int(i.strip())
# print(total)

# 4.计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
strvar = 'fhdal234slfh98769fjdla'
total = 0
for i in strvar:
	if i.isdecimal():
		total += 1
print(total) #8

import re
pattern = re.compile(r'\d')
lst = pattern.findall(strvar)
print(lst)  #['2', '3', '4', '9', '8', '7', '6', '9']
print(len(lst)) #8
print('-------------------4')

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”
# content = input('请输入:')
# if ('粉嫩' or '铁锤')  in content:  #优先级 成员 > 逻辑
	# print('存在敏感字符请重新输入')
# else:
	# print('内容合法')

# lst = ['粉嫩','铁锤']
# content = input('请输入:')
# for i in lst:
	# if i in content:  #
		# print('存在敏感字符请重新输入')
		# break
# else:
	# print('内容合法')

# 6.制作趣味模板程序需求：等待用户输入名字、地点、爱好
# 拼装数据打印出：敬爱可亲的xxx，最喜欢在xxx地方xxx
# print('敬爱可亲的{}，最喜欢在{}地方{}'.format('jack','beijing','run'))
print('敬爱可亲的{:s}，最喜欢在{:s}地方{:s}'.format('jack','beijing','run'))


### 列表相关练习
# 1.li = ["alex", "WuSir", "xboy", "oldboy"]
# 1)列表中追加元素"seven",并输出添加后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.append('seven')
print(li) #['alex', 'WuSir', 'xboy', 'oldboy', 'seven']

# 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.insert(0,'Tony')
print(li) #['alex', 'Tony', 'WuSir', 'xboy', 'oldboy']

# 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li[1] = 'kelly'
print(li) #['alex', 'kelly', 'xboy', 'oldboy']
print('--------------------------3')

# 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行
# 代码实现，不允许循环添加。
l2=[1,"a",3,4,"heart"]
l1= []
l1.extend(l2)
print(l1)  #[1, 'a', 3, 4, 'heart']

# 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
li = []
li.extend(s)
print(li) #['q', 'w', 'e', 'r', 't']

# 6)请删除列表中的元素"alex",并输出删除后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.remove('alex')
print(li)  #['WuSir', 'xboy', 'oldboy']

# 7)请删除列表请删除列表中的第2至4个元素，并输出删除元素后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
print(li[0]) #alex
print('--------------------------7')

# 8)删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
res = li.pop(1)
print(res) #"WuSir"
print(li) #['alex', 'xboy', 'oldboy']

# 9)请将列表所有得元素反转，并输出反转后的列表
#方法1  reverse
li = ["alex", "WuSir", "xboy", "oldboy"]
li.reverse()
print(li)  #['oldboy', 'xboy', 'WuSir', 'alex']

#方法2  切片  推荐 简洁
li = ["alex", "WuSir", "xboy", "oldboy"]
print(li[::-1])  #['oldboy', 'xboy', 'WuSir', 'alex']
 
#方法3
# 规律:把列表的最后一个元素拿出来pop,追加到列表append
li = ["alex", "WuSir", "xboy", "oldboy"]
lst = []
for i in range(len(li)):
	res = li.pop()
	lst.append(res)
print(lst) #['oldboy', 'xboy', 'WuSir', 'alex']
print('--------------------------9-3')

#方法4  尾递归
# 规律:把列表的最后一个元素拿出来,放到另外一个列表中
li = ["alex", "WuSir", "xboy", "oldboy"]
def func(len,lst):
	if len == 0:  #1 递归终止条件
		return  lst  #2 返回参数2 尾递归 最后要的值
	else:
		lst.append(li[len-1])  #3  递减的规律  长度递减1  把列表的最后一个元素拿出来,放到列表中
		return func(len-1,lst) # 4 return 函数调自己(参数递减的规律  第一个参数-1)  长度递减1
len1 = len(li)
lst1 = []
res = func(len1,lst1)
print(res)  #['oldboy', 'xboy', 'WuSir', 'alex']
print('--------------------------9-5')

# 10)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
li = ["alex", "WuSir", "xboy", "oldboy"]
res = li.count('alex')
print(res) #1

# 2，写代码，有如下列表，利用切片实现每一个功能
li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
print(li[:3]) #[1, 3, 2]

# 2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
print(li[3:6]) #['a', 4, 'b']

# 3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
print(li[::2]) #[1, 2, 4, 5]
print('--------------------------2-3')

# 4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
print(li[1:-1:2]) #[3, 'a', 'b']

# 5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
print(li[-1:]) #['c']

# 6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
print(li[-3:0:-2]) #['b', 'a', 3]
print('--------------------------2-6')

# 3,写代码，有如下列表，按照要求实现每一个功能。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表lis中的"tt"变成大写。
lis[3][2][1][0] = lis[3][2][1][0].upper()
print(lis)
#[2, 3, 'k', ['qwe', 20, ['k1', ['TT', 3, '1']], 89], 'ab', 'adv']

# 2)将列表中的数字3变成字符串"100"。
lis[3][2][1][1] = '100'
print(lis) #[2, 3, 'k', ['qwe', 20, ['k1', ['TT', '100', '1']], 89], 'ab', 'adv']

# 3)将列表中的字符串"1"变成数字101
lis[3][2][1][-1] = 101
print(lis)
#[2, 3, 'k', ['qwe', 20, ['k1', ['TT', '100', 101]], 89], 'ab', 'adv']
print('--------------------------3')

# 4,li = ["alex", "eric", "rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
li = ["alex", "eric", "rain"]
strvar = '_'.join(li)
print(strvar) #alex_eric_rain
print('--------------------------4')

# 5.利用for循环打印出下面列表的索引。
li = ["alex", "WuSir", "xboy", "oldboy"]
for i in range(len(li)):
	print(i,li[i])
# 0 alex
# 1 WuSir
# 2 xboy
# 3 oldboy
print('--------------------------5')

# 6.利用for循环和range 找出50以内能被3整除的数，并将这些数插入到一个新列表中。
lst = [i for i in range(50) if i % 3 == 0]
print(lst)
#[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
print('--------------------------6')

# 7.利用for循环和range从100~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来
lst = [i for i in range(100,10,-1) if i % 4 == 0]
print(lst) #[100, 96, 92, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12]
print('--------------------------7')

# 8.查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以"c"结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ["xboy ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]

li1 = []
for i in li:
	i = i.strip()
	if (i.startswith('A') or i.startswith('a')) and i.endswith('c'):
		li1.append(i)
print(li1) #['aqc']

# 9.敏感词列表 li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# 将用户输入的内容中的敏感词汇替换成等长度的*（苍老师就替换***），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到新列表中。
li = ["jack", "东京热", "武藤兰", "波多野结衣"]

# content = input('请输入词汇:')
# li1 = []
# li2 = []
# for i in li:
	# if i in content:
		# content2 = content.replace(i,len(i)*'*')
		# li1.append(content2)
		# continue
# else:
	# print('没有敏感词汇')
	# li2.append(content)
# print(li1)
print('--------------------------9')

# 10.li = [1, 3, 4, "alex", [3, 7, “23aa”,8, "xboy"], 5,(‘a’,’b’)]
# 循环打印列表中的每个元素,并转化为小写，遇到列表则再循环打印出它里面的元素。
li = [1, 3, 4, "alex", [3, 7, '23aa',8, "xboy"], 5,('a','b')]
for i in li:
	if isinstance(i,(list,set)):
		for j in i:
			if isinstance(j,str):
				print(j.lower())
			else:
				print(j)
	else:
		if isinstance(i,str):
			print(i.lower())
		else:
			print(i)
# 1
# 3
# 4
# alex
# 3
# 7
# 23aa
# 8
# xboy
# 5
# ('a', 'b')

# 11.tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# a.讲述元组的特性
# b.请问tu变量中的第一个元素 "alex" 是否可被修改？  #不可以
# c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven"  #可以
# d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 "Seven" #不可以

tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
tu[1][2]['k2'].append('Seven')
print(tu)
#('alex', [11, 22, {'k1': 'v1', 'k2': ['age', 'name', 'Seven'], 'k3': (11, 22, 33)}, 44])


# '''























