use world;
select a.Name, a.Population,b.Population
	from City a join Country b on a.CountryCode = b.Code
    where b.Code = "MEX"
    order by 2;
    update City set Population = Population + 1 where id = "5290";