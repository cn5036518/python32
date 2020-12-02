from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# 用户登录状态判断, 登录认证(判断cookie)
# 登录验证(判断用户名和密码)

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')

		if username == 'root' and password == '123':
			#登录验证
			ret = redirect('home')  #用的别名
			# ret = HttpResponse('ok')
			#跳转到首页home
			ret.set_cookie('is_login','True2')
	# 设置cookie,如果有同名(键)的cookie,那么就是修改cookie
			# 清除浏览器缓存后,第一次设置是新增 第二次设置同名键是修改cookie
			ret.set_cookie('username',username)
			return ret
		return redirect('login')  #用的别名
	# 验证不通过,返回登录页面

def home(request):
	ret = render(request,'home.html')
	# ret.set_cookie('is_login',"True2")
# 键相同,就是修改cookie
	print(request.COOKIES)
# {'is_login': 'True', 'username': 'root'}  字典数据
	status = request.COOKIES.get('is_login')
# 获取请求携带的cookie数据
	print(status,type(status))
	# True <	class 'str'> #这里的true是str,不是布尔类型
	if status == 'True2':
		# cookie验证通过,允许看到home首页
		return render(request,'home.html')
	else:
		# cookie验证不通过,不允许看到home首页,重定向回到登录页面
		return redirect('login')
	# return HttpResponse('ok')

def cart(request):
	print(request.COOKIES)
	# {'is_login': 'True', 'username': 'root'}
	status = request.COOKIES.get('is_login')
	# 获取请求携带的cookie数据
	print(status,type(status))
	#True2 <class 'str'>

	if status == 'True2':
		# cookie验证通过,允许看到购物车页面
		cart_list = ['读书','健身']
		return render(request,'cart.html',{'cart_list':cart_list})
	else:
		# cookie验证不通过,不允许看到购物车页面,回到登录页面
		return redirect('login')
	# return HttpResponse('ok')

def logout(request):
	ret = redirect('login')
	ret.delete_cookie('is_login')
	#删除cookie中的'is_login'键值对
	return ret






























