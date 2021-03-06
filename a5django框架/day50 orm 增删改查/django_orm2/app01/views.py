from django.shortcuts import render,HttpResponse

# Create your views here.

from app01 import models
import datetime

def add_book(request):
# 记录的增删改查
# 1添加
# 添加数据记录  方式1
	new_book = models.Book(
		title='金瓶梅',
		price=9.91,
		# pub_date=datetime.datetime.now()
		# 添加时间日期类型数据时可以是时间日期类型的数据,
		# 也可以是字符串数据
		pub_date='2022-02-02',
		publish='32期出版社'
		# 有默认值的或者可以为空的或者主键字段,都可以不用传值
	)
	# new_book.save()

# 添加方式2 create方法,create方法的返回值为 新添加的数据的模型类对象
# 	new_book = models.Book.objects.create(
# 		title='金瓶梅4',
# 		price=19.9,
# 		pub_date='2020-04-02',
# 		publish='32期出版社'
# 	)

	# print(new_book.title) #金瓶梅4
	# print(new_book.price) #19.9

# 批量添加
# 	obj_list = []
# 	for i in range(2):
# 		book_obj = models.Book(
# 			title=f'少年闰土{i}',
# 			# 和js的$(变量名)取值类似
# 			price=10 + i,
# 			pub_date=f'2022-04-1{i}',
# 			publish='32期出版社'
# 		)
# 		obj_list.append(book_obj)
#
# 	print(obj_list)
# # [<Book: Book object>, <Book: Book object>,
# # [<Book: 少年闰土0>, <Book: 少年闰土1>]  models中加了 __str__魔术方法
# 	models.Book.objects.bulk_create((obj_list))  #bulk_create 批量添加

	# 2 查询
	# 01 查询所有
	# book_objs = models.Book.objects.all() # #queryset 类似于列表
	# print(book_objs)
	# <QuerySet [<Book: 金瓶梅>, <Book: 金瓶梅>,

	#02 指定条件查询  方法1
# 结果为queryset类型数据
	# book_objs = models.Book.objects.filter(id=4)
	# print(book_objs)
	# <QuerySet [<Book: 金瓶梅4>]>

# 	book_objs = models.Book.objects.filter()
# # filter没有加条件,和all一样的效果
# 	print(book_objs)
# <QuerySet [<Book: 金瓶梅>, <Book: 金瓶梅>,

	# book_objs = models.Book.objects.filter(id=100)
	# print(book_objs)
	# <QuerySet []>

	#02 指定条件查询  方法2
# 	book_objs = models.Book.objects.get(id=4)
# ## 条件查找 结果为: 模型类对象
# 	print(book_objs)
# #金瓶梅4

# 	book_objs = models.Book.objects.get()  #查所有
# # 但是get方法的查询结果有要求,有且只能有一条
# 	print(book_objs)
# 	book_objs = models.Book.objects.get(id=100)  # 查询不到结果会报错 Book matching query does not exist.
# 	# 查询结果多于一条也会报错
# 	print(book_objs)
# get() returned more than one Book -- it returned 16!

# 3 删除  方法1
# 	models.Book.objects.filter(id=3).delete()
#queryset类型数据可以调用delete方法删除查询结果数据

# 方法2
# 	models.Book.objects.get(id=4).delete()

# 4 修改
# 修改方式1  通过queryset类型数据修改
# 	models.Book.objects.filter(id=5).update(
# 	price=20,
# 	title='读书'
# 	)

	# models.Book.objects.get(id=5).update(
	# 	price=30, #报错:模型类对象不能调用update方法
	# )
# 'Book' object has no attribute 'update'

# 修改方式2  通过模型类对象来修改
# 	ret = models.Book.objects.get(id=5)
# 	ret.price = 30
# 	ret.title = '健身'
# 	ret.save()

# DatetimeField、DateField、TimeField这个三个时间字段，都可以设置如下属性
# (7)auto_now_add
#     配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库。
#
# (8)auto_now
#     配置上auto_now=True，每次更新数据记录的时候会更新该字段，
#     标识这条记录最后一次的修改时间。

# 测试auto_now和auto_now_add两个参数
# 新添加的数据的模型类对象
# 	models.userinfo.objects.create(
# 		name='xx3',
# 	)

	# models.userinfo.objects.filter(id=1).update(
	# 	# (  #update不能触发自动更新时间的auto_now参数的作用,
	# 	# 	# 如果用update方法来更新记录,并保存更新记录的时间,
	# 	# 	需要我们手动给该字段传入当前时间
	# 	name='投资',
	# 	b1 = datetime.datetime.now()
	# )

# 这种save方式能够触发auto_now参数自动更新修改时间的动作
# 	ret = models.userinfo.objects.get(id=1)
# 	ret.name = '读书'
# 	ret.save()

	# 基于双下划线的模糊查询
# 查询书名以少年开头的哪些书
# 	obj_list = models.Book.objects.filter(title__startswith='少年')
# 	#以什么开头
# 	print(obj_list)
# #<QuerySet [<Book: 少年闰土1>, <Book: 少年闰土2>,

# 	obj_list = models.Book.objects.filter(title__endswith='梅')
# #以什么结尾
# 	print(obj_list)
# # <QuerySet [<Book: 金瓶梅>, <Book: 金瓶梅>]>

	# obj_list = models.Book.objects.filter(title__startswith='p')
	# print(obj_list)
# <QuerySet [<Book: python少年闰土1>]>

# 	obj_list = models.Book.objects.filter(title__istartswith='p')
# #不区分大小写
# 	print(obj_list)
# # <QuerySet [<Book: python少年闰土1>, <Book: Python少年闰土2>]>

# 	obj_list = models.Book.objects.filter(title__contains='th')
# #包含
# 	print(obj_list)
# # <QuerySet [<Book: Python少年闰土2>]>

# 	obj_list = models.Book.objects.filter(title__icontains='th')
# #包含 不区分大小写
# 	print(obj_list)
# # <QuerySet [<Book: pytHon少年闰土1>, <Book: Python少年闰土2>]>

# 	obj_list = models.Book.objects.filter(price__gt=18) #大于
# 	print(obj_list)
# # <QuerySet [<Book: 健身>, <Book: 少年闰土9>]>

	# obj_list = models.Book.objects.filter(price__gte=19) #大于等于
	# print(obj_list)
# <QuerySet [<Book: 健身>, <Book: 少年闰土9>]>

	# obj_list = models.Book.objects.filter(price__lt=10) #小于
	# print(obj_list)
	# #<QuerySet [<Book: 金瓶梅>, <Book: 金瓶梅>]>

	# obj_list = models.Book.objects.filter(price__lte=10)  #小于等于
	# print(obj_list)
# QuerySet [<Book: 金瓶梅>, <Book: 金瓶梅>, <Book: 少年闰土0>]>

# 	obj_list = models.Book.objects.filter(price__in=[15,18,30])
# #价格等于15或者等于18或者等于30的书籍
# 	print(obj_list)
# #<QuerySet [<Book: 健身>, <Book: 少年闰土5>, <Book: 少年闰土8>]>

# 	obj_list = models.Book.objects.filter(price__range=[15,17])
# #价格大于等于15并且小于等于17, between and
# 	print(obj_list)
#<QuerySet [<Book: 少年闰土5>, <Book: 少年闰土6>, <Book: 少年闰土7>]>

# 	obj_list = models.Book.objects.filter(id=10,price=15)
# #逗号连接的查询条件就是and的关系
# 	print(obj_list)
# <QuerySet [<Book: 少年闰土5>]>

# 	obj_list = models.Book.objects.filter(pub_date__year='2020')
# #2020年的所有书籍
# 	print(obj_list)
# # <QuerySet [<Book: 少年闰土1>]>

# 	obj_list = models.Book.objects.filter\
# 		(pub_date__year='2020',pub_date__month='04')
# #2020年4月份的所有书籍
# 	print(obj_list)
# # <QuerySet [<Book: 少年闰土1>]>

# 	obj_list = models.Book.objects.filter(pub_date__year='2020',
# 	                                      pub_date__month='04',
# 	                                      pub_date__day='11')
# # 2020年4月11号的所有书籍  方法1
# 	print(obj_list)
# # # <QuerySet [<Book: 少年闰土1>]>

	obj_list = models.Book.objects.filter(pub_date = '2020-04-11')
# # 2020年4月11号的所有书籍  方法2  推荐
	print(obj_list)
# # # <QuerySet [<Book: 少年闰土1>]>

	return HttpResponse('ok')




















