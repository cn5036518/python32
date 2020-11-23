"""django_view3 URL Configuration

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

from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^index/',views.index),
	
	url(r'^book/',views.BookView.as_view()),
	
	url(r'^articles/(\d+)/',views.ArticleView.as_view()),
	# views.类名.as_view() 是固定写法

	url(r'^articlesa/(\d+)/',views.ArticleView2.as_view()),
	url(r'^articlesb/(\d+)/',views.ArticleView3.as_view()),
]
