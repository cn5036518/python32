from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from app01 import  models
from app01.models import  Author
from app01.models import  Publish
from app01.models import  Book
import random

def query(request):
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
	# 批量插入9条书籍数据
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
# get只能获取一条数据
	# 	book_obj.authors.add(author1,author2)
	return HttpResponse('ok')

def books(request):
	books_obj = Book.objects.all()
	return  render(request,'books.html',{'books_obj':books_obj})

def add_book(request):
	# 打开添加书籍页面-get
	# 填入内容后提交-post
	if request.method == 'GET':
		publish_obj = Publish.objects.all()
		return  render(request,'add_book.html',{'publish_obj':publish_obj})
	else: #POST
		data = request.POST.dict()
		# print(data)  #{'title': '1', 'price': '1', 'pub_date': '2020-11-29', 'publishs': '读书出版社1'}
		# 书籍表需要添加出版社id字段,而前端页面获取的是出版社名字
		# 从字典中删除出版社名字键值对,添加出版社id字段
		# 出版社id通过出版社名字获取
		publish_name = data.pop('publishs')
		# print(data)  #{'title': '1', 'price': '1', 'pub_date': '2020-11-29'}
		# print(publish_name)  #读书出版社1

		# 出版社id通过出版社名字获取
		publish_obj = Publish.objects.get(name=publish_name)
		# print(publish_obj,type(publish_obj))
		# print(publish_obj.id)
		data['publishs_id'] = publish_obj.id
		# print(data)

		# 新增记录保存到数据库
		Book.objects.create(
			**data
		)

		return redirect('/books/')

def edit_book(request,book_id):
	pass
	# 打开编辑书籍页面-get
	# 获取数据库的数据.填入到前端页面的输入框  value属性
	# 填入内容后提交-post
	if request.method == 'GET':
		book_obj = Book.objects.get(id=book_id)
		publish_obj = Publish.objects.all()
		return render(request,'edit_book.html',{'book_obj':book_obj,'publish_obj':publish_obj})
	else: # POST
		data = request.POST.dict()
		# print(data)  #{'title': '1', 'price': '1', 'pub_date': '2020-11-29', 'publishs': '读书出版社1'}
		# 书籍表需要添加出版社id字段,而前端页面获取的是出版社名字
		# 从字典中删除出版社名字键值对,添加出版社id字段
		# 出版社id通过出版社名字获取
		publish_name = data.pop('publishs')
		# print(data)  #{'title': '1', 'price': '1', 'pub_date': '2020-11-29'}
		# print(publish_name)  #读书出版社1

		# 出版社id通过出版社名字获取
		publish_obj = Publish.objects.get(name=publish_name)
		# print(publish_obj,type(publish_obj))
		# print(publish_obj.id)
		data['publishs_id'] = publish_obj.id
		# print(data)

		# 保存修改到数据库
		# get不支持update方法
		Book.objects.filter(id=book_id).update(
			**data
		)

		return redirect('/books/')


def del_book(request,book_id):
	Book.objects.filter(id=book_id).delete()
	return  redirect('/books/')





















