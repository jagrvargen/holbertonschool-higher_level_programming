-- Lists cities of California found in a database.
-- Access database.
USE `hbtn_0d_usa`;
-- List cities from California.
SELECT `cities`.`id`, `cities`.`name` FROM `cities`
       WHERE cities.state_id=1
       ORDER BY `cities`.`id` ASC;
