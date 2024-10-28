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
create table library(lid int,name varchar(40),doj DATE);
insert into library values
  (1, 'Michael Martin','2020-06-01'),
  (2, 'Heather Hall', '2019-02-01'),
  (3, 'Brian Thompson','2018-10-01'),
  (4, 'Amy Walker', '2020-05-01'),
  (5, 'Christopher Brooks','2019-08-01'),
  (6, 'Jessica Davis','2018-12-01'),
  (7, 'Matthew Lee','2020-07-01');

select * from employee e inner join canteen c  on e.eid=c.id
inner join library l on e.eid=l.lid;

