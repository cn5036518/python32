from django.shortcuts import render, HttpResponse, redirect

# Create your views here.




def login(request):
	print('login>>>>')
	if request.method == 'GET':
		return render(request, 'login.html')

	username = request.POST.get('username')
	if username == 'root':

		request.session['is_login'] = True
		return redirect('index')
	else:
		return redirect('login')
	# return HttpResponse('ok')


def index(request,booK_id):
	print('index>>>>>')
	print('index>>>>>',booK_id)

	raise ValueError('xxxxxxxxxxx')


	return HttpResponse('index')