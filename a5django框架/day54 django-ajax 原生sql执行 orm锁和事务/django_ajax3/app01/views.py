from django.shortcuts import render,HttpResponse
from django.http import  JsonResponse

# Create your views here.

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else: #POST
		data = request.POST
		print(data) #<QueryDict: {'username': ['1'], 'password': ['2']}>
		# username = data.get('username')
		username = data.get('xname')
		password = data.get('pwd')
		if username == 'yuantao' and password == '666':
			return HttpResponse('ok')
		# else:
			# ret = render(request,'login.html',
			#              {'error':'用户名或者密码有误',
			#               'username':username,  #将错误的用户名和密码留在页面
			#               'password':password})
		ret = HttpResponse('not ok')
		ret.status_code = 400 # 自定义状态码
		return ret
			# return HttpResponse('nok')
	
def index(request):
	userinfo = {
		'name':'春培',
		'age':18,
	}	
	return  JsonResponse(userinfo)
	
def food(request):
	food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
	# 响应非字典类型数据时,需要加上safe=False的参数 否则报错
	return JsonResponse(food_list,safe=False)
	
	
	
	
	
	
	
	
	
	
	
	