#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/6 22:44

from django.shortcuts import redirect,HttpResponse,render
from django.utils.deprecation import MiddlewareMixin

# 登录认证中间件--自定义
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
		print(current_path)  #/login/
		if current_path not in self.white_list:
# 如果不在中间件白名单,请session验证
			status = request.session.get('is_login')
			print(status)
			if not status:
# 如果session认证不通过,重定向到登录页面
				return redirect('login')
		print('请求它来了')















