from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
from app01 import models
# 这里从别的应用导入的models,一般都是从自己的应用导入models


def books(request):
	# 展示数据 从数据库读取数据,展示到页面
	book_list = models.Book.objects.all()
	# 页面编辑后,数据库数据修改了,这里读取数据表后,显示修改后的数据到页面
	# print(book_list)
	# < QuerySet[ < Book: 金瓶梅12 >, < Book: 健身 >, < Book: pytHon少年闰土1 >, < Book: Python少年闰土2 >, < Book: 少年
	# 闰土3 >, < Book: 少年闰土4 >, < Book: 少年闰土5 >, < Book: 读书1 >] >
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
	print(book_id)
	# 这里获取的是urls中\d+ 匹配到的值
	#   url(r'^edit_book/(\d+)/', book_view.edit_book),
	# 点击编辑按钮后,打开的页面是get
	# 编辑按钮获取的id (href="/edit_book/{{ book.id }})-->urls中的\d+ -->book_id

	# 把数据库获取到的数据,发送填充到页面
	# 修改内容后,保存提交是post

	if request.method == 'GET':
		old_obj = models.Book.objects.get(id=book_id)
		# 根据id从数据库获取数据
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

