-- Create a new table with unique id.
-- Create the table unique_id with default value 1. id must be unique.
CREATE TABLE IF NOT EXISTS unique_id(`id` INT DEFAULT 1 UNIQUE,
       `name` VARCHAR(256));
