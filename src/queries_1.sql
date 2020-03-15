use world;

select * from results;

select count(*) from results;
select * from drivers;

select raceId, count(*) from results group by raceId;

create table results_updated as select r1.*, r2.forename, r3.name from results r1, drivers r2, races r3  where r1.driverId = r2.driverId and r1.raceId = r3.raceId;

select * from results_updated;

#wins for lewis hamilton
select forename, count(*) as wins from results_updated where forename = "Lewis" and positionOrder = "1";

select * from races;

select r1.resultId, r1.raceId, r2.forename,r2.driverId,r1.positionText,r3.name from results r1, drivers r2, races r3 where r1.raceId = r3.raceId and r1.driverId = r2.driverId group by r2.forename;
