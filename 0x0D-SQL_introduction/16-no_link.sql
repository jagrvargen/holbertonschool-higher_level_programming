-- Lists all records in second_table that have a name value by score and name
-- in descending order
-- Select by score and name, check name for NULL, and sort.
SELECT `score`, `name` FROM second_table WHERE `name` IS NOT NULL ORDER BY\
        `score` DESC;
