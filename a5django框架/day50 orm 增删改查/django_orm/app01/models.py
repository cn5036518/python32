from django.db import models

# Create your models here.


# 属性对应的字段,默认都是不能为空的,也就是加了not null约束
class Book(models.Model):

	# 如果没有指定主键字段,默认orm会给这个表添加一个名称为id的主键自增字段
	# 如果制定了,以指定的为准,那么orm不在创建那个id字段了
	# nid = models.AutoField(primary_key=True)  #int primary_key auto_increment,
	# select * from book where title='xxx'
	title = models.CharField(max_length=32)  #varchar 书籍名称
	# price = models.FloatField()  #
	price = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99 价格
	pub_date = models.DateField()  # date  出版日期
	publish = models.CharField(max_length=32)  #出版社名称
	# xx = models.CharField(max_length=18, null=True, blank=True)  # null=True,blank=True允许该字段数据为空
	# xx = models.CharField(max_length=18, default='xxx')  # null=True,blank=True允许该字段数据为空

	def __str__(self):
		return self.title
# 删表和删字段都是注释相关类和属性,再执行数据库同步指令



class userinfo(models.Model):

	name = models.CharField(max_length=12)
	b1 = models.DateTimeField(auto_now=True)
	#自动添加修改时间 (第一次也是添加的创建记录的时间)
	b2 = models.DateTimeField(auto_now_add=True)
# 自动添加创建记录的时间

# python manage.py makemigrations
# python manage.py migrate
# 执行上面的2个命令,可以完成新建表

# python manage.py runserver
# 起django服务




