#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/4 16:08

from django.shortcuts import redirect,HttpResponse,render
from django.utils.deprecation import MiddlewareMixin

# 登录认证中间件
class LoginAuth(MiddlewareMixin):
# # 白名单
	white_list = ['/login/','/register/']
#登录和注册页面不需要验证session
# 其他页面都需要登录后,才能访问
# #只有登录成功后,才会拿到session

# 	# 对请求处理用process_request,
# 	如果请求通过了处理,就return None,
# 	如果没有通过直接return HttpResponse对象  终止
	def process_request(self,request):
		current_path = request.path
		print(current_path)    #/login/
		if current_path not in self.white_list:
			#如果不在中间件白名单,请session验证
			status = request.session.get('is_login')
			print(status)  #True
			if not status:
				#如果session认证不通过,重定向
				return redirect('login')
		print('请求它来啦')


class Md1(MiddlewareMixin):
	def process_request(self,request):
		print('Md1-process_request')
		# print(request.META['REMOTE_ADDR']) ## 127.0.0.1

		# Md1 - process_request
		# Md2 - process_request
		# login >> >>

		# return HttpResponse('xxx')
	# 不经过视图函数和process_view 就 直接返回
		# Md1 - process_request
		# 127.0.0.1
		# Md1 - process_response

	def process_view(self,request,view_func,view_args,view_kwargs):
		print('md1--process_view')
		print(view_func,view_args,view_kwargs)

	# 不经过视图函数就 直接返回

		# return HttpResponse('not ok')
# 	Md1-process_request
# Md2-process_request
# md1--process_view
# <function login at 0x0000017699E45730> () {}
# Md2-process_response
# Md1-process_response
		
	def process_exception(self,request,exception):
		# 没有异常就不执行
		print(exception,type(exception))
		#ValueError: xxx
		print('md1-process_exception')
	# 统一做异常处理
		if isinstance(exception,ValueError):
			return HttpResponse('视图函数报错啦',status=500)

# 		Md1-process_request
# Md2-process_request
# md1--process_view
# <function index at 0x00000242DBB25D08> () {}
# md2--process_view
# index>>>>
# md2-process_exception
# xxx <class 'ValueError'>
# md1-process_exception
# Md2-process_response
# Md1-process_response



	def process_response(self,request,response):
		print('Md1-process_response')
		return response
	# Md1 - process_request
	# Md2 - process_request
	# login >> >>
	# Md2 - process_response
	# Md1 - process_response

	# Md1-process_request
	# Md2-process_request
	# index>>>>
	# Md2-process_response
	# Md1-process_response	

class Md2(MiddlewareMixin):
	def process_request(self,request):
		print('Md2-process_request')

	def process_response(self,request,response):
		print('Md2-process_response')
		return response

	def process_view(self,request,view_func,view_args,view_kwargs):
		print('md2--process_view')
# Md1-process_request
# Md2-process_request
# md1--process_vies
# <function login at 0x000001C89AE45730> () {}
# md2--process_view
# login>>>>
# Md2-process_response
# Md1-process_response

	def process_exception(self,request,exception):
		print('md2-process_exception')

















