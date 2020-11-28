from django.shortcuts import render, HttpResponse

# Create your views here.
from app01 import models
import datetime


def query(request):

	# # 添加数据记录  方式1
	# new_book = models.Book(
	# 	# id=2,
	# 	title='金瓶梅',
	# 	price=9.9,
	# 	# pub_date=datetime.datetime.now(),  #添加时间日期类型数据时可以是时间日期类型的数据,也可以是字符串数据
	# 	pub_date='2022-02-02',
	# 	publish='32期红浪漫出版社'
	# 	# 有默认值的或者可以为空的或者主键字段,都可以不用传值
	# )
	# new_book.save()
	#
	# # 添加方式2 create方法,create方法的返回值为 新添加的数据的模型类对象
	# new_book = models.Book.objects.create(
	# 	title='金瓶梅4',
	# 	price=19.9,
	# 	# pub_date=datetime.datetime.now(),
	# 	pub_date='2022-04-02',
	# 	publish='32期红浪漫出版社'
	# )
	#
	# print(new_book.title)  #通过模型类对象,直接获取属性对应的值
	# print(new_book.price)

	# 批量添加数据
	# 方法1
	# obj_list = []
	# for i in range(10):
	# 	book_obj = models.Book(
	# 		title=f'少年阿宾{i}',
	# 		price=10 + i,
	# 		pub_date=f'2022-04-1{i}',
	# 		publish='32期红浪漫出版社'
	#
	# 	)
	# 	obj_list.append(book_obj)
	#
	# models.Book.objects.bulk_create(obj_list)  #bulk_create 批量添加

	# 方法2  推荐 更简洁
	# for i in range(5):
	# 	Book.objects.create(
	# 		title=f'读书{i}',
	# 		price=10+i,
	# 		pub_date=f'2020-02-1{i}',
	# 		publish='读书出版社',
	# 	)

	# 查询所有书籍
	# book_objs = models.Book.objects.all()  #queryset 类似于列表
	# book_objs = models.Book.objects.filter(id=3) #<QuerySet [<Book: 金瓶梅3>]>
	# book_objs = models.Book.objects.get(id=3) # 模型类对象

	# print(book_objs)  #金瓶梅3
	# print(book_objs[0],type(book_objs[0]))  #模型类对象
	# print(book_objs[0].title)
	# ret = models.Book.objects.filter()  # filter没有加条件,和all一样的效果
	# models.Book.objects.get(id=4).delete()
	# ret = models.Book.objects.filter(id=100)
	# ret2 = models.Book.objects.get(id=100)
	# print(ret)
	# print(ret2)

	# # 修改方式1
	# models.Book.objects.filter(id=5).update(
	# 	price=20,
	# 	title='xxxx'
	# )
	# models.Book.objects.get(id=5).update(
	# 	price=30,
	# )

	# ret = models.Book.objects.get(id=5)
	# ret.price = 30
	# ret.title = '少年阿宾00'
	# ret.save()


	# 测试auto_now和auto_now_add两个参数
	# models.userinfo.objects.create(
	# 	name='xx3',
	# )

	# models.userinfo.objects.filter(id=1).update(  #update不能触发自动更新时间的auto_now参数的作用,
	# 	# 如果用update方法来更新记录,并保存更新记录的时间,需要我们手动给该字段传入当前时间
	# 	name='xxoo',
	# 	b1=datetime.datetime.now()
	#
	# )

	# 这种save方式能够触发auto_now参数自动更新修改时间的动作
	# ret = models.userinfo.objects.get(id=2)
	# ret.name='xxoo2'
	# ret.save()



	# 查询书名以少年开头的哪些书
	# obj_list = models.Book.objects.filter(title__startswith='少年')  #以什么开头
	# obj_list = models.Book.objects.filter(title__endswith='梅') #以什么结尾
	# obj_list = models.Book.objects.filter(title__startswith='p')  #区分大小写
	# obj_list = models.Book.objects.filter(title__istartswith='p')  #不区分大小写
	# obj_list = models.Book.objects.filter(title__contains='th') #包含
	# obj_list = models.Book.objects.filter(title__icontains='th') #包含 不区分大小写

	# obj_list = models.Book.objects.filter(price__gt=15)  大于
	# obj_list = models.Book.objects.filter(price__gte=15)  大于等于
	# obj_list = models.Book.objects.filter(price__lt=15)  小于
	# obj_list = models.Book.objects.filter(price__lte=15)  小于等于

	# obj_list = models.Book.objects.filter(price=15 or price=18 or price=30)
	# obj_list = models.Book.objects.filter(price__in=[15,18,30])  价格等于15或者等于18或者等于30的书籍
	# obj_list = models.Book.objects.filter(price__range=[15, 20])  #价格大于等于15并且小于等于20, between and

	# obj_list = models.Book.objects.filter(id=10, price=15)  #逗号连接的查询条件就是and的关系
	# obj_list = models.Book.objects.filter(pub_date__year='2020')  #2020年的所有书籍
	# obj_list = models.Book.objects.filter(pub_date__year='2020',pub_date__month='11')  #2020年11月份的所有书籍
	# obj_list = models.Book.objects.filter(pub_date__year='2020',pub_date__month='11',pub_date__day='25')  #2020年11月5号的所有书籍
	# obj_list = models.Book.objects.filter(pub_date='2020-11-25')  #2020年11月5号的所有书籍

	# exclude排除
	# 返回结果为queryset类型数据,通过objects控制器可以调用,queryset类型数据也能调用
	# obj_list = models.Book.objects.exclude(id=2)
	# obj_list = obj_list.filter(title='少年阿宾1')
	# obj_list = obj_list.all()
	# obj_list = models.Book.objects.exclude(id=2).filter(title__contains='少年').exclude(id=5)

	# order_by 排序
	# 返回结果为queryset类型数据,queryset类型数据可以调用这个方法
	# obj_list = models.Book.objects.all().order_by('-id')   #-id加个-号表示按照该字段降序排列, desc  asc
	# '''select * from app01_book order by id desc;'''
	# obj_list = models.Book.objects.all().order_by('price', '-id') #按照价格升序排列,价格相同的按照id降序排列

	# reverse()
	# 翻转必须在排序数据的基础上
	# 返回结果为queryset类型数据,queryset类型数据可以调用这个方法
	# obj_list = models.Book.objects.all().order_by('-id').reverse()

	# count
	# queryset类型数据可以调用这个方法,返回值为数字
	# obj_list = models.Book.objects.all().count()

	# first\last
	# queryset类型数据可以调用这个方法,返回值为模型类对象
	# obj_list = models.Book.objects.all().first()
	# obj_list = models.Book.objects.all()[0]
	# obj_list = models.Book.objects.all().last()

	# exists
	# 判断查询结果是有数据
	# queryset类型数据可以调用这个方法
	# obj_list = models.Book.objects.all().exists()  #判断是否有数据的效率高,只找一条记录 limit 1


	# values
	# 可以获取指定字段数据
	# objects可以调用, queryset也能调用,返回结果还是queryset,内容为一个个字典数据
	# obj_list = models.Book.objects.values('title', 'price')
	# obj_list = models.Book.objects.filter(id=5).values('title', 'price')

	# values_list
	# 可以获取指定字段数据,返回结果还是queryset,内容为一个个元组数据
	# obj_list = models.Book.objects.values_list('title', 'price')
	# obj_list = models.Book.objects.filter(id=5).values_list('title', 'price')

	# distinct 去重
	# 一般配合values和values_list来使用
	obj_list = models.Book.objects.values('price').distinct()

	print(obj_list)




	return HttpResponse('ok')

