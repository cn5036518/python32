from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import  models
from app01.models import  Author
from app01.models import  Publish
from app01.models import  Book
import random

def query(request):
	pass
# 1一对多
# 必须先给Publish表添加3条数据才行
#  出版社表
# 批量插入3条出版社数据
# 	for i in range(1,4):
# 		Publish.objects.create(
# 			name=f'读书出版社{i}',
# 			city=f'北京{i}',
# 		)

# 书籍表
	# 批量插入10条书籍数据
	# for i in range(1,10):
	# 	Book.objects.create(
	# 		title=f'读书{i}',
	# 		price=10 + i,
	# 		pub_date=f'2020-11-2{i}',
	# 		#"Column 'publishs_id' cannot be null")
	# 		publishs_id=random.randrange(1,4),
	# 	)


# 2多对多
# 在第三个关系表添加2个记录  1本书添加2个作者
# 读书0==>作者1 作者2

# 在第三个关系表添加2个记录  1本书添加2个作者
# 读书1==>作者1 作者2
	#  作者表
	# 批量插入2条作者数据
	# for i in range(1,3):
	# 	Author.objects.create(
	# 		name=f'元涛{i}',
	# 		age=18+i,
	# 	)

	# author1 = Author.objects.get(id=1)
	# author2 = Author.objects.get(id=2)
	#
	# for i in range(1,3):
	# 	book_obj = Book.objects.get(title=f'读书{i}')
	# 	book_obj.authors.add(author1,author2)
	return HttpResponse('ok')

def books(request):
	books_obj = Book.objects.all()
	return  render(request,'books.html',{'books_obj':books_obj})




























