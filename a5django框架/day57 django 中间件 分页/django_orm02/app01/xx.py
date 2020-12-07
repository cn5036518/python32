


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm02.settings")
import django
django.setup()


from app01 import models

#django外部脚本调用django环境来操作
# 批量创建100条数据到书籍表
obj_lsit = []
for i in range(100):
	book_obj = models.Book(
		title=f'白洁{i}',
		price=i,
		publishDate='2020-11-11',
		publishs_id=1,
	)
	obj_lsit.append(book_obj)

models.Book.objects.bulk_create(obj_lsit)
