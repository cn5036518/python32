# ### python 操作mysql 数据库 (增删改查)
import pymysql
# """
	# python 操作mysql增删改时,默认是开启事务的,
	# 必须最后commit提交数据,才能产生变化
	
	# 提交数据: commit 
	# 默认回滚: rollback
	
# """

# conn = pymysql.connect(host="127.0.0.1",user="root",password="123456",database="db005")
conn = pymysql.connect(
						host="127.0.0.1",
						user="root",
						password="123456",
						database="db006")

# 默认获取查询结果时是元组,可以设置返回字典;  cursor=pymysql.cursors.DictCursor
# cursor = conn.cursor()
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
##推荐字典

# 执行对mysql 的操作

# 1.增
# """
sql = "insert into t1(first_name,last_name,sex,age,money) values(%s,%s,%s,%s,%s)"
# 注意点:主键自增的,insert的时候,t1后面必须列出sex,age等字段,t1后面省略全部字段可能会报错
# (1) 一次插入一条   #参数2是元组
res = cursor.execute( sql , ("孙","健",0,15,20000)  )
print(res) # 1  #返回插入成功的条数

# 获取最后插入这条数据的id号
print(cursor.lastrowid)

# (2) 一次插入多条
# 方式1
res = cursor.execute(sql,("孙","健",0,15,20000))
res = cursor.execute(sql,("孙","健2",0,15,20000))

# 方式2    #参数2是列表 里面嵌套元组
res = cursor.executemany(  sql , 
[  ("安","晓东",0,18,30000) , 
("刘","玉波",1,20,50000) ,
("张","光旭",0,80,60000) , 
("李","是元",0,10,10) , 
("高","大奥",1,20,80000)   ]   )

print(res) # 5 返回插入成功的条数

# 插入5条数据中的第一条数据的id
print(cursor.lastrowid)
# 如果没有插入一条或者多条数据. 直接打印,就会报错
# AttributeError: 'DictCursor' object has no attribute 'lastrowid'

# 获取最后一个数据的id
sql = "select id from t1 order by id desc limit 1"
res = cursor.execute(sql)
print(res)  #1  返回查询的结果的条数
# 这里的1 不是最后一个数据的id

# 获取结果(最后一个数据的id),返回元组
res = cursor.fetchone()
print(res)
# {'id': 48}
print(res["id"])
# 48

# 默认元组 : (57, '高', '大奥', 1, 20, 80000.0)
# 返回字典 : {'id': 51, 'first_name': '高', 'last_name': '大奥', 'sex': 1, 'age': 20, 'money': 80000.0}
# """

# 2.删
# """
sql = "delete from t1 where id in (%s,%s,%s)"
res = cursor.execute(sql , (3,4,5) )
print(res) # 返回的是3,代表删除成功了3条

if res:
	print("删除成功")
else:
	print("删除失败")
# """

# 3.改
# 3.改
# 01 修改单条记录
sql = "update t1 set first_name = '王' where id = %s"
res = cursor.execute(sql,(2,)) #参数2是元组
print(res)  # 返回的是1,代表修改成功了1条

if res:
	print('修改成功')
else:
	print('修改失败')
print('---------------------3-1')
	
# 02 修改多条记录
sql = "update t1 set first_name = '王' where id in (%s,%s)"
res = cursor.execute(sql,(14,15)) #参数2是元组
print(res)  # 返回的是2,代表修改成功了2条

if res:
	print('修改成功')
else:
	print('修改失败')

# 4.查
# """
# fetchone  获取一条
# fetchmany 获取多条
# fetchall  获取所有
# """	

sql = "select * from t1"
res = cursor.execute(sql)
print(res) #48 针对于查询语句来说,返回的res是总条数;

# (1) fetchone 获取一条
res = cursor.fetchone()
print(res)
res = cursor.fetchone()
print(res)
# {'id': 1, 'first_name': '王', 'last_name': '键', 'sex': 0, 'age': 15, 'money': 20000.0}
# {'id': 2, 'first_name': '王', 'last_name': '键', 'sex': 0, 'age': 15, 'money': 20000.0}

# (2) fetchmany 获取多条
res = cursor.fetchmany() 
# 默认获取的是一条数据,返回列表,里面是一组一组的字典;
# 注意点:获取的数据是从上面fetchone之后的数据 类似生成器
# 上面fetchone获取第1 2条数据,这里就从第3条数据开始获取
data = cursor.fetchmany(3)  #获取3条数据
print(data)
# """
[
	{'id': 9, 'first_name': '王', 'last_name': '是元', 'sex': 0, 'age': 10, 'money': 10.0}, 
	{'id': 10, 'first_name': '孙', 'last_name': '健', 'sex': 0, 'age': 15, 'money': 20000.0}, 
	{'id': 11, 'first_name': '安', 'last_name': '晓东', 'sex': 0, 'age': 18, 'money': 30000.0}
]
# """

# 把字典拼接成字符串,通过json传给前端
for row in data:
	first_name = row["first_name"]
	last_name = row["last_name"]
	sex = row["sex"]
	if sex == 0:
		sex = "男性"
	else:
		sex = "女性"
	age = row["age"]
	money = row["money"]
	strvar = "姓:{},名:{},性别:{},年龄:{},收入:{}"
	.format(first_name,last_name,sex,age,money)
print(strvar)

# (3) fetchall 获取所有
# data = cursor.fetchall()
# print(data)

# (4) 自定义搜索查询的位置
print("<==================>")
# 1.相对滚动 relative
# """相对于上一次查询的位置往前移动(负数),或者往后移动(正数)"""
# """
cursor.scroll(-1,mode="relative")
# cursor.scroll(5,mode="relative")
res = cursor.fetchone()
print(res)
# """
# 2.绝对滚动 absolute
# """永远从数据的开头起始位置向后进行移动,不能向前滚"""
cursor.scroll(0,mode="absolute")
res = cursor.fetchone()
print(res)

conn.commit()
cursor.close()
conn.close()



























