#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/17 21:30


# 求吉利数字 100 ~ 999 之间 找 111 222 333 123 456 654 321 ...
for i in range(100,1000):
	gewei = int(str(i)[-1])
	shiwei = int(str(i)[-2])
	baiwei = int(str(i)[-3])
	if gewei == shiwei and shiwei == baiwei:
		print(i)
	elif shiwei == gewei + 1 and shiwei == baiwei -1:
		print(i)
	elif shiwei == gewei - 1 and shiwei == baiwei + 1:
		print(i)

# 百钱买百鸡
# 公鸡一个五块钱，母鸡一个三块钱，小鸡三个一块钱，现在要用一百块钱买一百只鸡，问公鸡、母鸡、小鸡各多少只？
for i in range(0,21):  #公鸡
	for j in range(0,34): #母鸡
		for k in range(0,100): #小鸡
			pass
			if (i + j + k == 100) and (5*i +3*j + 1/3*k == 100):
				print(i,j,k)

















