# Write your MySQL query statement below
WITH e2 AS (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
)
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COALESCE(e2.attended_exams, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN e2
  ON e2.student_id = s.student_id
 AND e2.subject_name = sub.subject_name
ORDER BY s.student_id, sub.subject_name;
