from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.

from app01.models import Book
from app01.models import Author
from app01.models import AuthorDetail
from app01.models import Publish


def query(request):
	# 一 多表的增删改查
	# 01增
	# 一对一关系的添加
	# 先创建作者详细信息表记录(被关联的表)
	# ret = models.AuthorDetail.objects.create(
	# 	birthday='2000-12-12',
	# 	telephone='122',
	# 	addr='惠州',
	# )
	#
	# 再创建作者表
	# models.Author.objects.create(
	# 	name='元涛',
	# 	age=18,
	# 	# au_id=ret.id,  #如果用的是属性名称_id,那么值为关联记录的id值  推荐
	# 	au=ret,  #如果写属性名称来添加关系数据,那么值为关联记录的模型类对象记录
	# )


	# 一对多  出版社表和书籍表
	# pub_obj = models.Publish.objects.get(id=1)

	# models.Book.objects.create(
	# 	title='白洁2',
	# 	price=10,
	# 	publishDate='1980-07-07',
	# 	# publishs=pub_obj, #如果写属性名称来添加关系数据,那么值为关联记录的模型类对象
	# 	publishs_id=2, #如果用的是属性名称_id,那么值为关联记录的id值
	# 	publishs_id=pub_obj_id, #如果用的是属性名称_id,那么值为关联记录的id值   推荐
	#
	# )

	# 多对多  作者表和书籍表

	# book_obj = models.Book.objects.get(title='金鳞岂是池中物')
	# author1 = models.Author.objects.get(id=1)
	# author2 = models.Author.objects.get(id=2)

	# book_obj.authors.add(author1,author2)
	# book_obj.authors.add(1, 2)
	# 书籍对象记录.关联字段.add(作者对象1,作者对象2)
	# 实质是往第三张关系表中添加记录

	#02 修改  只能用filter+update  因为get不支持updata方法
	# 一对一   作者表和作者详细表
	# Author.objects.filter(id=1).update(
	# 	age=19,
	# 	au_id=3,  #方法1 推荐
	# 	# au = AuthorDetail.objects.get(id=4),  #方法2
	# )

	# Book.objects.get(id=5).update(  # 报错:模型类对象不能调用update方法
	# 	price=30,
	# )  # 报错 'Book' object has no attribute 'update'

	# 一对多  出版社表和书籍表
	# Book.objects.filter(id=1).update(
	# 	title='白洁1',
	# 	publishs_id=2,  #方法1 推荐
	# 	# publishs = Publish.objects.get(id=1),  #方法2
	# )

	# 多对多  书籍表和作者表
	# 正向,通过关联属性字段
	# obj = Book.objects.get(id=3)
	# obj.authors.set(['2','3'])   #clear + add
	# 书籍对象记录.关联字段.set(['作者1-id','作者2-id'])
	# # 更新,先清空book_id为3的第三张表里的记录,再添加3 2和3 3记录
	# models中必须加上 db_constraint=False取消foreign key的强制约束效果,
	# # 还可以继续使用orm的提供的属性或者方法来操作关系记录


	# 03删除  	# 外键关联到这条作者详细记录的都会被删除(级联模式下)
	# 一对一  作者表和作者详细表 (关联字段在作者表)
	# 作者表关联作者详细表,作者详细表删除一条记录,作者表会级联删除,
	# 如果没有添加级联删除,则不允许删除作者详细表中有关联的数据
	# 反之不会,作者表删除一条记录,作者详细表不会级联删除

	# Author.objects.get(id=4).delete()  #不会级联删除
	# AuthorDetail.objects.get(id=4).delete() #会级联删除

	# 一对多   出版社表和书籍表(关联字段在书籍表)
	# 书籍表关联出版社表,出版社表删除一条记录,书籍表会级联删除,
	# 反之不会,书籍表删除一条记录,出版社表不会级联删除
	# Book.objects.get(id=1).delete()  #不会级联删除
	# Publish.objects.get(id=1).delete() #会级联删除

	# 多对多删除   书籍表和作者表(关联字段在书籍表)  不存在级联删除
	#只是对第三张关系表进行记录删除
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

	# 001 删除单条  remove
	# book_obj.authors.remove(6)
	# 书籍对象记录.关联字段.remove(作者id)
	# 删除第三张表中 书籍id为4 并且作者id为6的记录

	# 002 全部删除(清空)  clear
	# book_obj = Book.objects.get(id=5)
	# book_obj.authors.clear()
	# 清空  第三张表中的书籍id为5的所有记录

	# 003 删除多条  remove
	# book_obj = Book.objects.get(id=5)
	# book_obj.authors.remove(6,8) #删除多条  方法1
	# book_obj.authors.remove(*[6,8]) #删除多条 方法2
	# 删除第三张表中 书籍id为5 并且作者id为6和8的记录


	#二 基于对象的跨表查询  子查询
	# 01一对一  作者表和作者详细表 (关联字段在作者表)
	#  正向查询(关系属性在哪个表里面,通过这个表的数据去查询另外一张表的数据,就是正向查询,反之就是反向查询)
	# 正向查询靠关联属性字段,反向查询靠表名小写(一对一)或表名小写_set(一对多 多对多)

	# 查询一下元涛这个作者的手机号
	# 正向查询  正向查询靠关联属性字段
	# obj = Author.objects.get(name='元涛')
	# obj.au   #这就找到了关联的详细信息表里面的那个对象记录
	# print(obj.au.telephone)  #122

	# 查询手机号为111的作者姓名
	# 反向查询  反向查询靠表名小写(一对一)
	# obj = AuthorDetail.objects.get(telephone='111')
	# obj.author  #这就找到了关联的作者表里面的那个对象记录
	# print(obj.author.name)  #元涛2


	# 02一对多 出版社表和书籍表(关联字段在书籍表 多)
	#正向查询(关系属性在哪个表里面,
	#       通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询  正向查询靠关联属性字段
	# 001查询 <读书> 这本书是哪个出版社出版的?
	# obj = Book.objects.get(title='读书')
	# obj.publishs  #找到了关联的出版社记录
	# print(obj.publishs.name)  #读书出版社

	# 002查询读书出版社出版了哪些书(多本书)
	# 反向查询
	# 反向查询在一对多的关系是,使用 表名小写_set
	# obj = Publish.objects.get(name='读书出版社')
	# # obj.book_set.filter()  #类似于objects控制器
	# books = obj.book_set.all()  #queryset
	# for i in books:
	# 	print(i.title)
	# 	# 读书
	# 	# 读书2

	# 03多对多  书籍表和作者表(关联字段在书籍表)  不存在级联删除
	# 001查询一下读书这本书的作者是谁
	# 正向查询(关系属性在哪个表里面,
	#       通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询  正向查询靠关联属性字段
	# obj = Book.objects.filter(title='读书')
	# print(obj) #<QuerySet [<Book: Book object>]>
	# obj = obj.first()
	# print(obj) #Book object
	#
	# objs = obj.authors.all()
	# print(objs) #<QuerySet [<Author: Author object>]>
	# for i in objs:
	# 	print(i.name)  #元涛

	# 002查询一下元涛写了哪些书
	# 反向查询
	# 反向查询在多对多的关系是,使用 表名小写_set
	# obj = Author.objects.get(name='元涛')
	# objs = obj.book_set.all()
	# for i in objs:
	# 	print(i.title)  #读书


	#小结
	# 基于对象的跨表查询	子查询
	# # 正向查询(关系属性在哪个表里面,
	# #       通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询靠关联属性字段,反向查询靠表名小写

	# 一对一
	# 	正向查询    正向查询靠关联属性字段
	# 	反向查询    反向查询靠表名小写

	# 一对多
	# 	正向查询   正向查询靠关联属性字段
	# 	反向查询    反向查询在一对多的关系是,使用 表名小写_set

	# 多对多
	# 	正向查询    正向查询靠关联属性字段
	# 	反向查询    反向查询在多对多的关系是,使用 表名小写_set


	#三 基于双下划线的跨表查询 -- mysql连表查询
	# select app01_authordetail.telephone 
	# from app01_author inner join app01_authordetail on 
	# app01_author.au_id = app01_authordetail.id;

	# select app01_authordetail.telephone 
	# from app01_authordetail inner join app01_author 
	# on app01_author.au_id = app01_authordetail.id;

	# 正向查询靠关联属性字段, 反向查询靠表名小写

	# 01一对一的  出版社表和书籍表(关联字段在书籍表)
	# 查询一下元涛这个作者的手机号
	# 方法1 正向查询    正向查询靠关联属性字段
	# ret = Author.objects.filter(name='元涛').values('au__telephone')
	# print(ret)  #<QuerySet [{'au__telephone': '122'}]>
	# print(ret[0])  #{'au__telephone': '122'}
	# print(ret[0]['au__telephone'])  #122
	#  values中的关联字段__实现跨表(连表)

	# # 方法2 反向查询  反向查询靠表名小写
	# ret = AuthorDetail.objects.filter(author__name='元涛').values('telephone')
	# print(ret) #<QuerySet [{'telephone': '122'}]>
	# print(ret[0])  #{'telephone': '122'}
	# print(ret[0]['telephone'])  #122
	# filter中的表名小写__实现跨表(连表)

	# 02一对多的  出版社表和书籍表(关联字段在书籍表)
	# 查询<读书>这本书是哪个出版社出版的
	# 方法1 正向查询    正向查询靠关联属性字段
	# ret = Book.objects.filter(title='读书').values('publishs__name')
	# print(ret)  #<QuerySet [{'publishs__name': '读书出版社'}]>
	# print(ret[0])  #{'publishs__name': '读书出版社'}
	# 正向查询  values中的关联字段__实现跨表(连表)

	# 方法2 反向查询    反向查询靠表名小写
	# ret = Publish.objects.filter(book__title='读书').values('name')
	# print(ret)  #<QuerySet [{'name': '读书出版社'}]>
	# print(ret[0]) #{'name': '读书出版社'}
	# 反向查询  filter中的表名小写__实现跨表(连表)
	
	# 03多对多  书籍表和作者表(关联字段在书籍表)  不存在级联删除
	#  查询一下<读书>这本书的作者是谁
	# 方法1 正向查询    正向查询靠属性
	# ret = Book.objects.filter(title='读书').values('authors__name')
	# print(ret)  #<QuerySet [{'authors__name': '元涛'}]>
	# print(ret[0])  #{'authors__name': '元涛'}
	# 正向查询  values中的关联字段__实现跨表(连表)

	# 方法2 反向查询    反向查询靠表名小写
	# ret = Author.objects.filter(book__title='读书').values('name')
	# print(ret)  #<QuerySet [{'name': '元涛'}]>
	# print(ret[0])   #{'name': '元涛'}
	# 反向查询  filter中的表名小写__实现跨表(连表)


	# 小结
	# 基于双下划线的跨表查询 -- mysql连表查询
	# # 正向查询(关系属性在哪个表里面,
	# #       通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询靠关联属性字段,反向查询靠表名小写

	# 一对一
	# 一对多
	# 多对多
	# 上述3种情况,写法是一样的
	# 正向查询  values中的关联字段__实现跨表
	# 反向查询  filter中的表名小写__实现跨表

	
	from django.db.models import Avg,Max,Min,Sum,Count
	
	#四 聚合查询    aggregate
	# 查询所有书籍的平均价格 最大价格
	# 方法1
	# ret = Book.objects.all().aggregate(Avg('price'),Max('price'))
	# print(ret)  #{'price__avg': 9.5, 'price__max': Decimal('10.00')}

	# # 方法2
	# ret = Book.objects.aggregate(Avg('price'),Max('price'))
	# print(ret)  #{'price__avg': 9.5, 'price__max': Decimal('10.00')}
	# #字典类型数据,
	#
	# # 别名
	# ret = Book.objects.aggregate(m=Max('price'),a=Avg('price'))
	# print(ret)  #{'m': Decimal('10.00'), 'a': 9.5}

	# 五 分组查询  -- group by    annotate
	# 01查询每个出版社出版书的平均价格
	# 默认是用Publish的id字段值作为分组依据,
	# 自动会找book表里面的publishs_id去分组
	# 方法1   连表查询
	# 反向查询(通过出版社找书)  表名小写__实现连表
	# ret = Publish.objects.annotate(a=Avg('book__price')).values('a','name','city')
	# print(ret)
	# < QuerySet[{'name': '读书出版社', 'city': '沙河2', 'a': 9.5},
	# {'name': '健身出版社', 'city': '沙河3','a': None}] >
	# 表名小写__实现连表

	#原生sql
	# select
	# 	avg(t2.price),t1.name
	# from
	# 	app01_publish as t1,app01_book as t2
	# where
	# 	t1.id = t2.publishs_id
	# group by
	# 	t1.id;

	# 方法2  单表查询  推荐 更简洁
	# 按照publishs_id进行分组
	# ret = Book.objects.values('publishs_id').annotate(a=Avg('price'))
	# print(ret)  #<QuerySet [{'publishs_id': 2, 'a': 9.5}]>

	#sql
	# select
	# 	avg(price)
	# from
	# 	app01_book
	# group by
	# 	publishs_id;

	# 02每个作者出版书的最高价格
	# 别忘了:  1.检查数据正确性   2.剔除无用数据
	# 方法1   连表查询
	# 反向查询(通过作者表找书籍表)  annotate后的Max后的表名小写__
	# 默认按照author_id进行分组
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# print(ret)
	# < QuerySet[{'name': '元涛', 'm': Decimal('10.00')},
	# {'name': '元涛2', 'm': None}] >
	# annotate后的Max后的表名小写__实现连表

	# django orm翻译后的sql用的是左连接,所以有none

	# 方法2  单表查询  推荐 更简洁
	# 正向查询(通过书籍找作者) values后面按照关联属性字段__
	# 按照authors_id进行分组-annotate
	# ret = Book.objects.values('authors__id').annotate(m=Max('price'))
	# print(ret)
	# < QuerySet[{'authors__id': 6, 'm': Decimal('10.00')},
	# {'authors__id': None, 'm': Decimal('9.00')}] >


	# 注意:一定要起别名a=
	# #结果为Publish模型类对象,对象中有本表字典数据

	# django orm翻译后的sql用的是左连接,所以有none
	# SELECT 
	#   `app01_book_authors`.`author_id`, 
	#   MAX(`app01_book`.`price`) AS `m` 
	# FROM `app01_book` LEFT OUTER JOIN `app01_book_authors` ON 
	# (`app01_book`.`id` = `app01_book_authors`.`book_id`) 
	# GROUP BY `app01_book_authors`.`author_id` 
	# ORDER BY NULL LIMIT 21;

#课后作业
	# 1 查询每个作者的姓名以及出版的书的最高价格
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# print(ret)
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# print(ret)
	# print(ret[0])  #{'name': '元涛', 'm': Decimal('10.00')}
	# < QuerySet[{'name': '元涛', 'm': Decimal('10.00')},
	# {'name': '元涛2', 'm': None}] >

	# 2 查询作者id大于2作者的姓名以及出版的书的最高价格
	# 默认按照authors_id进行分组
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# # ret.filter(Author_id__gt=2)
	# ret = ret.filter(id__gt=2)
	# print(ret)
	# < QuerySet[{'name': '元涛', 'm': Decimal('10.00')}, {'name': '元涛2', 'm': None}] >

	# 3 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书的最高价格
	# ret = Author.objects.annotate(m=Max('book__price')).values('name', 'm')
	# ret = ret.filter(id__gt=2)
	# 或者 如何写?

	# 4 查询每个作者出版的书的最高价格 的平均值
	# ret = Author.objects.annotate(m=Max('book__price')).values('name','m')
	# ret = ret.aggregate(a = Avg('m'))
	# print(ret)  #{'a': 10.0}

	# annotate 分组
	# aggregate 聚合

	# day51单表的增删改查

	# day53多表的增删改查
	# 一对一
	# 一对多
	# 多对多
	#
	# 正向查询  关联属性字段   关系属性在哪个表里面,通过这个表的数据去查询另外一张表的数据,就是正向查询
	# 反向查询  表名小写

	# 基于对象的跨表查询	子查询
	# 基于双下划线的跨表查询 -- mysql连表查询
	# 聚合查询 aggregate
	# 分组查询  annotate



	return HttpResponse('ok')











