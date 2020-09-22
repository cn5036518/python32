#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 20:16

# #2.有如下文件，t1.txt,里面的内容为：
# 	葫芦娃，葫芦娃，
# 	一根藤上七个瓜
# 	风吹雨打，都不怕，
# 	啦啦啦啦。
# 	上面的内容你肯定是心里默唱出来的,对不对
#
# 分别完成下面的功能：
# a:以r+的模式打开原文件，判断原文件是否可读，是否可写。
# b:以r的模式打开原文件，利用for循环遍历文件对象。
# c:以r的模式打开原文件，以readlines()方法读取出来，并循环遍历
# d:以r模式读取‘葫芦娃，’前四个字符。
# e:以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
# f:以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
# g:以a+模式打开文件，先追加一行：‘老男孩教育’然后在全部读取出来。
# h:截取原文件，截取内容：‘葫芦娃，葫芦娃，’

# a:以r+的模式打开原文件，判断原文件是否可读，是否可写。
with open('t1.txt',mode='r+',encoding='utf-8') as fp:
	res = fp.readable()  #True
	print(res)
	res = fp.writable()  #True
	print(res)
print('-------------------1')

# b:以r的模式打开原文件，利用for循环遍历文件对象。
with open('t1.txt',mode='r',encoding='utf-8') as fp:
	for i in fp:
		print(i.strip())
print('-------------------2')

# c:以r的模式打开原文件，以readlines()方法读取出来，并循环遍历
with open('t1.txt',mode='r',encoding='utf-8') as fp:
	listvar = fp.readlines()
	for i in listvar:
		print(i.strip())
print('-------------------3')

# d:以r模式读取‘葫芦娃，’前四个字符。
with open('t1.txt',mode='r',encoding='utf-8') as fp:
	res = fp.read(4)  #4个字符
	print(res)  #葫芦娃，	
print('-------------------4')

# e:以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
with open('t1.txt',mode='r',encoding='utf-8') as fp:
	res = fp.readline()
	print(res.strip())  #葫芦娃，葫芦娃，
print('-------------------5')

# f:以r模式打开文件，从‘风吹雨打.....’开始读取，一直读到最后。
with open('t1.txt',mode='r',encoding='utf-8') as fp:
	listvar = fp.readlines()
	# print(listvar)
	for i in range(len(listvar)):
		if i >=2:
			print(listvar[i].strip())
print('-------------------6')

# g:以a+模式打开文件，先追加一行：‘老男孩教育’然后在全部读取出来。
with open('t1.txt',mode='a+',encoding='utf-8') as fp:
	fp.write('\n老男孩教育')
	fp.seek(0,0)
	res = fp.read()
	print(res)
print('-------------------7')

# h:截取原文件，截取内容：‘葫芦娃，葫芦娃，’
# with open('t1.txt',mode='r+',encoding='utf-8') as fp:
# 	fp.truncate(24)  #中文的逗号占3个字节  英文的逗号占1个字节
# print('-------------------8')
















