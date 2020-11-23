from django.shortcuts import render,HttpResponse

# Create your views here.

# 登录页面 get
def login(request):
	# print(1111111)
	return render(request,'login.html')

# post请求提交的数据,通过request.POST来获取
# get或者post,当请求url中含有查询参数时,
# 要在后台的request对象中获取查询参数,用的属性为request.GET
# http://127.0.0.1:8001/login/?a=1&b=2

# 提交页面  post   --nok
def login2(request):
	print(request.POST)

	return HttpResponse('hello')  #返回字符串

	# HttpResponse 回复普通字符串
	# render 回复html页面
	
# 登录和提交合并的一起
# post请求提交的数据,通过request.POST来获取
# def login3(request):
# 	print(request.method)
# # 获取当前请求的请求方法,大写的   GET POST
# 	if request.method == 'GET':
# 		return render(request,'login.html')  #返回登录页面
# 		# return HttpResponse('ok')
# 	# elif request.method == 'POST':
# 	else:
# 		print(1)
# 		# post请求提交的数据,通过request.POST来获取
# 		uname = request.POST.get('username')
# 		# 这里的'username'是input中的name属性
# 		pwd = request.POST.get('password')
# 		print(uname,pwd)
#
# 		return HttpResponse('hello')

def login3(request):
	print(request.method)  # 获取当前请求的请求方法,大写的

	if request.method == 'GET':
		return render(request, 'login.html')
	else:
		uname = request.POST.get('username')
        # 这里的'username'是input中的name属性
		pwd = request.POST.get('password')
		print(uname, pwd)

		if uname == 'root' and pwd == '123':
			return render(request,'home.html',{'username':uname})
		else:
			return  render(request,'404.html')

		# return HttpResponse('hello')


















