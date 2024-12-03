create schema world;

use world;

create table if not exists Country (
	id int(10) not null auto_increment,
	Code varchar(3) not null,
	Name varchar(100) not null,
	Continent enum('Africa','Antarctica','Asia','Europe','North America','Oceania','South America'),
	Region varchar(100) not null,
	SurfaceArea decimal(10,1) not null,
	IndepYear int(4) null,
	Population int(10) unsigned not null,
	LifeExpectancy decimal(10,1) null,
	GNP  decimal(10,1) not null,
	GNPOld  decimal(10,1) null,
	LocalName varchar(100) not null,
	GovernmentForm varchar(100) not null,
	HeadOfState varchar(100) null,
	Capital int(4) unsigned null,
	Code2 varchar(2) not null,
	primary key(id),
	unique key (Code)
)engine=InnoDB default charset=UTF8 default collate=utf8_unicode_ci;


create table if not exists City (
	id int(10) not null auto_increment,
	Name varchar(100) not null,
	CountryCode varchar(3) not null,
	District varchar(100) null,
	Population int(10) unsigned not null,
	primary key (id),
	index fk_CountryCode_idx (CountryCode ASC),
	constraint fk_CountryCode_city 
		foreign key (CountryCode)
		references Country (Code)
		on delete RESTRICT
		on update CASCADE
)engine=InnoDB default charset=UTF8 default collate=utf8_unicode_ci;

CREATE TABLE IF NOT EXISTS CountryLanguage (
	id int(10) not null auto_increment,
	CountryCode varchar(3) not null,
	Language varchar(100) not null,
	IsOfficial boolean not null default 0,
	Percentage decimal(4,1) not null,
	primary key (id),
	index fk_CountryCode_idx (CountryCode ASC),
	constraint fk_CountryCode_cl 
		foreign key (CountryCode)
		references Country (Code)
		on delete RESTRICT
		on update CASCADE
)engine=InnoDB default charset=UTF8 default collate=utf8_unicode_ci;
