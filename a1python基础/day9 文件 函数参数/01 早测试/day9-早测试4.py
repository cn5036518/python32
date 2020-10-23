#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/22 9:02

# 25	如何写入文件内容
with open('25.txt',mode='w',encoding='utf-8') as fp:
	fp.write('hello world')  #参数是字符串，文件的内容都是字符串

# 26	如问读取文件内容
with open('25.txt',mode='r',encoding='utf-8') as fp:
	res = fp.read()
	print(res)	  #hello world

# 27	存储字节流用什么模式  b
with open('day9-早测试默写.bmp',mode='rb') as fp:  #rb字节流模式，不能带encoding
	res = fp.read()
	print(res)

# 28	r+ 和a+，W+区别
# r+  可读可写  光标在文件开头，进行写入覆盖（写入的话，需要移动光标到文件末尾。否则会出现覆盖）
# a+  可读可写  文件末尾追加  光标强制到文件末尾（seek无效）
# w+  可读可写   每次都清空文件重写

# 29	使用with语法，复制图片
# 思路：先把老的文件中的图片读取出来，然后把读取后的内容写入到新的文件
with open('day9-早测试默写.bmp',mode='rb') as fp1:  #rb字节流模式，不能带encoding
	res = fp1.read()

with open('day9-早测试默写2.bmp',mode='wb') as fp1:  #rb字节流模式，不能带encoding
	fp1.write(res)









































