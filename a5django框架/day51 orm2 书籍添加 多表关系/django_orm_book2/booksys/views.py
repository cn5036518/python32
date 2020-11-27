from django.shortcuts import render

# Create your views here.
from  app01 import models
from  app01.models import Book
# 这里从别的应用导入的models,一般都是从自己的应用导入models

def books(request):
	book_list = Book.objects.all()
	# 展示数据 从数据库读取数据,展示到页面
	print(book_list)
	# < QuerySet[ < Book: 金瓶梅12 >, < Book: 健身 >, < Book: pytHon少年闰土1 >, < Book: Python少年闰土2 >, < Book: 少年
	# 闰土3 >, < Book: 少年闰土4 >, < Book: 少年闰土5 >, < Book: 读书1 >] >
	return render(request,'books.html',{'book_list':book_list})
