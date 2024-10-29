use 26june;
select * from employee;
alter table employee RENAME user;
select * from user;
alter table user change name user varchar(40);

select * from user;

select * from user
where user='John' ORDER BY salary desc limit 1;
