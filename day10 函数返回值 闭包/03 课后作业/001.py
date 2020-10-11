#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:   2020/10/11 下午3:22

def func(filename, str1, str2):
    with open(filename, mode="r+", encoding="utf-8") as fp:
        strvar = fp.read()
        print(strvar)
        # 123456
        # 654321
        res = strvar.replace(str1, str2)

    with open(filename, mode="w+", encoding="utf-8") as fp:
        fp.write(res)


func("ceshi2.py", "654321", "0")