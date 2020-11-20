#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/20 15:10

from wsgiref.simple_server import make_server
# wsgiref本身就是个web框架，提供了一些固定的功能
#（请求和响应信息的封装，不需要我们自己写原生的socket了
#也不需要咱们自己来完成请求信息的提取了，提取起来很方便）
#函数名字可以自定义

def application(environ,start_response):
	# :param environ: 是全部加工好的请求信息，加工成了一个字典，
	# 通过字典取值的方式就能拿到很多你想要拿到的信息
	# :param start_response: 帮你封装响应信息的（响应行和响应头），
	# 注意下面的参数
	# :return:

	start_response('200 ok',[('k1','v1'),('k2','v2')])
	print(environ)
	print(environ['PATH_INFO'])  #/
	#输入地址127.0.0.1:8000，这个打印的是'/',
	#输入的是127.0.0.1:8000/index，打印结果是'/index'

	return [b'<h1>hello,web!</h1>']

#和咱们学的socketserver那个模块很像啊
httpd = make_server('127.0.0.1',8000,application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求:
httpd.serve_forever()














