# Write your MySQL query statement below
with s2 as (select student_id, subject_name, count(subject_name) as attended_exams 
from Examinations group by student_id,subject_name),

s1 as (select st.student_id, st.student_name, su.subject_name 
from Students st
cross join Subjects su)

select s1.student_id, s1.student_name, s1.subject_name, ifnull(s2.attended_exams,0) as attended_exams
from s1
left join s2
on s1.student_id=s2.student_id and s1.subject_name=s2.subject_name
order by s1.student_id, s1.subject_name 
