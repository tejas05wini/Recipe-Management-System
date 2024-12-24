create database lib;
use lib;

create table library(b_no int, b_name varchar(50), author varchar(50), allowed_days int);

insert into library values
(1, "Wings of Fire", "Abdul Kalam", 30),
(2, "Ikigai", "Moshe", 28),
(3, "Twisted Love", "Ana Huang", 30),
(4, "Bhagavad Gita", "Krishna", 30);

update library set allowed_days = 30 where b_no = 2;

create table audit(b_no int, old_days int, new_days int);

select * from library;
select * from audit;


delimiter $$

create trigger t1
before update
on library
for each row
begin
insert into audit values(NEW.b_no, OLD.allowed_days, NEW.allowed_days);
end;
$$

update library set allowed_days = 50 where b_no = 2;
$$
select * from audit;