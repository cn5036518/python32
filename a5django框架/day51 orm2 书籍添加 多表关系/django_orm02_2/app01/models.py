from django.db import models

# Create your models here.

# 一对一:作者表和作者详细信息表
# 一对多:出版社表和书籍表
# 多对多:书籍表和作者表

# 作者表
class Author(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField()

# django2.x版本必须手动指定on_delete=models.CASCADE级联模式
# 	au = models.OneToOneField(
# 		to='AuthorDetail',to_field='id',on_delete=models.CASCADE())  #01全写
# 	au = models.OneToOneField('AuthorDetail')  #02简写 有外键关联关系
# 	au = models.IntegerField() # 03无外键关联关系 无法使用orm提供的属性和方法
	au = models.OneToOneField('AuthorDetail',db_constraint=False) #04推荐
	# db_constraint=False取消foreign key的强制约束效果,
# 还可以继续使用orm的提供的属性或者方法来操作关系记录
	# foreign key + unique   一对一关系  上述au字段也可以写在AuthorDetail表

# 属性是OneToOneField或者ForeignKey,那么生成的对应字段是  属性名称_id
# 比如:  au_id

# 作者详细信息表
class AuthorDetail(models.Model):
	birthday = models.DateField()
	# telephone = models.BigIntegerField()
	telephone = models.CharField(max_length=32)
	addr = models.CharField(max_length=64)

# 出版社表
class Publish(models.Model):
	name = models.CharField(max_length=32)
	city = models.CharField(max_length=32)

#书籍表
class Book(models.Model):
	title = models.CharField(max_length=32)
	publishDate = models.DateField()
	price = models.DecimalField(max_digits=5,decimal_places=2)

	# publishs = models.ForeignKey(
	# 	to='Publish',to_field='id',on_delete=models.CASCADE) #01全写
	publishs = models.ForeignKey('Publish')  #简写
	# 出版社和书籍表 一对多关系,上述publishs字段必须写在-多 处
	authors = models.ManyToManyField('Author')
	#  书籍表和作者表 多对多关系 上述authors字段可以写在Author表(待确认)
#      authors不是一个Book表的字段,会自动产生一个多对多的关系表

# class authortobook(models.Model):
# 	book_id = models.ForeignKey('Book')
# 	author_id = models.ForeignKey('Author')

#注意点:
#执行数据库同步指令前,最好是新建一个新的mysql库,然后把settings中的mysql的库名指向新的库名
# 不要用已有的库,已有的库执行同步指令后,会出现数据表未创建出来的情况,换新的库后,执行数据库同步指令后,就正常了























