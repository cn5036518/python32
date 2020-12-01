from django.shortcuts import render, HttpResponse, redirect
from app01 import models
# Create your views here.



def query(request):
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



	# 删除  	# 外键关联到这条作者记录的都会被删除(级联模式下)
	# 一对一
	# models.Author.objects.get(id=1).delete()
	# models.AuthorDetail.objects.get(id=2).delete()

	# 一对多
	# models.Book.objects.get(id=1).delete()
	# models.Publish.objects.get(id=2).delete()


	# 多对多删除
	# book_obj = models.Book.objects.get(id=6)
	# book_obj = models.Book.objects.filter(id=5)[0]
	# book_obj.authors.remove(1)  # 4   1  删除第三张表中id为4 并且作者id为1的记录
	# book_obj.authors.clear()  # 清空 第三张表中的书籍id为5的所有记录
	# book_obj.authors.remove(1, 4)  #删除多条
	# book_obj.authors.remove(*[1, 4]) #删除多条


	# 修改
	# 一对一
	# models.Author.objects.filter(id=3).update(
	# 	age=38,
	# 	# au_id=5,
	# 	# au=models.AuthorDetail.objects.get(id=5),
	# )




	# 一对多
	# models.Book.objects.filter(id=4).update(
		# title='白洁1',
		# publishs=models.Publish.objects.get(id=2),
		# publishs_id=2
	# )

	# 多对多

	# obj = models.Book.objects.get(id=5)
	# obj.authors.set(['1','3'])
	# #clear + add  更新,先清空book_id为5的第三张表里的记录,
	# 再添加5 1和5 3记录



	# 基于对象的跨表查询

	# 一对一的
	#  正向查询(关系属性在哪个表里面,通过这个表的数据去查询另外一张表的数据,就是正向查询)
	# 正向查询靠属性,反向查询靠表名小写

	# 查询一下闻哥这个作者的手机号
	# obj = models.Author.objects.get(name='闻哥')
	# obj.au   #这就找到了关联的详细信息表里面的那个记录对象
	# print(obj.au.telephone)

	# 查询手机号为555的作者姓名
	# obj = models.AuthorDetail.objects.get(telephone='555')
	# obj.author   #这就找到了关联的作者表表里面的那个记录对象
	# print(obj.author.name)



	# 一对多
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


	# 多对多
	# 查询一下白洁2这本书的作者是谁
	# 正向查询
	# obj = models.Book.objects.filter(title='白洁2').first()
	# obj.authors.all()  #类似objects控制器

	# objs = obj.authors.all()
	# for i in objs:
	# 	print(i.name)


	# 查询一下何导写了哪些书
	# 反向查询
	# obj = models.Author.objects.get(name='何导')
	# objs = obj.book_set.all()
	# for i in objs:
	# 	print(i.title)




	#####基于双下划线的跨表查询 -- mysql连表查询
	# select app01_authordetail.telephone from app01_author inner join app01_authordetail on app01_author.au_id = app01_authordetail.id;
	# select app01_authordetail.telephone from app01_authordetail inner join app01_author on app01_author.au_id = app01_authordetail.id;

	# 正向查询靠属性, 反向查询靠表名小写

	# 一对一的
	# 查询一下闻哥这个作者的手机号
	# ret = models.Author.objects.filter(name='闻哥').values('au__telephone')
	# <QuerySet [{'au__telephone': '222'}]>
	# 反向查询
	# ret  = models.AuthorDetail.objects.filter(author__name='闻哥').values('telephone')
	# print(ret)  #<QuerySet [{'telephone': '222'}]>


    # 一对多的
	# 查询白洁1这本书是哪个出版社出版的
	# ret = models.Book.objects.filter(title='白洁1').values('publishs__name')
	# <QuerySet [{'publishs__name': '闻哥出版社'}]>
	# print(ret)

	# ret = models.Publish.objects.filter(book__title='白洁1').values('name')
	# print(ret)  #<QuerySet [{'name': '闻哥出版社'}]>

	# 多对多
	#  查询一下白洁2这本书的作者是谁
	# ret = models.Book.objects.filter(title='白洁2').values('authors__name')
	# <QuerySet [{'authors__name': '闻哥'}, {'authors__name': '何导'}]>
	# print(ret)

	# ret = models.Author.objects.filter(book__title='白洁2').values('name')
	# print(ret) #<QuerySet [{'name': '何导'}, {'name': '闻哥'}]>

	from django.db.models import Avg,Max,Min,Sum,Count

	# 聚合查询
	# 查询所有书籍的平均价格
	# ret = models.Book.objects.all().aggregate(Avg('price'))
	# ret = models.Book.objects.aggregate(Max('price'),Avg('price'))
	# {'price__max': Decimal('19.00')} 字典类型数据,
	# ret = models.Book.objects.aggregate(m=Max('price'), a=Avg('price'))
	#
	# print(ret)



	# 分组查询  -- group by
	# 查询一下每个出版社出版书的平均价格
	# 默认是用Publish的id字段值作为分组依据,自动会找book表里面的publishs_id去分组
	# ret = models.Publish.objects.annotate(a=Avg('book__price')).values('a','name','city')
	# select t1.name,t1.city,avg(t2.price) from app01_publish as t1 inner join app01_book as t2 on t1.id = t2.publishs_id group by t1.id;

	#<QuerySet [{'name': '32期桔色成人出版社', 'city': '沙河', 'a': 12.5}, {'name': '闻哥出版社', 'city': '松兰堡', 'a': 14.0}, {'name': '牡丹花出版社', 'city': '洛阳', 'a': 13.75}]>


	# ret = models.Book.objects.values('publishs_id').annotate(a=Avg('price'))
	# select avg(price) from app01_book group by publishs_id;
	# print(ret)


	# 每个作者出版书的最高价格
	# 别忘了:  1.检查数据正确性   2.剔除无用数据
	# ret = models.Author.objects.annotate(m=Max('book__price')).values('name','m')
	# <QuerySet [{'name': '苑昊', 'm': None}, {'name': '何导', 'm': Decimal('17.00')}, {'name': '闻哥', 'm': Decimal('19.00')}]>
	# print(ret)



	# ret = models.Book.objects.values('authors__id').annotate(m=Max('price'))
	# <QuerySet [{'authors__id': '苑昊', 'm': 123},
	# 注意:一定要起别名a=  #结果为Publish模型类对象,对象中有本表字典数据
	# id name city a
	# print(ret)
	# ret = models.Author.objects.annotate(m=Max('book__price')).values('name', 'm')

	# ret = models.Author.objects.filter(id__gt=3).annotate(m=Max('book__price')).values('name', 'm')

	# ret = models.Author.objects.annotate(m=Max('book__price')).values('name', 'm').aggregate(Avg('m'))
	# print(ret)

	from django.db.models import F,Q
	# 1查询一下点赞数大于评论数的所有书籍
	# 方法1
	# books = models.Book.objects.all()
	# books_list = []
	# for book in books:
	# 	if book.dianzan > book.comment:
	# 		books_list.append(book)

	# 方法2
	# books = models.Book.objects.filter(dianzan__gt=F('comment'))  #F('属性名称')
	# print(books.values('title'))


	# 2所有书籍价格上调10块钱
	# 方法1 普通写法
	# books = models.Book.objects.all()
	# for book in books:
	# 	book.price += 10
	# 	book.save()

	#方法2 F查询
	# models.Book.objects.all().update(price=F('price')+10)
	# #支持四则运算

	# Q查询, 多条件查询的时候用的多, or查询
	# 1查询一下点赞数大于10或者评论数大于10的所有书籍
	# models.Book.objects.filter(Q(dianzan__gt=10) & Q(comment__gt=10))
	#   #| -- or   & -- and  ~ -- not
	# models.Book.objects.filter(dianzan__gt=10, comment__gt=10)
	# ret = models.Book.objects.filter(Q(dianzan__gt=10) | Q(comment__gt=10)).values('title')

	# 2点赞数大于10或者评论数大于10的并且价格大于30的
	# 方法1
	# ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) & Q(price__gt=30)).values('title')

	# 方法2
	# ret = models.Book.objects.filter(Q(dianzan__gt=10) | Q(comment__gt=10) , price__gt=30).values('title')
	#Q(dianzan__gt=10) | Q(comment__gt=10)
	# 通过连接符号连接的Q查询条件,算是一组查询条件
	# print(ret)

	# ret = models.Book.objects.filter(Q(Q(dianzan__gt=10) | Q(comment__gt=10)) & ~Q(price__gt=30)).values('title')
	# print(ret)



	return HttpResponse('ok')



from django.urls import reverse  # 别名解析

def books(request):
	print(reverse('books'))
	#/books/  #reverse('别名')来反向解析别名对应的路径
	print(reverse('add_book'))  #/add_book/  #/add_book/v1/

	print(reverse('edit_book',args=(3, )))  # /edit_book/2/
	# print(reverse('del_book',args=(3, )))
	# 当url用的是无名分组参数时,reverse反向解析路径用args来传参

	print(reverse('del_book', kwargs={'book_id': 3, }))
	#当url用的是有名分组参数时,reverse反向解析路径用kwargs来传参
	book_objs = models.Book.objects.all()

	return render(request, 'books.html', {'book_objs': book_objs})


from django.views import View


class AddBook(View):

	def get(self,request):
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		return render(request, 'add_book.html', {'publish_objs': publish_objs, 'author_objs': author_objs})

	def post(self,request):
		# request.POST.get('authors')
		authors = request.POST.getlist('authors')
		# ['3', '4', '5']  #获取多选数据时,用getlist方法
		# get只能获取最后一个数据
		# print(request.POST)
		# print(authors2)
		data = request.POST.dict()
		#注意:含有多选数据时,先提取多选数据,再使用dict,
		# 不然,dict会返回多选的最后一个结果值
		# print(data)
		data.pop('authors')  # ['3', '4']
		# print(authors)

		# 保存数据到数据库-书籍表  单表添加
		book_obj = models.Book.objects.create(
			**data
			# publishs=模型类对象,
			# publishs_id=3,
		)

		# 保存数据到数据库-书籍和作者关系表  多对多添加
		book_obj.authors.add(*authors) # ['4', '5']

		# return redirect(reverse('books',args=(1,2,3,)))
		# return redirect(reverse('books',kwargs={'book_id':1,}))
		return redirect('books') #/books/



class EditBook(View):

	def get(self,request,book_id):
		old_book_obj = models.Book.objects.get(id=book_id)
		publish_objs = models.Publish.objects.all()
		author_objs = models.Author.objects.all()
		# print(reverse('edit_book', args=(book_id, )))
		return render(request, 'edit_book.html', {'old_book_obj': old_book_obj, "publish_objs": publish_objs, 'author_objs': author_objs})

	def post(self,request, book_id):

		authors = request.POST.getlist('authors')  # [2, 3]
		data = request.POST.dict()
		data.pop('authors')
		old_obj = models.Book.objects.filter(id=book_id)
		# 修改书籍表  get不支持update方法
		old_obj.update(  # update返回值是受影响的条数,是个整数数字
			**data
		)

		# 修改书籍-作者关系表  多对多
		old_obj.first().authors.set(authors)#参数是列表
		# old_obj 是queryset
		# old_obj.first()  是对象记录

		# obj = models.Book.objects.get(id=5)
		# obj.authors.set(['1','3'])
		# #clear + add  更新,先清空book_id为5的第三张表里的记录,
		# 再添加5 1和5 3记录

		return redirect('books')


def del_book(request,book_id):
	models.Book.objects.get(id=book_id).delete()  # 默认级联删除
	return redirect('books')