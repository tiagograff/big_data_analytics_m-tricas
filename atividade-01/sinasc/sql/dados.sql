drop database if exists SINASC;
create database SINASC;
use SINASC;

create table dnrs2022(
	codestab   integer,
    descestab  varchar(255),
    dtnasc	   char(10),
	horanasc   char(10),
	sexo       char(10));