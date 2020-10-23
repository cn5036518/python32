#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 9:02

# ''''''
# '''
# 1	使用一组键和默认值创建字典
dic = {}.fromkeys([1,2,3],'a')
print(dic)  #{1: 'a', 2: 'a', 3: 'a'}

dic = {}
dic['name'] = 'jack'
dic['age'] = 18
print(dic)  #{'name': 'jack', 'age': 18}

dic = {'name':'bob','age':19}
print(dic)  #{'name': 'bob', 'age': 19}
print('------------------------1 fromkeys')

# 2	通过键去删除键值对（若没有该键可设置默认值，预防报错),并获取被删除的值
dic = {'name': 'jack', 'age': 18}
res = dic.pop('name1','对不起,没有该键')
print(res)  #对不起,没有该键
print(dic)  #{'name': 'jack', 'age': 18}

dic = {'name': 'jack', 'age': 18}
res = dic.pop('name','对不起,没有该键')
print(res)  #jack
print(dic)  #{'age': 18}
print('------------------------2-1 pop')

# 3	删除最后一个键值对,并获取值
dic = {'name': 'jack', 'age': 18}
res = dic.popitem()
print(res) #('age', 18)
print(dic) #{'name': 'jack'}
print('------------------------2-2 popitem')

# 4	清空字典
dic = {'name': 'jack', 'age': 18}
dic.clear()
print(dic)  #{}
print('------------------------2-3 clear')

# 5	批量更新(有该键就更新，没该键就添加）
dic = {'name': 'jack', 'age': 18}
dic2 = {'name2': 'jack', 'age': 20}
dic.update(dic2)
print(dic)  #{'name': 'jack', 'age': 20, 'name2': 'jack'}
print('------------------------3 updare 修改')

# 6	通过键获取值（若没有该键可设置默认值，预防报错）
dic = {'name': 'jack', 'age': 18}
print(dic['name'])  #jack
# print(dic['name2'])  #KeyError: 'name2'

dic = {'name': 'jack', 'age': 18}
print(dic.get('name'))  #jack
print(dic.get('name2','抱歉,没有该键'))  #抱歉,没有该键
print('------------------------4 get 获取')

# 7	将字典的键组成新的可选代对象
dic = {'name': 'jack', 'age': 18}
for i in dic.keys():
	print(i)
# name
# age
print('------------------------5-1 dic.keys()')

# 8	将字典中的值组成新的可迭代对象
dic = {'name': 'jack', 'age': 18}
for i in dic.values():
	print(i)
# jack
# 18
print('------------------------5-2 dic.values()')


# 9	将字典的键值对凑成一个个元组，组成新的可迭代对象
dic = {'name': 'jack', 'age': 18}
for k,v in dic.items():
	print(k,v)
# name jack
# age 18
print('------------------------5-3 dic.items()')

# 10	交集
set1 = {1,2}
set2 = {3,2}
set3 = set1 & set2
print(set3)  #{2}

set4 = set1.intersection(set2)
print(set4)  #{2}
print('------------------------1 集合  交集  &   intersection')

# 11	差集
set1 = {1,2}
set2 = {3,2}
set3 = set1 - set2
print(set3)  #{1}

set4 = set1.difference(set2)
print(set4)  #{1}
print('------------------------2 集合  差集  -   difference')

# 12	并集
set1 = {1,2}
set2 = {3,2}
set3 = set1 | set2
print(set3)  #{1, 2, 3}

set4 = set1.union(set2)
print(set4)  #{1, 2, 3}
print('------------------------3 集合  并集  |   union')

# 13	对称差集《补集情况涵盖在其中）
set1 = {1,2}
set2 = {3,2}
set3 = set1 ^ set2
print(set3)  #{1, 3}

set4 = set1.symmetric_difference(set2)
print(set4)  #{1, 3}
print('------------------------4 集合  对称查集-补集  ^   symmetric_difference')

# 14	判断是否是子集
set1 = {1,2}
set2 = {2}
print(set2<set1)  #True
print(set2.issubset(set1)) #True
print('------------------------5 集合  子集  <   issubset')

# 15	判断是否是父集
set1 = {1,2}
set2 = {2}
print(set1 > set2)  #True
print(set1.issuperset(set2)) #True
print('------------------------6 集合  父集  >   issuperset')

# 16	检测两集合是否不相交不相交True相交False
set1 = {1,2}
set2 = {2}
print(set1.isdisjoint(set2))  #False
print('------------------------7 集合  不相交     isdisjoint')

# 17	向集合中添加数据
set1 = {1,2}
set1.add(3)
print(set1) #{1, 2, 3}
print('------------------------1 集合 单个添加 add')

# 18	迭代着曾加
set1 = {1,2}
set1.update('abc')
print(set1)  #{1, 2, 'b', 'a', 'c'}
print('------------------------1-2 集合 迭代添加 update')

# 19	清空集合
set1 = {1,2}
set1.clear()
print(set1)  #set()
print('------------------------2-1 集合 删除清空  clear')

# 20	随机删除集合中的一个数据
set1 = {1,2}
set1.pop()  #不推荐
print(set1)  #{2}
print('------------------------2-2 集合 删除 pop')

# 21	删除集合中指定的值(不存在则报错）
set1 = {1,2}
set1.remove(2)
print(set1)  #{1}

# set1 = {1,2}
# set1.remove(23)  #KeyError: 23
# print(set1)
print('------------------------2-3 集合 删除 remove')

# 22	删除集合中指定的值（不存在的不删除推荐使用）
set1 = {1,2}
set1.discard(1)
print(set1) #{2}

set1 = {1,2}
set1.discard(55)  #只能是1个参数
print(set1)  #{1, 2}
print('------------------------2-4 集合 删除 discard')

# 23	可强转容器类型数据变为冰冻集合
set1 = {1,2}
fz = frozenset(set1)
print(fz)  #frozenset({1, 2})  #只读,只有交差并补,可以遍历  类似:元组

# 24	冰冻集合
# 25	如何写入文件内容
with open('1.txt',mode='w',encoding='utf-8') as fp:
	fp.write('hello') #写入文件的是str或者bytes

# 26	如问读取文件内容
with open('1.txt',mode='r',encoding='utf-8') as fp:
	res = fp.read()
	print(res)  #hello

# 27	存储字节流用什么模式   b
# 28	r+ 和a+，W+区别
# r+ 可读可写.打开文件后,光标默认在文件开头,会覆盖行首
# a+ 可读可写.打开文件后,光标默认强制在文件结尾,会覆盖seek()
# w+ 可读可写.每次都清空文件后,开始写

# 29	使用with语法，复制图片
# '''

# 读取字节流(从文件1)
with open('图片1.png',mode='rb') as fp:
	res = fp.read()  #bytes

# 写入字节流到另外一个文件2
with open('图片2.png',mode='wb') as fp:
	fp.write(res)  #写入文件的是str或者bytes 这里是bytes















