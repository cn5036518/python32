# ### sql 注入攻击
import pymysql
# (1) sql注入的现象
# ''' 现象:绕开账号密码登录成功 '''
# '''
user = input("请输入您的用户名>>>") 
# 输入  222' or 1=1 -- aaa  #aaa前面需要一个空格  222前面没有'
pwd  = input("请输入您的密码>>>")

conn = pymysql.connect(
host="127.0.0.1" , 
user="root" , 
password="123456",
database="db005")

cursor = conn.cursor()
sql1 = """
create table usr_pwd(
id int unsigned primary key auto_increment,
username varchar(255) not null,
password varchar(255) not null
)
"""
sql11 = "insert into usr_pwd values(1,'jack','123')"  #单双引号需要岔开

# res = cursor.execute(sql1)  #建表
# res = cursor.execute(sql11)  #插入一条数据  
#注意点:必须要在表里插入至少一条数据.否则无法模拟sql注入

sql2 = "select * from usr_pwd where username='%s' and password='%s' " % (user,pwd)  #这个写法会出现sql注入
print(sql2)
res = cursor.execute(sql2)
print(res) # 1查到成功 0没查到失败
res = cursor.fetchone()
print(res) #(1, 'jack', '123')
# """
# select * from usr_pwd where username='2222' or 4=4 -- aaa' and password='' 
# 相当于 : select * from usr_pwd where 10=10; 绕开了账户和密码的判断 -- 代表的是注释
# 后面的内容被注释了;
# """
if res:
	print("登录成功")
else:
	print("登录失败")

cursor.close()
conn.close()
# '''
# (2) 预处理机制  --应对sql注入
# """ 在执行sql语句之前,提前对sql语句中出现的字符进行过滤优化,避免sql注入攻击 """
# """ execute( sql , (参数1,参数2,参数3 .... ) ) execute2个参数默认开启预处理机制 """
# """ 填写 222' or 1=1 -- sdfsdfsdfsdf  尝试攻击  """


user = input("请输入您的用户名>>>")
pwd  = input("请输入您的密码>>>")

conn = pymysql.connect(
host="127.0.0.1" , 
user="root" , 
password="123456",
database="db005")

cursor = conn.cursor()
sql = "select * from usr_pwd where username=%s and password=%s"
# 单双引号需要岔开
res = cursor.execute(sql , (user,pwd)  )  #参数1是sql语句 参数2是元组
# 参数2是元组
print(res)


print(    "登录成功"  if res else "登录失败"    )

cursor.close()
conn.close()


# 请输入您的用户名>>>222' or 1=1 -- aaa
# 请输入您的密码>>>
# select * from usr_pwd where username='222' or 1=1 -- aaa' and password=''
# 1
# (1, 'jack', '123')
# 登录成功
# -------------------1
# 请输入您的用户名>>>222' or 1=1 -- aaa
# 请输入您的密码>>>
# 0
# 登录失败




















