#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/1 15:58

# django外部脚本调用django环境来操作

# 脱离django,单独运行的文件就叫做外部脚本
# (可以直接在pycharm中右键-run 运行)

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_外部脚本调用django环境.settings")
#上面行来自manage.py文件
import django
django.setup()

from app01 import models

ret = models.Book.objects.all()
print(ret)















