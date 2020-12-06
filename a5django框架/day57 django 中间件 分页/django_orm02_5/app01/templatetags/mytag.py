#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/6 15:47

from django import template

register = template.Library()
#注册器,变量名称必须叫register

# 通过inclusion_tag来做为装饰器,并且需要传入一个参数,
# 这个参数就是一个html文件(你想做成动态组件的html文件)
@register.inclusion_tag("menu.html")
def menu_tag(request):
	# 获取当前请求路径
	current_path = request.path
	print(current_path)  #/books/

	menu_data = request.session.get('menu_data')
	print(menu_data)
	# [{'title':'图书管理','url':'/books/'},
	# {'title':'作者管理','url':'/authors/','class':'menu_color'},
	# {'title':'出版社管理','url':'/publishs/'}]
# 这里root的菜单列表是3个元素  zhangsan的菜单列表是1个元素

# 给当前菜单添加高亮显示
	for i in menu_data:
		if current_path == i['url']:
			print('------------')
			i['class'] = 'menu_color'
			#添加一个键值对
	print(i)
	# {'id': 3, 'title': '出版社管理', 'url': '/publishs/', 'icon': 'fa fa-building', 'class': 'menu_color'}
	return {'menu_dict':menu_data}
# menu.html会收到定义的inclusion_tag函数的返回值,
# 然后进行menu.html这个动态组件的模板渲染


# 到了动态组件
# 1 数据库存放着每个用户和菜单的对应关系1
# 2 将用户和菜单的对应关系保存到session1
# 3 动态组件函数py--通过session获取到该登录用户的对应菜单
# 4 将步骤3中的对应菜单发给html
# 5 母版使用步骤3












