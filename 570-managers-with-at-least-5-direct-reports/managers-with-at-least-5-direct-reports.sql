# Write your MySQL query statement below
with s1 as (select e.name,e.managerId,count(e.managerId) as counter from Employee e
group by managerId)

select e.name from s1
join Employee e
on s1.managerId=e.id 
where s1.counter>=5