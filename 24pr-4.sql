create database 23june;
use 23june;
create table user(id int primary key,name varchar(40));
insert into user values(3,"vikaas");
insert into user values(4,"rohan");
create table canteen(id int,t_time TIMESTAMP,Foreign Key (id) REFERENCES user(id));
insert into canteen(id) values(2);
select * from user;
select * from canteen;