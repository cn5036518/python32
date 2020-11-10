# ### python 操作mysql 
import pymysql

# ### 1.基本语法
# """
# (1) 创建连接对象 host user password database 这四个参数必写
conn = pymysql.connect( host="127.0.0.1" , user="root" , password="123456" , database="db003" , charset="utf8" , port=3306 )

# (2) 创建游标对象 (用来操作数据库的增删改查)
cursor = conn.cursor()  #默认是元组，可以设置成字典
print(cursor)

# (3) 执行sql语句
sql = "select * from employee"
# 执行查询语句返回的总条数
res = cursor.execute(sql)
print(res)  #18

# (4) 获取数据 fetchone 获取一条数据
# 返回的是元组,里面包含的是第一条的完整数据
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)

# (5) 释放游标对象
cursor.close()

# (6) 释放连接对象
conn.close()
# """

# ### 2.创建/删除 表操作
# conn = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db003")
# cursor = conn.cursor()

# 1.创建一张表
sql = """
create table t1(
id int unsigned primary key auto_increment,
first_name varchar(255) not null,
last_name varchar(255) not null,
sex tinyint not null,
age tinyint unsigned not null,
money float
);
"""
# res = cursor.execute(sql)
# print(res) #0 创建表 返回值无意义

# 2.查询表结构
# """
sql = "desc t1"
res = cursor.execute(sql)
print(res) #6 返回的是字段的个数

res = cursor.fetchone()
print(res)  #获取第一个字段的信息
# ('id', 'int(10) unsigned', 'NO', 'PRI', None, 'auto_increment')

res = cursor.fetchone()
print(res)  #获取第2个字段的信息
res = cursor.fetchone()
print(res)  #获取第3个字段的信息

# """
# 3.删除表
# """
try:
	sql = "drop table t1"
	res = cursor.execute(sql)
	print(res) # 0 删除表 返回值无意义
except:
	pass
# """

# ### 3.事务处理
# """pymysql 默认开启事务的,所有增删改的数据必须提交commit,否则默认回滚;rollback"""
# 新建表、删除表drop、清空表truncate 无法rollback
conn = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db003")
cursor = conn.cursor()
sql1 = "begin"  #开启事务
sql2 = "update employee set emp_name='程咬钻石' where id = 18 "
sql3 = "commit"  #提交事务

res1 = cursor.execute(sql1)
# print(res1) #0
res1 = cursor.execute(sql2)
# print(res1) #0
res1 = cursor.execute(sql3)
# print(res1) #0

# 一般在查询的时候,通过fetchone来获取结果
res1 = cursor.fetchone()
# print(res1) #None


cursor.close()
conn.close()
















