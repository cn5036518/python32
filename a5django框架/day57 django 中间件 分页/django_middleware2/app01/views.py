from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def login(request):
	print('login>>>>')
	if request.method == 'GET':
		return render(request,'login.html')
	username = request.POST.get('username')
	if username == 'root':
		#登录成功后,设置session
		request.session['is_login'] = True
		return redirect('index')
	else:
		return redirect('login')

# def index(request,book_id):
def index(request):
	print('index>>>>')
	# raise ValueError('xxx')

	return  HttpResponse('ok-index')

































