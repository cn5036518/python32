#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/24 18:58

from django import template

register = template.Library()
#注册器,变量名称必须叫register 固定写法

# 一 定义自定义过滤器
@register.filter()   #自定义过滤器
def xx(v1):
	return v1 + 'xx'   #chaoxx
	#第一参数是使用过滤器时,
	# 管道符前面的数据 <h1>{{ name|xx }}</h1>
	#name

@register.filter()    #自定义过滤器,至多有两个参数
def xx2(v1,v2):
	return  v1 + 'xx2' + v2  #chaoxx2oo
	#第一参数是使用过滤器时,管道符前面的数据 ,--name
	# 第二个参数是冒号后面的值,--''oo
	# <h1>{{ name|xx:'oo' }}</h1>
	# chaoxx2oo

# 二 定义自定义标签
@register.simple_tag
def tag1(v1,v2,v3): #参数个数没有限制
	return v1+v2+v3

# 三  定义inclusion_tag自定义标签--动态组件
# 应用:不同权限的人可以看到不同的菜单
# 通过inclusion_tag来做为装饰器,并且需要传入一个参数,
# 这个参数就是一个html文件(你想做成动态组件的html文件)
@register.inclusion_tag('zujian2.html')
def dongtai(v1): #参数没有个数限制
	data = v1  #[22,33,44]
	return {'xx':data}

# zujian2.html会收到定义的inclusion_tag函数的返回值,
# 然后进行zujian2.html这个动态组件的模板渲染





