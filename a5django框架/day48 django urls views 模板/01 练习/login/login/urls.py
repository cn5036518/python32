"""login URL Configuration

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
    # url(r'^login/', views.login),  #登录首页  get 登录和提交在不同的页面
    # url(r'^login2/', views.login2),  #提交 post
    url(r'^login3/', views.login3),  #登录get和提交 post在一个页面
    
]
