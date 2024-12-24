create database management;
use management;

create table recipe(
	RecipeID int primary key,
    RecipeName varchar(2550),
    Category varchar(2550),
    Ingredients varchar(2550),
    RecipeDetails varchar(2550),
    Time int not null
);

drop table chinese;

create table chinese(
	RecipeID int primary key,
    RecipeName varchar(2000),
    Category varchar(2000),
    Ingredients varchar(2000),
    RecipeDetails varchar(2000),
    Time int not null
);

create table guj(
	RecipeID int primary key,
    RecipeName varchar(2000),
    Category varchar(2000),
    Ingredients varchar(2000),
    RecipeDetails varchar(2000),
    Time int not null
);
drop table maha;
create table maha(
	RecipeID int primary key,
    RecipeName varchar(2000),
    Category varchar(2000),
    Ingredients varchar(2000),
    RecipeDetails varchar(2000),
    Time int not null
);
select * from recipe;
create table south(
	RecipeID int primary key,
    RecipeName varchar(2000),
    Category varchar(2000),
    Ingredients varchar(2000),
    RecipeDetails varchar(2000),
    Time int not null
);
drop table south;
create table north(
	RecipeID int primary key,
    RecipeName varchar(2000),
    Category varchar(2000),
    Ingredients varchar(2000),
    RecipeDetails varchar(2000),
    Time int not null
);
drop table north;
select * from recipe;


SELECT * FROM management.register;
drop table register;
CREATE TABLE register (
    fname VARCHAR(255),
    lname VARCHAR(255),
    contact VARCHAR(255),
    email VARCHAR(255) PRIMARY KEY,
    securityQ VARCHAR(255),
    securityA VARCHAR(255),
    password VARCHAR(255)
);
select * from register;


