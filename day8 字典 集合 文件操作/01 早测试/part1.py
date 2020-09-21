#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/21 10:17

''''''
'''
# part1
# 1.集合的值和字典的键有什么数据类型上的要求
必须是不可变类型(number tuple str)
可变类型(list dict set)

# 2.对于python3.6来说,变量的缓存机制
numbers 
	int   -5~正无穷      值相同 id相同(内存地址)
	float   非负浮点数   值相同 id相同
	bool                 值相同 id相同
	complex              值相同 id不同(正虚数5j 除外)
容器类型
	str     值相同 id相同
	tuple   值相同 id不同(空元组例外)
	list    值相同 id不同
	dict    值相同 id不同
	set     值相同 id不同

# 3.bool类型为假的十种情况
numbers 
	int     0
	float   0.0
	bool      False       
	complex       0j       
容器类型
	str       ''
	tuple      ()
	list        []
	dict         {}
	set            set()
None

# 4.Number类型的自动转换原则
从低精度到高精度转换
bool --> int --> float --> complex

# 5.容器类型强转特征
str
	可以强转任何类型,两边加上引号即可

tuple
	str   把字符串的每个字符单独拿出来,作为元组的新元素
	dict   获取字典的键,作为元组的元素
	list\set(其他容器类型) 把外层的符号换成()小括号

list
	str   把字符串的每个字符单独拿出来,作为list的新元素
	dict   获取字典的键,作为list的元素
	tuple\set(其他容器类型) 把外层的符号换成[]中括号

set
	str   把字符串的每个字符单独拿出来,作为set的新元素
	dict   获取字典的键,作为set的元素
	list tuple(其他容器类型) 把外层的符号换成{}大括号

# 6.什么样的类型可以强转成字典   
	等长的二级容器,二级容器的长度是2

# 7.什么情况下会出现短路
	True or
	False and

# 8.is和==有什么区别
	is  判断两个变量的内存地址是否一样  id
	==  判断两个变量的数值是否相等   

# 9.逻辑运算符优先级排序
   ()  > not > and > or

# 10.<< >> 运算规律
	<<  左移   *2^n  (n是左移的位数)
	>>  右移   /2^n  (n是右移的位数)

'''












































