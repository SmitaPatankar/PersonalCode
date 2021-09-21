# steps
- download sql server exe
- install sql server exe
- download sql server management studio
- install sql server management studio
- open mgmt studio and connect to server
- download sample db
- save in c-> program files->ms sql server ->mssql->backup->paste db
- restore db from file
- has schema.table -> columns -> pk constraint, fk constraint, datatype, other constraints
- create new query

# commands
```
SELECT @@SERVERNAME;

SELECT @@VERSION;

USE MyDB;

select * from myschema.mytable;

select mycolumn1, myclolum2 from myschema.mytable;

select distinct mycolumn1 from myschema.mytable;

select *
from schema.table
where jobtitle = 'xx';
-- > >= < <=

select a, b, a+b as asumb
from schema.table
-- - * /
-- + works for concatenating strings
-- + ' '

where x+y > 500
-- not temp col name
-- from -> where -> select

where middlename is null;
-- is not null

where cond1 and cond2;
-- or

where job in ('x', 'y');

where job between 1 and 50;

where name like 'a%'; 0 or more at end
-- %o - 0 or more at start
-- am____ # 4 other characters

order by city;  # asc
-- desc
-- a asc, b desc

select a, sum(b) as bb
from xx.xx
grouby a;
-- avg, count, max, min 

concat(a,' ', b,' ', c)
-- null ignored

len(a)

left(name, 2) as initials

right(name,2)

substring(name, 3,4)  # start, length
-- starts from 1

d = 2011-05-31 00:00:00.00
day(d)
-- month, year

select current_timestamp;

group by xx
having price > 1000
-- for aggregate functions

select pid, eid from p
where pid in (
select pid from e where pid > 5
)
-- = for single result from inner query

query
union
query
union
query
-- similar data type
-- union all

select t1.common, t1.a, t2.b
from table1 t1 inner join table2 t2
on t1.common = t2.common
-- left (left outer) join, right(right outer), full

bit - 0 or 1 or null - 1 byte
smallint - 2 bytes
int - 4 bytes
int identity(S,I) - 4 bytes
money - 8 bytes
float(precision) - 4 or 8 bytes
char(n) - fixed upto 800 characters
varchar(n) - var value - 2 bytes + num of characters
nchar(n) - 2n - encoded
nvarchar(n) - 2n + 2 bytes - encoded
datetime - 8 bytes
date - 3 bytes
timestamp
uniqueidentifier - guid - 16 bytes

create database mydb;

create table tablename
(
    name char(5) unique,
    surname char(10) not null    
    id int primary key
)
-- dbo schema
-- unique has one null, it can be used multiple times

(
...,
constraint xx primary key(a,b),
constraint yy foreign key(i) references othertable(col)
);

insert into schema.tablename
values (1,2,3,4,5);

insert into schema.tablename
(colnames)
values (1,2,3,4,5);

-- dont use auto increment field

insert into schema.tablename
(colnames)
values (1,2,3,4,5)
values (1,2,3,4,5)
values (1,2,3,4,5);

update xx
set name = 5, surname=7
where id=6;

alter table xx
add mycol char(12);

alter table xx
alter column mycol varchar(20);

alter table xx
drop column mycol, mycol;

delete from table
where country=xx;

delete from table;

delete top (2) from table;
delete top (10) percent from table;

drop table xx;
```