from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	print(request.method)
	if request.method == "GET":
		return render(request,'test.html')
	else:
		uname = request.POST.get('username')
		print(uname)
		pwd = request.POST.get('password')
		print(pwd)
		return  HttpResponse("111")

		if uname == 'root'  and  pwd == '123':
			return render(request,'success.html',{'username':uname})



		else:
			return render(request,'false.html')