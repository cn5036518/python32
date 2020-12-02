"""django_orm_book图书管理 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import  views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^query/', views.query),
    
    # url(r'^books/', views.books), #图书展示
    # # url(r'^add_book/', views.add_book), #图书添加  fbv
    # url(r'^add_book/', views.AddBook.as_view()), #图书添加  cbv
    # url(r'^edit_book/(\d+)/', views.EditBook.as_view()), #图书编辑  cbv
    # url(r'^del_book/(\d+)/', views.del_book), #图书删除  fbv

    # 给路径起别名,
    #   作用:当url的路径变动的时候,只需要修改urls.py的r'^books/'v即可,
    #   其余地方都不需要修改
   
    url(r'^books/', views.books,name='books'),  # 图书展示
    # url(r'^add_book/', views.add_book), #图书添加  fbv
    url(r'^add_book/', views.AddBook.as_view(),name='add_book'),
    # url(r'^add_book/v1', views.AddBook.as_view(),name='add_book'),
    # 图书添加  cbv
    url(r'^edit_book/(\d+)/', views.EditBook.as_view(),name='edit_book'),  
    # 图书编辑  cbv   无名分组参数
    url(r'^del_book/(?P<book_id>\d+)/', views.del_book,name='del_book'),  
    # 图书删除  fbv   有名分组参数
    
    url(r'^ajax_del_book/(?P<book_id>\d+)/', views.ajax_del_book,name='ajax_del_book'), 

]

