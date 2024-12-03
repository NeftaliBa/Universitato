use world;
show databases;
show tables;
select Name,Code,Continent from Country where Continent like "%America" LIMIT 0, 50000;
select Code from Country where Continent like "%America" LIMIT 0, 50000;
select Country.Name as Pais, CountryLanguage.Language as "idioma oficial"
from Country join CountryLanguage on Country.Code = CountryLanguage.CountryCode     


where CountryLanguage.IsOfficial = 1 and Country.Continent like "%America" LIMIT 0, 50000;
select Country.Name as Pais, CountryLanguage.Language as "idioma oficial"  
from Country join CountryLanguage on Country.Code = CountryLanguage.CountryCode     
where CountryLanguage.IsOfficial = 1 and Country.Continent like "%America" LIMIT 0, 50000;

select a.Name as Pais, b.Language as "idioma oficial"  
from Country a join CountryLanguage b on a.Code = b.CountryCode     
where b.IsOfficial = 1 and a.Continent like "%America" LIMIT 0, 50000;

select a.Name as Ciudad, b.Language as "Idioma oficial"   
from City a join CountryLanguage b using(CountryCode)         
where a.CountryCode in (select code from Country where  Continent like "%America")    
	and b.IsOfficial = 1  order by 1 LIMIT 0, 50000;

select a.Name as Ciudad, b.Language as "Idioma oficial"   
	from City a join CountryLanguage b using(CountryCode)    
	join Country c on a.CountryCode = c.code          
	where c.Continent like "%America" and b.IsOfficial = 1             
	order by 1 LIMIT 0, 50000;
