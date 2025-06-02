-- Rank;Name;Total Net Worth;$ Last Change;$ YTD Change;Country;Industry;;;;
drop database if exists proyecto_raes;
create database proyecto_raes;
use proyecto_raes;

create table Dades_raes
(rango int not null, nombre varchar(40) not null, TotalNetWorth varchar(10) not null, Lastchange varchar(10) not null, YTDChange varchar(10) not null,
country varchar(20) not null, industry varchar(20) not null, valor_null char null, primary key(rango, nombre));

load data infile 'C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\500 richest people 2021.csv'
into table Dades_raes
fields terminated by ';'
optionally enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
(Rango,Nombre,TotalNetWorth,LastChange,YTDChange,Country,Industry, valor_null, valor_null, valor_null);

alter table Dades_raes drop column valor_null;

