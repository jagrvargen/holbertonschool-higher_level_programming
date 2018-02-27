-- Lists the number of records in second_table with the same score.
-- Count records and list them next to corresponding count.
SELECT `score`, COUNT(`score`) AS "number" FROM `second_table` GROUP BY `score` DESC;
