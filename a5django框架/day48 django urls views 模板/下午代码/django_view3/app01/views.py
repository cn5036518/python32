from django.shortcuts import render,HttpResponse

# Create your views here.

# def index(request):
# 	re = HttpResponse('xxx')
# 	return re  #返回字符串


from django.views import  View
class BookView(View):
# get post
# 通过反射获取到请求方法对应的类中的方法来执行
	def get(self,request):
		return HttpResponse('ok')


'''
	原码分析
	def dispatch(self, request, *args, **kwargs):
		# Try to dispatch to the right method; if a method doesn't exist,
		# defer to the error handler. Also defer to the error handler if the
		# request method isn't on the approved list.
		if request.method.lower() in self.http_method_names: #get
			# ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
			handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
		else:
			handler = self.http_method_not_allowed
		return handler(request, *args, **kwargs)  # HttpResponse('ok')

'''

#定义装饰器
def func(f):
	def inner(*args,**kwargs):
		print('aaa')
		ret = f(*args,**kwargs)
		print('bbb')
		return ret  #内函数返回值
	return inner

@func  # FBV装饰器用法和普通函数一样
# index = func(index)
# index = inner
# index() = inner()
# @符号 装饰器的标识符 :
	# (1) 自动把下面修饰的原函数当成参数传递给装饰器
	# (2) 把返回的新函数去替换原函数
def index(request):
	return HttpResponse('index')

from django.utils.decorators import method_decorator

# CBV方法加装饰器的方式1 --ok  推荐
class ArticleView(View):
	# def get(self,request,year):
	# 	print(year)  #2020
	# 	return HttpResponse('articles')
	
	@method_decorator(func)   # CBV方法加装饰器的方式1 
	# 固定写法
	def get(self,request,year):
		print(year)
		return render(request,'articles.html')
	# aaa
	# 2020
	# bbb

	@method_decorator(func)  # CBV方法加装饰器的方式1
	def post(self,request,year):
		# 可以获取用户的输入内容
		print(request.POST) #< QueryDict: {'uname': ['123']} >
		return HttpResponse('ok')

	# aaa
	# < QueryDict: {'uname': ['123']} >
	# bbb

# CBV方法加装饰器的方式2  同时给get和post两个方法加了装饰器,无法只给其中一个添加装饰器
class ArticleView2(View):
	def get(self,request,year):
		print(year)
		return HttpResponse('ok')

	# 重写dispatch方法来进行拓展
	@method_decorator(func)  # 方式2
	def dispatch(self, request, *args, **kwargs):
		print('111111')
		# ret = super(ArticleView2,self).dispatch(request, *args, **kwargs)  #可以
		# ret = super(ArticleView2).dispatch(request, *args, **kwargs)  #报错
		ret = super().dispatch(request, *args, **kwargs)
		# 调父类的成员
		# super(类名,self)

		print('222222')
		return ret

	def get(self,request,year):
		print(year)
		return render(request,'articles.html')

	# aaa
	# 111111
	# 2020
	# 222222
	# bbb

	def post(self,request,year):
		# 可以获取用户的输入内容
		print(request.POST) #< QueryDict: {'uname': ['123']} >
		return HttpResponse('ok')

	# aaa
	# 111111
	# < QueryDict: {'uname': ['4444']} >
	# 222222
	# bbb


# CBV方法加装饰器的方式3--ok   可以分别对post和get添加装饰器  用的少一点
@method_decorator(func,name='get')
@method_decorator(func,name='post')
class ArticleView3(View):
	def get(self,request,year):
		print(year)
		return render(request,'articles.html')

	# aaa
	# 2020
	# bbb

	def post(self,request,year):
		print(request.POST)
		return HttpResponse('ok')

# aaa
# <QueryDict: {'uname': ['1111']}>
# bbb















