-- Lists all records with a score >= 10 in second_table.
-- Select and list score and name in descending order.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY\
        `score` DESC;
