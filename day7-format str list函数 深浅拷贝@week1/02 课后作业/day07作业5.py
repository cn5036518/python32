#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 22:03


# 2，写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 1)通过对li列表的切片形成新的列表l1,l1 = [1,3,2]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res = li[:3]
print(res)  #[1, 3, 2]

# 2)通过对li列表的切片形成新的列表l2,l2 = ["a",4,"b"]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res = li[3:6]
print(res)  #['a', 4, 'b']

# 3)通过对li列表的切片形成新的列表l3,l3 = ["1,2,4,5]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res =li[::2]
print(res)  #[1, 2, 4, 5]

# 4)通过对li列表的切片形成新的列表l4,l4 = [3,"a","b"]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res = li[1:-2:2]
print(res)  #[3, 'a', 'b']

# 5)通过对li列表的切片形成新的列表l5,l5 = ["c"]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res = li[-1]
print(res)  #c

res = li[-1:]  #注意
print(res)  #['c']

# 6)通过对li列表的切片形成新的列表l6,l6 = ["b","a",3]
li = [1, 3, 2, "a", 4, "b", 5,"c"]
res = li[-3:0:-2]
print(res)  #['b', 'a', 3]

#
# 3,写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# 1)将列表lis中的"tt"变成大写。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

lis[3][2][1][0]= lis[3][2][1][0].upper()
print(lis)  #[2, 3, 'k', ['qwe', 20, ['k1', ['TT', 3, '1']], 89], 'ab', 'adv']

# 2)将列表中的数字3变成字符串"100"。
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][1] = '100'
print(lis)  #[2, 3, 'k', ['qwe', 20, ['k1', ['tt', '100', '1']], 89], 'ab', 'adv']

# 3)将列表中的字符串"1"变成数字101
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis[3][2][1][-1] = 101
print(lis)  #[2, 3, 'k', ['qwe', 20, ['k1', ['tt', 3, 101]], 89], 'ab', 'adv']

# 4,li = ["alex", "eric", "rain"]
# 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
li = ["alex", "eric", "rain"]
strvar = '_'.join(li)
print(strvar)  #alex_eric_rain

# 5.利用for循环打印出下面列表的索引。
# li = ["alex", "WuSir", "xboy", "oldboy"]
li = ["alex", "WuSir", "xboy", "oldboy"]
for i in range(len(li)):
	print(i,li[i])
# 0 alex
# 1 WuSir
# 2 xboy
# 3 oldboy
















