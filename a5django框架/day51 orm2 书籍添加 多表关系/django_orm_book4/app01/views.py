from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models
from app01.models import Book

def query(request):
	# 单条插入数据
	# new_book = Book.objects.create(
	# 	title='读书1',
	# 	price=9,
	# 	pub_date='2020-01-01',
	# 	publish='读书出版社',
	# )

	# 批量插入数据
	# for i in range(5):
	# 	Book.objects.create(
	# 		title=f'读书{i}',
	# 		price=10+i,
	# 		pub_date=f'2020-02-1{i}',
	# 		publish='读书出版社',
	# 	)
	
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
		return render(request,'add_book.html')
	else:
		data = request.POST.dict()
		# print(data)
		# {'title': '1', 'price': '2', 'pub_date': '2020-11-14', 'publish': '3'}

		Book.objects.create(
			**data
			# ** 在形参处是打包  关键字-->字典
			# ** 在实参处是解包打散  字典-->关键字  title=title
			# 这里是实参
		)
		return redirect('/books/')
	
def edit_book(request,book_id):
	#1 打开编辑页面  get
	# 获取数据库的数据.通过view发送到前端页面的输入框
	#2 提交数据到数据库保存  post
	if request.method == 'GET':
		old_obj = Book.objects.get(id=book_id)
		print(old_obj)  #对象记录
		# return HttpResponse('ok')
		return render(request,'edit_book.html',{'old_obj':old_obj})
	else: #post
		data = request.POST.dict()
		print(data)  #{'title': '读书1223', 'price': '9.00', 'pub_date': '2020-01-01', 'publish': '读书出版社'}

		Book.objects.filter(id=book_id).update(  #修订记录
			**data
			# ** 在形参处是打包  关键字-->字典
			# ** 在实参处是解包打散  字典-->关键字  title=title
			# 这里是实参
		)
		return  redirect('/books/')
		# return HttpResponse('ok')

def del_book(request,book_id):
	Book.objects.filter(id=book_id).delete()
	return redirect('/books/')























