五张表关系:
	class <=> student  关联:class_id
	teacher <=> course 关联:teacher_id
	score <=> student  关联: student.sid <=>student_id
	score <=> course   关联: course.cid <=> course_id


1、查询所有的课程的名称以及对应的任课老师姓名
# where 
select
	teacher.tname,course.cname
from
	teacher,course
where
	teacher.tid = course.teacher_id
	
# inner join
select
	t.tname,c.cname
from
	teacher as t inner join course as c on t.tid = c.teacher_id

	
2、查询学生表中男女生各有多少人
select
	gender,count(*)
from 
	student
group by 
	gender

3、查询物理成绩等于100的学生的姓名
# where
select
	st.sname , sc.num
from
	course as c,score as sc,student as st
where
	c.cid = sc.course_id 
	and
	st.sid = sc.student_id
	and
	sc.num = 100
	and
	c.cname = "物理"
	
# inner join 
select 
	st.sname , sc.num
from
	course as c inner join score as sc on c.cid = sc.course_id 
	inner join student as st on st.sid = sc.student_id
where
	sc.num = 100
	and
	c.cname = "物理"
	

4、查询平均成绩大于八十分的同学的姓名和平均成绩
# 搜一下id
select 
	score.student_id
from 
	score
group by 
	score.student_id
having
	avg(score.num) > 80

# 通过联表把id对应的姓名搜出来
select 
	score.student_id,student.sname
from 
	score inner join student on student.sid = score.student_id
group by 
	score.student_id
having
	avg(score.num) > 80

# where
select 
	score.student_id,student.sname
from 
	score , student
where	
	student.sid = score.student_id
group by 
	score.student_id
having
	avg(score.num) > 80

5、查询所有学生的学号，姓名，选课数，总成绩

# 1.选课数
# 查询的是score , 以参加考试的实际学生统计数量
select
	student_id,count(*)
from
	score
group by
	score.student_id
	
# 查询的是student , 以实际的学生id为参考标准,统计数量
select
	student.sid,count(score.course_id)
from
	score right join student on score.student_id = student.sid
group by
	student.sid
	
# 2.总成绩
select
	student.sid,sum(score.num)
from
	score right join student on score.student_id = student.sid
group by
	student.sid
	
# 综合拼接
select
	student.sid,student.sname,count(score.course_id),sum(score.num)
from
	score right join student on score.student_id = student.sid
group by
	student.sid
	
select class_id from student group by sid;


6、 查询姓李老师的个数

7、 查询没有报李平老师课的学生姓名

8、 查询物理课程的分数比生物课程的分数高的学生的学号

9、 查询没有同时选修物理课程和体育课程的学生姓名

10、查询挂科超过两门(包括两门)的学生姓名和班级

11、查询选修了所有课程的学生姓名

12、查询李平老师教的课程的所有成绩记录

13、查询全部学生都选修了的课程号和课程名

14、查询每门课程被选修的次数

15、查询只选修了一门课程的学生学号和姓名

16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

17、查询平均成绩大于85的学生姓名和平均成绩

18、查询生物成绩不及格的学生姓名和对应生物分数

19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名

20、查询每门课程成绩最好的课程id、学生姓名和分数

21、查询不同课程但成绩相同的课程号、学生号、成绩 

22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称 

23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名 

24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数