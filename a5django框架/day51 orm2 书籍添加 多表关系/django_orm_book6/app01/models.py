from django.db import models

# Create your models here.
# 属性对应的字段,默认都是不能为空的,也就是加了not null约束

# 作者表
class Author(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField()

	def __str__(self):
		return self.name

# 出版社表
class Publish(models.Model):
	name = models.CharField(max_length=32)
	city = models.CharField(max_length=32)

	# def __str__(self):
	# 	return self.name

# 书籍表
# 出版社表和书籍表  一对多
# 作者表和书籍表   多对多
class Book(models.Model):
	title = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	pub_date = models.DateField()

	publishs = models.ForeignKey('Publish')
	#一对多关联字段
	authors = models.ManyToManyField('Author')
	# 多对多 生成第三个表

	def __str__(self):
		return self.title





































