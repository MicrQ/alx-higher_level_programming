-- a script that lists all records of the table second_table, (score, name) desc. NULL name won't be displayed.
SELECT `score`, `name` 
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
