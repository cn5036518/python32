#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/4 20:14

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm02.settings")
import django
django.setup()

from app01 import models
from app01.models import Book
#django外部脚本调用django环境来操作
# 批量创建100条数据到书籍表
#方法1
# obj_list = []
# for i in range(10):
# 	book_obj = Book(
# 		title=f'白洁{i}',
# 		price=i,
# 		publishDate='2020-11-11',
# 		publishs_id=1,
# 	)
# 	obj_list.append(book_obj)
# Book.objects.bulk_create(obj_list)

#方法2  推荐
for i in range(101,201):
	Book.objects.create(
		title=f'白洁{i}',
		price=i,
		publishDate='2020-11-11',
		publishs_id=1,
	)



















