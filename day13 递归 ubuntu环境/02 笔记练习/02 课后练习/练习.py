#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/9/27 11:22

def jiecheng(n):
	if n == 1:   #递归终止条件
		return 1
	return jiecheng(n-1) * n	

res = jiecheng(3)
print(res)  #6

# def jiecheng2(n):
# 	pass
#     if n == 5:
# 	    pass
#     return jiecheng2(n+1)





















































