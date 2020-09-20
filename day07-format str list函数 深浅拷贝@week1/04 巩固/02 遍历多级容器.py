#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/19 15:53


# 1.遍历不等长多级容器
container = [1,2,3,4,("嗄","234",{"马春配","李虎凌","刘子涛"})]

for i in container:
	if isinstance(i,(tuple)):
		for j in i:
			if isinstance(j,(set)):
				for k in j:
					print(k)
			else:
				print(j)
		
	else:
		print(i)

# 1
# 2
# 3
# 4
# 嗄
# 234
# 马春配
# 李虎凌
# 刘子涛
print('-----------------------------------1')


# 1.遍历不等长多级容器
container = [1,2,3,4,("嗄","234",{"马春配","李虎凌","刘子涛"})]

for i in container:
	if isinstance(i,(tuple)):
		for j in i:
			if isinstance(j,(set)):
				for k in j:
					print(k)
			else:
				print(j)
	else:
		print(i)

print('-----------------------------------2')

# 1.遍历不等长多级容器
container = [1,2,3,4,("嗄","234",{"马春配","李虎凌","刘子涛"})]

for i in container:
	if isinstance(i,(tuple)):
		for j in i:
			if isinstance(j,(set)):  #参数2是元组
			# if isinstance(j,set):
				for k in j:
					print(k)
			else:
				print(j)			
	else:
		print(i)

print('-----------------------------------3')










































