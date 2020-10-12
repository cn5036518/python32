#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 9:02


# 1	使用一组键和默认值创建字典
# 2	通过键去删除键值对（若没有该键可设置默认值，预防报错)
# 3	删除最后一个键值对
# 4	清空字典
# 5	批量更新(有该键就更新，没该键就添加）
# 6	通过键获取值（若没有该键可设置默认值，预防报错）
# 7	将字典的键组成新的可选代对象
# 8	将字典中的值组成新的可迭代对象
# 9	将字典的键值对凑成一个个元组，组成新的可迭代对象
# 10	交集
# 11	差集
# 12	并集
# 13	对称差集《补集情况涵盖在其中）
# 14	判断是否是子集
# 15	判断是否是父集
# 16	检测两集合是否不相交不相交True相交False
# 17	向集合中添加数据
# 18	迭代着曾加
# 19	清空集合
# 20	随机删除集合中的一个数据
# 21	删除集合中指定的值(不存在则报错）
# 22	删除集合中指定的值（不存在的不删除推荐使用）
# 23	可强转容器类型数据变为冰冻集合
# 24	冰冻集合
# 25	如何写入文件内容
# 26	如问读取文件内容
# 27	存储字节流用什么模式
# 28	r+ 和a+，W+区别
# 29	使用with语法，贼值图片


# 1	使用一组键和默认值创建字典
lst = ['a','b','c']
dic = {}.fromkeys(lst,22)
print(dic)  #{'a': 22, 'b': 22, 'c': 22}
print('-----------------1')

# 2	通过键去删除键值对（若没有该键可设置默认值，预防报错)
dic = {'a': 22, 'b': 22, 'c': 22}
res = dic.pop('a')
print(res)  #22
print(dic)  #{'b': 22, 'c': 22}

res = dic.pop('d','没有该键')
print(res)  #没有该键
print(dic)  #{'b': 22, 'c': 22}
print('-----------------2')

# 3	删除最后一个键值对
dic = {'a': 22, 'b': 22, 'c': 22}
dic.popitem()
print(dic)  #{'a': 22, 'b': 22}
print('-----------------3')

# 4	清空字典
dic = {'a': 22, 'b': 22, 'c': 22}
dic.clear()
print(dic)  #{}
print('-----------------4')

# 5	批量更新(有该键就更新，没该键就添加）
dic = {'a': 22, 'b': 22, 'c': 22}
dic2 = {'a': 24, 'd': 22}
dic.update(dic2)
print(dic)  #{'a': 24, 'b': 22, 'c': 22, 'd': 22}
print('-----------------5')








































