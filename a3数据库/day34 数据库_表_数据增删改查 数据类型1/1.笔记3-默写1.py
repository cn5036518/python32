# 一数据库
# 创建数据库
create database db004 charset utf8;

# 查看数据库
show databases;

# 查看建库语句;
show create database db004;

# 选择数据库
use db004;

# 删除数据库
drop database db005;

# 修改数据库
alter database db004 charset gbk;


# 二数据表
# 创建表
create table t1(id int,name varchar(255));

# 查看所有表
show tables;
desc t1  # 查看表结构

# 查看建表语句
show create table t1;
show create table t1\G

# 删除表
drop table t1;

# modify 只能改变类型  
alter table t1 modify id int(2);
	
# change 改变类型+字段名
alter table t1 change id id12 int(3);

# add 添加字段
alter table t1 add age int;

# drop 删除字段
alter table t1 drop age;

# rename 更改表名
alter table t1 rename t11;


# 三数据记录
# 一次插入一条数据
insert into(id,name) values(1,'jack');

# 一次插入多条数据
insert into t1(id,name) values(1,'jack'),(2,'tom'),(3,'bob');  #用的不多,一般是多行插入

# 不指定具体字段,默认把所有字段全部插一遍
insert into t1 values(4,'lily');

# 可以具体指定某个或者某几个字段进行插入,不指定的默认写默认值
insert into t1(name) values('lucy');
	
# * 查询所有
select * from t1;

# 查询单个字段
select name from t1;

# 查询多个字段
select id,name from t1;
	
# update 表名 set 字段=值 where 条件
update t1 set name = 'kevin' where id = 1;

# 不加条件风险大,一改全改,一定加where  谨慎操作
update t1 set name = 'kevin'

# 删除的时候,必须加上where
delete from t1 where id = 3;

# 删除所有数据,一删全删,一定加where  
delete from t1;  #不重置id


# 删除所有 (数据+重置id)
truncate table t1;

















































