#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 9:02

# 10	交集
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1 & set2
print(set3)  #{2, 3}

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.intersection(set2)
print(set3)  #{2, 3}
print('---------------------10')

# 11	差集
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1 - set2
print(set3)  #{1}

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.difference(set2)
print(set3)  #{1}
print('---------------------11')

# 12	并集
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1 | set2
print(set3)  #{1, 2, 3, 4}

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.union(set2)
print(set3)  #{1, 2, 3, 4}
print('---------------------12')

# 13	对称差集《补集情况涵盖在其中）
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1 ^ set2
print(set3)  #  {1, 4}

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.symmetric_difference(set2)
print(set3)  # {1, 4}
print('---------------------13')

# 14	判断是否是子集
set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1 < set2
print(set3)  #  False

set1 = {1,2,3}
set2 = {2,3,4}
set3 = set1.issubset(set2)
print(set3)  # False
print('---------------------14')

# 15	判断是否是父集
set1 = {1,2,3}
set2 = {2,3}
set3 = set1 > set2
print(set3)  #  True

set1 = {1,2,3}
set2 = {2,3}
set3 = set1.issuperset(set2)
print(set3)  # True
print('---------------------15')

# 16	检测两集合是否不相交不相交True相交False
set1 = {1,2,3}
set2 = {2,3}
set3 = set1.isdisjoint(set2)
print(set3)  # False
print('---------------------16')

# 17	向集合中添加数据
set1 = {1,2,3}  #去重 无序
set1.add(4)
print(set1)  #{1, 2, 3, 4}
print('---------------------17')

# 18	迭代着曾加
set1 = {1,2,3}  #去重 无序
str1 = 'abc'
set1.update(str1)  #参数需要是可迭代类型（容器，range(),迭代器）
print(set1)  #{1, 2, 3, 'b', 'a', 'c'}

set1 = {1,2,3}  #
set1.update(range(4,6))  #参数需要是可迭代类型（容器，range(),迭代器）
print(set1)  #{1, 2, 3, 4, 5}
print('---------------------18')

# 19	清空集合
set1 = {1,2,3}  #
set1.clear()
print(set1)   #set()
print('---------------------19')

# 20	随机删除集合中的一个数据
set1 = {1,2,3}  #
set1.pop()  #不推荐
print(set1)   #
print('---------------------20')

# 21	删除集合中指定的值(不存在则报错）
set1 = {1,2,3}  #
set1.remove(1)  #不推荐
print(set1)   #{2, 3}

# set1.remove(4)  #
# print(set1)   #KeyError: 4
print('---------------------21')

# 22	删除集合中指定的值（不存在的不删除推荐使用）
set1 = {1,2,3}  #
set1.discard(1)  #推荐
print(set1)   #{2, 3}

set1 = {1,2,3}  #
set1.discard(4)  #推荐
print(set1)   #{1, 2, 3}
print('---------------------22')

# 23	可强转容器类型数据变为冰冻集合
set1 = {1,2,3} 
fz1 = frozenset(set1)
print(fz1)  #frozenset({1, 2, 3})
print('---------------------23')

# 24	冰冻集合











































