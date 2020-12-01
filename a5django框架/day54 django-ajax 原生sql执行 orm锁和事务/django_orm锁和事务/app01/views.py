from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import  models

# 锁和事务
# 加锁
# 原生sql加锁
# select * from app01_book where id=1 for update;#  查询手动加锁

# orm加锁
# models.Book.objects.filter(id=1).select_for_update()
#  查询手动加锁
#但是查询加锁,都要在事务中才能体现其效果.

# 加事务
# 　用法1：给函数做装饰器来使用　
from django.db import transaction

@transaction.Atomic
def viewfunc(request):
	d1 = {
		'name':'chao',
	}

	username = request.GET.get('name') #html的name属性 name2
	sid = transaction.savepoint() #创建保存点
# This code executes inside a transaction.
	models.Book.objects.filter(id=1).select_for_update()

	# do_stuff()
	try:
		d1[username]
	except:
# 保存点一般是代码运行逻辑过程中,代码出了问题,需要手动回滚事务时使用
		transaction.savepoint_rollback(sid)  #回滚到保存点
		return HttpResponse('hello')

# 用法2：作为上下文管理器来使用
def viewfunc(request):
# This code executes in autocommit mode (Django's default).
# 	do_stuff()  #sql   不在事务里

	with transaction.atomic():
# This code executes inside a transaction.
# 		do_more_stuff()  #sql  在事务里

	# do_other_stuff()  ##不在事务里

# 事务四大特性
# 
# 原子性(多个sql语句捆绑到一起, 要么都成功, 要么全失败)
# 
# 一致性
# 事务运行前后, 数据保持一致(我减100, 你加100, 别多加也别少加)
# 
# 隔离性
# 一个事务的执行和另外一个事务的执行是互相隔离的
# 
# 持久性
# 事务一旦提交, 就永久刷到磁盘上了






























