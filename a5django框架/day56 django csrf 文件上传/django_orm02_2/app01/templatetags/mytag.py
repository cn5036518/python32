
from django import template

register = template.Library()

@register.inclusion_tag('menu.html')
def menu_tag(request):
	# 当前请求路径
	current_path = request.path

	menu_data = request.session.get('menu_data')
	# [{'title':'图书管理','url':'/books/'},{'title':'作者管理','url':'/authors/','class':'menu_color'},{'title':'出版社管理','url':'/publishs/'}]
	# 这里root的菜单列表是3个元素  zhangsan的菜单列表是1个元素
	# xx = []
	for i in menu_data:
		if current_path == i['url']:
			i['class'] = 'menu_color'
		# xx.append(i)

	return {'menu_dict': menu_data }




