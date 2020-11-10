# [mysql周末作业]
### 1.表结构:
![表结构](assets/表结构.png)
### 2.黏贴如下sql,直接建表
```
# 1、创建表
# 创建班级表
create table class(
cid int primary key auto_increment,
caption varchar(32) not null
);

# 创建学生表
create table student(
sid int primary key auto_increment,
gender char(1) not null,
class_id int not null,
sname varchar(32) not null,
foreign key(class_id) references class(cid) on delete cascade on update cascade
);

# 创建老师表
create table teacher(
tid int primary key auto_increment,
tname varchar(32) not null
);

# 创建课程表
create table course(
cid int primary key auto_increment,
cname varchar(32) not null,
teacher_id int not null,
foreign key(teacher_id) references teacher(tid) on delete cascade on update cascade
);

# 创建成绩表
create table score(
sid int primary key auto_increment,
student_id int not null,
course_id int not null,
num int not null,
foreign key(student_id) references student(sid) on delete cascade on update cascade,
foreign key(course_id) references course(cid) on delete cascade on update cascade
);


# 2、插入记录
# 班级表插入记录
insert into class values
('1', '三年二班'), 
('2', '三年三班'), 
('3', '一年二班'), 
('4', '二年一班');

# 学生表插入记录
insert into student values
('1', '男', '1', '理解'), 
('2', '女', '1', '钢蛋'), 
('3', '男', '1', '张三'), 
('4', '男', '1', '张一'), 
('5', '女', '1', '张二'), 
('6', '男', '1', '张四'), 
('7', '女', '2', '铁锤'),
('8', '男', '2', '李三'), 
('9', '男', '2', '李一'), 
('10', '女', '2', '李二'), 
('11', '男', '2', '李四'), 
('12', '女', '3', '如花'), 
('13', '男', '3', '刘三'), 
('14', '男', '3', '刘一'), 
('15', '女', '3', '刘二'), 
('16', '男', '3', '刘四');

# 老师表插入记录
insert into teacher values
('1', '张磊'), 
('2', '李平'), 
('3', '刘海燕'), 
('4', '朱云海'), 
('5', '李春秋');

# 课程表插入记录
insert into course values
('1', '生物', '1'), 
('2', '物理', '2'), 
('3', '体育', '3'), 
('4', '美术', '2');

# 成绩表插入记录
insert into score values
('1', '1', '1', '10'), 
('2', '1', '2', '9'), 
('3', '1', '3', '76'),
('5', '1', '4', '66'), 
('6', '2', '1', '8'), 
('8', '2', '3', '68'), 
('9', '2', '4', '99'), 
('10', '3', '1', '77'), 
('11', '3', '2', '66'), 
('12', '3', '3', '87'), 
('13', '3', '4', '99'), 
('14', '4', '1', '79'), 
('15', '4', '2', '11'), 
('16', '4', '3', '67'), 
('17', '4', '4', '100'), 
('18', '5', '1', '79'), 
('19', '5', '2', '11'), 
('20', '5', '3', '67'), 
('21', '5', '4', '100'), 
('22', '6', '1', '9'), 
('23', '6', '2', '100'), 
('24', '6', '3', '67'), 
('25', '6', '4', '100'), 
('26', '7', '1', '9'), 
('27', '7', '2', '100'), 
('28', '7', '3', '67'), 
('29', '7', '4', '88'), 
('30', '8', '1', '9'), 
('31', '8', '2', '100'), 
('32', '8', '3', '67'),
('33', '8', '4', '88'), 
('34', '9', '1', '91'), 
('35', '9', '2', '88'), 
('36', '9', '3', '67'), 
('37', '9', '4', '22'), 
('38', '10', '1', '90'), 
('39', '10', '2', '77'), 
('40', '10', '3', '43'), 
('41', '10', '4', '87'), 
('42', '11', '1', '90'), 
('43', '11', '2', '77'), 
('44', '11', '3', '43'), 
('45', '11', '4', '87'), 
('46', '12', '1', '90'), 
('47', '12', '2', '77'), 
('48', '12', '3', '43'), 
('49', '12', '4', '87'), 
('52', '13', '3', '87');
```
### 3.练习题目

```
1、查询所有的课程的名称以及对应的任课老师姓名
select 
	*
from course as c,teacher as t
where  c.teacher_id = t.tid;

| cid | cname  | teacher_id | tid | tname     |
+-----+--------+------------+-----+-----------+
|   1 | 生物   |          1 |   1 | 张磊      |
|   2 | 物理   |          2 |   2 | 李平      |
|   3 | 体育   |          3 |   3 | 刘海燕    |
|   4 | 美术   |          2 |   2 | 李平 

select 
	cname,tname
from course as c,teacher as t
where  c.teacher_id = t.tid;

| cname  | tname     |
+--------+-----------+
| 生物   | 张磊      |
| 物理   | 李平      |
| 体育   | 刘海燕    |
| 美术   | 李平  

2、查询学生表中男女生各有多少人
select * from student;

select gender,count(*) from student group by gender;
# | gender | count(*) |
# +--------+----------+
# | 女     |        6 |
# | 男     |       10 

3、查询物理成绩等于100的学生的姓名
select
	t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num = 100
	and t2.cname = '物理';

| sname  | cname  | num |
+--------+--------+-----+
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |


4、查询平均成绩大于八十分的同学的姓名和平均成绩
# 1 查询每个同学的平均成绩
select
	t1.sid,t1.sname,avg(num) as avg_num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
group by t1.sid,t1.sname  #01先连3个表形成一个大表,02然后分组计算每个同学的平均成绩 group by+avg()
having avg_num >80;  #03 分组后二次过滤having

| sid | sname  | avg_num |
+-----+--------+---------+
|   1 | 理解   | 40.2500 |
|   2 | 钢蛋   | 58.3333 |
|   3 | 张三   | 82.2500 |
|   4 | 张一   | 64.2500 |
|   5 | 张二   | 64.2500 |
|   6 | 张四   | 69.0000 |
|   7 | 铁锤   | 66.0000 |
|   8 | 李三   | 66.0000 |
|   9 | 李一   | 67.0000 |
|  10 | 李二   | 74.2500 |
|  11 | 李四   | 74.2500 |
|  12 | 如花   | 74.2500 |
|  13 | 刘三   | 87.0000 |

| sname  | avg_num |
+--------+---------+
| 张三   | 82.2500 |
| 刘三   | 87.0000 

# select
	# t1.sid,t1.sname,avg(num) as avg_num
# from 
	# student as t1,course as t2,score as t3
# where 
	# t3.student_id = t1.sid and t3.course_id = t2.cid
# group by t1.sid,t1.sname;

# | sid | sname  | avg_num |
# +-----+--------+---------+
# |   1 | 理解   | 40.2500 |
# |   2 | 钢蛋   | 58.3333 |
# |   3 | 张三   | 82.2500 |
# |   4 | 张一   | 64.2500 |
# |   5 | 张二   | 64.2500 |
# |   6 | 张四   | 69.0000 |
# |   7 | 铁锤   | 66.0000 |
# |   8 | 李三   | 66.0000 |
# |   9 | 李一   | 67.0000 |
# |  10 | 李二   | 74.2500 |
# |  11 | 李四   | 74.2500 |
# |  12 | 如花   | 74.2500 |
# |  13 | 刘三   | 87.0000 |


# select avg_num from t11 wherer avg_num > 80;


# select t1.sname,t1.avg_num from (select
	# t1.sid,t1.sname,avg(num) as avg_num
# from 
	# student as t1,course as t2,score as t3
# where 
	# t3.student_id = t1.sid and t3.course_id = t2.cid
# group by t1.sid,t1.sname) as t11 where t1.avg_num > 80;
# | sname  | avg_num |
# +--------+---------+
# | 张三   | 82.2500 |
# | 刘三   | 87.0000 

# select avg_num from (select
	# t1.sid,t1.sname,avg(num) as avg_num
# from 
	# student as t1,course as t2,score as t3
# where 
	# t3.student_id = t1.sid and t3.course_id = t2.cid
# group by t1.sid,t1.sname)  where avg_num > 80;
# Every derived table must have its own alias


5、查询所有学生的学号，姓名，选课数，总成绩

select
	t1.sid,t1.sname,count(t2.cid),sum(t3.num)
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
group by 
	t1.sid,t1.sname;
	
| sid | sname  | count(t2.cid) | sum(t3.num) |
+-----+--------+---------------+-------------+
|   1 | 理解   |             4 |         161 |
|   2 | 钢蛋   |             3 |         175 |
|   3 | 张三   |             4 |         329 |
|   4 | 张一   |             4 |         257 |
|   5 | 张二   |             4 |         257 |
|   6 | 张四   |             4 |         276 |
|   7 | 铁锤   |             4 |         264 |
|   8 | 李三   |             4 |         264 |
|   9 | 李一   |             4 |         268 |
|  10 | 李二   |             4 |         297 |
|  11 | 李四   |             4 |         297 |
|  12 | 如花   |             4 |         297 |
|  13 | 刘三   |             1 |          87

6、 查询姓李老师的个数
select count(*) from teacher where tname like '李%';

# | count(*) |
# +----------+
# |        2 |

7、 查询没有报李平老师课的学生姓名
# 方法2 not in  推荐  比方法1的左连接更简洁
# 1 连4个表
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;
	
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;

# 1 所有报课学生的sid
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
# # 2 所有报李平老师课学生的sid
| sid |
+-----+
|   1 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|   2 |

select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t1.sid not in (1,2,3,...12);


#综合拼接
select
	# distinct(t1.sid)
	distinct(t1.sid),t1.sname
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t1.sid not in (select
						distinct(t1.sid)
					from 
						student as t1,course as t2,score as t3,teacher as t4
					where 
						t3.student_id = t1.sid 
						and t3.course_id = t2.cid
						and t2.teacher_id = t4.tid
						and t4.tname = '李平');						
# +-----+--------+
# | sid | sname  |
# +-----+--------+
# |  13 | 刘三   |

select 
	*
from 
	student as t1 left join t2 on t1.sid = t2.sid;

select 
	t1.sid,t1.sname,t2.num
from 
	student as t1 left join (select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid) as t2 on t1.sid = t2.sid;

# 4没报课的学生(一门课都没报),  --刘一 刘二 刘四
# 这个前3步是内连接,看不出来,第4步,用student当主表 左连接成绩表score才能看到

# 01 连接2个表成一个大表
select	* from 	student as t1 left join score as t2	 on t1.sid = t2.student_id;
# where t2.num is null;

| sid | gender | class_id | sname  | sid  | student_id | course_id | num  |
+-----+--------+----------+--------+------+------------+-----------+------+
|   1 | 男     |        1 | 理解   |    1 |          1 |         1 |   10 |
|   1 | 男     |        1 | 理解   |    2 |          1 |         2 |    9 |
|   1 | 男     |        1 | 理解   |    3 |          1 |         3 |   76 |
|   1 | 男     |        1 | 理解   |    5 |          1 |         4 |   66 |
|   2 | 女     |        1 | 钢蛋   |    6 |          2 |         1 |    8 |
....
|  12 | 女     |        3 | 如花   |   46 |         12 |         1 |   90 |
|  12 | 女     |        3 | 如花   |   47 |         12 |         2 |   77 |
|  12 | 女     |        3 | 如花   |   48 |         12 |         3 |   43 |
|  12 | 女     |        3 | 如花   |   49 |         12 |         4 |   87 |
|  13 | 男     |        3 | 刘三   |   52 |         13 |         3 |   87 |
|  14 | 男     |        3 | 刘一   | NULL |       NULL |      NULL | NULL |
|  15 | 女     |        3 | 刘二   | NULL |       NULL |      NULL | NULL |
|  16 | 男     |        3 | 刘四   | NULL |       NULL |      NULL | NULL |

# 02 对大表进行单表条件查询 (写在where后)  全部字段
select	* from 	student as t1 left join score as t2	 on t1.sid = t2.student_id
where t2.num is null;

| sid | gender | class_id | sname  | sid  | student_id | course_id | num  |
+-----+--------+----------+--------+------+------------+-----------+------+
|  14 | 男     |        3 | 刘一   | NULL |       NULL |      NULL | NULL |
|  15 | 女     |        3 | 刘二   | NULL |       NULL |      NULL | NULL |
|  16 | 男     |        3 | 刘四   | NULL |       NULL |      NULL | NULL

#03 选取字段
select	 t1.sid,t1.sname from 	student as t1 left join score as t2	 on t1.sid = t2.student_id
where t2.num is null;
| sid | sname  |
+-----+--------+
|  14 | 刘一   |
|  15 | 刘二   |
|  16 | 刘四  


# 方法1  左连接
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;
	
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;

# 1 所有报课学生的sid
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
# # 2 所有报李平老师课学生的sid
| sid |
+-----+
|   1 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|   2 |

select 
	*
from 
		(select
		distinct(t1.sid),t1.sname
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid) as t1 left join (select
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname = '李平') as t2 on t1.sid = t2.sid;

# 3报课的学生中,没有报李平老师可的同学  --刘三
| sid | sname  | sid  |
+-----+--------+------+
|   1 | 理解   |    1 |
|   2 | 钢蛋   |    2 |
|   3 | 张三   |    3 |
|   4 | 张一   |    4 |
|   5 | 张二   |    5 |
|   6 | 张四   |    6 |
|   7 | 铁锤   |    7 |
|   8 | 李三   |    8 |
|   9 | 李一   |    9 |
|  10 | 李二   |   10 |
|  11 | 李四   |   11 |
|  12 | 如花   |   12 |
|  13 | 刘三   | NULL |   

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	
select 
	*
from 
	student as t1 left join t2 on t1.sid = t2.sid;

select 
	t1.sid,t1.sname,t2.num
from 
	student as t1 left join (select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid) as t2 on t1.sid = t2.sid;

# 4没报课的学生(一门课都没报),  --刘一 刘二 刘四
# 这个前3步是内连接,看不出来,第4步,用student当主表 左连接才能看到
| sid | sname  | num  |
+-----+--------+------+
|   1 | 理解   |   10 |
|   1 | 理解   |    9 |
|   1 | 理解   |   76 |
|   1 | 理解   |   66 |
|   2 | 钢蛋   |    8 |
|   2 | 钢蛋   |   68 |
|   2 | 钢蛋   |   99 |
|   3 | 张三   |   77 |
|   3 | 张三   |   66 |
|   3 | 张三   |   87 |
|   3 | 张三   |   99 |
|   4 | 张一   |   79 |
|   4 | 张一   |   11 |
|   4 | 张一   |   67 |
|   4 | 张一   |  100 |
|   5 | 张二   |   79 |
|   5 | 张二   |   11 |
|   5 | 张二   |   67 |
|   5 | 张二   |  100 |
|   6 | 张四   |    9 |
|   6 | 张四   |  100 |
|   6 | 张四   |   67 |
|   6 | 张四   |  100 |
|   7 | 铁锤   |    9 |
|   7 | 铁锤   |  100 |
|   7 | 铁锤   |   67 |
|   7 | 铁锤   |   88 |
|   8 | 李三   |    9 |
|   8 | 李三   |  100 |
|   8 | 李三   |   67 |
|   8 | 李三   |   88 |
|   9 | 李一   |   91 |
|   9 | 李一   |   88 |
|   9 | 李一   |   67 |
|   9 | 李一   |   22 |
|  10 | 李二   |   90 |
|  10 | 李二   |   77 |
|  10 | 李二   |   43 |
|  10 | 李二   |   87 |
|  11 | 李四   |   90 |
|  11 | 李四   |   77 |
|  11 | 李四   |   43 |
|  11 | 李四   |   87 |
|  12 | 如花   |   90 |
|  12 | 如花   |   77 |
|  12 | 如花   |   43 |
|  12 | 如花   |   87 |
|  13 | 刘三   |   87 |
|  14 | 刘一   | NULL |
|  15 | 刘二   | NULL |
|  16 | 刘四   | NULL |
	

8、 查询物理课程的分数比生物课程的分数高的学生的学号
select
	t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 生物   |  10 |
| 钢蛋   | 生物   |   8 |
| 张三   | 生物   |  77 |
| 张一   | 生物   |  79 |
| 张二   | 生物   |  79 |
| 张四   | 生物   |   9 |
| 铁锤   | 生物   |   9 |
| 李三   | 生物   |   9 |
| 李一   | 生物   |  91 |
| 李二   | 生物   |  90 |
| 李四   | 生物   |  90 |
| 如花   | 生物   |  90 |
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |


select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理';
	
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |
|   3 | 张三   | 物理   |  66 |
|   4 | 张一   | 物理   |  11 |
|   5 | 张二   | 物理   |  11 |
|   6 | 张四   | 物理   | 100 |
|   7 | 铁锤   | 物理   | 100 |
|   8 | 李三   | 物理   | 100 |
|   9 | 李一   | 物理   |  88 |
|  10 | 李二   | 物理   |  77 |
|  11 | 李四   | 物理   |  77 |
|  12 | 如花   | 物理   |  77 |

	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物';
	
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |
|   2 | 钢蛋   | 生物   |   8 |
|   3 | 张三   | 生物   |  77 |
|   4 | 张一   | 生物   |  79 |
|   5 | 张二   | 生物   |  79 |
|   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 生物   |  91 |
|  10 | 李二   | 生物   |  90 |
|  11 | 李四   | 生物   |  90 |
|  12 | 如花   | 生物   |  90 |

select 
	*
from 
	(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理')as t1,(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物') as t2
where t1.sid = t2.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |   1 | 理解   | 生物   |  10 |
|   3 | 张三   | 物理   |  66 |   3 | 张三   | 生物   |  77 |
|   4 | 张一   | 物理   |  11 |   4 | 张一   | 生物   |  79 |
|   5 | 张二   | 物理   |  11 |   5 | 张二   | 生物   |  79 |
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 物理   |  88 |   9 | 李一   | 生物   |  91 |
|  10 | 李二   | 物理   |  77 |  10 | 李二   | 生物   |  90 |
|  11 | 李四   | 物理   |  77 |  11 | 李四   | 生物   |  90 |
|  12 | 如花   | 物理   |  77 |  12 | 如花   | 生物   |  90 |


select 
	*
from 
	(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理')as t1,(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物') as t2
where t1.sid = t2.sid and t1.num > t2.num;
| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 生物   |   9 |

# 查询物理课程的分数比生物课程的分数高的学生的学号

9、 查询没有同时选修物理课程和体育课程的学生姓名
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 生物   |  10 |
| 钢蛋   | 生物   |   8 |
| 张三   | 生物   |  77 |
| 张一   | 生物   |  79 |
| 张二   | 生物   |  79 |
| 张四   | 生物   |   9 |
| 铁锤   | 生物   |   9 |
| 李三   | 生物   |   9 |
| 李一   | 生物   |  91 |
| 李二   | 生物   |  90 |
| 李四   | 生物   |  90 |
| 如花   | 生物   |  90 |
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理';
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '体育';
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 体育   |  76 |
| 钢蛋   | 体育   |  68 |
| 张三   | 体育   |  87 |
| 张一   | 体育   |  67 |
| 张二   | 体育   |  67 |
| 张四   | 体育   |  67 |
| 铁锤   | 体育   |  67 |
| 李三   | 体育   |  67 |
| 李一   | 体育   |  67 |
| 李二   | 体育   |  43 |
| 李四   | 体育   |  43 |
| 如花   | 体育   |  43 |
| 刘三   | 体育   |  87 |

# 查询没有同时选修物理课程和体育课程的学生姓名

#001同时选修物理课程和体育课程的学生姓名
select 
	*
from 
		(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname = '物理') as t1,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname = '体育') as t2
where t1.sid = t2.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |   1 | 理解   | 体育   |  76 |
|   3 | 张三   | 物理   |  66 |   3 | 张三   | 体育   |  87 |
|   4 | 张一   | 物理   |  11 |   4 | 张一   | 体育   |  67 |
|   5 | 张二   | 物理   |  11 |   5 | 张二   | 体育   |  67 |
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 体育   |  67 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 体育   |  67 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 体育   |  67 |
|   9 | 李一   | 物理   |  88 |   9 | 李一   | 体育   |  67 |
|  10 | 李二   | 物理   |  77 |  10 | 李二   | 体育   |  43 |
|  11 | 李四   | 物理   |  77 |  11 | 李四   | 体育   |  43 |
|  12 | 如花   | 物理   |  77 |  12 | 如花   | 体育   |  43 

#报了物理课的同学,减去物理和体育2个课都报了的同学
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理' and t1.sid not in (select 
		t1.sid
	from 
			(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '物理') as t1,(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '体育') as t2
	where t1.sid = t2.sid);

#报了体育课的同学,减去物理和体育2个课都报了的同学	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '体育' and t1.sid not in (select 
		t1.sid
	from 
			(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '物理') as t1,(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '体育') as t2
	where t1.sid = t2.sid);
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   2 | 钢蛋   | 体育   |  68 |
|  13 | 刘三   | 体育   |  87


10、查询挂科超过两门(包括两门)的学生姓名和班级
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num<60;
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |
|   1 | 理解   | 物理   |   9 |
|   2 | 钢蛋   | 生物   |   8 |
|   4 | 张一   | 物理   |  11 |
|   5 | 张二   | 物理   |  11 |
|   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 美术   |  22 |
|  10 | 李二   | 体育   |  43 |
|  11 | 李四   | 体育   |  43 |
|  12 | 如花   | 体育   |  43 |

select t1.sid,t1.sname,count(*) from (select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num<60) as t1 group by t1.sid,t1.sname;
	
| sid | sname  | count(*) |
+-----+--------+----------+
|   1 | 理解   |        2 |
|   2 | 钢蛋   |        1 |
|   4 | 张一   |        1 |
|   5 | 张二   |        1 |
|   6 | 张四   |        1 |
|   7 | 铁锤   |        1 |
|   8 | 李三   |        1 |
|   9 | 李一   |        1 |
|  10 | 李二   |        1 |
|  11 | 李四   |        1 |
|  12 | 如花   |        1 

select
t1.sname,t2.caption
from
student as t1,class as t2
where t1.class_id = t2.cid;

| sid | gender | class_id | sname  | cid | caption      |
+-----+--------+----------+--------+-----+--------------+
|   1 | 男     |        1 | 理解   |   1 | 三年二班     |
|   2 | 女     |        1 | 钢蛋   |   1 | 三年二班     |
|   3 | 男     |        1 | 张三   |   1 | 三年二班     |
|   4 | 男     |        1 | 张一   |   1 | 三年二班     |
|   5 | 女     |        1 | 张二   |   1 | 三年二班     |
|   6 | 男     |        1 | 张四   |   1 | 三年二班     |
|   7 | 女     |        2 | 铁锤   |   2 | 三年三班     |
|   8 | 男     |        2 | 李三   |   2 | 三年三班     |
|   9 | 男     |        2 | 李一   |   2 | 三年三班     |
|  10 | 女     |        2 | 李二   |   2 | 三年三班     |
|  11 | 男     |        2 | 李四   |   2 | 三年三班     |
|  12 | 女     |        3 | 如花   |   3 | 一年二班     |
|  13 | 男     |        3 | 刘三   |   3 | 一年二班     |
|  14 | 男     |        3 | 刘一   |   3 | 一年二班     |
|  15 | 女     |        3 | 刘二   |   3 | 一年二班     |
|  16 | 男     |        3 | 刘四   |   3 | 一年二班  

select
t1.sname,t2.caption
from
student as t1,class as t2
where t1.class_id = t2.cid and t1.sname = '理解';

| sname  | caption      |
+--------+--------------+
| 理解   | 三年二班


11、查询选修了所有课程的学生姓名
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='生物';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='物理';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='体育';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='美术';
	
select 
	*
from (select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='生物') as t1,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='物理') as t2,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='体育') as t3,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='美术') as t4
where t1.sid = t2.sid and t2.sid = t3.sid and t3.sid = t4.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num | sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |   1 | 理解   | 物理   |   9 |   1 | 理解   | 体育   |  76 |   1 | 理解   | 美术   |  66 |
|   3 | 张三   | 生物   |  77 |   3 | 张三   | 物理   |  66 |   3 | 张三   | 体育   |  87 |   3 | 张三   | 美术   |  99 |
|   4 | 张一   | 生物   |  79 |   4 | 张一   | 物理   |  11 |   4 | 张一   | 体育   |  67 |   4 | 张一   | 美术   | 100 |
|   5 | 张二   | 生物   |  79 |   5 | 张二   | 物理   |  11 |   5 | 张二   | 体育   |  67 |   5 | 张二   | 美术   | 100 |
|   6 | 张四   | 生物   |   9 |   6 | 张四   | 物理   | 100 |   6 | 张四   | 体育   |  67 |   6 | 张四   | 美术   | 100 |
|   7 | 铁锤   | 生物   |   9 |   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 体育   |  67 |   7 | 铁锤   | 美术   |  88 |
|   8 | 李三   | 生物   |   9 |   8 | 李三   | 物理   | 100 |   8 | 李三   | 体育   |  67 |   8 | 李三   | 美术   |  88 |
|   9 | 李一   | 生物   |  91 |   9 | 李一   | 物理   |  88 |   9 | 李一   | 体育   |  67 |   9 | 李一   | 美术   |  22 |
|  10 | 李二   | 生物   |  90 |  10 | 李二   | 物理   |  77 |  10 | 李二   | 体育   |  43 |  10 | 李二   | 美术   |  87 |
|  11 | 李四   | 生物   |  90 |  11 | 李四   | 物理   |  77 |  11 | 李四   | 体育   |  43 |  11 | 李四   | 美术   |  87 |
|  12 | 如花   | 生物   |  90 |  12 | 如花   | 物理   |  77 |  12 | 如花   | 体育   |  43 |  12 | 如花   | 美术   |  87


12、查询李平老师教的课程的所有成绩记录
select
	*
from 
	course as t2,score as t3,teacher as t4
where 
	t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+
|   2 | 物理   |          2 |   2 |          1 |         2 |   9 |   2 | 李平   |
|   2 | 物理   |          2 |  11 |          3 |         2 |  66 |   2 | 李平   |
|   2 | 物理   |          2 |  15 |          4 |         2 |  11 |   2 | 李平   |
|   2 | 物理   |          2 |  19 |          5 |         2 |  11 |   2 | 李平   |
|   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  35 |          9 |         2 |  88 |   2 | 李平   |
|   2 | 物理   |          2 |  39 |         10 |         2 |  77 |   2 | 李平   |
|   2 | 物理   |          2 |  43 |         11 |         2 |  77 |   2 | 李平   |
|   2 | 物理   |          2 |  47 |         12 |         2 |  77 |   2 | 李平   |
|   4 | 美术   |          2 |   5 |          1 |         4 |  66 |   2 | 李平   |
|   4 | 美术   |          2 |   9 |          2 |         4 |  99 |   2 | 李平   |
|   4 | 美术   |          2 |  13 |          3 |         4 |  99 |   2 | 李平   |
|   4 | 美术   |          2 |  17 |          4 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  21 |          5 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  25 |          6 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  29 |          7 |         4 |  88 |   2 | 李平   |
|   4 | 美术   |          2 |  33 |          8 |         4 |  88 |   2 | 李平   |
|   4 | 美术   |          2 |  37 |          9 |         4 |  22 |   2 | 李平   |
|   4 | 美术   |          2 |  41 |         10 |         4 |  87 |   2 | 李平   |
|   4 | 美术   |          2 |  45 |         11 |         4 |  87 |   2 | 李平   |
|   4 | 美术   |          2 |  49 |         12 |         4 |  87 |   2 | 李平 


select
	t2.cname,t3.num,t4.tname
from 
	course as t2,score as t3,teacher as t4
where 
	t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
| cname  | num | tname  |
+--------+-----+--------+
| 物理   |   9 | 李平   |
| 物理   |  66 | 李平   |
| 物理   |  11 | 李平   |
| 物理   |  11 | 李平   |
| 物理   | 100 | 李平   |
| 物理   | 100 | 李平   |
| 物理   | 100 | 李平   |
| 物理   |  88 | 李平   |
| 物理   |  77 | 李平   |
| 物理   |  77 | 李平   |
| 物理   |  77 | 李平   |
| 美术   |  66 | 李平   |
| 美术   |  99 | 李平   |
| 美术   |  99 | 李平   |
| 美术   | 100 | 李平   |
| 美术   | 100 | 李平   |
| 美术   | 100 | 李平   |
| 美术   |  88 | 李平   |
| 美术   |  88 | 李平   |
| 美术   |  22 | 李平   |
| 美术   |  87 | 李平   |
| 美术   |  87 | 李平   |
| 美术   |  87 | 李平 

13、查询全部学生都选修了的课程号和课程名
select
	*
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	
select distinct(t11.sid) from (select
		t1.sid
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid) as t11;
		
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '物理';
| sid | cname  |
+-----+--------+
|   1 | 物理   |
|   3 | 物理   |
|   4 | 物理   |
|   5 | 物理   |
|   6 | 物理   |
|   7 | 物理   |
|   8 | 物理   |
|   9 | 物理   |
|  10 | 物理   |
|  11 | 物理   |
|  12 | 物理  

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '生物';
| sid | cname  |
+-----+--------+
|   1 | 生物   |
|   2 | 生物   |
|   3 | 生物   |
|   4 | 生物   |
|   5 | 生物   |
|   6 | 生物   |
|   7 | 生物   |
|   8 | 生物   |
|   9 | 生物   |
|  10 | 生物   |
|  11 | 生物   |
|  12 | 生物 

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术';
| sid | cname  |
+-----+--------+
|   1 | 美术   |
|   2 | 美术   |
|   3 | 美术   |
|   4 | 美术   |
|   5 | 美术   |
|   6 | 美术   |
|   7 | 美术   |
|   8 | 美术   |
|   9 | 美术   |
|  10 | 美术   |
|  11 | 美术 
|  12 | 美术 	

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '体育';
		
| sid | cname  |
+-----+--------+
|   1 | 体育   |
|   2 | 体育   |
|   3 | 体育   |
|   4 | 体育   |
|   5 | 体育   |
|   6 | 体育   |
|   7 | 体育   |
|   8 | 体育   |
|   9 | 体育   |
|  10 | 体育   |
|  11 | 体育   |
|  12 | 体育   |
|  13 | 体育 

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术';	
		
select
	*
from
	(select distinct(t11.sid) from (select
		t1.sid
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid) as t11) as t11 left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术') as t22 on t11.sid = t22.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '体育') as t33 on t11.sid = t33.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '物理') as t44 on t11.sid = t44.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '生物') as t55 on t11.sid = t55.sid

| sid | sid  | cname  | sid  | cname  | sid  | cname  | sid  | cname  |
+-----+------+--------+------+--------+------+--------+------+--------+
|   1 |    1 | 美术   |    1 | 体育   |    1 | 物理   |    1 | 生物   |
|   2 |    2 | 美术   |    2 | 体育   | NULL | NULL   |    2 | 生物   |
|   3 |    3 | 美术   |    3 | 体育   |    3 | 物理   |    3 | 生物   |
|   4 |    4 | 美术   |    4 | 体育   |    4 | 物理   |    4 | 生物   |
|   5 |    5 | 美术   |    5 | 体育   |    5 | 物理   |    5 | 生物   |
|   6 |    6 | 美术   |    6 | 体育   |    6 | 物理   |    6 | 生物   |
|   7 |    7 | 美术   |    7 | 体育   |    7 | 物理   |    7 | 生物   |
|   8 |    8 | 美术   |    8 | 体育   |    8 | 物理   |    8 | 生物   |
|   9 |    9 | 美术   |    9 | 体育   |    9 | 物理   |    9 | 生物   |
|  10 |   10 | 美术   |   10 | 体育   |   10 | 物理   |   10 | 生物   |
|  11 |   11 | 美术   |   11 | 体育   |   11 | 物理   |   11 | 生物   |
|  12 |   12 | 美术   |   12 | 体育   |   12 | 物理   |   12 | 生物   |
|  13 | NULL | NULL   |   13 | 体育   | NULL | NULL   | NULL | NULL  

14、查询每门课程被选修的次数
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |


select count(*) from t4 group by course_id;

select course_id,cname,count(*) from (select 
	 course_id,cname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid) as t4   #必须加别名
group by course_id;

| course_id | cname  | count(*) |
+-----------+--------+----------+
|         1 | 生物   |       12 |
|         2 | 物理   |       11 |
|         3 | 体育   |       13 |
|         4 | 美术   |       12


15、查询只选修了一门课程的学生学号和姓名
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |


select 
	t3.sid,t3.sname,group_concat(t1.cname),count(*)    #必须加 group_concat(t1.cname)
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
group by t3.sid
having count(*) = 1;

sid | sname  | group_concat(t1.cname) | count(*) |
+-----+--------+------------------------+----------+
|  13 | 刘三   | 体育                   |        1


16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |



select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid 
order by t2.num desc;

select 
	distinct(t2.num) ,t3.sname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid 
order by t2.num desc;

| num | sname  |
+-----+--------+
| 100 | 李三   |
| 100 | 张四   |
| 100 | 张一   |
| 100 | 铁锤   |
| 100 | 张二   |
|  99 | 钢蛋   |
|  99 | 张三   |
|  91 | 李一   |
|  90 | 如花   |
|  90 | 李二   |
|  90 | 李四  


17、查询平均成绩大于85的学生姓名和平均成绩
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |


select 
	t3.sid,t3.sname,avg(t2.num) as avg_num
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
group by t3.sid
having avg_num > 85;

| sid | sname  | avg_num |
+-----+--------+---------+
|  13 | 刘三   | 87.0000


18、查询生物成绩不及格的学生姓名和对应生物分数
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |


select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname = '生物'
	and t2.num < 60;
	
select 
	t3.sname,t1.cname,t2.num
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname = '生物'
	and t2.num < 60;    #这里不要分组

 sname  | cname  | num |
+--------+--------+-----+
| 理解   | 生物   |  10 |
| 钢蛋   | 生物   |   8 |
| 张四   | 生物   |   9 |
| 铁锤   | 生物   |   9 |
| 李三   | 生物   |   9 


19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	# and t4.tname = '李平';
	
select
	t1.sid,t1.sname,avg(num)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平'
group by t1.sid;

select
	t1.sid,t1.sname,avg(num) as avg_num
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平'
group by t1.sid
order by avg_num desc;

select
	t1.sid,t1.sname,avg(num) as avg_num
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平'
group by t1.sid
order by avg_num desc
limit 1;

# | sid | sname  | avg_num  |
# +-----+--------+----------+
# |   6 | 张四   | 100.0000


20、查询每门课程成绩最好的课程id、学生姓名和分数
0 步骤0
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |

# 查询每门课程成绩最好的课程id--1、学生姓名和分数

# 1查询每门课的最高分
select 
	# t2.course_id,max(t2.num),group_concat(t3.sname)
	t2.course_id,max(t2.num) as max_num
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
group by t2.course_id;

| course_id | max_num |
+-----------+---------+
|         1 |      91 |
|         2 |     100 |
|         3 |      87 |
|         4 |     100 |

# 2 将步骤1的最高分和步骤0连接

select
	*
from
	(select 
	t2.course_id,t3.sname,t2.num,t1.cname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid) as t11,(select 
	t2.course_id,max(t2.num) as max_num
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
group by t2.course_id) as t22
where 
	t11.course_id = t22.course_id
	and t11.num = max_num;   #这里的num前面是t11 而不是t2 注意点

| course_id | sname  | num | cname  | course_id | max_num |
+-----------+--------+-----+--------+-----------+---------+
|         1 | 李一   |  91 | 生物   |         1 |      91 |
|         2 | 张四   | 100 | 物理   |         2 |     100 |
|         2 | 铁锤   | 100 | 物理   |         2 |     100 |
|         2 | 李三   | 100 | 物理   |         2 |     100 |
|         3 | 张三   |  87 | 体育   |         3 |      87 |
|         3 | 刘三   |  87 | 体育   |         3 |      87 |
|         4 | 张一   | 100 | 美术   |         4 |     100 |
|         4 | 张二   | 100 | 美术   |         4 |     100 |
|         4 | 张四   | 100 | 美术   |         4 |     100 




21、查询不同课程但成绩相同的课程号、学生号、成绩 --nok
select 
	* 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid;
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | sid | gender | class_id | sname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+----------+--------+
|   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 男     |        1 | 理解   |
|   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   2 | 女     |        1 | 钢蛋   |
|   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   3 | 男     |        1 | 张三   |
|   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   4 | 男     |        1 | 张一   |
|   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   5 | 女     |        1 | 张二   |
|   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   6 | 男     |        1 | 张四   |
|   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   7 | 女     |        2 | 铁锤   |
|   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   8 | 男     |        2 | 李三   |
|   4 | 美术   |          2 |   5 |          1 |         4 |  66 |   1 | 男     |        1 | 理解   |
|   4 | 美术   |          2 |   9 |          2 |         4 |  99 |   2 | 女     |        1 | 钢蛋   |
|   4 | 美术   |          2 |  13 |          3 |         4 |  99 |   3 | 男     |        1 | 张三   |
|   4 | 美术   |          2 |  17 |          4 |         4 | 100 |   4 | 男     |        1 | 张一   |
|   4 | 美术   |          2 |  21 |          5 |         4 | 100 |   5 | 女     |        1 | 张二   |
|   4 | 美术   |          2 |  25 |          6 |         4 | 100 |   6 | 男     |        1 | 张四   |


select 
	t1.cname,t3.sid,t2.num 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
# order by t2.num;
	
# 查询不同课程但成绩相同的课程号、学生号、成绩 

cname  | sid | num |
+--------+-----+-----+
| 生物   |   1 |  10 |
| 生物   |   2 |   8 |
| 生物   |   3 |  77 |
| 生物   |   4 |  79 |
| 生物   |   5 |  79 |
| 生物   |   6 |   9 |
| 生物   |   7 |   9 |
| 生物   |   8 |   9 |
| 生物   |   9 |  91 |
| 生物   |  10 |  90 |
| 生物   |  11 |  90 |
| 生物   |  12 |  90 |
| 物理   |   1 |   9 |
| 物理   |   3 |  66 |
| 物理   |   4 |  11 |
| 物理   |   5 |  11 |
| 物理   |   6 | 100 |
| 物理   |   7 | 100 |
| 物理   |   8 | 100 |
| 物理   |   9 |  88 |
| 物理   |  10 |  77 |
| 物理   |  11 |  77 |
| 物理   |  12 |  77 |
| 体育   |   1 |  76 |
| 体育   |   2 |  68 |
| 体育   |   3 |  87 |
| 体育   |   4 |  67 |
| 体育   |   5 |  67 |
| 体育   |   6 |  67 |
| 体育   |   7 |  67 |
| 体育   |   8 |  67 |
| 体育   |   9 |  67 |
| 体育   |  10 |  43 |
| 体育   |  11 |  43 |
| 体育   |  12 |  43 |
| 体育   |  13 |  87 |
| 美术   |   1 |  66 |
| 美术   |   2 |  99 |
| 美术   |   3 |  99 |
| 美术   |   4 | 100 |
| 美术   |   5 | 100 |
| 美术   |   6 | 100 |
| 美术   |   7 |  88 |
| 美术   |   8 |  88 |
| 美术   |   9 |  22 |
| 美术   |  10 |  87 |
| 美术   |  11 |  87 |
| 美术   |  12 |  87 |


select 
	t1.cname,t3.sid,t2.num 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
order by t2.num;

# 查询不同课程但成绩相同的课程号、学生号、成绩 

 cname  | sid | num |
+--------+-----+-----+
| 生物   |   2 |   8 |
| 生物   |   8 |   9 |
| 生物   |   6 |   9 |
| 物理   |   1 |   9 |
| 生物   |   7 |   9 |
| 生物   |   1 |  10 |
| 物理   |   4 |  11 |
| 物理   |   5 |  11 |
| 美术   |   9 |  22 |
| 体育   |  11 |  43 |
| 体育   |  12 |  43 |
| 体育   |  10 |  43 |
| 物理   |   3 |  66 |
| 美术   |   1 |  66 |
| 体育   |   8 |  67 |
| 体育   |   6 |  67 |
| 体育   |   4 |  67 |
| 体育   |   9 |  67 |
| 体育   |   7 |  67 |
| 体育   |   5 |  67 |
| 体育   |   2 |  68 |
| 体育   |   1 |  76 |
| 物理   |  11 |  77 |
| 物理   |  12 |  77 |
| 物理   |  10 |  77 |

select 
	group_concat(t1.cname),group_concat(t3.sid),t2.num 
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
group by t2.num
order by t2.num;



22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称 

# 1 先查询 学过“李平”老师课程的学生姓名以及选修的课程名称
select
	# *
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
| sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname  |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+-----+--------+
|   1 | 男     |        1 | 理解   |   2 | 物理   |          2 |   2 |          1 |         2 |   9 |   2 | 李平   |
|   3 | 男     |        1 | 张三   |   2 | 物理   |          2 |  11 |          3 |         2 |  66 |   2 | 李平   |
|   4 | 男     |        1 | 张一   |   2 | 物理   |          2 |  15 |          4 |         2 |  11 |   2 | 李平   |
|   5 | 女     |        1 | 张二   |   2 | 物理   |          2 |  19 |          5 |         2 |  11 |   2 | 李平   |
|   6 | 男     |        1 | 张四   |   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   2 | 李平   |
|   7 | 女     |        2 | 铁锤   |   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   2 | 李平   |
|   8 | 男     |        2 | 李三   |   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   2 | 李平   |
|   9 | 男     |        2 | 李一   |   2 | 物理   |          2 |  35 |          9 |         2 |  88 |   2 | 李平   |
|  10 | 女     |        2 | 李二   |   2 | 物理   |          2 |  39 |         10 |         2 |  77 |   2 | 李平   |
|  11 | 男     |        2 | 李四   |   2 | 物理   |          2 |  43 |         11 |         2 |  77 |   2 | 李平   |
|  12 | 女     |        3 | 如花   |   2 | 物理   |          2 |  47 |         12 |         2 |  77 |   2 | 李平   |
|   1 | 男     |        1 | 理解   |   4 | 美术   |          2 |   5 |          1 |         4 |  66 |   2 | 李平   |
|   2 | 女     |        1 | 钢蛋   |   4 | 美术   |          2 |   9 |          2 |         4 |  99 |   2 | 李平   |
|   3 | 男     |        1 | 张三   |   4 | 美术   |          2 |  13 |          3 |         4 |  99 |   2 | 李平   |
|   4 | 男     |        1 | 张一   |   4 | 美术   |          2 |  17 |          4 |         4 | 100 |   2 | 李平   |
|   5 | 女     |        1 | 张二   |   4 | 美术   |          2 |  21 |          5 |         4 | 100 |   2 | 李平   |
|   6 | 男     |        1 | 张四   |   4 | 美术   |          2 |  25 |          6 |         4 | 100 |   2 | 李平   |
|   7 | 女     |        2 | 铁锤   |   4 | 美术   |          2 |  29 |          7 |         4 |  88 |   2 | 李平   |
|   8 | 男     |        2 | 李三   |   4 | 美术   |          2 |  33 |          8 |         4 |  88 |   2 | 李平   |
|   9 | 男     |        2 | 李一   |   4 | 美术   |          2 |  37 |          9 |         4 |  22 |   2 | 李平   |
|  10 | 女     |        2 | 李二   |   4 | 美术   |          2 |  41 |         10 |         4 |  87 |   2 | 李平   |
|  11 | 男     |        2 | 李四   |   4 | 美术   |          2 |  45 |         11 |         4 |  87 |   2 | 李平   |
|  12 | 女     |        3 | 如花   |   4 | 美术   |          2 |  49 |         12 |         4 |  87 |   2 | 李平 

| sid |
+-----+
|   1 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|   2 |


# 2 所有报课的同学
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;
	
# 3 查询没学过“李平”老师课程的学生姓名以及选修的课程名称
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname != '李平';
	
| sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname     |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+-----+-----------+
|   1 | 男     |        1 | 理解   |   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 张磊      |
|   2 | 女     |        1 | 钢蛋   |   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   1 | 张磊      |
|   3 | 男     |        1 | 张三   |   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   1 | 张磊      |
|   4 | 男     |        1 | 张一   |   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   1 | 张磊      |
|   5 | 女     |        1 | 张二   |   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   1 | 张磊      |
|   6 | 男     |        1 | 张四   |   1 | 生物   |          1 |  22 |          6 |         1 |   9 |   1 | 张磊      |
|   7 | 女     |        2 | 铁锤   |   1 | 生物   |          1 |  26 |          7 |         1 |   9 |   1 | 张磊      |
|   8 | 男     |        2 | 李三   |   1 | 生物   |          1 |  30 |          8 |         1 |   9 |   1 | 张磊      |
|   9 | 男     |        2 | 李一   |   1 | 生物   |          1 |  34 |          9 |         1 |  91 |   1 | 张磊      |
|  10 | 女     |        2 | 李二   |   1 | 生物   |          1 |  38 |         10 |         1 |  90 |   1 | 张磊      |
|  11 | 男     |        2 | 李四   |   1 | 生物   |          1 |  42 |         11 |         1 |  90 |   1 | 张磊      |
|  12 | 女     |        3 | 如花   |   1 | 生物   |          1 |  46 |         12 |         1 |  90 |   1 | 张磊      |
|   1 | 男     |        1 | 理解   |   3 | 体育   |          3 |   3 |          1 |         3 |  76 |   3 | 刘海燕    |
|   2 | 女     |        1 | 钢蛋   |   3 | 体育   |          3 |   8 |          2 |         3 |  68 |   3 | 刘海燕    |
|   3 | 男     |        1 | 张三   |   3 | 体育   |          3 |  12 |          3 |         3 |  87 |   3 | 刘海燕    |
|   4 | 男     |        1 | 张一   |   3 | 体育   |          3 |  16 |          4 |         3 |  67 |   3 | 刘海燕    |
|   5 | 女     |        1 | 张二   |   3 | 体育   |          3 |  20 |          5 |         3 |  67 |   3 | 刘海燕    |
|   6 | 男     |        1 | 张四   |   3 | 体育   |          3 |  24 |          6 |         3 |  67 |   3 | 刘海燕    |
|   7 | 女     |        2 | 铁锤   |   3 | 体育   |          3 |  28 |          7 |         3 |  67 |   3 | 刘海燕    |
|   8 | 男     |        2 | 李三   |   3 | 体育   |          3 |  32 |          8 |         3 |  67 |   3 | 刘海燕    |
|   9 | 男     |        2 | 李一   |   3 | 体育   |          3 |  36 |          9 |         3 |  67 |   3 | 刘海燕    |
|  10 | 女     |        2 | 李二   |   3 | 体育   |          3 |  40 |         10 |         3 |  43 |   3 | 刘海燕    |
|  11 | 男     |        2 | 李四   |   3 | 体育   |          3 |  44 |         11 |         3 |  43 |   3 | 刘海燕    |
|  12 | 女     |        3 | 如花   |   3 | 体育   |          3 |  48 |         12 |         3 |  43 |   3 | 刘海燕    |
|  13 | 男     |        3 | 刘三   |   3 | 体育   |          3 |  52 |         13 |         3 |  87 |   3 | 刘海燕 

| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

 # 在第3步 不在第1步 的sid  左连接
select
	*
from
	(select
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname != '李平') as t1 left join (select
		# *
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname = '李平') as t2  on t1.sid = t2.sid;
 
 | sid | sid  |
+-----+------+
|   1 |    1 |
|   2 |    2 |
|   3 |    3 |
|   4 |    4 |
|   5 |    5 |
|   6 |    6 |
|   7 |    7 |
|   8 |    8 |
|   9 |    9 |
|  10 |   10 |
|  11 |   11 |
|  12 |   12 |
|  13 | NULL |


select
	*
from
	(select
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname != '李平') as t1 left join (select
		# *
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname = '李平') as t2  on t1.sid = t2.sid
where t2.sid is null;
 
  sid | sid  |
+-----+------+
|  13 | NULL

select
	*
from 
	student as t1,course as t2,score as t3
where t1.sid = t3.student_id and t3.course_id = t2.cid
and t1.sid= 13;

| sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+
|  13 | 男     |        3 | 刘三   |   3 | 体育   |          3 |  52 |         13 |         3 |  87 

select
	t1.sid,t1.sname,t2.cname
from 
	student as t1,course as t2,score as t3
where t1.sid = t3.student_id and t3.course_id = t2.cid
and t1.sid= 13;

| sid | sname  | cname  |
+-----+--------+--------+
|  13 | 刘三   | 体育 
	

23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名 
# 先查询学号为2的同学选修过的课程

select 
	t3.sid,t2.num,t1.cname,t1.cid
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t3.sid = 2;
	
| sid | num | cname  | cid |
+-----+-----+--------+-----+
|   2 |   8 | 生物   |   1 |
|   2 |  68 | 体育   |   3 |
|   2 |  99 | 美术   |   4 |

select 
	t1.cname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t3.sid = 2;
	
| sid | num | cname  | cid |
+-----+-----+--------+-----+
|   2 |   8 | 生物   |   1 |
|   2 |  68 | 体育   |   3 |
|   2 |  99 | 美术   |   4 |

select 
	t3.sid,t2.num,t1.cname,t1.cid
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname in ('生物','体育','美术');
	
select 
	t3.sid,t3.sname,t2.num,t1.cname,t1.cid
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname in (select 
		t1.cname
	from
		course as t1,score as t2,student as t3
	where 
		t2.course_id = t1.cid and t2.student_id = t3.sid
		and t3.sid = 2);

| sid | sname  | num | cname  | cid |
+-----+--------+-----+--------+-----+
|   1 | 理解   |  10 | 生物   |   1 |
|   2 | 钢蛋   |   8 | 生物   |   1 |
|   3 | 张三   |  77 | 生物   |   1 |
|   4 | 张一   |  79 | 生物   |   1 |
|   5 | 张二   |  79 | 生物   |   1 |
|   6 | 张四   |   9 | 生物   |   1 |
|   7 | 铁锤   |   9 | 生物   |   1 |
|   8 | 李三   |   9 | 生物   |   1 |
|   9 | 李一   |  91 | 生物   |   1 |
|  10 | 李二   |  90 | 生物   |   1 |
|  11 | 李四   |  90 | 生物   |   1 |
|  12 | 如花   |  90 | 生物   |   1 |
|   1 | 理解   |  76 | 体育   |   3 |
|   2 | 钢蛋   |  68 | 体育   |   3 |
|   3 | 张三   |  87 | 体育   |   3 |

select 
	t3.sid,t3.sname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname in (select 
		t1.cname
	from
		course as t1,score as t2,student as t3
	where 
		t2.course_id = t1.cid and t2.student_id = t3.sid
		and t3.sid = 2)

select 
	t11.sid,t11.sname
from
	(select 
	t3.sid,t3.sname
from
	course as t1,score as t2,student as t3
where 
	t2.course_id = t1.cid and t2.student_id = t3.sid
	and t1.cname in (select 
		t1.cname
	from
		course as t1,score as t2,student as t3
	where 
		t2.course_id = t1.cid and t2.student_id = t3.sid
		and t3.sid = 2)) as t11
group by t11.sid;

| sid | sname  |
+-----+--------+
|   1 | 理解   |
|   2 | 钢蛋   |
|   3 | 张三   |
|   4 | 张一   |
|   5 | 张二   |
|   6 | 张四   |
|   7 | 铁锤   |
|   8 | 李三   |
|   9 | 李一   |
|  10 | 李二   |
|  11 | 李四   |
|  12 | 如花   |
|  13 | 刘三 

24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数
# 任课最多的老师
# 方法1
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;
	
| sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname     |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+-----+-----------+
|   1 | 男     |        1 | 理解   |   1 | 生物   |          1 |   1 |          1 |         1 |  10 |   1 | 张磊      |
|   2 | 女     |        1 | 钢蛋   |   1 | 生物   |          1 |   6 |          2 |         1 |   8 |   1 | 张磊      |
|   3 | 男     |        1 | 张三   |   1 | 生物   |          1 |  10 |          3 |         1 |  77 |   1 | 张磊      |
|   4 | 男     |        1 | 张一   |   1 | 生物   |          1 |  14 |          4 |         1 |  79 |   1 | 张磊      |
|   5 | 女     |        1 | 张二   |   1 | 生物   |          1 |  18 |          5 |         1 |  79 |   1 | 张磊      |
|   6 | 男     |        1 | 张四   |   1 | 生物   |          1 |  22 |          6 |         1 |   9 |   1 | 张磊      |
|   7 | 女     |        2 | 铁锤   |   1 | 生物   |          1 |  26 |          7 |         1 |   9 |   1 | 张磊      |
|   8 | 男     |        2 | 李三   |   1 | 生物   |          1 |  30 |          8 |         1 |   9 |   1 | 张磊      |
|   9 | 男     |        2 | 李一   |   1 | 生物   |          1 |  34 |          9 |         1 |  91 |   1 | 张磊      |
|  10 | 女     |        2 | 李二   |   1 | 生物   |          1 |  38 |         10 |         1 |  90 |   1 | 张磊      |
|  11 | 男     |        2 | 李四   |   1 | 生物   |          1 |  42 |         11 |         1 |  90 |   1 | 张磊      |
|  12 | 女     |        3 | 如花   |   1 | 生物   |          1 |  46 |         12 |         1 |  90 |   1 | 张磊      |


select
	t4.tname,group_concat(distinct(t2.cname))
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
group by t4.tname;

| tname     | group_concat(distinct(t2.cname)) |
+-----------+----------------------------------+
| 刘海燕    | 体育                             |
| 张磊      | 生物                             |
| 李平      | 物理,美术   


# 001任课最多的老师
# 方法2
select
	*
from 
	course as t2,teacher as t4
where 
	t2.teacher_id = t4.tid;
| cid | cname  | teacher_id | tid | tname     |
+-----+--------+------------+-----+-----------+
|   1 | 生物   |          1 |   1 | 张磊      |
|   2 | 物理   |          2 |   2 | 李平      |
|   3 | 体育   |          3 |   3 | 刘海燕    |
|   4 | 美术   |          2 |   2 | 李平   


select
	tname,count(*)
from 
	course as t2,teacher as t4
where 
	t2.teacher_id = t4.tid
group by tname;

| tname     | count(*) |
+-----------+----------+
| 刘海燕    |        1 |
| 张磊      |        1 |
| 李平      |        2 |


select
	tname,count(*)
from 
	course as t2,teacher as t4
where 
	t2.teacher_id = t4.tid
group by tname
order by count(*) desc
limit 1;

 tname  | count(*) |
+--------+----------+
| 李平   |        2 

select
	tname
from 
	course as t2,teacher as t4
where 
	t2.teacher_id = t4.tid
group by tname
order by count(*) desc
limit 1;

| tname  |
+--------+
| 李平 

# 24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数

# 002学生单科成绩最高
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = (select
		tname
	from 
		course as t2,teacher as t4
	where 
		t2.teacher_id = t4.tid
	group by tname
	order by count(*) desc
	limit 1);  #子句是李平老师


# select
	# *
# from 
	# student as t1,course as t2,score as t3,teacher as t4
# where 
	# t3.student_id = t1.sid 
	# and t3.course_id = t2.cid
	# and t2.teacher_id = t4.tid
	# and t4.tname = '李平';
	
| sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname  |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+-----+--------+
|   1 | 男     |        1 | 理解   |   2 | 物理   |          2 |   2 |          1 |         2 |   9 |   2 | 李平   |
|   3 | 男     |        1 | 张三   |   2 | 物理   |          2 |  11 |          3 |         2 |  66 |   2 | 李平   |
|   4 | 男     |        1 | 张一   |   2 | 物理   |          2 |  15 |          4 |         2 |  11 |   2 | 李平   |
|   5 | 女     |        1 | 张二   |   2 | 物理   |          2 |  19 |          5 |         2 |  11 |   2 | 李平   |
|   6 | 男     |        1 | 张四   |   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   2 | 李平   |
|   7 | 女     |        2 | 铁锤   |   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   2 | 李平   |
|   8 | 男     |        2 | 李三   |   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   2 | 李平   |
|   9 | 男     |        2 | 李一   |   2 | 物理   |          2 |  35 |          9 |         2 |  88 |   2 | 李平   |
|  10 | 女     |        2 | 李二   |   2 | 物理   |          2 |  39 |         10 |         2 |  77 |   2 | 李平   |
|  11 | 男     |        2 | 李四   |   2 | 物理   |          2 |  43 |         11 |         2 |  77 |   2 | 李平   |
|  12 | 女     |        3 | 如花   |   2 | 物理   |          2 |  47 |         12 |         2 |  77 |   2 | 李平   |
|   1 | 男     |        1 | 理解   |   4 | 美术   |          2 |   5 |          1 |         4 |  66 |   2 | 李平   |
|   2 | 女     |        1 | 钢蛋   |   4 | 美术   |          2 |   9 |          2 |         4 |  99 |   2 | 李平 


select
	max(t3.num)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';

 max(t3.num) |
+-------------+
|         100 |

select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平'
	and t3.num = (select max(t3.num)   #成绩最高的同学
				from student as t1,course as t2,score as t3,teacher as t4
				where t3.student_id = t1.sid 
					and t3.course_id = t2.cid
					and t2.teacher_id = t4.tid
					and t4.tname = '李平');

 sid | gender | class_id | sname  | cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname  |
+-----+--------+----------+--------+-----+--------+------------+-----+------------+-----------+-----+-----+--------+
|   6 | 男     |        1 | 张四   |   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   2 | 李平   |
|   7 | 女     |        2 | 铁锤   |   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   2 | 李平   |
|   8 | 男     |        2 | 李三   |   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   2 | 李平   |
|   4 | 男     |        1 | 张一   |   4 | 美术   |          2 |  17 |          4 |         4 | 100 |   2 | 李平   |
|   5 | 女     |        1 | 张二   |   4 | 美术   |          2 |  21 |          5 |         4 | 100 |   2 | 李平   |
|   6 | 男     |        1 | 张四   |   4 | 美术   |          2 |  25 |          6 |         4 | 100 |   2 | 李平  


# 任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数

select
	t2.cid,t1.sname,t3.num
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平'
	and t3.num = (select
					max(t3.num)
				from 
					student as t1,course as t2,score as t3,teacher as t4
				where 
					t3.student_id = t1.sid 
					and t3.course_id = t2.cid
					and t2.teacher_id = t4.tid
					and t4.tname = '李平');

| cid | sname  | num |
+-----+--------+-----+
|   2 | 张四   | 100 |
|   2 | 铁锤   | 100 |
|   2 | 李三   | 100 |
|   4 | 张一   | 100 |
|   4 | 张二   | 100 |
|   4 | 张四   | 100 

```












































