create database clg;
use clg;

create table stud(
	roll int primary key,
    name varchar(50),
    mks int
);

create table grading(
	roll int primary key,
    grade varchar(50)
);

delimiter $$
create procedure proc(in roll int, in name varchar(50), in mks int)
begin
declare grade varchar(50);
if mks <= 1500 and mks >= 990 then
set grade = "Distinction";
elseif mks <= 99 and mks >= 900 then
set grade = "First Class";
end if;
insert into stud values(roll, name, mks);
insert into grading values(roll, grade);
end $$

call proc(1, "Aradhya", 1423);
$$

call proc(2, "Anda", 789);
$$

select * from stud;
select * from grading;






