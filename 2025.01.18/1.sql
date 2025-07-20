-- 1. Вывести названия стран и названия сопоставленных им столиц
SELECT country.Name AS Country, city.Name AS Capital
FROM country
JOIN city ON country.Capital = city.ID;

-- 2. Сравнить по регионам сумму населения стран и сумму населения городов
SELECT country.Region,
       SUM(country.Population) AS Total_Country_Population,
       SUM(city.Population) AS Total_City_Population
FROM country
LEFT JOIN city ON country.Code = city.CountryCode
GROUP BY country.Region;

-- 3. Вывести десять языков, на которых разговаривает больше всего людей
SELECT language.Language,
       SUM(country.Population * language.Percentage / 100) AS Speakers
FROM countrylanguage AS language
JOIN country ON language.CountryCode = country.Code
GROUP BY language.Language
ORDER BY Speakers DESC
LIMIT 10;

-- 4. Вывести названия специальностей и суммарное количество дней отпусков, в которых были врачи каждой специальности; отсортировать по возрастанию суммарного количества дней отпуска
SELECT specialty.name AS specialty,
       COALESCE(SUM(vacation.days), 0) AS total_vacation_days
FROM doctor
JOIN specialty ON doctor.specialty_id = specialty.id
LEFT JOIN vacation ON doctor.id = vacation.doctor_id
GROUP BY specialty.name
ORDER BY total_vacation_days ASC;

-- 5. Вывести округлённую до целого сумму средств, которую можно выделить на одну палату этого отделения (в зависимости от количества палат в отделении), от всех пожертвований каждому отделению; отсортировать по убыванию найденной суммы
SELECT department.name AS department,
       ROUND(SUM(donation.amount) / NULLIF(COUNT(room.id), 0)) AS funds_per_room
FROM department
JOIN room ON department.id = room.department_id
JOIN donation ON department.id = donation.department_id
GROUP BY department.name
ORDER BY funds_per_room DESC;
