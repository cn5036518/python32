from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def upload(request):
	if request.method == 'GET':
		return render(request,'upload.html')
	else:
		print(request.POST)
# 如果没有修改请求消息格式(content-type),
# 那么文件名称会在request.POST中拿到,但是只是文件名称
# 		< QueryDict: {'csrfmiddlewaretoken': ['dVWOiodeSVWVx6VH5FUTDSoChF5xOE3bKHFZwDKqjPrNAjXOiLN21hg3OTAfyf6k']
# 			             , 'username': [''], 'password': ['']} >
		print(request.FILES)
		# < MultiValueDict: {'avatar': [ < InMemoryUploadedFile: QQ截图20201205193634.jpg(image / jpeg) >]} >
# 里面放的是文件数据(文件对象,类似于文件句柄)
# 		print(request.FILES.getlist('avatar')) #获取多个文件对象
# 		print(request.FILES.get('avatar'))  # timg.jpg   #获取单个文件对象
		# QQ截图20201205193634.jpg
		file_obj = request.FILES.get('avatar')
		print(file_obj.name)
		#QQ截图20201205193634.jpg

		with open(file_obj.name,'wb') as f:
			# for i in file_obj:
			# 	f.write(i)
			for i in file_obj.chunks():
				# 默认一次返回大小为经测试为65536B，也就是64KB，
				# 最大为2.5M，是一个生成器
				f.write(i)
		return HttpResponse('ok')























