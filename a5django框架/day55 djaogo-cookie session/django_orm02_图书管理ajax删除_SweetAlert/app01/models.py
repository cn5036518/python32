from django.db import models

# Create your models here.

# 作者表
class Author(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField()  #默认级联删除

# 出版社表
class Publish(models.Model):
	name = models.CharField(max_length=32)
	city = models.CharField(max_length=32)
	
# 书籍表
class Book(models.Model):
	title = models.CharField(max_length=32)
	PublishDate = models.DateField()  #不是pub_date 
	price = models.DecimalField(max_digits=5,decimal_places=2)
	
	publishs = models.ForeignKey('Publish')
	authors = models.ManyToManyField('Author')
	
	# 方法1 
	# def get_authors_name(self):
	# 	authors = self.authors.all() 
	# 	name_list = []
	# 	for i in authors:
	# 		name_list.append((i.name))
	# 	name_str = ','.join(name_list)
	# 	return  name_str
	
	# 方法2
	def get_authors_name(self):
		return ','.join([i.name for i in self.authors.all()])
	# 列表推导式























