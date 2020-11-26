from django.shortcuts import render,HttpResponse

# Create your views here.
from app01 import models #导入数据库
from app01.models import Book #导入数据库
from app01.models import userinfo #导入数据库
import datetime

def query(request):
	# 数据记录的增删改查
	#一 增加
# 1单条数据添加
# 方式1
# 	new_book = models.Book(
	new_book = Book(
		title='金瓶梅',
		price=9.9,
		# pub_date=datetime.datetime.now()
		# 添加时间日期类型数据时可以是时间日期类型的数据,也可以是字符串数据
		pub_date='2022-02-02',
		publish='32期出版社'
		# 有默认值的或者可以为空的或者主键字段,都可以不用传值
	)
	new_book.save()

	# 方式2 推荐
	# create方法,create方法的返回值为 新添加的数据的模型类对象
	# new_book = models.Book.objects.create(
	# new_book = Book.objects.create(
	# 	title='金瓶梅4',
	# 	price=19.9,
	# 	pub_date='2022-04-02',
	# 	publish='32期出版社'
	# )
	# print(new_book.title) #通过模型类对象,直接获取属性对应的值
	# print(new_book.price)

	# 2批量添加
	# obj_list = []
	# for i in range(10):
	# 	book_obj = models.Book(
	# 	book_obj = Book(
	# 		title=f'少年闰土{i}',
	# 		# 和js的$(变量名)取值类似    f和$类似
	# 		price=10+i,
	# 		pub_date=f'2020-04-1{i}',
	# 		publish='32期出版社'
	# 	)
	# 	obj_list.append(book_obj)
	# # print(obj_list)
	# #[<Book: 少年闰土0>, <Book: 少年闰土1>
	# models.Book.objects.bulk_create(obj_list) # #bulk_create 批量添加
	# Book.objects.bulk_create(obj_list) # #bulk_create 批量添加

	#二查询
	# 1 查询所有
	# book_objs = models.Book.objects.all()  #queryset 类似于列表
	# print(book_objs)
	# < QuerySet[ < Book: 金瓶梅 >, < Book: 金瓶梅4 >,

	# 2 条件查询  方法1
	# book_objs = models.Book.objects.filter(id=3)  #条件查询 结果为queryset类型数据
	# print(book_objs)
	# # < QuerySet[ < Book: 少年闰土0 >] >

	# book_objs = models.Book.objects.filter()
	# ## filter没有加条件,和all一样的效果
	# print(book_objs)
	# # < QuerySet[ < Book: 金瓶梅 >, < Book: 金瓶梅4 >,

	# book_objs = models.Book.objects.filter(id=100)
	# # 查不到数据,不会报错,返回空的queryset类型数据
	# print(book_objs)  #<QuerySet []>

	# 2 条件查询  方法2
	# book_objs = models.Book.objects.get(id=3)
	# # 条件查找 结果为: 模型类对象
	# print(book_objs)
	# #少年闰土0

	# book_objs = models.Book.objects.get()#也是查所有
   # # 但是get方法的查询结果有要求,有且只能有一条
	# print(book_objs)
	# book_objs = models.Book.objects.get(id=100)
	# # 查询不到结果会报错 Book matching query does not exist.
	# # 查询结果多于一条也会报错
	# # 报错是:get() returned more than one Book -- it returned 16!

	# 三	删除
	# 方法1
	# models.Book.objects.filter(id=3).delete()
	# queryset类型数据可以调用delete方法删除查询结果数据

	# models.Book.objects.filter().delete()
	# 删除所有

	# 方法2
	# models.Book.objects.get(id=4).delete()
	# 模型类对象也可以调用delete方法删除数据

	# models.Book.objects.get().delete()
	# 删除所有

	# 四 修改
	# 修改方式1  通过queryset类型数据修改
	# models.Book.objects.filter(id=5).update(
	# 	price=20,
	# 	title='读书'
	# )

	# models.Book.objects.get(id=5).update( #报错:模型类对象不能调用update方法
	# 	price=30,
	# )#报错  'Book' object has no attribute 'update'

	# 修改方式2  通过模型类对象来修改  推荐
	# ret = models.Book.objects.get(id=6)
	# ret.price = 30
	# ret.title = '健身'
	# ret.save()

	# 测试auto_now和auto_now_add两个参数
	# 新增一条数据
	# models.userinfo.objects.create(
	# 	name='投资',
	# )
	# 1	投资	2020-11-25 13:26:46.863857	2020-11-25 13:26:46.864854

	# models.userinfo.objects.filter(id=1).update(
	# 	# update不能触发自动更新时间的auto_now参数的作用,
	# 	# 	# 如果用update方法来更新记录,并保存更新记录的时间,
	# 	# 	需要我们手动给该字段传入当前时间
	# 	name='陪家人',
	# 	b1=datetime.datetime.now()
	# )
# 1	陪家人	2020-11-25 21:29:23.674595	2020-11-25 13:26:46.864854

	# # 这种save方式能够触发auto_now参数自动更新修改时间的动作 推荐
	# ret = models.userinfo.objects.get(id=1)
	# ret.name='帮朋友'
	# ret.save()
	# # 1	帮朋友	2020-11-25 13:31:34.959877	2020-11-25 13:26:46.864854

	# 基于双下划线的模糊查询
	# 查询书名以少年开头的哪些书
	# obj_list = models.Book.objects.filter(title__startswith='少年')#以什么开头
	# print(obj_list)
	# < QuerySet[ < Book: 少年闰土4 >, < Book: 少年闰土5 >




	return HttpResponse('ok')




















