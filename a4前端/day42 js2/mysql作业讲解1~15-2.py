五张表关系:
	class <=> student  关联:class_id
	teacher <=> course 关联:teacher_id
	score <=> student  关联: student.sid <=>student_id
	score <=> course   关联: course.cid <=> course_id


1、查询所有的课程的名称以及对应的任课老师姓名
# 1 方法1 where 连表
select
	cname,tname
from
	course as t1,teacher as t2
where
	t1.teacher_id = t2.tid;
	
# | cname  | tname     |
# +--------+-----------+
# | 生物   | 张磊      |
# | 物理   | 李平      |
# | 体育   | 刘海燕    |
# | 美术   | 李平  

# 2 方法2 inner join on 连表
select
	cname,tname
from
	course as t1 
	inner join teacher as t2
	on t1.teacher_id = t2.tid;

# | cname  | tname     |
# +--------+-----------+
# | 生物   | 张磊      |
# | 物理   | 李平      |
# | 体育   | 刘海燕    |
# | 美术   | 李平 
	
2、查询学生表中男女生各有多少人
select
	gender,count(*)
from
	student
group by gender;
 # gender | count(*) |
# +--------+----------+
# | 女     |        6 |
# | 男     |       10 


3、查询物理成绩等于100的学生的姓名
# 1 方法1 where 连表 推荐
select
	t2.sname
from 
	score as t1,student as t2,course as t3
where
	t1.student_id = t2.sid and
	t1.course_id = t3.cid and
	t1.num = 100 and
	t3.cname = '物理';

# | sname  |
# +--------+
# | 张四   |
# | 铁锤   |
# | 李三  

# 2 方法2 inner join on 连表
select
	t2.sname
from 
	score as t1 inner join student as t2 on t1.student_id = t2.sid
	inner join course as t3 on t1.course_id = t3.cid
where
	t1.num = 100 and
	t3.cname = '物理';
	
# | sname  |
# +--------+
# | 张四   |
# | 铁锤   |
# | 李三 
	

4、查询平均成绩大于八十分的同学的姓名和平均成绩
# 方法1 连表
# 1 搜一下平均成绩大于八十分的同学的id
select
	student_id,avg(num) as avg_num
from
	score as t1
group by
	t1.student_id
having
	avg_num > 80;
	
 # student_id | avg_num |
# +------------+---------+
# |          3 | 82.2500 |
# |         13 | 87.0000


# 2 通过联表把id对应的姓名搜出来
select
	student_id,t2.sname,avg(num) as avg_num
from
	score as t1,student as t2
where
	t1.student_id = t2.sid
group by
	t1.student_id
having
	avg_num > 80;
# | student_id | sname  | avg_num |
# +------------+--------+---------+
# |          3 | 张三   | 82.2500 |
# |         13 | 刘三   | 87.0000 


5、查询所有学生的学号，姓名，选课数，总成绩
# 1.选课数
# 查询的是score , 以参加考试的实际学生统计数量
select
	student_id,count(*) as 选课数
from
	score
group by
	student_id;
	
# | student_id | 选课数    |
# +------------+-----------+
# |          1 |         4 |
# |          2 |         3 |
# |          3 |         4 |
# |          4 |         4 |
# |          5 |         4 |
# |          6 |         4 |
# |          7 |         4 |
# |          8 |         4 |
# |          9 |         4 |
# |         10 |         4 |
# |         11 |         4 |
# |         12 |         4 |
# |         13 |         1

# 2.总成绩
select
	student_id,count(*) as 选课数,sum(num)
from
	score
group by
	student_id;
	
# | student_id | 选课数    | sum(num) |
# +------------+-----------+----------+
# |          1 |         4 |      161 |
# |          2 |         3 |      175 |
# |          3 |         4 |      329 |
# |          4 |         4 |      257 |
# |          5 |         4 |      257 |
# |          6 |         4 |      276 |
# |          7 |         4 |      264 |
# |          8 |         4 |      264 |
# |          9 |         4 |      268 |
# |         10 |         4 |      297 |
# |         11 |         4 |      297 |
# |         12 |         4 |      297 |
# |         13 |         1 |       87

	
# 3 连表，得到学生的姓名
select
	t2.sid,t2.sname,count(t1.course_id) as 选课数,sum(t1.num)
from
	score as t1 right join student as t2 on t1.student_id = t2.sid
group by
	# t1.student_id;  #这里如果不是主键或者unique属性，select后面的字段必须和group by后面的保持一致，否则报错
	t2.sid;  #这里如果是主键或者unique属性，select后面的字段不限制  t2.sid是主键
	# 结论：group by后面的字段优先选择主键或者unique属性
	
# | sid | sname  | 选课数    | sum(t1.num) |
# +-----+--------+-----------+-------------+
# |   1 | 理解   |         4 |         161 |
# |   2 | 钢蛋   |         3 |         175 |
# |   3 | 张三   |         4 |         329 |
# |   4 | 张一   |         4 |         257 |
# |   5 | 张二   |         4 |         257 |
# |   6 | 张四   |         4 |         276 |
# |   7 | 铁锤   |         4 |         264 |
# |   8 | 李三   |         4 |         264 |
# |   9 | 李一   |         4 |         268 |
# |  10 | 李二   |         4 |         297 |
# |  11 | 李四   |         4 |         297 |
# |  12 | 如花   |         4 |         297 |
# |  13 | 刘三   |         1 |          87 |
# |  14 | 刘一   |         0 |        NULL |
# |  15 | 刘二   |         0 |        NULL |
# |  16 | 刘四   |         0 |        NULL |
	

6、 查询姓李老师的个数
select
	count(*)
from
	teacher
where
	tname like '李%';
	
# | count(*) |
# +----------+
# |        2 

7、 查询没有报李平老师课的学生姓名
# 1.报了李平老师课程的学生id
select
	distinct(t3.student_id)
from
	teacher as t1,course as t2,score as t3
where
	t1.tid = t2.teacher_id and
	t2.cid = t3.course_id and
	t1.tname = '李平';
	
# | student_id |
# +------------+
# |          1 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |
# |          2 |

	
# 2.查询学生表,除了这些个id的学生,剩下的都是没有报李平老师课程的  not in
select
	t4.sname
from
	student as t4
where
	t4.sid not in (1,2,3,4,5,6,7,8,9,10,11,12);   #这里的小括号用步骤1替换
	
# | sname  |
# +--------+
# | 刘三   |
# | 刘一   |
# | 刘二   |
# | 刘四  


# 3.综合拼接
select
	t4.sname
from
	student as t4
where
	t4.sid not in (select
	distinct(t3.student_id)
from
	teacher as t1,course as t2,score as t3
where
	t1.tid = t2.teacher_id and
	t2.cid = t3.course_id and
	t1.tname = '李平');


select
	sname
from
	student
where
	sid not in (select
	distinct(t3.student_id)
from
	teacher as t1,course as t2,score as t3
where
	t1.tid = t2.teacher_id and
	t2.cid = t3.course_id and
	t1.tname = '李平');
	
# | sname  |
# +--------+
# | 刘三   |
# | 刘一   |
# | 刘二   |
# | 刘四   |

	
8、 查询物理课程的分数比生物课程的分数高的学生的学号
# 1.物理课程学生的分数查询
select
	t2.student_id,t2.num as physical_score
from
	course as t1,score as t2
where
	t1.cid = t2.course_id and
	t1.cname = '物理';
	
# | student_id | 物理分    |
# +------------+-----------+
# |          1 |         9 |
# |          3 |        66 |
# |          4 |        11 |
# |          5 |        11 |
# |          6 |       100 |
# |          7 |       100 |
# |          8 |       100 |
# |          9 |        88 |
# |         10 |        77 |
# |         11 |        77 |
# |         12 |        77 

# 2.生物课程学生的分数查询
select
	t2.student_id,t2.num as  biological_scrore
from
	course as t1,score as t2
where
	t1.cid = t2.course_id and
	t1.cname = '生物';
	
# | student_id | 生物分    |
# +------------+-----------+
# |          1 |        10 |
# |          2 |         8 |
# |          3 |        77 |
# |          4 |        79 |
# |          5 |        79 |
# |          6 |         9 |
# |          7 |         9 |
# |          8 |         9 |
# |          9 |        91 |
# |         10 |        90 |
# |         11 |        90 |
# |         12 |        90 

	
# 3.综合拼接前2步 连表
select 
	t1.student_id
from
	(步骤1) as t1, (步骤2) as t2
where
	t1.student_id = t2.student_id;

 查询物理课程的分数比生物课程的分数高的学生的学号	
 
# 4.终极版
select 
	t11.student_id,t11.physical_score,t22.biological_scrore  #这里的t11和t22都是别名
from
	(select
		t2.student_id,t2.num as physical_score
	from
		course as t1,score as t2
	where
		t1.cid = t2.course_id and
		t1.cname = '物理') as t11, 
	(select
		t2.student_id,t2.num as  biological_scrore
	from
		course as t1,score as t2
	where
		t1.cid = t2.course_id and
		t1.cname = '生物') as t22
where
	t11.student_id = t22.student_id and
	t11.physical_score > t22.biological_scrore;
	
# | student_id | physical_score | biological_scrore |
# +------------+----------------+-------------------+
# |          1 |              9 |                10 |
# |          3 |             66 |                77 |
# |          4 |             11 |                79 |
# |          5 |             11 |                79 |
# |          6 |            100 |                 9 |
# |          7 |            100 |                 9 |
# |          8 |            100 |                 9 |
# |          9 |             88 |                91 |
# |         10 |             77 |                90 |
# |         11 |             77 |                90 |
# |         12 |             77 |                90 

# | student_id | physical_score | biological_scrore |
# +------------+----------------+-------------------+
# |          6 |            100 |                 9 |
# |          7 |            100 |                 9 |
# |          8 |            100 |                 9 |
	
	
9、 查询没有同时选修物理课程和体育课程的学生姓名
# 方法1 子查询
# 1.找物理和体育的课程id
select
	cid
from 
	course
where
	cname in ('物理','体育');
	
# | cid |
# +-----+
# |   2 |
# |   3 |

	
# 2.找学习物理体育课程的学生id
select
	student_id
from 
	score
where
	course_id in (2,3);  #小括号内是步骤1

# 3.拼接数据
select
	student_id
from 
	score
where
	course_id in (select
		cid
	from 
		course
	where
		cname in ('物理','体育'));


# 4.(同时)学习体育+物理学生id   关键点
select
	student_id
from 
	score
where
	course_id in (select
		cid
	from 
		course
	where
		cname in ('物理','体育'))
group by student_id
having count(*) = 2;

# | student_id |
# +------------+
# |          1 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |

	
# 5.除了这些个id的剩下的学生就是没有同时选择的学生;
select
	sid,sname
from 
	student
where
	sid not in (步骤4);

	
# 6.拼接数据  #3层子查询
select
	sid,sname
from 
	student
where
	sid not in (select
		student_id
	from 
		score
	where
		course_id in (select
			cid
		from 
			course
		where
			cname in ('物理','体育'))
	group by student_id
	having count(*) = 2);

# | sid | sname  |
# +-----+--------+
# |   2 | 钢蛋   |
# |  13 | 刘三   |
# |  14 | 刘一   |
# |  15 | 刘二   |
# |  16 | 刘四 

# 方法2 连表   推荐  更简洁
# 1.找学习物理体育课程的学生id
select
	t2.student_id
from
	course as t1,score as t2
where
	t1.cid = t2.course_id and
	t1.cname in ('物理','生物');
	
# | student_id |
# +------------+
# |          1 |
# |          2 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |
# |          1 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |


# 2.(同时)学习体育+物理学生id   关键点
select
	t2.student_id
from
	course as t1,score as t2
where
	t1.cid = t2.course_id and
	t1.cname in ('物理','生物')
group by t2.student_id
having count(*) = 2;

# | student_id |
# +------------+
# |          1 |
# |          3 |
# |          4 |
# |          5 |
# |          6 |
# |          7 |
# |          8 |
# |          9 |
# |         10 |
# |         11 |
# |         12 |
	
# 3.除了这些个id的剩下的学生就是没有同时选择的学生;
select
    sid,sname
from
	student
where
	sid not in (select
		t2.student_id
	from
		course as t1,score as t2
	where
		t1.cid = t2.course_id and
		t1.cname in ('物理','生物')
	group by t2.student_id
	having count(*) = 2);

# | sid | sname  |
# +-----+--------+
# |   2 | 钢蛋   |
# |  13 | 刘三   |
# |  14 | 刘一   |
# |  15 | 刘二   |
# |  16 | 刘四  
	
	
10、查询挂科超过两门(包括两门)的学生姓名和班级
#连表
# 挂科:成绩小于60分
select
	t2.sname,t3.caption
from
	score as t1,student as t2,class as t3
where
	t1.student_id = t2.sid and
	t2.class_id = t3.cid and
	t1.num < 60
group by 
	# t1.student_id
	# 这里虽然不是主键或unique属性,但是select后的字段不是t1表的,也可以写  
	# 注意点
	t2.sid  #这里是主键或unique属性,select后的字段不受限制
having 
	count(*) >= 2;
	
| sname  | caption      |
+--------+--------------+
| 理解   | 三年二班 


11、查询选修了所有课程的学生姓名
# 方法1  子查询
# 1统计所有课程总数-数目
select 
	count(*)
from
	course;
	
 # count(*) |
# +----------+
# |        4 |

select 
	*
from
	course;
# | cid | cname  | teacher_id |
# +-----+--------+------------+
# |   1 | 生物   |          1 |
# |   2 | 物理   |          2 |
# |   3 | 体育   |          3 |
# |   4 | 美术   |          2 |

# 2.按照学生进行分类,统计课程总数是步骤1的学生姓名
mysql> select
    -> student_id,count(course_id)
    -> from
    -> score
    -> group by
    -> student_id
    -> having 
    -> count(course_id) = 4;
# +------------+------------------+
# | student_id | count(course_id) |
# +------------+------------------+
# |          1 |                4 |
# |          3 |                4 |
# |          4 |                4 |
# |          5 |                4 |
# |          6 |                4 |
# |          7 |                4 |
# |          8 |                4 |
# |          9 |                4 |
# |         10 |                4 |
# |         11 |                4 |
# |         12 |                4 |

select
	student_id,sname,count(course_id)
from
	score as t1,student as t2
where 
	t1.student_id = t2.sid
group by
	student_id
having 
	count(course_id) = 4;  //这里的4是步骤1

# | student_id | sname  | count(course_id) |
# +------------+--------+------------------+
# |          1 | 理解   |                4 |
# |          3 | 张三   |                4 |
# |          4 | 张一   |                4 |
# |          5 | 张二   |                4 |
# |          6 | 张四   |                4 |
# |          7 | 铁锤   |                4 |
# |          8 | 李三   |                4 |
# |          9 | 李一   |                4 |
# |         10 | 李二   |                4 |
# |         11 | 李四   |                4 |
# |         12 | 如花   |                4 
	
# 3.综合拼接
select
	student_id,sname,count(course_id)
from
	score as t1,student as t2
where 
	t1.student_id = t2.sid
group by
	student_id
having 
	count(course_id) = (select 	count(*) from course);
	
# | student_id | sname  | count(course_id) |
# +------------+--------+------------------+
# |          1 | 理解   |                4 |
# |          3 | 张三   |                4 |
# |          4 | 张一   |                4 |
# |          5 | 张二   |                4 |
# |          6 | 张四   |                4 |
# |          7 | 铁锤   |                4 |
# |          8 | 李三   |                4 |
# |          9 | 李一   |                4 |
# |         10 | 李二   |                4 |
# |         11 | 李四   |                4 |
# |         12 | 如花   |                4 |


12、查询李平老师教的课程的所有成绩记录
# 方法1:
# 内联  推荐 更简洁
select
	student_id,course_id,num
from
	teacher as t1,course as t2,score as t3
where 
	t1.tid = t2.teacher_id and
	t2.cid = t3.course_id and
	t1.tname = '李平';
	
# | student_id | course_id | num |
# +------------+-----------+-----+
# |          1 |         2 |   9 |
# |          3 |         2 |  66 |
# |          4 |         2 |  11 |
# |          5 |         2 |  11 |
# |          6 |         2 | 100 |
# |          7 |         2 | 100 |
# |          8 |         2 | 100 |
# |          9 |         2 |  88 |
# |         10 |         2 |  77 |
# |         11 |         2 |  77 |
# |         12 |         2 |  77 |
# |          1 |         4 |  66 |
# |          2 |         4 |  99 |
# |          3 |         4 |  99 |
# |          4 |         4 | 100 |
# |          5 |         4 | 100 |
# |          6 |         4 | 100 |
# |          7 |         4 |  88 |
# |          8 |         4 |  88 |
# |          9 |         4 |  22 |
# |         10 |         4 |  87 |
# |         11 |         4 |  87 |
# |         12 |         4 |  87 |

# 方法2:
# 子查询
# 1.找李平老师的课程id
select
	t2.cid
from
	teacher as t1,course as t2
where
	t1.tid = t2.teacher_id
	and tname = '李平';
	
# | cid |
# +-----+
# |   2 |
# |   4 


# 2 找课程id对应的成绩记录  in
select
	*
from
	score
where
	course_id in (2,4);  //(2,4)是步骤1
	
# 3综合拼接
# 全部字段
select   
	*
from
	score
where
	course_id in (select
	t2.cid
from
	teacher as t1,course as t2
where
	t1.tid = t2.teacher_id
	and tname = '李平'); 

# 选取字段	
select   
	student_id,course_id,num
from
	score
where
	course_id in (select
	t2.cid
from
	teacher as t1,course as t2
where
	t1.tid = t2.teacher_id
	and tname = '李平'); 
	
# | student_id | course_id | num |
# +------------+-----------+-----+
# |          1 |         2 |   9 |
# |          3 |         2 |  66 |
# |          4 |         2 |  11 |
# |          5 |         2 |  11 |
# |          6 |         2 | 100 |
# |          7 |         2 | 100 |
# |          8 |         2 | 100 |
# |          9 |         2 |  88 |
# |         10 |         2 |  77 |
# |         11 |         2 |  77 |
# |         12 |         2 |  77 |
# |          1 |         4 |  66 |
# |          2 |         4 |  99 |
# |          3 |         4 |  99 |
# |          4 |         4 | 100 |
# |          5 |         4 | 100 |
# |          6 |         4 | 100 |
# |          7 |         4 |  88 |
# |          8 |         4 |  88 |
# |          9 |         4 |  22 |
# |         10 |         4 |  87 |
# |         11 |         4 |  87 |
# |         12 |         4 |  87 

13、查询全部学生都选修了的课程号和课程名
# 方法1 子查询
# 1.通过score表,把有成绩的学生个数统计一下
select
	count(distinct(student_id)) as count1
from
	score;
	
# | count(distinct(student_id)) |
# +-----------------------------+
# |                          13 
	
# 2.通过课程id进行分类,找学生的个数
select 
	course_id,cname,count(student_id) as count2
from
	score as t1,course as t2
where t1.course_id = t2.cid
group by course_id
having count2 = 13;  //13是步骤1

# | course_id | cname  | count2 |
# +-----------+--------+--------+
# |         3 | 体育   |     13
	
# 3.综合拼接
select 
	course_id,cname,count(student_id) as count2
from
	score as t1,course as t2
where t1.course_id = t2.cid
group by course_id
having count2 = (select
	count(distinct(student_id)) as count1
from
	score);
# | course_id | cname  | count2 |
# +-----------+--------+--------+
# |         3 | 体育   |     13 


# 方法2 连表  推荐 更简洁
select 
	course_id,cname,count(student_id) as count2
from
	score as t1,course as t2
where t1.course_id = t2.cid
group by course_id;

# | course_id | cname  | count2 |
# +-----------+--------+--------+
# |         1 | 生物   |     12 |
# |         2 | 物理   |     11 |
# |         3 | 体育   |     13 |
# |         4 | 美术   |     12 

select 
	course_id,cname,count(student_id) as count2
from
	score as t1,course as t2
where t1.course_id = t2.cid
group by course_id
order by count2 desc
limit 1;

# | course_id | cname  | count2 |
# +-----------+--------+--------+
# |         3 | 体育   |     13 


14、查询每门课程被选修的次数
select
	course_id,count(*)
from
	score
group by course_id;

# | course_id | count(*) |
# +-----------+----------+
# |         1 |       12 |
# |         2 |       11 |
# |         3 |       13 |
# |         4 |       12
	
15、查询只选修了一门课程的学生学号和姓名
# 方法1  连表 推荐
# 1.按照学生分类,统计课程数为1的学生id
select
	student_id,count(*)
from
	score
group by student_id
having count(*) = 1;

# | student_id | count(*) |
# +------------+----------+
# |         13 |        1 


# 2.顺着1号查询出来的数据,顺手连一张学生表,把姓名带上
select
	student_id,sname,count(*)
from
	score as t1, student as t2
where 
	t1.student_id = t2.sid
group by student_id
having count(*) = 1;

# | student_id | sname  | count(*) |
# +------------+--------+----------+
# |         13 | 刘三   |        1 



16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

17、查询平均成绩大于85的学生姓名和平均成绩

18、查询生物成绩不及格的学生姓名和对应生物分数

19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名

20、查询每门课程成绩最好的课程id、学生姓名和分数

21、查询不同课程但成绩相同的课程号、学生号、成绩 

22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称 

23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名 

24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数




