create database a6;
use a6;

create table borrower(
	roll int primary key,
    name varchar(50),
    dissue date,
    bookname varchar(50),
    status varchar(50)
);

create table fine(
	roll int primary key,
    Date date,
    amt int,
    foreign key(roll) references borrower(roll)
);

insert into borrower values
(1, "Aish", "2024-03-03", "Wings of fire", "borrowed"),
(2, "Ak", "2024-02-01", "We dream of space", "returned"),
(3, "Ghani", "2024-09-08", "Ikigai", "borrowed"),
(4, "Dos", "2024-05-04", "Fault in our Stars", "returned");

insert into fine values
(1, "2024-05-03", 1500),
(2, "2024-04-01", 2100),
(3, "2024-10-08", 1600),
(4, "2024-07-04", 2500);

delimiter $$
create procedure d(in roll_new int, nm varchar(50))
begin
declare x int;
declare continue handler for not found
begin
select "not found";
end;

select datediff(curdate(), dissue) into x from borrower
where roll = roll_new;

if(x > 15 and x < 30) 
then
insert into fine values(roll_new, curdate(), (x*5));
end if;

if(x > 30)
then 
insert into fine values(roll_new, curdate(), (x*50));
end if;

update borrower
set status="returned"
where roll = roll_new;
end ;
$$

call d(4, "Dhumrasur");
$$
select * from borrower;
$$
select * from fine;
$$





