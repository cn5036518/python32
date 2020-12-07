from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from app01.models import UserInfo
from app01.models import Book
from app01.models import Menu
# Create your views here.
from django.urls import reverse  # 别名解析
from django.utils.decorators import method_decorator

# 登录认证装饰器--认证登录状态
# 定义装饰器函数  (可以用中间件来优化)
# def login_check(f):
# 	def inner(request,*args,**kwargs):
# 		status = request.session.get('is_login')
# 		if status == True:
# 			# 登录状态认证不通过,允许查看相关页面
# 			ret = f(request,*args,**kwargs)
# 			return ret
# 		else: #登录状态认证不通过,重定向对登录页面
# 			return redirect('login')
# 	return inner

def register(request):
	if request.method == 'GET':
		return render(request,'register.html')
	else:
		user_data = request.POST.dict()
		print(user_data)
		# {'csrfmiddlewaretoken': 'b7ke5USFaAECcBSbxsUq44As9TUCrd2gP4JLeTZwgbpWCXjVfsLA2jL4GP1fiiev', 'username':
		# 	'root', 'password': '123', 'confirm_password': '123', 'phone_number': '13501145281', 'email': '2@qq.com'
		#  }
		user_data.pop('confirm_password')
		user_data.pop('csrfmiddlewaretoken')
		#上述2个字段,数据库的用户表没有,需要删除
	    #否则,无法保存到数据库
		# todo 要校验数据的格式等

		#把注册页面的输入框内容保存到数据库
		UserInfo.objects.create(
			**user_data
		)
		return redirect('login')
		# return HttpResponse('ok')


def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		uname = request.POST.get('username')
		pwd =request.POST.get('password')
		# 获取用户在登录输入框的内容

		res = UserInfo.objects.filter(username=uname,password=pwd)
		# obj_list = Book.objects.filter(id=10, price=15)  #逗号连接的查询条件就是and的关系
		# 逗号是and
		print(res)
		#ret是queryset
		if res.exists():
			# < QuerySet[ < UserInfo: UserInfo object >] >			#
			# exists(): queryset类型的数据来调用，如果QuerySet包含数据，就返回True，否则返回False
			## 登录成功
			request.session['is_login'] = True
			#设置session的键值对 记录登录状态
		# django的session操作
			# 设置值 (新增和修改)
			# request.session['k1'] = 123  # 键相同的还是修改
			request.session['user_id'] = res.first().id  #记录用户id
			# < 8 > first(): queryset类型的数据来调用，返回第一条记录
			# Book.objects.all()[0] = Book.objects.all().first()，
		# 得到的都是model对象，不是queryset
			request.session['username'] = uname  #记录用户名
			request.session['avatar'] = res.first().avatar  #记录用户名
			print(request.session['avatar'] )

		# 查询该用户的菜单数据  正向查询 关联属性字段
			menu_list = res.first().menus.all().values('id','title','url','icon')
			# < 11 > values(*field): 用的比较多，queryset类型的数据来调用，返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系列
			# model的实例化对象，而是一个可迭代的字典序列, 只要是返回的queryset类型，就可以继续链式调用queryset类型的其他的查找方法，其他方法也是一样的。
			#这里手动把用户对应的菜单和关系添加到数据库
			print(menu_list)
			# < QuerySet[{'id': 1, 'title': '图书管理', 'url': '/books/', 'icon': 'fa fa-book'},
			#            {'id': 2, 'title': '作者管理', 'url': '/authors/', 'icon': 'fa fa-users'},
			#            {'id': 3, 'title': '出版社管理', 'url': '/publishs/', 'icon': 'fa fa-building'}] >
			request.session['menu_data'] = list(menu_list)
			#记录用户对应的菜单
			return  redirect('books')
		else:  #<QuerySet []>
			## 登录失败 (密码校验不通过)
			return redirect('login')
		# return HttpResponse('ok')

# @login_check
def logout(request):
	request.session.flush()  #删除所有session数据
	return redirect('login')

# @login_check
# #浏览器会自动保存sessionid  需要清除缓存看效果
# def books(request):
# 	print(reverse('books'))  #/books/  #reverse('别名')来反向解析别名对应的路径
# 	print(reverse('add_book'))  #/add_book/  #/add_book/v1/
# 	print(reverse('edit_book',args=(3, )))  # /edit_book/2/
# 	# print(reverse('del_book',args=(3, ))) # 当url用的是无名分组参数时,reverse反向解析路径用args来传参
# 	print(reverse('del_book', kwargs={'book_id': 3, }))  #当url用的是有名分组参数时,reverse反向解析路径用kwargs来传参
# 	book_objs = models.Book.objects.all()
#
# 	return render(request, 'books.html', {'book_objs': book_objs})

from app01.utils.page import Pagenation

# @login_check
def books(request):
	print(request.GET)
	# < QueryDict: {'page': ['11']} >
	# 获取page.py中的s = f'<li><a href="?page={i}">{i}</a></li>'
	# 即url上的?后面的参数
	current_page = request.GET.get('page')
	print(current_page)  #11 获取当前页码

	try:
		current_page = int(current_page)
	except:
		# 没有page参数或者不是数字字符串
		current_page = 1

	all_book_objs = Book.objects.all()
	total_count = all_book_objs.count()  # 总数据量
	page_obj = Pagenation(current_page,total_count) #新建对象

	book_objs = Book.objects.all()[page_obj.page_data_start:page_obj.end_data_start]

	# book_objs = models.Book.objects.all()[10:20] # 2
	# book_objs = models.Book.objects.all()[20:30] # 3
	return render(request,'books.html',
	              {'book_objs':book_objs,'page_obj':page_obj})


from django.views import View

class AddBook(View):
	# 给类中的方法加装饰器 day48 typora  方式1

	# @method_decorator(login_check)
	def get(self,request):
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

	# @method_decorator(login_check)
	def post(self,request):
		# request.POST.get('authors')
		authors = request.POST.getlist('authors')  # ['3', '4', '5']  #获取多选数据时,用getlist方法
		# print(request.POST)
		# print(authors2)
		data = request.POST.dict()  #注意:含有多选数据时,先提取多选数据,在使用dict,不然,dict会返回多选的最后一个结果值
		# print(data)
		data.pop('authors')  # ['3', '4']
		# print(authors)
		book_obj = models.Book.objects.create(
			**data
			# publishs=模型类对象,
			# publishs_id=3,
		)

		book_obj.authors.add(*authors) # ['4', '5']

		# return redirect(reverse('books',args=(1,2,3,)))
		# return redirect(reverse('books',kwargs={'book_id':1,}))
		return redirect('books') #/books/



class EditBook(View):

	# @method_decorator(login_check)
	def get(self,request,book_id):
		old_book_obj = models.Book.objects.get(id=book_id)
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		# print(reverse('edit_book', args=(book_id, )))
		return render(request, 'edit_book.html', {'old_book_obj': old_book_obj, "publish_objs": publish_objs, 'author_objs': author_objs})

	# @method_decorator(login_check)
	def post(self,request, book_id):

		authors = request.POST.getlist('authors')  # [2, 3]
		data = request.POST.dict()
		data.pop('authors')
		data.pop('csrfmiddlewaretoken')
# 		FieldDoesNotExist at /edit_book/143/
# Book has no field named 'csrfmiddlewaretoken'
		old_obj = models.Book.objects.filter(id=book_id)
		old_obj.update(  # update返回值是受影响的条数,是个整数数字
			**data
		)

		old_obj.first().authors.set(authors)

		return redirect('books')

# @login_check
def del_book(request,book_id):
	models.Book.objects.get(id=book_id).delete()  # 默认级联删除
	return redirect('books')


# @login_check
def ajax_del_book(request,book_id):

	try:
		models.Book.objects.get(id=book_id).delete()
		# 默认级联删除
		res_data = {'status': 1, 'msg': '删除成功!'}
	except:
		res_data = {'status': 0, 'msg': '删除失败!'}

	return JsonResponse(res_data)

# @login_check
def authors(request):
	return  render(request,'authors.html')

# @login_check
def publishs(request):
	return  render(request,'publishs.html')


def upload(request):
	if request.method == 'GET':
		return render(request,'upload.html')
	else:
		pass
		return HttpResponse('ok')




























