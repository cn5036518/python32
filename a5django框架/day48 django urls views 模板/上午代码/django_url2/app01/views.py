from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
	return HttpResponse('首页')

def index(request):
	return HttpResponse('ok')

def index2(request):
	return  HttpResponse('index2')

def books(request,y):
	print(y)   # 2019  匹配出来的都是字符串
	return HttpResponse('{}所有书籍都在这儿,你随意看'.format(y,))
# 2020所有书籍都在这儿,你随意看

def books2(request,y,m):
	print(y,m)
	return HttpResponse('{}-{}所有书籍都在这儿,你随意看2'.format(y,m))

def books3(request,year):
	print(year)  #2020
	return  HttpResponse('{}所有书籍都在这儿,你随意看3'.format(year))
	# 2020所有书籍都在这儿, 你随意看3

def books4(request,year,month):
	print(year,month)
	return HttpResponse('{}-{}所有书籍都在这儿,你随意看4'.format(year,month))
	# 2020-09所有书籍都在这儿, 你随意看4








