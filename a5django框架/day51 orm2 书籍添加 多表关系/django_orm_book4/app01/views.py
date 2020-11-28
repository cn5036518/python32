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












