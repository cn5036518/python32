from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import ensure_csrf_cookie



# Create your views here.
@ensure_csrf_cookie
def login(request):

	if request.method == 'GET':
		return render(request, 'login.html')

	else:
		# ajax第1 2个方式用这个 request.POST
		# data = request.POST
		# print(data) #<QueryDict: {'xname': ['yuantao'], 'pwd': ['666']}>
		# print('>>>>>',request.body)  #>>>>> b'xname=asdf&pwd=123'

		#ajax第3个方式需要 request.body
		data = request.body
		data = data.decode()
		import json
		data = json.loads(data)
		print(data,type(data))
		#{'xname': 'asdf', 'pwd': '123'} <class 'dict'>

		username = data.get('xname')
		password = data.get('pwd')
		if username == 'yuantao' and password == '666':
			return HttpResponse('ok')  # 200

		# ret = render(request, 'login.html', {'error':'用户名或者密码有误!!', 'username':username,'password':password})
		ret = HttpResponse('not ok')
		ret.status_code = 400
		return ret

























