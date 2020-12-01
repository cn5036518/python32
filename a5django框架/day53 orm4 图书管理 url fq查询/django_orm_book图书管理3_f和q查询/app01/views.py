from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.models import Author
from app01.models import Publish
from app01.models import Book
import random


# Create your views here.

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
	# 		price=10+i,
	# 		PublishDate=f'2020-11-2{i}',
	# 		# "Column 'publishs_id' cannot be null")
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

	from django.db.models import F, Q

	#F查询
	# 1查询一下点赞数大于评论数的所有书籍
	# 方法1  普通
	books = Book.objects.all()
	books_list = []
	for book in books:
		if book.dianzan > book.comment:
			books_list.append(book)
	# print(books_list)
	for i in books_list:
		pass
		# print(i.title)
		# 读书11
		# 读书3

	# 方法2  F查询
	books = Book.objects.filter(dianzan__gt=F('comment'))
	# print(books.values('title'))
	#<QuerySet [{'title': '读书11'}, {'title': '读书3'}]>

	# 2所有书籍价格上调10块钱
	# 方法1 普通写法
	# books = Book.objects.all()
	# for book in books:
	# 	book.price += 10
	# 	print(book.price)
	# 	book.save()  #把记录更新到数据库

	# 方法2 F查询
	Book.objects.all().update(price=F('price')+10)
	# #支持四则运算

	# Q查询, 多条件查询的时候用的多, or查询
	# 1查询一下点赞数大于10或者评论数大于10的所有书籍
	book = Book.objects.filter(Q(dianzan__gt=10) | Q(comment__gt=10))
	#   #| -- or   & -- and  ~ -- not
	# print(book.values('title'))
	#<QuerySet [{'title': '读书6'}, {'title': '读书7'}]>

	# 2点赞数大于10或者评论数大于10的并且价格大于30的
	# 方法1
	book = Book.objects.filter(Q(dianzan__gt=10)|Q(comment__gt=10),price__gt=30)
	# print(book.values('title'))
	#<QuerySet [{'title': '读书6'}, {'title': '读书7'}]>

	# 方法2
	book = Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) &Q(price__gt=30))
	print(book.values('title'))




	return HttpResponse('ok')

from django.urls import reverse  # 别名解析

#FBV  基于函数
def books(request):
	# print(reverse('books'))
	# ##/books/  #reverse('别名')来反向解析别名对应的路径
	# print(reverse('add_book'))
	# # / add_book /  #/add_book/v1/
	# # print(reverse('edit_book'))   #报错
	# # Reverse	# for 'edit_book' with no arguments not found.1 pattern(s) tried: ['edit_book/(\\d+)/']
	#
	# print(reverse('edit_book',args=(3,)))
	# #/edit_book/3/
	# # 当url用的是无名分组参数时,reverse反向解析路径用args来传参
	#
	# print(reverse('del_book',kwargs={'book_id':3,}))
	#/del_book/3/
	# 当url用的是有名分组参数时,reverse反向解析路径用kwargs来传参

	book_obj = Book.objects.all()
	return render(request, 'books.html', {'book_obj': book_obj})

#CBV  基于类

def add_book(request):
	# 打开添加页面get
	# 提交数据post
	if request.method == 'GET':
		publish_obj = Publish.objects.all()  # 获取出版社
		author_obj = Author.objects.all()  # 获取作者
		return render(request, 'add_book.html', {'publish_obj': publish_obj, 'author_obj': author_obj})
	else:
		pass

from django.views import View

class AddBook(View):
	def get(self,request):
		publish_objs = Publish.objects.all()  # 获取出版社
		author_objs = Author.objects.all()  # 获取作者
		return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

	def post(self,request):
		authors = request.POST.getlist('authors')
# ['3', '4', '5']  #获取多选数据时,用getlist方法
#get只能获取最后一个数据
		print(authors)  #['元涛1', '元涛2']  ['1', '2']作者id
		# 如果前端option中没有写value属性,就会把<option>{{ author.name }}</option> 作者姓名传递过来
		# 如果前端option标签中写了value属性,就会把<option value="{{ author.id }}" 作者id传递过来

		data = request.POST.dict()
		# 注意:含有多选数据时,先提取多选数据,再使用dict,
		# 不然,dict会返回多选的最后一个结果值
		print(data)
		# {'title': '1', 'price': '2', 'PublishDate': '2020-11-30', 'publishs_id': '读书出版社2', 'authors': '2'}

		data.pop('authors')  #这个字段书籍表没有 需要删除
		print(data) #invalid literal for int() with base 10: '读书出版社2'  ##注意 这里的出版社保存到数据库,需要用id 而不是出版社名字
		# {'title': '1', 'price': '2', 'PublishDate': '2020-11-30', 'publishs_id': '读书出版社3'}

		#保存数据到数据库-书籍表  单表添加
		book_obj = Book.objects.create(
			**data
		)

		# 保存数据到数据库-书籍和作者关系表  多对多添加
		book_obj.authors.add(*authors)
		# book对象记录.关联属性字段.add(作者1id,作者2id)
		# *authors 这里的*在实参处,是解包

		# return redirect('/books/')  #原路径
		# return redirect(reverse(('books')))  #路径别名
		return redirect('books')   #推荐

	# redirect用别名
	#
	# ```python
	# # 两种写法都可以
	# # return redirect(reverse('books'))
	# return redirect('books')  # 直接写别名
	# ```


class EditBook(View):
	# 打开编辑页面get
	# 提交修改后的数据post
	def get(self,request,book_id):
		old_book_obj = Book.objects.get(id=book_id)
		publish_objs = Publish.objects.all()  #publish少了一个b
		author_objs = Author.objects.all()
		return render(request,'edit_book.html',
		              {'old_book_obj':old_book_obj,
		               'publish_objs':publish_objs,  #publish少了一个b
		               'author_objs':author_objs})

	def post(self,request,book_id):
		authors = request.POST.getlist('authors')
		# print(authors)  #['1', '2']

		data = request.POST.dict()
		print(data)
		# {'title': '读书11', 'price': '11.00', 'PublishDate': '2020-11-21', 'publishs_id': '3', 'authors': '2'}
		# 获取多选数据时,用getlist方法
		# get只能获取最后一个数据
		
		data.pop('authors')   #这个字段书籍表没有 需要删除
		print(data)
		# {'title': '读书11', 'price': '11.00', 'PublishDate': '2020-11-21', 'publishs_id': '3'}

		old_obj = Book.objects.filter(id=book_id)
		print(old_obj)  #queryset  <QuerySet [<Book: Book object>]>
		# 修改书籍表  get不支持update方法
		old_obj.update(
			# update返回值是受影响的条数,是个整数数字
			**data
		)

		# 修改书籍-作者关系表  多对多
		old_obj.first().authors.set(authors)  #参数是列表
		# old_obj 是queryset
		# old_obj.first()  是对象记录

		# obj = models.Book.objects.get(id=5)
		# obj.authors.set(['1','3'])
		# #clear + add  更新,先清空book_id为5的第三张表里的记录,
		# 再添加5 1和5 3记录

		return redirect('/books/')

	# redirect用别名
	#
	# ```python
	# # 两种写法都可以
	# # return redirect(reverse('books'))
	# return redirect('books')  # 直接写别名
	# ```


def del_book(request,book_id):
	Book.objects.get(id=book_id).delete()
	# Book.objects.filter(id=book_id).delete()
	return redirect('/books/')

# redirect用别名
#
# ```python
# # 两种写法都可以
# # return redirect(reverse('books'))
# return redirect('books')  #直接写别名
# ```













