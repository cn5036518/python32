# ### char varchar (补充)
char    字符长度   255个
varchar 字符长度 21845个

# ### part1  时间类型
date  YYYY-MM-DD 年月日 (节假日,纪念日)
time  HH:MM:SS   时分秒 (体育竞赛,记录时间)
year  YYYY       年份   (历史,酒的年份)
datetime  YYYY-MM-DD HH:MM:SS  年月日 时分秒 (上线时间,下单时间)
	create table t1(d date, t time , y year , dt datetime);
	insert into t1 values("2020-11-3","9:19:30","2020","2020-11-3 9:19:30");
	insert into t1 values(now(),now(),now(),now());

timestamp YYYYMMDDHHMMSS(时间戳)  自动更新时间 (不需要手动写入,自动实现更新记录,[用作记录修改的时间])
	create table t2(dt datetime , ts timestamp);
	insert into t2 values(20201103092530 , 20201103092530);
	insert into t2 values(null,null); # 区别 timestamp 自动更新时间(以当前时间戳) datetime没有
	insert into t2 values(20390102101010 , 20390102101010); error # 超越2038 

# ### part2 约束 : 对编辑的数据进行类型的限制,不满足约束条件的报错
	unsigned   :    无符号
	not null   :    不为空
	default    :    默认值
	unique     :    唯一值,加入唯一索引
	(索引相当于字典目录,索引的提出是为了加快速度,一味地乱加索引不会提高查询效率)
	primary key:    主键
	auto_increment: 自增加一
	zerofill   :    零填充
	foreign key:    外键

# unsigned 无符号
	create table t3(id int unsigned);   #0~255  tiny   int 0~42亿
	insert into t3 values(-1); error
	insert into t3 values(+1);  #可以
	insert into t3 values(4000000000); success
	# |          1 |
	# | 4200000000 |
	
	
# not null   :    不为空
	create table t4(id int not null , name varchar(11));
	insert into t4 values(1,"张宇");
	insert into t4 values(null,"张宇"); error
	insert into t4(name) values("李四"); error
	
	
# default    :    默认值
	create table t5(id int not null  , name varchar(11) default "沈思雨" );
	insert into t5 values(1,null);
	insert into t5(id) values(2);
	
	create table t5_2(id int not null  default "1111" , name varchar(11) default "沈思雨" );
	insert into t5_2 values(); # 在values里面不写值,默认使用默认值;

# unique     :    唯一值,加入唯一索引(索引的提出是为了加快速度,一味地乱加索引不会提高查询效率)
	# 唯一 可为null  标记成: UNI
	create table t6(id int unique , name char(10) default "赵万里" );
	insert into t6(id) values(1);
	insert into t6(id) values(1); error
	insert into t6(id) values(null);
	insert into t6(id) values(null); # id变成了多个null

# primary key:    主键 [ 唯一 + 不为null ]   PRI 标记数据的唯一特征
	# """一个表中,只能设置一个字段为一个主键,unique唯一约束可以设置多个"""
	# 创建主键
	create table t7(id int primary key , name varchar(10) default "赵沈阳");
	insert into t7(id) values(1);
	insert into t7(id) values(1); error 
	insert into t7(id) values(null); error
	
	# unique + not null => PRI
	create table t8(id int unique not null ,  name varchar(10) default "赵沈阳" );
	
	# primary key  / unique + not null  => 优先把primary key 作为主键;
	create table t9(id1 int unique not null ,  id2 int primary key );
	
	# 一个表只能设置单个字段为一个主键;
	create table t10(id1 int  primary key  ,  id2 int primary key ); error
	
# auto_increment: 自增加一 (一般配合 主键或者unique 使用)
	create table t11(id int primary key auto_increment , name varchar(255) default "敬文栋");
	insert into t11 values(1,"张三");
	insert into t11 values(null,"李四");
	insert into t11(id) values(null);
	# 使用默认值或者自增插入数据
	insert into t11 values();
	# 删除数据
	delete from t11;
	# 删除数据 + 重置id
	truncate table t11;


# zerofill   :    零填充 (配合int使用,不够5位拿0来填充)
	create table t12(id int(5) zerofill);
	insert into t12 values(1234567);
	insert into t12 values(12);



























