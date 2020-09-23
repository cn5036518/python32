#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/23 23:09


# 2.定义函数:传入一个参数n，返回n的阶乘(5! = 5*4*3*2*1)
def func(num):
	factorial = 1
	for i in range(1, num + 1):
		factorial *=  i  #
	print("%d 的阶乘为 %d" % (num, factorial))

func(3)
print('-----------------------2')


















