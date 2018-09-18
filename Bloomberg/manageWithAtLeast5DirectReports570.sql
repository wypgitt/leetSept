# 570. Managers with at Least 5 Direct Reports
'

The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
Given the Employee table, write a SQL query that finds out managers with at least 5 direct report. For the above table, your SQL query should return:

+-------+
| Name  |
+-------+
| John  |
+-------+
Note:
No one would report to himself.
'
# Write your MySQL query statement below

Select e1.Name from Employee e1 JOIN Employee e2 on e1.Id = e2.ManagerId GROUP BY e2.ManagerId 
HAVING COUNT(*) >=5;

select Name from Employee as e1 join (select ManagerId from Employee GROUP BY ManagerId having count(ManagerId) >=5) as e2 on e1.Id = e2.ManagerId;
