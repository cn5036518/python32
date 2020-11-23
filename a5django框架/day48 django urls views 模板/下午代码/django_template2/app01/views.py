from django.shortcuts import render

# Create your views here.
import datetime

def index(request):
	name = '赵万里'
	age = 18
	hobby = ['读书','健身']
	d1 = {'a':'b', 'c': 'd'}
	file_size = 10283408
	# xx = [11,]
	xx = []
	class A:
		def __init__(self):
			self.name = '万里'
			
		def my_hobby(self):
			return '张宇'

	now = datetime.datetime.now()
	ss = 'wanli ai zhangyu'
	a_tag = '<a href="http://www.baidu.com">百度<a/>'
	aa = 'hello ni hao'
	
	a = A()
	dd = locals()  #把当前文件所有的变量的名字和值作为键值对存到字典
	print(dd)
	# dd = {
	# 	'name': name,
	# 	"age": age,
	# 	"hobby": hobby,
	# 	"d1": d1,
	# 	"a": a,
	# 	"xx": xx,
	# 	"file_size": file_size,
	# }
	# 'asdfasdfasdf{{hobby.0}}' --  hobby[0]
	# 模板渲染完成之后, 才返回给浏览器, 浏览器再进行页面渲染, 生成效果
	return  render(request,'index.html',dd)