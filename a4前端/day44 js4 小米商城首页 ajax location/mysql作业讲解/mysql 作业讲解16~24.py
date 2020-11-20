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
	

6、 查询姓李老师的个数
select 
	count(*)
from
	teacher
where
	tname like "李%"

7、 查询没有报李平老师课的学生姓名
# 1.报了李平老师课程的学生id
select
	distinct(score.student_id)
from
	teacher,course,score
where
	teacher.tid = course.teacher_id
	and
	course.cid = score.course_id
	and
	teacher.tname = "李平"
	
# 2.查询学生表,除了这些个id的学生,剩下的都是没有报李平老师课程的
select 
	sid,sname
from 
	student
where
	sid not in (1号)

# 综合拼接
select 
	sid,sname
from 
	student
where
	sid not in (select
	distinct(score.student_id)
from
	teacher,course,score
where
	teacher.tid = course.teacher_id
	and
	course.cid = score.course_id
	and
	teacher.tname = "李平")
	
8、 查询物理课程的分数比生物课程的分数高的学生的学号
# 1.物理课程学生的分数查询
select
	score.student_id,score.num,course.cid,course.cname
from
	course,score
where
	course.cid = score.course_id
	and
	course.cname="物理"
# 2.生物课程学生的分数查询
select
	score.student_id,score.num,course.cid,course.cname
from
	course,score
where
	course.cid = score.course_id
	and
	course.cname="生物"
	
# 3.综合拼接
select 
	student_id
from 
	(1号) as t1 inner join (2号) as t2 on t1.student_id = t2.student_id
where
	t1.num > t2.num
	
# 终极版
select 
	t1.student_id
from 
	(select
	score.student_id,score.num,course.cid,course.cname
from
	course,score
where
	course.cid = score.course_id
	and
	course.cname="物理") as t1 inner join (select
	score.student_id,score.num,course.cid,course.cname
from
	course,score
where
	course.cid = score.course_id
	and
	course.cname="生物") as t2 on t1.student_id = t2.student_id
where
	t1.num > t2.num
		
	
	
9、 查询没有同时选修物理课程和体育课程的学生姓名
# 1.找物理和体育的课程id
select 
	cid
from 
	course
where
	cname="物理"
	or
	cname="体育"
	
# 2.找学习物理体育课程的学生id
select
	student_id
from
	score
where  
	course_id in (2,3)

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
	cname="物理"
	or
	cname="体育"
	)
# 4.(同时)学习体育+物理学生id
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
	cname="物理"
	or
	cname="体育"
	)
group by 
	student_id
having
	count(*) = 2
	
# 5.除了这些个id的剩下的学生就是没有同时选择的学生;
select
	sid,sname
from 
	student
where
	sid not in (4号)
	
# 6.拼接数据
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
	cname="物理"
	or
	cname="体育"
	)
group by 
	student_id
having
	count(*) = 2)
	
	
	
10、查询挂科超过两门(包括两门)的学生姓名和班级
select
	student.sname , class.caption
from
	student,class,score
where
	student.class_id = class.cid
	and
	student.sid = score.student_id
	and
	num < 60
group by
	score.student_id
having 
	count(*) >= 2

11、查询选修了所有课程的学生姓名

# 1统计所有课程总数
select count(*) from course;
# 2.按照学生进行分类,
select
	score.student_id,student.sname
from
	score inner join student on score.student_id = student.sid
group by
	score.student_id
having 
	count(*) = (1号)
# 3.综合拼接
select
	score.student_id,student.sname
from
	score inner join student on score.student_id = student.sid
group by
	score.student_id
having 
	count(*) = (select count(*) from course);


12、查询李平老师教的课程的所有成绩记录

# 内联
select 
	s.student_id , c.cname , s.num
from 
	teacher as t,course as c,score as s
where
	t.tid = c.teacher_id
	and
	c.cid = s.course_id
	and
	t.tname = "李平"

# 子查询
# 1.找李平老师的课程id
select 
	course.cid
from 
	teacher,course
where 
	teacher.tid = course.teacher_id
	and
	tname = "李平"
	
# 2.通过课程id,找对应的成绩
select 
	*
from 
	score
where 
	course_id in (1号)
	
# 综合拼接
select 
	course_id,num
from 
	score
where 
	course_id in (select 
	course.cid
from 
	teacher,course
where 
	teacher.tid = course.teacher_id
	and
	tname = "李平")


13、查询全部学生都选修了的课程号和课程名
# 1.通过score表,把有成绩的学生个数统计一下
select 
	count(distinct(student_id))
from 
	score;
	
# 2.通过课程id进行分类,找学生的个数
select 
	course_id
from 
	score
group by
	score.course_id
having 
	count(*) = (1号)
	
# 3.综合拼接
select 
	course_id,course.cname
from 
	score,course
where 
	score.course_id = course.cid
group by
	score.course_id
having 
	count(*) = (select 
	count(distinct(student_id))
from 
	score)

14、查询每门课程被选修的次数
select 
	course_id,count(*)
from 
	score
group by
	course_id
	
15、查询只选修了一门课程的学生学号和姓名
# 1.按照学生分类,统计课程数为1的学生id
select
	student_id
from
	score
group by
	student_id
having
	count(*) = 1
# 2.顺着1号查询出来的数据,顺手连一张学生表,把姓名带上
select
	student_id,sname
from
	score,student
where
	student.sid = score.student_id
group by
	student_id
having
	count(*) = 1


16、查询所有学生考出的成绩并按从高到低排序（成绩去重）
# 同样的分数由多个学生考中; 推荐使用第一种
select
	distinct(num),group_concat(distinct(student_id))
from 
	score
group by
	num
order by
	num desc

# 有逻辑冲突,不能对平均分去重
select
	student_id,group_concat(distinct(num)),avg(num)
from 
	score
group by
	student_id
order by
	avg(num) desc



17、查询平均成绩大于85的学生姓名和平均成绩
select 
	student.sname,avg(num)
from 
	score,student
where 
	score.student_id = student.sid
group by
	score.student_id
having
	avg(num) > 85

18、查询生物成绩不及格的学生姓名和对应生物分数
select
	sname,num
from
	course,student,score
where
	course.cid = score.course_id
	and
	score.student_id = student.sid
	and
	course.cname = '生物'
	and
	score.num < 60;


19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)
	平均成绩最高的学生姓名
	
# 1.找李平老师的课程id
select
	cid
from 
	teacher inner join course on teacher.tid = course.teacher_id
where
	teacher.tname = "李平"
	
# 2.学习李平老师课程的学生中,找平均成绩最高的学生id
select 
	student_id
from
	score
where
	score.course_id in (1号)
group by
	student_id
having 
	avg(num) desc
limit 1

# 综合拼装 
# 连一张学生表,顺手查姓名
select 
	student_id,sname
from
	score inner join student on score.student_id = student.sid
where
	score.course_id in (2,4)
group by
	student_id
order by 
	avg(num) desc
limit 1



# 终极
select 
	student_id,sname
from
	score inner join student on score.student_id = student.sid
where
	score.course_id in (select
	cid
from 
	teacher inner join course on teacher.tid = course.teacher_id
where
	teacher.tname = "李平")
group by
	student_id
order by 
	avg(num) desc
limit 1


20、查询每门课程成绩最好的课程id、学生姓名和分数
# 1.找出成绩的最大分数
select
	course_id,max(num) as max_num
from
	score
group by 
	score.course_id
	
# 2.找分数对应的学生id
select
	student_id , sname , t1.course_id , t3.max_num
from
	score as t1 inner join student as t2 on t1.student_id = t2.sid
	inner join (1号) as t3 on t1.course_id = t3.course_id

# 3.综合拼接
select
	student_id , sname , t1.course_id , t3.max_num
from
	score as t1 inner join student as t2 on t1.student_id = t2.sid
	inner join (select
	course_id,max(num) as max_num
from
	score
group by 
	score.course_id) as t3 on t1.course_id = t3.course_id
where
	t1.num = t3.max_num

21、查询不同课程但成绩相同的课程号、学生号、成绩 

select
	s1.course_id as s1_course_id,
	s2.course_id as s2_course_id,
	s1.student_id as s1_student_id,
	s2.student_id as s2_student_id,
	s1.num as s1_num,
	s2.num as s2_num

from 
	score as s1,
	score as s2
where
	s1.num = s2.num
	and
	s1.course_id > s2.course_id

22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称  同7题;

23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名 
# 1.学号为2的同学,学了什么学科
select
	course_id
from 
	score
where
	student_id = 2
# 1 3 4

# 2.学过 1 3 4 学科的学生都有哪些id
select 
	distinct(sid),sname
from 
	score inner join student on score.student_id = student.sid
where
	score.course_id in (1号 => 1 3 4)

# 3.综合拼接
select 
	distinct(student_id),sname
from 
	score inner join student on score.student_id = student.sid
where
	score.course_id in (select
	course_id
from 
	score
where
	student_id = 2)
	
24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数

# 1.老师任课的最大数量是几?
select
	count(*)
from 
	course
group by
	teacher_id
order by
	count(*) desc
limit 1

# 2.找任课最大数量为2的老师id
select
	teacher_id
from 
	course
group by
	teacher_id
having
	count(*) = (1号)

# 综合拼接
select
	teacher_id
from 
	course
group by
	teacher_id
having
	count(*) = (select
	count(*)
from 
	course
group by
	teacher_id
order by
	count(*) desc
limit 1)


# 3.通过老师id , 找所教的课程id

select
	cid
from 
	course
where
	teacher_id in (2号)


# 综合拼装
select
	cid
from 
	course
where
	teacher_id in (select
	teacher_id
from 
	course
group by
	teacher_id
having
	count(*) = (select
	count(*)
from 
	course
group by
	teacher_id
order by
	count(*) desc
limit 1))


# 4.通过课程id,找其中的最大值(分数的最大值)

select 
	max(num) as max_num
from 
	score
where
	course_id in (3号)
group by
	course_id
	
# 综合拼装
select 
	course_id,max(num) as max_num
from 
	score
where
	course_id in (select
	cid
from 
	course
where
	teacher_id in (select
	teacher_id
from 
	course
group by
	teacher_id
having
	count(*) = (select
	count(*)
from 
	course
group by
	teacher_id
order by
	count(*) desc
limit 1)))
group by
	course_id

# 5.把对应的学生姓名,最大分数拼在一起,做单表联查
select 
	student.sid,student.sname,t3.max_num
from 
	score as t1 inner join student as t2 on t1.student_id = t2.sid 
	inner join (4号) as t3 on t3.course_id = t1.course_id
where
	t1.num = t3.max_num
	

# 综合拼装
select 
	t2.sid,t1.course_id,t2.sname,t3.max_num
from 
	score as t1 inner join student as t2 on t1.student_id = t2.sid 
	inner join (select 
	course_id,max(num) as max_num
from 
	score
where
	course_id in (select
	cid
from 
	course
where
	teacher_id in (select
	teacher_id
from 
	course
group by
	teacher_id
having
	count(*) = (select
	count(*)
from 
	course
group by
	teacher_id
order by
	count(*) desc
limit 1)))
group by
	course_id) as t3 on t3.course_id = t1.course_id
where
	t1.num = t3.max_num


































