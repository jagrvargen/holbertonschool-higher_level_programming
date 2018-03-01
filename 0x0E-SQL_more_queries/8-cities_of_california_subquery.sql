-- Lists cities of California found in a database.
-- Access database.
USE `hbtn_0d_usa`;
-- List cities from California.
SELECT `cities`.`id`, `cities`.`name` FROM `cities`
       WHERE state_id = (SELECT states.id FROM states WHERE states.name='California')
       ORDER BY `cities`.`id` ASC;
