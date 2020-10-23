#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:   2020/10/7 上午9:14

# ### 1.注册登录小程序
# 注册:
# (1)检测两次密码如果相同,确认注册成功
# (2)检测两次密码如果不同,提示两次密码不一致
# (3)用户名不能重复

# 登录:
# (1)输入账号密码:如果都正确,登录成功
# (2)如果用户登录时进行三次校验,都不对,记录黑名单文件中
# (3)如果是黑名单的用户,禁止下次再次登录


# 解题注意点:
# 1 先写思路伪代码,再写代码
# 2 先简单实现demo,再迭代完善
# 3 对自己保持足够的耐心
   # 不跳步骤
   # 不怕慢,就怕停

# 思路
# 注册
# 1 新建字典

# 登录
# 2 拿用户的输入和字典存储的进行校验

# 步骤:
# 1 先字典-内存1 后json到文件--nok
# 2 先注册1 后登录
    # 黑名单1    先字典 后文件1
# 3 注册和登录先分开,后合并到一个入口的2个选项--nok

#版本1   # 1注册和登录分开 2黑名单  3注册到字典
#版本2   # 1注册和登录分开 2黑名单  3注册到文件1
#              white.txt  先 w  后r+
#版本3   # 1注册和登录合并一个入口 2黑名单  3注册到文件

import json
import os

#注册
def register():
	dic = {}
	while True:
		name = input('注册,请输入你的用户名,输入q退出:')
		if name.upper() == 'Q':
			print('退出注册')
			break
		else:
			if name not in dic:
				while True:
					password1 = input('注册,请输入密码:')
					password2 = input('注册,请再次输入密码:')
					if password1 != password2:
						print('两次密码不一致,请重新输入密码:')
					else:
						print('恭喜你,用户名{}注册成功.'.format(name))
						# 把字典写入文件
						if not os.path.exists('white_list.txt'):
							dic[name] = password2
							with open('white_list.txt',mode='w',encoding='utf-8') as fp:
								json.dump(dic,fp,ensure_ascii=False)
								# fp.write('\n')	
							# break
						else: #如果用户文件存在,追加到字典中
							with open('white_list.txt',mode='r+',encoding='utf-8') as fp:
								dic = json.load(fp)
								dic[name] = password2
								fp.seek(0)
								json.dump(dic,fp,ensure_ascii=False)
						break
			else:
				print('用户名已存在,请重新输入用户名')
	print(dic)  #{'jack': '1', 'tom': '1'}
	
#调注册
register()

# 读取已注册的用户列表
# dic = {'jack': '1', 'tom': '1'}
with open('white_list.txt',mode='r',encoding='utf-8') as fp:
		dic = json.load(fp)
print(dic)


def login():
	list_black = []
	# 登录
	times = 0
	sign = True
	while sign:
		name = input('登录,请输入你的用户名:')
		password = input('登录,请输入你的密码:')
		# if name in list_black:
		if os.path.exists('black_list.txt'):  #1存在黑名单文件
			with open('black_list.txt',mode='r',encoding='utf-8') as fp:
				for i in fp:
					# lst = json.load(i) #AttributeError: 'str' object has no attribute 'read'
					lst = json.loads(i)
					if name in lst:
						print('对不起,该账户禁止登录哈')
						sign = False
						break
				else:
					if name not in dic:
						times +=1
						print('对不起,用户名或者密码不对,请重新输入,你还有{:d}次登录机会'.format(2-times))	
					else:
						if password != dic[name]:
							times +=1
							print('用户名或者密码不对,请重新输入,你还有{:d}次登录机会'.format(2-times))
						elif password == dic[name]:
							print('登录成功')
							break
			
		else:#2不存在黑名单文件
			if name not in dic:
				times +=1
				print('对不起,用户名或者密码不对,请重新输入,你还有{:d}次登录机会'.format(2-times))	
			else:
				if password != dic[name]:
					times +=1
					print('用户名或者密码不对,请重新输入,你还有{:d}次登录机会'.format(2-times))
				elif password == dic[name]:
					print('登录成功')
					break	
		if times == 2:  # 到达错误登录次数
			list_black.append(name)
			with open('black_list.txt',mode='a',encoding='utf-8') as fp:
				json.dump(list_black,fp,ensure_ascii=False)
				fp.write('\n')		
			print('对不起,你的账号被锁定')
			break

#调登录
# login()





















