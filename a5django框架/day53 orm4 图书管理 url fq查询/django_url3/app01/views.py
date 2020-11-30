from django.shortcuts import render,HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
	print('app01>>>>',reverse('app01:index'))
	#	#命名空间名称:别名名称
	
	# print('app01>>>>',reverse('index'))
	# app01 >> >> / app03 / index /
	# 如果app01 app02 app03 3个应用的url别名都是index
	# 会出现访问app01  但是reverse('index')解析后是/app03/index/
	# 命名空间名称:别名名称 可以解决这个问题

	return HttpResponse('app01-index')
# 在视图中使用别名反向解析是的写法:

# 在html文件中写法如下   在别名edit_book前面加上app01命名空间
# <a href="{% url 'app01:edit_book' book.id %}" class="btn btn-warning">编辑</a>












