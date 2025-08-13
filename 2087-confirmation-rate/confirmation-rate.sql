# Write your MySQL query statement below
# Write your MySQL query statement below
with s1 as (select user_id, count(*) as counter1 from Confirmations
group by user_id),

s2 as(select user_id, count(*) as counter2 from Confirmations
where action='confirmed'
group by user_id)

select s.user_id, round(ifnull(s2.counter2/s1.counter1,0),2) as confirmation_rate from Signups s
left join s1 on s.user_id=s1.user_id left join s2 on s.user_id=s2.user_id