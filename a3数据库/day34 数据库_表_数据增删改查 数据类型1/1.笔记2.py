# ### mysql关系型数据库
[快捷键]
快捷键:ctrl + l 清屏
快捷键:ctrl + c 终止
exit  : 退出数据库

[linux] 
service mysql stop
service mysql start
service mysql restart

[windows]
net stop mysql
net start mysql

sql语句要加;作为语句结尾

# ### part1
登录的完整语法
# (1) 登录
mysql -u用户 -p密码 -hip地址
mysal -uroot -p -h默认本地ip
localhost => 127.0.0.1 

# (2) 退出
exit 或者 \q

# ### part2
# 查询当前登录用户
select user();  

# 设置密码
set password = password('123456');

# 去除密码
set password = password('');


# ### part3
VMnet8: nat
VMnet1:host-only
ipconfig [windows] ifconfig  ip addr[linux]

# 给具体某个ip设置一个账户,连接linux
create user 'ceshi100'@'192.168.126.1' identified by '111';

# 给具体192.168.126.% 这个网段下的所有ip设置账户
create user 'ceshi101'@'192.168.126.%' identified by '222';

# 给所有ip下的主机设置账户
create user 'ceshi102'@'%' identified by '333';

USAGE 没有任何权限
# 查看具体某个ip下的用户权限
mysql> show grants for 'ceshi102'@'%';
+--------------------------------------+
| Grants for ceshi102@%                |
+--------------------------------------+
| GRANT USAGE ON *.* TO 'ceshi102'@'%' |
+--------------------------------------+

# 授权语法
grant 权限 on 数据库.表 to "用户名"@"ip地址" identified by "密码";
# select  查询数据的权限
# insert  添加数据的权限
# update  更改数据的权限
# delete  删除数据的权限
# *       所有

# 授予查询权限
grant select,insert on *.* to 'ceshi102'@'%' identified by '333';

# 授予所有权限
grant all on *.* to 'ceshi102'@'%' identified by '333';

# 移除删除权限(删除数据库/表)
revoke drop on *.* from 'ceshi102'@'%';

# 移除所有权限
revoke all on *.* from 'ceshi102'@'%';

# 刷新权限,立刻生效
flush privileges;

# ### part4 [必须熟练]
# mysql命令中,不区分大小写
# sudo find / -name db001
# sudo su root 切换到最高权限账户 cd mysql
# /var/lib/mysql/数据库...

# [windows]路径
# D:\MySQL5.7\mysql-5.7.25-winx64\data

# (1) 操作数据库 [文件夹]
增:
	# 创建数据库
	create database db001 charset utf8;

查:
	# 查看数据库
	show databases;
	
	# 查看建库语句;
	show create database db001;
	+----------+----------------------------------------------------------------+
	| Database | Create Database                                                |
	+----------+----------------------------------------------------------------+
	| db001    | CREATE DATABASE `db001` /*!40100 DEFAULT CHARACTER SET utf8 */ |
	+----------+----------------------------------------------------------------

改:
	alter database db001 charset gbk;

删:
	# 删除数据库
	drop database db002
	

# (2) 操作数据表 [文件]
增:
	# 选择数据库
	use db001
	
	# 创建表
	create table t1(id int,name char);

查:
	# 查看所有表
	show tables;
	
	# 查看建表语句
	show create table t1;
	       Table: t1
Create Table: CREATE TABLE `t1` (
  `id` int(11) DEFAULT NULL,
  `name` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=gbk

	# 查看表结构
	desc t1;
	+-------+---------+------+-----+---------+-------+
	| Field | Type    | Null | Key | Default | Extra |
	+-------+---------+------+-----+---------+-------+
	| id    | int(11) | YES  |     | NULL    |       |
	| name  | char(1) | YES  |     | NULL    |       |
	+-------+---------+------+-----+---------+-------+

改:
	# modify 只能改变类型
	alter table t1 modify name char(5);

	# change 改变类型+字段名
	alter table t1 change name name123 char(4);
	
	# add 添加字段
	alter table t1 add age int;

	# drop 删除字段
	alter table t1 drop age;

	# rename 更改表名
	alter table t1 rename t11;
	
删:
	drop table t11;


# (3) 操作记录 [文件的内容]
增:
	# 一次插入一条数据
	insert into t1(id,name) values(1,'abcd');

	# 一次插入多条数据
	insert into t1(id,name) values(2,'王文'),(3,'刘玉波');

	# 不指定具体字段,默认把所有字段全部插一遍
	insert into t1 values(6,'沈思雨');

	# 可以具体指定某个或者某几个字段进行插入
	insert into t1(name) values('张宇');

查:
	# * 所有
	select * from t1:
	
	# 查询单个字段
	select id from t1;
	
	# 查询多个字段
	select id,name from t1;
	
改:
	# update 表名 set 字段=值 where 条件
	update t1 set name = '汪伟' where id = 2;
	
	# 不加条件风险巨大,一改全改,一定加where  谨慎操作
	update t1 set name = '王伟';

删:
	# 删除的时候,必须加上where
	delete from t1 where id = 1;
	
	# 删除所有数据,一删全删,一定加where   风险巨大   谨慎操作
	delete from t1;

	# 删除所有 (数据+重置id)
	truncate table t1;

# 第二遍
# (1) 操作数据库 [文件夹]





























































