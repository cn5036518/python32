from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
# Create your views here.



def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')

	else:
		data = request.POST
		print(data) #<QueryDict: {'xname': ['yuantao'], 'pwd': ['666']}>
		username = data.get('xname')
		password = data.get('pwd')
		if username == 'yuantao' and password == '666':
			return HttpResponse('ok')  # 200

		# ret = render(request, 'login.html', {'error':'用户名或者密码有误!!', 'username':username,'password':password})
		ret = HttpResponse('not ok')
		ret.status_code = 400# 自定义状态码
		return ret




# def index(request):
# 	import json
# 	userinfo = {
# 		'name':'春培',
# 		'age': 18,
#
# 	}
# 	userinfo_st = json.dumps(userinfo, ensure_ascii=False)
#
# 	# return HttpResponse('ok')
# 	# ret = HttpResponse(userinfo_st)
# 	# ret['content_type'] = 'application\json'
# 	return HttpResponse(userinfo_st,content_type='application\json')
# 	# return JsonResponse(userinfo)


def index(request):
	# import json
	userinfo = {
		'name':'春培',
		'age': 18,

	}
	# userinfo_st = json.dumps(userinfo, ensure_ascii=False)

	# return HttpResponse('ok')
	# ret = HttpResponse(userinfo_st)
	# ret['content_type'] = 'application\json'
	# return HttpResponse(userinfo_st,content_type='application\json')
	return JsonResponse(userinfo)



# def food(request):
# 	import json
#
# 	food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
# 	food_str = json.dumps(food_list)
#
# 	return HttpResponse(food_str)
def food(request):
	# import json

	# food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
	food_list = ['黄瓜', '茄子', '香蕉', '萝卜', '冬瓜']
	# food_str = json.dumps(food_list)
	# 响应非字典类型数据时,需要加上safe=False的参数
	return JsonResponse(food_list, safe=False)



def mylogin(request):
	return render(request, 'mylogin.html')
