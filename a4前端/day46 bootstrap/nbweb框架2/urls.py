#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/19 17:33

import views
urlpatterns = [
	('/index',views.index),
	('/',views.html),
	('/xx.css',views.css),
	('/1.jpg',views.jpg),
	("/xx.js",views.js),
	('/person',views.person)
]

# http://127.0.0.1:8001/index  页面输入




















