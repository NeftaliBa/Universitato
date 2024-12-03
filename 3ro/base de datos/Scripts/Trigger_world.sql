use world;
Drop trigger if exists APopulation;

DELIMITER $$
CREATE TRIGGER APopulation
BEFORE UPDATE ON City FOR EACH ROW
BEGIN
  IF NEW.Population <> OLD.Population
    THEN
      SET NEW.Population = NEW.Population;
      UPDATE City SET Population = 500 WHERE CountryCode = "MEX";
  END IF ;
END$$
DELIMITER ;
SELECT * FROM City where CountryCode = "MEX";

drop table City;

    
