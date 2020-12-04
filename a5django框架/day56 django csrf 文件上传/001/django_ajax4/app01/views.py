from django.shortcuts import render,HttpResponse

# Create your views here.

def login(request):

	if request.method == 'GET':
		return render(request, 'login.html')

	else:
		# data = request.POST
		# print(data) #<QueryDict: {'xname': ['yuantao'], 'pwd': ['666']}>
		# print('>>>>>',request.body)  #>>>>> b'xname=asdf&pwd=123'

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