create database 25june;
use 25june;
create table employee(eid int,name varchar(40),salary int);
INSERT INTO employee(eid, name, salary)
VALUES
  (1, 'John', 50000),
  (2, 'vikas ', 60000),
  (3, 'Bob Johnson', 70000 ),
  (4, 'sumit', 40000),
  (5, 'Mike Davis', 55000)

create table canteen(id int,name varchar(40));
insert into canteen values(1,"sumit"),
 (2,"vivek"),
 (3,"vikas");
 select * from employee e inner join canteen c 
 on e.eid=c.id;
 select * from employee e left join canteen c on e.eid=c.id;
 select * from employee e right join canteen c on e.eid=c.id;