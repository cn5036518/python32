#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/18 9:02


# for  单循环
for i in range(64):
	if i // 10 % 2 == 0:
		if i % 2 == 0:
			print('□',end='')
		else:
			print("■",end='')
	else:
		if i % 2 == 0:
			print("■",end='')
		else:
			print('□',end='')
	if i % 8 ==7:
		print()
print('----------------------------1')

# for  双循环













