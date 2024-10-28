create database 21june;
use database;
create table employee(eid int,name varchar(40),salary int,doj DATE)

INSERT INTO employee(eid, name, salary, doj)
VALUES
  (1, 'John Doe', 50000, '2020-01-01'),
  (2, 'Jane Smith', 60000, '2019-06-01'),
  (3, 'Bob Johnson', 70000, '2018-03-01'),
  (4, 'Alice Brown', 40000, '2020-02-01'),
  (5, 'Mike Davis', 55000, '2019-09-01'),
  (6, 'Emily Taylor', 65000, '2018-11-01'),
  (7, 'Sarah Lee', 45000, '2020-04-01'),
  (8, 'David Kim', 58000, '2019-01-01'),
  (9, 'Lisa Nguyen', 62000, '2018-08-01'),
  (10, 'Kevin White', 52000, '2020-03-01'),
  (11, 'Rachel Patel', 68000, '2019-05-01'),
  (12, 'Michael Martin', 49000, '2020-06-01'),
  (13, 'Heather Hall', 56000, '2019-02-01'),
  (14, 'Brian Thompson', 63000, '2018-10-01'),
  (15, 'Amy Walker', 51000, '2020-05-01'),
  (16, 'Christopher Brooks', 59000, '2019-08-01'),
  (17, 'Jessica Davis', 67000, '2018-12-01'),
  (18, 'Matthew Lee', 48000, '2020-07-01'),
  (19, 'Rebecca Kim', 57000, '2019-04-01'),
  (20, 'Olivia Taylor', 64000, '2018-09-01'),
  (21, 'William Brown', 53000, '2020-08-01'),
  (22, 'Samantha Johnson', 61000, '2019-03-01'),
  (23, 'Benjamin Smith', 66000, '2018-07-01'),
  (24, 'Hannah Martin', 50000, '2020-09-01'),
  (25, 'Alexander White', 58000, '2019-10-01'),
  (26, 'Gabriella Patel', 62000, '2018-05-01'),
  (27, 'Julia Hall', 54000, '2020-10-01'),
  (28, 'Ethan Thompson', 60000, '2019-06-01'),
  (29, 'Ava Walker', 68000, '2018-01-01'),
  (30, 'Liam Brooks', 56000, '2020-11-01');

select * from employee;
select * from employee where name like'R%';
select * from employee where name like'%R';
select * from employee where name like'R%l';
select * from employee where name like'_a%';
select * from employee where name like'__n%';
INSERT INTO employee(eid, name, salary, doj)
VALUES
  (1, 'John Doe', 50000, '2020-01-01'),
  (1, 'John Doe', 50000, '2020-01-01'),
  (1, 'John Doe', 50000, '2020-01-01'),
  (2, 'Jane Smith', 60000, '2019-06-01'),
  (2, 'Jane Smith', 60000, '2019-06-01');
  select * from employee;
  select distinct * from employee;
  select  * from employee;
  create table emp(eid int,name varchar(40),salary int,doj DATE);
  insert into emp (select distinct * from employee);
  select * from emp;
  truncate table employee;
  insert into employee(select * from emp);
  select * from employee;
  select salary from employee where salary>50000 and salary <55000;
  select count(salary) from employee where salary>49000 and salary<51000;
  