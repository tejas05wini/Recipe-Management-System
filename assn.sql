create database emp;
use emp;

create table supplier(
	supp_no int primary key,
    supp_name varchar(50),
    status int,
    city varchar(50)
);

drop table supplier;

create table part(
	part_no int primary key,
    part_name varchar(50),
    color varchar(50),
    weight int,
    city varchar(50)
);

create table project(
	pro_no int primary key,
    pro_name varchar(50),
    city varchar(50)
);

create table shipment(
	supp_no int,
    part_no int,
    quantity int,
    pro_no int,
    primary key(part_no, supp_no, pro_no),
    foreign key(part_no) references part(part_no),
    foreign key(pro_no) references project(pro_no)
);

insert into supplier values(1, "Aish", 1, "Pune"),(2, "Riya", 0, "Mumbai"),(3, "Diya", 1, "Nashik"),(4, "Priya", 0, "Pune");

insert into part values(1, "Mouse", "red", 12, "Pune"),(2, "Table", "brown", 18, "Pune"),(3, "Key", "green", 14, "Mumbai"),(4, "Driver", "black", 5, "Nashik");

insert into project values(1, "ABC", "Mumbai"),(2, "XYZ", "Pune"),(3, "RYE", "Nashik"),(4, "DDR", "Pune");

insert into shipment values(1, 1, 3, 1),(2, 1 , 4, 1),(3, 2, 1, 4),(4, 3, 2, 3);


#suppliers are located at same place
select s1.supp_no, s2.supp_no
from supplier s1
join supplier s2
on s1.city = s2.city
where s1.supp_no < s2.supp_no;

select s.supp_no
from supplier s
where status > (select avg(status) from supplier);

select count(*)
from supplier;

select supp_no, avg(quantity) as avg
from shipment
group by supp_no;

delete from shipment
where quantity = (select min(quantity) from shipment where part_no = 2);

use emp;

select s1.supp_no, s2.supp_no
from supplier s1, supplier s2
where s1.city =s2.city AND s1.supp_no < s2.supp_no;

select s.supp_no 
from supplier s
where s.status > (select avg(status) from supplier);

select count(*)
from supplier;

select supp_no, avg(quantity)
from shipment
group by supp_no;

update supplier
set city="Mumbai"
where supp_no = 1; 

update shipment
set quantity = 3
where part_no = 1;

delete from project;

select color, city
from part
where city != "Chennai" and weight > 10;

select part_no, weight * 453.6
from part;

update part
set color = "black"
where part_no = 1;

select * from shipment;

update supplier
set supp_name = "Raj"
where supp_no = 1;

delete from project where city = "Chennai";

alter table shipment
add column date Date;

update shipment
set date="2024-02-02"
where part_no = 1;

alter table shipment
drop column date;

create index idx
on supplier(supp_no);

create index idx1
on supplier(supp_name);

show index from supplier;

alter table supplier
drop index idx1;

create view vw1 as
select supp_no, supp_name, status, city
from supplier
where city="Chennai" and status > 25;

INSERT INTO vw1 (supp_no, supp_name, status, city)
VALUES (5, 'New Supplier', 30, 'Gujarat');

drop view vw;

select s.supp_no, s.city, p.part_no, p.city
from supplier s
inner join part p 
where s.city = p.city;

select *
from project
left outer join shipment
on city;

select *
from project
right outer join shipment
on city;

select s.supp_no, s.supp_name, s.city, p.part_no, p.part_name
from supplier s
natural join part p;

select * 
from supplier
where part_no in (select part_no
				  from part
                  where part_no = 2);
                  
select * 
from project
natural left outer join shipment;

select *
from supplier
where supp_no in (select part_no
				  from part
                  where part_no = 2);
                  
select supp_no, sum(quantity)
from shipment
group by supp_no;

