from django.shortcuts import render

# Create your views here.

def home(request):# 参数名称业内一般都写成request,
	print(request.path)  #当前请求路径
	current_user = '昭志'
	ret = render(request,'home.html',{'username':current_user})
	return ret
