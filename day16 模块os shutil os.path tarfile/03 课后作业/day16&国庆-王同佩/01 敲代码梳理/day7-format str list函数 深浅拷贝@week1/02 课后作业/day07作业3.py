#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 21:25

""""""
'''
# 2.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算

# 3.升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。
#
# 4.计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
#
# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”
#
#
# 6.制作趣味模板程序需求：等待用户输入名字、地点、爱好
# 拼装数据打印出：敬爱可亲的xxx，最喜欢在xxx地方xxx
'''

# 2.实现一个整数加法计算器(两个数相加)：
# 如：content = input("请输入内容:") 用户输入：5+9或3+ 9或5 + 6，然后进行分割再进行计算
content = input('请输入内容:')
content = content.strip()
a , b = content.split('+')
a = a.strip()
b = b.strip()
if a.isdecimal() and b.isdecimal(): #
	print('%s + %s = %s' % (int(a),int(b),int(a)+int(b)))
else:
	print('请输入数字或者+,比如: 5+9')

# 4.计算用户输入的内容中有几个整数（以个位数为单位）。
# 如：content = input("请输入内容：")   # 如fhdal234slfh98769fjdla
input1 = input("请输入内容2：")
# input1 = 'fhdal234slfh98769fjdla'
count1 = 0
for i in input1:
	if i.isdecimal():
		count1 += 1
print(count1)  #8

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”

while True:
	content = input('请输入:')
	if ('铁锤' or '粉嫩') in content:  #成员运算符 > 逻辑运算符   加小括号
		print('存在敏感字符,请重新输入')
	else:
		print('输入正确')
		break

# 6.制作趣味模板程序需求：等待用户输入名字、地点、爱好
# 拼装数据打印出：敬爱可亲的xxx，最喜欢在xxx地方xxx

content1 = input('请输入名字:')
content2 = input('请输入地点:')
content3 = input('请输入爱好:')
print('敬爱可亲的%s,最喜欢在%s地方%s' % (content1,content2,content3))
print('敬爱可亲的{},最喜欢在{}地方{}'.format(content1,content2,content3))
print('敬爱可亲的{:s},最喜欢在{:s}地方{:s}'.format(content1,content2,content3))


# 3.升级题：实现一个整数加法计算器（多个数相加）：
# 如：content = input("请输入内容:") 用户输入：5+9+6 +12+  13，然后进行分割再进行计算。

# content = '5+9+6 +12+  13'
content = input('请输入内容,比如:1+2+3:')
listvar = content.split('+')
# print(listvar)  #['5', '9', '6 ', '12', '  13']
for i in listvar:
	if not i.strip().isdecimal():
		print('输入格式错误,正确的格式是数字和+,比如:1+2+3')
		break
else:
	total = 0
	for i in listvar:
		total += int(i.strip())
	print(total)  #45





















