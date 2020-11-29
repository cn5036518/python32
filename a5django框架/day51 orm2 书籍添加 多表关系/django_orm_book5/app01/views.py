from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models
from app01.models import Book
from app01.models import Publish
from app01.models import Author
import random

def query(request):
	# 单条插入数据
	# new_book = Book.objects.create(
	# 	title='读书1',
	# 	price=9,
	# 	pub_date='2020-01-01',
	# 	publish='读书出版社',
	# )

	# 一对多
	# pub_id = Publish.objects.all().values('id')
	# print(pub_id) #<QuerySet [{'id': 1}, {'id': 2}]>
	# print(pub_id[0])  #{'id': 1}
	# print(pub_id[0].dict())

	# 批量插入数据
	# for i in range(10):
	# 	Book.objects.create(
	# 		title=f'读书{i}',
	# 		price=10+i,
	# 		pub_date=f'2020-02-1{i}',
	# 		publishs_id=random.randrange(1,3)
	# 		# publish='读书出版社',
	# 	)

	# 多对多
	# book_obj = Book.objects.get(title='读书0')
	# author1 = Author.objects.get(id=1)
	# author2 = Author.objects.get(id=2)
	#
	# book_obj.authors.add(author1,author2)
	# 在第三个关系表添加2个记录  1本书添加2个作者
	# 读书0==>作者1 作者2

	# book_obj = Book.objects.get(title='读书1')
	# author1 = Author.objects.get(id=1)
	# author2 = Author.objects.get(id=2)
	#
	# book_obj.authors.add(author1,author2)
	# 在第三个关系表添加2个记录  1本书添加2个作者
	# 读书1==>作者1 作者2


	return HttpResponse('ok')

def books(request):
	#获取数据库的数据,给到前端页面展示
	book_list = Book.objects.all()
	# print(book_list)
	# < QuerySet[ < Book: 读书1 >, < Book: 读书0 >, < Book: 读书1 >, < Book: 读书2 >, < Book: 读书3 >, < Book: 读书4 >] >
	# return HttpResponse('ok')
	return render(request,'books.html',{'book_list':book_list})

def add_book(request):
	#1 打开添加页面  get
	#2 提交数据到数据库保存  post
	if request.method == 'GET':
		pub_obj = Publish.objects.all()   #获取所有出版社
		author_obj = Author.objects.all()  #获取所有作者
		return render(request,'add_book.html',{'pub_obj':pub_obj,'author_obj':author_obj})
	else:
		data = request.POST.dict()
		print(data)
		# {'title': '1', 'price': '2', 'pub_date': '2020-11-14', 'publish': '3'}
		#{'title': '健身2', 'price': '2', 'pub_date': '2020-11-15', 'publishs': '健身出版社'}  多表 一对多
		#{'title': '11', 'price': '11', 'pub_date': '2020-11-01', 'publishs': '读书出版社', 'authors': '元涛1'}  多表 多对多
		# 前端页面的添加书籍窗口,出版社这个单选下拉框,选择的是出版社的名字,而书籍数据表存的是publishs_id

		name1 = data.pop('publishs')   #pop后面是() 而不是[]
		author_name = data.pop('authors')
		print(data)  #{'title': '1', 'price': '2', 'pub_date': '2020-11-01'}
		#{'title': '3', 'price': '3', 'pub_date': '2020-11-01'}
		# # 
		# # 根据出版社名字,查询出版社的id
		pub_obj = Publish.objects.get(name=name1)  #获取指定的出版社对象记录
		# print(pub_obj)

		# 根据作者的名字,查询作者的对象记录--id
		# author_obj = Author.objects.get(name=author_name)
		# #获取指定一个的作者对象记录
		# print(author_obj)

		Book.objects.create(
			**data,
			publishs_id = pub_obj.id  #方法1  推荐
			# publishs= pub_obj  #方法2
			# ** 在形参处是打包  关键字-->字典
			# ** 在实参处是解包打散  字典-->关键字  title=title
			# 这里是实参
		)
		#
		# print(data.get('title'),'---------2')
		book_obj = Book.objects.get(title=data['title'])
		# print(book_obj,'------------3')

		author_list = request.POST.getlist('authors')
		# # 这里的'authors'html文件中的name属性
		# # 获取多选下拉菜单的作者名称
		# #获取指定一个或者多个的作者对象记录
		print(author_list)  #['元涛1', '元涛2']
		for i in author_list:
			author_obj = Author.objects.get(name=i)
			book_obj.authors.add(author_obj)
			# 往第三个关系表添加记录

		return redirect('/books/')
	
def edit_book(request,book_id):
	#1 打开编辑页面  get
	# 获取数据库的数据.通过view发送到前端页面的输入框
	#2 提交数据到数据库保存  post
	if request.method == 'GET':
		old_obj = Book.objects.get(id=book_id)  #获取指定的书籍对象记录
		pub_obj = Publish.objects.all()   #获取所有的出版社对象记录
		author_obj = Author.objects.all()  # 获取所有作者
		# print(old_obj)  #对象记录
		# return HttpResponse('ok')
		return render(request,'edit_book.html',{'old_obj':old_obj,'pub_obj':pub_obj,'author_obj':author_obj})
	else: #post
		data = request.POST.dict()
		print(data)  #{'title': '读书1223', 'price': '9.00', 'pub_date': '2020-01-01', 'publish': '读书出版社'}   单表
		# {'title': '读书0', 'price': '10.00', 'pub_date': '2020-02-10', 'publishs': '健身出版社'}   一对多
		# {'title': '读书01', 'price': '10.00', 'pub_date': '2020-02-10'}  一对多 下拉单选
		# {'title': '12', 'price': '12.00', 'pub_date': '2020-11-29', 'publishs': '读书出版社', 'authors': '元涛1'}

		name1 = data['publishs']
		print(name1)  #健身出版社
		# #
		data.pop('publishs')  #将字典的中的出版社名字删除  因为书籍表中的字段是出版社id 而不是出版社名字  关键点
		print(data)  #{'title': '读书0', 'price': '10.00', 'pub_date': '2020-02-10'}

		data.pop('authors')
		print(data)  #{'title': '12', 'price': '12.00', 'pub_date': '2020-11-29'}
		#
		pub_obj = Publish.objects.get(name=name1)
		print(pub_obj)  #Publish object
		# # 从出版社表中获取到名字是 健身出版社 的对象记录
		#
		Book.objects.filter(id=book_id).update(  #修订记录
			**data,
			publishs_id=pub_obj.id  # 方法1  推荐
		# publishs= pub_obj  #方法2
		# ** 在形参处是打包  关键字-->字典
		# ** 在实参处是解包打散  字典-->关键字  title=title
		# 这里是实参
		)

		# print(data.get('title'),'---------2')
		book_obj = Book.objects.get(title=data['title'])
		# print(book_obj,'------------3')

		author_list = request.POST.getlist('authors')
		# # 这里的'authors'html文件中的name属性
		# # 获取多选下拉菜单的作者名称
		# #获取指定一个或者多个的作者对象记录
		print(author_list)  #['元涛1', '元涛2']
		for i in author_list:
			author_obj = Author.objects.get(name=i)
			book_obj.authors.add(author_obj)
			# 往第三个关系表添加记录
		
		return  redirect('/books/')
		# return HttpResponse('ok')

def del_book(request,book_id):
	Book.objects.filter(id=book_id).delete()
	return redirect('/books/')























