import os
import pickle  #json不能存储对象
import random
import re



# from .card import Card     #相对路径的导包
from person import Person

class Operation():

	lst = [
		{"id":"1","name" :"alex","age":"28","hobbies":["上窜","瞎跳","真能浪"]},
		{"id":"2", "name" : "wusir","age":"23","hobbies":["忽悠","吹牛"]},
		{"id":"3","name" :"宋仲基","age":"99","hobbies":["撩妹","思密达","怕不怕"]}
		]
	
	lst_new = []

	# 1开户注册
	def register(self):
		# 创建一个用户的对象
		for i in range(len(self.lst)):
			# user = Person(id,name,age,hobbies)  #
			user = Person(self.lst[i]['id'],self.lst[i]['name'],self.lst[i]['age'],self.lst[i]['hobbies'])  #
			self.lst_new.append(user)
		
		return self.lst_new
		
obj = Operation()
res = obj.register()		
print(res)
# [<person.Person object at 0x7ff08fd7a0f0>, <person.Person object at 0x7ff08fd7a438>, <person.Person object at 0x7ff08fd11978>]




















































