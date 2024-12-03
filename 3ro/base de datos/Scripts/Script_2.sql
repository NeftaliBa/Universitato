#vistas
create view Paises_Codigos_America as
	select Name as Pais, Code as Codigo,Continent as Continente
	from Country where Continent like "%America";
    
    select * from Paises_Codigos_America;
    select Pais from Paises_Codigos_America where Continent like "North%";