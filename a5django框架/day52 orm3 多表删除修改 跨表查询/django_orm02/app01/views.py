from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.



def query(request):
	# 一 多表的增删改查
	# 增
	# 一对一关系的添加
	# 先创建作者详细信息表记录
	# ret = models.AuthorDetail.objects.create(
	# 	birthday='2000-12-12',
	# 	telephone='122',
	# 	addr='惠州',
	# )
	#
	#
	# models.Author.objects.create(
	# 	name='元涛',
	# 	age=18,
	# 	# au_id=ret.id,  #如果用的是属性名称_id,那么值为关联记录的id值
	# 	au=ret,  #如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	# )


	# 一对多
	# pub_obj = models.Publish.objects.get(id=1)
	# obj_list = []
	# import random
	# for i in range(10):
	# 	obj = models.Book(
	# 		title=f'佛经{i}',
	# 		price=10 + i,
	# 		publishDate=f'198{i}-07-07',
	# 		# publishs=pub_obj, #如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	# 		publishs_id=random.randint(1, 3),  # 如果用的是属性名称_id,那么值为关联记录的id值
	# 	)
	# 	obj_list.append(obj)
	# models.Book.objects.bulk_create(obj_list)
	# models.Book.objects.create(
	# 	title='白洁3',
	# 	price=10,
	# 	publishDate='1980-07-07',
	# 	# publishs=pub_obj, #如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	# 	publishs_id=1, #如果用的是属性名称_id,那么值为关联记录的id值
	#
	# )

	# 多对多

	# book_obj = models.Book.objects.get(title='金鳞岂是池中物')
	# author1 = models.Author.objects.get(id=1)
	# author2 = models.Author.objects.get(id=2)


	# book_obj.authors.add(author1,author2)
	# book_obj.authors.add(1, 2)

	# 03删除  	# 外键关联到这条作者详细记录的都会被删除(级联模式下)
	# 一对一  作者表和作者详细表 (关联字段在作者表)
	# 作者表关联作者详细表,作者详细表删除一条记录,作者表会级联删除,
	# 反之不,作者表删除一条记录,作者详细表不会级联删除
	# models.Author.objects.get(id=4).delete()  #不会级联删除
	# models.AuthorDetail.objects.get(id=4).delete()  # 会级联删除

	# 一对多   出版社表和书籍表(关联字段在书籍表)
	# 书籍表关联出版社表,出版社表删除一条记录,书籍表会级联删除,
	# 反之不会,书籍表删除一条记录,出版社表不会级联删除
	# Book.objects.get(id=1).delete()  #不会级联删除
	# Publish.objects.get(id=1).delete() #会级联删除

	# 多对多删除   书籍表和作者表(关联字段在书籍表)  不存在级联删除
	# 只是对第三张关系表进行删除
	# book_obj = Book.objects.get(id=4)
	# print(book_obj,type(book_obj))
	# 书的对象记录

	# book_obj = Book.objects.filter(id=4)
	# print(book_obj, type(book_obj))
	# #QuerySet
	#
	# book_obj = Book.objects.filter(id=4)[0]
	# print(book_obj, type(book_obj))
	# # 书的对象记录

	# book_obj.authors.remove(6)
	# 删除第三张表中 书籍id为4 并且作者id为6的记录

	# book_obj = Book.objects.get(id=5)
	# book_obj.authors.clear()
	# 清空  第三张表中的书籍id为5的所有记录


	#02 修改
	# 一对一   作者表和作者详细表
	# Author.objects.filter(id=1).update(
	# 	age=19,
	# 	au_id=3,  #方法1 推荐
	# 	# au = AuthorDetail.objects.get(id=4),  #方法2
	# )

	# 一对多  出版社表和书籍表
	# Book.objects.filter(id=1).update(
	# 	title='白洁1',
	# 	publishs_id=2,  #方法1 推荐
	# 	# publishs = Publish.objects.get(id=1),  #方法2
	# )

	# 多对多  书籍表和作者表
	# obj = models.Book.objects.get(id=3)
	# obj.authors.set(['2', '3'])  # clear + add
	# 更新,先清空book_id为3的第三张表里的记录,再添加3 2和3 3记录
	# models中必须加上 db_constraint=False取消foreign key的强制约束效果,
	# # 还可以继续使用orm的提供的属性或者方法来操作关系记录



	#二 基于对象的跨表查询  子查询

	# 一对一  作者表和作者详细表 (关联字段在作者表)
	#  正向查询(关系属性在哪个表里面,通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询靠属性字段,反向查询靠表名小写

	# 查询一下元涛这个作者的手机号
	# 正向查询  正向查询靠属性字段
	# obj = Author.objects.get(name='元涛')
	# obj.au   #这就找到了关联的详细信息表里面的那个记录对象
	# print(obj.au.telephone)  #122
	#
	# # 查询手机号为111的作者姓名
	# # 反向查询  反向查询靠表名小写
	# obj = AuthorDetail.objects.get(telephone='111')
	# obj.author  #这就找到了关联的作者表表里面的那个记录对象
	# print(obj.author.name)  #元涛2


	# 一对多   出版社表和书籍表(关联字段在书籍表)
	# 正向查询
	# 查询白洁1这本书是哪个出版社出版的
	# obj = models.Book.objects.get(title='白洁1')
	# obj.publishs   #找到了关联的出版社记录
	# print(obj.publishs.name)

	# 查询闻哥出版社出版了哪些书
	# 反向查询
	# 反向查询在一对多的关系是,使用  表名小写_set
	# obj = models.Publish.objects.get(name='闻哥出版社')
	# obj.book_set.filter()   #类似于objects控制器
	# books = obj.book_set.all()
	# for book in books:
	# 	print(book.title)


	# 多对多   书籍表和作者表(关联字段在书籍表)  不存在级联删除
	# 查询一下白洁2这本书的作者是谁
	# 正向查询
	# obj = models.Book.objects.filter(title='白洁2').first()
	# obj.authors.all()  #类似objects控制器

	# objs = obj.authors.all()
	# for i in objs:
	# 	print(i.name)


	# 查询一下何导写了哪些书
	# 反向查询
	# 反向查询在多对多的关系是,使用 表名小写_set
	# obj = models.Author.objects.get(name='何导')
	# objs = obj.book_set.all()
	# for i in objs:
	# 	print(i.title)




	#####基于双下划线的跨表查询 -- mysql连表查询
	# select app01_authordetail.telephone
	# from app01_author inner join app01_authordetail on
	# app01_author.au_id = app01_authordetail.id;

	# select app01_authordetail.telephone
	# from app01_authordetail inner join app01_author
	# on app01_author.au_id = app01_authordetail.id;

	# 正向查询靠属性, 反向查询靠表名小写

	# 一对一的  出版社表和书籍表(关联字段在书籍表)
	# 查询一下元涛这个作者的手机号
	# 方法1 正向查询    正向查询靠属性
	# ret = Author.objects.filter(name='元涛').values('au__telephone')
	# print(ret)  #<QuerySet [{'au__telephone': '122'}]>
	# print(ret[0])  #{'au__telephone': '122'}
	# print(ret[0]['au__telephone'])  #122
	#
	# # 方法2 反向查询  反向查询靠表名小写
	# ret = AuthorDetail.objects.filter(author__name='元涛').values('telephone')
	# print(ret) #<QuerySet [{'telephone': '122'}]>
	# print(ret[0])  #{'telephone': '122'}
	# print(ret[0]['telephone'])  #122


	# 一对多的  出版社表和书籍表(关联字段在书籍表)
	# 查询读书这本书是哪个出版社出版的
	# 方法1 正向查询    正向查询靠属性
	# ret = Book.objects.filter(title='读书').values('publishs__name')
	# print(ret)  #<QuerySet [{'publishs__name': '读书出版社'}]>
	# print(ret[0])  #{'publishs__name': '读书出版社'}

	# 方法2 反向查询    反向查询靠表名小写
	# ret = Publish.objects.filter(book__title='读书').values('name')
	# print(ret)  #<QuerySet [{'name': '读书出版社'}]>
	# print(ret[0]) #{'name': '读书出版社'}


	# 多对多
	#  查询一下白洁2这本书的作者是谁
	# ret = models.Book.objects.filter(title='白洁2').values('authors__name')
	# <QuerySet [{'authors__name': '闻哥'}, {'authors__name': '何导'}]>
	# print(ret)

	# ret = models.Author.objects.filter(book__title='白洁2').values('name')
	# print(ret) #<QuerySet [{'name': '何导'}, {'name': '闻哥'}]>

	from django.db.models import Avg,Max,Min,Sum,Count

	# 四 聚合查询
	# 查询所有书籍的平均 最大价格
	# 方法1
	# ret = Book.objects.all().aggregate(Avg('price'),Max('price'))
	# print(ret)  #{'price__avg': 9.5, 'price__max': Decimal('10.00')}

	# 方法2
	# ret = Book.objects.aggregate(Avg('price'), Max('price'))
	# print(ret)  # {'price__avg': 9.5, 'price__max': Decimal('10.00')}
	# # 字典类型数据,
	#
	# # 别名
	# ret = Book.objects.aggregate(m=Max('price'), a=Avg('price'))
	# print(ret)  # {'m': Decimal('10.00'), 'a': 9.5}



	# 五 分组查询  -- group by
	# 01查询每个出版社出版书的平均价格
	# 默认是用Publish的id字段值作为分组依据,自动会找book表里面的publishs_id去分组
	# 方法1   连表查询
	# ret = models.Publish.objects.annotate(a=Avg('book__price')).values('a','name','city')

	# select t1.name,t1.city,avg(t2.price)
	# from app01_publish as t1 inner join app01_book as t2
	# on t1.id = t2.publishs_id group by t1.id;

	#<QuerySet [{'name': '32期桔色成人出版社', 'city': '沙河', 'a': 12.5},
	# {'name': '闻哥出版社', 'city': '松兰堡', 'a': 14.0},
	# {'name': '牡丹花出版社', 'city': '洛阳', 'a': 13.75}]>

	# 方法2  单表查询
	# ret = models.Book.objects.values('publishs_id').annotate(a=Avg('price'))
	# select avg(price) from app01_book group by publishs_id;
	# print(ret)

	# 02每个作者出版书的最高价格
	# 别忘了:  1.检查数据正确性   2.剔除无用数据
	# 方法1
	# 反向查询  表名小写
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# print(ret)
	# < QuerySet[{'name': '元涛', 'm': Decimal('10.00')},
	# {'name': '元涛2', 'm': None}] >

	# django翻译后的sql用的是左连接,所以有none

	# 方法2
	# 按照authors_id进行分组-annotate
	# ret = Book.objects.values('authors__id').annotate(m=Max('price'))
	# print(ret)
	# < QuerySet[{'authors__id': 6, 'm': Decimal('10.00')},
	# {'authors__id': None, 'm': Decimal('9.00')}] >

	# django翻译后的sql用的是左连接,所以有none

	# 注意:一定要起别名a=
	# #结果为Publish模型类对象,对象中有本表字典数据






	return HttpResponse('ok')











