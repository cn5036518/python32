from django.db import models

# Create your models here.
# 属性对应的字段,默认都是不能为空的,也就是加了not null约束
class Book(models.Model):
	# 如果没有指定主键字段,默认orm会给这个表添加一个名称为id的主键自增字段
	# 如果指定了,以指定的为准,那么orm不在创建那个id字段了
	# nid = models.AutoField(primary_key=True) #int primary_key auto_increment.
	title = models.CharField(max_length=32) # varchar 书籍名称
	# price = models.FloatField()
	price = models.DecimalField(max_digits=5,decimal_places=2) # 999.99 价格
	pub_date = models.DateField() # date 出版日期
	publish = models.CharField(max_length=32) # 出版社名称
	# xx = models.CharField(max_length=18,null=True,blank=True)
# null=True,blank=True允许该字段数据为空
# 	xx = models.CharField(max_length=18,default='xxx')
#设置默认值
	def __str__(self):
		# 打印一个对象，让他显示一个能够看懂的值，__str__，
		# models.py的数据表类里面定义一个__str__方法就可以了

		# 后添加这个str方法，也不需要重新执行同步数据库的指令
		# 当我们打印这个类的对象的时候，显示title值
		return self.title

# Book生成的表名称为 应用名称_模型类名小写

# 查看orm的field对应MySQL的什么字段类型在下面看
# C:\Program Files\Python37\Lib\site-packages\django\db\backends\mysql\base.py


class userinfo(models.Model):
	name = models.CharField(max_length=12)
	b1 = models.DateTimeField(auto_now=True)
# 自动添加修改时间 (第一次也是添加的创建记录的时间)
	b2 = models.DateTimeField(auto_now_add=True)
# 自动添加创建记录的时间
















