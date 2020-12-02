from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')

		if username == 'root' and password == '123':
			ret = redirect('home')
			ret.set_cookie('is_login','true1')  #添加cookie
			ret.set_cookie('username',username)
			return ret
		else:
			return redirect('login')
		# return HttpResponse('ok')

def home(request):

	status = request.COOKIES.get('is_login')
	# print(status)  #true1

	if status == 'true1':
		return render(request,'home.html')
	else:
		return redirect('login')
	# return HttpResponse('ok-home')

def cart(request):
	status = request.COOKIES.get('is_login')
	# print(status)  #true1

	if status == 'true1':
		cart_list = ['读书','健身']
		return render(request, 'cart.html',{'cart_list':cart_list})
	else:
		return redirect('login')
	# return HttpResponse('ok-cart')

def logout(request):
	ret = redirect('login')
	ret.delete_cookie('is_login')
	return  ret
	# return HttpResponse('ok-logout')















