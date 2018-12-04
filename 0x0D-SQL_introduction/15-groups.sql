-- lists the number of records with the same score in table
SELECT `score`, COUNT(*) number FROM second_table GROUP BY `score` HAVING number > 0 ORDER BY `score` DESC;
