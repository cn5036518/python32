#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/26 19:07

# 7拼接任意个数值变成字符串（修改字典的键）
"""
班长: 赵万里
班花: 马春陪
划水群众: 赵沈阳,李虎凌,刘子涛
"""


# 1完成新字典的打印
def func(**kwargs):
	dic = {'monitor': '班长', 'classflower': '班花'}
	print(kwargs)  # {'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	dic_new = {}
	for k, v in kwargs.items():
		if k in dic:  #关键点
			dic_new[dic[k]] = v  # {'班长': '赵万里', '班花': '马春陪'}  #关键点
		else:
			dic_new[k] = v  # {'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	print(dic_new)  # {'班长': '赵万里', '班花': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}


func(monitor="赵万里", classflower="马春陪", water1="赵沈阳", water2="李虎凌", water3="刘子涛")

# 思路
# 1 实现   --ok
# dic = {'班长':"赵万里",'班花':"马春陪",water1="赵沈阳",water2="李虎凌",water3="刘子涛"}
# 2 先字典打印  --ok
# 3 后拼接字符串
print('---------------------------------1')

# 2 后拼接字符串输出
"""
班长: 赵万里
班花: 马春陪
划水群众: 赵沈阳,李虎凌,刘子涛
"""

def func(**kwargs):
	dic = {'monitor': '班长', 'classflower': '班花'}
	print(kwargs)  # {'monitor': '赵万里', 'classflower': '马春陪', 'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}

	strvar1 = ''
	strvar2 = ''

	for k, v in kwargs.items():
		if k in dic:
			strvar1 +=(dic[k] + ':' + v + '\n') # {'班长': '赵万里', '班花': '马春陪'}  #关键点  拼接字符串
		else:
			strvar2 +=(v + ',')  # {'water1': '赵沈阳', 'water2': '李虎凌', 'water3': '刘子涛'}
	print(strvar1.strip())
	print('划水群众：',strvar2.strip(','))


func(monitor="赵万里", classflower="马春陪", water1="赵沈阳", water2="李虎凌", water3="刘子涛")
print('---------------------------------2')

# 5.等待用户输入内容，是否包含敏感字符？
# 如果存在敏感字符提示“存在敏感字符请重新输入”，敏感字符：“粉嫩”、“铁锤”

#方法1
while True:
	content = input('请输入内容：')
	if ('粉嫩' or '铁锤')  in content:   #优先级  in成员运算符 > 逻辑运算符or  必须加上小括号
		print('存在敏感字符请重新输入')
	else:
		print('输入不包含敏感字符，符合要求')
		break

# 方法2
lst = ['粉嫩','铁锤']
while True:
	content = input('请输入内容：')
	for i in lst:
		if i in content:
			print('存在敏感字符请重新输入')
			break
	else:  #注意点：这个else和for是同一个缩进
		print('输入不包含敏感字符，符合要求')
		break









































