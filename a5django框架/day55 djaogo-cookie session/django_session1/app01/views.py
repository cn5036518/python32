from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		#get后的username是html中input标签的name属性
	# 把前端页面输入框的内容传递到后端
		password = request.POST.get('password')

		if username == 'root' and password == '123':
# 登录验证
# 			print(request.session)
# <django.contrib.sessions.backends.db.SessionStore object at 0x00000236B2A648D0>
			request.session['is_login'] = True
			request.session['username'] = username
			print(request.session['is_login']) #True
			# request.session.set_expiry(5)
		# 设置5秒后失效
	# '''
	#  1 生成随机字符串
	#  2 加入到cookie中,{sessioid: 'asdfasdfasdf'} 发给客户端浏览器
	#  3 将设置的session数据(is_login,username...),序列化然后加密保存到数据库中.
	#   django-session表
	# '''
			return redirect('home')
		# 1 登录密码验证通过,可以看到home首页
		# 这里还没有验证session
			# return HttpResponse('ok')
		return redirect('login')
	# 2 登录密码验证不通过,回到登录页面

def home(request):
	status = request.session.get('is_login')
	# 1	服务端取出cookie中的sessionid对应的随机字符串
	# 2	通过随机字符串去django - session表中找到对应记录
	# 3	将记录中session_data的数据进行解密并反序列化(变成字典),
	# 然后取出键对应的值
	print(status)
	if status == True:
		#这里和cookie不同,cookie的'True'是字符串
		# 这里的True是布尔值
		return render(request,'home.html')
	# 1 session 认证通过,返回home首页
	else:
		return redirect('login')  #url别名
# 2 session 认证不通过,跳转回到登录页面

	# return HttpResponse('ok')

# no such table: django_session
# 需要在setting中连接数据库

def cart(request):
	cart_list = ['读书','健身']
	status = request.session.get('is_login')
	if status == True:
		# 1 session 认证通过,返回购物车页面
		return render(request,'cart.html',{'cart_list':cart_list})
	else:
		return redirect('login')
# 2 session 认证不通过,跳转回到登录页面

def logout(request):
	request.session.flush()
	#清空session中的数据
	# 1	删除cookie中的sessionid值
	# 2	删除数据库中对应记录
	# (本次请求cookie中的sessionid的值对应的记录)
	return redirect('login') #urls别名写法















































