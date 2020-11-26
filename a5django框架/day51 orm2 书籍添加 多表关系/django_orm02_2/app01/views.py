from django.shortcuts import render,HttpResponse

from app01 import models
from app01.models import Author
from app01.models import AuthorDetail
from app01.models import Publish
from app01.models import Book

# Create your views here.
def query(request):
# 增
# 一对一关系的添加
# 先创建作者详细信息表记录  先创建被关联表
# 	ret = AuthorDetail.objects.create(
# 		birthday='2000-12-12',
# 		telephone='122',
# 		addr='惠州2',
# 	)
#
# 	Author.objects.create(
# 		name='元涛2',
# 		age=18,
# 		# au_id=ret.id,  #如果用的是属性名称_id,那么值为关联记录的id值  方法1 推荐
# 		au=ret,#如果写属性名称来添加关系数据,那么值为关联记录的模型类对象  方法2
# 	)

# 一对多关系的添加
# 先创建出版社记录   一对多的一表  先创建被关联表
# 先手动通过navicat在Publish表新建一个数据
# 这里也可以在这里通过orm新增记录
# 	pub_obj = Publish.objects.get(id=1)
#
# 	Book.objects.create(
# 		title='白洁4',
# 		price=10,
# 		publishDate='1980-07-07',
# 		# 方法1
# 		# publishs=pub_obj,#如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
#
# 		# 方法2
# 		# publishs_id=1,#如果用的是属性名称_id,那么值为关联记录的id值
# 		publishs_id=pub_obj.id,  #方法3 推荐
# 	)

# 多对多关系数据的添加
# 	book_obj = Book.objects.get(title='白洁1')
# #DoesNotExist at /query/  Book matching query does not exist.
# # 如果 白洁5 不存在  会报错
# 	author1 = Author.objects.get(id=1)
# 	author2 = Author.objects.get(id=2)
# 
# 	book_obj.authors.add(author1,author2)
#这个会往多对多的关系表app01_book_authors新增2条数据






	return HttpResponse('ok')