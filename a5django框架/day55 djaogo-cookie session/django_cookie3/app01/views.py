from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# 用户登录状态判断, 登录认证(判断cookie)
# 登录验证(判断用户名和密码)

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else: #post
		username = request.POST.get('username')
		password = request.POST.get('password')
		# 登录密码通过,重定向跳转到home页面,添加cookie
		if username == 'root' and password == '123':
			ret = redirect('home')
			ret.set_cookie('is_login','True2')
			ret.set_cookie('username',username)
			# print(request.COOKIES.get('is_login'))  #None
			# print(request.COOKIES,type(request.COOKIES))
			#{} <class 'dict'>
			return ret
		else:
			#登录密码错误,重定向跳转到登录页面
			return redirect('login')  #用的urls别名

def home(request):
	res = render(request,'home.html')
	print(request.COOKIES)
	#{'is_login': 'true', 'username': 'root'}
	status = request.COOKIES.get('is_login')
	# 获取请求携带的cookie数据
	print(status,type(status))
	#true <class 'str'>

	if status == 'True2':
		# cookie验证通过,允许看到home首页
		return render(request,'home.html')
	else:
		# cookie验证不通过,不允许看到home首页,重定向回到登录页面
		return redirect('login')
	# return HttpResponse('ok-home')

def cart(request):
	print(request.COOKIES)
	status = request.COOKIES.get('is_login')
	# 获取请求携带的cookie数据
	print(status,type(status))

	if status == 'True2':
	# cookie验证通过,允许看到购物车页面
		cart_list = ['读书','健身']
		return render(request,'cart.html',{'cart_list':cart_list})
	else:
		# cookie验证不通过,不允许看到购物车页面,回到登录页面
		return redirect('login')
	# return HttpResponse('ok-cart')

def logout(request):
	ret = redirect('login')
	ret.delete_cookie('is_login')
	# 删除cookie中的'is_login'键值对
	return ret



























