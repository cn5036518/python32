from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
from app01 import models
# 这里从别的应用导入的models,一般都是从自己的应用导入models


def books(request):

	book_list = models.Book.objects.all()

	return render(request, 'books.html', {'book_list': book_list})



def add_book(request):
	if request.method == 'GET':
		return render(request, 'add_book.html')
	# 打开添加页面,是get请求
	else:  #post
		# 把输入框的值获取放到 QueryDict  关键点1
		# dict()将querydict类型数据转化为普通字典类型数据
		data = request.POST.dict()
		print(data)
		# 方法1
		# title = request.POST.get('title')
		# price = request.POST.get('price')
		# pub_date = request.POST.get('pub_date')
		# publish = request.POST.get('publish')
		#
		# #把页面输入框获取的数据,往库里新增一条数据
		# ret = Book.objects.create(
		# 	title=title,
		# 	price=price,
		# 	pub_date=pub_date,
		# 	publish=publish,
		# )

		# 方法2  推荐  更简洁
		# 把页面输入框获取的数据,往库里新增一条数据
		# 关键字传参可以通过**打散的形式来传入
		ret = models.Book.objects.create(
			**data
			# ** 在形参处是打包  关键字-->字典
			# ** 在实参处是解包打散  字典-->关键字  title=title
			# 这里是实参
		)
		return redirect('/books/')
# 提交完毕后,返回图书展示列表

def edit_book(request, book_id):

	if request.method == 'GET':
		old_obj = models.Book.objects.get(id=book_id)
		return render(request,'edit_book.html', {'old_obj': old_obj})

	else:
		data = request.POST.dict()

		models.Book.objects.filter(id=book_id).update(
			**data
		)
		return redirect('/books/')


def del_book(request, book_id):
	models.Book.objects.get(id=book_id).delete()

	return redirect('/books/')

