# ### python 操作mysql 
import pymysql

# ### 1.基本语法

# (1) 创建连接对象 host user password database 这四个参数必写
conn = pymysql.connect(
host='127.0.0.1',
user='root',
password='123456',
database='db003',
charset='utf8',   #不能是utf-8  不写默认是utf8
port=3306)  #不写默认是3306

# (2) 创建游标对象 (用来操作数据库的增删改查)
cursor = conn.cursor()
print(cursor)
#<pymysql.cursors.Cursor object at 0x7fefa7ef60b8>

# (3) 执行sql语句
sql = 'select * from employee'  #末尾的;可以加也可以不加

# 执行查询语句返回的总条数
res = cursor.execute(sql)
print(res)  #18

# (4) 获取数据 fetchone 获取一条数据
# 返回的是元组,里面包含的是第一条的完整数据
res = cursor.fetchone()
print(res)
# (1, 'egon', 'male', 18, datetime.date(2017, 3, 1), '老男孩驻沙河办事处外交大使', None, 7300.33, 401, 1)

res = cursor.fetchone()
print(res)
# (2, 'alex', 'male', 78, datetime.date(2015, 3, 2), 'teacher', None, 1000000.31, 401, 1)

res = cursor.fetchone()
print(res)
# (3, 'wupeiqi', 'male', 81, datetime.date(2013, 3, 5), 'teacher', None, 8300.0, 401, 1)

# (5) 释放游标对象
cursor.close()

# (6) 释放连接对象
conn.close()

# ### 2.创建/删除 表操作
conn = pymysql.connect(
host = '127.0.0.1',
user = 'root',
password = '123456',
database = 'db003'
)
cursor = conn.cursor()

# 1.创建一张表
sql = '''
create table t1(
id int unsigned primary key auto_increment,
first_name varchar(255) not null,
last_name varchar(255) not null,
sex tinyint not null,
age tinyint unsigned not null,
money float
)
'''
# res = cursor.execute(sql)
# print(res)  # 无意义返回值
# pymysql.err.OperationalError: (1050, "Table 't1' already exists")
# 第二次创建会报错 因为表已经存在了

# 2.查询表结构
# sql = 'desc t1'
# res = cursor.execute(sql)
# print(res) #返回的是字段的个数  #6

# res = cursor.fetchone()
# print(res) #('id', 'int(10) unsigned', 'NO', 'PRI', None, 'auto_increment')

# res = cursor.fetchone()
# print(res)  #('first_name', 'varchar(255)', 'NO', '', None, '')

# res = cursor.fetchone()
# print(res)  #('last_name', 'varchar(255)', 'NO', '', None, '')

# 3.删除表
try:
	sql = 'drop table t1'
	res = cursor.execute(sql)
	print(res)  #无意义返回值
	#pymysql.err.ProgrammingError: (1146, "Table 'db003.t1' doesn't exist")
	# 第二次删除会报错 因为表已经不存在了
except:
	pass

# ### 3.事务处理
# """pymysql 默认开启事务的,所有增删改的数据必须提交commit,否则默认回滚;rollback"""
conn = pymysql.connect(
host = '127.0.0.1',
user = 'root',
password = '123456',
database = 'db003'
)
cursor = conn.cursor()
sql1 = 'begin'
sql2 = 'update employee set emp_name = "程咬钻石" where id = 18'
sql3 = 'commit'  #提交

res1 = cursor.execute(sql1)
res1 = cursor.execute(sql2)
res1 = cursor.execute(sql3)
# 一般在查询的时候,通过fetchone来获取结果
res1 = cursor.fetchone()
print(res1) #None

cursor.close()
conn.close()
























































