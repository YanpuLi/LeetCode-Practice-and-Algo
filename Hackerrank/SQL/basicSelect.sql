1.Revising the Select Query I
select * from CITY where POPULATION > 100000 and COUNTRYCODE = 'USA'

2.Revising the Select Query II
select name from CITY where population > 120000 and countrycode = 'USA'

3.Select All
select * from CITY

4.Select By ID
select * from city where id = 1661

5.Japanese Cities' Attributes
select * from city where countrycode = 'JPN'

6.Japanese Cities' Names
select name from city where countrycode = "JPN"

7.Weather Observation Station 1 
select city, state from station

8.Weather Observation Station 3
select distinct city from station where (id %2) = 0

9.Weather Observation Station 4 
select count(city) - count(distinct city) from station 

10.Weather Observation Station 5 
select city, length(city)  from station order by length(city) asc, city limit 1;
select city, length(city)  from station order by length(city) desc, city limit 1;

11.Weather Observation Station 6
select city from station where city regexp '^[aeiouAEIOU]';

12.Weather Observation Station 7
select distinct city from station where city regexp '[aeiouAEIOU]$';

13.Weather Observation Station 8 
select distinct city from station where city regexp '^[aeiouAEIOU].*[aeiouAEIOU]$';

14.Weather Observation Station 9
select distinct city from station where city regexp '^[^aeiouAEIOU]';

15.
select distinct city from station where city regexp '[^aeiouAEIOU]$'

16.
SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP "^[^aeiou].*" or CITY REGEXP ".*[^aeiou]$"
ORDER BY CITY;

17.
SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP "^[^aeiou].*[^aeiou]$"
ORDER BY CITY;

18.Higher Than 75 Marks 
select Name from students where marks >75 order by substring(name, length(name)-2, 3), ID;

19.Employee Names
select name from employee order by name asc;

20.
select name from employee where salary >2000 and months <10 order by employee_id asc;

