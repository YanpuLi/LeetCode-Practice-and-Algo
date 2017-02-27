1.
select sum(City.population) from City inner join Country on City.CountryCode = Country.Code where Country.Continent = 'Asia';

2.
select City.name from City inner join Country on City.CountryCode = Country.Code where Country.Continent = 'Africa';

3.
select country.continent, floor(avg(city.population)) from City inner join Country on City.CountryCode = Country.Code
group by country.continent;

4.
SELECT
    CASE WHEN Grade >= 8
        THEN Name
        ELSE NULL
    END,
    Grade, Marks
FROM Students
LEFT JOIN Grades
    ON Grades.Min_Mark <= Students.Marks AND Students.Marks <= Grades.Max_Mark
ORDER BY Grade DESC, Name, Marks;

5.
#straight forware inner join of all tables
select hackers.hacker_id, hackers.name from submissions inner join Challenges
on submissions.challenge_id =Challenges.challenge_id inner join Difficulty
on Difficulty.difficulty_level = Challenges.difficulty_level inner join Hackers on submissions.hacker_id = Hackers.hacker_id
where Difficulty.score = submissions.score group by hackers.hacker_id having count(hackers.hacker_id) >1
order by count(Submissions.hacker_id) desc, hackers.hacker_id asc

#no inner join, use sub-select clause
select hacker_id, name from
(
	select h.hacker_id, h.name, count(s.challenge_id) as num
	from hackers as h, submissions as s, Difficulty as d, Challenges as c
	where h.hacker_id = s.hacker_id and s.challenge_id = c.challenge_id and c.difficulty_level = d.difficulty_level
	and s.score = d.score group by h.hacker_id
) as A where num >1
order by num desc, hacker_id asc;

##must rename the subselect as a new table

6.
select A.id, wands_property.age, A.coins_needed, A.power
from wands A inner join
	(select code, power, min(coins_needed) coins_needed
		from wands group by code, power) B
on (A.code=B.code and A.power=B.power and A.coins_needed=B.coins_needed)
inner join wands_property on (A.code=wands_property.code and wands_property.is_evil<>1)
order by A.power desc, wands_property.age desc;

7.
select h.hacker_id, h.name, count(1) as total
from hackers as h, challenges
where h.hacker_id = challenges.hacker_id
group by hacker_id
having total = (
    select count(*) from challenges
    group by hacker_id
    order by count(*) desc limit 1
) or total not in (
    select t.cnt from (
        select count(*) as cnt from challenges
        group by hacker_id
    ) as t
    group by t.cnt
    having count(t.cnt) > 1
)
order by total desc, hacker_id

select h.hacker_id, h.name, count(1) as total
from hackers as h
join challenges using (hacker_id)
group by hacker_id
having total = (
    select count(*) from challenges
    group by hacker_id
    order by count(*) desc limit 1
) or total not in (
    select t.cnt from (
        select count(*) as cnt from challenges
        group by hacker_id
    ) as t
    group by t.cnt
    having count(t.cnt) > 1
)
order by total desc, hacker_id

7.
select h.hacker_id, h.name,  sum(a.max_score) as total
from
(select s.hacker_id, challenge_id, max(score) as max_score
from Submissions s
where score > 0
group by s.hacker_id, s.challenge_id) as a
inner join Hackers h on a.hacker_id = h.hacker_id
group by h.hacker_id
order by total desc, h.hacker_id
