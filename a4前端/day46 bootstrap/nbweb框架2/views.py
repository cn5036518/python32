#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/11/19 17:33

import  time

# 必须要写一个conn形参
def index(conn):
	with open('templates/index.html','rb') as f:
		data = f.read()
		# return  data
	conn.send(data)
	conn.close()

def css(conn):
	with open('statics/xx.css','rb') as f:
		data = f.read()
		conn.send(data)
		conn.close()

def jpg(conn):
	with open('statics/1.jpg','rb') as f:
		data = f.read()
		conn.send(data)
		conn.close()

def js(conn):
	with open('statics/xx.js','rb') as f:
		data = f.read()
		conn.send(data)
		conn.close()

def html(conn):
	now = str(time.time())
	# with open('templates/beautfulpage.html','rb') as f:
	# 	data = f.read()

	with open('templates/beautfulpage.html', 'r', encoding='utf-8') as f:
		data = f.read()
		data = data.replace('%xxoo%', now).encode()
		#
		conn.send(data)
		conn.close()

def person(conn):
	with open('templates/person.html','rb') as f:
		data = f.read()
		conn.send(data)
		conn.close()










