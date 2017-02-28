1.
select 
     case 
         when a+b<=c or a+c<=b or b+c<=a Then 'Not A Triangle'
         when A=B and B=C and A=C Then 'Equilateral'
         when A=B or B=C or A=C Then 'Isosceles'
         else 'Scalene'
     end
from TRIANGLES

2.
select concat(Name, '(', substring(OCCUPATION, 1, 1), ')') from OCCUPATIONS order by name;
# if use alias count(*) as num, num cant be used in order by, because of concat?
select concat('There are total ', count(*), ' ', lower(occupation), 's.') 
from occupations group by occupation order by  count(*), occupation;