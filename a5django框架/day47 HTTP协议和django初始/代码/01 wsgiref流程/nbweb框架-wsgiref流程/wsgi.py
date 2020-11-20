import  time
from threading import  Thread
from wsgiref.simple_server import make_server
from urls import  urlpatterns
# from 文件名 import =变量

def run():
	# wsgiref本身就是个web框架，提供了一些固定的功能
	# （请求和响应信息的封装，不需要我们自己写原生的socket了
	# 也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
	# 函数名字随便起
	def application(environ,start_response):
	#:param environ: 是全部加工好的请求信息，
	# 加工成了一个字典，通过字典取值的方式就能拿到很多你想要拿到的信息
	#:param start_response: 帮你封装响应信息的（响应行和响应头），
	# 注意下面的参数
		start_response('200 ok',[])
		print(environ)
		print(environ['PATH_INFO'])
		# 输入地址127.0.0.1:8080，这个打印的是'/',
		# 输入的是127.0.0.1:8080/index，打印结果是'/index'

		path = environ['PATH_INFO']
		for item in urlpatterns:
			if item[0] == path:
				# t = Thread(target=item[1],args=(conn,))
				# t.start()
				data = item[1]()
				break
		else:
			data = b'page no foung'
		return  [data]   #列表

		# 和咱们学的socketserver那个模块很像啊
	httpd = make_server('127.0.0.1',8080,application)

	print('Serving HTTP on port 8080...')
	# 开始监听HTTP请求:
	httpd.serve_forever()

# server.close()
# 1. 运行项目
# 2. 接受请求  ,wsgiref模块
# 	a wsgiref模块将请求信息封装为一个字典,然后将字典传给了application函数,并执行该函数
# 	b application函数中完成了不同路径找到不同的视图函数来执行,并获取视图函数的返回值,返回值为文件字节数据
# 	c aplication函数返回列表数据,列表中是视图函数的返回值
# 	d wsgiref模块的make_server类的内部原码中将 application函数的返回值,通过socket发送给了浏览器

















