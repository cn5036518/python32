from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST.get('username')
		password = request.POST.get('password')

		if username == 'root' and password == '123':
			request.session['is_login'] = True   #添加session
			request.session['username'] = username
			return redirect('home')
		else:
			return  redirect('login')
	# return HttpResponse('ok')

def home(request):
	status = request.session.get('is_login')
	print(status,type(status))  #True <class 'bool'>
	if status == True:
		return render(request,'home.html')
	else:
		return  redirect('login')
	# return HttpResponse('ok-home')

# no such table: django_session
# 需要执行数据库迁移指令

def cart(request):
	cart_list = ['读书','健身']
	status = request.session.get('is_login')
	if status == True:
		return render(request,'cart.html',{"cart_list":cart_list})
	else:
		return  redirect('login')
	# return HttpResponse('ok-cart')

def logout(request):
	request.session.flush()
	return redirect('login')
	# return HttpResponse('ok-logout')

















