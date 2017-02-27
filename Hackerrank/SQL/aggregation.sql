1.
select count(id) from city where population >100000

2.
select sum(population) from city where district = 'california'

3.
select avg(population) from city where district = 'california'

4.
select floor(avg(population)) from city 

5.
select sum(population) from city where countrycode = "JPN"

6.
select max(population)-min(population) from city 

7.
select ceil(avg(salary) - avg(replace(salary, 0, '')as float)) from employees

8.
select max(months*salary) as maxSalary, count(*) from employee 
where months*salary = (select max(months*salary) from employee)

select concat(salary*months,' ', count(employee_id))
    from employee
    group by salary*months
    order by salary*months desc
    limit 1;

9.
select round(sum(lat_n), 2), round(sum(long_w),2) from station

10.
select round(sum(lat_n), 4) from station where lat_n between 38.7880 and 137.2345

11.
select round(max(lat_n),4) from station where lat_n < 137.2345

12.
select round(long_w,4) from station where lat_n < 137.2345 order by lat_n desc limit 1;

13.
select round(min(lat_n),4) from station where lat_n > 38.7780;

14.
select round(long_w,4) from station where lat_n > 38.7780 order by lat_n asc limit 1;

15.
select round( abs(max(long_w)-min(long_w)) +abs(max(lat_n)- min(lat_n)), 4) from station

16.
select round(sqrt(pow(min(lat_n)-min(long_w),2) + pow(max(lat_n)-max(long_w),2)),4)
from station;

17.
SET @R1 = 0;
SET @IND1 = (SELECT FLOOR((COUNT(*) + 1) / 2) FROM STATION);
SET @IND2 = (SELECT CEIL((COUNT(*) + 1) / 2) FROM STATION);
SELECT ROUND(AVG(LAT_N), 4)
FROM
(SELECT CASE WHEN TRUE THEN @R1:=@R1+1 END AS NROW, 
        CASE WHEN TRUE THEN @IND1 END AS LIND, 
        CASE WHEN TRUE THEN @IND2 END AS UIND, LAT_N
FROM STATION
ORDER BY LAT_N) TEMP
WHERE NROW >= LIND AND NROW <= UIND