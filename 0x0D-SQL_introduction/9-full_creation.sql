-- Creates the table second_table with 4 rows.
-- Create second_table and with id, name, and score columns.
CREATE TABLE IF NOT EXISTS `second_table`(`id` INT NULL, `name` VARCHAR(256)\
       NULL, `score` INT NULL);
-- Add John to second_table
INSERT INTO `second_table`(`id`, `name`, `score`) VALUES (1, "John", 10);
-- Add Alex to second_table
INSERT INTO `second_table`(`id`, `name`, `score`) VALUES (2, "Alex", 3);
-- Add Bob to second_table
INSERT INTO `second_table`(`id`, `name`, `score`) VALUES (3, "Bob", 14);
-- Add Alex to second_table
INSERT INTO `second_table`(`id`, `name`, `score`) VALUES (4, "George", 8);
