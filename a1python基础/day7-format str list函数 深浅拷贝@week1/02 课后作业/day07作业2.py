#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 20:50


# 1.有变量name = "aleX leNb" 完成如下操作：

# 移除 name 变量对应的值两边的空格,并输出处理结果

# 1)移除name变量左边的"al"并输出处理结果
name = 'aleX leNb'
res = name.lstrip('al')
print(res)  #eX leNb

# 2)移除name变量右面的"Nb",并输出处理结果
name = 'aleX leNb'
res = name.rstrip('Nb')
print(res)  #aleX le

# 3)移除name变量开头的a与最后的"b",并输出处理结果
name = 'aleX leNb'
res = name.strip('ab')
print(res) #leX leN

# 4)判断 name 变量是否以 "al" 开头,并输出结果
name = 'aleX leNb'
res = name.startswith('al')
print(res)  #True

# 5)判断name变量是否以"Nb"结尾,并输出结果
name = 'aleX leNb'
res = name.endswith('Nb')
print(res)  #True

# 6)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
name = 'aleX leNb'
res = name.replace('l','p')
print(res)  #apeX peNb

# 7)将name变量对应的值中的第一个"l"替换成"p",并输出结果
name = 'aleX leNb'
res = name.replace('l','p',1)
print(res)  #apeX leNb

# 8)将 name 变量对应的值根据 所有的"l" 分割,并输出结果。
name = 'aleX leNb'
res = name.split('l')
print(res)  #['a', 'eX ', 'eNb']

# 9)将name变量对应的值根据第一个"l"分割,并输出结果。
name = 'aleX leNb'
res = name.split('l',1)
print(res)  #['a', 'eX leNb']

# 10)将 name 变量对应的值变大写,并输出结果
name = 'aleX leNb'
res = name.upper()
print(res)  #ALEX LENB

# 11)将 name 变量对应的值变小写,并输出结果
name = 'aleX leNb'
res = name.lower()
print(res)  #alex lenb

# 12)将name变量对应的值首字母"a"大写,并输出结果
name = 'aleX leNb'
res = name.capitalize()
print(res)  #Alex lenb

# 13)判断name变量对应的值字母"l"出现几次，并输出结果
name = 'aleX leNb'
res = name.count('l')
print(res)  #2

# 14)如果判断name变量对应的值前四位"l"出现几次,并输出结果
name = 'aleX leNb'
res = name.count('l',0,4)
print(res)  #1

# 15)从name变量对应的值中找到"N"对应的索引(如果找不到则报错)，并输出结果
name = 'aleX leNb'
res = name.index('N')
print(res)  #7

# 16)从name变量对应的值中找到"N"对应的索引(如果找不到则返回-1)输出结果
name = 'aleX leNb'
res = name.find('N')
print(res)  #7

# 17)从name变量对应的值中找到"X le"对应的索引,并输出结果
name = 'aleX leNb'
res = name.find('X le')
print(res)  #3

# 18)请输出 name 变量对应的值的第 2 个字符?
name = 'aleX leNb'
res = name[1]
print(res)  #l

# 19)请输出 name 变量对应的值的前 3 个字符?
name = 'aleX leNb'
res = name[:3]
print(res)  #ale

# 20)请输出 name 变量对应的值的后 2 个字符?
name = 'aleX leNb'
res = name[-2:]
print(res)  #Nb

# 21)请输出 name 变量对应的值中 "e" 所在索引位置?
name = 'aleX leNb'
res = name.find('e')
print(res)  #2

















