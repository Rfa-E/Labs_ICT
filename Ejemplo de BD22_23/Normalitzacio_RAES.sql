use proyecto_raes;
-- TAULA PAIS -----------------------------------------------------------------------------------------------------------------------------------------
drop table if exists pais;
create table pais (idcountry int auto_increment, country varchar(20), primary key (idcountry));
insert into pais
select distinct null as idcountry, country from dades_raes group by country;
-- TAULA INDUSTRIA ------------------------------------------------------------------------------------------------------------------------------------
drop table if exists industria;
create table industria (cod_indu int auto_increment, industry varchar(20), primary key(cod_indu));
insert into industria
select distinct null as cod_indu, industry from dades_raes;
-- TAULA MILIONARI ------------------------------------------------------------------------------------------------------------------------------------
drop table if exists Milionari;
create table Milionari select * from dades_raes;

alter table Milionari add column idcountry int;
alter table Milionari add column cod_indu int;
update Milionari as m1 set idcountry = (select idcountry from pais as p1 where m1.country=p1.country);
update Milionari as m2 set cod_indu = (select cod_indu from industria as i1 where m2.industry=i1.industry);
alter table milionari drop column country;
alter table milionari drop column industry;
-- MODIFICACIO DE TotalNetWorth -----------------------------------------------------------------------------------------------------------------------
update Milionari set TotalNetWorth = replace(TotalNetWorth, '$', "");
update Milionari set TotalNetWorth = replace(TotalNetWorth,'B', "");
alter table Milionari modify column TotalNetWorth double;
update Milionari set TotalNetWorth = TotalNetWorth*1000000000;
-- FOREIGN KEYS --------------------------------------------------------------------------------------------------------------------------------------
alter table milionari add foreign key (idcountry)
references pais (idcountry);
alter table milionari add foreign key (cod_indu)
references industria (cod_indu);