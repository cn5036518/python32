from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def login(request):
	print(request)  #<WSGIRequest: GET '/login/?a=1&b=2'> WSGIRequest类的实例化对象
	print(request.method)
	print(request.POST)
	print(request.GET)  # request.GET.get('a')  == 1
	print(request.path)  #当前请求路径
	print(request.get_full_path())  #当前请求路径包含查询参数
	print(request.META)  #所有请求头的信息 {''HTTP_USER_AGENT':'asdfasdfasdf',....}
	# 	request.META 字典类型数据,所有的请求头的键都加上了一个HTTP_键名称
	# return HttpResponse('ok')
	if request.method == 'GET':
		return render(request, 'login.html')

	else:
		uname = request.POST.get('username')
		if uname == 'shiyuan':

			# return redirect('/home/')  #redirect的参数为一个路径
			return render(request, 'home.html')  #redirect的参数为一个路径


def home(request):
	book = '金瓶梅'
	return render(request,'home.html' , {'book': book})



def index(request):
	re = HttpResponse('xxx')
	# re = render('xxx')
	# ret = redirect('/home/')
	re['name'] = 'gaodaao'  # 添加响应头键值对
	re.status_code = 404  # 修改状态码
	return re  #返回字符串



from django.views import View
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

# 定义装饰器
def func(f):
	def inner(*args,**kwargs):
		print('aaaaa')
		ret = f(*args,**kwargs)
		print('bbbbb')
		return ret
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

# 方式 3
# @method_decorator(func,name='post')
# @method_decorator(func,name='get')
class ArticalView(View):

	# def get(self,request, year):
	# 	print(year)
	# 	return HttpResponse('articals')

	# 重写dispatch方法来进行拓展
	# @method_decorator(func)  # 方式2
	# def dispatch(self, request, *args, **kwargs):
	#
	# 	print('111111')
	# 	ret = super(ArticalView, self).dispatch(request, *args, **kwargs)
	#
	# 	print('222222')
	# 	return ret

	# @method_decorator(func)  # CBV方法加装饰器的方式1
	# 固定写法
	def get(self,request, year):
		print(year)
		return render(request, 'articals.html')
	# aaa
	# 2020
	# bbb

	# @method_decorator(func)  # CBV方法加装饰器的方式1
	def post(self,request, year):
		print(request.POST)  #可以获取用户的输入内容
		# < QueryDict: {'uname': ['123']} >
		return HttpResponse('ok')
# aaa
	# < QueryDict: {'uname': ['123']} >
	# bbb

print('-----------------------------------------------1')


# CBV方法加装饰器的方式1 --ok  推荐
class ArticleView4(View):
	# def get(self,request,year):
	# 	print(year)  #2020
	# 	return HttpResponse('articles')

	@method_decorator(func)  # CBV方法加装饰器的方式1
	# 固定写法
	def get(self, request, year):
		print(year)
		return render(request, 'articles.html')

	# aaa
	# 2020
	# bbb

	@method_decorator(func)  # CBV方法加装饰器的方式1
	def post(self, request, year):
		# 可以获取用户的输入内容
		print(request.POST)  # < QueryDict: {'uname': ['123']} >
		return HttpResponse('ok')


# aaa
# < QueryDict: {'uname': ['123']} >
# bbb

# CBV方法加装饰器的方式2  同时给get和post两个方法加了装饰器,无法只给其中一个添加装饰器
class ArticleView2(View):
	def get(self, request, year):
		print(year)
		return HttpResponse('ok')

	# 重写dispatch方法来进行拓展
	@method_decorator(func)  # 方式2
	def dispatch(self, request, *args, **kwargs):
		print('111111')
		# ret = super(ArticleView2,self).dispatch(request, *args, **kwargs)  #可以
		# ret = super(ArticleView2).dispatch(request, *args, **kwargs)  #报错
		ret = super().dispatch(request, *args, **kwargs)
		# """
		# (1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
		# (2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
		# (3)super用途: 解决复杂的多继承调用顺序
		# """super()只调用父类的相关成员,顺带传递对象参数"""
		# """self按照顺序找: 对象本身 => 类 => 父类 对应的成员 """
		# """
		# 调父类的成员
		# super(类名,self)

		print('222222')
		return ret

	def get(self, request, year):
		print(year)
		return render(request, 'articles.html')

	# aaa
	# 111111
	# 2020
	# 222222
	# bbb

	def post(self, request, year):
		# 可以获取用户的输入内容
		print(request.POST)  # < QueryDict: {'uname': ['123']} >
		return HttpResponse('ok')


# aaa
# 111111
# < QueryDict: {'uname': ['4444']} >
# 222222
# bbb


# CBV方法加装饰器的方式3--ok   可以分别对post和get添加装饰器  用的少一点
@method_decorator(func, name='get')
@method_decorator(func, name='post')
class ArticleView3(View):
	def get(self, request, year):
		print(year)
		return render(request, 'articles.html')

	# aaa
	# 2020
	# bbb

	def post(self, request, year):
		print(request.POST)
		return HttpResponse('ok')

# aaa
# <QueryDict: {'uname': ['1111']}>
# bbb






















