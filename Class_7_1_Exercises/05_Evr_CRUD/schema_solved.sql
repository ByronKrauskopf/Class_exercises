-- Drop table if exists
DROP TABLE firepower;

-- Create new table to import data
CREATE TABLE firepower (
	country VARCHAR,
	ISO3 VARCHAR,
	rank INT,
	TotalPopulation INT,
	ManpowerAvailable INT,
	TotalMilitaryPersonnel INT,
	ActivePersonnel INT,
	ReservePersonnel INT,
	TotalAircraftStrength INT,
	FighterAircraft INT,
	AttackAircraft INT,
	TotalHelicopterStrength INT,
	AttackHelicopters INT
);

-- Import data from firepower.csv
-- View the table to ensure all data has been imported correctly
SELECT * FROM firepower;

--Add 'id' as the Primary Key 
ALTER TABLE firepower
ADD COLUMN id SERIAL PRIMARY KEY;

--Find the rows that have a `ReservePersonnel` of 0 and delete these rows from the dataset.
DELETE FROM firepower
WHERE ReservePersonnel = 0;

--Every country in the world at least deserves one `FighterAircraft`—it only seems fair. Let's add one to each nation that has none.
UPDATE firepower
SET FighterAircraft = 1
WHERE FighterAircraft = 0;

--Oh no! By updating this column, the values within `TotalAircraftStrength` column are now off for those nations! 


--Find the [Averages](https://www.w3schools.com/sql/sql_count_avg_sum.asp) 
--for `TotalMilitaryPersonnel`, `TotalAircraftStrength`, `TotalHelicopterStrength`, and `TotalPopulation`, 
--and rename the columns with their designated average.
--We need to [add 1](https://stackoverflow.com/a/2680352) to the original number.
SELECT AVG(TotalMilitaryPersonnel) AS AvgTotMilPersonnel,
    AVG(TotalAircraftStrength) AS AvgTotAircraftStrength,
    AVG(TotalHelicopterStrength) AS AvgTotHelicopterStrength,
    AVG(TotalPopulation) AS AvgTotPopulation
FROM firepower