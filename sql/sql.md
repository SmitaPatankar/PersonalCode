# Theory
- DBMS is a software for creating and managing DBs
- secure
- backup mechanism
- import export mechanism
- interacts with other softwares
- for CRUD operations

# Types of DBs
- relational - tables - RDBMS: mySQL, Oracle, PostGres, Maria, MS SQL Server - SQL language
- non-relational - json, xml, graphs etc - DBMS: mongodb, dynamodb, apache cassandra, firebase - nosql: own language

# DB Features
- rows
- columns
- primary key(unique, not null) - natural/surrogate
- composite primary key - with foreign keys combo
- foreign key(s) - for 2 tables to map to each other or same table to map to itself

# SQL
- changes as per RDBMS
- keywords are not case sensitive but caps are preferred

# Types of SQL operations
- DQL
- DDL
- DCL
- DML

# Installation
- my sql server (set creds for root account)
- my sql shell

# Usage
- login to mysql cli client with credentials
- port is 3306 by default

-----

# Data Types
- int
- decimal(m,n) - total, post decimal
- varchar(l)
- blob - binary
- date - YYYY-MM-DD
- timestamp - YYYY-MM-DD HH:MM:SS

# Constraints
- not null
- unique
- default - eg: 'undecided'
- auto_increment
- primary key
- foreign key

# Additional information
- set foreign key value as null initially when the other table is not present
- Default value for text is null and numbers is 0

-----

# create db
```
create database girrafe;
```
# create table
```
create table student(
student_id int primary key,
name varchar(20),
major varchar(20)
);
```
```
create table student(
student_id int,
name varchar(20),
major varchar(20),
primary key (student_id)  # as many
);
```
```
create table student(
student_id int,
teacher_id int,
name varchar(20),
major varchar(20),
mgr_id int,
primary key (student_id),
foreign key (mgr_id) references employee (emp_id) on delete set null  # or cascade
);
```

# describe table
```
describe student;
```

# alter table - add column, delete column, add constraint
```
alter table student add gpa decimal(3,2);
```
```
alter table student drop column gpa;
```
```
alter table employee add foreign key (super_id) references employee (emp_id) on delete set null;
```

# drop table
```
drop table student;
```

# insert into table
```
insert into student values (1,'Jack','Biology');
```
```
insert into student (student_id, name) values (2,'Kate');
```
```
insert into items (id,name,cost) values
(1,2,3),
(1,2,3),
(1,2,3);
```
```
insert into items (id,name)
select * from anothertable;
```

# update into table
```
update student
set major='Bio'
where major='Biology';
```
```
update student
set major='Biochemistry'
where major='Bio' or major='chemistry';
```
```
update student
set name'Tom', major='undecided'
where student_id=1;
```
```
update student
set major='undecided';
```

# delete from table
```
delete from student;
```
```
delete from student
where student_id=5 and name='Tom';
```
```
delete t1
from mytable t1, mytable t2
where t1.columnA = t2.columnA and t1.columnB = t2.columnB and t1.rowid > t2.rowid;
```

# query from table
```
select * from student;
```
```
select name from student;
```
```
select name,major from student;
```
```
select student.name, student.major from student;
```
```
select * from student
order by name asc;  # default
```
```
select * from student
order by name desc;
```
```
select * from student
order by name, student_id;
```
```
select * from student
order by name, student_id desc;
```
```
select * from student
limit 2;
```
```
select * from student
where student_id = 5; # = < > <= >= = <> and or
```
```
select * from student
where name in ('smita', 'neha');
```
```
select first_name as fname, last_name as lname
from employee;
```
```
select distinct major
from student;
```
```
select count(emp_id)  # not null ones  # avg, sum
from employee;
```
```
select count(sex), sex
from employee
group by sex;
```
```
select count(sex), sex
from employee
group by sex
having sex='F';
```
```
select concat(city,',', state) as address from users;
```
```
select * from client
where client_name like '%LLC';  # % - any, _ one
```
```
select firsname as name from student
union
select firstname from employee;  # same no of cols  # as many statements
```
```
select employee.emp_id, employee.first_name, branch.branch_name
from employee
JOIN branch
on employee.emp_id = branch.mgr_id; # inner join, left, right, full
```
```
select *
from employee e, department d;  # cross join
```
```
select employee.first_name, employee.last_name
from employee
where employee.emp_id in(
    select works_with.emp_id
    from works_with
    where works_with.total_sales > 30000
);
```
```
select name from student
where name REGEXP 'new';
```
```
select name from student
where name REGEXP '.mita';
```
```
select name from student
where name REGEXP 'smita|neha';
```
```
select name from student
where name REGEXP '[cbn]ad';  # cad bad nad
```
```
select name from student
where name REGEXP '[^cbn]ad';  # had
```
```
select name from student
where name REGEXP '[a-c]ad';  # aad, bad, cad
```

# create trigger
```
delimeter $$
create
    trigger my_trigger before insert  # before after  # insert update delete
    on employee
    for each row begin
        insert into anothertable values ('added new employee');
    end$$
delimeter ;
```
```
DELIMITER $$
create trigger my_trigger before insert on employee
for each row begin
    insert into anothertable values (NEW.first_name);
end$$
DELIMITER ;
```
```
DELIMITER $$
create trigger my_trigger before insert on employee
for each row begin
    if NEW.sex = 'M' then
        insert into anothertable values ('adedd male employee');
    elseif new.sex = 'F' then
        insert into anothertable values ('adedd female employee');
    else
        insert into anothertable values ('added other employee');
    end if;
end$$
DELIMITER ;
```

# drop trigger
```
drop trigger my_trigger;
```

# create views   
(temporary table - not real data - data from other table - dynamic)  
```
create view myview as
select id, name, bids from items
order by bids desc
limit 10;
```
```
create view myview as
select concat(city,',', state) as address from users;
```

# query views
```
select * from myview;
```

# truncate  
(deletes all rows in one shot # cannot be rolled back)  
```
truncate table student;
```

# commit  
(otherwise changes will go away when instance is closed - o/w changes won't reflect in other instances)  
```
commit
```

# rollback  
(after commit we can't rollback)  
```
rollback
```

# create index  
(takes time but queries will be faster)  
```
create index person_first_name_idx
on person (first_name)
```
```
create index person_first_name_last_name_idx
on person (last_name, first_name)
```

# create stored procedure
```
create procedure my_procedure @gender varchar(20)
as
select * from employee where gender=@gender
go
```

# execute stored procedure
```
exec my_procedure @gender='Male'
```

# create function
```
create function my_function(@num1 as int, @num2 as int)
returns int
as
begin
return(@int1+@int2)
end
```

# execute function
```
select my_function(2,5)
```

-----

# ER diagram
- entity relationship
- entity - eg: student
- attributes - name, id
- primary key
- composite attrs
- multivalued attrs
- derived attr - eg: has_honors
- relationship between entities - total, partial
    - 1:1
    - 1:N
    - N:M
- attrs for relationship
- weak entity - dependent on another entity

# Schema
- entity and simple attrs
- map weak entity - new table with composite key
- map 1-1 relationships via foreign keys
- map 1-n relationships via foreign keys
- map n-m relations via new table with composite key and attr

# Normalization
- organize data, reduce redundancy
- dependencies should make sense
- 1 NF - no composite data like multiple phone numbers in a cell
- 2 NF - no partial dependency - eg: employee, department id but not dept location
- 3 NF - no partial dependency
- 3.5 NF/BCNF - super key is needed for functional dependencies

----

# 2nd highest emp salary
```
select max(salary) from employee where salary < (select max(salary) from employee)
```
  
(emp - ename, deptno, salary)  

# highest salary in each dept
```
select max(salary), deptno from employee group by deptno
```

# calculate no of employees in dept
```
select count(*), deptno from employee group by deptno 
```

# display 4th record
```
select * from emp where rownum <= 4
minus
select * from emp where rownum <= 3
```

# find duplicate values in column and their count
```
select count(ename) as ename_count, ename from emp group by ename
having ename_count > 1
order by ename_count
```