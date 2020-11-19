#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/19 17:33

import  sys
from wsgi import run
from models import  create_model

# python manage.py xx xx2  命令行输入
# 执行py文件时,后面携带的参数,
#可以通过py文件中的sys模块的sys.argv这个属性拿到,
#是个列表,列表第一项是文件名称,第二项之后,都是携带的参数

commands = sys.argv  # xx xx2
# ['manage.py', 'xx', 'oo']

# 运行项目的指令: python manage.py runserver
# 数据库同步指令: python manage.py migrate  建表
#http://127.0.0.1:8001/index 页面输入访问
a1 = commands[1]
if a1 == 'runserver':
	run()
elif a1 == 'migrate':
	create_model()
















