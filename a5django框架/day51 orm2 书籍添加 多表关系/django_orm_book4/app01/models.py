from django.db import models

# Create your models here.
# 属性对应的字段,默认都是不能为空的,也就是加了not null约束
class Book(models.Model):
	title = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	pub_date = models.DateField()
	publish = models.CharField(max_length=32)
	
	def __str__(self):
		return self.title