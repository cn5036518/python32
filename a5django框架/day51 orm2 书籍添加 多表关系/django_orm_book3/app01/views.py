from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models  #导入数据库models
from app01.models import Book

def books(request):
# 展示数据 从数据库读取数据,展示到页面
	book_list = Book.objects.filter()
	# book_list = Book.objects.all()  #和上面行等效
# 页面编辑后,数据库数据修改了,这里读取数据表后,显示修改后的数据到页面
# 	print(book_list)
# <QuerySet [<Book: 金瓶梅12>, <Book: 健身>, <Book: pytHon少年闰土1>, <Book: Python少年闰土22>, <Book: 少年
# 闰土5>, <Book: 读书1>, <Book: 读书2>, <Book: 健身>]>

	# return HttpResponse('ok')
	return render(request,'books.html',{'book_list':book_list})

def add_book(request):
	# 打开添加页面get
	# 输入内容提交数据是post
	if request.method == 'GET':
		return render(request,'add_book.html')
	else:
	# 1 获取前端页面输入框输入的内容
		data = request.POST.dict()
		print(data)  #通过前端页面的input标签的name属性获取输入框的输入内容
		# {'title': '1', 'price': '2', 'pub_date': '2020-11-28', "'publish": '3'}

	# 2 把输入框的内容存入数据库
		Book.objects.create(
			**data
			# **用在实参处，是解包的意思，把字典转成title=title的关键字
		)
		return redirect('/books/')

def edit_book(request,book_id):
# 打开添加页面get
#     1 把数据从数据库查询到后，传递给前端页面的输入框，作为编辑页面，输入框的默认值
# 在输入框，输入内容提交数据是post
	if request.method == 'GET':
		old_obj = Book.objects.get(id=book_id)
		# print(old_obj)  #对象记录
		# return HttpResponse('ok')
		return render(request,'edit_book.html',{'old_obj':old_obj})
	else:
		# 这里和添加页面的逻辑是一样的
		# 1 获取前端页面输入框输入的内容
		data = request.POST.dict()
		print(data)  # 通过前端页面的input标签的name属性获取输入框的输入内容
		# {'title': '1', 'price': '2', 'pub_date': '2020-11-28', "'publish": '3'}

		# 2 把输入框修改后的内容存入数据库
		Book.objects.filter(id=book_id).update(
			**data
			# **用在实参处，是解包的意思，把字典转成title=title的关键字
		)

		return redirect('/books/')

def del_book(request,book_id):
	Book.objects.get(id=book_id).delete()
	return redirect('/books/')




















