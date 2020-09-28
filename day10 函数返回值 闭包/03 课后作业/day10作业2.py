#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@time:  2020/9/23 21:04


# ### 闭包
#下面代码成立么?如果不成立为什么报错?怎么解决?
#1
# a = 2
# def wrapper():
#	print(a)
# wrapper()

#2
# a = 2
# def wrapper():
#     a += 1
#     print(a)
# wrapper()

#3
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()

#4
# def wrapper():
#      a = 1
#      def inner():
#          print(a)
#      inner()
# wrapper()

#5
# def wrapper():
#      a = 1
#      def inner():
#          a += 1
#          print(a)
#      inner()
# wrapper()

#6
# def wrapper():
#     a = 1
#     def inner():
#         nonlocal a
#         a += 1
#         print(a)
#     inner()
# wrapper()

#下面代码成立么?如果不成立为什么报错?怎么解决?
#1
# a = 2
# def wrapper():
# 	print(a)  #2
# wrapper()  #可以

#2
# a = 2
# def wrapper():
# 	global a  #加这行
# 	a += 1
# 	print(a)
# wrapper()

#3
# a = 2
# def wrapper():
#     global a
#     a += 1
#     print(a)
# wrapper()  #可以

#4  嵌套函数
# def wrapper():
#      a = 1
#      def inner():
#          print(a)  #1
#      inner()
# wrapper()

#5 闭包
# def wrapper():
# 	a = 1
# 	def inner():
# 		nonlocal a  #加这行
# 		a += 1
# 		print(a)  #2
# 	inner()
# wrapper()

#6
def wrapper():
    a = 1
    def inner():
        nonlocal a
        a += 1
        print(a) #2
    inner()
wrapper()



































