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


# 指导思想:
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
#版本3   # 1注册和登录合并一个入口1 2黑名单  3注册到文件
#版本4   # 1注册和登录合并一个入口1 2黑名单  3注册到文件  4优化黑名单list
#版本5   优化锁定次数1
#版本6   解决tab和空格的缩进不一致
#版本7   优化整体逻辑1  判断优先级1 重复代码1(删除非必要注释1)  先注册1后登录1
#版本8   小结

import json
import os



#注册
def register():
	dic = {}  #初始化字典
	# 1 如果用户数据不存在,就创建一个
	if not os.path.exists('white_list.txt'):
		with open('white_list.txt', mode='w', encoding='utf-8') as fp:
			json.dump(dic, fp, ensure_ascii=False)
	# 2 如果用户数据存在,就读取用户账号
	else:
		with open('white_list.txt', mode='r', encoding='utf-8') as fp:
			dic = json.load(fp)
			
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
						#追加到字典中
						with open('white_list.txt',mode='r+',encoding='utf-8') as fp:
							dic[name] = password2
							fp.seek(0)
							json.dump(dic,fp,ensure_ascii=False)
						break
			else:
				print('用户名已存在,请重新输入用户名')
	print('已注册名单:',dic)  #{'jack': '1', 'tom': '1'}


#登录
def login():
	list_black = []
	# 读取已注册的用户账号列表
	# dic = {'jack': '1', 'tom': '1'}
	with open('white_list.txt',mode='r',encoding='utf-8') as fp:
		dic = json.load(fp)
	print('已注册名单:',dic)
	times = 0
	sign = True
	while sign:
		name = input('登录,请输入你的用户名:')
		password = input('登录,请输入你的密码:')
		
		# 1 如果用户黑名单不存在,就创建一个
		if not os.path.exists('black_list.txt'):
			with open('black_list.txt', mode='w', encoding='utf-8') as fp:
				json.dump(list_black, fp, ensure_ascii=False)
		# 2 如果用户黑名单存在,就读取用户黑名单
		else:
			with open('black_list.txt', mode='r', encoding='utf-8') as fp:
				list_black = json.load(fp)			

		if name in list_black:  #判断优先级1 黑名单
			print('对不起,该账户禁止登录哈')
			sign = False
			break
		else:
			if name not in dic:  #判断优先级2  已注册(白名单)
				print('对不起,用户名未注册,请重新输入')	
			else:
				if password != dic[name]:
					times +=1
					print('用户名或者密码不对,请重新输入,你还有{:d}次登录机会'.format(2-times))
				elif password == dic[name]:
					print('登录成功')
					break			

		if times == 2:  # 到达错误登录次数
			list_black.append(name)
			with open('black_list.txt',mode='w',encoding='utf-8') as fp:
				json.dump(list_black,fp,ensure_ascii=False)
			print('对不起,你的账号被锁定')
			print('黑名单:',list_black)
			break

while True:
	choice = input('您好,注册(R),登录(L),退出(Q),请按键选择:')
	if choice.upper() == 'R':
		register()
	elif choice.upper() == 'L':
		login()
	elif choice.upper() == 'Q':
		break
	else:
		print('输入错误,请重新输入')
	

















