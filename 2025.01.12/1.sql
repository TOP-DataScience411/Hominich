-- Запросы к таблице doctors:
-- 1. Вывести средний оклад (salary) всех сотрудников
SELECT AVG(salary) AS average_salary FROM doctors;

-- 2. Вывести среднюю премию для всех сотрудников, чей доход выше среднего(взять явное значение из результата предыдущего запроса)
SELECT AVG(bonus) AS average_bonus
FROM doctors
WHERE salary > 55641.74;

-- Запросы к таблице vacations:
-- 3. Вывести с сортировкой по возрастанию среднее количество дней в отпуске для каждого сотрудника
SELECT doctor_id, AVG(end_date - start_date) AS avg_vacation_days
FROM vacations
GROUP BY doctor_id
ORDER BY avg_vacation_days ASC;

-- 4. Вывести для каждого сотрудника самый ранний год отпуска и самый поздний год отпуска с сортировкой по возрастанию разности между этими двумя значениями
SELECT doctor_id,
       MIN(EXTRACT(YEAR FROM start_date)) AS earliest_year,
       MAX(EXTRACT(YEAR FROM end_date)) AS latest_year,
       (MAX(EXTRACT(YEAR FROM end_date)) - MIN(EXTRACT(YEAR FROM start_date))) AS year_difference
FROM vacations
GROUP BY doctor_id
ORDER BY year_difference ASC;

-- Запросы к таблице donations:
-- 5. Вывести сумму пожертвований за всё время для каждого отделения с сортировкой по возрастанию номеров отделений
SELECT dep_id, SUM(amount) AS total_donations
FROM donations
GROUP BY dep_id
ORDER BY dep_id ASC;

-- 6. Вывести сумму пожертвований за каждый год для каждого спонсора с сортировкой по возрастанию номеров спонсоров и годов
SELECT sponsor_id, EXTRACT(YEAR FROM date) AS donation_year, SUM(amount) AS total_donations
FROM donations
GROUP BY sponsor_id, donation_year
ORDER BY sponsor_id ASC, donation_year ASC;
