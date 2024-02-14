-- a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending) of 'temperatures' table.
SELECT `city`, AVG(`value`) AS `avr_temp`
FROM `temperatures` GROUP BY `city` ORDER BY `avr_temp` DESC;
