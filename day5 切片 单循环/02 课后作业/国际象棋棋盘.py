#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/16 22:28


# ★☆★☆★☆★☆
# ☆★☆★☆★☆★
# ★☆★☆★☆★☆
# ☆★☆★☆★☆★
# ★☆★☆★☆★☆
# ☆★☆★☆★☆★
# ★☆★☆★☆★☆
# ☆★☆★☆★☆★

# 先做10*10 再换成8*8
i = 0
while i < 64:
	if i //8 %2 ==0:
		if i % 2 ==0:
			print('★',end='')
		else:
			print('☆', end='')
	else:
		if i % 2 == 0:
			print('☆', end='')
		else:
			print('★', end='')
	if i % 8 ==7:
		print()
	i +=1















