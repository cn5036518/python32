from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.
from django.utils.decorators import method_decorator

from django.views import View


from django.urls import reverse  # 别名解析

# 登录认证装饰器
def login_check(f):

	def inner(request, *args, **kwargs):
		status = request.session.get('is_login')
		if status == True:
			ret = f(request, *args, **kwargs)
			return ret
		else:
			return redirect('login')
	return inner

def login(request):
	if request.method == 'GET':
		return render(request, 'templates/login.html')
	else:
		uname = request.POST.get('username')
		pwd = request.POST.get('password')

		res = models.UserInfo.objects.filter(username=uname, password=pwd)
		if res.exists():
			## 登录成功
			request.session['is_login'] = True
			request.session['user_id'] = res.first().id
			request.session['username'] = uname

			# 注入菜单数据
			menu_list = res.first().menus.all().values('id', 'title', 'url', 'icon')

			request.session['menu_data'] = list(menu_list)

			return redirect('books')
		else:
			return redirect('login')
		
def register(request):
	if request.method == 'GET':
		return render(request, 'templates/register.html')
	else:
		user_data = request.POST.dict()
		print(user_data)
		# {'csrfmiddlewaretoken': 'Id8TbGJwdp2jOyD0DfZpFlYFbcFP7JGFfZR4pVgIEjxbRLF7QlSy3KQ6IqaxRkJO', 'username': 'root',
		#  'password': '123', 'confirm_password': '123', 'phone_number': '13501145287', 'email': '2@qq.com'
		user_data.pop('confirm_password')
		user_data.pop('csrfmiddlewaretoken')
		#如果不执行上面行,会提示'csrfmiddlewaretoken' is an invalid keyword argument for this function
		# todo 要校验数据的格式等

		models.UserInfo.objects.create(
			**user_data
		)
		return redirect('login')

@login_check
def logout(request):

	request.session.flush()
	return redirect('login')

@login_check
def books(request):
	print(reverse('books'))  #/books/  #reverse('别名')来反向解析别名对应的路径
	print(reverse('add_book'))  #/add_book/  #/add_book/v1/
	print(reverse('edit_book',args=(3, )))  # /edit_book/2/
	# print(reverse('del_book',args=(3, ))) # 当url用的是无名分组参数时,reverse反向解析路径用args来传参
	print(reverse('del_book', kwargs={'book_id': 3, }))  #当url用的是有名分组参数时,reverse反向解析路径用kwargs来传参
	book_objs = models.Book.objects.all()

	return render(request, 'books.html', {'book_objs': book_objs})


# from django.views import View


class AddBook(View):
	# 给类中的方法加装饰器 day48 typora
	@method_decorator(login_check)
	def get(self,request):
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

	@method_decorator(login_check)
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
	@method_decorator(login_check)
	def get(self,request,book_id):
		old_book_obj = models.Book.objects.get(id=book_id)
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		# print(reverse('edit_book', args=(book_id, )))
		return render(request, 'edit_book.html', {'old_book_obj': old_book_obj, "publish_objs": publish_objs, 'author_objs': author_objs})

	@method_decorator(login_check)
	def post(self,request, book_id):

		authors = request.POST.getlist('authors')  # [2, 3]
		data = request.POST.dict()
		data.pop('authors')
		old_obj = models.Book.objects.filter(id=book_id)
		old_obj.update(  # update返回值是受影响的条数,是个整数数字
			**data
		)

		old_obj.first().authors.set(authors)

		return redirect('books')

@login_check
def del_book(request,book_id):
	models.Book.objects.get(id=book_id).delete()  # 默认级联删除
	return redirect('books')


@login_check
def ajax_del_book(request,book_id):

	try:
		models.Book.objects.get(id=book_id).delete()
		# 默认级联删除
		res_data = {'status': 1, 'msg': '删除成功!'}
	except:
		res_data = {'status': 0, 'msg': '删除失败!'}

	return JsonResponse(res_data)

@login_check
def authors(request):
	return render(request, 'authors.html')

@login_check
def publishs(request):
	return render(request, 'publishs.html')









