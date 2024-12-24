create database stud;
use stud;

create table student(roll int, name varchar(20), class varchar(20), percent int, marks int);

insert into student values
(1,"Aish","TE",80,90),
(2,"Tejas","TE",30,50),
(3,"Vrunda","TE",70,80),
(4,"Arya","TE",65,76);

delimiter $$
create procedure proz()
begin

declare nm varchar(20);
declare pt int;
declare finish int default 0;

declare cur cursor for
select name,marks from student
where marks > 76;

declare continue handler for not found set finish = 1;

open cur;
pass : loop
fetch cur into nm, pt;
select nm, pt;
if finish = 1 then
leave pass;
end if;
end loop pass;
end;
$$

call proz();

