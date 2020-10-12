#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 21:51

# # ### 列表相关练习
# 1.li = ["alex", "WuSir", "xboy", "oldboy"]
# 1)列表中追加元素"seven",并输出添加后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.append('seven')
print(li)  #['alex', 'WuSir', 'xboy', 'oldboy', 'seven']

# 2)请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.insert(0,'Tony')
print(li)  #['Tony', 'alex', 'WuSir', 'xboy', 'oldboy']

# 3)请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li[1] = 'Kelly'
print(li)  #['alex', 'Kelly', 'xboy', 'oldboy']

# 4)请将列表l2=[1,"a",3,4,"heart"]的每一个元素添加到列表li中，一行
# 代码实现，不允许循环添加。
li = ["alex", "WuSir", "xboy", "oldboy"]
l2=[1,"a",3,4,"heart"]
li.extend(l2)
print(li)  #['alex', 'WuSir', 'xboy', 'oldboy', 1, 'a', 3, 4, 'heart']

# 5)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
li = ["alex", "WuSir", "xboy", "oldboy"]
s = 'qwert'
li.extend(s)
print(li)  #['alex', 'WuSir', 'xboy', 'oldboy', 'q', 'w', 'e', 'r', 't']

# 6)请删除列表中的元素"alex",并输出添加后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.remove('alex')
print(li) #['WuSir', 'xboy', 'oldboy']

# 7)请删除列表请删除列表中的第2至4个元素，并输出删除元素后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
del li[1:4]
print(li)

# 8)删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
res = li.pop(1)
print(res)  #WuSir
print(li)  #['alex', 'xboy', 'oldboy']

# 9)请将列表所有得元素反转，并输出反转后的列表
li = ["alex", "WuSir", "xboy", "oldboy"]
li.reverse()
print(li) #['oldboy', 'xboy', 'WuSir', 'alex']

# 10)请计算出"alex"元素在列表li中出现的次数，并输出该次数。
li = ["alex", "WuSir", "xboy", "oldboy"]
res = li.count('alex')
print(res)  #1



































