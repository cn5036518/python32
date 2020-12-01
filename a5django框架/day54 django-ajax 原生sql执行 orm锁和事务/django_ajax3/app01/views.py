from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else: #POST
		data = request.POST
		print(data) #<QueryDict: {'username': ['1'], 'password': ['2']}>
		username = data.get('username')
		password = data.get('password')
		if username == 'yuantao' and password == '666':
			return HttpResponse('ok')
		else:
			ret = render(request,'login.html',
			             {'error':'用户名或者密码有误',
			              'username':username,  #将错误的用户名和密码留在页面
			              'password':password})
			ret.status_code = 400 # 自定义状态码
			return ret
			# return HttpResponse('nok')