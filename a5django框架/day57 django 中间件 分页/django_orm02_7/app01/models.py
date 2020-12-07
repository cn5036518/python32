from django.db import models

# Create your models here.

# 左侧菜单表
class Menu(models.Model):
	title = models.CharField(max_length=10)
	url = models.CharField(max_length=20)
	#跳转地址
	icon = models.CharField(max_length=32,null=True,blank=True)
	# 允许为空  菜单的图标
	#菜单有图标,用户表的用户也可以存头像

# 登录用户表
class UserInfo(models.Model):
	username = models.CharField(max_length=32)
	password = models.CharField(max_length=32)
	phone_number = models.CharField(max_length=18)
	avatar = models.CharField(max_length=64,null=True,blank=True)
	#这里默认非空,设置允许为空
	email = models.EmailField() # 底层也是CharField
	#上述4个属性字段的名字建议和模板中的input标签的name属性保持一致

	menus = models.ManyToManyField('Menu')  #参数是另外一张表对应的类名
	# 登录用户表UserInfo和左侧菜单表Menu  多对多

# 作者表
class Author(models.Model):
	name = models.CharField( max_length=32)
	age = models.IntegerField()

	# django2.x版本必须手动指定on_delete=models.CASCADE级联模式
	# au = models.OneToOneField(to="AuthorDetail", to_field="id", on_delete=models.CASCADE)
	# au = models.OneToOneField("AuthorDetail")
	# au = models.IntegerField()
	au = models.OneToOneField("AuthorDetail")
	# db_constraint=False取消foreign key的强制约束效果,还可以继续使用orm的提供的属性或者方法来操作关系记录
	# foreign key + unique

# 属性是OneToOneField或者ForeignKey,那么生成的对应字段是  属性名称_id

#作者详细信息表
class AuthorDetail(models.Model):
	birthday=models.DateField()
	# telephone=models.BigIntegerField()
	telephone=models.CharField(max_length=32)
	addr=models.CharField(max_length=64)

# 出版社表
class Publish(models.Model):
	name=models.CharField( max_length=32)
	city=models.CharField( max_length=32)


#书籍表
class Book(models.Model):

	title = models.CharField( max_length=32)
	publishDate=models.DateField()
	price=models.DecimalField(max_digits=5,decimal_places=2)

	# publishs=models.ForeignKey(to="Publish",to_field="id",on_delete=models.CASCADE)
	publishs=models.ForeignKey("Publish")
	authors = models.ManyToManyField('Author')

	dianzan = models.IntegerField(default=1)
	comment = models.IntegerField(default=1)


	# def get_authors_name(self):
	# 	authors = self.authors.all()
	# 	name_list = []
	# 	for i in authors:
	# 		name_list.append(i.name)
	# 	name_str = ','.join(name_list)
	# 	return name_str

	def get_authors_name(self):

		return ','.join([i.name for i in self.authors.all()])

# class authortobook(models.Model):
# 	book_id = models.ForeignKey('Book')
# 	author_id = models.ForeignKey('Author')
