from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
from app01 import models


def books(request):

	book_list = models.Book.objects.all()

	return render(request, 'books.html', {'book_list': book_list})



def add_book(request):
	if request.method == 'GET':

		return render(request, 'add_book.html')
	else:
		# dict()将querydict类型数据转化为普通字典类型数据
		data = request.POST.dict()

		print(data)
		# title = request.POST.get('title')
		# price = request.POST.get('price')
		# pub_date = request.POST.get('pub_date')
		# publish = request.POST.get('publish')

		# 关键字传参可以通过**打伞的形式来传入
		ret = models.Book.objects.create(
			**data
		)


		return redirect('/books/')


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

