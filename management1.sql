create database management;
use management;

create table recipe(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

create table chinese(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

create table guj(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

create table maha(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

create table south(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

create table north(
	RecipeID int primary key,
    RecipeName varchar(20),
    Category varchar(20),
    Ingredients varchar(50),
    RecipeDetails varchar(50),
    Time int not null
);

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


