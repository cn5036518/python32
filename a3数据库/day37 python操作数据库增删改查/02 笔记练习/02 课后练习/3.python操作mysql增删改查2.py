# ### python 操作mysql 数据库 (增删改查)
import pymysql
	# python 操作mysql增删改时,默认是开启事务的,
	# 必须最后commit提交数据,才能产生变化
	
	# 提交数据: commit 
	# 默认回滚: rollback

conn = pymysql.connect(
host = '127.0.0.1',
user = 'root',
password = '123456',
database = 'db006'
)
# 默认获取查询结果时是元组,可以设置返回字典;  cursor=pymysql.cursors.DictCursor
#cursor = conn.cursor()  
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  #推荐字典

# 执行对mysql 的操作
# 1.创建一张表
# sql = """
# create table t1(
# id int unsigned primary key auto_increment,
# first_name varchar(255) not null,
# last_name varchar(255) not null,
# sex tinyint not null,
# age tinyint unsigned not null,
# money float
# );
# """
# res = cursor.execute(sql)
# print(res)  0  #建表返回无意义

# 1.增
sql = 'insert into t1 values(%s,%s,%s,%s,%s)'
# 主键自增必须指定字段才行
sql = 'insert into t1(first_name,last_name,sex,age,money) \
values(%s,%s,%s,%s,%s)'

# (1) 一次插入一条  #参数2是元组
# res = cursor.execute(sql,('孙','键',0,15,20000))
# print(res) #1
# # 获取最后插入这条数据的id号
# print(cursor.lastrowid)

# (2) 一次插入多条  #参数2是列表
# res = cursor.executemany(sql,
# [('孙','键2',0,15,20000),
# ('孙','键3',0,15,20000)]
# )
# print(res)  # 返回插入的条数 

# 插入2条数据中的第一条数据的id
# print(cursor.lastrowid)

# 获取最后一个数据的id
# sql = 'select id from t1 order by id desc limit 1'
# sql = 'select id from t1 order by id asc limit 1'
# res = cursor.execute(sql)
# print(res)

sql = "select id from t1 order by id desc limit 1"
res = cursor.execute(sql)
print(res)  #1  返回查询的结果的条数

# 获取结果,返回元组
res = cursor.fetchone()
print(res)  #{'id': 22}
print(res['id'])  #22
print('----------------1')

# 2.删
sql = 'delete from t1 where id in (%s,%s,%s)'
res = cursor.execute(sql,(6,7,8))  #参数2是元组
print(res)  # 返回的是3,代表删除了3条

if res:
	print('删除成功')
else:
	print('删除失败')
print('----------------2')

# 3.改
# 01修改单条数据
sql = 'update t1 set first_name = "王" where id = %s'
res = cursor.execute(sql,(1,))
print(res) #1  代表修改了1条   #如果,修改前已经是姓王了,就会显示0,表示0条被修改

# 02修改多条数据
sql = 'update t1 set first_name = "王" where id in (%s,%s)'
res = cursor.execute(sql,(21,22))
print(res)  #2  代表修改了2条   

if res:
	print('修改成功')
else:
	print('修改失败')
print('----------------3')


# 4.查
# """
# fetchone  获取一条
# fetchmany 获取多条
# fetchall  获取所有
# """

sql = 'select * from t1'
res = cursor.execute(sql)
print(res)  #16 针对于查询语句来说,返回的res是总条数;

# (1) fetchone 获取一条
res = cursor.fetchone()
print(res)
#{'id': 1, 'first_name': '王', 'last_name': '键', 'sex': 0, 'age': 15, 'money': 20000.0}

res = cursor.fetchone()
print(res)
# {'id': 2, 'first_name': '孙', 'last_name': '键', 'sex': 0, 'age': 15, 'money': 20000.0}

# (2) fetchmany 获取多条
res = cursor.fetchmany()
#默认获取的是一条数据,返回列表,里面里面是一组一组的字典;
print(res)
# [{'id': 9, 'first_name': '王', 'last_name': '键2', 'sex': 0, 'age': 15, 'money': 20000.0}]

data = cursor.fetchmany(2)
print(data)
# [{'id': 10, 'first_name': '孙', 'last_name': '键3', 'sex': 0, 'age': 15, 'money': 20000.0}, 
# {'id': 11, 'first_name': '孙', 'last_name': '健', 'sex': 0, 'age': 15, 'money': 20000.0}]

# 把字典拼接成字符串,通过json传给前端
for i in data:
	first_name = i['first_name']
	last_name = i['last_name']
	sex = i['sex']
	if sex == 0:
		sex = '男'
	else:
		sex = '女'
	age = i['age']
	money = i['money']
	strvar = '姓:{},名:{},性别:{},年龄:{},收入:{}'\
	.format(first_name,last_name,sex,age,money)
print(strvar)
#姓:孙,名:健,性别:男,年龄:15,收入:20000.0

# (3) fetchall 获取所有
data = cursor.fetchall()
print(data)
print('----------------4-3')

# (4) 自定义搜索查询的位置
# 1.相对滚动 relative
# """相对于上一次查询的位置往前移动(负数),或者往后移动(正数)"""
cursor.scroll(-1,mode='relative')
res = cursor.fetchone()
print(res)
# {'id': 22, 'first_name': '王', 'last_name': '大奥', 'sex': 1, 'age': 20, 'money': 80000.0}

# 2.绝对滚动 absolute
# """永远从数据的开头起始位置向后进行移动,不能向前滚"""
cursor.scroll(0,mode='absolute')
res = cursor.fetchone()
print(res)
# {'id': 1, 'first_name': '王', 'last_name': '键', 'sex': 0, 'age': 15, 'money': 20000.0}

























conn.commit()  #写操作,必须提交才能生效
cursor.close()
conn.close()
































