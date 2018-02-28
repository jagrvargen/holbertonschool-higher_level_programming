-- Lists all cities contained in a database.
-- List records by cities.id cities.name states.name
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
       FROM `cities` INNER JOIN `states`
       WHERE `cities`.`state_id`=`states`.`id`;
