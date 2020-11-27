from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

# render  响应页面  默认响应状态码为200
# HttpResponse 响应字符串  默认响应状态码为200
# redirect 重定向  默认响应状态码是302

def login(request):
	print(request)  #<WSGIRequest: GET '/login/'>
	print(request.method)  #GET
	print(request.POST) #<QueryDict: {}>
	print(request.GET)  #<QueryDict: {'a': ['1'], 'b': ['2']}>
	# http://127.0.0.1/login/?a = 1 & b = 2
	print(request.path) #当前请求路径
	#/login/

	print(request.get_full_path()) #当前请求路径包含查询参数
	# /login/?a = 1&b = 2
	print(request.META)#所有请求头的信息 {''HTTP_USER_AGENT':'asdfasdfasdf',....}
	# 	request.META 字典类型数据,所有的请求头的键都加上了一个HTTP_键名称


	if request.method == 'GET':
		return render(request,'login.html')
	else:  #POST
		uname = request.POST.get('username')
		print(uname)  #获取用户在用户名输入框输入的内容
		if uname =='shiyuan':
			# return render(request,'home.html')
			return redirect('/home/')  #redirect的参数为一个路径
	# 重定向跳转到/home/路径
	
		# return HttpResponse('ok')

def home(request):
	book2 = '金瓶梅'
	return render(request,'home.html',{'book':book2})

def index(request):
	re = HttpResponse('xxx')
	print(re)  #<HttpResponse status_code=200, "text/html; charset=utf-8">
	re['name'] = 'gaodaao' #添加响应头键值对
	re.status_code = 404  #修改状态码  不写默认是200
	print(re)  #[23/Nov/2020 20:41:09] "GET /index/ HTTP/1.1" 404 3
	return  re


from django.views import View
class BookView(View):  #继承父类
# get post
# 通过反射获取到请求方法对应的类中的方法来执行
	def get(self,request):
		return HttpResponse('ok')
# 需要处理什么请求方法,就写对应名称的方法


'''
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













